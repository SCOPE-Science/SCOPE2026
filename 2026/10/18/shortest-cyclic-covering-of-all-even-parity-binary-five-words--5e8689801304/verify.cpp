#include <bits/stdc++.h>
using namespace std;
static string bits(uint64_t w,int n){string s;for(int i=n-1;i>=0;i--)s+=((w>>i)&1)?'1':'0';return s;}
static string minrot(const string &s){string z=s;for(int i=1;i<(int)s.size();i++){string t=s.substr(i)+s.substr(0,i);if(t<z)z=t;}return z;}
static bool covers(uint64_t w,int n,int k,int *oddOut=nullptr,int *repeatEvenOut=nullptr){
 if(n<k)return false;
 unsigned seen=0; int odd=0,ev=0;int mask=(1<<k)-1; int cur=(w>>(n-k))&mask;
 for(int i=0;i<n;i++){
  if((__builtin_popcount((unsigned)cur)&1)==0){seen|=1u<<(cur>>1);ev++;}else odd++;
  cur=((cur<<1)&mask) | ((w>>(n-1-((i+k)%n)))&1);
 }
 if(oddOut)*oddOut=odd;if(repeatEvenOut)*repeatEvenOut=ev-(1<<(k-1));
 return seen==((1u<<(1<<(k-1)))-1u);
}
int main(){
 for(int k=2;k<=5;k++){
  int opt=-1; uint64_t rooted=0; set<string>neck,brace;map<pair<int,int>,long long>dist;string witness;
  for(int n=k;n<=26;n++){
   long long cnt=0; uint64_t limit=1ull<<(n-k);
   for(uint64_t w=0;w<limit;w++){
    int odd=0,repeats=0;
    if(!covers(w,n,k,&odd,&repeats))continue;
    cnt++;if(opt<0){opt=n;}
    if(n==opt){
     string s=bits(w,n),r=s;reverse(r.begin(),r.end());
     neck.insert(minrot(s));brace.insert(min(minrot(s),minrot(r)));
     dist[{odd,repeats}]++;
     if(witness.empty())witness=s;
    }
   }
   if(cnt){rooted=cnt;break;}
  }
  cout << "k="<<k<<" opt="<<opt<<" rooted0000="<<rooted<<" necklaces="<<neck.size()<<" bracelets="<<brace.size()<<" witness="<<witness<<"\n";
  for(auto [pair,ct]:dist)cout << " odd="<<pair.first<<" dup_even="<<pair.second<<" anchored="<<ct<<"\n";
  if(k==5){cout<<"k5 canonical necklaces:\n"; for(auto &s:neck)cout<<s<<"\n";}
 }
}
