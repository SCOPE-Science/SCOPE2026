#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct Balls {array<U,32> d2{}; array<U,16> d3{};};
static inline unsigned subseq(int x,int n,int i,int j,int k){
 unsigned z=0;
 for(int p=0;p<n;++p)if(p!=i && p!=j && p!=k)z=(z<<1)|((x>>(n-1-p))&1);
 return z;
}
int main(int argc,char**argv){
 int Nmax=13;
 if(argc>1){cerr<<"No runtime change to exhaustive range is supported.\n";return 1;}
 // Verify attainable value counts for n=3..13, including m=0.
 for(int n=3;n<=Nmax;++n){
  int N=1<<n;vector<Balls> B(N);
  for(int x=0;x<N;++x){
   for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){
    unsigned z=subseq(x,n,i,j,-1); B[x].d2[z>>6]|=1ULL<<(z&63);
    for(int k=j+1;k<n;++k){
     unsigned z3=subseq(x,n,i,j,k);B[x].d3[z3>>6]|=1ULL<<(z3&63);
    }
   }
  }
  array<long long,21> hist{};int maxv=0;
  for(int x=0;x<N;++x)for(int y=0;y<x;++y){
   bool disj=true;
   for(int z=0;z<32;++z)if(B[x].d2[z]&B[y].d2[z]){disj=false;break;}
   if(!disj)continue;
   int val=0;for(int z=0;z<16;++z)val+=__builtin_popcountll(B[x].d3[z]&B[y].d3[z]);
   if(val>20){cerr<<"OUT_OF_BOUND "<<n<<' '<<x<<' '<<y<<' '<<val<<'\n';return 2;}
   ++hist[val];maxv=max(maxv,val);
  }
  string vals;for(int k=0;k<=20;++k)if(hist[k]){if(!vals.empty()) vals+=',';vals+=to_string(k);}
  cout<<"n="<<n<<" possible="<<vals<<" max="<<maxv<<" admissible_pairs="<<accumulate(hist.begin(),hist.end(),0LL)<<'\n';
  if(hist[18]!=0){cerr<<"RADIUS_THREE_EIGHTEEN_FOUND n="<<n<<"\n";return 3;}
  if(n==13){
   for(int k=0;k<=20;++k){bool expected=(k!=18);if(expected!=(hist[k]!=0)){cerr<<"SPECTRUM_MISMATCH m="<<k<<"\n";return 4;}}
  }
 }
 cout<<"VERIFY_OK exhaustive binary unordered-word pairs through length "<<Nmax<<"\n";
}
