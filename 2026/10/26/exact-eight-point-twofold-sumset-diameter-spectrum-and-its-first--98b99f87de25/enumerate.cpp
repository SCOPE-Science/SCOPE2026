#include <bits/stdc++.h>
using namespace std;
static unsigned long long rec_n=0;
static int K,MAX;
static long long hist[128]={};
static int D[128];
static vector<int> W[128];
static int a[20];
static void dfs(int j, int start){
 if(j==K){
  unsigned long long lo=0,hi=0;
  for(int i=0;i<K;i++)for(int t=i;t<K;t++){
   int z=a[i]+a[t]; if(z<64)lo|=1ULL<<z;else hi|=1ULL<<(z-64);
  }
  int n=__builtin_popcountll(lo)+__builtin_popcountll(hi);
  ++rec_n;
  hist[n]++;
  if(a[K-1]<D[n]){D[n]=a[K-1]; W[n].assign(a,a+K);}
  return;
 }
 for(int v=start;v<=MAX-(K-1-j);v++){
  a[j]=v;dfs(j+1,v+1);
 }
}
int main(int argc,char**argv){
 K=atoi(argv[1]); MAX=atoi(argv[2]);
 for(int &d:D)d=INT_MAX;
 a[0]=0; dfs(1,1);
 cout<<"K="<<K<<" MAX="<<MAX<<" enumerated="<<rec_n<<"\n";
 for(int k=0;k<128;k++)if(hist[k]){
  cout<<"size="<<k<<" min_d="<<D[k]<<" count="<<hist[k]<<" witness=";
  for(int v:W[k])cout<<v<<",";
  cout<<"\n";
 }
}
