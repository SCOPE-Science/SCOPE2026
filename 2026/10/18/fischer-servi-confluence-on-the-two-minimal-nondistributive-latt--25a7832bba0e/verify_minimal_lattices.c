#include <stdio.h>
#include <stdint.h>
#include <string.h>
#define N 5
static uint32_t bit[N][N];
static int le[N][N];
static uint64_t counts[2], endpoint[2][4], fixedM3[6];
static int perms[6][5];
static int check(uint32_t r){
  // Reflexivity is built in. Check transitivity for ALL ordered triples.
  for(int x=0;x<N;x++)for(int y=0;y<N;y++)if(r&bit[x][y])
    for(int z=0;z<N;z++)if((r&bit[y][z])&&!(r&bit[x][z]))return 0;
  // (<=;R) subset (R;<=): x <= y R z => x R u <= z.
  for(int x=0;x<N;x++)for(int y=0;y<N;y++)if(le[x][y])
    for(int z=0;z<N;z++)if(r&bit[y][z]){
      int ok=0;for(int u=0;u<N;u++)if((r&bit[x][u])&&le[u][z]){ok=1;break;}
      if(!ok)return 0;
    }
  // (R;>=) subset (>=;R): x R y >= z => x >= u R z.
  for(int x=0;x<N;x++)for(int y=0;y<N;y++)if(r&bit[x][y])
    for(int z=0;z<N;z++)if(le[z][y]){
      int ok=0;for(int u=0;u<N;u++)if(le[u][x]&&(r&bit[u][z])){ok=1;break;}
      if(!ok)return 0;
    }
  return 1;
}
static int fixed(uint32_t r,int *p){
 for(int x=0;x<N;x++)for(int y=0;y<N;y++)
  if((!!(r&bit[x][y]))!=(!!(r&bit[p[x]][p[y]])))return 0;
 return 1;
}
static void run(int which){
 memset(le,0,sizeof(le));
 for(int i=0;i<N;i++)le[i][i]=1;
 for(int i=0;i<N;i++){le[0][i]=1;le[i][4]=1;}
 if(which==1){le[1][2]=1;}
 int offdiag[N*N][2], cnt=0;
 uint32_t diagonal=0;
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){
  if(i==j)diagonal|=bit[i][i];
  else {offdiag[cnt][0]=i;offdiag[cnt][1]=j;cnt++;}
 }
 for(uint32_t cfg=0;cfg<(1u<<cnt);cfg++){
  uint32_t r=diagonal;
  for(int k=0;k<cnt;k++)if(cfg&(1u<<k))r|=bit[offdiag[k][0]][offdiag[k][1]];
  if(!check(r))continue;
  counts[which]++;
  endpoint[which][((r&bit[0][4])?1:0)+((r&bit[4][0])?2:0)]++;
  if(which==0)for(int p=0;p<6;p++)fixedM3[p]+=fixed(r,perms[p]);
 }
 printf("%s label_count=%llu endpoints=[%llu,%llu,%llu,%llu]",which?"N5":"M3",
  (unsigned long long)counts[which],
  (unsigned long long)endpoint[which][0],(unsigned long long)endpoint[which][1],
  (unsigned long long)endpoint[which][2],(unsigned long long)endpoint[which][3]);
 if(which==0){
  uint64_t s=0; for(int p=0;p<6;p++){printf(" FIX%d=%llu",p,(unsigned long long)fixedM3[p]);s+=fixedM3[p];}
  printf(" isoclasses=%llu",(unsigned long long)(s/6));
 }
 printf("\n");
}
int main(){
 int n=0;
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)bit[i][j]=1u<<(i*N+j);
 for(int a=1;a<=3;a++)for(int b=1;b<=3;b++)if(a!=b)
  for(int c=1;c<=3;c++)if(c!=a&&c!=b){int *p=perms[n++];p[0]=0;p[4]=4;p[1]=a;p[2]=b;p[3]=c;}
 if(n!=6)return 1;
 run(0);run(1);
 return 0;
}
