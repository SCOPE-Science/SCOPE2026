// Independent brute-force verification of rowmotion on the Fano incidence poset.
// Compile: c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
int main(){
  vector<array<int,3>> lines;
  for(int a=1;a<=7;a++) for(int b=a+1;b<=7;b++){
    array<int,3> t{a,b,a^b}; sort(t.begin(),t.end());
    if(find(lines.begin(),lines.end(),t)==lines.end())lines.push_back(t);
  }
  sort(lines.begin(),lines.end());
  assert(lines.size()==7);
  array<int,14> pred{};
  for(int j=0;j<7;j++) for(int p:lines[j])pred[7+j]|=1<<(p-1);
  vector<int> ideals;
  vector<bool> good(1<<14,false);
  for(int s=0;s<(1<<14);s++){
    bool valid=true;
    for(int j=7;j<14;j++) if((s>>j)&1)
      if((s&pred[j])!=pred[j])valid=false;
    if(valid){ideals.push_back(s);good[s]=true;}
  }
  assert(ideals.size()==458);
  vector<int> transition(1<<14,-1);
  for(int s:ideals){
    int ans=0;
    for(int i=0;i<14;i++){
      if((s>>i)&1)continue;
      if((s & pred[i])==pred[i])ans |= (1<<i) | pred[i];
    }
    assert(good[ans]);transition[s]=ans;
  }
  set<int> image;
  for(int s:ideals)image.insert(transition[s]);
  assert(image.size()==ideals.size());
  vector<bool> seen(1<<14,false);
  map<int,int> counts;
  int total=0;
  for(int s:ideals)if(!seen[s]){
    int x=s,length=0;
    do{assert(!seen[x]);seen[x]=true;x=transition[x];length++;}while(x!=s);
    counts[length]++;total+=length;
  }
  map<int,int> expected{{3,29},{5,35},{7,28}}; assert(total==458 && counts==expected);
  assert(3*29+5*35+7*28==458);
  for(int s:ideals){
    int x=s;
    for(int z=0;z<105;z++)x=transition[x];
    assert(x==s);
  }
  cout<<"VERIFY_INDEPENDENT_OK points=7 lines=7 ideals=458"<<'\n';
  cout<<"VERIFY_INDEPENDENT_OK cycle_lengths=3:29,5:35,7:28 order=105"<<'\n';
}
