#include <bits/stdc++.h>
using namespace std;

static bool direct_check(int N, const vector<int>& primes, const vector<int>& spf) {
    vector<int> E(N+1,0), T(N+1,0);
    for (int p: primes) {
        if (p>N) break;
        long long z=N; int e=0;
        while (z) { z/=p; e += (int)z; }
        if (p==3) --e;
        E[p]=e;
        int v=e+1;
        while (v>1) {
            int q=spf[v], c=0;
            do { v/=q; ++c; } while (v>1 && spf[v]==q);
            T[q]+=c;
        }
    }
    for (int q: primes) {
        if (q>N) break;
        if (T[q]>E[q]) return false;
    }
    return true;
}

int main(int argc, char** argv) {
    int L=100000000;
    if (argc>1) L=stoi(argv[1]);
    if (L<3) return 2;

    vector<int> spf((size_t)L+2), primes;
    primes.reserve((size_t)L/10);
    for (int i=2;i<=L+1;++i) {
        if (!spf[i]) { spf[i]=i; primes.push_back(i); }
        for (int p: primes) {
            long long v=1LL*p*i;
            if (v>L+1 || p>spf[i]) break;
            spf[(size_t)v]=p;
        }
    }

    vector<int> E((size_t)L+2), T((size_t)L+2);
    long long bad=0, checks=0;
    auto is_bad=[&](int q){ return T[q]>E[q]; };
    auto add_E=[&](int q,int d){ bool b=is_bad(q); E[q]+=d; bool a=is_bad(q); bad += (long long)a-(long long)b; };
    auto add_T=[&](int q,int d){ bool b=is_bad(q); T[q]+=d; bool a=is_bad(q); bad += (long long)a-(long long)b; };
    auto adjust_factorization=[&](int v,int sign){
        while (v>1) {
            int q=spf[v], c=0;
            do { v/=q; ++c; } while (v>1 && spf[v]==q);
            add_T(q,sign*c);
        }
    };

    // X_3=3!/3=2, so E_2=1 and tau(X_3)=2.
    add_E(2,1); add_T(2,1);
    int direct_samples=0;
    for (int N=3; N<=L; ++N) {
        if (N>3) {
            int z=N;
            while (z>1) {
                int p=spf[z], c=0;
                do { z/=p; ++c; } while (z>1 && spf[z]==p);
                int olde=E[p], newe=olde+c;
                adjust_factorization(olde+1,-1);
                adjust_factorization(newe+1,+1);
                add_E(p,c);
            }
        }
        ++checks;
        if (bad!=0) {
            cerr << "FAIL N=" << N << " bad_prime_count=" << bad << "\n";
            return 1;
        }
        if (N<=1000 || N==1234 || N==5000 || N==9999 || N==10000) {
            if (!direct_check(N,primes,spf)) {
                cerr << "DIRECT_FAIL N=" << N << "\n";
                return 1;
            }
            ++direct_samples;
        }
    }
    cout << "VERIFY_OK limit=" << L << " checks=" << checks
         << " direct_samples=" << direct_samples << "\n";
    return 0;
}
