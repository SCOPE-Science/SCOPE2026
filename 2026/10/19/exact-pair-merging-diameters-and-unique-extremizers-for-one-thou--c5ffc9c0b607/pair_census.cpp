// Exact finite pair-collision census for the Dzyga--Szykula automata.
// Compile: c++ -O3 -std=c++17 -Wall -Wextra -pedantic pair_census.cpp -o pair_census
// Run: ./pair_census 500 > pair_census.tsv
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

struct Automaton {vector<int> a,b;};

Automaton make(int k) {
    if(k<1) throw runtime_error("k must be >=1");
    const int n=3*k+6;
    vector<int> a(n,-1), b(n,-1);
    a[0]=0; b[0]=1;
    for(int i=1; i<=2*k+3; ++i) {
        a[i]=(i%2 ? i+1 : i-1);
        b[i]=(i%2 ? i-1 : i+1);
    }
    for(int i=2*k+4; i<n; ++i) {
        if (i==2*k+5) a[i]=3;
        else if (i==n-1 && i%2==0) a[i]=i;
        else if (i%2==0) a[i]=i+1;
        else a[i]=i-1;

        if (i==2*k+4) b[i]=2;
        else if (i==n-1 && i%2==1) b[i]=i;
        else if (i%2==1) b[i]=i+1;
        else b[i]=i-1;
    }
    for(int i=0;i<n;++i) {
        if(a[i]<0 || a[i]>=n || b[i]<0 || b[i]>=n)
            throw runtime_error("invalid transition");
    }
    return {a,b};
}

int main(int argc, char** argv) {
    try {
        if(argc != 2) throw runtime_error("usage: pair_census MAX_K");
        int K=stoi(argv[1]);
        if(K<1 || K>1000) throw runtime_error("bound MAX_K must lie in 1..1000");
        cout << "k\tn\tdiameter\tfarthest_p\tfarthest_q\tcount_farthest\tall_pairs_merge\n";
        for(int k=1;k<=K;++k) {
            auto m=make(k);
            const int n=3*k+6;
            const int total=n*(n+1)/2;
            vector<vector<int>> ra(n),rb(n);
            for(int p=0;p<n;++p) {ra[m.a[p]].push_back(p);rb[m.b[p]].push_back(p);}
            auto id=[n](int p,int q)->int {return p*n - p*(p-1)/2 + q-p;};
            vector<int> d(total,-1);
            vector<int> Q(total);
            int head=0,tail=0;
            for(int p=0;p<n;++p) {
                d[id(p,p)]=0;
                Q[tail++]=p*n+p;
            }
            while(head<tail) {
                const int z=Q[head++];
                const int x=z/n,y=z%n;
                const int h=d[id(x,y)]+1;
                auto reverse_step=[&](const vector<vector<int>>& R) {
                    for(int p:R[x]) for(int q:R[y]) {
                        if(x==y && p>=q) continue;
                        const int lo=min(p,q), hi=max(p,q);
                        const int ix=id(lo,hi);
                        if(d[ix]<0) {d[ix]=h; Q[tail++]=lo*n+hi;}
                    }
                };
                reverse_step(ra);reverse_step(rb);
            }
            int diameter=-1, pstar=-1, qstar=-1, count=0;
            for(int p=0;p<n;++p) for(int q=p+1;q<n;++q) {
                int t=d[id(p,q)];
                if(t<0) throw runtime_error("nonsynchronizable pair k="+to_string(k));
                if(t>diameter) {diameter=t;pstar=p;qstar=q;count=1;}
                else if(t==diameter) ++count;
            }
            const int expected=(k%2 ? (5*k*k+32*k+47)/4 : (5*k*k+34*k+44)/4);
            const int ep=(k+2)/2;
            if(diameter!=expected || pstar!=ep || qstar!=ep+1 || count!=1)
                throw runtime_error("unexpected value at k="+to_string(k));
            cout<<k<<'\t'<<n<<'\t'<<diameter<<'\t'<<pstar<<'\t'<<qstar<<'\t'<<count<<"\t1\n";
        }
        return 0;
    } catch (const exception& e) {cerr << "FAIL: " << e.what()<<'\n';return 2;}
}
