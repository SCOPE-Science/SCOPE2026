// Exhaustive finite certificate for ordinary color refinement on split graphs.
// Build: g++ -std=c++17 -O3 -Wall -Wextra verify_split_cutoff.cpp -o verify_split_cutoff
// Run:   ./verify_split_cutoff
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

struct Graph {
    int n, clique_size;
    array<unsigned short, 10> adj{};
    bool edge(int a, int b) const { return (adj[a] >> b) & 1u; }
    int degree(int a) const { return __builtin_popcount((unsigned int)adj[a]); }
};

Graph split_graph(int n, int k, const vector<int>& columns) {
    Graph g; g.n=n; g.clique_size=k;
    for (int a=0;a<k;a++) for (int b=a+1;b<k;b++) {
        g.adj[a] |= 1u<<b; g.adj[b] |= 1u<<a;
    }
    for (int j=0;j<(int)columns.size();j++) for (int a=0;a<k;a++)
        if ((columns[j]>>a)&1) {
            g.adj[a] |= 1u<<(k+j); g.adj[k+j] |= 1u<<a;
        }
    return g;
}

// Equivalent colors receive identical integers; numbers themselves are irrelevant.
vector<int> stable_colors(const Graph& g) {
    vector<int> colors(g.n,0);
    while (true) {
        map<vector<int>,int> unique_signatures;
        vector<int> next(g.n);
        for (int a=0;a<g.n;a++) {
            vector<int> sig(g.n+1,0);
            sig[0]=colors[a];
            for (int b=0;b<g.n;b++) if(g.edge(a,b)) sig[1+colors[b]]++;
            auto [it,inserted]=unique_signatures.emplace(sig,(int)unique_signatures.size());
            (void) inserted;
            next[a]=it->second;
        }
        bool same_partition=true;
        for (int a=0;a<g.n;a++) for (int b=0;b<a;b++)
            if ((next[a]==next[b]) != (colors[a]==colors[b])) same_partition=false;
        if (same_partition) return next;
        colors=next;
    }
}

// Complete, exact backtracking over all color-preserving vertex bijections.
// A partial image must preserve adjacency and non-adjacency to assigned vertices.
struct Automorphism {
    const Graph& g;
    const vector<int>& colors;
    array<int,10> image{};
    unsigned short occupied=0;
    Automorphism(const Graph& graph, const vector<int>& c):g(graph),colors(c) {
        image.fill(-1);
    }
    bool extend(int left) {
        if (left==0) return true;
        int v=-1;
        vector<int> best;
        int fewest=100;
        for (int a=0;a<g.n;a++) if(image[a]<0) {
            vector<int> feasible;
            for (int b=0;b<g.n;b++) if(!(occupied>>b&1) && colors[a]==colors[b]) {
                bool matches=true;
                for (int x=0;x<g.n;x++) if(image[x]>=0 && g.edge(a,x)!=g.edge(b,image[x])) {
                    matches=false; break;
                }
                if(matches) feasible.push_back(b);
            }
            if(feasible.empty()) return false;
            if((int)feasible.size()<fewest) {
                fewest=(int)feasible.size();
                v=a; best=std::move(feasible);
                if(fewest==1)break;
            }
        }
        for(int b:best) {
            image[v]=b; occupied |= (1u<<b);
            if(extend(left-1))return true;
            occupied ^= (1u<<b); image[v]=-1;
        }
        return false;
    }
    bool moves(int source, int target) {
        image.fill(-1); image[source]=target; occupied=1u<<target;
        return extend(g.n-1);
    }
};

bool orbit_exact(const Graph& g, const vector<int>& colors, pair<int,int>& mismatch) {
    Automorphism aut(g,colors);
    for(int a=0;a<g.n;a++)for(int b=a+1;b<g.n;b++)
        if(colors[a]==colors[b] && !aut.moves(a,b)) {
            mismatch={a,b}; return false;
        }
    return true;
}

// Under the degree separation verified below, isomorphisms must preserve
// the clique and the independent set. Independent labels only permute the
// columns, and clique labels permute mask bits. This is an exact canonical form.
vector<int> column_canonical(int k, const vector<int>& columns) {
    vector<int> p(k); iota(p.begin(),p.end(),0);
    vector<int> best;
    bool first=true;
    do {
        vector<int> transformed;
        for(int mask:columns) {
            int new_mask=0;
            for(int i=0;i<k;i++)if((mask>>i)&1)new_mask|=1<<p[i];
            transformed.push_back(new_mask);
        }
        sort(transformed.begin(),transformed.end());
        if(first || transformed<best) {best=transformed;first=false;}
    }while(next_permutation(p.begin(),p.end()));
    return best;
}

struct FailedRepresentation { int k; vector<int> columns; };

int main() {
    vector<FailedRepresentation> witnesses;
    for(int n=1;n<=10;n++) {
        long long tested=0,failed=0;
        for(int k=0;k<=n;k++) {
            const int independent_size=n-k;
            const int maximum_mask=(1<<k)-1;
            vector<int> masks(independent_size,0);
            auto enumerate=[&](auto&&self,int index,int lower_bound)->void {
                if(index<independent_size) {
                    for(int m=lower_bound;m<=maximum_mask;m++) {
                        masks[index]=m;
                        self(self,index+1,m);
                    }
                    return;
                }
                Graph g=split_graph(n,k,masks);
                tested++;
                auto colors=stable_colors(g);
                pair<int,int> mismatch{-1,-1};
                if(!orbit_exact(g,colors,mismatch)) {
                    failed++;
                    if(n<10) { cerr<<"Unexpected smaller obstruction.\n"; exit(3); }
                    witnesses.push_back({k,masks});
                    cout<<"FAIL k="<<k<<" columns=";
                    for(int j=0;j<independent_size;j++)cout<<(j?",":"")<<masks[j];
                    cout<<" mismatch="<<mismatch.first<<":"<<mismatch.second<<"\n";
                }
            };
            enumerate(enumerate,0,0);
        }
        cout<<"COUNT n="<<n<<" representations="<<tested<<" failures="<<failed<<"\n";
        if(n==9 && (tested!=123983 || failed!=0))return 4;
        if(n==10 && (tested!=1592513 || failed!=71))return 5;
    }
    map<pair<int,vector<int>>,int> classes;
    for(auto& w:witnesses) {
        Graph g=split_graph(10,w.k,w.columns);
        int clique_degree=g.degree(0);
        int independent_degree=g.degree(w.k);
        if(clique_degree<=independent_degree)return 6;
        for(int i=0;i<w.k;i++)if(g.degree(i)!=clique_degree)return 7;
        for(int i=w.k;i<10;i++)if(g.degree(i)!=independent_degree)return 8;
        classes[{w.k,column_canonical(w.k,w.columns)}]++;
    }
    cout<<"ISOMORPHISM_CLASSES "<<classes.size()<<"\n";
    for(const auto&[key,multiplicity]:classes) {
        cout<<"CLASS k="<<key.first<<" canonical_columns=";
        for(int i=0;i<(int)key.second.size();i++)cout<<(i?",":"")<<key.second[i];
        cout<<" representations="<<multiplicity<<"\n";
    }
    if(classes.size()!=4)return 9;
    cout<<"VERIFIED_EXACT_CUTOFF_AND_FOUR_CLASSES\n";
}
