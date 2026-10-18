// Exhaustive ordered-pair check with independent C++ implementation.
#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Perm=vector<int>;

bool commuting(const Perm& f,const Perm& g){
  for(int x=0;x<(int)f.size();++x) if(f[g[x]]!=g[f[x]]) return false;
  return true;
}
string fingerprint(const Perm& f,const Perm& g,bool stable){
  int n=f.size();int masks[6][6]{};
  for(int x=0;x<n;x++) for(int y=0;y<n;y++)
    masks[x][y]=16*(x==y)+(f[x]==y)+2*(g[x]==y)+4*(f[y]==x)+8*(g[y]==x);
  vector<int> color(n,0);
  if(stable){
    for(int run=0;run<n+2;run++){
      map<vector<int>,int> keys;
      vector<vector<int>> sig(n);
      for(int x=0;x<n;x++){
        vector<int> s(1+32*n,0);s[0]=color[x];
        for(int y=0;y<n;y++) s[1+32*color[y]+masks[x][y]]++;
        sig[x]=s;keys.emplace(s,0);
      }
      int rank=0;for(auto &kv:keys)kv.second=rank++;
      vector<int> after(n);
      for(int x=0;x<n;x++)after[x]=keys[sig[x]];
      if(after==color)break;
      color=after;
    }
  }
  map<vector<int>,int> quotient;
  for(int x=0;x<n;x++){
    vector<int> s(1+32*n,0);s[0]=color[x];
    for(int y=0;y<n;y++)s[1+32*color[y]+masks[x][y]]++;
    quotient[s]++;
  }
  string result;
  for(const auto &kv:quotient){
    result+=to_string(kv.second)+":";
    for(int j=0;j<(int)kv.first.size();j++)
      if(kv.first[j])result+=to_string(j)+"="+to_string(kv.first[j])+",";
    result+=';';
  }
  return result;
}
int main(){
  for(int n=1;n<=6;n++){
    Perm p(n);for(int i=0;i<n;i++)p[i]=i;
    vector<Perm> perms;do{perms.push_back(p);}while(next_permutation(p.begin(),p.end()));
    map<string,int> one,finals;
    long total=0;
    for(const auto& f:perms)for(const auto& g:perms){
      int mask=commuting(f,g)?1:2;
      one[fingerprint(f,g,false)]|=mask;
      finals[fingerprint(f,g,true)]|=mask;
      total++;
    }
    int oneMixed=0,stableMixed=0;
    for(auto &kv:one)if(kv.second==3)oneMixed++;
    for(auto &kv:finals)if(kv.second==3)stableMixed++;
    cout<<"n="<<n<<" pairs="<<total<<" first_profiles="<<one.size()<<" mixed_first="<<oneMixed
        <<" stable_profiles="<<finals.size()<<" mixed_C2="<<stableMixed<<"\n";
    if(n<=5&&oneMixed) return 2;
    if(n==6&&(oneMixed!=7||stableMixed!=3))return 3;
  }
  cout<<"FULL_PAIRS_PASS\n";
}
