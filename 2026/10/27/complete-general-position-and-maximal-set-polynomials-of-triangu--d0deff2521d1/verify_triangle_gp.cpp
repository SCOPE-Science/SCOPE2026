#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
using namespace std;

pair<vector<uint64_t>, vector<uint64_t>> brute(int n) {
  vector<pair<int,int>> edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  int m=edges.size();
  vector<uint64_t> nbr(m,0);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j &&
       (edges[i].first==edges[j].first||edges[i].first==edges[j].second||
        edges[i].second==edges[j].first||edges[i].second==edges[j].second))
          nbr[i]|=uint64_t(1)<<j;
  vector<uint64_t> count(m+1,0);
  vector<unsigned char> good(uint64_t(1)<<m, 0);
  for(uint64_t subset=0;subset<(uint64_t(1)<<m);++subset){
    bool valid=true;
    for(uint64_t temp=subset;temp && valid;temp&=temp-1){
      int i=__builtin_ctzll(temp);
      uint64_t neighbors=subset & nbr[i];
      for(uint64_t t=neighbors;t;t&=t-1){
        int j=__builtin_ctzll(t);
        if((neighbors & ~nbr[j] & ~(uint64_t(1)<<j))!=0){valid=false;break;}
      }
    }
    if(valid){count[__builtin_popcountll(subset)]++; good[subset]=1;}
  }
  vector<uint64_t> maximal(m+1,0);
  for(uint64_t subset=0;subset<(uint64_t(1)<<m);++subset){
    if(!good[subset])continue;
    bool extends=false;
    for(int i=0;i<m;++i)if(!(subset&(uint64_t(1)<<i)) && good[subset|(uint64_t(1)<<i)]){
      extends=true;break;
    }
    if(!extends)maximal[__builtin_popcountll(subset)]++;
  }
  return {count,maximal};
}
int main(){
  vector<vector<uint64_t>> expected={
    {},{},{1,1},
    {1,3,3,1},
    {1,6,15,8},
    {1,10,45,60,15},
    {1,15,105,275,240,66,10},
    {1,21,210,910,1680,1092,217}
  };
  vector<vector<uint64_t>> max_expected={
    {},{},{0,1},
    {0,0,0,1},
    {0,0,3,8},
    {0,0,0,0,15},
    {0,0,0,15,60,6,10},
    {0,0,0,0,0,210,217}
  };
  for(int n=2;n<=7;n++){
    auto both=brute(n);
    auto got=both.first;
    auto maximal=both.second;
    for(size_t j=0;j<got.size();j++){
      uint64_t ex=j<expected[n].size()?expected[n][j]:0;
      if(got[j]!=ex){cerr << "FAIL n="<<n<<" j="<<j<<" expected="<<ex<<" got="<<got[j]<<"\n";return 1;}
    }
    for(size_t j=0;j<maximal.size();j++){
      uint64_t ex=j<max_expected[n].size()?max_expected[n][j]:0;
      if(maximal[j]!=ex){cerr<<"MAXIMAL_FAIL n="<<n<<" j="<<j<<" expected="<<ex<<" got="<<maximal[j]<<"\n";return 1;}
    }
    cout<<"n="<<n<<" ALL: ";for(auto c:got)if(c)cout<<c<<" ";
    cout<<"MAXIMAL: ";for(auto c:maximal)if(c)cout<<c<<" ";cout<<"\n";
  }
  cout<<"ALL_EXHAUSTIVE_CHECKS_OK\n";
}
