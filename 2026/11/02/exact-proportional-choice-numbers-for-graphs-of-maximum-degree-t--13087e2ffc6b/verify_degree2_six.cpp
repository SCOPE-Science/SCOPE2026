// Exact exhaustive checker for proportional 3-choosability of every six-vertex graph of maximum degree two.
// No external libraries: g++ -O3 -std=c++17 verify_degree2_six.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
constexpr int N=6, MASKS=(1<<N)-1;
int freq[MASKS+1], colmask[3*N], cnt, lists[N][3], lo[3*N], hi[3*N], used[3*N], current[N];
int neighbor[N];
uint64_t checked=0;
int which=0;
struct Graph {const char*name; int edges[6][2];int m;};
Graph graphs[]={
  {"C6", {{0,1},{1,2},{2,3},{3,4},{4,5},{5,0}},6},
  {"C3+C3",{{0,1},{1,2},{2,0},{3,4},{4,5},{5,3}},6},
  {"C4+K2",{{0,1},{1,2},{2,3},{3,0},{4,5}},5},
  {"C5+K1",{{0,1},{1,2},{2,3},{3,4},{4,0}},5},
};
bool rec(int i) {
 if(i==N) {for(int d=0;d<cnt;d++)if(used[d]<lo[d]) return false;return true;}
 for(int j=0;j<3;j++){
  int c=lists[i][j];if(used[c]==hi[c])continue;
  bool valid=true;
  for(int p=0;p<i;p++)if((neighbor[i]>>p&1) && current[p]==c){valid=false;break;}
  if(!valid)continue;
  current[i]=c;used[c]++;
  bool possible=true;
  for(int d=0;d<cnt;d++)if(used[d]<lo[d]){
   int remaining=__builtin_popcount((unsigned)(colmask[d] & (MASKS ^ ((1<<(i+1))-1))));
   if(used[d]+remaining<lo[d]){possible=false;break;}
  }
  if(possible&&rec(i+1)){used[c]--;return true;}
  used[c]--;
 }
 return false;
}
void check(){
 checked++;cnt=0;int slots[N]={};
 for(int m=1;m<=MASKS;m++)for(int j=0;j<freq[m];j++){
  int c=cnt++;colmask[c]=m;used[c]=0;
  int t=__builtin_popcount((unsigned)m);
  lo[c]=t/3;hi[c]=(t+2)/3;
  for(int v=0;v<N;v++)if((m>>v)&1)lists[v][slots[v]++]=c;
 }
 for(int v=0;v<N;v++)if(slots[v]!=3){fputs("INVALID_ENUMERATION\n",stderr);exit(3);}
 if(!rec(0)){
  printf("FAIL %s case %llu\n",graphs[which].name,(unsigned long long)checked);
  for(int v=0;v<N;v++)printf("%d : %d,%d,%d\n",v,lists[v][0],lists[v][1],lists[v][2]);
  exit(2);
 }
}
void gen(int m,int rem[N]) {
 if(m>MASKS){for(int i=0;i<N;i++)if(rem[i])return;check();return;}
 int maxk=3;for(int i=0;i<N;i++)if(m>>i&1)if(rem[i]<maxk)maxk=rem[i];
 for(int k=0;k<=maxk;k++){
  freq[m]=k;for(int i=0;i<N;i++)if(m>>i&1)rem[i]-=k;
  gen(m+1,rem);
  for(int i=0;i<N;i++)if(m>>i&1)rem[i]+=k;
 }
}
int main(){
 for(which=0;which<4;which++){
  for(int i=0;i<N;i++)neighbor[i]=0;
  auto &g=graphs[which];
  for(int e=0;e<g.m;e++){
   int a=g.edges[e][0],b=g.edges[e][1];
   neighbor[a]|=1<<b;neighbor[b]|=1<<a;
  }
  checked=0;int rem[N]={3,3,3,3,3,3};
  gen(1,rem);
  printf("PASS %s canonical_color_list_types=%llu\n",g.name,(unsigned long long)checked);
 }
 puts("VERIFY_OK");return 0;
}
