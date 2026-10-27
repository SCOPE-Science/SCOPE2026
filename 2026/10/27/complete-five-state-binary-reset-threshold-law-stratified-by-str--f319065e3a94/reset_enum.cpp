#include <cstdio>
#include <cstdint>
using namespace std;

// Complete enumeration of ordered pairs of maps on five labeled states.
// Minimal reset length via breadth-first search of reachable image sets.
// Strong connectivity via two independent reachability searches, original and transpose.
static uint8_t image[3125][32];
static uint8_t maps[3125][5];
static bool connected(int a, int b) {
    uint8_t forward=1,reverse=1;
    for(int pass=0;pass<5;pass++) {
        for(int i=0;i<5;i++) {
            if(forward&(1<<i))
                forward |= (1<<maps[a][i]) | (1<<maps[b][i]);
            if((reverse&(1<<maps[a][i])) || (reverse&(1<<maps[b][i])))
                reverse |= 1<<i;
        }
    }
    return forward==31 && reverse==31;
}
int main(){
 for(int v=0;v<3125;v++){
   int x=v;
   for(int i=0;i<5;i++){maps[v][i]=x%5;x/=5;}
   for(int s=1;s<32;s++){
     int l=__builtin_ctz((unsigned)s);
     image[v][s]=image[v][s&(s-1)]|(1<<maps[v][l]);
   }
 }
 long long hist[34][2]={0}, nonsync[2]={0}, moment[2]={0};
 for(int a=0;a<3125;a++) for(int b=0;b<3125;b++){
  int sc=connected(a,b)?1:0;
  uint32_t seen=1u<<31;
  uint8_t queue[32],dist[32];
  int head=0,tail=1; queue[0]=31;dist[0]=0;
  int answer=0;
  while(head<tail){
   int s=queue[head],depth=dist[head++];
   if ((s&(s-1))==0){answer=depth;break;}
   for(int c=0;c<2;c++){
    int t=image[c?b:a][s];
    if(!(seen&(1u<<t))){seen|=1u<<t;queue[tail]=t;dist[tail++]=depth+1;}
   }
  }
  if(answer==0) nonsync[sc]++;
  else{hist[answer][sc]++;moment[sc]+=answer;}
 }
 for(int i=1;i<=16;i++)printf("H[%d]=%lld,%lld\n",i,hist[i][0],hist[i][1]);
 printf("NONSYNC_NONSC=%lld NONSYNC_SC=%lld\n",nonsync[0],nonsync[1]);
 printf("MOMENT_NONSC=%lld MOMENT_SC=%lld\n",moment[0],moment[1]);
}
