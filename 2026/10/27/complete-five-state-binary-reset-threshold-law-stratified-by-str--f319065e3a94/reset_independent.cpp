#include <cstdio>
#include <cstdint>
#include <cstring>
using namespace std;

// Separate implementation: breadth expansion by exact word length
// (not a BFS queue). Strong connectivity by Floyd--Warshall reachability.
static uint8_t tabs[3125][5];
static uint8_t ims[3125][32];

int main(){
 for(int t=0;t<3125;t++){
   int n=t;for(int i=0;i<5;i++){tabs[t][i]=n%5;n/=5;}
   for(int s=1;s<32;s++){
    int v=0;
    for(int i=0;i<5;i++) if(s&(1<<i)) v|=1<<tabs[t][i];
    ims[t][s]=v;
   }
 }
 long long hist[17][2]={0};
 long long nonsync[2]={0};
 long long moment[2]={0};
 int maxdist=0; long long maxct=0;
 const uint32_t singletons=(1u<<1)|(1u<<2)|(1u<<4)|(1u<<8)|(1u<<16);
 for(int a=0;a<3125;a++)for(int b=0;b<3125;b++){
   uint8_t conn[5];
   for(int i=0;i<5;i++)conn[i]=(1<<i)|(1<<tabs[a][i])|(1<<tabs[b][i]);
   for(int k=0;k<5;k++)for(int i=0;i<5;i++)if(conn[i]&(1<<k))conn[i]|=conn[k];
   bool sc=true;for(int i=0;i<5;i++)if(conn[i]!=31)sc=false;
   uint32_t achieved=1u<<31, frontier=achieved;
   int answer=0;
   for(int length=1;length<=31;length++){
      uint32_t layer=0;
      uint32_t t=frontier;
      while(t){int s=__builtin_ctz(t);t&=t-1;layer|=1u<<ims[a][s];layer|=1u<<ims[b][s];}
      if(layer&singletons){answer=length;break;}
      frontier=layer &~ achieved;
      achieved|=layer;
      if(!frontier)break;
   }
   if(answer>0){
      if(answer>16){fprintf(stderr,"ERROR length exceeds 16\n");return 2;}
      hist[answer][sc]++;moment[sc]+=answer;
      if(answer>maxdist){maxdist=answer;maxct=1;}else if(answer==maxdist)maxct++;
   }else nonsync[sc]++;
 }
 printf("MAX=%d MAX_COUNT=%lld\n",maxdist,maxct);
 for(int i=1;i<=16;i++)printf("H[%d]=%lld,%lld\n",i,hist[i][0],hist[i][1]);
 printf("NONSYNC_NONSC=%lld NONSYNC_SC=%lld\n",nonsync[0],nonsync[1]);
 printf("MOMENT_NONSC=%lld MOMENT_SC=%lld\n",moment[0],moment[1]);
}
