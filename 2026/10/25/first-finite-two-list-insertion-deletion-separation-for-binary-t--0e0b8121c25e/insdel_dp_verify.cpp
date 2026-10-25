#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <functional>
#include <algorithm>
using namespace std;

// Three-word shortest common supersequence and longest common subsequence.
// Input bit order is most-significant-bit first.
struct TripleDP {
  int n, w[3], scmemo[216], lcmemo[216];
  TripleDP(int nn,int a,int b,int c):n(nn),w{a,b,c}{
    fill(scmemo,scmemo+216,-1);fill(lcmemo,lcmemo+216,-1);
  }
  int bit(int z,int p) const {return (w[z]>>(n-1-p))&1;}
  int index(int i,int j,int k) const{return (i*(n+1)+j)*(n+1)+k;}
  int scs(int i,int j,int k){
    int &v=scmemo[index(i,j,k)];if(v>=0)return v;
    if(i==n&&j==n&&k==n)return v=0;
    v=999;
    for(int b=0;b<2;b++){
      int x=i+(i<n&&bit(0,i)==b);
      int y=j+(j<n&&bit(1,j)==b);
      int z=k+(k<n&&bit(2,k)==b);
      if(x!=i||y!=j||z!=k)v=min(v,1+scs(x,y,z));
    }
    return v;
  }
  int lcs(int i,int j,int k){
    int &v=lcmemo[index(i,j,k)];if(v>=0)return v;
    if(i==n||j==n||k==n)return v=0;
    if(bit(0,i)==bit(1,j)&&bit(1,j)==bit(2,k))return v=1+lcs(i+1,j+1,k+1);
    return v=max({lcs(i+1,j,k),lcs(i,j+1,k),lcs(i,j,k+1)});
  }
};
struct Model {
  int n,N; bool insertion;
  vector<array<int,3>> forbidden;
  Model(int nn,bool ins):n(nn),N(1<<nn),insertion(ins){
    for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){
      TripleDP d(n,a,b,c);
      bool bad=ins?(d.scs(0,0,0)<=n+2):(d.lcs(0,0,0)>=n-2);
      if(bad)forbidden.push_back({a,b,c});
    }
  }
  bool valid(uint64_t mask)const{
    for(const auto &t:forbidden)if((mask>>t[0]&1)&&(mask>>t[1]&1)&&(mask>>t[2]&1))return false;
    return true;
  }
  unsigned long long count(int k)const{
    unsigned long long num=0;uint64_t mask=(uint64_t(1)<<k)-1,limit=uint64_t(1)<<N;
    while(mask<limit){
      if(valid(mask))++num;
      uint64_t t=mask&-mask,u=mask+t;
      if(!u||u>=limit)break;
      mask=u|(((mask^u)>>2)/t);
    }
    return num;
  }
};
int main(){
 for(int n=2;n<=5;n++)for(bool ins:{false,true}){
   Model m(n,ins);
   cout<<n<<' '<<(ins?"insertion":"deletion")<<" forbidden_triples="<<m.forbidden.size();
   int k=n==2?2:n==3?3:n==4?4:(ins?6:4);
   cout<<" maximum_size="<<k<<" maxima="<<m.count(k)<<" next_level="<<m.count(k+1)<<'\n';
 }
}
