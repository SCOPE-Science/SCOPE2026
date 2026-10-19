// Independent shortest-path search *forward* from the proposed unique hardest pair.
// Checks selected cases against the 1000-row exhaustive census.
// Compile: c++ -O3 -std=c++17 crosscheck_forward.cpp -o crosscheck_forward
// Run: ./crosscheck_forward
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

pair<vector<int>,vector<int>> automaton(int k) {
 int N=3*k+6;
 vector<int> A(N),B(N);
 A[0]=0; B[0]=1;
 for(int s=1;s<N;s++) {
  if(s<=2*k+3) {
   A[s]=(s&1)?s+1:s-1;
   B[s]=(s&1)?s-1:s+1;
  } else if(s==2*k+4) {
   A[s]=s+1;B[s]=2;
  } else if(s==2*k+5) {
   A[s]=3;B[s]=s+1;
  } else if(s==N-1) {
   A[s]=(s%2==0?s:s-1);
   B[s]=(s%2==1?s:s-1);
  } else {
   A[s]=(s%2==0?s+1:s-1);
   B[s]=(s%2==1?s+1:s-1);
  }
 }
 for(int s=0;s<N;s++) if(A[s]<0||B[s]<0||A[s]>=N||B[s]>=N) throw runtime_error("bad map");
 return {A,B};
}

int forward_distance(int k){
 const int n=3*k+6;
 auto [A,B]=automaton(k);
 const int z=n*(n+1)/2;
 auto ix=[n](int p,int q){return p*n-p*(p-1)/2+q-p;};
 vector<int> dist(z,-1),qu(z);
 int p=(k+2)/2,q=p+1;
 int h=0,t=1;qu[0]=p*n+q;dist[ix(p,q)]=0;
 while(h<t){
  int cur=qu[h++]; int x=cur/n,y=cur%n;
  int d=dist[ix(x,y)];
  if(x==y) return d;
  auto step=[&](const vector<int>& E) {
   int u=E[x],v=E[y];
   if(u>v) swap(u,v);
   int a=ix(u,v);
   if(dist[a]==-1){dist[a]=d+1;qu[t++]=u*n+v;}
  };
  step(A);step(B);
 }
 return -1;
}

int main(){
 for(int k:{1,16,17,40,101,499,500,501,999,1000}){
  long long expected=k%2?(5LL*k*k+32*k+47)/4:(5LL*k*k+34*k+44)/4;
  int actual=forward_distance(k);
  if(actual!=expected){cerr<<"MISMATCH k="<<k<<" expected="<<expected<<" actual="<<actual<<'\n';return 2;}
  cout<<"FORWARD_OK k="<<k<<" n="<<(3*k+6)<<" shortest="<<actual<<'\n';
 }
 return 0;
}
