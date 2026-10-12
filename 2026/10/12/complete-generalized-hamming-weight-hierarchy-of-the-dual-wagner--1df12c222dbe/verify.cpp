#include <bits/stdc++.h>
using namespace std;
int main(){
int G[14][23] = {
{1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1},
{0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1},
{0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1},
{0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1},
{0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0},
{0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1},
{0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0},
{0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1},
{0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1},
{0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0},
{0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0},
{0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0},
{0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1},
{0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,1}};
uint16_t col[23]{};
for(int j=0;j<23;j++)for(int i=0;i<14;i++) if(G[i][j]) col[j]|=(1u<<i);
vector<int> best(10,99); vector<uint32_t>wit(10);
uint32_t N=1u<<23;
for(uint32_t mask=1;mask<N;mask++){
  int sz=__builtin_popcount(mask);
  bool needed=false; for(int r=1;r<=9;r++) if(sz<best[r]) {needed=true;break;} if(!needed) continue;
  uint16_t b[14]{}; int rank=0;
  uint32_t m=mask;
  while(m){int j=__builtin_ctz(m);m&=m-1; uint16_t x=col[j];
    while(x){int p=31-__builtin_clz((unsigned)x); if(b[p]) x^=b[p]; else {b[p]=x;rank++;break;}}
  }
  int nul=sz-rank;
  for(int r=1;r<=min(9,nul);r++) if(sz<best[r]){best[r]=sz;wit[r]=mask;}
}
int expv[10]={0,8,12,15,17,18,20,21,22,23};
for(int r=1;r<=9;r++){if(best[r]!=expv[r]){cerr<<"mismatch at r="<<r<<"\n"; return 2;} cout<<r<<" "<<best[r]<<" "; for(int j=0;j<23;j++)if(wit[r]>>j&1)cout<<j+1<<",";cout<<"\n";}
cout<<"VERIFY_OK\n";
}
