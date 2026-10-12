// Exact coset-leader distribution of RM_2(1,4) in the two-row block metric.
// Compile: g++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <algorithm>
using namespace std;
constexpr int variables=4, n=1<<variables, k=variables+1;
constexpr int red=n-k, syndrome_count=1<<red, states=1<<(2*red);
using Histogram=array<uint64_t,n+1>;
static void demand(bool condition,const char*what){if(!condition){fprintf(stderr,"FAILED: %s\n",what);exit(1);}}
int main(){
 const int piv[k]={0,1,2,4,8};
 bool isp[n]={}; for(int p:piv)isp[p]=true;
 int nonp[red],rankidx[n];fill(rankidx,rankidx+n,-1);
 for(int x=0,j=0;x<n;x++)if(!isp[x]){nonp[j]=x;rankidx[x]=j++;}
 array<uint16_t,n> parity_columns{};
 for(int x=0;x<n;x++)if(!isp[x]){
  const int bit=1<<rankidx[x];
  parity_columns[x]|=bit;
  if((__builtin_popcount((unsigned)x)&1)==0)parity_columns[0]|=bit;
  for(int i=0;i<variables;i++)if(x&(1<<i))parity_columns[1<<i]|=bit;
 }
 // Independent construction of all affine evaluation words.
 array<uint16_t,1<<k> affine{};
 for(int b=0;b<(1<<k);b++){
  uint16_t w=0;
  for(int x=0;x<n;x++)if(((b>>variables)&1) ^ (__builtin_popcount((unsigned)(b&x))&1))w|=1<<x;
  affine[b]=w;
 }
 for(int b=0;b<(1<<k);b++){
  uint16_t syn=0;
  for(int x=0;x<n;x++)if(affine[b]&(1<<x))syn^=parity_columns[x];
  demand(syn==0,"affine evaluation word must satisfy every parity check");
  for(int c=0;c<b;c++)demand(affine[b]!=affine[c],"affine codewords distinct");
 }
 for(int b=1;b<(1<<k);b++)demand(__builtin_popcount((unsigned)affine[b])>=8,"minimum distance is eight");
 // Algorithm A: 16 consecutive 4-choice syndrome convolutions.
 vector<uint8_t> dist(states,100),next(states);dist[0]=0;
 for(int x=0;x<n;x++){
  unsigned h=parity_columns[x],u=h,v=h<<red,w=u|v;
  for(unsigned s=0;s<(unsigned)states;s++){
   int z=dist[s]; z=min(z,int(dist[s^u])+1);
   z=min(z,int(dist[s^v])+1); z=min(z,int(dist[s^w])+1);
   next[s]=(uint8_t)z;
  }
  dist.swap(next);
 }
 Histogram a{};int radius=0,first_witness=-1;
 for(int s=0;s<states;s++){
  demand(dist[s]<=n,"all states covered");
  ++a[dist[s]];
  if(dist[s]>radius){radius=dist[s];first_witness=s;}
 }
 // Algorithm B: directly minimize a union of supports of two residual
 // words in the independent, explicit 32-word affine code.
 static uint16_t residual[syndrome_count][1<<k];
 uint8_t least[syndrome_count];
 for(int s=0;s<syndrome_count;s++){
  uint16_t canonical=0;
  for(int j=0;j<red;j++)if(s&(1<<j))canonical|=1<<nonp[j];
  int small=n;
  for(int b=0;b<(1<<k);b++){
   uint16_t w=canonical^affine[b];
   residual[s][b]=w;
   small=min(small,__builtin_popcount((unsigned)w));
  }
  least[s]=(uint8_t)small;
 }
 Histogram b{};
 for(int u=0;u<syndrome_count;u++)for(int v=0;v<syndrome_count;v++){
  int smallest=n,lower=max(least[u],least[v]);
  for(int i=0;i<(1<<k)&&smallest>lower;i++){
   uint16_t aword=residual[u][i];
   if(__builtin_popcount((unsigned)aword)>=smallest)continue;
   for(int j=0;j<(1<<k);j++){
    smallest=min(smallest,__builtin_popcount((unsigned)(aword|residual[v][j])));
    if(smallest==lower)break;
   }
  }
  demand(smallest==dist[u|(v<<red)],"discrepancy in direct coset minimization");
  ++b[smallest];
 }
 demand(a==b,"independent histograms disagree");
 const Histogram expected={1,48,1080,15120,144585,858144,2359602,798000,17388,336,0,0,0,0,0,0,0};
 demand(a==expected,"unexpected distance histogram");
 demand(accumulate(a.begin(),a.end(),uint64_t(0))==(uint64_t)states,"invalid coset total");
 demand(radius==9,"radius mismatch");
 demand(first_witness==424309,"witness syndrome mismatch");
 printf("VERIFY_OK\n");
 printf("code=[16,5,8]_2; number_of_two_row_cosets=%d\n",states);
 printf("R_2=9; distance_9_cosets=%llu; witness_syndrome=(%d,%d)\n",(unsigned long long)a[9],first_witness&(syndrome_count-1),first_witness>>red);
 printf("distribution=");for(int i=0;i<=9;i++)printf("%s%llu",i?",":"",(unsigned long long)a[i]);printf("\n");
 return 0;
}
