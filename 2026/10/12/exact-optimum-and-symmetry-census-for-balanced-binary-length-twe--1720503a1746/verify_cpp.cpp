#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
static constexpr int MAXN=300, WORDS=5;
struct Bits {
 array<uint64_t,WORDS> v{};
 bool any() const {for(auto x:v) if(x)return true;return false;}
 int count() const {int s=0;for(auto x:v)s+=__builtin_popcountll(x);return s;}
 void set(int x){v[x>>6]|=1ULL<<(x&63);}
 void reset(int x){v[x>>6]&=~(1ULL<<(x&63));}
 Bits operator&(const Bits& b)const {Bits r;for(int i=0;i<WORDS;i++)r.v[i]=v[i]&b.v[i];return r;}
 Bits operator|(const Bits& b)const {Bits r;for(int i=0;i<WORDS;i++)r.v[i]=v[i]|b.v[i];return r;}
 Bits minus(const Bits& b)const {Bits r;for(int i=0;i<WORDS;i++)r.v[i]=v[i]&~b.v[i];return r;}
 template<class F> void each(F f)const{for(int j=0;j<WORDS;j++){uint64_t m=v[j];while(m){int bit=__builtin_ctzll(m);f(64*j+bit);m &= m-1;}}}
};
vector<string> words;
vector<Bits> neighbors;
map<int,uint64_t> maximal_hist;
vector<vector<int>> maxima;
uint64_t bk_calls=0;
static bool unbordered(const string&s){int n=s.size();for(int k=1;k<n;k++)if(s.substr(0,k)==s.substr(n-k,k))return false;return true;}
static bool compatible(const string&a,const string&b){int n=a.size(),d=0;for(int i=0;i<n;i++)d+=(a[i]!=b[i]);if(d<4)return false;for(int k=1;k<n;k++){if(a.compare(0,k,b,n-k,k)==0 || b.compare(0,k,a,n-k,k)==0)return false;}return true;}
void bk(Bits P,Bits X,vector<int>&cur){
 ++bk_calls;
 if(!P.any()&&!X.any()){
   int k=cur.size();maximal_hist[k]++;
   if(k>=(int)(maxima.empty()?0:maxima[0].size())){
     if(maxima.empty() || k>(int)maxima[0].size())maxima.clear();
     maxima.push_back(cur);
   }
   return;
 }
 Bits U=P|X;int pivot=-1,best=-1;
 U.each([&](int j){int s=(P&neighbors[j]).count();if(s>best){best=s;pivot=j;}});
 Bits candidates=(pivot<0?P:P.minus(neighbors[pivot]));
 vector<int> todo; candidates.each([&](int v){todo.push_back(v);});
 for(int v:todo){
   cur.push_back(v);
   bk(P&neighbors[v],X&neighbors[v],cur);
   cur.pop_back();
   P.reset(v);X.set(v);
 }
}
int main(int argc,char**argv){
 int n=12;for(int v=0;v<(1<<n);v++){
  if(__builtin_popcount((unsigned)v)!=n/2)continue;
  string s;for(int i=n-1;i>=0;i--)s+=((v>>i)&1)?'1':'0';
  if(unbordered(s))words.push_back(s);
 }
 int N=words.size();if(N>MAXN){cerr<<"Too many vertices";return 2;}
 neighbors.resize(N);uint64_t edges=0;
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(compatible(words[i],words[j])){neighbors[i].set(j);neighbors[j].set(i);edges++;}
 Bits P;for(int i=0;i<N;i++)P.set(i);
 vector<int> cur;bk(P,{},cur);
 for(auto &c:maxima)sort(c.begin(),c.end());
 sort(maxima.begin(),maxima.end());
 if(argc>1){ofstream out(argv[1]);if(!out){cerr<<"cannot open";return 2;}
 for(const auto&c:maxima){for(int j=0;j<(int)c.size();j++){if(j)out<<' ';out<<words[c[j]];}out<<'\n';}}
 cout<<"vertices="<<N<<" edges="<<edges<<" bk_calls="<<bk_calls<<" maximal_cliques=";
 uint64_t total=0;for(auto [k,num]:maximal_hist)total+=num;cout<<total<<" max="<<maxima[0].size()<<" optimizers="<<maxima.size()<<"\n";
 for(auto [k,num]:maximal_hist)cout<<"maximal_size_"<<k<<"="<<num<<"\n";
}
