#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using ll = long long;

ll choose(int n,int k){if(k<0||k>n)return 0;ll v=1;for(int i=1;i<=k;i++)v=v*(n-i+1)/i;return v;}
ll fact(int n){ll v=1;for(int i=2;i<=n;i++)v*=i;return v;}

vector<ll> predicted(const vector<int>& a){
 int r=a.size(), n=accumulate(a.begin(),a.end(),0);vector<ll> answer(n+1);
 answer[n]+=fact(r+1);
 for(int j=0;j<r;j++){
  if(a[j]<2)continue;
  vector<ll> noempty(n+1), oneempty(n+1);
  noempty[0]=1;
  for(int i=0;i<r;i++)if(i!=j){
   vector<ll> next0(n+1),next1(n+1);
   for(int s=0;s<=n;s++){
    next1[s]+=noempty[s];
    for(int t=1;t<=a[i]&&s+t<=n;t++){
     next0[s+t]+=noempty[s]*choose(a[i],t);
     next1[s+t]+=oneempty[s]*choose(a[i],t);
    }
   }
   noempty.swap(next0);oneempty.swap(next1);
  }
  ll mult=fact(r+1)/2*((1LL<<a[j])-2);
  for(int s=0;s+a[j]<=n;s++)answer[s+a[j]]+=mult*(noempty[s]+oneempty[s]);
 }
 return answer;
}

vector<ll> exhaustive(const vector<int>& a){
 int r=a.size(),lambda=r+1,n=accumulate(a.begin(),a.end(),0);
 vector<int> part,vals(n);
 for(int i=0;i<r;i++)for(int k=0;k<a[i];k++)part.push_back(i);
 long long total=1;for(int i=0;i<n;i++)total*=lambda+1;
 vector<ll> answer(n+1,0);
 for(long long num=0;num<total;num++){
  long long q=num;int colored=0;
  vector<int> mask(r,0);
  for(int i=0;i<n;i++){
   vals[i]=q%(lambda+1);q/=(lambda+1);
   if(vals[i]){colored++; mask[part[i]]|=1<<(vals[i]-1);}
  }
  bool stable=true;
  for(int i=0;i<r&&stable;i++)for(int j=i+1;j<r;j++)
   if(mask[i]&mask[j]){stable=false;break;}
  if(!stable)continue;
  bool changed=true;
  while(changed){
   changed=false;
   for(int i=0;i<n;i++)if(vals[i]==0){
    int seen=0;
    for(int j=0;j<n;j++)if(part[j]!=part[i] && vals[j])seen|=1<<(vals[j]-1);
    if(__builtin_popcount((unsigned)seen)==lambda-1){
     int remaining=((1<<lambda)-1)^seen;
     vals[i]=__builtin_ctz((unsigned)remaining)+1;
     changed=true;
    }
   }
  }
  if(any_of(vals.begin(),vals.end(),[](int v){return v==0;}))continue;
  for(int i=0;i<n&&stable;i++)for(int j=i+1;j<n;j++)
   if(part[i]!=part[j]&&vals[i]==vals[j]){stable=false;break;}
  if(stable)answer[colored]++;
 }
 return answer;
}

void profiles(int r,int idx,int prev,vector<int>& a,ll& tests,ll& states){
 if(idx==r){
  int n=accumulate(a.begin(),a.end(),0);
  if(n>8)return;
  vector<ll> p=predicted(a),b=exhaustive(a);
  if(p!=b){
   cerr<<"FAIL profile";for(int x:a)cerr<<" "<<x;cerr<<"\n";
   cerr<<"predicted:";for(auto x:p)cerr<<" "<<x;cerr<<"\n";
   cerr<<"exhaustive:";for(auto x:b)cerr<<" "<<x;cerr<<"\n";
   exit(1);
  }
  tests++;
  ll cells=1;for(int j=0;j<n;j++)cells*=r+2;
  states+=cells;
  return;
 }
 for(int t=prev;t<=4;t++){
  a.push_back(t);profiles(r,idx+1,t,a,tests,states);a.pop_back();
 }
}
int main(){
 ll tests=0,states=0;
 for(int r=2;r<=4;r++){
  vector<int> a;profiles(r,0,1,a,tests,states);
 }
 cout<<"PASS: "<<tests<<" multipartite profiles, "<<states<<" initial assignments checked\n";
 for(auto a:vector<vector<int>>{{1,1},{1,2},{2,2},{2,3},{1,1,2},{2,2,2},{1,2,2,2}}){
  auto v=predicted(a);cout<<"profile";
  for(auto x:a)cout<<" "<<x;
  cout<<" : fcol_by_seed_size";
  for(auto x:v)cout<<" "<<x;
  cout<<"\n";
 }
 return 0;
}
