// Exhaustive finite verification of characteristic-sequence inequalities
// for transitive permutations on 13 ordered sites.
//
// Compile: c++ -O3 -std=c++17 verify_characteristic13.cpp -o verify_characteristic13
// Execute each fixed first successor a=1,...,12 separately.
// The zero-based symbols here correspond to the one-based symbols in Wang's
// formulation by adding one throughout.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
using namespace std;

int main(int argc, char** argv) {
    constexpr int n = 13, v = n - 1;
    if (argc != 2) { cerr << "usage: verify_characteristic13 FIRST_SUCCESSOR(1..12)\n"; return 2; }
    char* end = nullptr;
    long arg = strtol(argv[1], &end, 10);
    if (*end != '\0' || arg < 1 || arg >= n) return 2;
    int a = int(arg);

    // Every 13-cycle has exactly one ordered cyclic representation
    // 0 -> a -> cycle[2] -> ... -> cycle[12] -> 0.
    array<int,n> cycle{}, p{};
    iota(cycle.begin(), cycle.end(), 0);
    swap(cycle[1], cycle[a]);
    sort(cycle.begin()+2, cycle.end());
    uint64_t total=0, violations=0, equality_cases=0, equality_nonshifts=0;
    uint64_t min_positive_deficit=UINT64_MAX, near_count=0;
    array<int,n> near_witness{};
    do {
        for (int i=0; i<n-1; i++) p[cycle[i]] = cycle[i+1];
        p[cycle[n-1]] = cycle[0];
        // The graph vertices are unit edges [i,i+1], i=0,...,11.
        // Edge i->j exists iff [j,j+1] lies in the integer convex hull
        // of {p[i],p[i+1]}. As n=13, uint16_t stores every graph mask.
        array<uint16_t,v> edges{}, m{};
        for (int i=0; i<v; i++) {
            int lo=min(p[i],p[i+1]), hi=max(p[i],p[i+1]);
            edges[i] = uint16_t(((1u<<hi)-1u) ^ ((1u<<lo)-1u));
        }
        // Breadth-first search by bitset layers gives the shortest
        // strictly positive closed directed walk through each vertex.
        for (int i=0; i<v; i++) {
            uint16_t frontier=edges[i], seen=uint16_t(1u<<i);
            int length=1;
            while (length<=v && !(frontier&(1u<<i))) {
                uint16_t fresh=uint16_t(frontier & ~seen);
                seen=uint16_t(seen|frontier);
                frontier=0;
                while (fresh) {
                    int j=__builtin_ctz(unsigned(fresh));
                    fresh=uint16_t(fresh & (fresh-1));
                    frontier=uint16_t(frontier|edges[j]);
                }
                ++length;
            }
            m[i] = uint16_t(length);
        }
        sort(m.begin(),m.end());
        bool bad=false, eq=true;
        uint64_t deficit=0;
        for (int i=0; i<v; i++) {
            if (m[i] > i+1) bad=true;
            if (m[i] != i+1) eq=false;
            if(m[i]<=i+1) deficit += (i+1)-m[i];
        }
        if (bad) {
            if (++violations == 1) {
                cerr << "First violation permutation:";
                for (int x:p) cerr<<' '<<x;
                cerr<<"; sorted characteristic:";
                for (int x:m) cerr<<' '<<x;
                cerr<<'\n';
            }
        }
        if (!bad && deficit>0) {
            if(deficit<min_positive_deficit){min_positive_deficit=deficit;near_count=1;near_witness=p;}
            else if(deficit==min_positive_deficit) ++near_count;
        }
        if (eq) {
            ++equality_cases;
            bool shift=true;
            for (int j=0;j<n;j++) if(p[j] != (j+a)%n) shift=false;
            if(!shift) {
                ++equality_nonshifts;
                cerr<<"Unexpected equality permutation:";
                for(int x:p)cerr<<' '<<x;
                cerr<<'\n';
            }
        }
        ++total;
    } while(next_permutation(cycle.begin()+2, cycle.end()));
    cout << "first_successor="<<a<<" cycles="<<total
         <<" violations="<<violations<<" equality="<<equality_cases
         <<" equality_nonshifts="<<equality_nonshifts
         <<" min_positive_deficit="<<min_positive_deficit
         <<" near_count="<<near_count<<'\n';
    cout << "near_witness:"; for(int x:near_witness) cout<<' '<<x;cout<<'\n';
    if(total!=39916800ULL || violations || equality_cases!=1 || equality_nonshifts) return 1;
    return 0;
}
