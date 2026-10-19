// Alternate exact check using the generalized Petersen P(10,3) graph.
// Compile: c++ -O2 -std=c++17 verify_petersen.cpp -o verify_petersen
// Execute: ./verify_petersen
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using Mask=uint32_t;
constexpr int N=20;
constexpr Mask FULL=(Mask(1)<<N)-1;
std::array<Mask,N> adj{};
std::array<Mask,N> closed{};
int bits(Mask x){return __builtin_popcount(x);}
void edge(int x,int y){adj[x] |= Mask(1)<<y;adj[y] |= Mask(1)<<x;}
void setup(){
 for(int i=0;i<10;i++){
  edge(i,(i+1)%10);
  edge(i,i+10);
  edge(i+10,10+(i+3)%10);
 }
 for(int i=0;i<N;i++){assert(bits(adj[i])==3);closed[i]=adj[i]|(Mask(1)<<i);}
}
bool dominates(Mask S){
 Mask covered=0;
 for(Mask z=S;z;z&=z-1){int v=__builtin_ctz(z);covered|=closed[v];}
 return covered==FULL;
}
bool secure(Mask S){
 if(!dominates(S))return false;
 for(int attack=0;attack<N;attack++)if(!(S&(Mask(1)<<attack))){
  bool defended=false;
  Mask guard_choices=adj[attack]&S;
  for(Mask z=guard_choices;z;z&=z-1){
   int defender=__builtin_ctz(z);
   if(dominates((S&~(Mask(1)<<defender))|(Mask(1)<<attack))){defended=true;break;}
  }
  if(!defended)return false;
 }
 return true;
}
int main(){
 setup();
 std::array<unsigned,N+1> count{};std::vector<Mask> opt;
 for(Mask s=0;s<=FULL;s++){
  if(bits(s)>8)continue;
  if(secure(s)){
   ++count[bits(s)];if(bits(s)==8)opt.push_back(s);
  }
 }
 for(int k=0;k<8;k++)assert(count[k]==0);
 assert(count[8]==155);
 std::map<Mask,int> index;
 for(int i=0;i<(int)opt.size();i++)index[opt[i]]=i;
 int jumping=0,twoexchange=0;
 std::vector<std::vector<int>> E(opt.size());
 for(int i=0;i<(int)opt.size();i++)for(int j=i+1;j<(int)opt.size();j++){
  int d=bits(opt[i]^opt[j]);
  if(d==2)jumping++;
  if(d==4){twoexchange++;E[i].push_back(j);E[j].push_back(i);}
 }
 assert(jumping==0 && twoexchange==750);
 std::map<int,int> degrees;
 for(auto &x:E)degrees[x.size()]++;
 assert((degrees==std::map<int,int>({{6,30},{10,120},{24,5}})));
 for(int i=0;i<(int)opt.size();i++){
  std::vector<int> dist(opt.size(),-1);dist[i]=0;std::queue<int> Q;Q.push(i);int far=0;
  while(!Q.empty()){
   int v=Q.front();Q.pop();
   for(int w:E[v])if(dist[w]==-1){dist[w]=dist[v]+1;far=std::max(far,dist[w]);Q.push(w);}
  }
  assert(std::count_if(dist.begin(),dist.end(),[](int d){return d>=0;})==155);
  assert(far==4);
 }
 // Explicit isomorphism: vertices of GP(10,3) to lexicographically
 // ordered 2-subsets (first 10) and 3-subsets (last 10) of five points.
 std::array<int,N> iso={0,10,4,16,7,19,9,15,3,12,11,1,17,5,13,8,18,2,14,6};
 std::vector<std::array<int,5>> sets;
 for(int k=2;k<=3;k++)for(int a=0;a<5;a++)for(int b=a+1;b<5;b++){
  if(k==2)sets.push_back({a,b,-1,-1,-1});
  else for(int c=b+1;c<5;c++)sets.push_back({a,b,c,-1,-1});
 }
 assert(sets.size()==20);
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  bool subset=false;
  int x=iso[i],y=iso[j];
  if((x<10)!=(y<10)){
   auto const &a=sets[x<10?x:y],&b=sets[x<10?y:x];
   subset=(a[0]==b[0]||a[0]==b[1]||a[0]==b[2])&&(a[1]==b[0]||a[1]==b[1]||a[1]==b[2]);
  }
  assert((bool)(adj[i]&(Mask(1)<<j))==subset);
 }
 std::set<Mask> mapped;
 for(Mask S:opt){Mask T=0;for(int v=0;v<N;v++)if(S&(Mask(1)<<v))T|=Mask(1)<<iso[v];mapped.insert(T);}
 assert(mapped.size()==155);
 std::cout<<"vertex_count=20; degree=3; secure_domination_number=8\n";
 std::cout<<"secure_counts_0_to_8=";
 for(int k=0;k<=8;k++){if(k)std::cout<<',';std::cout<<count[k];}
 std::cout<<"\nminimum_sets=155; single_exchanges=0; two_exchanges=750\n";
 std::cout<<"minimum_two_exchange_degrees=6:30,10:120,24:5\n";
 std::cout<<"two_exchange_connected=1; radius=4; diameter=4\n";
 std::cout<<"mapped_H5_masks=";
 bool first=true;for(Mask s:mapped){if(!first)std::cout<<',';first=false;std::cout<<s;}
 std::cout<<'\n';
}
