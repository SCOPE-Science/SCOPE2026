// Exact standalone checks for the minimum outer-independent 2-rainbow
// function counts on one-leaf cycle coronas (sunlet graphs).
// Compile: g++ -std=c++17 -O3 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <boost/multiprecision/cpp_int.hpp>
using boost::multiprecision::cpp_int;
using Matrix = std::array<std::array<cpp_int,3>,3>;
Matrix multiply(const Matrix &A, const Matrix &B) {
    Matrix C{};
    for (int i=0;i<3;i++) for (int k=0;k<3;k++)
        for (int j=0;j<3;j++) C[i][j]+=A[i][k]*B[k][j];
    return C;
}
Matrix power(Matrix A, int e) {
    Matrix R{};
    for(int i=0;i<3;i++) R[i][i]=1;
    while(e){ if(e&1) R=multiply(R,A); A=multiply(A,A); e>>=1; }
    return R;
}
cpp_int predicted_count(int n) {
    Matrix T{{ {{2,4,2}}, {{4,2,2}}, {{4,4,2}} }};
    int m=n/2;
    Matrix R=power(T,m);
    if (!(n&1)) return 2*(R[0][0]+R[1][1]+R[2][2]);
    cpp_int sum=0;
    int weights[3]={2,2,1};
    for(int i=0;i<3;i++) for(int j=0;j<3;j++) sum+=weights[i]*R[i][j];
    return n*sum;
}
std::pair<int,std::uint64_t> exhaustive_count(int n) {
    // Encodes the 2-color sets as 0,1,2,3; vertices 0..n-1
    // are cycle vertices, vertices n..2n-1 are their private leaves.
    const std::uint64_t N=std::uint64_t(1) << (4*n);
    int min_weight=2*n+1;
    std::uint64_t count=0;
    int f[16]{};
    for(std::uint64_t mask=0;mask<N;mask++) {
        int wt=0;
        for(int i=0;i<2*n;i++) {
            f[i]=int((mask>>(2*i))&3);
            wt+=__builtin_popcount(unsigned(f[i]));
        }
        if(wt>min_weight) continue;
        bool valid=true;
        for(int i=0;i<n && valid;i++) {
            int left=(i+n-1)%n, right=(i+1)%n;
            if(f[i]==0) {
                // All empty vertices must be independent; an empty
                // cycle vertex requires both colors from its neighbors.
                if(f[left]==0 || f[right]==0 || f[n+i]==0 ||
                    ((f[left]|f[right]|f[n+i])!=3)) valid=false;
            }
            if(f[n+i]==0 && f[i]!=3) valid=false;
        }
        if(!valid) continue;
        if(wt<min_weight) { min_weight=wt; count=0; }
        if(wt==min_weight) ++count;
    }
    return {min_weight,count};
}
int main(){
    std::uint64_t total=0;
    for(int n=3;n<=6;n++){
        auto actual=exhaustive_count(n);
        auto expected=predicted_count(n);
        if(actual.first != 2*n-n/2 || cpp_int(actual.second)!=expected)
            throw std::runtime_error("Exhaustive and transfer-matrix results disagree");
        total += std::uint64_t(1) << (4*n);
    }
    // Verify the reduced two-state transfer recurrence beyond the
    // exhaustive range, with exact integer arithmetic.
    cpp_int odd_previous=5, odd_current=42;
    cpp_int tr_previous=2, tr_current=8; // trace(B^0), trace(B^1)
    for(int m=1;m<=25;m++) {
        if(m>1){
            cpp_int next=8*odd_current+4*odd_previous;
            odd_previous=odd_current; odd_current=next;
            cpp_int next_trace=8*tr_current+4*tr_previous;
            tr_previous=tr_current; tr_current=next_trace;
        }
        if(predicted_count(2*m+1) != (2*m+1)*odd_current)
            throw std::runtime_error("Odd-cycle recurrence disagreement");
        cpp_int negtwo=1;
        for(int i=0;i<m;i++) negtwo*=(-2);
        if(2*m>=3 && predicted_count(2*m) != 2*(tr_current+negtwo))
            throw std::runtime_error("Even-cycle recurrence disagreement");
    }
    std::cout<<"VERIFICATION_OK n=3..6 exhaustive_labelings="<<total
             <<" matrix_profiles=3..51\n";
    std::cout<<"Counts n=3: "<<predicted_count(3)
             <<"; n=4: "<<predicted_count(4)
             <<"; n=5: "<<predicted_count(5)
             <<"; n=6: "<<predicted_count(6)
             <<"; n=7: "<<predicted_count(7)
             <<"; n=8: "<<predicted_count(8)<<"\n";
}
