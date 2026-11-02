#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
/* Independent literal verification: test each full host against each target by scanning its bits. */
static int matches(unsigned int bits, int n, unsigned int x, int k) {
  int p=0;
  for(int j=n-1;j>=0 && p<2*k;j--){
    int ch=(bits>>j)&1;
    int wanted=(x>>(k-1-(p%k)))&1;
    if(p>=k) wanted^=1;
    if(ch==wanted)p++;
  }
  return p==2*k;
}
static int univ(unsigned int bits,int n){int seen=0,v=0;for(int j=n-1;j>=0;j--){seen|=1<<((bits>>j)&1);if(seen==3){seen=0;v++;}}return v;}
static int pal(unsigned int bits,int n){for(int i=0;i<n/2;i++)if(((bits>>i)&1)!=((bits>>(n-1-i))&1)) return 0;return 1;}
int main(int argc,char **argv) {
 int limit=argc>1?atoi(argv[1]):5;
 for(int k=1;k<=limit;k++) {
  for(int n=4*k-2;n<=4*k-1;n++){
   uint64_t cnt=0,ps=0,u[32]={0};
   for(unsigned int w=0;w<(1u<<n);w++){
    int good=1;
    for(unsigned int x=0;x<(1u<<k);x++)if(!matches(w,n,x,k)){good=0;break;}
    if(good){cnt++;ps+=pal(w,n);u[univ(w,n)]++;}
   }
   printf("literal k=%d n=%d good=%llu pal=%llu",k,n,(unsigned long long)cnt,(unsigned long long)ps);
   for(int i=0;i<=2*k;i++)if(u[i])printf(" %d:%llu",i,(unsigned long long)u[i]);puts("");fflush(stdout);
  }
 }
}
