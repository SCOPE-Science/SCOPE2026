// Exhaustive small-instance verification of zero forcing reconfiguration on clique-path joins.
// Compile: c++ -std=c++17 -O2 generalized_fan_zero_forcing_check.cpp -o check && ./check
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using U=uint64_t;
static int pop(U x) { return __builtin_popcountll(x); }

bool zero_forces(const vector<U>& adj, U blue) {
    int N=(int)adj.size(); U all=(U(1)<<N)-1;
    for (;;) {
        U next=blue;
        for(int i=0;i<N;++i) if ((blue>>i)&1) {
            U white=adj[i]&(~blue);
            if (white && !(white&(white-1))) next |= white;
        }
        if(next==all) return true;
        if(next==blue) return false;
        blue=next;
    }
}

vector<U> expected(int s,int n) {
    U hubs=(U(1)<<s)-1;
    vector<U> v{hubs|(U(1)<<s),hubs|(U(1)<<(s+n-1))};
    for(int u=0;u<s;++u) {
        U rest=hubs&~(U(1)<<u);
        v.push_back(rest|(U(1)<<s)|(U(1)<<(s+1)));
        v.push_back(rest|(U(1)<<(s+n-2))|(U(1)<<(s+n-1)));
    }
    sort(v.begin(),v.end());
    if(unique(v.begin(),v.end())!=v.end()) throw runtime_error("Duplicate predicted set");
    return v;
}

int main() {
    unsigned long long tests=0,good=0,edges=0;
    int graphs=0;
    for(int s=1;s<=6;++s) for(int n=4;n<=12;++n) {
        int N=s+n; vector<U> a(N,0);
        for(int i=0;i<N;++i) for(int j=i+1;j<N;++j) {
            bool isedge = (i<s && j<s)||(i<s && j>=s)||(i>=s && j>=s && j==i+1);
            if(isedge) {a[i]|=U(1)<<j; a[j]|=U(1)<<i;}
        }
        auto exp=expected(s,n);
        vector<U> actual;
        U all=U(1)<<N;
        for(U B=0;B<all;++B) {
            int k=pop(B);
            if(k>s+1) continue;
            ++tests;
            bool z=zero_forces(a,B);
            if(k<=s) { if(z) throw runtime_error("Forcing set below predicted minimum"); }
            else if(z) {actual.push_back(B);++good;}
        }
        sort(actual.begin(),actual.end());
        if(actual!=exp) throw runtime_error("Incorrect predicted minimum sets");
        int ecount=0;
        for(int i=0;i<(int)actual.size();++i)
            for(int j=i+1;j<(int)actual.size();++j)
                if(pop(actual[i]^actual[j])==2) ++ecount;
        int predicted_edges=s*(s+1)+1; // two K_{s+1} plus one bridge
        if(ecount!=predicted_edges) throw runtime_error("Wrong edge count");
        // Check unique cross-clique edge and complete cliques, using explicit labels.
        set<U> left,right;
        U hubs=(U(1)<<s)-1;
        left.insert(hubs|(U(1)<<s));
        right.insert(hubs|(U(1)<<(s+n-1)));
        for(int u=0;u<s;++u) {
            U rest=hubs&~(U(1)<<u);
            left.insert(rest|(U(1)<<s)|(U(1)<<(s+1)));
            right.insert(rest|(U(1)<<(s+n-2))|(U(1)<<(s+n-1)));
        }
        int bridge=0;
        for(U x:left) for(U y:right) if(pop(x^y)==2) ++bridge;
        if(bridge!=1) throw runtime_error("Bridge not unique");
        for(auto it=left.begin();it!=left.end();++it)
            for(auto jt=next(it);jt!=left.end();++jt)
                if(pop(*it^*jt)!=2) throw runtime_error("Left clique incomplete");
        for(auto it=right.begin();it!=right.end();++it)
            for(auto jt=next(it);jt!=right.end();++jt)
                if(pop(*it^*jt)!=2) throw runtime_error("Right clique incomplete");
        ++graphs; edges+=ecount;
    }
    cout<<"VERIFICATION_OK graph_cases="<<graphs<<" initial_sets_checked="<<tests
        <<" minimum_sets_found="<<good<<" reconfiguration_edges_checked="<<edges<<"\n";
}
