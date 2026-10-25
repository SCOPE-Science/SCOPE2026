#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define Q 5
#define NP 31
#define NF 10
static int P[NP][3], M[NP][NF], D[NP][3][NF], npts=0;
static uint32_t LM[NP];
static const int expo[NF][3]={{3,0,0},{0,3,0},{0,0,3},{2,1,0},{2,0,1},{1,2,0},{0,2,1},{1,0,2},{0,1,2},{1,1,1}};
static int fmod5(int a){a%=5;return a<0?a+5:a;}
static int pow5(int a,int k){int r=1;while(k--)r=r*a%5;return r;}
int find_point(int a,int b,int c){if(a==0&&b==0&&c==0)return -1;int first=a?a:(b?b:c),iv=1;while((first*iv)%5!=1)iv++; a=a*iv%5;b=b*iv%5;c=c*iv%5;for(int i=0;i<NP;i++)if(P[i][0]==a&&P[i][1]==b&&P[i][2]==c)return i;return -1;}
int main(int argc,char**argv){
 for(int a=0;a<5;a++)for(int b=0;b<5;b++)for(int c=0;c<5;c++){if(!(a||b||c))continue;int first=a?a:(b?b:c);if(first!=1)continue;P[npts][0]=a;P[npts][1]=b;P[npts][2]=c;npts++;}
 if(npts!=31){fprintf(stderr,"POINTS %d\n",npts);return 1;}
 for(int i=0;i<NP;i++){for(int j=0;j<NF;j++){int a=P[i][0],b=P[i][1],c=P[i][2],*e=(int*)expo[j];M[i][j]=pow5(a,e[0])*pow5(b,e[1])%5*pow5(c,e[2])%5;for(int v=0;v<3;v++){D[i][v][j]=(e[v]>0)?e[v]*pow5(a,e[0]-(v==0))*pow5(b,e[1]-(v==1))*pow5(c,e[2]-(v==2))%5:0;}}}
 for(int i=0;i<NP;i++)for(int j=0;j<NP;j++){int x=0;for(int k=0;k<3;k++)x+=P[i][k]*P[j][k];if(x%5==0)LM[i]|=(1u<<j);}
 FILE *winfp=fopen("maximizers.bin","wb");
 long long histogram[32]={0};int maxCov=0;long long winners=0; long long maximizers_s[32]={0};long long examined=0; int cand[200][NF];int cand_n=0;
 int coef[NF];for(int i=0;i<NF;i++)coef[i]=0;
 long long total=1;for(int i=0;i<NF;i++)total*=5;
 for(long long m=1;m<total;m++){long long n=m;int seen=0,ok=0;for(int j=0;j<NF;j++){coef[j]=n%5;n/=5;if(coef[j]&&!seen){seen=1;ok=(coef[j]==1);}}
 if(!ok)continue;examined++;
 uint32_t mask=0;int nsmooth=0;
 for(int i=0;i<NP;i++){
  int eval=0;for(int j=0;j<NF;j++)eval+=coef[j]*M[i][j];if(eval%5)continue;
  int grad[3]={0};for(int k=0;k<3;k++)for(int j=0;j<NF;j++)grad[k]+=coef[j]*D[i][k][j];
  int l=find_point(fmod5(grad[0]),fmod5(grad[1]),fmod5(grad[2]));if(l<0)continue;
  nsmooth++;mask |= LM[l];if(mask==0x7fffffff)break;
 }
 int cover=__builtin_popcount(mask); histogram[cover]++; if(cover==29){uint32_t key=(uint32_t)m;fwrite(&key,4,1,winfp);}
 if(cover>maxCov){maxCov=cover;winners=0;cand_n=0;memset(maximizers_s,0,sizeof(maximizers_s));fprintf(stderr,"NEW MAX %d index %lld\n",cover,m);}
 if(cover==maxCov){winners++;maximizers_s[nsmooth]++;if(cand_n<200){memcpy(cand[cand_n],coef,sizeof(coef));cand_n++;}}
 }
 printf("examined %lld max %d winners %lld\n",examined,maxCov,winners);
 for(int i=0;i<32;i++)if(histogram[i])printf("hist %d %lld\n",i,histogram[i]);
 for(int i=0;i<32;i++)if(maximizers_s[i])printf("winner_nsmooth %d %lld\n",i,maximizers_s[i]);
 for(int i=0;i<cand_n;i++){printf("winner %d",i);for(int j=0;j<NF;j++)printf(" %d",cand[i][j]);printf("\n");}
 fclose(winfp); return 0;
}
