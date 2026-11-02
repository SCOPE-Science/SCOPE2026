#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
// Exhaustive labelled Q_d Greenberg--Hastings 3-state threshold-one census.
// Every state is a radix-3 word, one trit per bit-vector vertex.
int main(int argc,char**argv){
 int d=(argc>=2?atoi(argv[1]):4),n=1<<d;
 if(d<1 || d>4)return 2;
 vector<uint32_t> pow3(n+1,1);
 for(int i=0;i<n;i++)pow3[i+1]=pow3[i]*3;
 uint32_t N=pow3[n], bsize=pow3[n/2];
 vector<uint16_t> oneL(bsize),twoL(bsize);
 for(uint32_t s=0;s<bsize;s++){
  uint32_t x=s;
  for(int v=0;v<n/2;v++){
   int t=x%3; x/=3;
   if(t==1)oneL[s]|=(1u<<v);
   else if(t==2)twoL[s]|=(1u<<v);
  }
 }
 vector<uint32_t> score(1u<<n);vector<uint16_t> neighbors(1u<<n);
 for(uint32_t mask=1;mask<(1u<<n);mask++){
  uint32_t bit=__builtin_ctz(mask),prev=mask&(mask-1);
  score[mask]=score[prev]+pow3[bit];
  uint16_t nb=0;
  for(int j=0;j<d;j++)nb|=(1u<<(bit^(1<<j)));
  neighbors[mask]=neighbors[prev]|nb;
 }
 vector<uint8_t> state(N,0);
 vector<uint32_t> path;
 map<int,uint64_t> cycles,states,examples;
 uint32_t max_path=0;
 for(uint32_t root=0;root<N;root++){
  if(state[root])continue;
  path.clear();uint32_t s=root;
  while(state[s]==0){
   state[s]=1;path.push_back(s);
   uint32_t lo=s%bsize,hi=s/bsize;
   uint16_t a=oneL[lo]|(oneL[hi]<<(n/2));
   uint16_t b=twoL[lo]|(twoL[hi]<<(n/2));
   uint16_t e=neighbors[a] & ~uint16_t(a|b);
   s=score[e]+2*score[a];
  }
  if(state[s]==1){
   int len=1;
   for(int idx=int(path.size())-1;path[idx]!=s;idx--)len++;
   cycles[len]++;
   states[len]+=len;
   if(!examples.count(len))examples[len]=s;
  }
  for(uint32_t x:path)state[x]=2;
  max_path=max<uint32_t>(max_path,path.size());
 }
 printf("d=%d vertices=%d total_states=%u max_exploration_path=%u\n",d,n,N,max_path);
 for(auto& kv:cycles)printf("primitive_period=%d orbit_count=%llu periodic_states=%llu witness_radix3=%llu\n",kv.first,(unsigned long long)kv.second,(unsigned long long)states[kv.first],(unsigned long long)examples[kv.first]);
}
