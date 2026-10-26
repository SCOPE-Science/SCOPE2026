// Reproducible exhaustive checks for sequential three-site OR dynamics on cycles.
// Build: c++ -std=c++17 -O2 verify.cpp -o verify
// Run:   ./verify
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>
using std::vector;

static uint32_t sweep(uint32_t x, int n, const vector<int>& order) {
    for (int i : order) {
        int left = (i+n-1)%n, right = (i+1)%n;
        if ((x & (uint32_t(1)<<left)) || (x & (uint32_t(1)<<right)))
            x |= uint32_t(1)<<i;
    }
    return x;
}
static int arrival(uint32_t x, int n, const vector<int>& order) {
    const uint32_t full = (uint32_t(1)<<n)-1;
    int t=0;
    while(x && x!=full && t<=n) { x=sweep(x,n,order); ++t; }
    if (x && x!=full) throw std::runtime_error("failed to converge");
    return t;
}
static int witness_count(int n, const vector<int>& rank) {
    if(n%2) return 0;
    int m=n/2, count=0;
    for(int s=0;s<n;++s) {
        bool good=true;
        for(int d=1;d<m;++d) {
            if(rank[(s+d)%n] <=rank[(s+d+1)%n]) good=false;
            if(rank[(s-d+n)%n] <=rank[(s-d-1+n)%n]) good=false;
        }
        count+=good;
    }
    return count;
}
static uint64_t choose(int n,int k) {
    uint64_t r=1;
    for(int j=1;j<=k;++j) r=r*(n-j+1)/j;
    return r;
}
int main() {
    uint64_t perms=0,singleton_trials=0,full_state_trials=0;
    for(int n=3;n<=10;++n) {
        vector<int> order(n);
        std::iota(order.begin(),order.end(),0);
        uint64_t tested=0, slow=0, multiple=0;
        int largest=0;
        do {
            vector<int> rank(n);
            for(int j=0;j<n;++j) rank[order[j]]=j;
            int worst=0;
            for(int s=0;s<n;++s) {
                worst=std::max(worst,arrival(uint32_t(1)<<s,n,order));
                ++singleton_trials;
            }
            if (worst>n/2) throw std::runtime_error("diameter bound violated");
            largest=std::max(largest,worst);
            if(n%2==0) {
                int w=witness_count(n,rank);
                if ((worst==n/2)!=(w>0)) throw std::runtime_error("witness equivalence violated");
                if(n>=6 && w>1) throw std::runtime_error("antipodal witness not unique");
                if(w>1)++multiple;
                if(worst==n/2)++slow;
            }
            if(n<=7) {
                for(uint32_t state=0;state<(uint32_t(1)<<n);++state) {
                    int t=arrival(state,n,order);
                    if(t>worst) throw std::runtime_error("singleton reduction violated");
                    ++full_state_trials;
                }
            }
            ++tested;
        } while(std::next_permutation(order.begin(),order.end()));
        if(largest!=n/2) throw std::runtime_error("worst time not sharp");
        if(n%2==0) {
            uint64_t expected=(n==4) ? 24 : uint64_t(n)*n*choose(n-2,n/2-1);
            if(slow!=expected) throw std::runtime_error("extremal count incorrect");
            if(n==4 && multiple!=8) throw std::runtime_error("small cycle exception incorrect");
            std::cout << "n="<<n<<" permutations="<<tested<<" slow="<<slow
                      <<" multiple_witness="<<multiple<<"\n";
        } else {
            std::cout << "n="<<n<<" permutations="<<tested<<" sharp_bound="<<largest<<"\n";
        }
        perms+=tested;
    }
    std::cout << "VERIFY_OK permutations="<<perms
              <<" singleton_tests="<<singleton_trials
              <<" all_state_tests="<<full_state_trials<<"\n";
}
