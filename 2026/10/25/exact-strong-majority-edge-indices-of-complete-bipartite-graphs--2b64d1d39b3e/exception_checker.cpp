#include <cstdio>
#include <vector>
#include <array>
#include <algorithm>
using namespace std;
int rows,cols,t;
long long examined=0,checks=0;
vector<vector<int>> patterns;vector<vector<int>> partial;

bool check(){
 int r=partial.size();
 for(int i=0;i<r;i++)for(int j=0;j<cols;j++){
  int ct[3]={0,0,0};
  for(int jj=0;jj<cols;jj++)if(jj!=j)ct[partial[i][jj]]++;
  for(int ii=0;ii<r;ii++)if(ii!=i)ct[partial[ii][j]]++;
  for(int c=0;c<3;c++)if(ct[c]>t)return false;
 }
 return true;
}
bool search(int lo){
 if((int)partial.size()==rows){examined++;return true;}
 for(int j=lo;j<(int)patterns.size();j++){
  partial.push_back(patterns[j]);
  checks++;
  if(check() && search(j))return true;
  partial.pop_back();
 }
 return false;
}
int main(){
 for(auto [m,n]:{pair<int,int>{3,4},{4,5}}){
 rows=m;cols=n;t=(m+n-2)/2;examined=checks=0;
 patterns.clear();partial.clear();
 int total=1;for(int i=0;i<n;i++)total*=3;
 for(int a=0;a<total;a++){
  int x=a;vector<int>row;
  for(int j=0;j<n;j++){row.push_back(x%3);x/=3;}
  patterns.push_back(row);
 }
 // All canonical first rows (up to color and column permutations), sorted by descending class sizes.
 vector<vector<int>> first;
 for(int a=n;a>=0;a--)for(int b=min(a,n-a);b>=0;b--){
  int c=n-a-b;
  if(c<0||c>b)continue;
  vector<int>v;
  for(int i=0;i<a;i++)v.push_back(0);
  for(int i=0;i<b;i++)v.push_back(1);
  for(int i=0;i<c;i++)v.push_back(2);
  first.push_back(v);
 }
 bool found=false;
 for(const auto &p:first){partial.clear();partial.push_back(p);if(search(0)){found=true;break;}}
 printf("m=%d n=%d canonical_first_rows=%zu examined_complete=%lld tested_partial=%lld exists_three=%s\n",m,n,first.size(),examined,checks,found?"yes":"no");
 }
}
