#include <bits/stdc++.h>
using namespace std;
constexpr int M=124, K=7;
using Ull=unsigned long long;
int a[K],sums[64];
long long combinations=0,passedSubset=0,good=0;
vector<array<int,K>> hits;
// direct disassociation via generating the 64 possible subset sums, no cyclic-bit-rotation recurrence.
bool injective(){
  char seen[M]={0};
  sums[0]=0;
  int len=1;
  for(int j=1;j<K;j++){
    for(int i=0;i<len;i++)sums[len+i]=(sums[i]+a[j])%M;
    len*=2;
  }
  for(int i=0;i<64;i++) {int q=sums[i];if(seen[q])return false;seen[q]=1;}
  return true;
}
// Enumerate every nonnegative multiplicity vector of sum seven, directly.
bool nontriv(int pos,int remain,int cur,bool changed,int target){
 if(pos==6){return (changed||remain!=1)&&((cur+remain*a[pos])%M==target);}
 for(int q=0;q<=remain;q++)if(nontriv(pos+1,remain-q,(cur+q*a[pos])%M,changed||q!=1,target))return true;
 return false;
}
int main(){
 a[0]=0;a[1]=1;
 for(int b=2;b<=119;b++)for(int c=b+1;c<=120;c++)for(int d=c+1;d<=121;d++)for(int e=d+1;e<=122;e++)for(int f=e+1;f<=123;f++){
  a[2]=b;a[3]=c;a[4]=d;a[5]=e;a[6]=f;
  combinations++;
  if(!injective())continue;
  passedSubset++;
  int target=(1+b+c+d+e+f)%M;
  if(nontriv(0,7,0,false,target))continue;
  good++;
  array<int,K> x;copy(a,a+K,x.begin());hits.push_back(x);
 }
 cerr<<"all_combinations="<<combinations<<" subset_distinct="<<passedSubset<<" valid="<<good<<"\n";
 for(const auto &x:hits){for(int y:x)cout<<y<<' ';cout<<'\n';}
}
