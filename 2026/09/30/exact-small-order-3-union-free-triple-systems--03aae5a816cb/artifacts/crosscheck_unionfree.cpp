#include <bits/stdc++.h>
using namespace std;
static vector<unsigned> E; static int n,target; static long long hits,nodes; static vector<unsigned> fam; static unordered_set<unsigned> seen;
bool extend_ok(unsigned e, vector<unsigned>& nw){
  nw.push_back(e);
  for(unsigned a:fam) nw.push_back(e|a);
  for(size_t i=0;i<fam.size();++i) for(size_t j=i+1;j<fam.size();++j) nw.push_back(e|fam[i]|fam[j]);
  sort(nw.begin(),nw.end());
  if(adjacent_find(nw.begin(),nw.end())!=nw.end()) return false;
  for(unsigned u:nw) if(seen.count(u)) return false;
  return true;
}
void dfs(int start,bool all){
  ++nodes;
  if((int)fam.size()==target){++hits; return;}
  int need=target-(int)fam.size();
  for(int j=start;j<=(int)E.size()-need;++j){
    vector<unsigned> nw; if(!extend_ok(E[j],nw)) continue;
    fam.push_back(E[j]); for(unsigned u:nw) seen.insert(u);
    dfs(j+1,all);
    fam.pop_back(); for(unsigned u:nw) seen.erase(u);
    if(!all && hits) return;
  }
}
long long run(int N,int T,bool all,long long &NODES){
  n=N;target=T;E.clear();fam.clear();seen.clear();hits=nodes=0;
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)E.push_back((1u<<a)|(1u<<b)|(1u<<c));
  unsigned first=7; auto it=find(E.begin(),E.end(),first); int fi=it-E.begin(); fam={first};seen.insert(first); dfs(fi+1,all); NODES=nodes; return hits;
}
int main(){
  for(int N=4;N<=9;++N){ long long a,b; auto h1=run(N,N-1,false,a); auto h2=run(N,N-2,true,b); if(h1!=0||h2!=3) return 2; cout<<N<<" "<<N-2<<" "<<h1<<" "<<h2<<" "<<a<<" "<<b<<"\n"; }
  cout<<"CROSSCHECK_OK\n";
}
