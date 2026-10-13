// Exact independent enumeration of binary five-bit bounded-delay capacity codes.
// Compile: c++ -O2 -std=c++17 delay_verify.cpp -o delay_verify
// Run: ./delay_verify [catalogue.csv]
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
constexpr int N=5;
string bits(int x){ string s(5,'0');for(int i=4;i>=0;--i){s[i]=char('0'+(x&1));x>>=1;}return s; }
int rot(int x,int r){return ((x<<r)&31)|(x>>(5-r));}
int phase_word(int u,int v,int r){return ((u<<r)&31)|(v>>(5-r));}
int depth_direct(const array<int,6>& c){
 bool isword[32]={}; for(int x:c)isword[x]=true;
 int longest=0;
 for(int r=1;r<5;r++){
  bool adj[6][6]={};
  for(int i=0;i<6;i++)for(int j=0;j<6;j++)
   adj[i][j]=isword[phase_word(c[i],c[j],r)];
  bool active[6]; for(int i=0;i<6;i++)active[i]=true;
  for(int k=1;k<=6;k++){
   bool next[6]={};
   for(int j=0;j<6;j++)for(int i=0;i<6;i++)if(active[i] && adj[i][j]) next[j]=true;
   bool any=false;for(int j=0;j<6;j++){active[j]=next[j];any|=next[j];}
   if(!any)break;
   if(k==6)return 0;  // a cycle is necessary and sufficient here
   longest=max(longest,k);
  }
 }
 return longest+1;
}
int main(int argc,char**argv){
 vector<vector<int>> orbit; bool seen[32]={};
 for(int x=0;x<32;x++)if(!seen[x]){
  set<int> s;for(int r=0;r<5;r++)s.insert(rot(x,r));
  for(int w:s)seen[w]=true;
  if(s.size()==5)orbit.emplace_back(s.begin(),s.end());
 }
 if(orbit.size()!=6){cerr<<"not six necklaces\n";return 2;}
 uint64_t count[5]={},unsync=0;
 vector<pair<string,int>> catalog;
 for(int assignment=0;assignment<15625;assignment++){
  int q=assignment;array<int,6> c;
  for(int j=0;j<6;j++){c[j]=orbit[j][q%5];q/=5;}
  int delay=depth_direct(c);
  if(delay==0){unsync++;continue;}
  if(delay>4){cerr<<"Unexpected delay "<<delay<<"\n";return 3;}
  count[delay]++;
  vector<int> sortcode(c.begin(),c.end());sort(sortcode.begin(),sortcode.end());
  string row;
  for(int j=0;j<6;j++){if(j)row+=',';row+=bits(sortcode[j]);}
  catalog.push_back({row,delay});
 }
 sort(catalog.begin(),catalog.end());
 if(argc>1){ofstream out(argv[1]);out<<"codewords,delay\n";
  for(auto& e:catalog)out<<'"'<<e.first<<"\","<<e.second<<"\n";}
 cout<<"primitive_orbits="<<orbit.size()<<" assignments=15625 invalid="<<unsync
 <<" delay1="<<count[1]<<" delay2="<<count[2]<<" delay3="<<count[3]
 <<" delay4="<<count[4]<<" accepted="<<catalog.size()<<"\n";
 if(unsync!=6421||count[1]!=86||count[2]!=5546||count[3]!=3116||count[4]!=456||catalog.size()!=9204){cerr<<"MISMATCH\n";return 1;}
}
