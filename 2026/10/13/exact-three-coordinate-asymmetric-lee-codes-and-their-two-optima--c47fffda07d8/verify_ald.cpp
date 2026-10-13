// Independent exact bitset branch-and-bound verification, C++17.
// The vertices are quaternary words of length three, indexed by
// s0+4*s1+16*s2, and the matrix is the ALD cost at lambda=1.
#include <iostream>
#include <cstdint>
using namespace std;

static uint64_t adjacent[64];
static int optimum=0;
static unsigned long long number_of_optima=0, search_nodes=0;
static inline int low(uint64_t m) {return __builtin_ctzll(m);}

// Greedy proper coloring of the induced compatibility graph.
// Each color class is independent, so each clique uses at most one
// vertex from every color class. The sorted color labels are bounds.
static void colored_order(uint64_t mask, int vertices[64],
                          int colors[64], int &length) {
    length=0;
    int color=0;
    while(mask) {
        uint64_t available=mask;
        ++color;
        while(available) {
            int v=low(available);
            uint64_t bit=1ULL<<v;
            vertices[length]=v;
            colors[length]=color;
            ++length;
            mask &= ~bit;
            available &= ~bit;
            available &= ~adjacent[v];
        }
    }
}

static void search(uint64_t candidates, int depth) {
    ++search_nodes;
    if(!candidates) {
        if(depth>optimum) {
            optimum=depth;
            number_of_optima=1;
        } else if(depth==optimum) {
            ++number_of_optima;
        }
        return;
    }
    int order[64], color[64], length;
    colored_order(candidates,order,color,length);
    for(int i=length-1;i>=0;--i) {
        if(depth+color[i]<optimum) return;
        int vertex=order[i];
        uint64_t bit=1ULL<<vertex;
        search(candidates&adjacent[vertex],depth+1);
        candidates &= ~bit;
    }
}

int main() {
    const int d[4][4]={{0,2,2,4},{2,0,1,2},
                       {2,1,0,2},{4,2,2,0}};
    int edges=0;
    for(int i=0;i<64;++i) for(int j=i+1;j<64;++j) {
        int a=i,b=j,weight=0;
        for(int k=0;k<3;++k) {
            weight+=d[a%4][b%4];
            a/=4;
            b/=4;
        }
        if(weight>=3) {
            adjacent[i]|=1ULL<<j;
            adjacent[j]|=1ULL<<i;
            ++edges;
        }
    }
    search(~0ULL,0);
    if(edges!=1752 || optimum!=19 || number_of_optima!=32) return 1;
    cout << "VERIFY_OK_CPP edges=" << edges
         << " maximum=" << optimum
         << " labeled_optima=" << number_of_optima
         << " search_nodes=" << search_nodes << '\n';
    return 0;
}
