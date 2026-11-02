#include <bits/stdc++.h>
using namespace std;
using U64=uint64_t;
struct I {int l,r;};
int code(int u,int v,int w,const vector<vector<unsigned char>>& adj){
 int m=0;
 if(u==v) m|=1;
 if(u==w) m|=2;
 if(v==w) m|=4;
 if(adj[u][v])m|=8;
 if(adj[u][w])m|=16;
 if(adj[v][w])m|=32;
 return m;
}
int main(int argc,char** argv){
 int N=argc>1?atoi(argv[1]):26;
 map<vector<U64>,int> oneIds;
 map<vector<int>,int> graphIds;
 for(int n=1;n<=N;n++){
  vector<I> xs;
  for(int i=1;i<=n;i++)for(int j=i;j<=n;j++)xs.push_back({i,j});
  int V=xs.size();
  vector<vector<unsigned char>> adj(V,vector<unsigned char>(V));
  for(int i=0;i<V;i++)for(int j=0;j<V;j++)adj[i][j]=(i!=j && xs[i].l<=xs[j].r && xs[j].l<=xs[i].r);
  vector<int> singIds;
  for(int u=0;u<V;u++){
    vector<U64> twoTypes;
    twoTypes.reserve(V);
    for(int v=0;v<V;v++){
      U64 mask=0;
      for(int w=0;w<V;w++)mask |= U64(1)<<code(u,v,w,adj);
      twoTypes.push_back(mask);
    }
    sort(twoTypes.begin(),twoTypes.end());
    twoTypes.erase(unique(twoTypes.begin(),twoTypes.end()),twoTypes.end());
    auto [it,newType]=oneIds.emplace(twoTypes,oneIds.size()+1);
    singIds.push_back(it->second);
  }
  sort(singIds.begin(),singIds.end());
  singIds.erase(unique(singIds.begin(),singIds.end()),singIds.end());
  auto [it,newType]=graphIds.emplace(singIds,graphIds.size()+1);
  cout << "n="<<n<<" V="<<V<<" rank3_type="<<it->second<<" distinct_single_types="<<singIds.size()<<" new="<<newType<<"\n";
  cout.flush();
 }
}
