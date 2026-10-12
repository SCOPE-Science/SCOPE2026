#include <bits/stdc++.h>
using namespace std;
using U=unsigned long long;
U adj[64]; vector<int> S; vector<vector<int>> sol; unsigned long long nodes=0;
int pairdist(int a,int b){int d=a^b;return __builtin_popcount((unsigned)(d|((d<<1)&63)|(d>>5)));}
void search(U p){++nodes;
 if(S.size()==16){sol.push_back(S);return;}
 if((int)S.size()+__builtin_popcountll(p)<16)return;
 while(p){if((int)S.size()+__builtin_popcountll(p)<16)return;
  int v=__builtin_ctzll(p);p&=p-1;
  S.push_back(v);search(p&adj[v]);S.pop_back();
 }
}
int main(){for(int a=0;a<64;a++)for(int b=a+1;b<64;b++)if(pairdist(a,b)>=4)adj[a]|=1ULL<<b;search(~0ULL);
 cout<<"# nodes "<<nodes<<" solutions "<<sol.size()<<"\n";
 for(auto const& c:sol){for(int i=0;i<16;i++){if(i)cout<<" ";cout<<c[i];}cout<<"\n";}
}
