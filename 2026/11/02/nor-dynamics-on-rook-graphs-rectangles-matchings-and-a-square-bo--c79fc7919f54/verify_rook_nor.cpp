// Exhaustive finite checks for the open-neighborhood NOR map on rook graphs.
// Standalone reproducibility code; no external dependencies beyond C++17.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using ull = unsigned long long;

ull comb(int n,int k){if(k<0||k>n)return 0;ull z=1;for(int j=1;j<=k;j++)z=z*(n-k+j)/j;return z;}
ull fact(int n){ull z=1;for(int j=1;j<=n;j++)z*=j;return z;}
bool feasible(int p,int q){return (p==0&&q==0)||(p>=1&&q>=1&&p+q>=3);}
ull predicted(int a,int b){
 ull match=0,rect=0;
 for(int k=0;k<=min(a,b);k++)match+=comb(a,k)*comb(b,k)*fact(k);
 if(a==b)match-=a*fact(a);
 for(int r=1;r<=a;r++)for(int c=1;c<=b;c++)if(r*c>=2)
  for(int k=0;k<=min(a-r,b-c);k++)if(feasible(a-r-k,b-c-k))
   rect+=comb(a,r)*comb(b,c)*comb(a-r,k)*comb(b-c,k)*fact(k);
 return match+rect;
}
uint32_t step(uint32_t s,int a,int b){
 int r[8]={0},c[12]={0};
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(s&(1U<<(i*b+j))){r[i]++;c[j]++;}
 uint32_t ans=0;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++){
  bool bit=(s&(1U<<(i*b+j)))!=0;
  if(r[i]==(int)bit && c[j]==(int)bit)ans|=1U<<(i*b+j);
 }
 return ans;
}
// Classify a proposed period state directly from its occupied cells.
bool structural(uint32_t s,int a,int b){
 int row[8]={0},col[12]={0};
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(s&(1U<<(i*b+j))){row[i]++;col[j]++;}
 bool matching=true;
 int k=0;
 for(int i=0;i<a;i++)if(row[i]>1)matching=false;
 for(int j=0;j<b;j++)if(col[j]>1)matching=false;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(s&(1U<<(i*b+j)))k++;
 if(matching)return !(a==b && k==a-1);
 // A nonmatching must be a disjoint nontrivial full rectangle and matching.
 int usedrows[8]={0},usedcols[12]={0};
 for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(s&(1U<<(i*b+j)))
  if(row[i]>1 || col[j]>1){usedrows[i]=1;usedcols[j]=1;}
 int r=0,c=0,isolated=0;
 for(int i=0;i<a;i++)r+=usedrows[i];
 for(int j=0;j<b;j++)c+=usedcols[j];
 if(r*c<2)return false;
 for(int i=0;i<a;i++)for(int j=0;j<b;j++){
  bool bit=!!(s&(1U<<(i*b+j)));
  if(usedrows[i]&&usedcols[j]&&!bit)return false;
  if(bit && (usedrows[i]!=usedcols[j]))return false;
  if(bit&&!usedrows[i]&&!usedcols[j]){
   if(row[i]!=1||col[j]!=1)return false;
   isolated++;
  }
 }
 return feasible(a-r-isolated,b-c-isolated);
}

int main(){
 ull total=0;
 for(int a=2;a<=4;a++)for(int b=a;b<=10;b++){
  if(a*b>20)continue;
  const uint32_t states=1U<<(a*b);
  set<uint32_t> image;
  for(uint32_t s=0;s<states;s++){
   uint32_t t=step(s,a,b);
   assert(step(step(t,a,b),a,b)==t); // F^3 = F.
   image.insert(t);
  }
  ull expected=predicted(a,b);
  ull fixed=0;
  for(auto s:image){
   if(!structural(s,a,b)){
    cerr<<"STRUCTURAL_MISMATCH "<<a<<" "<<b<<" "<<s<<"\n";return 1;
   }
   if(step(s,a,b)==s)fixed++;
  }
  for(uint32_t s=0;s<states;s++)if(structural(s,a,b) && !image.count(s)){
   cerr<<"MISSING_PERIODIC "<<a<<" "<<b<<" "<<s<<"\n";return 1;
  }
  ull fixpred=fact(b)/fact(b-a);
  if(expected!=image.size()||fixed!=fixpred){
   cerr<<"COUNT_MISMATCH "<<a<<" "<<b<<" "<<expected<<" "<<image.size()<<" "<<fixed<<" "<<fixpred<<"\n";return 1;
  }
  ull orbits=(expected-fixed)/2;
  if(a==2 && b>=3 && orbits!=(1ULL<<b)-1){
   cerr<<"TWO_ROW_MISMATCH "<<a<<" "<<b<<"\n";return 1;
  }
  cout<<"PASS "<<a<<"x"<<b<<" states="<<states<<" recurrent="<<image.size()<<" fixed="<<fixed<<" primitive_two_orbits="<<orbits<<"\n";
  total+=states;
 }
 cout<<"ALL_CHECKS_PASSED exhaustive_configuration_checks="<<total<<"\n";
}
