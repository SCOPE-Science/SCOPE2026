#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <vector>
#include <map>
#include <array>
#include <algorithm>
using namespace std;
// Direct three-state vertex-wise dynamics; exhaustive first-entry and eventual-period census.
static uint32_t step(uint32_t s,int d,const vector<uint32_t>& weight){
 int n=1<<d;uint8_t a[16],b[16];
 for(int v=0;v<n;v++){a[v]=s%3;s/=3;}
 for(int v=0;v<n;v++){
  if(a[v]==1)b[v]=2;
  else if(a[v]==2)b[v]=0;
  else {b[v]=0;for(int i=0;i<d;i++)if(a[v^(1<<i)]==1){b[v]=1;break;}}
 }
 uint32_t y=0;for(int v=0;v<n;v++)y+=b[v]*weight[v];return y;
}
int main(int argc,char**argv){
 int d=argc>1?atoi(argv[1]):4, n=1<<d;
 vector<uint32_t> weight(n+1,1);for(int v=0;v<n;v++)weight[v+1]=3*weight[v];
 uint32_t N=weight[n];vector<uint8_t> status(N),entry(N),period(N);vector<uint32_t> path;
 map<pair<int,int>,uint64_t> counts;
 for(uint32_t i=0;i<N;i++){
  if(status[i])continue;
  path.clear();uint32_t z=i;
  while(!status[z]){status[z]=1;path.push_back(z);z=step(z,d,weight);}
  int j=int(path.size())-1;
  if(status[z]==1){
   int c=0;for(int k=j;k>=0;k--){c++;if(path[k]==z)break;}
   int cut= int(path.size())-c;
   for(int k=cut;k<int(path.size());k++){
    uint32_t x=path[k];status[x]=2;entry[x]=0;period[x]=c;counts[{0,c}]++;
   }
   j=cut-1;
  }
  for(int k=j;k>=0;k--){
   uint32_t x=path[k],next=step(x,d,weight);
   status[x]=2;period[x]=period[next];entry[x]=entry[next]+1;
   if(entry[x]<entry[next]){puts("ERROR: entry distance overflow");return 3;}
   counts[{entry[x],period[x]}]++;
  }
 }
 printf("BASINS d=%d states=%u\n",d,N);
 for(auto& kv:counts)printf("entrance=%d eventual_period=%d states=%llu\n",kv.first.first,kv.first.second,(unsigned long long)kv.second);
}
