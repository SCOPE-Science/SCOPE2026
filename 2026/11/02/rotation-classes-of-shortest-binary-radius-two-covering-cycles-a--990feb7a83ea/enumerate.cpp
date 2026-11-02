// Exact census of binary cyclic Hamming-radius-two covering sequences.
// C++17; no external libraries. All x in [0,2^L) are visited.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
static unsigned weight(unsigned x) { unsigned c=0; while(x){x&=x-1; ++c;} return c; }
static string bits(uint32_t x,int L){string s(L,'0');for(int i=0;i<L;++i)if((x>>i)&1u)s[i]='1';return s;}
static string canonical(const string& s){string best=s;for(size_t k=1;k<s.size();++k)best=min(best,s.substr(k)+s.substr(0,k));return best;}
static bool covers(unsigned n,unsigned L,uint32_t seq, const vector<array<uint64_t,8>>& ball){
  array<uint64_t,8> unionball{};
  for(unsigned i=0;i<L;++i){
    unsigned w=0;
    for(unsigned j=0;j<n;++j)w|=((seq>>((i+j)%L))&1u)<<j;
    for(unsigned k=0;k<8;++k)unionball[k]|=ball[w][k];
  }
  unsigned full=n==9?8:(1u<<n)/64;
  for(unsigned k=0;k<full;++k)if(unionball[k]!=UINT64_MAX)return false;
  if(n<6){uint64_t m=(1ull<<(1u<<n))-1;if(unionball[0]!=m)return false;}
  return true;
}
int main(){
  for(unsigned n=7;n<=9;++n){
    unsigned Lmax=(n==7?10:n==8?14:20);
    vector<array<uint64_t,8>> ball(1u<<n);
    for(unsigned w=0;w<(1u<<n);++w)
      for(unsigned t=0;t<(1u<<n);++t)
        if(weight(w^t)<=2)ball[w][t/64]|=1ull<<(t%64);
    for(unsigned L=1;L<=Lmax;++L){
      uint64_t count=0;
      map<string,unsigned> orbit_counts;
      for(uint32_t x=0;x<(1u<<L);++x){
        if(!covers(n,L,x,ball))continue;
        ++count; orbit_counts[canonical(bits(x,L))]++;
      }
      cout<<"length,"<<n<<','<<L<<','<<count<<','<<orbit_counts.size()<<'\n';
      if(L==Lmax){
        for(const auto& kv:orbit_counts)
          cout<<"orbit,"<<n<<','<<L<<','<<kv.second<<','<<kv.first<<'\n';
      }
    }
  }
}
