// Direct finite enumeration of optimal k-rainbow labelings of matching-deleted bicliques.
// Build: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
static int n,k,m,limit_weight;
static long long tested=0,accepted=0,lower_accepted=0,classified=0,boundary=0;
static int f[30];
static bool admissible(){
  int total=2*n;
  for(int i=0;i<total;i++)if(f[i]==0){
    int colors=0;
    if(i<n){for(int j=0;j<n;j++)if(i!=j)colors|=f[n+j];}
    else{for(int j=0;j<n;j++)if(i-n!=j)colors|=f[j];}
    if(colors!=(1<<k)-1)return false;
  }
  return true;
}
static bool expected_pattern(){
  int sa=0,sb=0,wa=0,wb=0,maskA=0,maskB=0;
  vector<int> cntA(k),cntB(k);
  for(int i=0;i<n;i++){
    if(f[i]){maskA|=1<<i;sa++;}
    if(f[n+i]){maskB|=1<<i;sb++;}
    for(int c=0;c<k;c++){
      if(f[i]&(1<<c)){cntA[c]++;wa++;}
      if(f[n+i]&(1<<c)){cntB[c]++;wb++;}
    }
  }
  if(wa==k && wb==k && maskA==maskB){
    bool ok=true;for(int c=0;c<k;c++)ok &= cntA[c]==1&&cntB[c]==1;
    if(ok){classified++;return true;}
  }
  if(n==2*k && ((sa==n&&sb==0)||(sa==0&&sb==n))){
    bool ok=true;
    for(int i=0;i<n;i++)ok &= (f[i]==0 || __builtin_popcount((unsigned)f[i])==1)&& (f[n+i]==0|| __builtin_popcount((unsigned)f[n+i])==1);
    for(int c=0;c<k;c++)ok &= (sa==n?cntA[c]:cntB[c])==2;
    if(ok){boundary++;return true;}
  }
  return false;
}
static void combinations(int depth,int last,int w){
 if(depth==w){
   tested++; if(!admissible())return;
   if(w<2*k){lower_accepted++;return;}
   accepted++; if(!expected_pattern()){cerr<<"UNKNOWN_VALID_PATTERN k="<<k<<" n="<<n<<"\n";exit(2);}
   return;
 }
 for(int a=last+1;a<=m-(w-depth);a++){
   int v=a/k,c=a%k;
   f[v]|=1<<c;combinations(depth+1,a,w);f[v]^=1<<c;
 }
}
static long long choose(int N,int R){if(R<0||R>N)return 0;long long z=1;for(int i=1;i<=R;i++)z=z*(N-R+i)/i;return z;}
static long long fact(int t){long long z=1;for(int i=2;i<=t;i++)z*=i;return z;}
static long long S(int nn,int pp){vector<vector<long long>> x(nn+1,vector<long long>(nn+1));x[0][0]=1;for(int i=1;i<=nn;i++)for(int j=1;j<=i;j++)x[i][j]=x[i-1][j-1]+j*x[i-1][j];return x[nn][pp];}
static long long prediction(int nn,int kk){long long z=0;for(int p=1;p<=kk;p++){long long v=fact(p)*S(kk,p);z+=choose(nn,p)*v*v;}if(nn==2*kk)z+=2*fact(2*kk)/(1LL<<kk);return z;}
static void run(int nn,int kk){
 n=nn;k=kk;m=2*n*k;fill(begin(f),end(f),0);tested=accepted=lower_accepted=classified=boundary=0;
 for(int w=0;w<=2*k;w++)combinations(0,-1,w);
 long long pred=prediction(n,k);
 cout<<"k="<<k<<" n="<<n<<" tested="<<tested<<" accepted="<<accepted<<" predicted="<<pred<<" matched="<<classified<<" boundary="<<boundary<<" suboptimal_accepted="<<lower_accepted<<"\n";
 if(lower_accepted || accepted!=pred || classified+boundary!=pred)exit(3);
}
int main(){run(1+1,1);run(3,1);run(4,2);run(5,2);run(6,3);run(7,3);cout<<"VERIFY_OK\n";}
