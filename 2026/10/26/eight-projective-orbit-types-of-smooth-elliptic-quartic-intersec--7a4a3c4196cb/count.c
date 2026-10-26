#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static uint8_t mul[4][4]={{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};
static int pairidx[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
static inline uint8_t sq(uint8_t x){return mul[x][x];}
static inline uint8_t val(uint8_t q[10],uint8_t x[4]){uint8_t v=0;for(int i=0;i<4;i++)v^=mul[q[i]][sq(x[i])];for(int i=0;i<6;i++)v^=mul[q[4+i]][mul[x[pairidx[i][0]]][x[pairidx[i][1]]]];return v;}
static int check(int a,int b,int t){
  uint8_t q[10]={0},q0[10]={0},qother[10]={0},mat[4][4]={0};
  for(int i=0;i<10;i++){q0[i]=(a>>i)&1; qother[i]= (t==0)?((b>>i)&1):q0[i]; q[i]=q0[i]^mul[t][(b>>i)&1];}
  for(int i=0;i<6;i++){int x=pairidx[i][0],y=pairidx[i][1];mat[x][y]=mat[y][x]=q[4+i];}
  uint8_t rref[4][4];memcpy(rref,mat,sizeof(mat));int pivs[4],rank=0;
  for(int col=0;col<4;col++){int row=-1;for(int i=rank;i<4;i++)if(rref[i][col]){row=i;break;}if(row<0)continue;
  for(int j=0;j<4;j++){uint8_t tmp=rref[rank][j];rref[rank][j]=rref[row][j];rref[row][j]=tmp;}
  uint8_t inv=1;for(int k=1;k<=3;k++)if(mul[rref[rank][col]][k]==1){inv=k;break;}
  for(int j=0;j<4;j++)rref[rank][j]=mul[inv][rref[rank][j]];
  for(int i=0;i<4;i++)if(i!=rank){uint8_t c=rref[i][col];for(int j=0;j<4;j++)rref[i][j]^=mul[c][rref[rank][j]];}
  pivs[rank++]=col;
  }
  if(rank==4)return 1;
  if(rank<2)return 0; // a quadric with a >=plane of singular points meets the other quadric geometrically
  uint8_t ker[2][4]={{0}},coef[2]={0};int n=0;
  for(int j=0;j<4;j++){int p=0;for(int k=0;k<rank;k++)p|=(pivs[k]==j);if(p)continue;ker[n][j]=1;for(int k=0;k<rank;k++)ker[n][pivs[k]]=rref[k][j];n++;}
  if(n!=2){fprintf(stderr,"rank unexpected\n");exit(2);}
  coef[0]=val(q,ker[0]);coef[1]=val(q,ker[1]);
  if(coef[0]==0&&coef[1]==0)return 0;
  uint8_t x[4];for(int i=0;i<4;i++)x[i]=mul[ker[0][i]][sq(coef[1])]^mul[ker[1][i]][sq(coef[0])];
  return val(qother,x)!=0; // if q0 nonzero, singular x not in common base
}
static int smooth(int a,int b){int qs[]={a,b,a^b};
  // t=0, 1, infinity: swap to make q1 member with parameter zero.
  if(!check(a,b,0)||!check(b,a,0)||!check(a,b,1))return 0;
  // t = omega,omega^2; these only polar-degenerate if pfaffian identically zero or irreducible quadratic
  if(!check(a,b,2)||!check(a,b,3))return 0;
  return 1;
}
int main(int argc,char **argv){int pairsout=(argc>1 && strcmp(argv[1],"--pairs")==0);long long cnt=0,hist[16]={0},yespfzero=0;
  for(int a=1;a<1024;a++)for(int b=a+1;b<1024;b++){int c=a^b;if(c<b)continue;
    int ok=smooth(a,b);if(!ok)continue;
    int pa=(((a>>4)&1)&((a>>9)&1))^(((a>>5)&1)&((a>>8)&1))^(((a>>6)&1)&((a>>7)&1));
    int pb=(((b>>4)&1)&((b>>9)&1))^(((b>>5)&1)&((b>>8)&1))^(((b>>6)&1)&((b>>7)&1));
    int pc=((((a^b)>>4)&1)&(((a^b)>>9)&1))^(((((a^b)>>5)&1)&(((a^b)>>8)&1)))^(((((a^b)>>6)&1)&(((a^b)>>7)&1)));
    if(pa==0 && pb==0 && pc==0) yespfzero++;
    int n=0;for(int x=1;x<16;x++){int qv[3]={0};for(int j=0;j<3;j++){int q=(j==0?a:j==1?b:c);int v=0;for(int i=0;i<4;i++)v^=((q>>i)&1)*((x>>i)&1);for(int i=0;i<6;i++)v^=((q>>(i+4))&1)*((x>>pairidx[i][0])&1)*((x>>pairidx[i][1])&1);qv[j]=v;}
       if(qv[0]==0&&qv[1]==0)n++;}
    hist[n]++;if(pairsout)printf("PAIR %d %d\n",a,b);cnt++;
  }
  printf("TOTAL %lld pfzero %lld\n",cnt,yespfzero);for(int i=0;i<16;i++)if(hist[i])printf("points %d: %lld\n",i,hist[i]);
  return 0;
}
