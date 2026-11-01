#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <utility>
#include <cassert>
using U=uint32_t; using ULL=unsigned long long;
ULL choose(int n,int k){if(k<0||k>n)return 0;ULL r=1;for(int i=1;i<=k;i++)r=r*(n-i+1)/i;return r;}
ULL covered(int m){ long long s=0;for(int j=0;j<=m;j++){int e=(m-j)*(m-j-1)/2;long long t=(long long)choose(m,j)*(1LL<<e);s+=j%2?-t:t;}return (ULL)s; }
int main(){
  for(int n=4;n<=7;n++){
    std::vector<std::pair<int,int>> edges;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edges.push_back({a,b});
    int e=edges.size();U all=(1U<<e)-1;
    std::vector<U> clique(1<<n,0);
    for(int vmask=0;vmask<(1<<n);vmask++)for(int i=0;i<e;i++)if(((vmask>>edges[i].first)&1)&&((vmask>>edges[i].second)&1))clique[vmask]|=(1U<<i);
    auto supp=[&](U state){int v=0; for(int i=0;i<e;i++)if(state&(1U<<i))v|=1<<edges[i].first | 1<<edges[i].second;return v;};
    auto F=[&](U state){return clique[((1<<n)-1)^supp(state)];};
    std::map<std::pair<U,U>,ULL> cnt;
    ULL entry0=0,entry1=0;
    for(U x=0;x<(1U<<e);x++){
      U y=F(x),z=F(y); assert(F(z)==y&&y!=z);
      if(x==y||x==z)entry0++;else entry1++;
      cnt[{y<z?y:z,y<z?z:y}]++;
    }
    ULL special=1+covered(n)+n*covered(n-1);
    assert(cnt.size()==((1U<<(n-1))-n));
    assert((cnt[{0,all}]==special));
    for(auto const &p:cnt){
      if(p.first.first==0&&p.first.second==all)continue;
      int m=__builtin_popcount((unsigned)supp(p.first.first));
      assert(m>=2&&m<=n-2&&p.second==covered(m)+covered(n-m));
    }
    printf("n=%d states=%u orbits=%zu special_basin=%llu first_periodic=%llu first_step=%llu\n",n,(1U<<e),cnt.size(),special,entry0,entry1);
  }
  puts("VERIFY_CPP_OK");
}
