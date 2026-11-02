#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

// Independently enumerate shortest-path edge triples in clique-path Cartesian graphs.
struct Checker {
  int m, L, ne;
  vector<pair<int,int>> edges;
  vector<vector<pair<int,int>>> adj;
  uint64_t forbidden[64][64]{};
  uint64_t expected[64]{};
  int64_t solutions = 0;
  int64_t inspected = 0;
  bool unexpected = false;
  int target;
  Checker(int mm, int LL):m(mm),L(LL),ne(0),adj(m*L) {
    auto edge=[&](int u,int v){int id=edges.size();edges.emplace_back(u,v);adj[u].emplace_back(v,id);adj[v].emplace_back(u,id);};
    for(int i=0;i<L;i++)for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)edge(i*m+a,i*m+b);
    for(int i=0;i<L-1;i++)for(int a=0;a<m;a++)edge(i*m+a,(i+1)*m+a);
    ne=edges.size(); if(ne>63)throw runtime_error("too many edges");
    target=L*m*(m-1)/2+m;
    for(int cut=0;cut<L-1;cut++) {
      uint64_t bits=0;
      for(int e=0;e<ne;e++) {
        int u=edges[e].first,v=edges[e].second;
        if(u/m==v/m || (u/m==cut && v/m==cut+1))bits|=uint64_t(1)<<e;
      }
      expected[cut]=bits;
      if(__builtin_popcountll(bits)!=target)throw runtime_error("bad construction");
    }
  }
  void pathTriples(const vector<int>& p) {
    for(size_t i=0;i<p.size();i++)for(size_t j=i+1;j<p.size();j++)for(size_t k=j+1;k<p.size();k++) {
      int a=p[i],b=p[j],c=p[k];
      forbidden[a][b]|=uint64_t(1)<<c; forbidden[b][a]|=uint64_t(1)<<c;
      forbidden[a][c]|=uint64_t(1)<<b; forbidden[c][a]|=uint64_t(1)<<b;
      forbidden[b][c]|=uint64_t(1)<<a; forbidden[c][b]|=uint64_t(1)<<a;
    }
  }
  void dfsPath(int u,int t,const vector<int>& d,vector<int>&path) {
    if(u==t){pathTriples(path);return;}
    for(auto [v,k]:adj[u])if(d[v]==d[u]-1) {
      path.push_back(k);dfsPath(v,t,d,path);path.pop_back();
    }
  }
  void build() {
    for(int t=0;t<m*L;t++) {
      vector<int>d(m*L,-1);queue<int>q;d[t]=0;q.push(t);
      while(!q.empty()) {int u=q.front();q.pop();for(auto [v,e]:adj[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}}
      for(int s=0;s<t;s++) {vector<int>p;dfsPath(s,t,d,p);}
    }
  }
  bool canAdd(uint64_t mask,int k) {
    for(uint64_t a=mask;a;a&=a-1) {
      int j=__builtin_ctzll(a);
      if(forbidden[k][j] & mask)return false;
    }
    return true;
  }
  void search(int next,uint64_t mask,int count) {
    if(count==target) {
      ++solutions;
      bool recognized=false;
      for(int cut=0;cut<L-1;cut++)if(mask==expected[cut])recognized=true;
      if(!recognized)unexpected=true;
      return;
    }
    if(next>=ne || count+ne-next<target)return;
    ++inspected;
    if(canAdd(mask,next))search(next+1,mask|(uint64_t(1)<<next),count+1);
    search(next+1,mask,count);
  }
  void run() {
    build();
    for(int i=0;i<L-1;i++){
      uint64_t mask=expected[i];
      for(int k=0;k<ne;k++)if(mask>>k&1) {
        if(!canAdd(mask^(uint64_t(1)<<k),k)) throw runtime_error("construction fails");
      }
      for(int k=0;k<ne;k++)if(!(mask>>k&1)) {
        if(canAdd(mask,k)) throw runtime_error("expected configuration is extendible");
      }
    }
    search(0,0,0);
    if(unexpected||solutions!=L-1)throw runtime_error("counterexample to optimizer classification");
    cout<<"m="<<m<<" L="<<L<<" E="<<ne<<" target="<<target
      <<" solutions="<<solutions<<" search_nodes="<<inspected<<" OK\n";
  }
};
int main(){
  try{
    for(int m=2;m<=4;m++)for(int L=2;L<=(m==4?3:5);L++)Checker(m,L).run();
    cout<<"VERIFY_OK\n";
  }catch(const exception &e){cerr<<"VERIFY_FAIL: "<<e.what()<<"\n";return 1;}
}
