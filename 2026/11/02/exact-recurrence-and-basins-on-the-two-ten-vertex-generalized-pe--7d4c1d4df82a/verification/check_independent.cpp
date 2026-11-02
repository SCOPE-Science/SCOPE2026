// Exhaustive independent functional-graph verification of ternary excitation on GP(5,k).
// No Python dependencies, and no use of precomputed transition certificates.
#include <array>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <algorithm>
#include <iostream>
using namespace std;
constexpr int n=10, N=59049;
constexpr int POW3[10]={1,3,9,27,81,243,729,2187,6561,19683};
array<array<int,3>,n> make_graph(int k) {
  array<vector<int>,n> nbr;
  auto edge=[&](int u,int v){assert(u!=v); nbr[u].push_back(v);nbr[v].push_back(u);};
  for(int i=0;i<5;i++){
    edge(i,(i+1)%5);
    edge(5+i,5+(i+k)%5);
    edge(i,5+i);
  }
  array<array<int,3>,n> graph;
  for(int i=0;i<10;i++){
    sort(nbr[i].begin(),nbr[i].end());
    assert(nbr[i].size()==3 && adjacent_find(nbr[i].begin(),nbr[i].end())==nbr[i].end());
    copy(nbr[i].begin(),nbr[i].end(),graph[i].begin());
  }
  return graph;
}
int advance(int s,const array<array<int,3>,n>&g){
  int d[n];
  for(int i=0;i<n;i++)d[i]=s/POW3[i]%3;
  int z=0;
  for(int i=0;i<n;i++){
    int b;
    if(d[i]==1) b=2;
    else if(d[i]==2) b=0;
    else b=(d[g[i][0]]==1 || d[g[i][1]]==1 || d[g[i][2]]==1)?1:0;
    z+=POW3[i]*b;
  }
  assert(z>=0&&z<N);
  return z;
}
int main(){
 for(int k=1;k<=2;k++){
  auto graph=make_graph(k);
  vector<int> f(N);
  for(int s=0;s<N;s++)f[s]=advance(s,graph);
  vector<int> color(N,0),position(N,-1),dist(N,-1),period(N,0);
  map<int,int> orbit_counts;
  for(int seed=0;seed<N;seed++){
   if(color[seed])continue;
   vector<int> path;
   int v=seed;
   while(color[v]==0){
    color[v]=1;position[v]=(int)path.size();path.push_back(v);v=f[v];
   }
   if(color[v]==1){
     assert(position[v]>=0 && position[v]<(int)path.size());
     int start=position[v],p=(int)path.size()-start;
     orbit_counts[p]++;
     for(int t=start;t<(int)path.size();t++){
       int x=path[t];dist[x]=0;period[x]=p;
     }
     for(int t=start-1;t>=0;t--){
       int x=path[t];dist[x]=1+dist[f[x]];period[x]=period[f[x]];
     }
   } else{
     assert(color[v]==2 && dist[v]>=0);
     for(int t=(int)path.size()-1;t>=0;t--){
       int x=path[t];dist[x]=1+dist[f[x]];period[x]=period[f[x]];
     }
   }
   for(int x:path){color[x]=2;position[x]=-1;}
  }
  map<int,int> basins;map<pair<int,int>,int> table;
  int maximum=0;
  for(int s=0;s<N;s++){
   assert(color[s]==2 && period[s]>0 && dist[s]>=0);
   basins[period[s]]++;table[{dist[s],period[s]}]++;maximum=max(maximum,dist[s]);
   if(dist[s]>0){assert(dist[f[s]]==dist[s]-1);assert(period[f[s]]==period[s]);}
  }
  cout<<"GP(5,"<<k<<")\nORBIT";
  for(auto [p,count]:orbit_counts)cout<<" "<<p<<":"<<count;
  cout<<"\nBASIN";
  for(auto [p,count]:basins)cout<<" "<<p<<":"<<count;
  cout<<"\nMAX_ENTRY "<<maximum<<"\nENTRIES";
  for(auto [t,count]:table)cout<<" "<<t.first<<","<<t.second<<":"<<count;
  cout<<"\n";
 }
}
