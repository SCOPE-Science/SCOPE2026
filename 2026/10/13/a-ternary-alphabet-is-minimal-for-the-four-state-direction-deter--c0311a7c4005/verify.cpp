#include <bits/stdc++.h>
using namespace std;

struct Tr { signed char to, dir; };
static Tr M[625][4];

static int ipow(int a, int b) {
    int r = 1;
    while (b--) r *= a;
    return r;
}

// For a fixed split |Q+|=k, input-letter transitions have exactly five choices
// at each source state: undefined, one of k right targets, or one of 4-k left targets.
static void build_maps(int k) {
    for (int code=0; code<625; ++code) {
        int z=code;
        for (int q=0; q<4; ++q) {
            int d=z%5; z/=5;
            if (d==0) M[code][q] = {-1,0};
            else if (d<=k) M[code][q] = {(signed char)(d-1),+1};
            else M[code][q] = {(signed char)(k+d-k-1),-1};
        }
    }
}

// Exact deterministic simulation. Position -1 is the left end-marker,
// positions 0..n-1 are input symbols, and n is the right end-marker.
// The initial left-endmarker entrance is normalized to state 0 in Q+.
// lcode independently specifies later returns from Q- at the left marker;
// this is a deliberate superset of actual automata and therefore is safe
// for the binary upper bound.
static bool accepts_binary(int bits, int n, int ia, int ib, int k,
                           int lcode, int rcode, int fin) {
    int l=4-k, q=0, pos=0;
    uint32_t seen=0;
    for (int step=0; step<64; ++step) {
        if (pos==n) {
            if (q==fin) return true;
            if (q<0 || q>=k) return false;
            int z=rcode, base=l+1;
            for (int i=0;i<q;i++) z/=base;
            int opt=z%base;
            if (opt==0) return false;
            q=k+opt-1; --pos;
            continue;
        }
        if (pos<0) {
            if (q<k) return false;
            int z=lcode, base=k+1;
            for (int i=k;i<q;i++) z/=base;
            int opt=z%base;
            if (opt==0) return false;
            q=opt-1; ++pos;
            continue;
        }
        int idx=(pos+1)*4+q;
        uint32_t bit=1u<<idx;
        if (seen&bit) return false;
        seen|=bit;
        int sym=(bits>>(n-1-pos))&1;
        Tr t=(sym?M[ib][q]:M[ia][q]);
        if (t.to<0) return false;
        q=t.to; pos+=t.dir;
    }
    return false;
}

static string word_of(int bits, int n) {
    string s;
    for (int p=0;p<n;p++) s.push_back(char('a'+((bits>>(n-1-p))&1)));
    return s;
}

struct SplitResult {
    int maximum=-1;
    long long configurations=0;
};

// State relabeling inside Q+ lets us fix the initial entered state to 0.
// With that fixed, a singleton accepting state has only two symmetry types:
// state 0 itself, or state 1 (when k>1).
static SplitResult exhaust_binary_split(int k) {
    int l=4-k;
    build_maps(k);
    int LB=ipow(k+1,l), RB=ipow(l+1,k);
    SplitResult out;
    vector<int> finals={0};
    if (k>1) finals.push_back(1);

    for (int ia=0;ia<625;ia++)
    for (int ib=0;ib<625;ib++)
    for (int lc=0;lc<LB;lc++)
    for (int rc=0;rc<RB;rc++)
    for (int fin:finals) {
        ++out.configurations;
        int d=-1;
        for (int n=0;n<=5 && d<0;n++) {
            for (int bits=0;bits<(1<<n);bits++) {
                if (accepts_binary(bits,n,ia,ib,k,lc,rc,fin)) {
                    d=n; break;
                }
            }
        }
        out.maximum=max(out.maximum,d);
        if (d>=5) {
            cerr<<"unexpected binary length-5 witness in split "<<k<<","<<l<<"\n";
            exit(2);
        }
    }
    return out;
}

struct WTr { int to, dir; bool def; };

static bool accepts_witness(const string& w,
                            const array<array<WTr,4>,3>& T,
                            int alphabet_size, int start, int fin) {
    int n=(int)w.size(), pos=0, q=start;
    set<pair<int,int>> seen;
    for (int step=0;step<128;step++) {
        if (pos==n) return q==fin;
        if (pos<0) return false;
        if (!seen.insert({q,pos}).second) return false;
        int a=w[pos]-'a';
        if (a<0 || a>=alphabet_size) return false;
        WTr t=T[a][q];
        if (!t.def) return false;
        q=t.to; pos+=t.dir;
    }
    return false;
}

int main() {
    vector<int> got;
    long long total=0;
    for (int k=1;k<=4;k++) {
        SplitResult r=exhaust_binary_split(k);
        got.push_back(r.maximum);
        total+=r.configurations;
    }
    vector<int> expected={0,3,4,3};
    if (got!=expected) return 3;

    // Independent direct check of a binary length-4 witness.
    array<array<WTr,4>,3> B{};
    for (auto& row:B) for (auto& t:row) t={-1,0,false};
    B[0] = array<WTr,4>{WTr{2,+1,true},WTr{1,+1,true},WTr{3,-1,true},WTr{-1,0,false}};
    B[1] = array<WTr,4>{WTr{3,-1,true},WTr{2,+1,true},WTr{0,+1,true},WTr{1,+1,true}};
    for (int n=0;n<4;n++) {
        for (int bits=0;bits<(1<<n);bits++) {
            if (accepts_witness(word_of(bits,n),B,2,0,1)) return 4;
        }
    }
    if (!accepts_witness("abba",B,2,0,1)) return 5;

    // Ternary witness for the published unrestricted maximum 5.
    array<array<WTr,4>,3> T{};
    for (auto& row:T) for (auto& t:row) t={-1,0,false};
    T[0] = array<WTr,4>{WTr{0,+1,true},WTr{-1,0,false},WTr{2,+1,true},WTr{1,+1,true}};
    T[1] = array<WTr,4>{WTr{3,-1,true},WTr{0,+1,true},WTr{2,+1,true},WTr{2,+1,true}};
    T[2] = array<WTr,4>{WTr{-1,0,false},WTr{1,+1,true},WTr{3,-1,true},WTr{-1,0,false}};
    for (int n=0;n<5;n++) {
        int N=1;
        for (int i=0;i<n;i++) N*=3;
        for (int code=0;code<N;code++) {
            int z=code; string w(n,'a');
            for (int i=n-1;i>=0;i--) { w[i]=char('a'+z%3); z/=3; }
            if (accepts_witness(w,T,3,0,1)) return 6;
        }
    }
    if (!accepts_witness("abbac",T,3,0,1)) return 7;

    cout<<"VERIFY_OK binary_max=4 split_maxima=0,3,4,3 "
        <<"ternary_witness_shortest=5 unrestricted_published_max=5 "
        <<"minimum_extremal_alphabet=3 binary_search_configurations="<<total<<"\n";
    return 0;
}
