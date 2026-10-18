#include <cstdio>
#include <cstdint>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
using U=uint32_t; using L=uint64_t;
struct M {int a,b,c;};
vector<M> mon(int n){vector<M> a;for(int c=0;c<=n;c++)for(int b=0;b<=n-c;b++)a.push_back({n-b-c,b,c});return a;}
int main(){
 auto f5=mon(5),f4=mon(4),f6=mon(6),f10=mon(10);
 int m4[6][6][6]={},m10[11][11][11]={};
 for(int i=0;i<15;i++){auto a=f4[i];m4[a.a][a.b][a.c]=i;}
 for(int i=0;i<66;i++){auto a=f10[i];m10[a.a][a.b][a.c]=i;}
 U evalu[7]={}; L contain[7]={};
 for(int p=1;p<=7;p++)for(int i=0;i<21;i++){auto a=f5[i];if((!a.a||(p&1))&&(!a.b||(p&2))&&(!a.c||(p&4))) evalu[p-1] |=1u<<i;}
 for(int l=1;l<=7;l++)for(int p=1;p<=7;p++)if(!(__builtin_parity(l&p)))contain[l-1] |=1ull<<(p-1);
 int masks[10];for(int &v:masks)v=-1;int cntpat[10]={};
 for(int mask=0;mask<128;mask++){
  int n=__builtin_popcount((U)mask), col=0;
  for(int l=0;l<7;l++) if((mask & contain[l])==contain[l])col++;
  int type=n;
  if(n==3) type=col?3:4;
  else if(n==4) type=col==0?5:6;
  else if(n>=5) type=n+2;
  if(n<=2)type=n;
  if(masks[type]==-1)masks[type]=mask;
  cntpat[type]++;
 }
 printf("fiber types and representative masks:\n");for(int i=0;i<10;i++)printf("%d: %d x %u\n",i,cntpat[i],masks[i]);
 // Different rank method: construct 66 rows of 84-bit column incidence for gradient multiplication.
 auto smooth=[&](U F)->bool{
  U grad[3]={};
  for(int i=0;i<21;i++)if(F>>i&1){auto a=f5[i];int ex[]={a.a,a.b,a.c};for(int k=0;k<3;k++)if(ex[k]&1){ex[k]--;grad[k]^=1u<<m4[ex[0]][ex[1]][ex[2]];ex[k]++;}}
  struct Two {L lo=0,hi=0;};Two rows[66]={};
  for(int k=0;k<3;k++)for(int j=0;j<28;j++){
    int col=28*k+j;auto b=f6[j];U g=grad[k];while(g){int i=__builtin_ctz(g);g&=g-1;auto a=f4[i];int r=m10[a.a+b.a][a.b+b.b][a.c+b.c];if(col<64)rows[r].lo ^= 1ull<<col;else rows[r].hi ^=1ull<<(col-64);}
  }
  int rank=0;
  for(int bit=83;bit>=0;bit--){
    int pivot=-1;for(int r=rank;r<66;r++)if((bit<64?rows[r].lo>>bit:rows[r].hi>>(bit-64))&1ull){pivot=r;break;}
    if(pivot<0)continue;
    auto t=rows[rank];rows[rank]=rows[pivot];rows[pivot]=t;
    for(int r=rank+1;r<66;r++)if((bit<64?rows[r].lo>>bit:rows[r].hi>>(bit-64))&1ull){rows[r].lo^=rows[rank].lo;rows[r].hi^=rows[rank].hi;}
    rank++;if(rank==66)break;
  }
  return rank==66;
 };
 long long counts[10]={};
 for(U F=1;F<(1u<<21);F++){
  int pattern=0;for(int i=0;i<7;i++)if(!__builtin_parity(F&evalu[i]))pattern|=1<<i;
  for(int j=0;j<10;j++)if(pattern==masks[j]){counts[j]+=smooth(F);break;}
 }
 printf("smooth per representative rational-point fiber:\n");for(int j=0;j<10;j++)printf("%d %lld\n",j,counts[j]);
}
