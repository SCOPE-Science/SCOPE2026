// Independent census using the cyclic (7,3,1) difference-set model of the Fano plane.
// Compile: c++ -std=c++17 -O2 secure_fano_crosscheck.cpp -o secure_fano_crosscheck
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;

int main() {
    array<array<int,7>,7> inc{};
    for (int p=0;p<7;p++) for (int ell=0;ell<7;ell++) {
        int d=(ell-p+7)%7;
        inc[p][ell] = (d==0 || d==1 || d==3);
    }
    auto dominates = [&](int A,int B)->bool {
        // A is a point mask, B is a line mask.
        for (int p=0;p<7;p++) if (!(A&(1<<p))) {
            bool covered=false;
            for (int ell=0;ell<7;ell++)
                if ((B&(1<<ell)) && inc[p][ell]) covered=true;
            if (!covered) return false;
        }
        for (int ell=0;ell<7;ell++) if (!(B&(1<<ell))) {
            bool covered=false;
            for (int p=0;p<7;p++)
                if ((A&(1<<p)) && inc[p][ell]) covered=true;
            if (!covered) return false;
        }
        return true;
    };
    auto secure = [&](int A,int B)->bool {
        if (!dominates(A,B)) return false;
        for (int p=0;p<7;p++) if (!(A&(1<<p))) {
            bool defended=false;
            for (int ell=0;ell<7;ell++) if ((B&(1<<ell)) && inc[p][ell]) {
                if (dominates(A|(1<<p), B^(1<<ell))) defended=true;
            }
            if (!defended) return false;
        }
        for (int ell=0;ell<7;ell++) if (!(B&(1<<ell))) {
            bool defended=false;
            for (int p=0;p<7;p++) if ((A&(1<<p)) && inc[p][ell]) {
                if (dominates(A^(1<<p), B|(1<<ell))) defended=true;
            }
            if (!defended) return false;
        }
        return true;
    };
    array<int,15> counts{};
    int ordinary_four=0;
    bool ordinary_below_four=false;
    vector<int> optimal;
    int geometric_solutions=0;
    for (int A=0;A<128;A++) for (int B=0;B<128;B++) {
        int k=__builtin_popcount((unsigned)A)+__builtin_popcount((unsigned)B);
        if (k == 4 && dominates(A,B)) ordinary_four++;
        if (k < 4 && dominates(A,B)) ordinary_below_four=true;
        bool good=secure(A,B);
        if (good) {
            counts[k]++;
            if (k==6) optimal.push_back(A | (B<<7));
        }
        int incidences=0;
        for(int p=0;p<7;p++) for(int ell=0;ell<7;ell++)
            if ((A&(1<<p)) && (B&(1<<ell))) incidences+=inc[p][ell];
        bool geom=(k==6 && __builtin_popcount((unsigned)A)==3 &&
                   __builtin_popcount((unsigned)B)==3 && incidences==2);
        if (geom) geometric_solutions++;
        // Independently compare predicates, not just minimum counts.
        if (k<=6) assert(good == geom);
    }
    assert(counts[6]==84 && optimal.size()==84 && geometric_solutions==84);
    assert(ordinary_four==21 && !ordinary_below_four);
    for (int k=0;k<6;k++) assert(counts[k]==0);
    vector<vector<int>> adj(optimal.size());
    for (int i=0;i<(int)optimal.size();i++) for(int j=0;j<i;j++) {
        if (__builtin_popcount((unsigned)(optimal[i]^optimal[j]))==2) {
            adj[i].push_back(j); adj[j].push_back(i);
        }
    }
    int total_deg=0;
    for (auto &lst: adj) { assert(lst.size()==4); total_deg+=lst.size(); }
    assert(total_deg==336);
    vector<int> levels;
    int radius=100,diam=0;
    for (int src=0; src<(int)optimal.size();src++) {
        vector<int> dist(optimal.size(),-1); queue<int> q;
        dist[src]=0; q.push(src);
        while(!q.empty()) {
            int v=q.front();q.pop();
            for(int w:adj[v]) if(dist[w]<0) {dist[w]=dist[v]+1;q.push(w);}
        }
        assert(all_of(dist.begin(),dist.end(),[](int x){return x>=0;}));
        int ecc=*max_element(dist.begin(),dist.end());
        diam=max(diam,ecc);radius=min(radius,ecc);
        if(src==0) {
            levels.assign(ecc+1,0);
            for(auto d:dist)levels[d]++;
        }
    }
    assert(radius==7 && diam==7);
    assert(levels==vector<int>({1,4,8,16,28,22,4,1}));
    cout << "graph_vertices=14 graph_edges=21\n";
    cout << "examined_subsets=16384\n";
    cout << "secure_sets_by_size=[";
    bool first=true;
    for(int k=0;k<=14;k++) if(counts[k]) {
        if(!first)cout<<", "; first=false;
        cout<<"("<<k<<", "<<counts[k]<<")";
    }
    cout<<"]\n";
    cout<<"ordinary_domination_minimum=4 ordinary_domination_minimum_count=21\n";
    cout<<"minimum_size=6 minimum_count=84 split_3_plus_3=84 incidences_two=84\n";
    cout<<"geometric_criterion_tested_for_all_subsets_of_size_at_most_6=true\n";
    cout<<"exchange_vertices=84 exchange_edges=168 exchange_degree=4 connected=true\n";
    cout<<"distance_layers=[";
    for(int i=0;i<(int)levels.size();i++) {if(i)cout<<", ";cout<<levels[i];}
    cout<<"]\n";
    cout<<"radius=7 diameter=7 eccentricity_distribution={7: 84}\n";
    return 0;
}
