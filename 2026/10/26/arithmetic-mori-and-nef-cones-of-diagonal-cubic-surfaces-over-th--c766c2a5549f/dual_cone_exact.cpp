// Exact enumeration of extremal rays of the dual of an integer cone.
// Input: r n followed by r*n column-coordinate entries, row major.
// Enumerates all sets of r-1 active independent inequalities.
#include <iostream>
#include <vector>
#include <set>
#include <numeric>
#include <algorithm>
#include <cstdlib>
#include <cstdint>
using namespace std;
using i64=long long;
static i64 det(vector<vector<i64>> x) {
 int n=(int)x.size(); if(n==0)return 1;
 i64 prev=1, sign=1;
 for(int k=0;k<n-1;k++) {
  int p=k;while(p<n && x[p][k]==0)++p;
  if(p==n)return 0;
  if(p!=k){swap(x[k],x[p]);sign=-sign;}
  const i64 pivot=x[k][k];
  for(int i=k+1;i<n;i++)for(int j=k+1;j<n;j++) {
   const i64 v=x[i][j]*pivot-x[i][k]*x[k][j];
   if(v%prev){cerr<<"nonintegral Bareiss division\n";exit(3);}
   x[i][j]=v/prev;
  }
  for(int i=k+1;i<n;i++)x[i][k]=0;
  prev=pivot;
 }
 return sign*x[n-1][n-1];
}
int main(){
 ios::sync_with_stdio(false);cin.tie(nullptr);
 int r,n;if(!(cin>>r>>n)||r<1||r>7||n<r||n>30)return 4;
 vector<vector<i64>> A(r,vector<i64>(n));
 for(int i=0;i<r;i++)for(int j=0;j<n;j++)cin>>A[i][j];
 set<vector<i64>> rays;long long subsets=0,independent=0;
 vector<int> idx;
 auto visit=[&](){
  ++subsets; vector<i64> v(r);
  for(int omit=0;omit<r;omit++){
   vector<vector<i64>> minor(r-1,vector<i64>(r-1));
   for(int i=0;i<r-1;i++)for(int j=0,k=0;j<r;j++)if(j!=omit)minor[i][k++]=A[j][idx[i]];
   v[omit]=(omit%2?-1:1)*det(minor);
  }
  i64 g=0;for(i64 x:v)g=std::gcd(g,std::llabs(x));if(g==0)return;
  ++independent;
  for(auto &x:v)x/=g;
  bool nonnegative=true,nonpositive=true;
  for(int j=0;j<n;j++){
   i64 dot=0;for(int i=0;i<r;i++)dot+=v[i]*A[i][j];
   if(dot<0)nonnegative=false;
   if(dot>0)nonpositive=false;
  }
  if(!nonnegative&&!nonpositive)return;
  if(nonpositive)for(auto &x:v)x=-x;
  rays.insert(v);
 };
 auto recurse=[&](auto&& self,int begin,int left)->void{
  if(left==0){visit();return;}
  for(int j=begin;j<=n-left;j++){
   idx.push_back(j);self(self,j+1,left-1);idx.pop_back();
  }
 };
 recurse(recurse,0,r-1);
 cout<<"EXACT_DUAL "<<r<<" "<<n<<" "<<rays.size()<<" "<<subsets<<" "<<independent<<"\n";
 return 0;
}
