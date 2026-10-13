#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

constexpr int N=56;
constexpr int K=9;
set<uint64_t> exhaustive;
uint64_t nodes=0;
void search(vector<int>& a, int start, array<unsigned char,N> occupied) {
 ++nodes;
 if(int(a.size())==K) {
  uint64_t bits=0;for(int x:a)bits |= 1ULL<<x;
  if(!exhaustive.insert(bits).second)abort();
  return;
 }
 for(int x=start; x<=N-(K-int(a.size())); ++x) {
  auto next=occupied;
  bool okay=true;
  for(int y:a) {const int s=(x+y)%N; if(next[s]) {okay=false;break;}next[s]=1;}
  if(!okay)continue;
  a.push_back(x);search(a,x+1,next);a.pop_back();
 }
}
int main(){
 vector<int> a{0};array<unsigned char,N> occupied{};search(a,1,occupied);
 const array<int,K> model{0,1,2,4,7,13,24,32,42};
 set<uint64_t> allTransforms, normalizedTransforms;
 for(int u=1;u<N;u++) if(gcd(u,N)==1)
  for(int t=0;t<N;t++) {
   uint64_t bits=0;
   for(int x:model){int y=(u*x+t)%N;bits |= 1ULL<<y;}
   if(__builtin_popcountll(bits)!=K) return 2;
   allTransforms.insert(bits);
   if(bits&1)normalizedTransforms.insert(bits);
  }
 cout<<"search_nodes="<<nodes<<" exhaustive_zero_containing="<<exhaustive.size()
     <<" orbit_zero_containing="<<normalizedTransforms.size()
     <<" entire_affine_orbit="<<allTransforms.size()<<'\n';
 if(exhaustive!=normalizedTransforms)return 3;
 if(exhaustive.size()!=216||allTransforms.size()!=1344)return 4;
 cout<<"VERIFY_OK\n";
}
