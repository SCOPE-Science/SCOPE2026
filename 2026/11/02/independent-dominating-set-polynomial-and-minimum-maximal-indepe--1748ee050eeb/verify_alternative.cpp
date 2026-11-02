// Independent enumeration of all inclusion-maximal independent sets.
#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
struct Solver {
 int m,n,N;vector<pair<int,int>> state;vector<ull> compatibility;map<int,long long> histogram;
 Solver(int m_,int n_):m(m_),n(n_){
  for(int a=0;a<m+n;a++)for(int b=a+1;b<m+n;b++)state.push_back({a,b});
  N=state.size();if(N>62)throw runtime_error("too many token states");
  compatibility.assign(N,0);
  for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
    auto [a,b]=state[i];auto [c,d]=state[j];
    int k=(a==c)+(a==d)+(b==c)+(b==d);
    bool touching=false;
    if(k==1){
       int u=-1,v=-1;
       for(int x:{a,b})if(x!=c&&x!=d)u=x;
       for(int x:{c,d})if(x!=a&&x!=b)v=x;
       touching=((u<m)!=(v<m));
    }
    if(!touching){compatibility[i]|=1ULL<<j;compatibility[j]|=1ULL<<i;}
  }
 }
 void bk(ull R,ull P,ull X){
  if(!(P|X)){histogram[__builtin_popcountll(R)]++;return;}
  ull possible=P|X;int pivot=-1,best=-1;
  while(possible){int v=__builtin_ctzll(possible);possible&=possible-1;int deg=__builtin_popcountll(P&compatibility[v]);if(deg>best){best=deg;pivot=v;}}
  ull candidates=P&~compatibility[pivot];
  while(candidates){int v=__builtin_ctzll(candidates);ull bit=1ULL<<v;candidates&=~bit;
    bk(R|bit,P&compatibility[v],X&compatibility[v]);P&=~bit;X|=bit;
  }
 }
 map<int,long long> run(){bk(0,(1ULL<<N)-1,0);return histogram;}
};
long long choose(int n,int k){if(k>n||k<0)return 0;long long out=1;for(int i=1;i<=k;i++)out=out*(n-i+1)/i;return out;}
map<int,long long> formula(int m,int n){map<int,long long>h;h[choose(m,2)+choose(n,2)]++;
 for(int s=0;s<m;s++){if(s==1)continue;for(int t=0;t<n;t++){if(t==1)continue;
 h[choose(s,2)+choose(t,2)+(m-s)*(n-t)] += choose(m,s)*choose(n,t);
 }}return h;
}
int main(){for(auto [m,n]:vector<pair<int,int>>{{2,2},{2,3},{2,5},{3,3},{3,4},{3,5},{3,6},{4,4},{4,5},{5,5}}){
 Solver s(m,n);auto h=s.run();if(h!=formula(m,n)){cerr<<"MISMATCH "<<m<<","<<n<<"\n";return 2;}
 long long count=0;for(auto [size,num]:h)count+=num;
 cout<<"ALTERNATIVE_OK m="<<m<<" n="<<n<<" maximal="<<count<<" min="<<h.begin()->first<<" max="<<h.rbegin()->first<<"\n";
 }cout<<"ALTERNATIVE_COMPLETE_OK\n";
}
