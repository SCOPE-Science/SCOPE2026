// Exact finite coverage certificate for sums of a Zumkeller and a practical number.
// Usage: g++ -O3 -std=c++17 verify_large.cpp -o verify_large && ./verify_large
#include <bits/stdc++.h>
using namespace std;
int main() {
  constexpr int N=42000000, MOD=99225, FINAL_START=19069;
  vector<int> spf(N+1);
  for(int i=2;i<=N;i++)if(!spf[i]){
    spf[i]=i;
    if(1LL*i*i<=N)
      for(long long j=1LL*i*i;j<=N;j+=i)if(!spf[j])spf[j]=i;
  }
  size_t len=(N+64ULL)/64;
  vector<uint64_t> practical_bits(len),representable(len);
  vector<int> first(MOD,-1);first[1]=1;
  long long pc=0;
  for(int n=2;n<=N;n+=2){
    int z=n;long long sigma=1;bool practical=true;
    while(z>1){
      int p=spf[z],pp=1,geom=1;
      while(z%p==0){z/=p;pp*=p;geom+=pp;}
      if(p>sigma+1){practical=false;break;}
      sigma*=geom;
    }
    if(practical){
      pc++; practical_bits[n>>6]|=1ULL<<(n&63);
      if(first[n%MOD]<0)first[n%MOD]=n;
    }
  }
  int missing=0, maxfirst=0, maxresidue=-1;
  for(int r=0;r<MOD;r++){
    if(first[r]<0)missing++;
    if(first[r]>maxfirst){maxfirst=first[r];maxresidue=r;}
  }
  if(missing || maxfirst!=41235272 || maxresidue!=56897){
    cerr<<"Residue-class certificate failed: "<<missing<<"/"<<maxfirst<<"/"<<maxresidue<<"\n";
    return 1;
  }
  const int bound=maxfirst+945;
  if(bound>N){cerr<<"Bound outside sieve\n";return 1;}
  ifstream in("odd_z_witnesses.txt");
  if(!in){cerr<<"Missing witnesses\n";return 1;}
  int count=0,last=0;long long w;
  while(in>>w){
    if(w<945 || w>1000000 || (w&1)==0 || w<=last){cerr<<"Invalid witness index\n";return 1;}
    last=(int)w;count++;
    size_t s=w>>6,r=w&63;
    for(size_t i=s;i<len;i++){
      uint64_t v=practical_bits[i-s]<<r;
      if(r && i>s)v|=practical_bits[i-s-1]>>(64-r);
      representable[i]|=v;
    }
  }
  if(count!=1989){cerr<<"Unexpected witness count "<<count<<"\n";return 1;}
  int missing_inside=0, first_gap=0;
  for(int n=FINAL_START;n<bound;n+=2){
    if(!(representable[n>>6]>>(n&63)&1ULL)){
      missing_inside++;
      if(!first_gap)first_gap=n;
    }
  }
  cout<<"PRACTICAL_COUNT="<<pc<<" RESIDUES="<<MOD
      <<" MAX_FIRST="<<maxfirst<<" RESIDUE="<<maxresidue
      <<" BOUND="<<bound<<" ODD_WITNESSES="<<count
      <<" EXCEPTIONS_ABOVE_19067="<<missing_inside
      <<" FIRST_EXCEPTION="<<first_gap<<"\n";
  if(missing_inside!=1||first_gap!=20177)return 1;
  cout<<"LARGE_CERTIFICATE_OK\n";
}
