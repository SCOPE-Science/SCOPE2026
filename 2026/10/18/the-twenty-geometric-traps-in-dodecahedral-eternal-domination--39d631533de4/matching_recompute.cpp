// A second finite verification of all-guards-move defense on GP(10,2).
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
static constexpr int n=20;
static constexpr uint32_t FULL=(1u<<20)-1;
uint32_t adj[n]{};
vector<int> elems(uint32_t m){vector<int> v;while(m){int j=__builtin_ctz(m);v.push_back(j);m &= m-1;}return v;}
void edge(int a,int b){adj[a]|=1u<<b;adj[b]|=1u<<a;}
bool dom(uint32_t m){uint32_t v=m; for(int i:elems(m))v|=adj[i];return v==FULL;}

bool augment(int i,vector<int> const &src,vector<int> const &dst,vector<int>&match,uint32_t &seen){
    for(int j=0;j<(int)dst.size();++j){
        if((seen>>j)&1u) continue;
        if(dst[j]!=src[i] && ((adj[src[i]]>>dst[j])&1u)==0)continue;
        seen|=1u<<j;
        if(match[j]<0 || augment(match[j],src,dst,match,seen)){
            match[j]=i;return true;
        }
    }
    return false;
}
// Hall matching, not destination enumeration: a zero- or one-edge injective move
// exists precisely when a matching saturates all original guard positions.
bool move_possible(uint32_t s,uint32_t t){
    if(__builtin_popcount(s)!=__builtin_popcount(t))return false;
    auto src=elems(s),dst=elems(t);
    vector<int> match(src.size(),-1);
    for(int i=0;i<(int)src.size();++i){uint32_t seen=0;
        if(!augment(i,src,dst,match,seen))return false;}
    return true;
}
vector<uint32_t> getdom(int k){
    vector<uint32_t> ret;
    for(uint32_t m=0;m<=FULL;++m){
        if(__builtin_popcount(m)==k && dom(m))ret.push_back(m);
    }
    return ret;
}
struct Group {
 vector<uint32_t> states;
 vector<vector<int>> succ;
 vector<vector<int>> fatal;
};
Group analyze(int k){
 Group g;g.states=getdom(k);int count=g.states.size();
 g.succ.resize(count);g.fatal.resize(count);
 for(int i=0;i<count;++i)for(int j=0;j<count;++j)
    if(move_possible(g.states[i],g.states[j]))g.succ[i].push_back(j);
 for(int i=0;i<count;++i){uint32_t reachable=0;
    for(int j:g.succ[i])reachable|=g.states[j];
    uint32_t missed=FULL & ~reachable & ~g.states[i];
    g.fatal[i]=elems(missed);
 }
 return g;
}
vector<int> distances(int x){
 vector<int>d(n,-1);d[x]=0;vector<int>q(1,x);
 for(int h=0;h<(int)q.size();++h){int i=q[h];for(int j:elems(adj[i]))if(d[j]<0){d[j]=d[i]+1;q.push_back(j);}}
 return d;
}
int main(){
 for(int i=0;i<10;++i){edge(i,(i+1)%10);edge(i,i+10);edge(i+10,10+(i+2)%10);}
 vector<pair<int,int>> es;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)if((adj[i]>>j)&1u)es.push_back({i,j});
 assert(es.size()==30);for(int i=0;i<n;++i)assert(__builtin_popcount(adj[i])==3);
 for(int k=1;k<=5;++k){auto v=getdom(k);if(!v.empty())return 10;cout<<"D"<<k<<"_COUNT "<<v.size()<<"\n";}
 Group g6=analyze(6),g7=analyze(7);
 if(g6.states.size()!=10||g7.states.size()!=780)return 11;
 for(int i=0;i<(int)g6.states.size();++i){
   if(g6.fatal[i].size()!=2)return 12;
   cout<<"F6 "<<g6.states[i];for(int a:g6.fatal[i])cout<<" "<<a;cout<<"\n";
 }
 set<uint32_t> bad,good;
 map<uint32_t,int> fatal_by_mask;
 for(int i=0;i<(int)g7.states.size();++i){
   auto s=g7.states[i];if(g7.fatal[i].empty())good.insert(s);
   else {if(g7.fatal[i].size()!=1)return 13;
      bad.insert(s);fatal_by_mask[s]=g7.fatal[i][0];}
 }
 if(bad.size()!=20||good.size()!=760)return 14;
 for(int x=0;x<n;++x){
   auto d=distances(x);uint32_t b=0;vector<int>num(6,0);
   for(int v=0;v<n;++v){if(d[v]<0||d[v]>5)return 15;
      num[d[v]]++;if(d[v]==1||d[v]>=4)b|=1u<<v;}
   if(num!=vector<int>({1,3,6,6,3,1}))return 16;
   if(!bad.count(b)||fatal_by_mask[b]!=x)return 17;
 }
 int minimum=100000;
 for(int i=0;i<(int)g7.states.size();++i){
   auto s=g7.states[i];if(!good.count(s))continue;
   for(int a=0;a<n;++a)if(((s>>a)&1u)==0){
      int m=0;
      for(int j:g7.succ[i])if(good.count(g7.states[j])&&((g7.states[j]>>a)&1u))++m;
      if(m==0)return 18;
      minimum=min(minimum,m);
   }
 }
 for(int i=0;i<(int)g7.states.size();++i)cout<<"D7 "<<g7.states[i]<<"\n";
 for(auto s:bad)cout<<"F7 "<<s<<" "<<fatal_by_mask[s]<<"\n";
 cout<<"RESULT D6=10 D7=780 BAD7=20 GOOD7=760 MINGOOD="<<minimum<<"\n";
 return 0;
}
