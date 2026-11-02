// Reproducible Schenker-sum first-six-residue census.
// Standard C++17; no external libraries or datasets.
// Compile: c++ -O2 -std=c++17 verify_schenker.cpp -o verify_schenker
// Run: ./verify_schenker
// Optional: ./verify_schenker --census > census.csv
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
using namespace std;
using u64=uint64_t;
static constexpr int CAP=2339;

// Test a_n mod p through the truncated exponential and modular inverses.
static vector<int> roots_inverse(int p){
    vector<int> inv(p); inv[1]=1;
    for(int k=2;k<p;k++) inv[k]=(p-(int)((u64)(p/k)*inv[p%k]%p))%p;
    vector<int> roots;
    for(int n=1;n<p;n++){
        u64 term=1,sum=1;
        for(int k=1;k<=n;k++){
            term=term*(u64)n%p;
            term=term*(u64)inv[k]%p;
            sum+=term; if(sum>=p) sum-=p;
        }
        if(sum==0) roots.push_back(n);
    }
    return roots;
}

// Independent representation: Horner evaluation with coefficients n!/j!.
static u64 a_mod(u64 n,u64 mod){
    u64 coef=1,poly=1;
    for(u64 j=n;j>0;j--){
        coef=coef*j%mod;
        poly=(poly*n+coef)%mod;
    }
    return poly;
}
static vector<int> roots_horner(int p){
    vector<int> roots;
    for(int n=1;n<p;n++)if(a_mod(n,p)==0)roots.push_back(n);
    return roots;
}
static u64 powmod(u64 a,u64 e,u64 mod){
    u64 v=1;
    for(;e;e>>=1,a=a*a%mod)if(e&1)v=v*a%mod;
    return v;
}
int main(int argc,char**argv){
    const bool csv=(argc==2 && string(argv[1])=="--census");
    if(argc>2 || (argc==2 && !csv))return 2;
    vector<bool> isprime(CAP+1,true);
    isprime[0]=isprime[1]=false;
    for(int i=2;i*i<=CAP;i++)if(isprime[i])for(int j=i*i;j<=CAP;j+=i)isprime[j]=false;
    array<int,7> hist{};
    int primecount=0; vector<int> first(7),endpoint;
    u64 index_tests=0,monomial_tests=0;
    if(csv)cout<<"prime,lambda,residue_roots\n";
    for(int p=3;p<=CAP;p+=2)if(isprime[p]){
        ++primecount;
        auto v=roots_inverse(p), w=roots_horner(p);
        if(v!=w){cerr<<"Independent algorithms disagree at p="<<p<<"\n";return 1;}
        int c=(int)v.size();
        if(c>6){cerr<<"Unexpected root count above six at p="<<p<<"\n";return 1;}
        ++hist[c];
        for(int j=1;j<=6;j++)if(c>=j && !first[j])first[j]=p;
        index_tests+=p-1;
        monomial_tests+=(u64)p*(p-1)/2;
        if(p<CAP && c>=6){cerr<<"Earlier six-root prime p="<<p<<"\n";return 1;}
        if(p==CAP)endpoint=v;
        if(csv){
            cout<<p<<","<<c<<",\"";
            for(size_t i=0;i<v.size();i++){if(i)cout<<";";cout<<v[i];}
            cout<<"\"\n";
        }
    }
    const vector<int> target_roots={156,470,520,589,1092,2170};
    const vector<int> target_digits={1537,434,1366,1060,878,1205};
    const vector<int> target_q_factors={843,1662,1732,24,685,1079};
    const array<int,7> target_hist={121,139,65,14,4,1,1};
    if(primecount!=345 || endpoint!=target_roots || hist!=target_hist ||
       first[6]!=CAP || index_tests!=369924 || monomial_tests!=280932418){
        cerr<<"Census or endpoint mismatch\n";return 1;
    }
    const u64 p=CAP,mod=p*p;
    for(size_t i=0;i<target_roots.size();i++){
        u64 n=target_roots[i], a=a_mod(n,mod), b=a_mod(n+p,mod);
        // The Miska nondegeneracy difference Q(n,p):
        u64 factor=powmod(n+p,n+2,mod)*powmod(n,p-n-2,mod)%mod;
        u64 q=(b+mod-a*factor%mod)%mod;
        if(q%p || q/p!=(u64)target_q_factors[i] || a%p){
            cerr<<"First-order Hensel certificate mismatch at n="<<n<<"\n";return 1;
        }
        const u64 alpha=a/p,beta=q/p;
        const u64 t=(p-(alpha*n%p)*powmod(beta,p-2,p)%p)%p;
        if(t!=(u64)target_digits[i] || a_mod(n+t*p,mod)!=0){
            cerr<<"Second-order Hensel lift mismatch at n="<<n<<"\n";return 1;
        }
    }
    ostream& summary=csv?cerr:cout;
    summary<<"VERIFY_OK odd_primes="<<primecount<<" tested_indices="<<index_tests
      <<" monomials_per_method="<<monomial_tests<<" independent_methods=2 second_level_lifts=6\n";
    summary<<"histogram_lambda_0_to_6:";for(auto x:hist)summary<<" "<<x;summary<<"\n";
    summary<<"first_primes_for_lambda_at_least_1_to_6:";
    for(int i=1;i<=6;i++)summary<<" "<<first[i];summary<<"\n";
    summary<<"p=2339 six_roots:";for(int r:endpoint)summary<<" "<<r;summary<<"\n";
    return 0;
}
