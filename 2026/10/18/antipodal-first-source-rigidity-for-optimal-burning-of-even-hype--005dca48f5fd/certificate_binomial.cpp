#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdlib>
using namespace std;
int n,k,g[8],choose[15][15],rad[4],best[15];long long classes[15];
long long missed;
void witness(int p,int d0,int d1,int d2,int d3,int mult){
 if(p==8){if(d0>rad[0]&&d1>rad[1]&&d2>rad[2]&&d3>rad[3])missed+=mult;return;}
 int size=g[p];
 for(int ones=0;ones<=size;ones++){
  int x2=(p&4)?size-ones:ones;
  int x3=(p&2)?size-ones:ones;
  int x4=(p&1)?size-ones:ones;
  witness(p+1,d0+ones,d1+x2,d2+x3,d3+x4,mult*choose[size][ones]);
 }
}
void compositions(int p,int remain){
 if(p==7){
  g[p]=remain;
  int d=0;for(int a=0;a<8;a++)if(a&4)d+=g[a];
  if(d==n)return;
  missed=0;witness(0,0,0,0,0,1);
  best[d]=min(best[d],(int)missed);classes[d]++;
  return;
 }
 for(int x=0;x<=remain;x++){g[p]=x;compositions(p+1,remain-x);}
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 n=atoi(argv[1]);if(n<6||n>14||n%2)return 2;
 k=n/2+1;for(int j=0;j<4;j++)rad[j]=k-1-j;
 for(int a=0;a<=n;a++){choose[a][0]=choose[a][a]=1;for(int b=1;b<a;b++)choose[a][b]=choose[a-1][b-1]+choose[a-1][b];best[a]=n==14?16385:(1<<n)+1;}
 compositions(0,n);
 for(int d=0;d<n;d++)printf("dimension=%d second_weight=%d composition_classes=%lld min_uncovered=%d\n",n,d,classes[d],best[d]);
}
