/* Exhaustive checker for the opposite two-run common-supersequence spectrum. */
#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
static int emb(uint32_t w,int L,int m,int first){int part=0,c=0;for(int k=0;k<L;k++){int b=(w>>k)&1;if(part==0&&b==first){if(++c==m){part=1;c=0;}}else if(part==1&&b!=first){if(++c==m)return 1;}}return 0;}
static int common(uint32_t w,int L,int m){return emb(w,L,m,0)&&emb(w,L,m,1);}
static int minimal(uint32_t w,int L,int m){if(!common(w,L,m))return 0;for(int k=0;k<L;k++){uint32_t x=(w&((1U<<k)-1U))|((w>>(k+1))<<k);if(common(x,L-1,m))return 0;}return 1;}
static int form(uint32_t w,int L,int m,int flip){int z=0,o=0,left=-1,right=-1;for(int k=0;k<L;k++){int b=((w>>k)&1)^flip;if(!b){z++;if(z==m)left=k;if(z==m+1)right=k;}else o++;}if(z!=2*m||o<m||o>=2*m||left<0||right<0)return 0;int gap=right-left-1,p=0,s=0;if(gap<1||gap>m)return 0;for(int k=0;k<left;k++)if((((w>>k)&1)^flip)==1)p++;for(int k=right+1;k<L;k++)if((((w>>k)&1)^flip)==1)s++;return p==m-gap&&s==m-gap;}
static uint64_t binom(int a,int b){uint64_t r=1;for(int i=1;i<=b;i++)r=r*(a-b+i)/(uint64_t)i;return r;}
int main(void){uint64_t seen=0,found_total=0;for(int m=1;m<=5;m++)for(int L=2*m;L<=4*m;L++){uint64_t cnt=0,exp=0;if(L>=3*m&&L<4*m){int j=L-3*m;uint64_t b=binom(m+j-1,j);exp=2*b*b;}for(uint32_t w=0;w<(1U<<L);w++){int a=minimal(w,L,m),b=form(w,L,m,0)||form(w,L,m,1);if(a!=b){fprintf(stderr,"mismatch m=%d L=%d word=%u\n",m,L,w);return 2;}cnt+=a;}if(cnt!=exp){fprintf(stderr,"count mismatch m=%d L=%d\n",m,L);return 3;}seen+=(uint64_t)1<<L;found_total+=cnt;printf("m=%d L=%d count=%"PRIu64"\n",m,L,cnt);}printf("VERIFY_OK objects=%"PRIu64" minimum_supersequences=%"PRIu64" n<=5\n",seen,found_total);return 0;}
