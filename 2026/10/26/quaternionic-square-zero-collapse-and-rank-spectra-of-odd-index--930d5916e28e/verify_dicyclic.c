/* Standalone exhaustive finite checks for the mathematical group-algebra
   and chain-ring square-zero rank formulas. No external dependencies. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <string.h>

static uint64_t binom_q2_expected[13]={1,1,15,9,140,78,708,168,2016,384,3648,0,3072};
static int multiplication_index(int i,int j,int m){
  int n=4*m, a=i%n, b=i/n, c=j%n,d=j/n;
  int v=(a+(b?-c:c)+2*m*b*d)%n;
  if(v<0)v+=n;
  return v+n*((b+d)&1);
}
static int check_binary_group(int m){
  int n=8*m; if(n>24)return 0;
  uint32_t cols[24][24],comm[24][24],deriv[24],y=0;
  uint64_t hist[25]={0};hist[0]=1;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)cols[i][j]=1u<<multiplication_index(i,j,m);
  for(int i=0;i<n;i++){
    deriv[i]=cols[i][i];
    for(int j=0;j<n;j++)comm[i][j]=cols[i][j]^cols[j][i];
  }
  for(uint32_t k=1;k<(1u<<n);k++){
    int i=__builtin_ctz(k);y^=deriv[i];
    for(int j=0;j<n;j++)deriv[j]^=comm[j][i];
    if(y)continue;
    uint32_t xx=k^(k>>1),v[24];
    for(int j=0;j<n;j++){
      uint32_t r=0,t=xx;
      while(t){int h=__builtin_ctz(t);t&=t-1;r^=cols[h][j];}
      v[j]=r;
    }
    int rk=0;
    for(int c=0;c<n;c++){
      int row=rk;while(row<n && ((v[row]>>c)&1u)==0)row++;
      if(row==n)continue;
      uint32_t tmp=v[row];v[row]=v[rk];v[rk]=tmp;
      for(int j=rk+1;j<n;j++)if((v[j]>>c)&1u)v[j]^=v[rk];
      rk++;
    }
    hist[rk]++;
  }
  if(m==1){uint64_t ans[9]={1,1,6,0,8};for(int i=0;i<=8;i++)if(hist[i]!=ans[i])return 0;}
  else if(m==3){for(int i=0;i<=24;i++){
    uint64_t want=i<=12?binom_q2_expected[i]:0;
    if(hist[i]!=want){fprintf(stderr,"Q24 rank %d: got %"PRIu64" expected %"PRIu64"\n",i,hist[i],want);return 0;}
  }}
  else return 0;
  uint64_t sum=0;for(int i=0;i<=n;i++)sum+=hist[i];
  printf("DIRECT_GROUP_GF2_OK m=%d total=%"PRIu64" max-rank=%"PRIu64"\n",m,sum,hist[n/2]);
  return 1;
}
static uint8_t mul4(uint8_t x,uint8_t y){
  uint8_t p=0;
  while(y){if(y&1)p^=x;y>>=1;x<<=1;if(x&4)x^=7;}
  return p;
}
static int gf4_group(void){
  int mm[8][8];for(int i=0;i<8;i++)for(int j=0;j<8;j++)mm[i][j]=multiplication_index(i,j,1);
  int inv[4]={0,1,3,2};uint64_t hist[9]={0};
  for(unsigned x=0;x<(1u<<16);x++){
    uint8_t a[8],sq[8]={0};unsigned t=x;
    for(int i=0;i<8;i++){a[i]=t&3;t>>=2;}
    for(int i=0;i<8;i++)for(int j=0;j<8;j++)sq[mm[i][j]]^=mul4(a[i],a[j]);
    int ok=1;for(int i=0;i<8;i++)if(sq[i]){ok=0;break;}if(!ok)continue;
    uint8_t v[8][8];for(int i=0;i<8;i++)for(int j=0;j<8;j++)v[i][j]=0;
    for(int j=0;j<8;j++)for(int i=0;i<8;i++)v[j][mm[i][j]]^=a[i];
    int rk=0;
    for(int c=0;c<8;c++){
      int row=rk;while(row<8 && !v[row][c])row++;
      if(row==8)continue;
      for(int h=0;h<8;h++){uint8_t tmp=v[row][h];v[row][h]=v[rk][h];v[rk][h]=tmp;}
      uint8_t s=inv[v[rk][c]];
      for(int h=c;h<8;h++)v[rk][h]=mul4(v[rk][h],s);
      for(int j=rk+1;j<8;j++)if(v[j][c]){uint8_t f=v[j][c];for(int h=c;h<8;h++)v[j][h]^=mul4(f,v[rk][h]);}
      rk++;
    }
    hist[rk]++;
  }
  uint64_t want[9]={1,3,60,0,192};for(int i=0;i<9;i++)if(hist[i]!=want[i])return 0;
  printf("DIRECT_GROUP_GF4_OK m=1 total=256 max-rank=192\n");return 1;
}
static unsigned pmul(unsigned a,unsigned b){unsigned c=0;
  for(int i=0;i<4;i++)if((a>>i)&1)for(int j=0;i+j<4;j++)if((b>>j)&1)c^=1u<<(i+j);
  return c;
}
static int chain_matrix(void){
  uint64_t hist[9]={0};
  for(unsigned a=0;a<16;a++)for(unsigned b=0;b<16;b++)for(unsigned c=0;c<16;c++)for(unsigned d=0;d<16;d++){
    if((pmul(a,a)^pmul(b,c)) || (pmul(a,b)^pmul(b,d)) || (pmul(c,a)^pmul(d,c)) ||(pmul(c,b)^pmul(d,d)))continue;
    uint16_t vec[8];
    for(int j=0;j<8;j++){
      unsigned u=j%4,src=j/4,r0,r1;
      if(src==0){r0=(pmul(a,1u<<u));r1=pmul(c,1u<<u);}else{r0=pmul(b,1u<<u);r1=pmul(d,1u<<u);}
      vec[j]=(uint16_t)(r0+(r1<<4));
    }
    int rank=0;
    for(int k=0;k<8;k++){
      int row=rank;while(row<8 && !((vec[row]>>k)&1))row++;
      if(row==8)continue;
      uint16_t t=vec[row];vec[row]=vec[rank];vec[rank]=t;
      for(int j=rank+1;j<8;j++)if((vec[j]>>k)&1)vec[j]^=vec[rank];
      rank++;
    }
    hist[rank]++;
  }
  uint64_t want[9]={1,9,78,168,384};
  for(int i=0;i<9;i++)if(hist[i]!=want[i]){fprintf(stderr,"CHAIN rank %d: %"PRIu64" vs %"PRIu64"\n",i,hist[i],want[i]);return 0;}
  printf("DIRECT_CHAIN_GF2_OK length=4 total=640 max-rank=384\n");return 1;
}
int main(void){
 if(!check_binary_group(1)||!gf4_group()||!chain_matrix()||!check_binary_group(3)){puts("CHECK_FAILED");return 1;}
 puts("QUATERNION_DICYCLIC_CHECK_OK");return 0;
}
