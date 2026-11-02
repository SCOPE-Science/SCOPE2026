// Exact finite enumeration certificate for the prime--Zumkeller covering height.
// Build: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
// Uses only the C++17 standard library, with all arithmetic exact.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static bool is_zumkeller(uint32_t z){
    vector<uint32_t> divisors;
    for(uint32_t d=1;d<=z;d++) if(z%d==0)divisors.push_back(d);
    uint32_t sigma=0;
    for(uint32_t d:divisors)sigma+=d;
    if(sigma&1u || sigma<2*z)return false;
    const uint32_t target=sigma/2-z;
    vector<uint8_t> dp(target+1,0);dp[0]=1;
    for(uint32_t d:divisors){
        if(d==z || d>target)continue;
        for(uint32_t s=target;s>=d;s--){
            if(dp[s-d])dp[s]=1;
            if(s==d)break;
        }
    }
    return dp[target]!=0;
}
int main(){
    constexpr uint32_t LIMIT=1000000000U;
    constexpr uint32_t SUMMAND_BOUND=4288;
    constexpr uint32_t EXTREMAL_N=679570815;
    vector<uint32_t> summands;
    for(uint32_t z=2;z<=SUMMAND_BOUND;z+=2)if(is_zumkeller(z))summands.push_back(z);
    assert(binary_search(summands.begin(),summands.end(),SUMMAND_BOUND));
    // Odd-only Eratosthenes: bit i indicates that 2i+1 is composite.
    const uint64_t odd_count=uint64_t(LIMIT)/2+1;
    vector<uint64_t> composite((odd_count+63)/64,0);
    const auto is_composite=[&](uint64_t i)->bool{return (composite[i>>6]>>(i&63))&1ULL;};
    const auto mark=[&](uint64_t i){composite[i>>6]|=1ULL<<(i&63);};
    mark(0); // The odd integer 1 is not prime.
    for(uint64_t p=3;p*p<=LIMIT;p+=2){
        if(!is_composite(p>>1))
            for(uint64_t m=p*p;m<=LIMIT;m+=2*p)mark(m>>1);
    }
    const auto prime=[&](uint64_t p)->bool{
        return p==2 || (p>=3 && (p&1ULL) && p<=LIMIT && !is_composite(p>>1));
    };
    uint64_t checked=0, uncovered=0, attained=0, first_attained=0;
    uint32_t maximum=0;
    for(uint64_t n=39;n<=LIMIT;n+=18){
        checked++;
        uint32_t least=0;
        for(uint32_t z:summands){
            if(z>=n)break;
            if(prime(n-z)){least=z;break;}
        }
        if(!least){uncovered++;continue;}
        if(least>maximum){maximum=least;attained=1;first_attained=n;}
        else if(least==maximum)attained++;
    }
    // The only maximum is at EXTREMAL_N, with a prime difference.
    assert(checked==55555554ULL);
    assert(uncovered==0);
    assert(maximum==SUMMAND_BOUND);
    assert(attained==1);
    assert(first_attained==EXTREMAL_N);
    assert(prime(uint64_t(EXTREMAL_N)-SUMMAND_BOUND));
    // Exhaust all smaller EVEN offsets. An odd offset would leave an even
    // prime, necessarily 2, requiring the offset EXTREMAL_N-2 > 4288.
    for(uint32_t z=2;z<SUMMAND_BOUND;z+=2)
        assert(!is_zumkeller(z) || !prime(uint64_t(EXTREMAL_N)-z));
    cout<<"VERIFY_OK checked="<<checked
        <<" uncovered="<<uncovered
        <<" maximum_least_summand="<<maximum
        <<" unique_max_n="<<first_attained
        <<" extremal_prime="<<(EXTREMAL_N-SUMMAND_BOUND)
        <<" admissible_even_summands="<<summands.size()<<"\n";
}
