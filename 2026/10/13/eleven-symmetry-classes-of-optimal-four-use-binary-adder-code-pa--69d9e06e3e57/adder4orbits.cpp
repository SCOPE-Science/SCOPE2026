#include <bits/stdc++.h>
using namespace std;using Pair=pair<int,int>;
int transform(int A,const int mapv[16]){int B=0;for(int i=0;i<16;i++)if(A>>i&1)B|=1<<mapv[i];return B;}
int main(){vector<Pair> rooted;int a,b;ifstream f("adder4_root_pairs.txt");while(f>>a>>b)rooted.push_back({a,b});set<Pair> all;for(auto [A,B]:rooted)for(int s=0;s<16;s++){int a=0,b=0;for(int t=0;t<16;t++){if(A>>t&1)a|=1<<(t^s);if(B>>t&1)b|=1<<(t^s);}all.insert({a,b});}
 cerr<<"full pairs "<<all.size()<<"\n";
 map<Pair,int> orbit;array<int,4> perm={0,1,2,3};vector<array<int,16>> m;
 do{for(int s=0;s<16;s++){array<int,16> mapv;for(int v=0;v<16;v++){int w=0;for(int j=0;j<4;j++)if(v>>perm[j]&1)w|=1<<j;mapv[v]=w^s;}m.push_back(mapv);}}while(next_permutation(perm.begin(),perm.end()));
 for(auto [A,B]:all){Pair best={65536,65536};for(auto mp:m){int aa=transform(A,mp.data()),bb=transform(B,mp.data());best=min(best,Pair(aa,bb));best=min(best,Pair(bb,aa));}orbit[best]++;}
 map<int,int> hist;for(auto &[rep,c]:orbit)hist[c]++;
 cout<<"orbits "<<orbit.size()<<" histogram";for(auto [n,k]:hist)cout<<" "<<n<<":"<<k;cout<<"\n";
 for(auto [rep,c]:orbit)cout<<rep.first<<","<<rep.second<<","<<c<<","<<__builtin_popcount((unsigned)rep.first)<<","<<__builtin_popcount((unsigned)rep.second)<<"\n";
}
