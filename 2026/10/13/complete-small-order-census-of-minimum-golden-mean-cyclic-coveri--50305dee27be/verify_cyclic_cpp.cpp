#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int n,N,allowed;U target;U validCount=0;unordered_map<U,int> orbit;
int F(int n){int a=0,b=1;while(n--){int c=a+b;a=b;b=c;}return a;}
U canonical(U x){
 U best=~U(0); auto rot=[&](U u){return (u>>1)|((u&1)<<(N-1));};
 U rev=0;for(int i=0;i<N;i++)if((x>>i)&1)rev|=U(1)<<(N-1-i);
 for(U u:{x,rev})for(int k=0;k<N;k++){best=min(best,u);u=rot(u);}
 return best;
}
void dfs(int i,U v){
 if(i==N){
  if((v&1)&&((v>>(N-1))&1))return;
  U seen=0;
  for(int j=0;j<N;j++){
    int x=0;
    for(int k=0;k<n;k++)x=(x<<1)|int((v>>((j+k)%N))&1);
    seen|=U(1)<<x;
  }
  if(seen!=target)return;
  validCount++;
  orbit[canonical(v)]++;
  return;
 }
 dfs(i+1,v);
 if(i==0||!((v>>(i-1))&1))dfs(i+1,v|(U(1)<<i));
}
int main(){for(n=2;n<=6;n++){
 N=F(n+2)+F(n)-1;
 allowed=0;target=0;for(int x=0;x<(1<<n);x++)if(!(x&(x<<1))){allowed++;target|=U(1)<<x;}
 validCount=0;orbit.clear();dfs(0,0);
 map<int,int> hist;for(auto&z:orbit)hist[z.second]++;
 const U expected_labelled[]={0,0,3,6,20,102,2352};
 const int expected_orbits[]={0,0,1,1,1,3,42};
 if(validCount!=expected_labelled[n] || int(orbit.size())!=expected_orbits[n])abort();
 if(n==6 && !(hist.size()==1 && hist[56]==42))abort();
 cerr<<"n "<<n<<" N "<<N<<" allowed "<<allowed<<" labelled "<<validCount<<" dihedral_orbits "<<orbit.size()<<" sizes";for(auto [s,k]:hist)cerr<<" "<<s<<":"<<k;cerr<<"\n";if(n==6){vector<U> keys;for(auto&kv:orbit)keys.push_back(kv.first);sort(keys.begin(),keys.end());for(U u:keys){string x;for(int j=0;j<N;j++)x+=char('0'+((u>>j)&1));cout<<x<<"\n";}}
 }}
