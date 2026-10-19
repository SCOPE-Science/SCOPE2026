// Exact finite enumeration of metric bases and their one-vertex exchange graph.
// Standard C++17. Build: g++ -std=c++17 -O3 check_direct.cpp -o check_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <numeric>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int n=20, V=40;
using U=uint64_t;
int main(){
 array<vector<int>,V>g;
 auto add=[&](int a,int b){g[a].push_back(b);g[b].push_back(a);};
 for(int i=0;i<n;i++){add(i,(i+1)%n);add(i,n+i);add(n+i,n+(i+3)%n);}
 for(auto &v:g){sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());assert(v.size()==3);}
 int d[V][V];
 for(int s=0;s<V;s++){
  fill(d[s],d[s]+V,-1);d[s][s]=0;queue<int>q;q.push(s);
  while(!q.empty()){
   int u=q.front();q.pop();for(int v:g[u])if(d[s][v]==-1){d[s][v]=d[s][u]+1;q.push(v);}
  }
  for(int t=0;t<V;t++)assert(d[s][t]>=0&&d[s][t]<16);
 }
 vector<U>bases;
 long long trials4=0,trials5=0;
 // An ordered distance vector separates all vertices exactly when its 40 codes are distinct.
 auto resolving=[&](const array<int,5>& s,int k)->bool{
  array<uint32_t,V>code{};
  for(int v=0;v<V;v++)for(int i=0;i<k;i++)code[v]|=uint32_t(d[v][s[i]])<<(4*i);
  sort(code.begin(),code.end());
  for(int i=1;i<V;i++)if(code[i]==code[i-1])return false;
  return true;
 };
 for(int a=0;a<V;a++)for(int b=a+1;b<V;b++)for(int c=b+1;c<V;c++)for(int e=c+1;e<V;e++){
  array<int,5>s={a,b,c,e,0};trials4++;
  if(resolving(s,4)){cerr<<"a resolving 4-set exists\n";return 1;}
 }
 for(int a=0;a<V;a++)for(int b=a+1;b<V;b++)for(int c=b+1;c<V;c++)for(int e=c+1;e<V;e++)for(int f=e+1;f<V;f++){
  array<int,5>s={a,b,c,e,f};trials5++;
  if(resolving(s,5))bases.push_back((U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<e)|(U(1)<<f));
 }
 const int N=bases.size();assert(trials4==91390 && trials5==658008);
 unordered_map<U,int>lookup;lookup.reserve(2*N);
 for(int i=0;i<N;i++){assert(lookup.emplace(bases[i],i).second);}
 vector<vector<int>>adj(N);long long sumdeg=0;map<int,int>degrees,outer_profile;
 for(int i=0;i<N;i++){
  U s=bases[i];outer_profile[__builtin_popcountll(s&((U(1)<<n)-1))]++;
  for(int a=0;a<V;a++)if((s>>a)&1)for(int b=0;b<V;b++)if(!((s>>b)&1)){
   auto it=lookup.find(s^(U(1)<<a)^(U(1)<<b));
   if(it!=lookup.end())adj[i].push_back(it->second);
  }
  sort(adj[i].begin(),adj[i].end());
  assert(unique(adj[i].begin(),adj[i].end())==adj[i].end());
  sumdeg+=adj[i].size();degrees[adj[i].size()]++;
 }
 for(int i=0;i<N;i++)for(int j:adj[i])assert(binary_search(adj[j].begin(),adj[j].end(),i));
 // Rotations and simultaneous reflections on both 20-cycles preserve all distances.
 vector<char>seen(N,0);vector<pair<int,int>>reps;
 map<int,int>orbit_sizes;
 for(int i=0;i<N;i++)if(!seen[i]){
  set<int>orb;
  for(int sign: {1,-1})for(int shift=0;shift<n;shift++){
   U t=0,s=bases[i];
   for(int j=0;j<V;j++)if((s>>j)&1){int x=(sign*(j%n)+shift+2*n)%n;t|=U(1)<<(x+n*(j/n));}
   auto it=lookup.find(t);assert(it!=lookup.end());orb.insert(it->second);
  }
  for(int j:orb)seen[j]=1;
  reps.push_back({i,(int)orb.size()});orbit_sizes[orb.size()]++;
 }
 assert(accumulate(seen.begin(),seen.end(),0)==N);
 vector<int>dist(N),fifo(N);int radius=N,diameter=0;
 map<int,int>ecc_count;map<pair<int,int>,int>ecc_outer;map<pair<int,int>,int>ecc_orbits;
 for(auto[root,multiplicity]:reps){
  fill(dist.begin(),dist.end(),-1);dist[root]=0;int head=0,tail=0;fifo[tail++]=root;
  int ecc=0;
  while(head<tail){int u=fifo[head++];ecc=max(ecc,dist[u]);for(int v:adj[u])if(dist[v]==-1){dist[v]=dist[u]+1;fifo[tail++]=v;}}
  assert(tail==N);
  radius=min(radius,ecc);diameter=max(diameter,ecc);
  ecc_count[ecc]+=multiplicity;ecc_orbits[{ecc,multiplicity}]++;
  ecc_outer[{ecc,__builtin_popcountll(bases[root]&((U(1)<<n)-1))}]+=multiplicity;
 }
 assert(N==41040 && sumdeg/2==670930 && sumdeg%2==0);
 assert(reps.size()==1032&&orbit_sizes[20]==12&&orbit_sizes[40]==1020);
 assert(radius==6&&diameter==7&&ecc_count[6]==40180&&ecc_count[7]==860);
 cout<<"metric_dimension=5\n";
 cout<<"four_set_candidates="<<trials4<<" five_set_candidates="<<trials5<<"\n";
 cout<<"bases="<<N<<" exchange_edges="<<sumdeg/2<<"\n";
 cout<<"outer_profile=";for(auto[k,v]:outer_profile)cout<<k<<":"<<v<<" ";cout<<"\n";
 cout<<"degree_min="<<degrees.begin()->first<<" degree_max="<<degrees.rbegin()->first<<"\n";
 cout<<"dihedral_orbits="<<reps.size()<<" size20="<<orbit_sizes[20]<<" size40="<<orbit_sizes[40]<<"\n";
 cout<<"connected=yes radius="<<radius<<" diameter="<<diameter<<"\n";
 cout<<"eccentricities=";for(auto[k,v]:ecc_count)cout<<k<<":"<<v<<" ";cout<<"\n";
 cout<<"eccentricity_by_orbit_size=";for(auto[k,v]:ecc_orbits)cout<<"("<<k.first<<","<<k.second<<"):"<<v<<" ";cout<<"\n";
 cout<<"eccentricity_by_outer_count=";for(auto[k,v]:ecc_outer)cout<<"("<<k.first<<","<<k.second<<"):"<<v<<" ";cout<<"\n";
 cout<<"VERIFY_OK\n";
}
