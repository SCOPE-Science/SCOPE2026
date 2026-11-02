// Independent exhaustive extension-profile verifier for strict betweenness.
// Every type is interned by an exact pair (atomic diagram, sorted child type set).
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
static map<pair<uint64_t,vector<int>>,int> dictionary[5];
static uint64_t atom(const array<int,4>& x,int length){
  uint64_t a=0;
  for(int i=0;i<length;i++)for(int j=i+1;j<length;j++)
    a=(a<<1)|static_cast<uint64_t>(x[i]==x[j]);
  for(int i=0;i<length;i++)for(int j=0;j<length;j++)for(int k=0;k<length;k++)
    if(i!=j&&j!=k&&i!=k)
      a=(a<<1)|static_cast<uint64_t>((x[i]<x[j]&&x[j]<x[k])||(x[k]<x[j]&&x[j]<x[i]));
  return a;
}
static int intern(int lev,uint64_t atom_id,vector<int> ch){
  sort(ch.begin(),ch.end());ch.erase(unique(ch.begin(),ch.end()),ch.end());
  auto key=make_pair(atom_id,move(ch));
  auto &d=dictionary[lev];auto it=d.find(key);
  if(it!=d.end())return it->second;
  int id=d.size();d.emplace(move(key),id);return id;
}
static int evaluate(int n){
  vector<int> old(1);array<int,4> x{};
  for(int k=0;k<4;k++)old.resize(old.size()*n);
  for(int p=0;p<(int)old.size();p++){
    int rem=p;
    for(int i=3;i>=0;i--){x[i]=rem%n;rem/=n;}
    old[p]=intern(4,atom(x,4),{});
  }
  for(int level=3;level>=0;level--){
    int tuples=old.size()/n;
    vector<int> now(tuples);
    for(int p=0;p<tuples;p++){
      int rem=p;x.fill(0);
      for(int i=level-1;i>=0;i--){x[i]=rem%n;rem/=n;}
      vector<int> ch;ch.reserve(n);
      for(int v=0;v<n;v++)ch.push_back(old[p*n+v]);
      now[p]=intern(level,atom(x,level),move(ch));
    }
    if(level==1&&(n==14||n==15)){
       cout<<"onepoint_positions=";
       for(int j=0;j<n;j++)cout<<(j?",":"")<<now[j];
       cout<<"\n";
    }
    old.swap(now);
  }
  return old[0];
}
int main(){
  map<int,int> cls;
  for(int n=1;n<=17;n++){
    int id=evaluate(n);
    if(!cls.count(id))cls[id]=cls.size()+1;
    cout<<"order="<<n<<" class="<<cls[id]<<"\n";
  }
  cout<<"CLASS_COUNT="<<cls.size()<<"\n";
}
