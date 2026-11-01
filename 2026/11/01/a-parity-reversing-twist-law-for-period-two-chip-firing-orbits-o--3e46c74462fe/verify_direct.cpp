// Independent direct vertex-cut enumeration and two-update dynamics checks.
#include <iostream>
#include <vector>
#include <cassert>
#include <cstdint>
using namespace std;
using ll = long long;

vector<vector<int>> graph(int n, bool twist) {
    vector<vector<int>> g(2*n);
    auto add=[&](int x,int y){assert(x!=y);g[x].push_back(y);g[y].push_back(x);};
    for(int k=0;k<n;k++)add(2*k,2*k+1);
    for(int k=0;k<n-1;k++)for(int row=0;row<2;row++)add(2*k+row,2*(k+1)+row);
    for(int row=0;row<2;row++)add(2*(n-1)+row,2*0+(twist?(1-row):row));
    for(auto v:g)assert(v.size()==3);
    return g;
}
vector<int> update(const vector<vector<int>>&g,const vector<int>&x) {
    int N=g.size();vector<int> next=x;vector<int> fires(N,0);
    for(int i=0;i<N;i++)fires[i]=(x[i]>=int(g[i].size()));
    for(int i=0;i<N;i++){
        if(fires[i])next[i]-=g[i].size();
        for(int j:g[i])next[i]+=fires[j];
        assert(next[i]>=0);
    }
    return next;
}
ll count_direct(int n,bool twist,bool test_states) {
    auto g=graph(n,twist);int nv=2*n;ll sum=0;ll tested=0;
    for(int mask=0;mask<(1<<nv);mask++) {
        vector<vector<int>> choices(nv);
        ll weight=1;
        for(int v=0;v<nv;v++){
            int cv=0;
            for(int w:g[v])cv+=((mask>>v)&1)!=((mask>>w)&1);
            weight*=cv;
            if(test_states){
                int lo=((mask>>v)&1)?3:3-cv;
                for(int q=lo;q<lo+cv;q++)choices[v].push_back(q);
            }
        }
        sum+=weight;
        if(test_states&&weight){
            vector<int> x(nv);int testedmask=0;
            auto go=[&](auto&&self,int at)->void{
                if(at==nv){
                    auto y=update(g,x);auto z=update(g,y);
                    assert(x==z&&x!=y);
                    for(int v=0;v<nv;v++)assert((x[v]>=3)==bool((mask>>v)&1));
                    tested++;testedmask++;return;
                }
                for(int k:choices[at]){x[at]=k;self(self,at+1);}
            };
            go(go,0);
            assert(testedmask==weight);
        }
    }
    assert((sum%2)==0);
    if(test_states)assert(tested==sum);
    return sum/2;
}
int main(){
    for(int n=3;n<=10;n++){
        ll a=count_direct(n,false,n<=4);
        ll b=count_direct(n,true,n<=4);
        cout<<"n="<<n<<" prism_orbits="<<a<<" mobius_orbits="<<b<<" difference="<<(a-b)<<"\n";
    }
    cout<<"ALL_DIRECT_TESTS_PASS\n";
}
