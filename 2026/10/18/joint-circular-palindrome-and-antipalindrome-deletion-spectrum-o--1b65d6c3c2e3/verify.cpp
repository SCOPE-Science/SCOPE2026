// Exhaustive verification of circular palindrome and antipalindrome deletion profiles.
// Compile: g++ -O2 -std=c++17 verify.cpp -o verify
// Run: ./verify cycles.csv
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
constexpr int N=32;
string canonical(const string &s) {
  string d=s+s, best=s;
  for(int i=1;i<N;i++) best=min(best,d.substr(i,N));
  return best;
}
string reverse_bits(string s) { reverse(s.begin(),s.end());return s; }
string complement(string s) {for(auto &x:s)x=(x=='0'?'1':'0');return s;}
bool is_db(const string &s) {
  if(s.size()!=N)return false;
  uint32_t seen=0;
  for(int i=0;i<N;i++) {
    int v=0;
    for(int j=0;j<5;j++)v=2*v+(s[(i+j)%N]-'0');
    seen|=(uint32_t(1)<<v);
  }
  return seen==UINT32_MAX;
}
int pair_dp(const string &s,bool anti) {
  int d[33][33]{};
  for(int i=0;i<N;i++)d[i][i]=anti?0:1;
  for(int len=2;len<=N;len++)for(int i=0;i+len<=N;i++){
    int j=i+len-1;
    int z=max(d[i+1][j],d[i][j-1]);
    if((s[i]!=s[j])==anti) z=max(z,2+(len==2?0:d[i+1][j-1]));
    d[i][j]=z;
  }
  return d[0][N-1];
}
int independently_via_lcs(const string &s,bool anti){
  string t=reverse_bits(s);
  if(anti)t=complement(t);
  int dp[33][33]{};
  for(int i=1;i<=N;i++) for(int j=1;j<=N;j++){
    dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
    if(s[i-1]==t[j-1])dp[i][j]=max(dp[i][j],1+dp[i-1][j-1]);
  }
  return dp[N][N];
}
set<string> by_pairings(){
  set<string> words;
  for(uint32_t pairing=0;pairing<65536;pairing++){
    uint32_t used=0;
    int e=0;
    string s;
    for(int i=0;i<N;i++){
      if(used&(uint32_t(1)<<e)){s.clear();break;}
      used|=uint32_t(1)<<e;
      s.push_back(char('0'+(e&1)));
      int v=e&15;
      e=(v<<1)+((e>>4)^((pairing>>v)&1));
    }
    if(s.size()==N&&e==0)words.insert(canonical(s));
  }
  return words;
}
set<string> by_dfs(){
  set<string> words;
  string bits;
  auto visit=[&](auto &&self,int vertex,uint32_t mask)->void {
    if(bits.size()==N){
      if(vertex==0)words.insert(canonical(bits));
      return;
    }
    for(int b=0;b<2;b++){
      int edge=2*vertex+b;
      if(mask&(uint32_t(1)<<edge))continue;
      bits.push_back(char('0'+b));
      self(self,edge&15,mask|(uint32_t(1)<<edge));
      bits.pop_back();
    }
  };
  bits="0";visit(visit,0,uint32_t(1));
  return words;
}
int main(int argc,char**argv){
  if(argc!=2){cerr<<"usage: verify cycles.csv\n";return 1;}
  set<string> x=by_pairings(),y=by_dfs();
  if(x.size()!=2048||x!=y){cerr<<"independent generators disagree "<<x.size()<<" "<<y.size()<<"\n";return 2;}
  map<pair<int,int>,int> joint;
  map<string,pair<int,int>> calc;
  unsigned long long cutcount=0;
  for(const auto& w:x){
    if(!is_db(w)){cerr<<"invalid universal word\n";return 3;}
    int a=0,p=0;
    for(int k=0;k<N;k++){
      string cut=(w+w).substr(k,N);
      int aa=pair_dp(cut,true),pp=pair_dp(cut,false);
      int al=independently_via_lcs(cut,true),pl=independently_via_lcs(cut,false);
      if(aa!=al||pp!=pl){cerr<<"independent subsequence methods disagree\n";return 4;}
      a=max(a,aa);p=max(p,pp);cutcount++;
    }
    calc[w]={a,p};joint[{a,p}]++;
  }
  const map<pair<int,int>,int> expected={
    {{26,25},4},{{26,26},16},{{26,27},284},{{26,28},52},{{26,29},32},
    {{28,25},52},{{28,26},80},{{28,27},860},{{28,28},180},{{28,29},136},
    {{30,25},12},{{30,26},16},{{30,27},192},{{30,28},44},{{30,29},24},
    {{32,25},8},{{32,26},2},{{32,27},44},{{32,28},10}
  };
  if(joint!=expected){cerr<<"joint table mismatch\n";for(const auto& kv:joint)cerr<<kv.first.first<<","<<kv.first.second<<":"<<kv.second<<" ";cerr<<"\n";return 5;}
  ifstream in(argv[1]);
  string line;getline(in,line);
  if(line!="cycle,anti_lps,pal_lps"){cerr<<"bad header\n";return 6;}
  size_t rowcount=0;
  while(getline(in,line)){
    if(line.empty())continue;
    stringstream ss(line);string w,sa,sp;
    getline(ss,w,',');getline(ss,sa,',');getline(ss,sp,',');
    auto it=calc.find(w);
    if(it==calc.end()||it->second.first!=stoi(sa)||it->second.second!=stoi(sp)){
      cerr<<"CSV entry mismatch\n";return 7;
    }
    rowcount++;
  }
  if(rowcount!=2048){cerr<<"CSV row count mismatch\n";return 8;}
  map<int,int> ac,pc;
  map<pair<int,int>,pair<int,int>> orbit_hist;
  set<string> visited;
  for(const auto& w:x){
    auto [a,p]=calc.at(w);ac[a]++;pc[p]++;
    if(visited.count(w))continue;
    set<string> orbit={w,canonical(reverse_bits(w)),canonical(complement(w)),canonical(complement(reverse_bits(w)))};
    if(orbit.size()!=2&&orbit.size()!=4){cerr<<"bad orbit size\n";return 9;}
    for(auto z:orbit){if(!x.count(z)||calc[z]!=make_pair(a,p)){cerr<<"symmetry mismatch\n";return 10;}visited.insert(z);}
    if((orbit.size()==2)!=(a==32)){cerr<<"CR boundary orbit mismatch\n";return 13;}
    if(orbit.size()==2)orbit_hist[{a,p}].first++;
    else orbit_hist[{a,p}].second++;
  }
  int t2=0,t4=0;for(auto kv:orbit_hist){t2+=kv.second.first;t4+=kv.second.second;}
  if(t2!=32||t4!=496){cerr<<"wrong orbit totals\n";return 11;}
  if(ac!=map<int,int>{{26,388},{28,1308},{30,288},{32,64}}||pc!=map<int,int>{{25,76},{26,114},{27,1380},{28,286},{29,192}}){cerr<<"marginal mismatch\n";return 12;}
  cout<<"VERIFY_OK pairings=65536 generator_pairings=2048 independent_Eulerian_DFS=2048 cyclic_cuts="<<cutcount<<" LPS_methods=2 anti_LPS_methods=2 joint_cells="<<joint.size()<<" symmetry_orbits="<<(t2+t4)<<" anti_marginal=26:388,28:1308,30:288,32:64 pal_marginal=25:76,26:114,27:1380,28:286,29:192 csv_rows="<<rowcount<<"\n";
}
