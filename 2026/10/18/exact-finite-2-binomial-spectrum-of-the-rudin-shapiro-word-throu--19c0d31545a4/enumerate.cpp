// Exhaustive factor-profile census for a four-letter Rudin-Shapiro presentation.
// C++17: g++ -O2 -std=c++17 enumerate.cpp -o enumerate && ./enumerate output.csv dyadic.csv
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
static const array<array<int,2>,4> phi{{{{0,1}},{{0,3}},{{2,3}},{{2,1}}}};
vector<int> expand(vector<int> a,int rounds){
 for(int i=0;i<rounds;++i){ vector<int>b; b.reserve(a.size()*2); for(int x:a){ b.push_back(phi[x][0]);b.push_back(phi[x][1]);} a.swap(b); }
 return a;
}
int digit_bit(int n){
 unsigned x=(unsigned)n;return __builtin_parity(x&(x>>1));
}
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage: enumerate.csv dyadic.csv\n";return 2;}
 constexpr int H=12, B=(1<<H), MAXN=B;
 vector<int> t=expand({0},4);
 set<pair<int,int>> adj;for(int i=0;i+1<(int)t.size();++i)adj.insert({t[i],t[i+1]});
 if(adj.size()!=8){cerr<<"wrong pair closure\n";return 3;}
 // Closure under substitution and fixed-point evidence ensure this is all adjacent pairs.
 set<pair<int,int>> cp;
 for(auto [a,b]:adj){
  cp.insert({phi[a][0],phi[a][1]}); cp.insert({phi[b][0],phi[b][1]});
  cp.insert({phi[a][1],phi[b][0]});
 }
 if(cp!=adj){cerr<<"nonclosed pairs\n";return 4;}
 vector<vector<int>> blocks(4);
 for(int a=0;a<4;++a){auto z=expand({a},H); blocks[a].reserve(B); for(int x:z)blocks[a].push_back(x/2);}
 // Independent automatic rule cross-check at 2^16 consecutive positions.
 auto u=expand({0},H+4);
 if(u.size()!=65536){cerr<<"wrong fixed point\n";return 5;}
 for(int i=0;i<(int)u.size();++i)if(u[i]/2!=digit_bit(i)){
   cerr<<"coding discrepancy at "<<i<<"\n";return 6;
 }
 vector<vector<int>> pairs;
 for(auto [a,b]:adj){vector<int> q=blocks[a];q.insert(q.end(),blocks[b].begin(),blocks[b].end());pairs.push_back(move(q));}
 ofstream f(argv[1]);ofstream g(argv[2]);
 f<<"n,binomial2_classes,abelian_classes,min_ones,max_ones\n";
 g<<"n,ones,binomial2_classes_in_weight\n";
 for(int n=1;n<=MAXN;++n){
  unordered_set<uint64_t> profiles;
  profiles.reserve((size_t)8*n+40);
  for(auto &q:pairs){
    int w=0;int64_t z=0;
    for(int j=0;j<n;++j){ w+=q[j]; z+=(int64_t)j*q[j]; }
    for(int s=0;s<B;++s){
      profiles.insert(((uint64_t)w<<32)|(uint64_t)z);
      int old=q[s],newb=q[s+n];
      z=z-w+old+(int64_t)(n-1)*newb;
      w=w-old+newb;
    }
  }
  int lo=n+1,hi=-1;
  vector<int> counts(n+1,0);
  for(uint64_t key:profiles){int w=(int)(key>>32);lo=min(lo,w);hi=max(hi,w);counts[w]++;}
  int ab=hi-lo+1;
  for(int w=lo;w<=hi;++w)if(!counts[w]){cerr<<"weight gap at "<<n<<"\n";return 7;}
  f<<n<<','<<profiles.size()<<','<<ab<<','<<lo<<','<<hi<<'\n';
  if((n&(n-1))==0)for(int w=lo;w<=hi;++w)g<<n<<','<<w<<','<<counts[w]<<'\n';
  if((n&(n-1))==0)cerr<<"dyadic "<<n<<" b="<<profiles.size()<<" a="<<ab<<"\n";
 }
 f.close();g.close();if(!f||!g){cerr<<"write failed\n";return 8;}
 cerr<<"VERIFY_OK: exact aligned-pair cover for every n=1..4096\n";
}
