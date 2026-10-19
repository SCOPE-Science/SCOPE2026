// Exact finite cyclic-factor-orbit enumeration for the binary Rudin--Shapiro word.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
using namespace std;
static const array<string,4> image={"01","02","31","32"};
string step(const string& s){string t;t.reserve(2*s.size());for(char c:s)t+=image[c-'0'];return t;}
string binary(const string& s){string t=s;for(char& c:t)c=(c<'2'?'0':'1');return t;}
// Booth's exact lexicographically least cyclic rotation, linear time.
string rotation(const string& s){int n=(int)s.size(),i=0,j=1,k=0;
 while(i<n&&j<n&&k<n){char a=s[(i+k)%n],b=s[(j+k)%n];
 if(a==b){++k;continue;}
 if(a>b){i+=k+1;if(i<=j)i=j+1;}else{j+=k+1;if(j<=i)j=i+1;}k=0;}
 int p=min(i,j);return s.substr(p)+s.substr(0,p);}
string slow_rotation(const string& s){string best=s;for(int i=1;i<(int)s.size();i++){
 string t=s.substr(i)+s.substr(0,i);if(t<best)best=t;}return best;}
char parity11(unsigned int v){unsigned int q=(v&(v>>1));char parity=0;while(q){parity^=1;q&=q-1;}return char('0'+parity);}
int main(){
 string fixed="0";for(int j=0;j<14;j++)fixed=step(fixed);
 set<string> pairs;for(size_t j=0;j+1<fixed.size();j++)pairs.insert(fixed.substr(j,2));
 assert(pairs==set<string>({"01","02","10","13","20","23","31","32"}));
 for(const auto& ab:pairs){string t=step(ab);for(size_t j=0;j+1<t.size();j++)assert(pairs.count(t.substr(j,2)));}
 string coded=binary(fixed);for(unsigned int i=0;i<16384;i++)assert(coded.at(i)==parity11(i));
 // Pair factors are exhaustive: all occur in this fixed-point prefix and
 // their set is closed under substitution. Every length-2^k factor
 // crosses at most one 2^k-block boundary.
 for(int k=4;k<=13;k++){
  const int n=1<<k;array<string,4> block;
  for(int a=0;a<4;a++){string s(1,char('0'+a));for(int j=0;j<k;j++)s=step(s);block[a]=binary(s);assert((int)block[a].size()==n);}
  unordered_set<string> factors;factors.reserve(8*n+8);
  for(const string& ab:pairs){string t=block[ab[0]-'0']+block[ab[1]-'0'];
   for(int i=0;i<=n;i++)factors.insert(t.substr(i,n));}
  if(n<=64){string direct=binary(fixed);unordered_set<string> found;
   for(size_t i=0;i+n<=direct.size();i++)found.insert(direct.substr(i,n));
   assert(found==factors);}
  unordered_map<string,int> orbit;orbit.reserve(factors.size());
  for(const auto& f:factors){string c=rotation(f);
   if(n<=32)assert(c==slow_rotation(f));
   orbit[c]++;}
  map<int,int> distribution;for(const auto& kv:orbit)distribution[kv.second]++;
  assert((int)factors.size()==8*n-8);
  assert((int)orbit.size()==4*n-6);
  assert((int)distribution.size()==3);
  assert(distribution[1]==4*n-12 && distribution[2]==2 && distribution[n]==4);
  cout<<n<<","<<factors.size()<<","<<orbit.size()<<","<<distribution[1]<<","<<distribution[2]<<","<<distribution[n]<<"\n";
 }
 cout<<"VERIFY_OK\n";
}
