// Standalone finite-field checks for maximal nilpotency index in products of triangular matrices.
// Build: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using ull=unsigned long long;
static ull power(ull a,int n){ull x=1;while(n--)x*=a;return x;}
static ull predicted(int n,int q){
    ull u=q-1;
    ull c=(n+1)*power(u,n)+n*power(u,n-1);
    return power(q,(n-1)*(n-1))*power(u,n-1)*c;
}
static ull nilpotent_pairs(int n,int q){return power(2*q-1,n)*power(q,n*(n-1));}
static void brute(int n,int q){
    int len=n*(n+1)/2, count=(int)power(q,len);
    std::vector<std::vector<int>> mats(count,std::vector<int>(n*n,0));
    std::vector<std::pair<int,int>> coords;
    for(int i=0;i<n;i++)for(int j=i;j<n;j++)coords.push_back({i,j});
    for(int m=0;m<count;m++){
       int x=m;
       for(int c=0;c<len;c++){
           int i=coords[c].first,j=coords[c].second;
           mats[m][i*n+j]=x%q; x/=q;
       }
    }
    ull nil=0,maxidx=0;
    for(const auto &a:mats)for(const auto &b:mats){
        bool zeroDiag=true;
        for(int i=0;i<n;i++)if(a[i*n+i]*b[i*n+i]%q){zeroDiag=false;break;}
        if(!zeroDiag)continue;
        nil++;
        std::vector<int> ab(n*n,0);
        for(int i=0;i<n;i++)for(int j=i;j<n;j++){
            int s=0;for(int k=i;k<=j;k++)s+=a[i*n+k]*b[k*n+j];
            ab[i*n+j]=s%q;
        }
        bool full=true;
        for(int i=0;i<n-1;i++)if(ab[i*n+i+1]==0)full=false;
        if(full)maxidx++;
    }
    assert(nil==nilpotent_pairs(n,q));
    assert(maxidx==predicted(n,q));
    std::cout << "ENUM_OK n="<<n<<" q="<<q<<" nil="<<nil<<" maxindex="<<maxidx<<"\n";
}
static void weighted_states(int n,int q){
    ull total=0,u=q-1;
    for(int code=0;code<(int)power(3,n);code++){
      int x=code,last=-1;ull w=1;bool good=true;
      for(int i=0;i<n;i++){
        int st=x%3;x/=3; // 0: first coordinate nonzero; 1: second nonzero; 2: both zero
        w*=(st==2 ? 1 : u);
        if(i>0 && last!=0 && st!=1)good=false;
        last=st;
      }
      if(good)total+=w;
    }
    ull ans=(n+1)*power(u,n)+n*power(u,n-1);
    assert(total==ans);
}
int main(){
 for(int q: {2,3,4,5,7})for(int n=2;n<=8;n++)weighted_states(n,q);
 for(int q: {2,3,5})brute(2,q);
 for(int q: {2,3})brute(3,q);
 brute(4,2);
 std::cout << "VERIFY_OK\n";
}
