#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using ull = unsigned long long;

static ull fact(int n){ ull x=1;for(int i=2;i<=n;i++)x*=i;return x; }
static ull pow2(int k){return 1ULL<<k;}
static array<ull,3> formula(int n){
    int k=n/3, r=n%3;
    if(r==0){
        ull a=fact(n)/(pow2(k)*fact(k));
        ull b=(k>=2)?fact(n)*125/(120*pow2(k-2)*fact(k-2)):0;
        ull c=(k>=3)?fact(n)*256/(2*24*24*pow2(k-3)*fact(k-3)):0;
        return {a,b,c};
    }
    if(r==1) return {fact(n)/(pow2(k)*fact(k)),0,0};
    return {fact(n)*16/(24*pow2(k-1)*fact(k-1)),0,0};
}
struct DSU{
    vector<int> parent, sz;
    DSU(int n):parent(n),sz(n,1){iota(parent.begin(),parent.end(),0);}
    int root(int a){while(a!=parent[a])a=parent[a];return a;}
    void join(int a,int b){a=root(a);b=root(b);if(a!=b){parent[b]=a;sz[a]+=sz[b];}}
};
static int classify(int n,const vector<pair<int,int>>&e,const vector<int>&idx){
    vector<int>d(n);
    DSU ds(n);
    for(int j:idx){auto [a,b]=e[j];d[a]++;d[b]++;ds.join(a,b);}
    int isolated=count(d.begin(),d.end(),0);
    if(isolated>1)return -1;
    for(int j:idx){auto [a,b]=e[j];if(d[a]==1&&d[b]==1)return -1;}
    vector<int> comps(n), ed(n);
    for(int v=0;v<n;v++)if(d[v])comps[ds.root(v)]++;
    for(int j:idx){auto [a,b]=e[j];ed[ds.root(a)]++;}
    int t3=0,t4=0,t5=0;
    for(int j=0;j<n;j++)if(comps[j]){
        if(ed[j]!=comps[j]-1)return -2;
        if(comps[j]==3)t3++;
        else if(comps[j]==4)t4++;
        else if(comps[j]==5)t5++;
        else return -2;
    }
    int k=n/3,r=n%3;
    if(r==0){
        if(isolated==0&&t3==k&&t4==0&&t5==0)return 0;
        if(isolated==1&&t3==k-2&&t4==0&&t5==1)return 1;
        if(isolated==1&&t3==k-3&&t4==2&&t5==0)return 2;
    } else if(r==1){
        if(isolated==1&&t3==k&&t4==0&&t5==0)return 0;
    } else {
        if(isolated==1&&t3==k-1&&t4==1&&t5==0)return 0;
    }
    return -2;
}
int main(){
    for(int n=4;n<=10;n++){
        vector<pair<int,int>> es;
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)es.push_back({i,j});
        int m=es.size(),h=(2*(n-1)+2)/3;
        vector<int> choose(h);iota(choose.begin(),choose.end(),0);
        array<ull,3> cnt{};
        ull inspected=0;
        do {
            ++inspected;
            int c=classify(n,es,choose);
            if(c==-2){cerr<<"unexpected shape for n="<<n<<"\n";return 2;}
            if(c>=0)++cnt[c];
            int i=h-1;
            while(i>=0&&choose[i]==m-h+i)--i;
            if(i<0)break;
            ++choose[i];for(int j=i+1;j<h;j++)choose[j]=choose[j-1]+1;
        }while(true);
        auto want=formula(n);
        if(cnt!=want){cerr<<"count mismatch "<<n<<"\n";return 3;}
        cout<<"n="<<n<<" inspected="<<inspected<<" optimum="<<(cnt[0]+cnt[1]+cnt[2])
            <<" families="<<cnt[0]<<","<<cnt[1]<<","<<cnt[2]<<" OK\n";
    }
    cout<<"VERIFY_OK n=4..10 exhaustive, direct adjacency and exact component-classification checks\n";
}
