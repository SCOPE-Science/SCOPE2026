#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
long long binom(int n,int k){if(k<0||k>n)return 0;long long z=1;for(int i=1;i<=k;i++)z=z*(n-i+1)/i;return z;}
int main(){unsigned long long checked=0,accepted=0,facets=0;
for(int n=3;n<=6;n++){
 const int N=3*n; vector<uint32_t> common;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){
  int ra=a/n,ca=a%n,rb=b/n,cb=b%n;
  if(ra!=rb && ca!=cb)continue; // adjacent
  uint32_t mask=0;
  for(int w=0;w<N;w++) {
   int rw=w/n,cw=w%n;
   if(rw!=ra && cw!=ca && rw!=rb && cw!=cb) mask|=(uint32_t(1)<<w);
  }
  assert(mask);
  common.push_back(mask);
 }
 vector<unsigned long long> actual(N+1,0),expected(N+1,0);
 for(uint32_t X=0;X<(1u<<N);X++){
  bool good=true;
  for(uint32_t C:common)if((C & ~X)==0){good=false;break;}
  int bits=__builtin_popcount(X);
  actual[bits]+=good;
  if(good){
    bool maximal=true;
    for(int v=0;v<N;v++)if(!(X&(1u<<v))){
      uint32_t larger=X | (1u<<v);
      bool still=true;
      for(uint32_t C:common)if((C & ~larger)==0){still=false;break;}
      if(still){maximal=false;break;}
    }
    if(maximal){assert(bits==3*n-6);facets++;}
  }
  checked++;
  accepted+=good;
 }
 const int q=n*(n-1)/2;
 vector<long long> B(N+1),res(N+1),t(N+1);
 for(int k=3;k<=n;k++)B[n-k]=binom(n,k);
 auto conv=[&](const vector<long long>& A,const vector<long long>& D){vector<long long>E(N+1);for(int i=0;i<=N;i++)for(int j=0;i+j<=N;j++)E[i+j]+=A[i]*D[j];return E;};
 auto B2=conv(B,B),B3=conv(B2,B);
 for(int i=0;i<=N;i++){
  res[i]=B3[i];
  if(i>=n-2)res[i]+=3LL*q*B2[i-(n-2)];
  if(i>=2*n-4)res[i]+=3LL*q*(q-1)*B[i-(2*n-4)];
  if(i==3*n-6)res[i]+=1LL*q*(q-1)*(q-2);
  assert((unsigned long long)res[i]==actual[i]);
 }
 assert(actual[3*n-6]==(unsigned long long)q*(q-1)*(q-2));
 for(int j=3*n-5;j<=N;j++)assert(actual[j]==0);
 cout<<"n="<<n<<" subsets="<<(1u<<N)<<" total_sets=";
 unsigned long long num=0;for(auto a:actual)num+=a;cout<<num<<" max_size="<<3*n-6<<" max_count="<<actual[3*n-6]<<" PASS\n";
}
cout<<"VERIFICATION_OK subsets="<<checked<<" accepted="<<accepted<<" facets="<<facets<<" n=3..6\n";
}
