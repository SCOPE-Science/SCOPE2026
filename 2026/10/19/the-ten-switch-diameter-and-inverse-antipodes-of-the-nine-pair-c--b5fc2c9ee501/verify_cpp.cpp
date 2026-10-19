// Independent crown-graph perfect-matching enumeration and switch-metric verifier.
// Requires C++17; no external libraries or data files.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using Assignment = array<unsigned char,9>;
struct Profile {vector<int> type; int orbit=0,ecc=0,reached=0,far=0; bool inverse=false; vector<int> hist;};
struct Outcome {int n=0,count=0,edges=0,radius=0,diameter=0;bool connected=true;vector<Profile> rows;};
static int N;
static vector<Assignment> matchings;
static unordered_map<uint64_t,int> lookup;
static uint64_t encode(const Assignment &a){uint64_t x=0;for(int i=0;i<N;i++)x|=uint64_t(a[i])<<(4*i);return x;}
static void backtrack(int row,unsigned mask,Assignment &a){
 if(row==N){int index=int(matchings.size());uint64_t key=encode(a);auto r=lookup.emplace(key,index);assert(r.second);matchings.push_back(a);return;}
 for(int partner=0;partner<N;partner++)if(partner!=row && !(mask&(1u<<partner))){
  a[row]=partner;backtrack(row+1,mask|(1u<<partner),a);
 }
}
static vector<int> cycletype(const Assignment &a){
 int seen=0;vector<int> lens;
 for(int x=0;x<N;x++)if(!(seen&(1<<x))){int len=0,y=x;do{seen|=1<<y;len++;y=a[y];}while(y!=x);lens.push_back(len);}
 sort(lens.begin(),lens.end());return lens;
}
static Outcome run(int n){
 N=n;matchings.clear();lookup.clear();lookup.reserve(150000);
 Assignment a{};backtrack(0,0,a);
 Outcome o;o.n=n;o.count=matchings.size();
 map<vector<int>,pair<int,int>> classes;
 for(int i=0;i<o.count;i++){
  auto type=cycletype(matchings[i]);auto &p=classes[type];
  if(p.second==0)p.first=i;
  p.second++;
 }
 long long degrees=0;
 for(const auto &p:matchings){
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(p[i]!=j && p[j]!=i)degrees++;
 }
 assert(degrees%2==0);o.edges=degrees/2;
 for(auto const &it:classes){
  int source=it.second.first; Profile pr;pr.type=it.first;pr.orbit=it.second.second;
  vector<int> dist(o.count,-1);deque<int> q;dist[source]=0;q.push_back(source);
  while(!q.empty()){
   int v=q.front();q.pop_front();int dv=dist[v];
   if(int(pr.hist.size())<=dv)pr.hist.resize(dv+1,0);
   pr.hist[dv]++;
   const Assignment &p=matchings[v];
   for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(p[i]!=j && p[j]!=i){
    Assignment tmp=p;swap(tmp[i],tmp[j]);
    auto next=lookup.find(encode(tmp));assert(next!=lookup.end());int w=next->second;
    if(dist[w]<0){dist[w]=dv+1;q.push_back(w);}
   }
  }
  pr.ecc=int(pr.hist.size())-1;
  pr.reached=accumulate(pr.hist.begin(),pr.hist.end(),0);
  auto p=matchings[source];Assignment inv{};for(int i=0;i<n;i++)inv[p[i]]=i;
  int ant=lookup.find(encode(inv))->second;
  pr.far=0;int farthest=-1;
  for(int v=0;v<o.count;v++)if(dist[v]==pr.ecc){pr.far++;farthest=v;}
  pr.inverse=(pr.far==1 && farthest==ant);
  o.connected &= (pr.reached==o.count);o.rows.push_back(pr);
 }
 o.radius=100000;o.diameter=0;
 for(auto &r:o.rows){o.radius=min(o.radius,r.ecc);o.diameter=max(o.diameter,r.ecc);}
 return o;
}
static void arr(const vector<int> &a){cout<<'[';for(size_t j=0;j<a.size();j++){if(j)cout<<',';cout<<a[j];}cout<<']';}
int main(){
 cout<<"{\"method\":\"independent column-assignment search and direct switch BFS\",\"results\":[";
 for(int n=4;n<=9;n++){
  Outcome r=run(n);
  if(n!=4)cout<<',';
  cout<<"{\"n\":"<<n<<",\"vertices\":"<<r.count<<",\"edges\":"<<r.edges<<",\"connected\":"<<(r.connected?"true":"false")<<",\"radius\":"<<r.radius<<",\"diameter\":"<<r.diameter<<",\"types\":[";
  for(size_t i=0;i<r.rows.size();i++){
   if(i)cout<<',';
   auto &p=r.rows[i];cout<<"{\"cycle_type\":";arr(p.type);
   cout<<",\"count\":"<<p.orbit<<",\"eccentricity\":"<<p.ecc<<",\"reached\":"<<p.reached<<",\"farthest_count\":"<<p.far<<",\"inverse_unique_antipode\":"<<(p.inverse?"true":"false")<<",\"distance_counts\":";arr(p.hist);cout<<'}';
  }
  cout<<"]}";
  int reference[6]={3,4,6,7,8,10}; assert(r.diameter==reference[n-4]);
  if(n==9){assert(r.count==133496 && r.edges==int(r.edges));int cnt=0;for(auto &p:r.rows)if(p.ecc==10){assert(p.type==vector<int>({3,3,3}) && p.orbit==2240 && p.far==1 && p.inverse);cnt++;}assert(cnt==1);}
 }
 cout<<"]}\n";
}
