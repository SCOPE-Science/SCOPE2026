// Independent ternary enumeration without symbol-canonicalization.
// Parikh vectors are represented by three independent base-32 digits.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
constexpr int N=16;
array<vector<uint64_t>,N+1> all;
int p[N+1];
uint64_t codes[N+1];
void grow(int n){
 all[n].push_back(codes[n]);
 if(n==N)return;
 for(int a=0;a<3;a++){
  p[n+1]=p[n]+(1<<(5*a));
  int best=0;
  for(int j=1;j<=n;j++)if(p[j]==p[n+1]-p[n+1-j])best=j;
  codes[n+1]=codes[n] | ((uint64_t)best << (4*n));
  grow(n+1);
 }
}
int main(){
 p[0]=0;p[1]=1;codes[1]=0;grow(1);
 for(int n=1;n<=N;n++){
   auto &v=all[n];sort(v.begin(),v.end());
   cout << n << " " << v.size() << " " << (unique(v.begin(),v.end())-v.begin()) << "\n";
 }
}
