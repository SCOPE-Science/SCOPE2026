#include <cstdio>
#include <cstdint>
#include <cstring>
#include <map>
#include <array>
using namespace std;
constexpr int M=3125;
static uint8_t inverse[M][32];
static uint64_t bylength[32]={},unique[32]={}, sumwords[32]={};
static map<unsigned, uint64_t> bynumber;
static uint64_t nonsync=0,extremal=0;static unsigned maxways=0;
int main(){
  for(int i=0;i<M;i++){
    int t[5],v=i;
    for(int s=0;s<5;s++){t[s]=v%5;v/=5;}
    for(int mask=0;mask<32;mask++){
      int ans=0;
      for(int s=0;s<5;s++)if(mask>>t[s]&1)ans|=1<<s;
      inverse[i][mask]=ans;
    }
  }
  for(int ai=0;ai<M;ai++)for(int bi=0;bi<M;bi++){
    int8_t depth[32];memset(depth,-1,sizeof(depth));
    unsigned ways[32]={};
    int queue[32],h=0,n=0;
    for(int i=0;i<5;i++){int mask=1<<i;queue[n++]=mask;depth[mask]=0;ways[mask]=1;}
    while(h<n){
      int mask=queue[h++];
      for(int letter=0;letter<2;letter++){
        int successor=letter==0?inverse[ai][mask]:inverse[bi][mask];
        if(successor==0)continue;
        if(depth[successor]<0){depth[successor]=depth[mask]+1;ways[successor]=ways[mask];queue[n++]=successor;}
        else if(depth[successor]==depth[mask]+1){ways[successor]+=ways[mask];}
      }
    }
    if(depth[31]<0){nonsync++;continue;}
    int len=depth[31], w=ways[31];
    bylength[len]++;sumwords[len]+=w;bynumber[w]++;
    if(w==1)unique[len]++;
    if(w>maxways){maxways=w;extremal=1;}
    else if(w==maxways)extremal++;
  }
  printf("NONSYNC %llu MAX %u EXTREMAL %llu\n",(unsigned long long)nonsync,maxways,(unsigned long long)extremal);
  for(int k=1;k<32;k++)if(bylength[k])printf("LEN %d COUNT %llu UNIQUE %llu SUMWORDS %llu\n",k,(unsigned long long)bylength[k],(unsigned long long)unique[k],(unsigned long long)sumwords[k]);
  for(auto [w,count]:bynumber)printf("MULT %u COUNT %llu\n",w,(unsigned long long)count);
}
