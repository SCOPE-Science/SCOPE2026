#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static uint8_t patt[256][32], progress[33][256], word[32];
static unsigned long long dist[32], checked=0, accepted=0;
static int k,np;
static void recurse(int depth,int z,int o){
  if(depth==2*k){
    checked++;
    for(int i=0;i<np;i++)if(progress[depth][i]!=k)return;
    accepted++;
    int a=0,seen=0;
    for(int i=0;i<depth;i++){
      seen|=1<<word[i];
      if(seen==3){a++;seen=0;}
    }
    dist[a]++;
    return;
  }
  for(int b=0;b<2;b++){
    if(b==0 && z==k)continue;
    if(b==1 && o==k)continue;
    if(depth==0 && b==1)continue; // complement pairing; every accepted word has a nonconstant first symbol.
    int rem=2*k-(depth+1);
    int ok=1;
    for(int i=0;i<np;i++){
      uint8_t m=progress[depth][i];
      m+=(m<k && patt[i][m]==b);
      progress[depth+1][i]=m;
      if(m+rem<k){ok=0;break;}
    }
    if(!ok)continue;
    word[depth]=b;
    recurse(depth+1,z+(b==0),o+(b==1));
  }
}
int main(int argc,char**argv){
  if(argc!=2)return 2;
  k=atoi(argv[1]);if(k<1||k>15)return 2;
  np=1<<((k+1)/2);
  for(int i=0;i<np;i++)for(int j=0;j<k;j++){
    int b=j<((k+1)/2)?j:k-1-j;
    patt[i][j]=(i>>(((k+1)/2)-1-b))&1;
  }
  recurse(0,0,0);
  unsigned long long total=0;
  for(int i=0;i<=k;i++)total+=dist[i];
  printf("k=%d checked_half=%llu accepted_half=%llu total=%llu classes",k,checked,accepted,2*total);
  for(int i=0;i<=k;i++)if(dist[i])printf(" iota_%d=%llu",i,2*dist[i]);
  puts("");
  return 0;
}
