/* Exact three-symbol cyclic weight enumerators for the binary length-32 ideal chain.
   Low-index codes use Hasse-syndrome transfer states;
   the remaining codes use exhaustive message enumeration.
   Requires only ISO C11 and SPECTRUM.csv in the working directory. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define N 32
#define R 11
#define S (1<<R)
#define W (N+1)
#define IDX(s,p,w) ((((size_t)(s)*4)+(p))*W+(w))
static uint64_t hist[N+1][W];
static uint64_t *dp,*nxt;
static unsigned col[N];
static int bits(uint32_t x){int n=0;while(x){x&=x-1;n++;}return n;}
static int w3(uint32_t x){return bits(x|(x>>1)|(x<<31)|(x>>2)|(x<<30));}
int main(){
 for(int k=0;k<N;k++)for(int j=0;j<R;j++)if((k&j)==j)col[k]|=1u<<j;
 size_t L=(size_t)S*4*W;
 dp=calloc(L,8);nxt=calloc(L,8); if(!dp||!nxt)return 1;
 uint64_t h0[S][W];memset(h0,0,sizeof(h0));
 for(int b0=0;b0<2;b0++)for(int b1=0;b1<2;b1++){
  memset(dp,0,L*8);int syn=(b0?col[0]:0)^(b1?col[1]:0);dp[IDX(syn,b0*2+b1,0)]=1;
  for(int k=2;k<N;k++){
   memset(nxt,0,L*8);
   for(int s=0;s<S;s++) for(int p=0;p<4;p++){
    int np0=((p&1)<<1), np1=np0|1;
    int add0=(p!=0),add1=1; // older/newer plus new b
    uint64_t *in=dp+IDX(s,p,0); uint64_t *o0=nxt+IDX(s,np0,0);uint64_t *o1=nxt+IDX(s^col[k],np1,0);
    for(int w=0;w<=k-2;w++){uint64_t v=in[w];if(v){o0[w+add0]+=v;o1[w+add1]+=v;}}
   }
   uint64_t *tmp=dp;dp=nxt;nxt=tmp;
  }
  for(int s=0;s<S;s++)for(int p=0;p<4;p++){
   int older=p>>1,newer=p&1;
   int wrap=(older|newer|b0?1:0)+(newer|b0|b1?1:0);
   uint64_t *in=dp+IDX(s,p,0);
   for(int w=0;w<=N-2;w++) if(in[w])h0[s][w+wrap]+=in[w];
  }
 }
 for(int s=0;s<S;s++)for(int w=0;w<=N;w++)if(h0[s][w]){
  for(int i=0;i<=R;i++) if((s&((1<<i)-1))==0)hist[i][w]+=h0[s][w];
 }
 free(dp);free(nxt);
 for(int i=R+1;i<=N;i++){
  if(i==N){hist[i][0]=1;continue;}
  int dim=N-i;uint32_t g=0;
  for(int j=0;j<=i;j++)if((j&i)==j)g|=1u<<j;
  uint32_t code=0;int prev=0;
  for(int x=0;x<(1<<dim);x++){
   int gray=x^(x>>1); if(x){uint32_t t=(uint32_t)(gray^prev);int bit=0;while(!(t&1u)){bit++;t>>=1;}code^=g<<bit;} prev=gray;
   hist[i][w3(code)]++;
  }
 }
 FILE *f=fopen("SPECTRUM.csv","r"); if(!f){perror("SPECTRUM.csv");return 2;}
 char head[1024]; if(!fgets(head,sizeof head,f)){puts("MISSING_HEADER");return 3;}
 for(int i=0;i<=N;i++){
  int index,dimension;unsigned d,m; unsigned long long x;
  if(fscanf(f,"%d,%d,%u,%u",&index,&dimension,&d,&m)!=4 || index!=i || dimension!=N-i){puts("ROW_ERROR");return 4;}
  int min=0;unsigned long long mult=0,total=0;
  for(int w=0;w<=N;w++){
   if(fscanf(f,",%llu",&x)!=1 || x!=hist[i][w]){printf("COEFF_MISMATCH %d %d\n",i,w);return 5;}
   total+=hist[i][w]; if(w && hist[i][w] && !min){min=w;mult=hist[i][w];}
  }
  if(min!=(int)d || mult!=m || total!=(1ULL<<(N-i))){printf("SUMMARY_MISMATCH %d\n",i);return 6;}
  int c=fgetc(f); if(c=='\r')c=fgetc(f);if(c!='\n' && c!=EOF){puts("TRAILING_ERROR");return 7;}
 }
 fclose(f);puts("VERIFY_OK");return 0;
}
