// Direct graph-neighborhood evolution; does not use the reduced support update.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using State=vector<unsigned char>;
static State update(const State &x, int r){
  const int N=r+2;
  State y=x;
  for(int v=0;v<N;v++){
    int succ=(x[v]+1)%3;
    bool found=false;
    if(v==N-1){found=x[0]==succ;}
    else {
      for(int u=0;u<N;u++)if(u!=v && (u<N-1 || (v==0 && u==N-1)))
        if(x[u]==succ){found=true;break;}
    }
    if(found)y[v]=succ;
  }
  return y;
}
static long long power3(int n){long long r=1;while(n--)r*=3;return r;}
static long long power2(int n){long long r=1;while(n--)r*=2;return r;}
static string statekey(const State& s){
  string k; k.reserve(s.size()); for(auto a:s)k.push_back(char('0'+a));return k;
}
int main(){
 long long checked=0;
 for(int r=1;r<=11;r++){
  const int N=r+2;
  map<pair<int,int>,long long> cnt;
  map<string,int> periodic_basin_sizes;
  map<string,int> fixed_basin_sizes;
  map<pair<string,int>,int> three_cycle_layers, fixed_layers;
  for(long long code=0;code<power3(N);code++){
   long long z=code; State x(N);
   for(int v=0;v<N;v++){x[v]=z%3;z/=3;}
   vector<State> orbit{x};
   for(int t=0;t<5;t++)orbit.push_back(update(orbit.back(),r));
   int T=-1,p=0;
   for(int t=0;t<=2;t++){
     if(orbit[t]==orbit[t+1]){T=t;p=1;break;}
     if(orbit[t]==orbit[t+3]){T=t;p=3;break;}
   }
   if(T<0){cerr<<"no period by two";return 1;}
   cnt[{T,p}]++;
   if(p==1){string key=statekey(orbit[T]);fixed_basin_sizes[key]++;fixed_layers[{key,T}]++;}
   else{
    string key=statekey(orbit[T]);
    for(int d=1;d<3;d++)key=min(key,statekey(orbit[T+d]));
    periodic_basin_sizes[key]++;three_cycle_layers[{key,T}]++;
   }
   ++checked;
  }
  long long q=power3(r)-2*power2(r)+1;
  const map<pair<int,int>,long long> expected={
    {{0,1},3},{{1,1},3*(3*power2(r)-2)},{{2,1},3*(3*power2(r)-2)},
    {{0,3},3*q},{{1,3},3*q},{{2,3},3*q}};
  for(auto kv:expected){if(cnt[kv.first]!=kv.second){cerr<<"wrong count for r="<<r<<" at "<<kv.first.first<<","<<kv.first.second<<"\n";return 2;}}
  if((long long)periodic_basin_sizes.size()!=q){cerr<<"wrong number of 3-cycles\n";return 3;}
  for(const auto &kv:periodic_basin_sizes){
    if(kv.second!=9){cerr<<"period3 basin not size9\n";return 4;}
    for(int t=0;t<3;t++)if(three_cycle_layers[{kv.first,t}]!=3){cerr<<"three-cycle layer not size3\n";return 7;}
  }
  if(fixed_basin_sizes.size()!=3){cerr<<"wrong number fixed basins\n";return 5;}
  for(const auto &kv:fixed_basin_sizes){
    if(kv.second!=3*(power2(r+1)-1)){cerr<<"fixed basin wrong size\n";return 6;}
    for(int t=0;t<3;t++){
      int expected_count=(t==0)?1:(3*power2(r)-2);
      if(fixed_layers[{kv.first,t}]!=expected_count){cerr<<"fixed temporal layer wrong size\n";return 8;}
    }
  }
  cout<<"r="<<r<<" states="<<power3(N)<<" primitive3_orbits="<<q
      <<" primitive3_basin=9 each, fixed_basin="<<3*(power2(r+1)-1)<<" PASS\n";
 }
 cout<<"DIRECT_VERIFIED labelled_states="<<checked<<"\n";
}
