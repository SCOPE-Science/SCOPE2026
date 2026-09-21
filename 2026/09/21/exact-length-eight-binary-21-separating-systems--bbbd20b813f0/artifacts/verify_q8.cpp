#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using std::array;
using std::cout;
using std::vector;

class ExactSearch {
public:
    int n = 8;
    int mask = 255;
    int d = 0;
    int base_word = 0;
    int vertex_count = 0;
    int blocks = 0;
    int best = 0;
    vector<int> words;
    vector<vector<std::uint64_t>> adjacency;

    static int popcount(int x) {
        return __builtin_popcount(static_cast<unsigned>(x));
    }

    bool separating_triple(int a, int b, int c) const {
        const int t[3] = {a,b,c};
        for (int k=0;k<3;k++) {
            const int outsider=t[k], y=t[(k+1)%3], z=t[(k+2)%3];
            // There must be a coordinate at which y,z agree and outsider differs.
            if ((((~(y^z)) & mask) & (outsider^y)) == 0) return false;
        }
        return true;
    }

    bool adjacent(int i,int j) const {
        return (adjacency[i][j>>6] >> (j&63)) & 1ULL;
    }

    void build_for_distance(int delta) {
        d=delta;
        base_word=(1<<d)-1;
        words.clear();
        for (int x=1;x<=mask;x++) {
            if (x==base_word) continue;
            if (popcount(x)<d || popcount(x^base_word)<d) continue;
            if (!separating_triple(0,base_word,x)) continue;
            words.push_back(x);
        }
        vertex_count=static_cast<int>(words.size());
        blocks=(vertex_count+63)/64;
        adjacency.assign(vertex_count,vector<std::uint64_t>(blocks,0));
        for (int i=0;i<vertex_count;i++) for (int j=i+1;j<vertex_count;j++) {
            if (popcount(words[i]^words[j])<d) continue;
            if (!separating_triple(0,words[i],words[j])) continue;
            if (!separating_triple(base_word,words[i],words[j])) continue;
            adjacency[i][j>>6] |= 1ULL<<(j&63);
            adjacency[j][i>>6] |= 1ULL<<(i&63);
        }
    }

    // Exact maximum-clique search with the additional 3-uniform separating constraint.
    // The greedy coloring is only an upper bound for pruning: every feasible completion
    // is a clique in the compatibility graph.
    void expand(vector<int>& chosen, const vector<int>& candidates) {
        if (static_cast<int>(chosen.size()+candidates.size())<=best) return;
        if (candidates.empty()) {
            best=std::max(best,static_cast<int>(chosen.size()));
            return;
        }

        vector<int> order, bound, remaining=candidates;
        int color=0;
        while (!remaining.empty()) {
            ++color;
            vector<int> next, cls;
            for (int v:remaining) {
                bool conflict=false;
                for (int u:cls) if (adjacent(v,u)) { conflict=true; break; }
                if (!conflict) {
                    cls.push_back(v);
                    order.push_back(v);
                    bound.push_back(color);
                } else next.push_back(v);
            }
            remaining.swap(next);
        }

        vector<char> alive(vertex_count,0);
        for (int v:candidates) alive[v]=1;

        for (int k=static_cast<int>(order.size())-1;k>=0;k--) {
            if (static_cast<int>(chosen.size())+bound[k]<=best) return;
            const int v=order[k];
            if (!alive[v]) continue;

            chosen.push_back(v);
            vector<int> next;
            for (int w:candidates) {
                if (!alive[w] || w==v || !adjacent(v,w)) continue;
                bool ok=true;
                for (int r:chosen) {
                    if (r!=v && !separating_triple(words[r],words[v],words[w])) {
                        ok=false;
                        break;
                    }
                }
                if (ok) next.push_back(w);
            }
            expand(chosen,next);
            chosen.pop_back();
            alive[v]=0;
        }
    }

    int maximum_with_canonical_third_word(int word) {
        const auto it=std::find(words.begin(),words.end(),word);
        if (it==words.end()) return -1;
        const int root=static_cast<int>(it-words.begin());
        best=1;
        vector<int> chosen={root};
        vector<int> candidates;
        for (int w=0;w<vertex_count;w++) if (w!=root && adjacent(root,w)) candidates.push_back(w);
        expand(chosen,candidates);
        return best+2; // add the normalized closest pair 0 and base_word
    }
};

static bool explicit_code_is_valid() {
    const array<int,10> C={0x00,0x03,0xea,0xe6,0xd2,0xa1,0x9d,0x71,0x4d,0x3e};
    ExactSearch S;
    for (int i=0;i<10;i++) for (int j=i+1;j<10;j++) {
        if (ExactSearch::popcount(C[i]^C[j])<2) return false;
    }
    for (int i=0;i<10;i++) for (int j=i+1;j<10;j++) for (int k=j+1;k<10;k++) {
        if (!S.separating_triple(C[i],C[j],C[k])) return false;
    }
    return true;
}

int main() {
    assert(explicit_code_is_valid());
    cout << "explicit_size=10 valid=yes\n";

    ExactSearch S;
    int global_max=2;
    for (int d=2;d<=4;d++) {
        S.build_for_distance(d);
        const int outside=8-d;
        for (int alpha=1;alpha<=d-1;alpha++) {
            for (int beta=0;beta<=outside;beta++) {
                if (alpha+beta<d || beta<alpha) continue;
                const int canonical=((1<<alpha)-1) | (((1<<beta)-1)<<d);
                const int value=S.maximum_with_canonical_third_word(canonical);
                assert(value>=0);
                global_max=std::max(global_max,value);
                cout << "d=" << d << " alpha=" << alpha << " beta=" << beta
                     << " maximum=" << value << "\n";
            }
        }
    }
    assert(global_max==10);
    cout << "upper_certificate=10\n";
    cout << "gp_Q8=10\n";
    return 0;
}
