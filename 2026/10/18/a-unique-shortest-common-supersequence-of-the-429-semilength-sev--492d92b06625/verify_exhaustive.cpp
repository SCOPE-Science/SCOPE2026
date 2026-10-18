#include <bits/stdc++.h>
using namespace std;
void rec(int n,int a,int b,uint32_t mask,vector<uint32_t>&v){if(a+b==2*n){v.push_back(mask);return;}if(a<n)rec(n,a+1,b,mask,v);if(b<a)rec(n,a,b+1,mask|(1u<<(a+b)),v);}
// Bit 1 represents right parenthesis. Bit i counts from the left.
bool covers(uint32_t host,int L,uint32_t pat,int n){int j=0;for(int i=0;i<L && j<2*n;i++)if(((host>>i)&1u)==((pat>>j)&1u))++j;return j==2*n;}
string str(uint32_t u,int L){string s;for(int i=0;i<L;i++)s+=((u>>i)&1u)?')':'(';return s;}
int main(int argc,char**argv){int n=7;vector<uint32_t> v;rec(n,0,0,0,v);int S=v.size();cerr<<"Catalan="<<S<<"\n";vector<uint32_t> w;w.push_back(v[0]);w.push_back(v.back());for(auto x:v)if(x!=v[0]&&x!=v.back())w.push_back(x);
for(int L=21;L<=22;L++){uint64_t hits=0;string witness;uint64_t candidate=0;
 for(uint32_t x=0;x<(1u<<L);x++){
  // Exhaust all binary hosts without restrictions, before the safe target filter.
  if(!covers(x,L,w[0],n)||!covers(x,L,w[1],n))continue;
  ++candidate;
  bool ok=true;for(int j=2;j<S;j++)if(!covers(x,L,w[j],n)){ok=false;break;}
  if(ok){++hits;witness=str(x,L);}
 }
 cout<<"L="<<L<<" prefilter_pass="<<candidate<<" universal="<<hits<<" witness="<<witness<<"\n";
  if(hits != (uint64_t)(L==22)) return 2;
}}
