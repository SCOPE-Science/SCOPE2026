#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
static unsigned char patterns[512][22];
static unsigned char stackp[40][512];
static int k,n,T;
static unsigned long long counts[40], goods=0,prunes=0,pals=0,uni[32]={0};
static char repr[64],example[64];
static int indexof(int n) {
  int seen=0,arch=0;
  for(int i=0;i<n;i++) {
    seen |= 1 << (repr[i]-'0');
    if(seen==3) {arch++;seen=0;}
  }
  return arch;
}
static void rec(int depth) {
    counts[depth]++;
    int remain=n-depth;
    unsigned char *cur=stackp[depth];
    for(int i=0;i<T;i++) if (cur[i]+remain<2*k) {prunes++;return;}
    if(depth==n) {
      goods++;if(goods==1) {repr[n]=0;strcpy(example,repr);} 
      uni[indexof(n)]++;
      int pal=1;for(int i=0;i<n/2;i++) if(repr[i]!=repr[n-1-i]){pal=0;break;}
      pals+=pal;
      return;
    }
    unsigned char *nxt=stackp[depth+1];
    for(int bit=0;bit<2;bit++) {
        for(int i=0;i<T;i++) {
            unsigned char p=cur[i];
            nxt[i]=p+(p<2*k && patterns[i][p]==bit);
        }
        repr[depth]='0'+bit;
        rec(depth+1);
    }
}
int main(int argc,char **argv) {
    k=atoi(argv[1]);n=4*k-1; if(argc>2) n=atoi(argv[2]);T=1<<k;
    for(int i=0;i<T;i++)for(int j=0;j<k;j++) {int bit=(i>>(k-1-j))&1;patterns[i][j]=bit;patterns[i][j+k]=1-bit;}
    clock_t begin=clock(); rec(0);
    unsigned long long nodes=0;for(int i=0;i<=n;i++)nodes+=counts[i];
    printf("k=%d n=%d good=%llu nodes=%llu prunes=%llu first=%s pal=%llu orbit=%llu cpu=%.3f\n",k,n,goods,nodes,prunes,example,pals,(goods+pals)/4,(double)(clock()-begin)/CLOCKS_PER_SEC);
    printf("univ:");for(int i=0;i<=2*k;i++) if(uni[i]) printf(" %d:%llu",i,uni[i]);puts("");
    return 0;
}
