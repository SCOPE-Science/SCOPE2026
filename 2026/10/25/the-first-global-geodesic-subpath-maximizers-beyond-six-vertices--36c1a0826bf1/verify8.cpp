// Exact eight-vertex extremal census from the complete <=7-vertex Graph Atlas.
// Needs atlas7_masks.txt: all 1044 seven-vertex graph representatives, one
// 21-bit edge mask per line, with bits in lexicographic edge-pair order.
// Enumerates every possible eighth-vertex neighbourhood (2^7 choices).
// Graph Atlas: Read & Wilson, An Atlas of Graphs (1998); NetworkX 3.6.1 data.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using U = uint32_t;
constexpr int N=8, E=28;
array<pair<int,int>,E> edge_pairs;
int eindex[N][N];

void prepare(){
 int k=0;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){
  eindex[u][v]=eindex[v][u]=k;edge_pairs[k++]={u,v};
 }
 assert(k==E);
}
U mask_from_pairs(const vector<pair<int,int>>& edges){
 U mask=0;
 for(auto [u,v]:edges){assert(0<=u && u<N && 0<=v && v<N && u!=v);mask|=U(1)<<eindex[u][v];}
 return mask;
}
U graph_from_seven(U old,int new_links){
 U result=0;
 int k=0;
 for(int u=0;u<7;u++)for(int v=u+1;v<7;v++,k++)if((old>>k)&1)result|=U(1)<<eindex[u][v];
 for(int u=0;u<7;u++)if((new_links>>u)&1)result|=U(1)<<eindex[u][7];
 return result;
}
int gpn(U mask){
 U nb[N]={};
 for(int k=0;k<E;k++)if((mask>>k)&1){
  auto [u,v]=edge_pairs[k];nb[u]|=U(1)<<v;nb[v]|=U(1)<<u;
 }
 int total=N;
 for(int root=0;root<N;root++){
  int dist[N],ways[N]={},queue[N];
  fill(dist,dist+N,-1);dist[root]=0;ways[root]=1;
  int head=0,tail=0;queue[tail++]=root;
  while(head<tail){
   int u=queue[head++];U neighbours=nb[u];
   while(neighbours){int v=__builtin_ctz(neighbours);neighbours&=neighbours-1;
    if(dist[v]<0){dist[v]=dist[u]+1;ways[v]=ways[u];queue[tail++]=v;}
    else if(dist[v]==dist[u]+1)ways[v]+=ways[u];
   }
  }
  if(tail!=N)return -1;
  for(int v=root+1;v<N;v++)total+=ways[v];
 }
 return total;
}
U permute(U edges,const array<int,N>& p){
 U out=0;
 for(int e=0;e<E;e++)if((edges>>e)&1){
  auto [u,v]=edge_pairs[e];out|=U(1)<<eindex[p[u]][p[v]];
 }
 return out;
}
set<U> graph_orbit(U mask){
 set<U> result;
 array<int,N> p={0,1,2,3,4,5,6,7};
 do {result.insert(permute(mask,p));} while(next_permutation(p.begin(),p.end()));
 return result;
}
int main(int argc,char**argv){
 prepare();
 const string name = argc>1 ? argv[1] : "atlas7_masks.txt";
 ifstream input(name);
 vector<U> bases;U x;
 while(input>>x)bases.push_back(x);
 if(bases.size()!=1044 || set<U>(bases.begin(),bases.end()).size()!=1044){
  cerr<<"Expected exactly 1044 distinct representatives\n";return 1;
 }
 // Balanced K_4,4 and the two candidate extremal classes.
 vector<pair<int,int>> biclique;
 for(int a=0;a<4;a++)for(int b=4;b<8;b++)biclique.push_back({a,b});
 U complete=mask_from_pairs(biclique);
 U one=complete&~(U(1)<<eindex[0][4]);
 U two=one&~(U(1)<<eindex[1][5]);
 cout<<"balanced_biclique_gpn="<<gpn(complete)<<"\n";
 cout<<"one_deleted_matching_edge_gpn="<<gpn(one)<<"\n";
 cout<<"two_deleted_matching_edges_gpn="<<gpn(two)<<"\n";
 if(gpn(complete)!=72||gpn(one)!=74||gpn(two)!=74)return 2;
 uint64_t total=0,connected=0;
 int maximum=-1;
 map<int,vector<U>> maximizers;
 for(U base:bases)for(int sub=0;sub<128;sub++){
  U graph=graph_from_seven(base,sub);
  total++;
  int value=gpn(graph);
  if(value<0)continue;
  connected++;
  if(value>maximum){maximum=value;maximizers.clear();}
  if(value==maximum)maximizers[__builtin_popcount(graph)].push_back(graph);
 }
 cout<<"base_isomorphism_classes="<<bases.size()<<"\n";
 cout<<"eight_vertex_candidates="<<total<<"\n";
 cout<<"connected_candidates="<<connected<<"\n";
 cout<<"maximum="<<maximum<<"\n";
 int nmax=0;
 for(auto& [edges,graphs]:maximizers){
  cout<<"max_candidates_with_"<<edges<<"_edges="<<graphs.size()<<"\n";
  nmax+=graphs.size();
 }
 cout<<"all_max_candidates="<<nmax<<"\n";
 const auto orbit1=graph_orbit(one),orbit2=graph_orbit(two);
 cout<<"orbit_one_removed="<<orbit1.size()<<"\n";
 cout<<"orbit_two_removed="<<orbit2.size()<<"\n";
 if(total!=133632||connected!=119980||maximum!=74||
    maximizers.size()!=2||maximizers[14].size()!=4||maximizers[15].size()!=5)return 3;
 for(auto [edges,graphs]:maximizers){
  for(U graph:graphs){
   if((edges==15 && !orbit1.count(graph))||(edges==14 && !orbit2.count(graph))){
    cerr<<"Unexpected eight-vertex maximizing graph\n";return 4;
   }
  }
 }
 cout<<"exhaustive_classification=PASS\n";
 return 0;
}
