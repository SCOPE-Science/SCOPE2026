#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int maxn=argc>1?atoi(argv[1]):6;
for(int n=1;n<=maxn;n++){
 vector<pair<int,int>> ij;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ij.push_back({i,j});
 int e=ij.size();uint64_t total=1ULL<<e;vector<array<int,8>> perms;
 array<int,8> p;for(int i=0;i<n;i++)p[i]=i;do{perms.push_back(p);}while(next_permutation(p.begin(),p.begin()+n));
 set<uint64_t> canon;
 for(uint64_t mask=0;mask<total;mask++){
   uint64_t adj[8]={};for(int k=0;k<e;k++)if(mask>>k&1)adj[ij[k].first]|=1ULL<<ij[k].second;
   uint64_t low=~0ULL;
   for(auto &pp:perms){uint64_t code=0;int idx=0;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){if(adj[pp[i]]>>pp[j]&1ULL)code|=1ULL<<idx;idx++;}if(code<low)low=code;}
   canon.insert(low);
 }
 cerr<<"n="<<n<<" topological="<<total<<" types="<<canon.size()<<"\n";
 for(uint64_t z:canon)cout<<n<<" "<<z<<"\n";
}
}
