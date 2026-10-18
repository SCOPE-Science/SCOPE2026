#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;
using M=uint32_t;
constexpr int N=27;
const M FULL=(M(1)<<N)-1;
array<M,N> compatible;
array<array<int,N>,8> gen;
int encode(int a,int b,int c){return 9*a+3*b+c;}
void init(){
 for(int i=0;i<N;++i){int a=i/9,b=(i/3)%3,c=i%3;
  for(int t=0;t<N;++t){int x=t/9,y=(t/3)%3,z=t%3;
    if(a==x||b==y||c==z)compatible[i]|=M(1)<<t;}}
 for(int i=0;i<N;++i){int a=i/9,b=i/3%3,c=i%3;
  gen[0][i]=encode(a==0?1:a==1?0:2,b,c);
  gen[1][i]=encode((a+1)%3,b,c);
  gen[2][i]=encode(a,b==0?1:b==1?0:2,c);
  gen[3][i]=encode(a,(b+1)%3,c);
  gen[4][i]=encode(a,b,c==0?1:c==1?0:2);
  gen[5][i]=encode(a,b,(c+1)%3);
  gen[6][i]=encode(b,a,c);
  gen[7][i]=encode(b,c,a);
 }
}
M transform(M mask,const array<int,N>&g){M out=0;while(mask){int i=__builtin_ctz(mask);mask&=mask-1;out|=M(1)<<g[i];}return out;}
bool minimally_uncoverable(const vector<int>&v){
 int k=v.size();vector<M>pre(k+1),suf(k+1);pre[0]=suf[k]=FULL;
 for(int j=0;j<k;j++)pre[j+1]=pre[j]&compatible[v[j]];
 if(pre[k])return false;
 for(int j=k-1;j>=0;j--)suf[j]=suf[j+1]&compatible[v[j]];
 for(int j=0;j<k;j++)if(!(pre[j]&suf[j+1]))return false;
 return true;
}
int main(int argc,char**argv){
 bool csv=(argc==2 && string(argv[1])=="--classes");
 if(argc>2 || (argc==2 && !csv)){fprintf(stderr,"usage: verify [--classes]\n");return 3;}
 FILE* summary=csv?stderr:stdout;
 vector<tuple<int,M,int>> classes;
 init();array<long long,9> found{};array<vector<M>,9> all;array<M,9> examples{};
 for(int k=1;k<=8;k++){
  vector<int> v(k);iota(v.begin(),v.end(),0);
  long long visited=0;
  do{
   if(minimally_uncoverable(v)){
    M b=0;for(int x:v)b|=M(1)<<x;
    all[k].push_back(b);found[k]++;
    if(!examples[k])examples[k]=b;
   }
   ++visited;
   int j=k-1;while(j>=0&&v[j]==N-k+j)--j;
   if(j<0)break;
   v[j]++;for(int h=j+1;h<k;h++)v[h]=v[h-1]+1;
  }while(1);
  fprintf(summary,"size=%d subsets=%lld minimal_noncover=%lld\n",k,visited,found[k]);
 }
 fprintf(summary,"total=%lld\n",accumulate(found.begin(),found.end(),0LL));
 for(int k=1;k<=8;k++){
  if(all[k].empty())continue;
  unordered_set<M> unseen(all[k].begin(),all[k].end());
  map<int,int> orbit_size_frequency;
  long long n_orbits=0, sumorbit=0;
  while(!unseen.empty()){
   M first=*unseen.begin();unseen.erase(first);
   vector<M> queue{first};
   for(int h=0;h<(int)queue.size();h++)for(auto &g:gen){
    M next=transform(queue[h],g);
    if(unseen.erase(next))queue.push_back(next);
    else if(next!=first && find(queue.begin(),queue.end(),next)==queue.end()){
      fprintf(stderr,"ERROR generated orbit not in minimal family size %d mask %u\n",k,next);return 2;
    }
   }
   n_orbits++;sumorbit+=queue.size();orbit_size_frequency[queue.size()]++;
   M canon=*min_element(queue.begin(),queue.end());
   classes.emplace_back(k,canon,(int)queue.size());
  }
  assert(sumorbit==(long long)all[k].size());
  fprintf(summary,"orbits size=%d count=%lld distribution=",k,n_orbits);
  for(auto [s,ct]:orbit_size_frequency)fprintf(summary,"%d:%d,",s,ct);
  fprintf(summary," example={");
  M ex=examples[k];for(int j=0;j<N;j++)if(ex>>j&1)fprintf(summary,"(%d%d%d)",j/9,j/3%3,j%3);
  fprintf(summary,"}\n");
 }
 if(csv){
  sort(classes.begin(),classes.end());
  puts("team_size,canonical_27bit_mask_hex,orbit_size");
  for(auto [k,mask,orbit]:classes)printf("%d,%07x,%d\n",k,mask,orbit);
 }

}
