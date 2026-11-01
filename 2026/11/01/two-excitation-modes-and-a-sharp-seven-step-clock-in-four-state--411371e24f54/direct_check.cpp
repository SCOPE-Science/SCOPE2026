// Direct verification of the four-color threshold-two complete-bipartite automaton.
// No experimental conclusion is used in place of the finite-quotient proof.
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using u64=unsigned long long;
static u64 update(u64 x,int a,int b){
    const int n=a+b;
    int ca=0,cb=0;
    for(int i=0;i<a;i++)ca+=(((x>>(2*i))&3ULL)==1ULL);
    for(int i=a;i<n;i++)cb+=(((x>>(2*i))&3ULL)==1ULL);
    u64 y=0;
    for(int i=0;i<n;i++){
        int c=(x>>(2*i))&3ULL;
        int next= c ? ((c+1)&3) : ((i<a ? cb:ca)>=2 ? 1:0);
        y|=u64(next)<<(2*i);
    }
    return y;
}
static u64 S(int n){ if(n<4)return 0;return (1ULL<<n)-2ULL*n-2ULL; }
static u64 T(int n){
    if(n<8)return 0;
    u64 f[21]={};f[0]=1; for(int i=1;i<=n;i++) f[i]=i*f[i-1];
    u64 ans=0;
    for(int a=2;a<=n-6;a++)for(int b=2;b<=n-a-4;b++)for(int c=2;c<=n-a-b-2;c++){
        int d=n-a-b-c;
        ans+=f[n]/(f[a]*f[b]*f[c]*f[d]);
    }
    return ans;
}
static void test(int a,int b){
    const int n=a+b; const u64 total=1ULL<<(2*n);
    u64 periodic=0,first[8]={};u64 fixed=0;
    for(u64 x=0;x<total;x++){
        u64 v[12]={x};
        for(int j=1;j<=11;j++)v[j]=update(v[j-1],a,b);
        assert(v[7]==v[11]);
        int t=0;while(t<8&&v[t]!=v[t+4])t++;
        assert(t<=7);first[t]++;
        if(t==0){periodic++;if(v[0]==v[1])fixed++;}
    }
    u64 S1=S(a),S2=S(b),T1=T(a),T2=T(b);
    u64 expected=1+2*S1*S2+T1*T2;
    assert(periodic==expected&&fixed==1);
    std::cout<<"K_"<<a<<","<<b<<" states="<<total<<" periodic="<<periodic<<" Q4="<<(periodic-1)/4<<" max_entry=";
    int mx=7;while(!first[mx])mx--;
    std::cout<<mx<<" histogram=";
    for(int j=0;j<=7;j++)std::cout<<(j?",":"")<<first[j];
    std::cout<<" PASS\n";
}
int main(){
    for(auto p:std::vector<std::pair<int,int>>{{2,2},{2,6},{3,3},{3,5},{4,4},{4,5},{4,6},{5,5},{3,7},{2,8}})test(p.first,p.second);
}
