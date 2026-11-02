// Fully exhaustive finite certificate using folded five-cube quotient and sequential forcing.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
constexpr int n=16, ALL=(1<<n)-1;
int canonical(int x){return min(x,x^31);}
int main(){
 array<array<int,5>,n> adj{};
 for(int u=0;u<n;u++)for(int j=0;j<5;j++)adj[u][j]=canonical(u^(1<<j));
 auto is_force=[&](int input){
  int black=input;
  while(true){
   bool progress=false;
   for(int u=0;u<n && !progress;u++)if(black&(1<<u)){
    int w=0, last=-1;
    for(int v:adj[u])if(!(black&(1<<v))){w++;last=v;}
    if(w==1){black|=1<<last;progress=true;}
   }
   if(!progress)return black==ALL;
  }
 };
 int smaller=0; vector<int> states;
 for(int x=0;x<=ALL;x++){
  int k=__builtin_popcount((unsigned)x);
  if(k==9 && is_force(x))smaller++;
  if(k==10 && is_force(x))states.push_back(x);
 }
 assert(smaller==0 && states.size()==3872);
 vector<int> index(1<<n,-1);
 for(int i=0;i<(int)states.size();i++)index[states[i]]=i;
 vector<vector<int>> G(states.size());
 map<int,long long> degree, eccentricity, distances, detours;
 for(int i=0;i<(int)states.size();i++){
  int x=states[i];
  for(int a=0;a<n;a++)if(x&(1<<a))for(int b=0;b<n;b++)if(!(x&(1<<b))){
   int j=index[x^(1<<a)^(1<<b)];
   if(j>=0)G[i].push_back(j);
  }
  degree[G[i].size()]++;
 }
 assert((degree==map<int,long long>{{30,672},{32,960},{34,1440},{37,800}}));
 for(int start=0;start<(int)states.size();start++){
  vector<int> di(states.size(),-1);
  queue<int> q;q.push(start);di[start]=0;
  int far=0,reached=0;
  while(!q.empty()){
   int u=q.front();q.pop();reached++;
   far=max(far,di[u]);
   for(int v:G[u])if(di[v]<0){di[v]=di[u]+1;q.push(v);}
  }
  assert(reached==(int)states.size());
  eccentricity[far]++;
  for(int j=start+1;j<(int)states.size();j++){
   int d=di[j], h=__builtin_popcount((unsigned)(states[start]^states[j]))/2;
   distances[d]++;detours[d-h]++;
   assert(d==h || (d==h+1 && h==2 && d==3));
  }
 }
 assert((eccentricity==map<int,long long>{{6,3872}}));
 assert((distances==map<int,long long>{{1,64720},{2,625440},{3,2214640},{4,2986160},{5,1412976},{6,190320}}));
 assert((detours==map<int,long long>{{0,7494016},{1,240}}));
 cout<<"ALL_SOURCE_FOLDED_CUBE_EXHAUSTIVE_PASS\n";
 cout<<"states=3872 edges=64720 radius=6 diameter=6\n";
 cout<<"pairs=";for(auto [k,v]:distances)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"excess=";for(auto [k,v]:detours)cout<<" "<<k<<":"<<v;cout<<"\n";
}
