#include <bits/stdc++.h>
using namespace std;
int q=56;uint64_t leaves=0,nodes=0;
vector<int> a{0},units;
map<array<unsigned char,9>,unsigned long long> orbits;
array<unsigned char,9> canonical(const vector<int>& a){
 array<unsigned char,9> best;best.fill(100);
 for(int pivot:a)for(int u:units){
  array<unsigned char,9> v{};
  for(int i=0;i<9;++i)v[i]=(u*(a[i]-pivot)+56*56)%56;
  sort(v.begin(),v.end());if(v<best)best=v;
 }
 return best;
}
void dfs(int next,uint64_t used){
 ++nodes;int k=a.size();
 if(k==9){++leaves;++orbits[canonical(a)];return;}
 if(q-next<9-k)return;
 for(int x=next;x<=q-(9-k);++x){
  uint64_t add=0;bool ok=true;
  for(int b:a){uint64_t bit=1ULL<<((x+b)%q);if((used|add)&bit){ok=false;break;}add|=bit;}
  if(ok){a.push_back(x);dfs(x+1,used|add);a.pop_back();}
 }
}
int main(){for(int x=1;x<56;++x)if(gcd(x,56)==1)units.push_back(x);dfs(1,0);
 cout<<"nodes="<<nodes<<" normalized_sets="<<leaves<<" affine_orbits="<<orbits.size()<<'\n';
 for(auto& [rep,count]:orbits){cout<<"count="<<count<<" rep=";for(auto x:rep)cout<<int(x)<<',';cout<<'\n';}
}
