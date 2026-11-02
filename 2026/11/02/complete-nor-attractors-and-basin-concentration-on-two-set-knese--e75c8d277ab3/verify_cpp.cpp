// Independent integer bit-mask enumerator for NOR dynamics on KG(n,2).
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
using U=uint64_t;
U C(int n,int r){if(r<0||r>n)return 0;U v=1;for(int i=1;i<=r;i++)v=v*(n-i+1)/i;return v;}
int main(){
 for(int n=5;n<=7;n++){
  vector<pair<int,int>> E;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)E.push_back({a,b});
  int m=(int)E.size();U full=(U(1)<<m)-1;
  vector<U> neigh(m,0);for(int i=0;i<m;i++)for(int j=0;j<m;j++){
   auto [a,b]=E[i];auto[c,d]=E[j];
   if(a!=c&&a!=d&&b!=c&&b!=d)neigh[i]|=(U(1)<<j);
  }
  auto step=[&](U s){U t=0;for(int i=0;i<m;i++)if(!(s&neigh[i]))t|=(U(1)<<i);return t;};
  map<pair<U,U>,U> basin;
  for(U s=0;s<=full;s++){
   U a=step(s),b=step(a);assert(step(b)==a);
   if(a>b)swap(a,b);
   basin[{a,b}]++;
  }
  U g=(U(1)<<(n-1))-n-C(n-1,2);
  U h=g+1+C(n-3,2);
  U e=1+2*((U(1)<<(n-2))-n+1)*((U(1)<<(n-2))-n+1)-C(n-2,2);
  U B=(U(1)<<m) - (n*g+C(n,3)+C(n,2)*e+3*C(n,3)*h+18*C(n,4));
  map<U,U> predicted={{1,C(n,3)},{2,9*C(n,4)},{g,(U)n},{h,3*C(n,3)},{e,C(n,2)},{B,1}};
  map<U,U> actual;
  U fixes=0,two=0;
  for(auto [key,size]:basin){actual[size]++;if(key.first==key.second)fixes++;else two++;}
  assert(actual==predicted);
  assert(fixes==(U)n+C(n,3));
  assert(two==1+C(n,2)+3*C(n,3)+9*C(n,4));
  assert(basin[make_pair(U(0),full)]==B);
  cout<<"n="<<n<<" states="<<(U(1)<<m)<<" attractors="<<basin.size()<<" fixed="<<fixes<<" two_cycles="<<two<<" dominant="<<B<<" histogram=";
  for(auto [k,v]:actual)cout<<k<<":"<<v<<",";cout<<"\n";
 }
 cout<<"CPP_VERIFY_OK\n";
}
