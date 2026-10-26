#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
static uint8_t mult4[4][4]={{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};
static inline uint8_t addmul(uint8_t a,uint8_t b,uint8_t c){return a^mult4[b][c];}
static int rank16(uint8_t x[16],uint8_t tab[16][16]){
 uint8_t bs[16][16]={{0}};int dim=0;
 for(int j=0;j<16;j++){
  uint8_t v[16]={0};
  for(int i=0;i<16;i++)if(x[i])v[tab[i][j]]^=x[i];
  for(int k=15;k>=0;k--)if(v[k]){
   if(bs[k][k]){uint8_t t=mult4[v[k]][(bs[k][k]==1?1:(bs[k][k]==2?3:2))];for(int h=0;h<16;h++)v[h]^=mult4[t][bs[k][h]];}
   else{uint8_t inv=(v[k]==1?1:(v[k]==2?3:2));for(int h=0;h<16;h++)bs[k][h]=mult4[inv][v[h]];dim++;break;}
  }
 }
 return dim;
}
void calc(int r,int c,int q,int rank){
 uint8_t gtab[16][16],sigma[8];for(int i=0;i<8;i++)sigma[i]=(r*i)&7;
 for(int i=0;i<16;i++)for(int j=0;j<16;j++){
  int e=i&7,f=j&7,gi=i>>3,gj=j>>3;
  gtab[i][j]=(e+(gi?r:1)*f+c*gi*gj)%8 +8*(gi^gj);
 }
 long long counts[17]={0},v_good=0,u_good=0;
 int maxv=1;for(int i=0;i<8;i++)maxv*=q;
 for(int vcode=0;vcode<maxv;vcode++){
  uint8_t v[8],vs[8]={0},norm[8]={0},u0[8]={0};
  int t=vcode;for(int i=0;i<8;i++){v[i]=t%q;t/=q;vs[sigma[i]]=v[i];}
  for(int i=0;i<8;i++)if(v[i])for(int j=0;j<8;j++)if(vs[j])norm[(i+j+c)&7]^=mult4[v[i]][vs[j]];
  if(norm[1]||norm[3]||norm[5]||norm[7])continue;
  v_good++;
  for(int i=0;i<4;i++){uint8_t z=norm[2*i];u0[i]=(q==4)?mult4[z][z]:z;}
  int maxu=1;for(int i=0;i<4;i++)maxu*=q;
  for(int uc=0;uc<maxu;uc++){
   uint8_t u[8],z[8]={0};memcpy(u,u0,8);
   int w=uc;for(int i=0;i<4;i++){int a=w%q;w/=q;u[i]^=a;u[i+4]^=a;}
   for(int i=0;i<8;i++){z[i]^=u[i];z[sigma[i]]^=u[i];}
   uint8_t cross[8]={0};for(int i=0;i<8;i++)if(v[i])for(int j=0;j<8;j++)if(z[j])cross[(i+j)&7]^=mult4[v[i]][z[j]];
   int iszero=1;for(int i=0;i<8;i++)if(cross[i]){iszero=0;break;}
   if(!iszero)continue;
   u_good++;
   if(rank){uint8_t x[16];memcpy(x,u,8);memcpy(x+8,v,8);int rr=rank16(x,gtab);counts[rr]++;}
  }
 }
 printf("q=%d r=%d c=%d v_allowed=%lld squarezero=%lld rank=%d\n",q,r,c,v_good,u_good,rank);
 if(rank){for(int i=0;i<=8;i++)if(counts[i])printf(" %d:%lld",i,counts[i]);puts("");}
}
int main(int argc,char**argv){int q=argc>=2?atoi(argv[1]):4;int rank=argc>=3?atoi(argv[2]):1;calc(7,0,q,rank);calc(7,4,q,rank);calc(3,0,q,rank);return 0;}
