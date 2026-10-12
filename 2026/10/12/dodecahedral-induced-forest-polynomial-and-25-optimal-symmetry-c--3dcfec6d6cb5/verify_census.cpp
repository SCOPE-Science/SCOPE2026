// Exhaustive induced-forest census for the dodecahedral graph GP(10,2).
// Compile: c++ -O2 -std=c++17 verify_census.cpp -o verify_census
// Run: ./verify_census
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct DSU {
    int p[20];
    DSU() {for (int i=0;i<20;++i)p[i]=i;}
    int root(int x) {while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
    bool join(int x,int y){x=root(x);y=root(y);if(x==y)return false;p[x]=y;return true;}
};
int main(){
    const int N=20,ALL=1<<N;
    vector<pair<int,int>> edges;
    auto edge=[&](int i,int j){edges.push_back({i,j});};
    for(int i=0;i<10;++i){
        edge(i,(i+1)%10);
        edge(i,10+i);
        edge(10+i,10+(i+2)%10);
    }
    assert(edges.size()==30);
    array<int,20> degree{};
    for(auto [i,j]:edges){degree[i]++;degree[j]++;}
    for(int d:degree)assert(d==3);
    vector<unsigned char> acyclic(ALL,0), one_tree(ALL,0);
    array<uint64_t,21> forest{}, tree{}, maximal{};
    uint64_t total=0;
    for(int s=0;s<ALL;++s){
        DSU dsu;
        bool good=true;
        for(auto [i,j]:edges){
            if((s&(1<<i)) && (s&(1<<j))){
                if(!dsu.join(i,j)){good=false;break;}
            }
        }
        if(good){
            int order=__builtin_popcount((unsigned)s);
            acyclic[s]=1;forest[order]++;total++;
            int roots=0;
            for(int i=0;i<N;++i)if((s>>i&1) && dsu.root(i)==i) roots++;
            if(order && roots==1){one_tree[s]=1;tree[order]++;}
        }
    }
    for(int s=0;s<ALL;++s)if(acyclic[s]){
        bool can_extend=false;
        for(int i=0;i<N;++i)if(!(s>>i&1) && acyclic[s|(1<<i)]){
            can_extend=true;break;
        }
        if(!can_extend)maximal[__builtin_popcount((unsigned)s)]++;
    }
    const array<uint64_t,21> expect={1,20,190,1140,4845,15492,38580,
        76260,120540,151920,150480,113400,60620,19600,2520,
        0,0,0,0,0,0};
    assert(forest==expect);
    assert(total==755608);
    assert(maximal[13]==1120 && maximal[14]==2520);
    for(int i=0;i<=20;++i)if(i!=13 && i!=14)assert(maximal[i]==0);
    assert(tree[14]==1860);
    std::cout << "CENSUS_OK vertices=20 edges=30 tested=1048576 forests=755608\n";
    std::cout << "CENSUS_OK forest_coefficients=";
    for(int i=0;i<=14;++i)cout<<(i?",":"")<<forest[i];
    cout<<"\n";
    std::cout << "CENSUS_OK maximum_order=14 minimum_FVS_size=6 optimum=2520\n";
    std::cout << "CENSUS_OK maximum_induced_trees=1860 disconnected_maximum_forests=660\n";
    std::cout << "CENSUS_OK inclusion_maximal_forests_13=1120 _14=2520\n";
}
