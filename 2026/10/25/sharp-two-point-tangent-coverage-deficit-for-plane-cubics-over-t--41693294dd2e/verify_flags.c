/* Independent finite-field verification by coefficients of the restriction to a line.
   Every rational flag (P,L) uses another rational Q on L.  The coefficient
   of t in F(P+t Q) detects tangency when F(P)=0.  No differential or
   gradient formula is used. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define K 10
#define NP 31
static const int E[10][3]={{3,0,0},{0,3,0},{0,0,3},{2,1,0},{2,0,1},{1,2,0},{0,2,1},{1,0,2},{0,1,2},{1,1,1}};
static int pts[NP][3],mon[NP][K],flag[NP][6],flagval[NP][6][K];
static uint32_t lines[NP];
static int pw(int x,int n){int p=1;while(n--)p=p*x%5;return p;}
static int eval_monomial(int p[3],int j){int r=1;for(int d=0;d<3;d++)r=r*pw(p[d],E[j][d])%5;return r;}
static int incident(int a[3],int b[3]){return (a[0]*b[0]+a[1]*b[1]+a[2]*b[2])%5==0;}
static int tm_value(int a[3],int b[3],int j){int v[3]; int f1,f4,f2;
  for(int d=0;d<3;d++)v[d]=(a[d]+b[d])%5;f1=eval_monomial(v,j);
  for(int d=0;d<3;d++)v[d]=(a[d]+4*b[d])%5;f4=eval_monomial(v,j);
  for(int d=0;d<3;d++)v[d]=(a[d]+2*b[d])%5;f2=eval_monomial(v,j);
  int U=(f1-f4+5)*3%5,B=(f1+f4)*3%5;
  return (3*U+4*B-f2+15)%5;
}
int main(void){int count=0;
  for(int x=0;x<5;x++)for(int y=0;y<5;y++)for(int z=0;z<5;z++){
    int p[3]={x,y,z};int first=x?x:(y?y:z);if(first!=1)continue;
    for(int d=0;d<3;d++)pts[count][d]=p[d];count++;
  }
  if(count!=31)return 1;
  for(int i=0;i<NP;i++)for(int j=0;j<K;j++)mon[i][j]=eval_monomial(pts[i],j);
  for(int i=0;i<NP;i++)for(int l=0;l<NP;l++)if(incident(pts[i],pts[l]))lines[l]|=1u<<i;
  for(int i=0;i<NP;i++){
    int k=0;for(int l=0;l<NP;l++)if(incident(pts[i],pts[l])){
      if(k>=6)return 2;flag[i][k]=l;int q=0;
      while(q<NP && (q==i || !incident(pts[q],pts[l])))q++;
      if(q==NP)return 3;
      for(int j=0;j<K;j++)flagval[i][k][j]=tm_value(pts[i],pts[q],j);k++;
    }if(k!=6)return 4;
  }
  long long histogram[32]={0};long long winners=0;int biggest=0;int coefficients[K];
  for(int prefix=0;prefix<K;prefix++){
    int power=1;for(int i=prefix+1;i<K;i++)power*=5;
    for(int index=0;index<power;index++){
      for(int j=0;j<K;j++)coefficients[j]=0; coefficients[prefix]=1;
      int v=index;for(int j=prefix+1;j<K;j++){coefficients[j]=v%5;v/=5;}
      uint32_t covered=0;
      for(int p=0;p<NP;p++){
        int n=0;for(int j=0;j<K;j++)n+=coefficients[j]*mon[p][j];if(n%5)continue;
        int tangent=-1,zeros=0;
        for(int k=0;k<6;k++){
          int a=0;for(int j=0;j<K;j++)a+=coefficients[j]*flagval[p][k][j];
          if(a%5==0){zeros++;tangent=flag[p][k];}
        }
        if(zeros==6)continue; // geometrically singular at this rational point
        if(zeros!=1){fprintf(stderr,"flag error at %d %d\n",prefix,index);return 7;}
        covered |= lines[tangent];
      }
      int c=__builtin_popcount(covered);histogram[c]++;
      if(c>biggest){biggest=c;winners=0;}
      if(c==biggest)winners++;
    }
  }
  printf("max %d count %lld\n",biggest,winners);
  for(int i=0;i<32;i++)if(histogram[i])printf("hist %d %lld\n",i,histogram[i]);
  return 0;
}
