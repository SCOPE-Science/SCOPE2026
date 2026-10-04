#include <bits/stdc++.h>
using namespace std;

struct Solver {
    static constexpr int n = 5;
    static constexpr int k = 2;
    int q, N = 16, root = 15;
    vector<uint32_t> adj;
    vector<vector<int>> autos;
    unordered_map<unsigned long long, uint8_t> memo;
    long long nodes = 0;

    explicit Solver(int q_) : q(q_) { build(); memo.reserve(1 << 24); }
    int vid(int layer, int i) const { return layer * n + i; }
    void add(int u, int v) { adj[u] |= 1u << v; adj[v] |= 1u << u; }

    void build() {
        adj.assign(N, 0);
        for (int i = 0; i < n; ++i) {
            int j = (i + 1) % n;
            add(vid(0, i), vid(0, j));
        }
        for (int layer = 0; layer < k; ++layer) {
            for (int i = 0; i < n; ++i) {
                int j = (i + 1) % n;
                add(vid(layer, i), vid(layer + 1, j));
                add(vid(layer, j), vid(layer + 1, i));
            }
        }
        for (int i = 0; i < n; ++i) add(root, vid(k, i));

        for (int r = 0; r < n; ++r) for (int refl = 0; refl < 2; ++refl) {
            vector<int> p(N);
            for (int layer = 0; layer <= k; ++layer) for (int i = 0; i < n; ++i) {
                int j = refl ? ((r - i) % n + n) % n : (r + i) % n;
                p[vid(layer, i)] = vid(layer, j);
            }
            p[root] = root;
            autos.push_back(p);
        }
    }

    unsigned long long encode(const vector<uint8_t>& a) const {
        unsigned long long x = 0;
        for (int i = N - 1; i >= 0; --i) x = (x << 3) | a[i];
        return x;
    }

    unsigned long long canon(const vector<uint8_t>& a) const {
        unsigned long long best = ULLONG_MAX;
        vector<uint8_t> b(N);
        for (const auto& p : autos) {
            array<uint8_t, 5> mp{};
            uint8_t nxt = 1;
            fill(b.begin(), b.end(), 0);
            for (int i = 0; i < N; ++i) if (a[i]) b[p[i]] = a[i];
            for (int i = 0; i < N; ++i) if (b[i]) {
                if (!mp[b[i]]) mp[b[i]] = nxt++;
                b[i] = mp[b[i]];
            }
            best = min(best, encode(b));
        }
        return best;
    }

    void decode(unsigned long long code, vector<uint8_t>& a) const {
        for (int i = 0; i < N; ++i) { a[i] = code & 7; code >>= 3; }
    }

    bool blocked(const vector<uint8_t>& a) const {
        for (int v = 0; v < N; ++v) if (!a[v]) {
            int mask = 0;
            uint32_t nb = adj[v];
            while (nb) {
                int u = __builtin_ctz(nb); nb &= nb - 1;
                if (a[u]) mask |= 1 << (a[u] - 1);
            }
            if (mask == (1 << q) - 1) return true;
        }
        return false;
    }

    bool full(const vector<uint8_t>& a) const {
        for (auto c : a) if (!c) return false;
        return true;
    }

    struct Move { int v, c, score; };

    bool win_code(unsigned long long code) {
        auto it = memo.find(code);
        if (it != memo.end()) return it->second == 2;
        ++nodes;
        vector<uint8_t> a(N); decode(code, a);
        if (full(a)) { memo[code] = 2; return true; }
        if (blocked(a)) { memo[code] = 1; return false; }

        int colored = 0; for (auto c : a) colored += c != 0;
        bool alice = (colored % 2 == 0);
        vector<Move> mv;
        for (int v = 0; v < N; ++v) if (!a[v]) {
            int used = 0;
            uint32_t nb = adj[v];
            while (nb) {
                int u = __builtin_ctz(nb); nb &= nb - 1;
                if (a[u]) used |= 1 << (a[u] - 1);
            }
            for (int c = 1; c <= q; ++c) if (!(used & (1 << (c - 1)))) {
                a[v] = c;
                int sc = 0;
                for (int w = 0; w < N; ++w) if (!a[w] && (adj[w] & (1u << v))) {
                    int mm = 0; uint32_t nb2 = adj[w];
                    while (nb2) {
                        int u = __builtin_ctz(nb2); nb2 &= nb2 - 1;
                        if (a[u]) mm |= 1 << (a[u] - 1);
                    }
                    sc = max(sc, __builtin_popcount((unsigned)mm));
                }
                a[v] = 0;
                mv.push_back({v, c, sc});
            }
        }
        if (alice) sort(mv.begin(), mv.end(), [](const Move& A, const Move& B){ return A.score < B.score; });
        else sort(mv.begin(), mv.end(), [](const Move& A, const Move& B){ return A.score > B.score; });

        unordered_set<unsigned long long> seen;
        seen.reserve(mv.size() * 2 + 1);
        if (alice) {
            for (auto m : mv) {
                a[m.v] = m.c; auto ns = canon(a); a[m.v] = 0;
                if (!seen.insert(ns).second) continue;
                if (win_code(ns)) { memo[code] = 2; return true; }
            }
            memo[code] = 1; return false;
        }
        for (auto m : mv) {
            a[m.v] = m.c; auto ns = canon(a); a[m.v] = 0;
            if (!seen.insert(ns).second) continue;
            if (!win_code(ns)) { memo[code] = 1; return false; }
        }
        memo[code] = 2; return true;
    }

    bool run() { vector<uint8_t> a(N, 0); return win_code(canon(a)); }

    void verify_structure() const {
        long long degsum = 0;
        for (auto x : adj) degsum += __builtin_popcount(x);
        if (degsum / 2 != 30) throw runtime_error("edge-count mismatch");
        if ((int)autos.size() != 10) throw runtime_error("automorphism-count mismatch");
        for (const auto& p : autos) for (int u = 0; u < N; ++u) for (int v = 0; v < N; ++v) {
            bool e1 = (adj[u] >> v) & 1u;
            bool e2 = (adj[p[u]] >> p[v]) & 1u;
            if (e1 != e2) throw runtime_error("invalid symmetry quotient");
        }
    }
};

int main() {
    Solver s3(3); s3.verify_structure(); bool w3 = s3.run();
    Solver s4(4); s4.verify_structure(); bool w4 = s4.run();
    cout << "M2(C5), q=3: Alice_win=" << (w3 ? 1 : 0) << ", canonical_states=" << s3.nodes << "\n";
    cout << "M2(C5), q=4: Alice_win=" << (w4 ? 1 : 0) << ", canonical_states=" << s4.nodes << "\n";
    if (w3 || !w4) return 1;
    cout << "ALL CHECKS PASSED\n";
    return 0;
}
