#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

struct Grid {
 int n,N;
 vector<uint64_t> nbr;
 vector<pair<int,int>> edges;
 explicit Grid(int width):n(width),N(3*width),nbr(N,0) {
  for(int c=0;c<n;c++)for(int r=0;r<3;r++){
   int v=3*c+r;
   if(c+1<n) add(v,v+3);
   if(r+1<3) add(v,v+1);
  }
 }
 void add(int a,int b){nbr[a]|=1ULL<<b;nbr[b]|=1ULL<<a;edges.emplace_back(a,b);}
 bool is_cycle_supported_dominating(uint64_t s)const {
  uint64_t dominated=s;
  for(int v=0;v<N;v++)if(s&(1ULL<<v))dominated|=nbr[v];
  if(dominated!=((1ULL<<N)-1))return false;
  uint64_t remaining=s;
  while(remaining){
   uint64_t front=remaining&-remaining,seen=0;
   int vertices=0,twice_edges=0;
   while(front){
    uint64_t bit=front&-front;front-=bit;
    int v=__builtin_ctzll(bit);
    if(seen&bit) continue;
    seen|=bit;vertices++;
    twice_edges+=__builtin_popcountll(nbr[v]&s);
    front|=nbr[v]&s&~seen;
   }
   if(twice_edges<2*vertices)return false;
   remaining&=~seen;
  }
  return true;
 }
 bool exists_size(int i,int left,uint64_t s)const {
  if(!left)return is_cycle_supported_dominating(s);
  if(N-i<left)return false;
  return exists_size(i+1,left-1,s|(1ULL<<i))||exists_size(i+1,left,s);
 }
 int min_cycle_supported_size()const {
  for(int size=0;size<=n+2;size++)if(exists_size(0,size,0))return size;
  return -1;
 }
 int min_over_orientations()const {
  assert(edges.size()<20);
  int best=N+1;
  uint64_t total=1ULL<<edges.size();
  for(uint64_t o=0;o<total;o++){
   vector<uint64_t> incoming(N,0);
   for(size_t i=0;i<edges.size();i++){
    auto [a,b]=edges[i];
    if((o>>i)&1) incoming[a]|=1ULL<<b;
    else incoming[b]|=1ULL<<a;
   }
   bool valid=true;
   for(int v=0;v<N;v++)if(!incoming[v])valid=false;
   if(!valid)continue;
   for(uint64_t s=0;s<(1ULL<<N);s++){
    if(__builtin_popcountll(s)>=best)continue;
    bool total_dominates=true;
    for(int v=0;v<N;v++)if(!(incoming[v]&s)){
     total_dominates=false;break;
    }
    if(total_dominates)best=__builtin_popcountll(s);
   }
  }
  return best==N+1?-1:best;
 }
};

int main(){
 for(int n=2;n<=9;n++){
  Grid grid(n);
  int answer=grid.min_cycle_supported_size();
  if(answer!=n+2){cerr<<"wrong exhaustive minimum, width="<<n<<"\n";return 1;}
  uint64_t witness=0;
  for(int c=0;c<n;c++)witness|=1ULL<<(3*c+1);
  witness|=1ULL<<0;witness|=1ULL<<3;
  if(!grid.is_cycle_supported_dominating(witness))return 2;
  if(n<=3){
   int directed=grid.min_over_orientations();
   if(directed!=answer){cerr<<"orientation cross-check failed, width="<<n<<"\n";return 3;}
  }
  cout<<"width "<<n<<" minimum "<<answer<<" checked\n";
 }
 cout<<"VERIFY_OK\n";
}
