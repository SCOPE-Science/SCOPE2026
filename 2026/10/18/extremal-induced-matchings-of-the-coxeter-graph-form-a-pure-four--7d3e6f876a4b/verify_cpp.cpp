// Standalone exact finite enumeration for induced matchings in a Fano-triangle graph.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;

int main() {
    set<int> fano;
    for (int i = 0; i < 7; ++i)
        fano.insert((1 << i) | (1 << ((i+1)%7)) | (1 << ((i+3)%7)));
    vector<int> triples;
    for (int a=0;a<7;++a) for(int b=a+1;b<7;++b) for(int c=b+1;c<7;++c) {
        int mask=(1<<a)|(1<<b)|(1<<c);
        if (!fano.count(mask)) triples.push_back(mask);
    }
    assert(triples.size()==28);
    bool adj[28][28] = {};
    vector<pair<int,int>> edges;
    for(int a=0;a<28;++a) for(int b=a+1;b<28;++b) {
        if ((triples[a]&triples[b])==0) {
            adj[a][b]=adj[b][a]=true;
            edges.emplace_back(a,b);
        }
    }
    assert(edges.size()==42);
    for (int a=0;a<28;++a) {
        int degree=0;for (int b=0;b<28;++b) degree+=adj[a][b];
        assert(degree==3);
    }
    auto compatible = [&](int i,int j) {
        auto [a,b]=edges[i];auto [c,d]=edges[j];
        if (a==c||a==d||b==c||b==d) return false;
        return !adj[a][c]&&!adj[a][d]&&!adj[b][c]&&!adj[b][d];
    };
    array<long long,43> histogram{};
    vector<U> sevens;
    vector<int> chosen;
    // Unlike the bitmask verifier, test each candidate against every selected edge.
    auto expand = [&](auto&& rec,int start,U bits)->void {
        histogram[chosen.size()]++;
        if(chosen.size()==7) sevens.push_back(bits);
        for (int j=start;j<42;++j) {
            bool legal=true;
            for(int i:chosen) if(!compatible(i,j)){legal=false;break;}
            if(!legal) continue;
            chosen.push_back(j);
            rec(rec,j+1,bits|(U(1)<<j));
            chosen.pop_back();
        }
    };
    expand(expand,0,0);
    sort(sevens.begin(),sevens.end());
    const array<int,9> expected{1,42,609,3808,10374,11172,4242,84,0};
    for(int i=0;i<9;++i) assert(histogram[i]==expected[i]);
    for(int i=8;i<43;++i) assert(histogram[i]==0);
    assert(sevens.size()==84);
    array<long long,85> pack{};
    // Independent depth first enumeration, checking new disjointness directly.
    vector<int> packing;
    auto pack_search = [&](auto&& rec,int start)->void {
        pack[packing.size()]++;
        for(int j=start;j<(int)sevens.size();++j){
            bool legal=true;
            for(int i:packing) if(sevens[i]&sevens[j]){legal=false;break;}
            if(!legal) continue;
            packing.push_back(j);
            rec(rec,j+1);
            packing.pop_back();
        }
    };
    pack_search(pack_search,0);
    const array<int,6> packs{1,84,1092,3528,2478,0};
    for(int i=0;i<6;++i) assert(pack[i]==packs[i]);
    for(int i=5;i<85;++i) assert(pack[i]==0);
    // Verify regularity and purity: no maximal compatible family has size < 4.
    for(int i=0;i<84;++i){
        int deg=0;for(int j=0;j<84;++j) if(i!=j && !(sevens[i]&sevens[j])) deg++;
        assert(deg==26);
    }
    array<int,4> small_maximal{};
    vector<int> family;
    auto purity = [&](auto&& rec,int from)->void {
        if(!family.empty()){
            bool extension=false;
            for(int j=0;j<84;++j) {
                if(find(family.begin(),family.end(),j)!=family.end()) continue;
                bool eligible=true;
                for(int i:family) if(sevens[i]&sevens[j]) {eligible=false;break;}
                if(eligible){extension=true;break;}
            }
            if(!extension) small_maximal[family.size()]++;
        }
        if(family.size()==3) return;
        for(int j=from;j<84;++j) {
            bool eligible=true;
            for(int i:family) if(sevens[i]&sevens[j]) {eligible=false;break;}
            if(eligible){family.push_back(j);rec(rec,j+1);family.pop_back();}
        }
    };
    purity(purity,0);
    assert((small_maximal==array<int,4>{0,0,0,0}));
    vector<vector<int>> witness{
        {0,4,19,28,33,39}, {1,20,22,32,35,41},
        {3,11,14,16,26,27,34}, {8,13,29,30,37,38},
        {9,17,23,25,36}, {2,7,10,15,18,21},
        {5,6,12,24,31,40}
    };
    array<int,42> seen{};
    for(const auto& group:witness) {
        for(int i:group) {assert(i>=0 && i<42);seen[i]++;}
        for(int i=0;i<(int)group.size();++i)
            for(int j=i+1;j<(int)group.size();++j)
                assert(compatible(group[i],group[j]));
    }
    for(int x:seen) assert(x==1);
    cout<<"VERTICES=28 EDGES=42\n";
    cout<<"INDUCED_MATCHING_COUNTS=";
    for(int i=0;i<9;++i) cout<<(i?",":"")<<histogram[i];
    cout<<"\nMAXIMUM_SIZE=7 MAXIMUM_COUNT=84\n";
    cout<<"PAIRWISE_DISJOINT_PACK_COUNTS=";
    for(int i=0;i<6;++i) cout<<(i?",":"")<<pack[i];
    cout<<"\nMAX_DISJOINT_PACK=4\nSEVEN_COLOR_WITNESS=VALID\n";
    cout<<"DISJOINTNESS_GRAPH=84_VERTICES_DEGREE_26_PURE_FACETS_2478\n";
    cout<<"MAXIMUM_MASKS_BEGIN\n";
    for(U bits:sevens)
        cout<<hex<<setfill('0')<<setw(11)<<bits<<dec<<"\n";
    cout<<"MAXIMUM_MASKS_END\n";
}
