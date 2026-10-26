#include <bits/stdc++.h>
using namespace std;
struct Gen {uint64_t co,gr;};
int main(){
 vector<array<int,4>> mons;
 for(int a=0;a<=4;a++) for(int b=0;b<=4;b++) for(int c=0;c<=4;c++) for(int d=0;d<=4;d++) if(a+b+c+d==4) mons.push_back({a,b,c,d});
 assert(mons.size()==35);
 auto mid=[&](array<int,4> a){for(int t=0;t<35;t++)if(mons[t]==a)return t;assert(false);return 0;};
 vector<Gen> raw;
 for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)for(int k=0;k<4;k++){
  array<int,4>a{},b{};a[i]=2;a[j]=1;b[i]=1;b[j]=2;a[k]++;b[k]++;
  uint64_t coeff=(1ULL<<mid(a))^(1ULL<<mid(b));
  uint64_t grad=0;
  for(int p=1;p<=15;p++)if(p&(1<<k)){
   int q=(((p>>j)&1)<<i)^(((p>>i)&1)<<j);
   grad |= uint64_t(q)<<(4*(p-1));
  }
  raw.push_back({coeff,grad});
 }
 assert(raw.size()==24);
 uint64_t piv[35]={};vector<Gen> basis;
 for(auto [a,g]:raw){uint64_t v=a;
  for(int j=34;j>=0;j--)if((v>>j)&1){if(piv[j])v^=piv[j];else{piv[j]=v;basis.push_back({a,g});break;}}
 }
 assert(basis.size()==20);
 array<uint64_t,16> hist={}; array<uint64_t,16> zero={};
 uint64_t gray=0, coeff=0,totgood=0,maxd=0;
 for(int index=0;index<(1<<20);index++){
  if(index){int j=__builtin_ctz((unsigned)index);gray ^= basis[j].gr;coeff ^=basis[j].co;}
  unsigned seen=0, numzero=0;
  for(int p=0;p<15;p++){
   unsigned g=(gray>>(4*p))&15U;
   if(g)seen |= 1U<<g; else numzero++;
  }
  if(numzero==0){unsigned d=__builtin_popcount(seen); hist[d]++;totgood++; maxd=max<uint64_t>(maxd,d);}
  else zero[numzero]++;
 }
 cout<<"generator_count="<<raw.size()<<" dimension="<<basis.size()<<" total="<<(1<<20)<<"\n";
 cout<<"rationally_nonsingular="<<totgood<<" max_distinct_tangent_planes="<<maxd<<"\n";
 for(int i=0;i<16;i++)if(hist[i])cout<<"distinct="<<i<<" count="<<hist[i]<<"\n";
 for(int i=0;i<16;i++)if(zero[i])cout<<"rational_singular_points="<<i<<" count="<<zero[i]<<"\n";
 assert(totgood==124992 && maxd==12);
 assert(hist[10]==24192 && hist[11]==80640 && hist[12]==20160);
 return 0;
}
