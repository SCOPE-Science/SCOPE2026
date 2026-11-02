#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <vector>
#include <array>
#include <map>
#include <algorithm>
using namespace std;
// Independent direct vertex-wise implementation, no bitboard/neighborhood-image lookup.
static uint32_t step(uint32_t s, int d, const vector<uint32_t>& radix){
 const int n=1<<d;
 uint8_t a[16], b[16];uint32_t tmp=s;
 for(int v=0;v<n;v++){a[v]=tmp%3;tmp/=3;}
 for(int v=0;v<n;v++){
   if(a[v]==1)b[v]=2;
   else if(a[v]==2)b[v]=0;
   else { b[v]=0;for(int i=0;i<d;i++)if(a[v^(1<<i)]==1){b[v]=1;break;} }
 }
 uint32_t out=0;for(int v=0;v<n;v++)out+=radix[v]*b[v];return out;
}
int main(int argc,char**argv){
 int d=argc>1?atoi(argv[1]):4;int n=1<<d;
 vector<uint32_t> radix(n+1,1);for(int i=0;i<n;i++)radix[i+1]=radix[i]*3;
 uint32_t N=radix[n];vector<uint8_t> color(N);vector<uint32_t> path;map<unsigned long long,unsigned long long> cnt;
 for(uint32_t root=0;root<N;root++){
  if(color[root])continue;
  uint32_t cur=root;path.clear();
  while(!color[cur]){
    color[cur]=1;path.push_back(cur);cur=step(cur,d,radix);
  }
  if(color[cur]==1){
    unsigned long long len=0;
    for(int j=int(path.size())-1;j>=0;j--){len++;if(path[j]==cur)break;}
    cnt[len]++;
  }
  for(uint32_t s:path)color[s]=2;
 }
 printf("INDEPENDENT d=%d N=%u",d,N);
 for(auto& v:cnt)printf(" P%llu=%llu",v.first,v.second);
 printf("\n");
}
