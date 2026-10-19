// Exact independent enumerations of 1-gap 3-binomial profiles, q=3.
// This verification program contains only mathematical algorithms and no external dependencies.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using Profile=array<uint8_t,39>;
struct Record {Profile p{}; uint32_t id=0; bool operator<(Record const&b) const{return p<b.p;}};
struct Census {uint64_t distinct=0, nontriv=0; vector<pair<uint32_t,uint32_t>> pairs; uint64_t max_class=0;};
uint32_t power3(int n){uint32_t x=1;while(n--)x*=3;return x;}
array<uint8_t,13> decode(uint32_t id,int n){array<uint8_t,13> a{}; for(int j=n-1;j>=0;j--){a[j]=id%3;id/=3;}return a;}
Profile direct(const array<uint8_t,13>&w,int n){
 Profile v{};
 for(int i=0;i<n;i++){
  v[w[i]]++;
  for(int j=i+2;j<n;j++){
   v[3+3*w[i]+w[j]]++;
   for(int k=j+2;k<n;k++)v[12+9*w[i]+3*w[j]+w[k]]++;
  }
 }
 return v;
}
Census summarize(vector<Record> &records){
 sort(records.begin(),records.end());Census c;
 for(size_t i=0;i<records.size();){size_t j=i+1;
  while(j<records.size()&&records[j].p==records[i].p)j++;
  c.distinct++;c.max_class=max(c.max_class,uint64_t(j-i));
  if(j>i+1){ c.nontriv++; if(j-i!=2)throw runtime_error("class larger than two");
   auto a=records[i].id,b=records[i+1].id; if(a>b)swap(a,b);c.pairs.emplace_back(a,b);
  }
  i=j;
 }
 sort(c.pairs.begin(),c.pairs.end());return c;
}
Census run_direct(int n){vector<Record> a(power3(n));for(uint32_t i=0;i<a.size();i++){a[i].id=i;a[i].p=direct(decode(i,n),n);}return summarize(a);}
struct State {Profile p{};array<uint8_t,9> last_pairs{};array<uint8_t,3> singles{};int last=-1;};
void grow(State const&s,int len,int n,uint32_t id,vector<Record>&out){
 if(len==n){out.push_back({s.p,id});return;}
 for(int x=0;x<3;x++){
  State t=s;
  if(len>0){
   for(int a=0;a<3;a++)for(int b=0;b<3;b++){
    int oldpair=s.p[3+3*a+b];
    if(oldpair<s.last_pairs[3*a+b])throw runtime_error("pair bookkeeping");
    t.p[12+9*a+3*b+x]+=oldpair-s.last_pairs[3*a+b];
   }
   for(int a=0;a<3;a++)t.p[3+3*a+x]+=s.singles[a]-(s.last==a);
  }
  t.last_pairs.fill(0);
  if(len>0)for(int a=0;a<3;a++)t.last_pairs[3*a+x]=s.singles[a]-(s.last==a);
  t.p[x]++; t.singles[x]++; t.last=x;
  grow(t,len+1,n,id*3+x,out);
 }
}
Census run_incremental(int n){vector<Record> a;a.reserve(power3(n));State s;grow(s,0,n,0,a);return summarize(a);}
int distinct_symbols_pair(int n,uint32_t a,uint32_t b){auto x=decode(a,n),y=decode(b,n);bool seen[3]={};for(int i=0;i<n;i++){seen[x[i]]=true;seen[y[i]]=true;}return seen[0]+seen[1]+seen[2];}
int main(){
 try{
  for(int n=1;n<=13;n++){
   Census a=run_direct(n), b=run_incremental(n);
   if(a.distinct!=b.distinct || a.nontriv!=b.nontriv || a.max_class!=b.max_class || a.pairs!=b.pairs)throw runtime_error("independent mismatch");
   if(n<13){if(n>=5 && (a.distinct!=power3(n) || a.nontriv))throw runtime_error("premature collision for n>=5");}
   else{
    if(a.distinct!=1594311 || a.nontriv!=12 || a.max_class!=2)throw runtime_error("wrong 13-classification");
    for(auto [u,v]:a.pairs)if(distinct_symbols_pair(n,u,v)!=2)throw runtime_error("nonbinary collision");
    int cnt[3]={}; for(auto [u,v]:a.pairs){auto x=decode(u,n),y=decode(v,n);bool z[3]={};for(int i=0;i<n;i++){z[x[i]]=true;z[y[i]]=true;}for(int k=0;k<3;k++)if(!z[k])cnt[k]++;}
    if(cnt[0]!=4||cnt[1]!=4||cnt[2]!=4)throw runtime_error("relabeling count");
   }
   cout << "n=" << n << " q=3 profiles=" << a.distinct << " pairs=" << a.nontriv << " max_class=" << a.max_class << " methods=agree\n";
  }
  cout<<"PASS: two complete exact enumerators; arbitrary-alphabet reduction is mathematical.\n";
 }catch(exception const&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
