// Standalone exhaustive finite certificate for total metric dimensions of Q4,Q5,Q6
// and the complete minimum-basis orbit classification of Q4.
// Build: g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify_total_hypercubes.cpp -o verify_total_hypercubes
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using U64=std::uint64_t;

int weight(unsigned x) { int k=0; while(x){x&=x-1; ++k;} return k; }
U64 bit(int x){return U64(1)<<x;}

std::vector<U64> separator_masks(int n) {
 const int N=1<<n; std::vector<U64> out;
 for(int u=0;u<N;++u)for(int v=u+1;v<N;++v){
  // All pairs at odd Hamming distance are resolved by any third vertex.
  // Every tested candidate has at least five vertices.
  if(weight(u^v)%2) continue;
  U64 mask=0;
  for(int w=0;w<N;++w){
   if(w!=u && w!=v && weight(u^w)!=weight(v^w)) mask|=bit(w);
  }
  out.push_back(mask);
 }
 return out;
}

bool valid(U64 selected,const std::vector<U64>& masks){
 for(U64 m:masks)if(!(selected&m))return false;
 return true;
}

U64 setmask(const std::vector<int>& ids){U64 m=0;for(int i:ids)m|=bit(i);return m;}

long long checked_five_with_zero(int n,const std::vector<U64>& masks){
 const int N=1<<n;long long checked=0;long long hits=0;
 for(int a=1;a<N;++a)for(int b=a+1;b<N;++b)
 for(int c=b+1;c<N;++c)for(int d=c+1;d<N;++d){
  U64 m=bit(0)|bit(a)|bit(b)|bit(c)|bit(d);
  ++checked; if(valid(m,masks))++hits;
 }
 std::cout<<"n="<<n<<" normalized_five_sets_checked="<<checked<<" valid="<<hits<<"\n";
 assert(hits==0);
 return checked;
}

std::set<U64> orbit_of(U64 original){
 std::array<int,4> p={0,1,2,3};std::set<U64> orbit;
 do{
  int mapped[16];
  for(int x=0;x<16;++x){
   int y=0;for(int i=0;i<4;++i)if(x&(1<<i))y|=1<<p[i];
   mapped[x]=y;
  }
  for(int translate=0;translate<16;++translate){
   U64 m=0;
   for(int x=0;x<16;++x)if(original&bit(x))m|=bit(mapped[x]^translate);
   orbit.insert(m);
  }
 }while(std::next_permutation(p.begin(),p.end()));
 return orbit;
}

int main(){
 const std::array<std::array<int,6>,3> witnesses={{{0,1,2,3,4,5},
   {0,1,13,14,21,23},{6,15,26,38,55,60}}};
 for(int n=4;n<=6;++n){
  auto masks=separator_masks(n);
  long long total5=checked_five_with_zero(n,masks);
  U64 w=setmask(std::vector<int>(witnesses[n-4].begin(),witnesses[n-4].end()));
  std::cout<<"n="<<n<<" nontrivial_pair_constraints="<<masks.size()
           <<" exhibited_six_set_valid="<<valid(w,masks)<<"\n";
  assert(valid(w,masks));
  assert(total5==(n==4?1365:(n==5?31465:595665)));
 }
 const auto masks=separator_masks(4);
 std::set<U64> bases;long long total6=0;
 for(int a=0;a<16;++a)for(int b=a+1;b<16;++b)
 for(int c=b+1;c<16;++c)for(int d=c+1;d<16;++d)
 for(int e=d+1;e<16;++e)for(int f=e+1;f<16;++f){
  ++total6;U64 m=bit(a)|bit(b)|bit(c)|bit(d)|bit(e)|bit(f);
  if(valid(m,masks))bases.insert(m);
 }
 assert(total6==8008 && bases.size()==1600);
 std::cout<<"Q4_all_six_sets="<<total6<<" total_bases="<<bases.size()<<"\n";
 // Explicit representatives of the 11 disjoint orbits under 2^4 : S_4.
 const std::array<std::array<int,6>,11> reps={{{0,1,2,3,4,5},
 {0,1,2,3,4,9},{0,1,2,4,9,10},{0,1,2,5,6,7},
 {0,1,2,5,6,11},{0,1,2,5,6,12},{0,1,2,5,6,15},
 {0,1,2,5,10,12},{0,1,2,5,11,12},{0,1,6,7,10,11},
 {0,1,6,7,10,13}}};
 std::set<U64> union_orbits;std::vector<int> sizes;
 for(const auto& rep:reps){
  U64 m=setmask(std::vector<int>(rep.begin(),rep.end()));
  auto orbit=orbit_of(m);
  assert(bases.count(m));
  for(U64 x:orbit){assert(bases.count(x));assert(!union_orbits.count(x));union_orbits.insert(x);}
  sizes.push_back(int(orbit.size()));
 }
 std::sort(sizes.begin(),sizes.end());
 assert(union_orbits==bases);
 assert((sizes==std::vector<int>{32,32,96,96,192,192,192,192,192,192,192}));
 std::cout<<"Q4_orbits="<<sizes.size()<<" sizes=";
 for(int s:sizes){std::cout<<s<<" ";}
 std::cout<<"\nALL_CHECKS_PASSED\n";
}
