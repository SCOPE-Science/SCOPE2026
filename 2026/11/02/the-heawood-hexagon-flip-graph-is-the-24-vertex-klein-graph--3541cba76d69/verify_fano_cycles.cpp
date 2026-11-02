// Independent exact check: GF(2)^3 incidence and explicit alternating hexagons.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
  bool hit[7][7] = {};
  vector<vector<int>> nbr(14);
  for (int p=0;p<7;p++) for(int l=0;l<7;l++) {
    int v=(p+1)&(l+1), parity=__builtin_popcount((unsigned)v)%2;
    if (!parity) {hit[p][l]=1; nbr[p].push_back(7+l);nbr[7+l].push_back(p);}
  }
  for(auto const& n:nbr) assert(n.size()==3);
  vector<array<int,7>> ms;
  array<int,7> m{};
  auto rec=[&](auto&& self,int p,int used)->void {
    if(p==7){ms.push_back(m);return;}
    for(int l=0;l<7;l++) if(hit[p][l] && !(used>>l&1)){
      m[p]=l;self(self,p+1,used|(1<<l));
    }
  };
  rec(rec,0,0); assert(ms.size()==24);
  map<array<int,7>,int> idx;
  for(int i=0;i<24;i++)idx[ms[i]]=i;
  set<vector<int>> cycles;
  vector<int> path;
  auto walk=[&](auto&& self,int s,int v)->void {
    if(path.size()==6){
      if(find(nbr[v].begin(),nbr[v].end(),s)==nbr[v].end())return;
      vector<int> es;
      for(int i=0;i<6;i++) {
        int a=path[i],b=path[(i+1)%6];
        int p=a<7?a:b; int l=a>=7?a-7:b-7;
        assert(hit[p][l]);es.push_back(7*p+l);
      }
      sort(es.begin(),es.end());cycles.insert(es);return;
    }
    for(int w:nbr[v]) if(find(path.begin(),path.end(),w)==path.end()){
      path.push_back(w);self(self,s,w);path.pop_back();
    }
  };
  for(int s=0;s<14;s++){path={s};walk(walk,s,s);}
  assert(cycles.size()==28);
  vector<set<int>> adj(24);
  for(int i=0;i<24;i++)for(auto const& c:cycles){
    vector<int> old;
    for(int e:c) if(ms[i][e/7]==e%7)old.push_back(e);
    if(old.size()!=3)continue;
    auto next=ms[i];
    for(int e:c)if(ms[i][e/7]!=e%7)next[e/7]=e%7;
    auto it=idx.find(next);assert(it!=idx.end());
    int j=it->second;assert(j!=i);adj[i].insert(j);
  }
  int E=0; for(int i=0;i<24;i++){
    assert(adj[i].size()==7);E+=(int)adj[i].size();
    for(int j:adj[i])assert(adj[j].count(i));
  }
  assert(E==168);
  vector<vector<int>> dist(24,vector<int>(24,-1));
  for(int root=0;root<24;root++){
    queue<int> q;dist[root][root]=0;q.push(root);
    while(!q.empty()){
      int x=q.front();q.pop();
      for(int y:adj[x])if(dist[root][y]<0){dist[root][y]=dist[root][x]+1;q.push(y);}
    }
    array<int,4> ct{};
    for(int x=0;x<24;x++){assert(dist[root][x]>=0 && dist[root][x]<=3);ct[dist[root][x]]++;}
    assert((ct==array<int,4>{1,7,14,2}));
  }
  const int b[4]={7,4,1,0},c[4]={0,1,2,7};
  for(int root=0;root<24;root++)for(int x=0;x<24;x++) {
    int d=dist[root][x],below=0,above=0;
    for(int y:adj[x]) {if(dist[root][y]==d-1)below++;if(dist[root][y]==d+1)above++;}
    assert(below==c[d] && above==b[d]);
  }
  int fibers=0; set<int> seen;
  for(int i=0;i<24;i++)if(!seen.count(i)){
    vector<int> f{i};for(int j=0;j<24;j++)if(dist[i][j]==3)f.push_back(j);
    assert(f.size()==3);
    for(int a:f)for(int d:f)if(a!=d)assert(dist[a][d]==3);
    for(int a:f)seen.insert(a);
    fibers++;
  }
  assert(fibers==8 && seen.size()==24);
  cout<<"FANO_CYCLE_PASS matchings="<<ms.size()<<" hexagons="<<cycles.size()
      <<" exchanges="<<E/2<<" array=[7,4,1;1,2,7] antipodal="<<fibers<<"\n";
}
