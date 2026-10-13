#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

template<int N>
struct CensusResult {
    int map_count;
    int maximum;
};

template<int N>
static CensusResult<N> threshold_only() {
    using Map = array<unsigned char,N>;
    vector<Map> maps;
    Map cur{};
    function<void(int,int)> rec = [&](int i, int lo) {
        if (i==N) { maps.push_back(cur); return; }
        for (int v=lo; v<N; ++v) { cur[i]=v; rec(i+1,v); }
    };
    rec(0,0);

    constexpr int P=N*(N+1)/2;
    int idx[N][N];
    vector<pair<int,int>> pairs;
    for (int i=0;i<N;i++) for (int j=i;j<N;j++) {
        idx[i][j]=(int)pairs.size();
        pairs.push_back({i,j});
    }

    vector<array<unsigned long long,P>> pred(maps.size());
    unsigned long long diag=0;
    for (int i=0;i<N;i++) diag |= 1ULL<<idx[i][i];

    for (int m=0;m<(int)maps.size();m++) {
        for (int s=0;s<P;s++) {
            auto [i,j]=pairs[s];
            int x=maps[m][i], y=maps[m][j];
            pred[m][idx[x][y]] |= 1ULL<<s;
        }
    }

    int global_max=-1;
    #pragma omp parallel for schedule(dynamic,8) reduction(max:global_max)
    for (int ia=0; ia<(int)maps.size(); ia++) {
        for (int ib=ia; ib<(int)maps.size(); ib++) {
            unsigned long long seen=diag, frontier=diag;
            int depth=0;
            while (frontier) {
                unsigned long long pre=0, x=frontier;
                while (x) {
                    int u=__builtin_ctzll(x);
                    x&=x-1;
                    pre |= pred[ia][u] | pred[ib][u];
                }
                unsigned long long next=pre & ~seen;
                if (!next) break;
                ++depth;
                seen |= next;
                frontier=next;
            }
            global_max=max(global_max,depth);
        }
    }
    return {(int)maps.size(),global_max};
}

struct Ext9 {
    string a,b;
    pair<int,int> hard;
};

static vector<Ext9> classify_nine() {
    const int N=9, P=45;
    using Map=array<unsigned char,N>;
    vector<Map> maps;
    Map cur{};
    function<void(int,int)> rec = [&](int i,int lo) {
        if (i==N) { maps.push_back(cur); return; }
        for (int v=lo;v<N;v++) { cur[i]=v; rec(i+1,v); }
    };
    rec(0,0);

    int idx[N][N];
    vector<pair<int,int>> pairs;
    for (int i=0;i<N;i++) for (int j=i;j<N;j++) {
        idx[i][j]=(int)pairs.size();
        pairs.push_back({i,j});
    }
    vector<array<unsigned long long,P>> pred(maps.size());
    unsigned long long diag=0;
    for (int i=0;i<N;i++) diag |= 1ULL<<idx[i][i];
    for (int m=0;m<(int)maps.size();m++) for (int s=0;s<P;s++) {
        auto [i,j]=pairs[s];
        pred[m][idx[maps[m][i]][maps[m][j]]] |= 1ULL<<s;
    }

    struct Raw { int ia,ib,s; };
    vector<Raw> raw;
    #pragma omp parallel for schedule(dynamic,8)
    for (int ia=0; ia<(int)maps.size(); ia++) {
        for (int ib=ia; ib<(int)maps.size(); ib++) {
            unsigned long long seen=diag, frontier=diag, level9=0;
            int depth=0;
            while (frontier) {
                unsigned long long pre=0, x=frontier;
                while (x) {
                    int u=__builtin_ctzll(x); x&=x-1;
                    pre |= pred[ia][u] | pred[ib][u];
                }
                unsigned long long next=pre & ~seen;
                if (!next) break;
                ++depth; seen|=next; frontier=next;
                if (depth==9) level9=next;
            }
            if (depth==9) {
                while (level9) {
                    int s=__builtin_ctzll(level9); level9&=level9-1;
                    #pragma omp critical
                    raw.push_back({ia,ib,s});
                }
            }
            if (depth>9) {
                #pragma omp critical
                { cerr<<"distance above nine found\n"; exit(2); }
            }
        }
    }

    sort(raw.begin(),raw.end(),[](const Raw&x,const Raw&y){
        return tie(x.ia,x.ib,x.s)<tie(y.ia,y.ib,y.s);
    });
    vector<Ext9> out;
    for (auto r:raw) {
        auto encode=[&](int m) {
            string s; for (auto v:maps[m]) s.push_back(char('0'+v)); return s;
        };
        out.push_back({encode(r.ia),encode(r.ib),pairs[r.s]});
    }
    return out;
}

int main() {
    vector<int> maxes, counts;
    auto r1=threshold_only<1>(); counts.push_back(r1.map_count); maxes.push_back(r1.maximum);
    auto r2=threshold_only<2>(); counts.push_back(r2.map_count); maxes.push_back(r2.maximum);
    auto r3=threshold_only<3>(); counts.push_back(r3.map_count); maxes.push_back(r3.maximum);
    auto r4=threshold_only<4>(); counts.push_back(r4.map_count); maxes.push_back(r4.maximum);
    auto r5=threshold_only<5>(); counts.push_back(r5.map_count); maxes.push_back(r5.maximum);
    auto r6=threshold_only<6>(); counts.push_back(r6.map_count); maxes.push_back(r6.maximum);
    auto r7=threshold_only<7>(); counts.push_back(r7.map_count); maxes.push_back(r7.maximum);
    auto r8=threshold_only<8>(); counts.push_back(r8.map_count); maxes.push_back(r8.maximum);
    auto r9=threshold_only<9>(); counts.push_back(r9.map_count); maxes.push_back(r9.maximum);

    vector<int> expected_counts={1,3,10,35,126,462,1716,6435,24310};
    vector<int> expected_maxes={0,1,2,3,4,5,6,7,9};
    if (counts!=expected_counts || maxes!=expected_maxes) return 3;

    auto ext=classify_nine();
    if (ext.size()!=2) return 4;
    if (!(ext[0].a=="001244558" && ext[0].b=="023446788" && ext[0].hard==make_pair(1,6))) return 5;
    if (!(ext[1].a=="001244568" && ext[1].b=="033446788" && ext[1].hard==make_pair(2,7))) return 6;

    // Two unordered pairs give four ordered pairs because both letters differ.
    cout<<"VERIFY_OK maxima=0,1,2,3,4,5,6,7,9 "
        <<"map_counts=1,3,10,35,126,462,1716,6435,24310 "
        <<"n9_unordered_extremals=2 n9_ordered_extremals=4 "
        <<"hard_pairs=(1,6),(2,7)\n";
}
