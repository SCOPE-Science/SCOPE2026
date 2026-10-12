#include <bits/stdc++.h>
using namespace std;
using ull=uint64_t;using u128=unsigned __int128;
constexpr int N=6;constexpr int V=1<<N,T=1<<(N+1);
u128 cover[V],ALL;ull options[T];
long long nodes=0;vector<int> path,witness;
bool dfs(u128 rem,int budget,ull chosen){
  nodes++;if(!rem){witness=path;return true;}
  if(budget<=0)return false;
  // bound on maximal residual coverage count by a center
  int mx=0;int scores[V]{};
  for(int c=0;c<V;c++)if(!(chosen>>c&1)){
    int cc=__builtin_popcountll((ull)(cover[c]&rem))+__builtin_popcountll((ull)((cover[c]&rem)>>64));
    scores[c]=cc;mx=max(mx,cc);
  }
  int r=__builtin_popcountll((ull)rem)+__builtin_popcountll((ull)(rem>>64));
  if(r>mx*budget) return false;
  // top-budget cover cap
  int maxcov=0;int ccs[V],count=0;
  for(int c=0;c<V;c++)if(!(chosen>>c&1)&&scores[c])ccs[count++]=scores[c];
  sort(ccs,ccs+count,greater<int>());for(int i=0;i<budget&&i<count;i++)maxcov+=ccs[i];
  if(maxcov<r)return false;
  int ti=-1,low=100,maxgain=0;
  for(int t=0;t<T;t++)if(rem>>t&1){
    ull allowed=options[t]&~chosen;
    int cnt=__builtin_popcountll(allowed);
    if(cnt<low){ti=t;low=cnt;maxgain=0;for(ull m=allowed;m;m&=m-1){int c=__builtin_ctzll(m);maxgain=max(maxgain,scores[c]);}if(cnt<=1)break;}
    else if(cnt==low){int gain=0;for(ull m=allowed;m;m&=m-1){int c=__builtin_ctzll(m);gain=max(gain,scores[c]);}if(gain>maxgain){ti=t;maxgain=gain;}}
  }
  if(ti<0||low==0)return false;
  vector<pair<int,int>> cand;
  for(ull m=options[ti]&~chosen;m;m&=m-1){int c=__builtin_ctzll(m);cand.push_back({scores[c],c});}
  sort(cand.begin(),cand.end(),greater<pair<int,int>>());
  for(auto [score,c]:cand){path.push_back(c);if(dfs(rem&~cover[c],budget-1,chosen|(1ULL<<c)))return true;path.pop_back();}
  return false;
}
int main(){ALL=((u128)-1);for(int c=0;c<V;c++)for(int pos=0;pos<=N;pos++)for(int bit=0;bit<2;bit++){
  int t=0;for(int j=0;j<=N;j++){int b=j==pos?bit:(c>>(N-(j<pos?j:j-1)-1)&1);t=(t<<1)|b;} cover[c]|=((u128)1<<t);options[t]|=(1ULL<<c);
 }
  for(int k:{19,20}){
    nodes=0;bool ok=dfs(ALL,k,0);cerr<<"k="<<k<<" feasible="<<ok<<" nodes="<<nodes<<"\n";if(k==19 && ok)return 1;if(k==20){if(!ok || witness.size()!=20)return 2;u128 unioncov=0;for(int c:witness)unioncov|=cover[c];if(unioncov!=ALL)return 3;sort(witness.begin(),witness.end());cout<<"WITNESS";for(int c:witness)cout<<" "<<c;cout<<"\nVERIFY_OK\n";}
  }
}
