// Exhaustive modular certificate for the first prime with six Schenker roots.
// Build: c++ -std=c++17 -O2 verify_minimum.cpp -o verify_minimum
// Run: ./verify_minimum
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

// For r>=1, this computes a_r = r! sum_{j=0}^r r^j/j! (mod p).
// The loop invariant is b=j! sum_{i=0}^j r^i/i! and power=r^j mod p.
static int schenker_mod(int r,int p){
    long long b=1,power=1;
    for(int j=1;j<=r;++j){power=power*r%p; b=(j*b+power)%p;}
    return int(b);
}
int main(){
    constexpr int N=2339;
    vector<unsigned char> prime(N+1,1);prime[0]=prime[1]=0;
    for(int d=2;d*d<=N;++d)if(prime[d])for(int k=d*d;k<=N;k+=d)prime[k]=0;
    if(!prime[N])return 2;
    int max_prior=0,first_five=0,num_below=0; vector<int> rootsN;array<int,7> hist{};
    for(int p=2;p<=N;++p)if(prime[p]){
        vector<int> roots;
        for(int r=1;r<p;++r)if(schenker_mod(r,p)==0)roots.push_back(r);
        int count=int(roots.size());
        if(p<N){++num_below;max_prior=max(max_prior,count);if(count==5&&!first_five)first_five=p;
            if(count>=6){cerr<<"Unexpected earlier six-root prime: "<<p<<"\n";return 3;}
            ++hist[count];}
        else rootsN=roots;
    }
    const vector<int> expected={156,470,520,589,1092,2170};
    const array<int,7> expected_hist={121,140,65,14,4,1,0};
    if(rootsN!=expected || max_prior!=5 || first_five!=593 || num_below!=345 || hist!=expected_hist){
        cerr<<"Certificate mismatch\n";return 4;
    }
    cout<<"earliest_prime_with_lambda_ge_6="<<N<<"\n";
    cout<<"lambda_2339="<<rootsN.size()<<"\nroots:";
    for(int x:rootsN)cout<<" "<<x;
    cout<<"\nprimes_checked_below="<<num_below<<"\nmax_prior="<<max_prior;
    cout<<"\nfirst_prime_with_lambda_5="<<first_five<<"\n";
    cout<<"lambda_histogram_below_2339:";
    for(int i=0;i<6;++i)cout<<" "<<i<<":"<<hist[i];
    cout<<"\nVERIFY_OK\n";
}
