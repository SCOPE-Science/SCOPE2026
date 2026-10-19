// Independent direct vertex-decision enumeration of minimum maximal matchings.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
static constexpr int N=24;
static array<unsigned, N> nbr{};
static vector<pair<int,int>> edges;
static int edge_id[N][N];
static set<vector<int>> answers;
static unsigned long long leaves=0;

static void search(unsigned undecided, unsigned unmatched, vector<int>& chosen) {
    if (chosen.size()>8) return;
    if (!undecided) {
        if (chosen.size()!=8) return;
        ++leaves;
        auto row=chosen;
        sort(row.begin(),row.end());
        assert(row.size()==8);
        for(int i=0;i<8;i++) for(int j=0;j<i;j++) {
            auto a=edges[row[i]], b=edges[row[j]];
            assert(a.first!=b.first && a.first!=b.second && a.second!=b.first && a.second!=b.second);
        }
        for(auto e:edges) assert(!((unmatched>>e.first&1u) && (unmatched>>e.second&1u)));
        answers.insert(row);
        return;
    }
    int u=__builtin_ctz(undecided);
    unsigned rest=undecided&~(1u<<u);
    // A vertex may remain unmatched iff this cannot create an uncovered edge.
    if ((nbr[u]&unmatched)==0) search(rest,unmatched|(1u<<u),chosen);
    unsigned options=nbr[u]&rest;
    while(options) {
        int v=__builtin_ctz(options);
        options&=options-1;
        chosen.push_back(edge_id[u][v]);
        search(rest&~(1u<<v),unmatched,chosen);
        chosen.pop_back();
    }
}
int main() {
    set<pair<int,int>> eset;
    for(int i=0;i<12;i++) {
        auto add=[&](int a,int b){if(a>b)swap(a,b); eset.insert({a,b});};
        add(i,(i+1)%12);
        add(i,i+12);
        add(i+12,12+(i+5)%12);
    }
    edges.assign(eset.begin(),eset.end());
    assert(edges.size()==36);
    for (int i=0;i<N;i++) for(int j=0;j<N;j++) edge_id[i][j]=-1;
    for(int i=0;i<(int)edges.size();i++) {
        auto [u,v]=edges[i];
        nbr[u]|=1u<<v; nbr[v]|=1u<<u;
        edge_id[u][v]=edge_id[v][u]=i;
    }
    vector<int> chosen;
    search((1u<<N)-1,0,chosen);
    assert(leaves==90 && answers.size()==90);
    ofstream out("matchings_cpp.txt");
    for(const auto& row: answers) {
        for(int i=0;i<8;i++) out << row[i] << (i==7?'\n':' ');
    }
    out.close();
    cout << "edge_count=" << edges.size() << " minimum_lower_bound=8 minimum_witnesses=" << answers.size() << " verified_leaves=" << leaves << "\n";
    cout << "matchings_cpp.txt has 90 rows of 8 edge indices, canonical ascending\n";
}
