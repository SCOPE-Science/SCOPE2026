// Exact exhaustive census for distinct consecutive sums of increasing subsets of [N].
// Compile: g++ -O3 -std=c++17 verify_interval.cpp -o verify_interval
// Run: ./verify_interval
#include <cstdint>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>

static int naive_count(uint32_t mask, int N) {
    int s[25], k=0, p=0; s[0]=0;
    for (int i=0; i<N; ++i) if (mask & (1u<<i)) s[++k]=(p+=i+1);
    const int cap=N*(N+1)/2;
    bool seen[301]={}; int answer=0;
    for(int j=1; j<=k; ++j) for(int i=0;i<j;++i) {
        int d=s[j]-s[i];
        if(d<1 || d>cap) std::abort();
        if(!seen[d]){seen[d]=true;++answer;}
    }
    return answer;
}

int main(){
    static const int expected[25]={0,1,3,5,9,12,16,21,27,33,40,47,55,63,70,77,89,101,110,123,134,146,159,171,188};
    static const int full_expected_24=186;
    unsigned long long tested=0;
    for(int N=1;N<=24;++N) {
        const int cap=N*(N+1)/2;
        std::vector<uint32_t> seen(cap+1,0);
        int maxval=0, fullval=-1; uint32_t maximizer=0; unsigned long long count=0;
        const uint32_t total=1u<<N;
        for(uint32_t mask=1;mask<total;++mask){
            int p[25],length=0,psum=0;p[0]=0;
            for(int i=0;i<N;++i) if(mask & (1u<<i)) p[++length]=(psum+=i+1);
            int distinct=0;
            for(int j=1;j<=length;++j)for(int i=0;i<j;++i){
                const int difference=p[j]-p[i];
                if(seen[difference]!=mask){seen[difference]=mask;++distinct;}
            }
            if(distinct>maxval){maxval=distinct;maximizer=mask;count=1;}
            else if(distinct==maxval)++count;
            if(mask==total-1)fullval=distinct;
            if(N<=17 && (mask==1 || mask==(total-1) || (mask%17==3)) && distinct!=naive_count(mask,N)) std::abort();
            ++tested;
        }
        if(maxval!=expected[N]) std::abort();
        if(N<24 && maxval!=fullval) std::abort();
        if(N==24 && (maxval!=188 || fullval!=full_expected_24 || count!=1 || maximizer!=(total-1-(1u<<10)))) std::abort();
        std::printf("n=%d maximum=%d full=%d maximizers=%llu\n",N,maxval,fullval,count);
    }
    std::printf("VERIFY_OK masks=%llu first_strict_improvement_n=24 maximum=188 full=186 unique_omitted=11\n",tested);
    return 0;
}
