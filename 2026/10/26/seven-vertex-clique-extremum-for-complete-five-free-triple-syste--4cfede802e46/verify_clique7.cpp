// Exhaustive certificate for the seven-vertex K_5^(3)-free clique extremum.
// This program uses only the C++17 standard library. Vertices are 0,...,6.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;

static vector<array<int,3>> triples;
static vector<array<int,4>> fours;
static vector<array<int,5>> fives;
static uint64_t four_shadow[35], five_shadow[35];
static uint64_t all_fives;
static long long examined[9]={}, covers[9]={};
static int min_four[9], min_free_shadow[9], winners=0;
static vector<vector<int>> optimal;
static int size_chosen;
static int pop(uint64_t a){int z=0;while(a){a&=a-1;++z;}return z;}

// Every unordered missing-triple family is isomorphic to one containing 012.
// The other t-1 triple indices are strictly increasing, so no case repeats.
static void enumerate(int next, vector<int>& chosen, uint64_t sh4, uint64_t sh5){
  int t=(int)chosen.size();
  if(t==size_chosen){
    ++examined[t];
    if(pop(sh4)<min_four[t])min_four[t]=pop(sh4);
    if(sh5==all_fives){
      ++covers[t];
      if(pop(sh4)<min_free_shadow[t])min_free_shadow[t]=pop(sh4);
      if(t+pop(sh4)==22){++winners;optimal.push_back(chosen);}
      assert(t+pop(sh4)>=22);
    }
    return;
  }
  for(int j=next;j<=35-(size_chosen-t);++j){
    chosen.push_back(j);
    enumerate(j+1,chosen,sh4|four_shadow[j],sh5|five_shadow[j]);
    chosen.pop_back();
  }
}
int main(){
  for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++) triples.push_back({a,b,c});
  for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int d=c+1;d<7;d++) fours.push_back({a,b,c,d});
  for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)for(int d=c+1;d<7;d++)for(int e=d+1;e<7;e++) fives.push_back({a,b,c,d,e});
  assert(triples.size()==35 && fours.size()==35 && fives.size()==21);
  for(int i=0;i<35;i++){
    four_shadow[i]=five_shadow[i]=0;
    for(int k=0;k<35;k++)if(includes(fours[k].begin(),fours[k].end(),triples[i].begin(),triples[i].end())) four_shadow[i]|=1ULL<<k;
    for(int k=0;k<21;k++)if(includes(fives[k].begin(),fives[k].end(),triples[i].begin(),triples[i].end())) five_shadow[i]|=1ULL<<k;
    assert(pop(four_shadow[i])==4 && pop(five_shadow[i])==6);
  }
  assert(triples[0]==(array<int,3>{0,1,2}));
  all_fives=(1ULL<<21)-1;
  for(int t=1;t<=8;t++){
    min_four[t]=99; min_free_shadow[t]=99;
    size_chosen=t;
    vector<int> chosen={0};
    enumerate(1,chosen,four_shadow[0],five_shadow[0]);
    printf("t=%d families=%lld K5free=%lld min_four_shadow=%d min_free_shadow=%d\n",t,examined[t],covers[t],min_four[t],min_free_shadow[t]);
  }
  assert(covers[1]==0 && covers[2]==0 && covers[3]==0 && covers[4]==0);
  assert(covers[5]==245 && covers[6]==15300 && covers[7]==235992);
  assert(min_four[8]==16); // All 8-family shadows have at least sixteen 4-sets.
  assert(min_free_shadow[5]==17 && min_free_shadow[6]==19 && min_free_shadow[7]==20);
  assert(winners==5);
  // Each optimal missing-triple family must comprise all triples of complementary
  // parts of sizes three and four. Check this directly, not by visually matching.
  for(auto &win:optimal){
    assert(win.size()==5);
    bool is_bipartite_template=false;
    for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++){
      bool small[7]={};small[a]=small[b]=small[c]=true;
      vector<int> intended;
      for(int i=0;i<35;i++){
        int s=0;for(int v:triples[i])s+=small[v];
        if(s==0||s==3)intended.push_back(i);
      }
      if(intended==win)is_bipartite_template=true;
    }
    assert(is_bipartite_template);
  }
  puts("CERTIFICATE_OK maximum_cliques=77 normalized_optima=5 labeled_optima=35");
  // A missing-triple set of size >=8 contains an 8-subset; the 8-family
  // shadow bound gives at least 16 shadow four-sets. Therefore its score
  // t+|shadow| is at least 8+16=24, so cannot tie/beat 22.
}
