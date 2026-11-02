// Exhaustive finite-state certificate for synchronous majority on Boolean cubes Q_1 through Q_4.
// Build: g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_hypercube.cpp -o verify_hypercube
// Run: ./verify_hypercube
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;
static uint32_t step(int dim,uint32_t bits){
 const int vertices=1<<dim;
 uint32_t next=0;
 for(int v=0;v<vertices;v++){
  int ones=0;
  for(int axis=0;axis<dim;axis++) ones += (bits>>(v^(1<<axis)))&1u;
  bool old=(bits>>v)&1u;
  bool now = 2*ones>dim || (2*ones==dim && old);
  next|=uint32_t(now)<<v;
 }
 return next;
}
int main(){
 for(int dim=1;dim<=4;dim++){
  const int v=1<<dim;const uint32_t states=uint32_t(1)<<v;
  vector<uint32_t> next(states);for(uint32_t x=0;x<states;x++)next[x]=step(dim,x);
  uint64_t fixed=0,twostates=0,basinfix=0,basintwo=0;
  array<uint64_t,8> shell={},basin1={},basin2={};
  array<uint64_t,17> fixed_weight={},two_weight={};
  unsigned maxdepth=0;uint32_t witness=0;
  for(uint32_t x=0;x<states;x++){
   if(next[x]==x){fixed++;fixed_weight[__builtin_popcount(x)]++;}
   else if(next[next[x]]==x){twostates++;two_weight[__builtin_popcount(x)]++;}
   uint32_t y=x;unsigned t=0;
   while(next[next[y]]!=y){y=next[y];t++;assert(t<8);}
   assert(t<8);shell[t]++;if(t>maxdepth){maxdepth=t;witness=x;}
   if(next[y]==y){basinfix++;basin1[t]++;}else{basintwo++;basin2[t]++;}
  }
  const int expect_fixed[]={0,2,6,8,702};
  const int expect_twostates[]={0,2,2,56,1770};
  const int expect_maxdepth[]={0,0,1,1,4};
  assert(fixed==uint64_t(expect_fixed[dim])&&twostates==uint64_t(expect_twostates[dim])&&maxdepth==(unsigned)expect_maxdepth[dim]);
  assert(fixed+twostates==shell[0]);
  assert(basinfix+basintwo==states);
  cout<<"dimension="<<dim<<" vertices="<<v<<" states="<<states<<" fixed="<<fixed
      <<" primitive_two_orbits="<<twostates/2<<" basin_fixed="<<basinfix
      <<" basin_two="<<basintwo<<" max_entry="<<maxdepth
      <<" witness_decimal="<<witness<<"\n";
  cout<<"  entry_shells:";for(unsigned t=0;t<=maxdepth;t++)cout<<" "<<shell[t];cout<<"\n";
  cout<<"  fixed_entry_shells:";for(unsigned t=0;t<=maxdepth;t++)cout<<" "<<basin1[t];cout<<"\n";
  cout<<"  two_entry_shells:";for(unsigned t=0;t<=maxdepth;t++)cout<<" "<<basin2[t];cout<<"\n";
  cout<<"  fixed_weight:";for(int t=0;t<=v;t++)cout<<" "<<fixed_weight[t];cout<<"\n";
  cout<<"  two_state_weight:";for(int t=0;t<=v;t++)cout<<" "<<two_weight[t];cout<<"\n";
  if(dim==4){
   for(uint32_t x=0;x<states;x++)if(next[next[x]]==x&&next[x]!=x&&x<next[x])
    cout<<"PAIR "<<x<<" "<<next[x]<<"\n";
  }
 }
}
