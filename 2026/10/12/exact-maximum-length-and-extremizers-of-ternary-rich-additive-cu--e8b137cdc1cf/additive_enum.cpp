// Exact exhaustive enumeration of rich, additive-cube-free ternary words.
// Every labeled word is enumerated; alphabet weights are 0,1,2.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra additive_enum.cpp -o additive_enum
// Execute: ./additive_enum
#include <algorithm>
#include <cstdlib>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

constexpr int LIMIT=105;
struct PalNode {
  int len=0, link=0;
  array<int,3> next{{0,0,0}};
};
class Enumerator {
  PalNode p[108];
  int nodes=2, suffix=1;
  array<int,LIMIT+1> w{};
  array<int,LIMIT+2> pref{};
  array<uint64_t,LIMIT+1> level{};
  vector<string> extremizers;
  uint64_t calls=0;
  bool appended_cube(int n) const {
    for (int k=1;3*k<=n;++k) {
      int a=n-3*k,b=a+k,c=b+k,d=c+k;
      if(pref[b]-pref[a]==pref[c]-pref[b] && pref[c]-pref[b]==pref[d]-pref[c])return true;
    }
    return false;
  }
  void search(int n){
    ++calls; ++level[n];
    if(n==104){
      string s; s.reserve(180);
      for(int i=0;i<n;++i)s+=char('0'+w[i]);
      extremizers.push_back(s);
    }
    if(n==LIMIT)return;
    for(int ch=0;ch<3;++ch){
      w[n]=ch;
      pref[n+1]=pref[n]+ch;
      if(appended_cube(n+1))continue;
      int old=suffix,cur=suffix;
      while (n-1-p[cur].len<0 || w[n-1-p[cur].len]!=ch)
        cur=p[cur].link;
      if(p[cur].next[ch]!=0)continue;
      // The appended word has a previously unseen palindromic suffix.
      int fresh=nodes++;
      p[fresh]=PalNode();p[fresh].len=p[cur].len+2;
      if(p[fresh].len>1){
        int other=p[cur].link;
        while(n-1-p[other].len<0 || w[n-1-p[other].len]!=ch)
          other=p[other].link;
        p[fresh].link=p[other].next[ch];
        if(p[fresh].link==0){cerr<<"PAL_LINK_FAILURE\n";abort();}
      } else p[fresh].link=1;
      p[cur].next[ch]=fresh;suffix=fresh;
      search(n+1);
      suffix=old;p[cur].next[ch]=0;--nodes;
    }
  }
public:
  void run(){
    p[0].len=-1;p[0].link=0;
    p[1].len=0;p[1].link=0;
    search(0);
    if(level[105]!=0 || extremizers.size()!=8){cerr<<"ENUMERATION_MISMATCH\n";abort();}
    cout<<"VISITED "<<calls<<"\n";
    for(int i=0;i<=LIMIT;++i)cout<<"COUNT "<<i<<" "<<level[i]<<"\n";
    for(const auto &s:extremizers)cout<<"REP "<<s<<"\n";
    cout<<"VERIFY_ENUM_OK\n";
  }
};
int main(){Enumerator e;e.run();}
