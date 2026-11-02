#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){ for(int n : {8,9,10,11}) {
  int N=1;for(int i=2;i<=n;i++)N*=i;
  vector<int>d;for(int i=1;i*(long long)i<=N;i++)if(N%i==0){d.push_back(i);if(i!=N/i)d.push_back(N/i);}
  sort(d.begin(),d.end());
  int K=8, W=N/64+1; vector<vector<uint64_t>>v(K+1,vector<uint64_t>(W));v[0][0]=1;
  for(int z:d){int ww=z/64, bb=z%64;
    for(int k=K;k>=1;k--)for(int i=W-1;i>=ww;i--){uint64_t nw=v[k-1][i-ww]<<bb;
        if(bb && i-ww-1>=0) nw|=v[k-1][i-ww-1]>>(64-bb);
        v[k][i]|=nw;
    }
  }
  int h=-1;vector<uint64_t>un(W);
  for(int k=0;k<=K;k++){
   for(int i=0;i<W;i++)un[i]|=v[k][i];
   long long cnt=0;int first=0;
   for(int x=1;x<=N;x++)if(!((un[x/64]>>(x%64))&1)) {cnt++;if(first==0)first=x;}
   if(cnt==0){h=k;cout<<"n="<<n<<" h="<<h<<" div="<<d.size()<<"\n";break;}
   if(k==K-1)cerr<<"n="<<n<<" k="<<k<<" misses="<<cnt<<" first="<<first<<"\n";
  }
  if(h<0) return 2;
 }
}
