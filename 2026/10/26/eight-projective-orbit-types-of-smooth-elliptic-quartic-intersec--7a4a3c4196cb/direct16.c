#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
static uint8_t M[16][16];
static const int pairs[6][2]={{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}};
static uint8_t val4[1024][85],gv4[1024][85][4];
static uint8_t val16[1024][4369],gv16[1024][4369][4];
static uint8_t xx4[85][4],xx16[4369][4];
static void initmul(void){for(int a=0;a<16;a++)for(int b=0;b<16;b++){
 int prod=0;for(int j=0;j<4;j++)if((b>>j)&1)prod^=a<<j;
 for(int i=6;i>=4;i--)if(prod&(1<<i))prod^=(0x13<<(i-4));M[a][b]=(uint8_t)prod;
 }}
static int initpts(uint8_t pts[][4],int q){int n=0;for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++){
 int x[4]={a,b,c,d},start=-1;if(q==4){const int e[4]={0,1,6,7};for(int z=0;z<4;z++)x[z]=e[x[z]];}for(int k=0;k<4;k++)if(x[k]){start=k;break;}
 if(start<0||x[start]!=1)continue;for(int k=0;k<4;k++)pts[n][k]=x[k];n++;}
 return n;
}
static void precomp(int n,uint8_t p[][4],uint8_t *val,uint8_t *grad){
 for(int a=0;a<1024;a++)for(int npt=0;npt<n;npt++){
  int off=a*n+npt; uint8_t *g=grad+4*off;const uint8_t *x=p[npt];uint8_t v=0;
  for(int k=0;k<4;k++)if((a>>k)&1)v^=M[x[k]][x[k]];
  for(int k=0;k<6;k++)if((a>>(4+k))&1){int i=pairs[k][0],j=pairs[k][1];v^=M[x[i]][x[j]];g[i]^=x[j];g[j]^=x[i];}
  val[off]=v;
 }
}
static int test(int a,int b,int n,const uint8_t *v,const uint8_t *gr){
 for(int k=0;k<n;k++){
  if(v[a*n+k]||v[b*n+k])continue;
  const uint8_t *u=gr+4*(a*n+k),*w=gr+4*(b*n+k);
  int rk2=0;for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)if(M[u[i]][w[j]]^M[u[j]][w[i]])rk2=1;
  if(!rk2)return 1;
 }return 0;
}
int main(int argc,char **argv){int pairsout=(argc>1 && strcmp(argv[1],"--pairs")==0);initmul();int n4=initpts(xx4,4),n16=initpts(xx16,16);if(n4!=85||n16!=4369){fprintf(stderr,"Point normalization: %d %d\n",n4,n16);return 2;}
 precomp(n4,xx4,&val4[0][0],&gv4[0][0][0]); precomp(n16,xx16,&val16[0][0],&gv16[0][0][0]);
 long all=0,smooth=0,smooth4=0,extra=0,hist[16]={0};
 for(int a=1;a<1024;a++)for(int b=a+1;b<1024;b++)if((a^b)>b){all++;
 if(test(a,b,n4,&val4[0][0],&gv4[0][0][0]))continue;smooth4++;
 if(test(a,b,n16,&val16[0][0],&gv16[0][0][0])){extra++;continue;}
 smooth++;if(pairsout)printf("PAIR %d %d\n",a,b);int npts=0;for(int p=0;p<n16;p++){
  int rat=1;for(int i=0;i<4;i++)if(xx16[p][i]>1)rat=0;
  if(rat&&!val16[a][p]&&!val16[b][p])npts++;
 }hist[npts]++;
 }
 printf("All pencils %ld; GF4-Jacobian clean %ld; additional singular over F16 %ld; geometrically smooth %ld\n",all,smooth4,extra,smooth);
 for(int i=0;i<16;i++)if(hist[i])printf("rational_points=%d count=%ld\n",i,hist[i]);
 return 0;
}
