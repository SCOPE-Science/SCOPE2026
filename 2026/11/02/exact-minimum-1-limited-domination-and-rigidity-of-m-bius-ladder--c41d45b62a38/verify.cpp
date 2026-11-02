// Exact finite cross-check for one-limited domination in Mobius ladders.
// This program is not used as a substitute for the all-m proof.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

static bool valid(uint32_t mask, int m) {
  int n=2*m;
  for (int v=0;v<n;++v) {
    int hits=((mask>>((v+n-1)%n))&1u)+((mask>>((v+1)%n))&1u)+((mask>>((v+m)%n))&1u);
    if(hits < ((mask>>v)&1u ? 2:1)) return false;
  }
  return true;
}
static uint32_t rotate(uint32_t mask,int n,int k) {
  uint32_t r=0;
  for(int i=0;i<n;++i) if((mask>>i)&1u) r|=1u<<((i+k)%n);
  return r;
}
static set<uint32_t> predicted(int m) {
  int n=2*m;set<uint32_t> r;
  if(m%4==0) {
    uint32_t word=0;
    for(int i=0;i<n;++i) if(i%4==0 || i%4==1) word|=1u<<i;
    for(int k=0;k<n;++k) r.insert(rotate(word,n,k));
    return r;
  }
  uint32_t interval=(1u<<(m+1))-1u;
  for(int k=0;k<n;++k)r.insert(rotate(interval,n,k));
  if(m%2) {
    // Both endpoints of an antipodal pair are selected according to a
    // minimum total dominating set on the m-cycle.
    for(uint32_t a=0;a<(1u<<m);++a) {
      if(__builtin_popcount(a)!=(m+1)/2) continue;
      bool total=true;
      for(int i=0;i<m;++i) {
        int left=(i+m-1)%m,right=(i+1)%m;
        if(!((a>>left)&1u) && !((a>>right)&1u))total=false;
      }
      if(total)r.insert(a|(a<<m));
    }
  }
  return r;
}
int main() {
  uint64_t candidates=0;
  for(int m=3;m<=12;++m) {
    int n=2*m;
    int target=m+(m%4!=0);
    set<uint32_t> actual;
    for(uint32_t mask=0;mask<(1u<<n);++mask) {
      int k=__builtin_popcount(mask);
      if(k>target)continue;
      ++candidates;
      if(!valid(mask,m))continue;
      if(k<target) { cerr<<"Below-bound witness m="<<m<<" mask="<<mask<<"\n";return 1; }
      actual.insert(mask);
    }
    auto expected=predicted(m);
    if(actual!=expected) {
      cerr<<"Mismatch m="<<m<<" actual="<<actual.size()<<" expected="<<expected.size()<<"\n";return 2;
    }
    int count=m%4==0?4:(m%2==0?2*m:3*m);
    if((int)actual.size()!=count) {cerr<<"Bad formula m="<<m<<"\n";return 3;}
    cout<<"m="<<m<<" gamma="<<target<<" minimum_count="<<count<<"\n";
  }
  cout<<"VERIFY_OK parameters=3..12 candidates_examined="<<candidates<<"\n";
}
