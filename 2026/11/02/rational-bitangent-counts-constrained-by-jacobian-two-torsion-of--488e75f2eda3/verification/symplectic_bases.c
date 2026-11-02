#include <stdio.h>
#include <stdint.h>
#include <string.h>

static unsigned char basis[6];
static unsigned long long table[7][29];
static unsigned long long total=0;
static unsigned long long class_signature[7][29];
static int odd[28], oddn=0;
static int parity[64], quad[64];
static int bil(int x,int y){ int z=0;for(int i=0;i<6;i+=2)z^=((x>>i)&1)*((y>>(i+1))&1)^((x>>(i+1))&1)*((y>>i)&1);return z;}
static void one(){
 int fixed=0;
 for(int a=0;a<28;a++){
  int t=odd[a],ok=1;
  for(int j=0;j<6;j++) if (quad[basis[j]] ^ bil(t,basis[j]^(1<<j))) {ok=0;break;}
  fixed+=ok;
 }
 unsigned char rows[6]={0};
 for(int i=0;i<6;i++) for(int j=0;j<6;j++) if ((basis[j]>>i)&1) rows[i]|=(1<<j);
 for(int i=0;i<6;i++) rows[i]^=1<<i;
 int rank=0;
 for(int j=0;j<6;j++){
  int pivot=rank;while(pivot<6&&!(rows[pivot]&(1<<j)))pivot++;
  if(pivot==6)continue;
  unsigned char h=rows[pivot];rows[pivot]=rows[rank];rows[rank]=h;
  for(int i=0;i<6;i++)if(i!=rank&&(rows[i]&(1<<j)))rows[i]^=rows[rank];
  rank++;
 }
 table[6-rank][fixed]++;
 total++;
}
static void go(int depth){
 if(depth==3){one();return;}
 for(int v=1;v<64;v++){
  int ok=1;
  for(int j=0;j<2*depth;j++)if (bil(v,basis[j])){ok=0;break;}
  if(!ok)continue;
  basis[2*depth]=v;
  for(int w=1;w<64;w++){
   if(!bil(v,w))continue;
   ok=1;for(int j=0;j<2*depth;j++)if (bil(w,basis[j])){ok=0;break;}
   if(!ok)continue;
   basis[2*depth+1]=w;
   go(depth+1);
  }
 }
}
int main(){
 for(int x=0;x<64;x++){
  int q=0;for(int i=0;i<6;i+=2)q^=((x>>i)&1)&((x>>(i+1))&1);
  quad[x]=q;if(q)odd[oddn++]=x;
 }
 go(0);
 printf("TOTAL=%llu ODD=%d\n",total,oddn);
 printf("dimJ2fixed,rationalbitangents,number_symplectic_elements\n");
 for(int i=0;i<=6;i++)for(int j=0;j<=28;j++)if(table[i][j])printf("%d,%d,%llu\n",i,j,table[i][j]);
}
