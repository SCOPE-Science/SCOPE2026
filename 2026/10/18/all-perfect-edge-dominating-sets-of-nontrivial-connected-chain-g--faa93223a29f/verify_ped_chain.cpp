#include <bits/stdc++.h>
using namespace std;
// Exhaustive verifier for perfect edge domination in connected chain graphs.
// Build: g++ -std=c++17 -O2 verify_ped_chain.cpp -o verify_ped_chain
// Run: ./verify_ped_chain
uint64_t profiles=0,subsets=0,valid_count=0;
int max_edges=0;
void verify(const vector<int>& alpha,const vector<int>& beta){
 const int p=alpha.size();
 vector<int> al,be;
 for(int i=0;i<p;i++)for(int j=0;j<alpha[i];j++)al.push_back(i);
 for(int i=0;i<p;i++)for(int j=0;j<beta[i];j++)be.push_back(i);
 int na=al.size(),nb=be.size(),n=na+nb;
 vector<pair<int,int>> E;
 for(int i=0;i<na;i++)for(int j=0;j<nb;j++)if(be[j]<=al[i])E.push_back({i,na+j});
 const int m=E.size();if(m>19)return;
 max_edges=max(max_edges,m);
 vector<uint64_t> predicted={(1ULL<<m)-1};
 for(int v=0;v<n;v++)if((v<na && al[v]==p-1)||(v>=na && be[v-na]==0)){
  uint64_t mask=0;
  for(int e=0;e<m;e++)if(E[e].first==v||E[e].second==v)mask|=1ULL<<e;
  predicted.push_back(mask);
 }
 if(p==2 && alpha[1]==1 && beta[0]==1){
  int v=-1,w=-1;
  for(int i=0;i<na;i++)if(al[i]==1)v=i;
  for(int j=0;j<nb;j++)if(be[j]==0)w=na+j;
  for(int e=0;e<m;e++)if(E[e]==make_pair(v,w))predicted.push_back(1ULL<<e);
 }
 sort(predicted.begin(),predicted.end());
 predicted.erase(unique(predicted.begin(),predicted.end()),predicted.end());
 vector<uint64_t> actual;
 for(uint64_t mask=0;mask<(1ULL<<m);mask++){
  vector<int> d(n,0);
  for(int e=0;e<m;e++)if((mask>>e)&1){auto [u,v]=E[e];d[u]++;d[v]++;}
  bool ok=true;
  for(int e=0;e<m;e++)if(!((mask>>e)&1)){
   auto [u,v]=E[e];if(d[u]+d[v]!=1){ok=false;break;}
  }
  if(ok)actual.push_back(mask);
 }
 if(actual!=predicted){
  cerr<<"FAIL A=[";for(auto a:alpha)cerr<<a<<",";
  cerr<<"] B=[";for(auto b:beta)cerr<<b<<",";
  cerr<<"] m="<<m<<" got="<<actual.size()<<" expected="<<predicted.size()<<"\n";
  for(auto x:actual)if(!binary_search(predicted.begin(),predicted.end(),x))cerr<<"Unexpected="<<x<<"\n";
  for(auto x:predicted)if(!binary_search(actual.begin(),actual.end(),x))cerr<<"Missing="<<x<<"\n";
  exit(1);
 }
 profiles++;subsets+=(1ULL<<m);valid_count+=actual.size();
}
void gen(int p,int index,int remaining,vector<int>&alpha,vector<int>&beta){
 if(index==2*p){if(remaining==0)verify(alpha,beta);return;}
 int lo=2*p-index-1;
 for(int v=1;v<=remaining-lo;v++){
  if(index<p){alpha.push_back(v);gen(p,index+1,remaining-v,alpha,beta);alpha.pop_back();}
  else {beta.push_back(v);gen(p,index+1,remaining-v,alpha,beta);beta.pop_back();}
 }
}
int main(){
 for(int total=2;total<=12;total++)for(int p=1;p<=min(5,total/2);p++){
  vector<int> a,b;gen(p,0,total,a,b);
 }
 cout<<"Exact candidate sets matched for every examined chain-graph profile.\n";
 cout<<"Profiles: "<<profiles<<"\n";
 cout<<"Edge subsets examined: "<<subsets<<"\n";
 cout<<"Perfect edge dominating sets: "<<valid_count<<"\n";
 cout<<"Largest tested edge count: "<<max_edges<<"\n";
}
