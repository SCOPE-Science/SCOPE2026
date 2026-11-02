// Independent exhaustive certificate: sequential forcing, LCF/GP presentations.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
using U = uint32_t;
using Graph = vector<U>;

void edge(Graph& g,int a,int b) { assert(a!=b); g[a]|=U(1)<<b;g[b]|=U(1)<<a; }
Graph pappus_lcf() {
  Graph g(18,0); const int steps[]={5,7,-7,7,-7,-5};
  for(int i=0;i<18;++i){ edge(g,i,(i+1)%18);int j=(i+steps[i%6]+18)%18;edge(g,i,j);}
  return g;
}
Graph desargues_gp() {
  Graph g(20,0);
  for(int i=0;i<10;++i) {
    edge(g,i,(i+1)%10);edge(g,i,10+i);edge(g,10+i,10+(i+3)%10);
  }
  return g;
}
Graph pappus_incidence(){
  Graph g(18,0);const int t[][3]={{0,1,2},{3,4,5},{6,7,8},{0,4,6},{3,1,6},{0,5,7},{3,2,7},{1,5,8},{4,2,8}};
  for(int j=0;j<9;++j)for(int i=0;i<3;++i)edge(g,t[j][i],9+j);
  return g;
}
Graph desargues_cover(){
  Graph g(20,0);vector<pair<int,int>> v;
  for(int i=0;i<5;++i)for(int j=i+1;j<5;++j)v.push_back({i,j});
  for(int i=0;i<10;++i)for(int j=0;j<10;++j)
   if(v[i].first!=v[j].first && v[i].first!=v[j].second && v[i].second!=v[j].first && v[i].second!=v[j].second)
     edge(g,i,10+j);
  return g;
}
void check_isomorphism(const Graph& source,const Graph& target,const vector<int>& f){
  assert(source.size()==target.size()&&source.size()==f.size());
  auto v=f;sort(v.begin(),v.end());for(int i=0;i<(int)v.size();++i)assert(v[i]==i);
  for(int i=0;i<(int)f.size();++i)for(int j=0;j<(int)f.size();++j)
   assert(bool(source[i]&(U(1)<<j))==bool(target[f[i]]&(U(1)<<f[j])));
}
bool forces(const Graph& g,U chosen){
  const U all=(U(1)<<g.size())-1;
  while(chosen!=all){
    bool progress=false;
    for(int v=0;v<(int)g.size();++v)if(chosen&(U(1)<<v)){
      U white=g[v]&~chosen;
      if(white && !(white&(white-1))){chosen|=white;progress=true;break;}
    }
    if(!progress)return false;
  }
  return true;
}
vector<U> find_minima(const Graph& g,int expected_k){
  vector<U> bases;int n=g.size();
  for(U m=0;m<(U(1)<<n);++m){
    int k=__builtin_popcount(m);
    if(k>expected_k)continue;
    bool ok=forces(g,m);
    if(k<expected_k)assert(!ok);
    if(k==expected_k&&ok)bases.push_back(m);
  }
  return bases;
}
vector<vector<int>> slide_graph(const Graph& g,const vector<U>& bases){
  unordered_map<U,int> locate;
  for(int i=0;i<(int)bases.size();++i)locate[bases[i]]=i;
  vector<vector<int>> neigh(bases.size());
  for(int i=0;i<(int)bases.size();++i){
    U m=bases[i];
    for(int a=0;a<(int)g.size();++a) if(m&(U(1)<<a)) {
      for(int b=0;b<(int)g.size();++b)if(g[a]&(U(1)<<b)){
        if(m&(U(1)<<b))continue;
        auto it=locate.find(m^(U(1)<<a)^(U(1)<<b));
        if(it!=locate.end())neigh[i].push_back(it->second);
      }
    }
  }
  return neigh;
}
vector<vector<int>> jump_graph_by_pairs(const vector<U>& bases){
  vector<vector<int>> g(bases.size());
  for(int i=0;i<(int)bases.size();++i)for(int j=i+1;j<(int)bases.size();++j){
    if(__builtin_popcount(bases[i]^bases[j])==2){g[i].push_back(j);g[j].push_back(i);}
  }
  return g;
}
map<int,int> component_sizes(const vector<vector<int>>& g){
  vector<bool> seen(g.size());map<int,int> hist;
  for(int s=0;s<(int)g.size();++s)if(!seen[s]){
    int count=0;queue<int> q;q.push(s);seen[s]=true;
    while(!q.empty()){
      int v=q.front();q.pop();++count;
      for(int w:g[v])if(!seen[w]){seen[w]=true;q.push(w);}
    }
    ++hist[count];
  }
  return hist;
}
map<int,int> eccentricity_histogram(const vector<vector<int>>& g){
  int n=g.size();map<int,int> hist;
  for(int s=0;s<n;++s){
    vector<int> dist(n,-1);dist[s]=0;
    vector<int> queue(n);queue[0]=s;int head=0,tail=1;
    while(head<tail){int v=queue[head++];for(int w:g[v])if(dist[w]==-1){dist[w]=dist[v]+1;queue[tail++]=w;}}
    assert(tail==n);int d=*max_element(dist.begin(),dist.end());++hist[d];
  }
  return hist;
}
int edge_count(const vector<vector<int>>& g){
  long long d=0;for(auto &n:g)d+=n.size();assert(!(d&1));return d/2;
}
int main(){
  Graph P=pappus_lcf(),D=desargues_gp();
  const vector<int> pmap={0,9,2,17,4,12,6,13,1,16,8,11,7,15,3,10,5,14};
  const vector<int> dmap={0,17,6,11,9,10,7,16,1,19,18,3,12,5,14,8,13,2,15,4};
  check_isomorphism(P,pappus_incidence(),pmap);
  check_isomorphism(D,desargues_cover(),dmap);
  for(auto&g:{P,D}){for(U m:g)assert(__builtin_popcount(m)==3);}
  cout<<"GRAPH_PRESENTATIONS_OK"<<endl;
  auto bp=find_minima(P,7),bd=find_minima(D,8);
  assert(bp.size()==6912&&bd.size()==13520);
  cout<<"MINIMUM_CERTIFICATE_OK Pappus 7:6912 Desargues 8:13520"<<endl;
  auto ps=slide_graph(P,bp),ds=slide_graph(D,bd);
  assert(edge_count(ps)==10962&&edge_count(ds)==0);
  assert((component_sizes(ps)==map<int,int>{{6912,1}}));
  assert((component_sizes(ds)==map<int,int>{{1,13520}}));
  map<int,int> degree;
  for(auto&row:ps)++degree[row.size()];
  assert(degree==(map<int,int>{{2,1080},{3,3564},{4,2268}}));
  cout<<"SLIDE_CERTIFICATE_OK Pappus 10962:1 Desargues 0:13520"<<endl;
  auto hist=eccentricity_histogram(ps);
  assert(hist==(map<int,int>{{16,648},{17,4968},{18,1296}}));
  cout<<"METRIC_CERTIFICATE_OK Pappus radius=16 diameter=18"<<endl;
  auto dtj=jump_graph_by_pairs(bd);
  assert((edge_count(dtj)==178560&&component_sizes(dtj)==map<int,int>{{13520,1}}));
  cout<<"JUMP_CERTIFICATE_OK Desargues edges=178560 connected=1"<<endl;
  cout<<"INDEPENDENT_CERTIFICATE_OK"<<endl;
}
