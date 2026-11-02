#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
static int lyndon(uint32_t code,int k){
 if(k==1)return 1;
 uint32_t mask=(1U<<k)-1U, x=code&mask;
 if ((x&(1u<<(k-1))) || !(x&1U)) return 0;
 for(int j=1;j<k;j++){
  uint32_t y=((x<<j)&mask)|(x>>(k-j));
  if(y<=x)return 0;
 }
 return 1;
}
int main(int argc,char**argv){int N=argc>1?atoi(argv[1]):18; if(N<1||N>22)return 2;
 uint32_t siz=1U<<(N+1),*stamp=calloc(siz,sizeof(uint32_t)),*list=malloc(siz*sizeof(uint32_t));
 uint8_t *isly=calloc(siz,sizeof(uint8_t));
 if(!stamp||!list||!isly)return 3;
 for(int k=1;k<=N;k++)for(uint32_t bits=0;bits<(1U<<k);bits++)isly[(1U<<k)|bits]=lyndon((1U<<k)|bits,k);
 uint32_t next_tag=0;
 for(int n=1;n<=N;n++){
  uint32_t limit=1U<<n,mx=0,best=0,totbest=0; uint64_t sum=0;
  for(uint32_t x=0;x<limit;x++){
   uint32_t sz=1;list[0]=1;uint32_t tag=++next_tag,cnt=0;stamp[1]=tag;
   for(int i=n-1;i>=0;i--){uint32_t b=(x>>i)&1U,old=sz;
    for(uint32_t j=0;j<old;j++){
     uint32_t z=(list[j]<<1)|b;
     if(stamp[z]!=tag){stamp[z]=tag;list[sz++]=z;cnt+=isly[z];}
    }
   }
   sum+=cnt;
   if(cnt>mx){mx=cnt;best=x;totbest=1;}
   else if(cnt==mx)totbest++;
  }
  printf("n=%d max=%u first=",n,mx);
  for(int i=n-1;i>=0;i--)putchar('0'+((best>>i)&1U));
  printf(" nmax=%u sum=%llu\n",totbest,(unsigned long long)sum);fflush(stdout);
 }
 free(stamp);free(list);free(isly);return 0;
}
