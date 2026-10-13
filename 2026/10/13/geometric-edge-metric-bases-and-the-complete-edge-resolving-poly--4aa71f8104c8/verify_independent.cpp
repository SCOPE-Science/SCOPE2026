// Independent breadth-first shortest-path enumeration of vertex-to-edge signatures.
// Compile: g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
  const int N=18;
  vector<pair<int,int>> E;vector<int> adj[N];
  for(int x=0;x<3;++x)for(int y=0;y<3;++y)
    for(int a=0;a<3;++a)for(int b=0;b<3;++b)
      if((y-a*x-b+9)%3==0){int u=3*x+y,v=9+3*a+b;E.push_back({u,v});adj[u].push_back(v);adj[v].push_back(u);}
  assert(E.size()==27);
  int dist[N][N];
  for(int s=0;s<N;++s){
    fill(dist[s],dist[s]+N,-1);queue<int> Q;Q.push(s);dist[s][s]=0;
    while(!Q.empty()){
      int u=Q.front();Q.pop();
      for(int w:adj[u])if(dist[s][w]<0){dist[s][w]=dist[s][u]+1;Q.push(w);}
    }
  }
  int signature[N][27];
  for(int v=0;v<N;++v)for(int j=0;j<(int)E.size();++j)
    signature[v][j]=min(dist[v][E[j].first],dist[v][E[j].second]);
  long long count[N+1]={},metric_count[N+1]={};
  for(int mask=0;mask<(1<<N);++mask){
    bool good=true,mgood=true;
    for(int e=0;e<27&&good;++e)for(int f=0;f<e;++f){
      bool diff=false;
      for(int v=0;v<N;++v)if(((mask>>v)&1)&&signature[v][e]!=signature[v][f]){diff=true;break;}
      if(!diff){good=false;break;}
    }
    for(int v=0;v<N&&mgood;++v)for(int w=0;w<v;++w){
      bool diff=false;
      for(int s=0;s<N;++s)if(((mask>>s)&1)&&dist[s][v]!=dist[s][w]){diff=true;break;}
      if(!diff){mgood=false;break;}
    }
    int k=__builtin_popcount((unsigned)mask);
    if(good)++count[k];
    if(mgood)++metric_count[k];
    assert(!mgood||good);
  }
  long long expected[]={0,0,0,0,540,5976,17106,31392,43704,48620,43758,31824,18564,8568,3060,816,153,18,1};
  for(int k=0;k<=N;++k)assert(count[k]==expected[k]);
  assert(metric_count[4]==216);
  long long total=0,vertex=0;
  for(int k=0;k<=N;++k){total+=count[k];vertex+=metric_count[k];}
  assert(total==254100&&vertex==243834);
  cout<<"VERIFY_CPP_OK all_262144_masks edge_bases=540 metric_bases=216 edge_resolving=254100 vertex_resolving=243834\\n";
  cout<<"VERIFY_CPP_OK polynomial=";
  for(int k=4;k<=N;++k)cout<<k<<":"<<count[k]<<(k==N?'\n':',');
  return 0;
}
