// Reproducible exhaustive seven-vertex simple-graph census; C++17 standard library only.
// Counts the number of unordered geodesics, including seven zero-length paths.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using U = uint32_t;
constexpr int N=7, E=21;
array<pair<int,int>,E> pairs7;
int edge_index[N][N];

void initialize_pairs(){
 int p=0;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){
   pairs7[p]={u,v};edge_index[u][v]=edge_index[v][u]=p;p++;
 }
 assert(p==E);
}
U encode(const vector<pair<int,int>>& edges){
 U mask=0;
 for(auto [u,v]:edges){assert(u>=0 && u<N && v>=0 && v<N && u!=v);mask|=(U(1)<<edge_index[u][v]);}
 return mask;
}
U permuted(U mask,const array<int,N>& perm){
 U out=0;
 for(int i=0;i<E;i++)if((mask>>i)&1){
  auto [u,v]=pairs7[i];out|=(U(1)<<edge_index[perm[u]][perm[v]]);
 }
 return out;
}
set<U> orbit(U rep){
 set<U> answer;
 array<int,N> p={0,1,2,3,4,5,6};
 do{answer.insert(permuted(rep,p));}while(next_permutation(p.begin(),p.end()));
 return answer;
}
int gpn(U mask){
 U neighbour[N]={};
 for(int k=0;k<E;k++)if((mask>>k)&1){
  auto [u,v]=pairs7[k]; neighbour[u]|=U(1)<<v;neighbour[v]|=U(1)<<u;
 }
 int total=N;
 for(int root=0;root<N;root++){
  int dist[N];int paths[N]={};int queue[N];
  fill(dist,dist+N,-1);
  dist[root]=0;paths[root]=1;int head=0,tail=0;queue[tail++]=root;
  while(head<tail){
   int u=queue[head++];U nbr=neighbour[u];
   while(nbr){int v=__builtin_ctz(nbr);nbr&=nbr-1;
    if(dist[v]<0){dist[v]=dist[u]+1;paths[v]=paths[u];queue[tail++]=v;}
    else if(dist[v]==dist[u]+1){paths[v]+=paths[u];}
   }
  }
  if(tail!=N)return -1;
  for(int v=root+1;v<N;v++)total+=paths[v];
 }
 return total;
}
int main(){
 initialize_pairs();
 const vector<pair<int,int>> edgesA={{0,1},{0,3},{0,4},{1,2},{1,5},{2,3},{2,4},{3,5},{3,6},{4,5},{4,6}};
 const vector<pair<int,int>> edgesB={{0,1},{0,2},{0,4},{0,5},{1,3},{1,6},{2,3},{2,6},{3,4},{3,5},{4,6},{5,6}};
 U A=encode(edgesA),B=encode(edgesB);
 cout << "representative_A="<<gpn(A)<<" edges="<<__builtin_popcount(A)<<"\n";
 cout << "representative_B="<<gpn(B)<<" edges="<<__builtin_popcount(B)<<"\n";
 if(gpn(A)!=49||gpn(B)!=49)return 1;
 map<int,uint64_t> counts;
 map<int,set<U>> maxmasks;
 uint64_t connected=0;int maximum=-1;
 for(U m=0;m<(U(1)<<E);m++){
  int k=gpn(m);
  if(k<0)continue;
  ++connected;counts[k]++;
  if(k>maximum){maximum=k;maxmasks.clear();}
  if(k==maximum)maxmasks[__builtin_popcount(m)].insert(m);
 }
 cout << "all_labelled_graphs=" << (U(1)<<E) << "\n";
 cout << "connected_labelled_graphs=" << connected << "\n";
 cout << "max_gpn="<<maximum<<"\n";
 uint64_t nmax=0;
 for(auto& [e,S]:maxmasks){cout<<"max_edge_count_"<<e<<"="<<S.size()<<"\n";nmax+=S.size();}
 cout << "max_labelled_total="<<nmax<<"\n";
 for(auto [label,rep]:vector<pair<char,U>>{{'A',A},{'B',B}}){
  auto S=orbit(rep);
  cout<<"orbit_"<<label<<"="<<S.size()<<"\n";
  if(S!=maxmasks[__builtin_popcount(rep)]){
    cerr<<"orbit mismatch for "<<label<<"\n";return 2;
  }
 }
 if(connected!=1866256 || maximum!=49 || maxmasks.size()!=2 ||maxmasks.at(11).size()!=420|| maxmasks.at(12).size()!=35){
  cerr <<"Unexpected enumeration tally\n"; return 3;
 }
 cout<<"classification=PASS\n";
 return 0;
}
