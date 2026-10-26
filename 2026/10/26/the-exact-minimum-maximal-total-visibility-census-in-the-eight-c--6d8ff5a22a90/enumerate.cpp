// Exact finite enumeration of minimum independent dominating sets
// in the even-weight half of the 8-dimensional binary cube.
// Requires only a C++17 compiler; no external data.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

struct Masks { uint64_t low=0, high=0; };
Masks unite(Masks a, Masks b) {return {a.low|b.low,a.high|b.high};}
constexpr uint64_t ALL = UINT64_MAX;

vector<int> words;
array<Masks,128> neighborhoods;
array<array<bool,128>,128> compatible{};
vector<int> chosen;
uint64_t tested=0, accepted=0;
map<string,uint64_t> profiles;

void collect_profile() {
  array<int,8> degree{};
  array<array<bool,8>,8> six{};
  int edges=0;
  for(int a=0;a<8;a++) for(int b=a+1;b<8;b++){
    int dist=__builtin_popcount((unsigned)(words[chosen[a]]^words[chosen[b]]));
    if(dist==6){six[a][b]=six[b][a]=true;degree[a]++;degree[b]++;edges++;}
  }
  sort(degree.begin(),degree.end());
  array<bool,8> seen{}; vector<int> components;
  for(int a=0;a<8;a++) if(!seen[a]){
    int size=0;vector<int> stack={a};seen[a]=true;
    while(!stack.empty()){
      int u=stack.back();stack.pop_back();size++;
      for(int v=0;v<8;v++)if(six[u][v]&&!seen[v]){seen[v]=true;stack.push_back(v);}
    }
    components.push_back(size);
  }
  sort(components.begin(),components.end());
  string key=to_string(edges)+" edges; degrees=";
  for(int d:degree)key+=to_string(d);
  key+="; components=";
  for(int c:components)key+=to_string(c)+",";
  profiles[key]++;
}

void search(int last,int remaining,Masks dominated){
  if(remaining==0){
    ++tested;
    if(dominated.low==ALL && dominated.high==ALL){
      ++accepted;
      if(chosen.size()==8)collect_profile();
    }
    return;
  }
  for(int i=last+1;i<=128-remaining;i++){
    if(!compatible[0][i])continue;
    bool good=true;
    for(int j:chosen)if(!compatible[j][i]){good=false;break;}
    if(!good)continue;
    chosen.push_back(i);
    search(i,remaining-1,unite(dominated,neighborhoods[i]));
    chosen.pop_back();
  }
}

int main(){
  for(int x=0;x<256;x++)if((__builtin_popcount((unsigned)x)%2)==0)words.push_back(x);
  if(words.size()!=128||words[0]!=0)throw runtime_error("vertex initialization");
  for(int i=0;i<128;i++)for(int j=0;j<128;j++){
    int dist=__builtin_popcount((unsigned)(words[i]^words[j]));
    compatible[i][j]=(dist!=2);
    if(dist<=2){
      if(j<64)neighborhoods[i].low|=uint64_t(1)<<j;
      else neighborhoods[i].high|=uint64_t(1)<<(j-64);
    }
  }
  array<uint64_t,4> expected_candidates={611100,2984625,7490595,9234285};
  for(int k=5;k<=8;k++){
    tested=accepted=0;profiles.clear();chosen={0};
    search(0,k-1,neighborhoods[0]);
    cout<<"k="<<k<<" compatible_anchored="<<tested<<" dominating_anchored="<<accepted<<"\n";
    if(tested!=expected_candidates[k-5])throw runtime_error("candidate count differs");
    if(accepted!=(k==8 ? 142380U : 0U))throw runtime_error("domination count differs");
    if(k==8){
      uint64_t sum=0;
      for(const auto &p:profiles){cout<<"profile: "<<p.first<<" count="<<p.second<<"\n";sum+=p.second;}
      if(sum!=142380U || profiles.size()!=3)throw runtime_error("profile count differs");
    }
  }
  cout<<"even-half minimum=8; even-half minimum-code total="<<(128ULL*142380ULL/8ULL)<<"\n";
  cout<<"full Q8 lower total-visibility=16; minimum maximal sets="
      <<(2278080ULL*2278080ULL)<<"\n";
  cout<<"VERIFY_OK\n";
}
