// Standalone exact verifier for the 25-site Latin-square Ising comparison.
// Compile: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
using A26=array<uint64_t,26>;
static constexpr int N=25;
static constexpr int LAT[2][5][5]={
 {{0,1,2,3,4},{1,2,3,4,0},{2,3,4,0,1},{3,4,0,1,2},{4,0,1,2,3}},
 {{0,1,2,3,4},{1,0,3,4,2},{2,3,4,0,1},{3,4,1,2,0},{4,2,0,1,3}}
};
static constexpr uint32_t WITNESS[2][13]={
 {0x0,0x1,0x30,0x602,0xc104,0x182082,0x18120a,0x18068a,0x181a2c,0x18e186,0x3644d8,0x32e07c,0x31e0fc},
 {0x0,0x1,0x30,0x502,0xc044,0x281028,0x180582,0x18068a,0x180d86,0x18e186,0x336289,0x336389,0x31e0fc}
};
static constexpr uint64_t EXPECT[2][26]={
 {1,25,150,250,75,15,400,3950,6150,1375,130,2250,15250,15250,2250,130,1375,6150,3950,400,15,75,250,150,25,1},
 {1,25,150,250,79,3,400,4030,6126,1371,30,2274,15282,15282,2274,30,1371,6126,4030,400,3,79,250,150,25,1}
};
struct Counts {array<int,26> best; A26 mult; uint64_t hist[26][151]{};
 Counts(){best.fill(99999);mult.fill(0);}
 void record(int k,int e){assert(k>=0&&k<=25&&e>=0&&e<=150);hist[k][e]++;
  if(e<best[k]){best[k]=e;mult[k]=1;}else if(e==best[k])mult[k]++;}
};
static uint64_t HIST[2][26][151]{};
static __int128 choose(int n,int r){if(r<0||r>n)return 0;__int128 v=1;for(int i=1;i<=r;i++)v=v*(n-i+1)/i;return v;}
static vector<__int128> mul(const vector<__int128>&a,const vector<__int128>&b){vector<__int128> v(a.size()+b.size()-1);for(size_t i=0;i<a.size();i++)for(size_t j=0;j<b.size();j++)v[i+j]+=a[i]*b[j];return v;}
static vector<__int128> power(vector<__int128> f,int n){vector<__int128> g={1};for(int j=0;j<n;j++)g=mul(g,f);return g;}
static vector<__int128> shifted(vector<__int128> f,int n){vector<__int128> g(n,0);for(auto v:f)g.push_back(v);return g;}
static __int128 ipow(__int128 b,int n){__int128 v=1;for(int i=0;i<n;i++)v*=b;return v;}
static void check_physics(){
 __int128 D[9][26]{};
 for(int k=0;k<=25;k++)for(int e=0;e<=150;e++){
  long long dd=(long long)HIST[0][k][e]-(long long)HIST[1][k][e];
  for(int r=0;r<=8;r++)D[r][k]+=dd*choose(e,r);
 }
 for(int r=0;r<6;r++)for(int k=0;k<=25;k++)assert(D[r][k]==0);
 auto expected6=shifted(mul(power({-1,1},4),power({1,1},13)),4);
 for(auto &z:expected6)z*=-4;
 auto expected7=shifted(mul(mul(power({-1,1},2),power({1,1},11)),{3,-3,-15,17}),5);
 for(auto &z:expected7)z*=-24;
 for(int k=0;k<=25;k++){assert(D[6][k]==(k<(int)expected6.size()?expected6[k]:0));assert(D[7][k]==(k<(int)expected7.size()?expected7[k]:0));}
 __int128 total8=0;for(int k=0;k<=25;k++)total8+=D[8][k];assert(total8==-24576);
 for(int h : {-2,0,1,3})for(int r=0;r<=8;r++){
  __int128 moment=0;
  for(int k=0;k<=25;k++)for(int e=0;e<=150;e++){
   long long dd=(long long)HIST[0][k][e]-(long long)HIST[1][k][e];
   if(dd)moment+=dd*ipow(-(__int128)(150-24*k+4*e-h*(25-2*k)),r);
  }
  if(r<=7)assert(moment==0);
  else assert(moment==-(__int128)48*(1LL<<25)*40320);
 }
 cout<<"MOMENTS_OK fugacity_series_0_to_7 checked physical_beta_0_to_8 fields=4 difference_eulerian8=-48"<<endl;
}
int ce(int n){return n*(n-1)/2;}
int bound(int k){int q=k/5,r=k%5;return 3*(5*ce(q)+q*r);}
int induced(uint32_t subset,const uint32_t* nbr){int res=0;while(subset){int v=__builtin_ctz(subset);subset&=subset-1;res+=__builtin_popcount(subset&nbr[v]);}return res;}
void walk_rows(int t,int row,int k,int edges,array<int,5>& col,array<int,5>& sym,Counts &c){
 if(row==5){c.record(k,edges);return;}
 for(int mask=0;mask<32;mask++){
  int d=edges+ce(__builtin_popcount((unsigned)mask));
  for(int j=0;j<5;j++)if(mask&(1<<j)){d+=col[j]+sym[LAT[t][row][j]];col[j]++;sym[LAT[t][row][j]]++;}
  walk_rows(t,row+1,k+__builtin_popcount((unsigned)mask),d,col,sym,c);
  for(int j=0;j<5;j++)if(mask&(1<<j)){col[j]--;sym[LAT[t][row][j]]--;}
 }
}
int main(){
 for(int t=0;t<2;t++){
  uint32_t nbr[N]={};int edgeCount=0;
  for(int r=0;r<5;r++){
    uint32_t usedRow=0,usedCol=0,usedSym=0;
    for(int c=0;c<5;c++){
      int x=LAT[t][r][c];assert(0<=x&&x<5);
      assert(!(usedSym&(1u<<x)));usedSym|=1u<<x;
    }
    assert(usedSym==31);
  }
  for(int c=0;c<5;c++){int used=0;for(int r=0;r<5;r++)used|=1<<LAT[t][r][c];assert(used==31);}
  for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){
    int r=u/5,c=u%5,s=v/5,d=v%5;
    if(r==s||c==d||LAT[t][r][c]==LAT[t][s][d]){nbr[u]|=1u<<v;nbr[v]|=1u<<u;edgeCount++;}
  }
  assert(edgeCount==150);
  for(int u=0;u<N;u++){assert(__builtin_popcount(nbr[u])==12);for(int v=u+1;v<N;v++)assert(__builtin_popcount(nbr[u]&nbr[v])==((nbr[u]>>v)&1?5:6));}
  // Count all K4 directly (a K5 contains 5 K4 subgraphs).
  int fours=0;
  for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)if(nbr[a]&(1u<<b))
   for(int c=b+1;c<N;c++)if((nbr[a]&(1u<<c))&&(nbr[b]&(1u<<c)))
    for(int d=c+1;d<N;d++)if((nbr[a]&(1u<<d))&&(nbr[b]&(1u<<d))&&(nbr[c]&(1u<<d)))fours++;
  assert(fours==(t==0?75:79));
  // The lower bound is proved by balancing five row, column and symbol occupancies.
  // The 13 masks below certify equality; complements certify the other 13 sizes.
  for(int k=0;k<=12;k++){
   uint32_t mask=WITNESS[t][k];assert(__builtin_popcount(mask)==k);
   int e=induced(mask,nbr);assert(e==bound(k));
   uint32_t comp=((1u<<25)-1u)^mask;
   assert(induced(comp,nbr)==bound(25-k));
  }
  // Independent counting A: Gray-code traversal and bitset induced-edge updates.
  Counts a;int k=0,e=0;uint32_t g=0;
  for(uint32_t i=0;i<(1u<<25);i++){
   if(i){int flip=__builtin_ctz(i);g=i^(i>>1);if(g&(1u<<flip)){
     e+=__builtin_popcount(g&nbr[flip]);k++;
    }else{e-=__builtin_popcount(g&nbr[flip]);k--;}}
   a.record(k,e);
  }
  // Independent counting B: recursively add complete rows, counting same-column/symbol collisions.
  Counts b;array<int,5> col{};array<int,5> sym{};
  walk_rows(t,0,0,0,col,sym,b);
  for(int i=0;i<=25;i++){
    assert(a.best[i]==bound(i)&&b.best[i]==bound(i));
    assert(a.mult[i]==b.mult[i]);assert(a.mult[i]==EXPECT[t][i]);
    for(int e2=0;e2<=150;e2++){assert(a.hist[i][e2]==b.hist[i][e2]);HIST[t][i][e2]=a.hist[i][e2];}
  }
  assert(a.mult[10]==(t==0?130:30));assert(a.mult[5]==(t==0?15:3));
  cout <<"CLASS="<<t<<" K4="<<fours<<" K5_SECTOR="<<a.mult[5]<<" K10_SECTOR="<<a.mult[10]<<" CONFIGS="<<(1u<<25)<<" OK\n";
 }
 check_physics();
 cout <<"VERIFY_OK graph_classes=2 methods=2 subsets_each=33554432 sector_sizes=26 hist_cells=7852\n";
}
