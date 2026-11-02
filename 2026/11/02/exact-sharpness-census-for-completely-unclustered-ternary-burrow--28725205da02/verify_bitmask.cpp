// Independent bit-decision enumeration of completely unclustered ternary BWT images.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <chrono>
using namespace std;
static int w[33], at[3][33], cnt[3];
int main(int argc,char** argv){
 int lo=(argc>1?atoi(argv[1]):13),hi=(argc>2?atoi(argv[2]):30);
 for(int n=lo;n<=hi;n++){
  long long answer=0;
  uint64_t total=(1ULL<<(n-1));
  for(uint64_t m=0;m<total;m++){
   for(int first=0;first<3;first++){
    memset(cnt,0,sizeof(cnt));
    w[0]=first;at[first][cnt[first]++]=0;
    for(int i=1;i<n;i++){w[i]=(w[i-1]+1+((m>>(i-1))&1))%3;at[w[i]][cnt[w[i]]++]=i;}
    const int half=(n+1)/2;
    int mismatch=0, p=0;
    for(int a=0;a<3;a++)for(int j=0;j<cnt[a];j++,p++) mismatch+=(w[p]!=a);
    if(mismatch!=half)continue;
    int piInv[33], idx=0;
    for(int a=0;a<3;a++)for(int j=0;j<cnt[a];j++)piInv[idx++]=at[a][j];
    int x=0, steps=0;
    do {x=piInv[x];++steps;}while(x && steps<n);
    if(steps==n)answer++;
   }
  }
  printf("%d %lld\n",n,answer);fflush(stdout);
 }
}
