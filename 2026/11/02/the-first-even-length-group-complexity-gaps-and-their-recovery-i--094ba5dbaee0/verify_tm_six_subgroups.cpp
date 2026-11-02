#include <bits/stdc++.h>
using namespace std;
constexpr int n=6; constexpr int N=720;
using Bits=array<uint64_t,12>;
struct Hash {size_t operator()(Bits const& b) const noexcept {uint64_t h=1469598103934665603ULL;for(auto x:b)h=(h^x)*1099511628211ULL;return h;}};
struct Entry {Bits bits;vector<int> gens; int count;};
int mul[N][N];
int act[N][64];
inline bool has(Bits const& b,int i){return (b[i>>6]>>(i&63))&1ULL;}
inline void setbit(Bits& b,int i){b[i>>6]|=1ULL<<(i&63);}
Bits close_group(vector<int> const& gens,vector<int>* member=nullptr) {
 Bits b{};setbit(b,0); vector<int> q={0};
 for(size_t j=0;j<q.size();j++)for(int g:gens){int y=mul[q[j]][g];if(!has(b,y)){setbit(b,y);q.push_back(y);}}
 if(member)*member=move(q);return b;
}
int main(){
 vector<array<int,n>> p;array<int,n> a; iota(a.begin(),a.end(),0);
 do{p.push_back(a);}while(next_permutation(a.begin(),a.end()));
 map<array<int,n>,int> index; for(int i=0;i<N;i++)index[p[i]]=i;
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){
  array<int,n> comp; for(int k=0;k<n;k++)comp[k]=p[i][p[j][k]];
  mul[i][j]=index.at(comp);
 }
 for(int i=0;i<N;i++)for(int mask=0;mask<64;mask++){
  int v=0;for(int k=0;k<n;k++)if(mask&(1<<p[i][k]))v|=(1<<k); act[i][mask]=v;
 }
 string s="0";for(int i=0;i<9;i++){string t;for(char c:s)t+=(c=='0'?"01":"10");s=t;}
 set<int> ff;for(int i=0;i+(int)n<=(int)s.size();i++){int x=0;for(int k=0;k<n;k++)if(s[i+k]=='1')x|=1<<k;ff.insert(x);}
 Bits init{};setbit(init,0);vector<Entry> groups={{init,{},1}};
 unordered_set<Bits,Hash> seen;seen.insert(init);
 map<int,int> pcount;map<int,map<int,int>> tab;
 for(size_t idx=0;idx<groups.size();idx++){
  auto H=groups[idx];
  set<int> orbit;
  for(int m:ff){int v=64; for(int z=0;z<N;z++)if(has(H.bits,z))v=min(v,act[z][m]);orbit.insert(v);}
  pcount[orbit.size()]++;tab[H.count][orbit.size()]++;
  for(int g=1;g<N;g++)if(!has(H.bits,g)){
   vector<int> G=H.gens;G.push_back(g);vector<int> member;
   Bits b=close_group(G,&member);
   if(seen.insert(b).second){groups.push_back({b,move(G),(int)member.size()});}
  }
 }
 cout<<"factors "<<ff.size()<<" subgroup_count "<<groups.size()<<"\n";
 for(auto [k,v]:pcount)cout<<"value "<<k<<" subgroups "<<v<<"\n";
 for(auto &[sz,mp]:tab){cout<<"order "<<sz<<" ";for(auto [v,c]:mp)cout<<v<<":"<<c<<" ";cout<<"\n";}
}
