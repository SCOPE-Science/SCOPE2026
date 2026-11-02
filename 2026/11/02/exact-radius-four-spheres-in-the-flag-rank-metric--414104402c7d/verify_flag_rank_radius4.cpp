// Reproducible finite checks of the flag-rank radius-four sphere formula.
// Uses only C++17 and exact finite-field arithmetic; no external dependencies.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

static int n, q;
static int a[7][7];
static vector<pair<int,int>> positions;

static int field_mul(int x, int y) {
    if(q != 4) return x*y % q;
    // GF(4) = GF(2)[z]/(z^2+z+1), bit representation 0,1,z,z+1.
    int t=0;
    if(y&1) t ^= x;
    if(y&2) t ^= (x<<1);
    if(t&4) t ^= 7;
    return t;
}
static int field_sub(int x, int y) {
    if(q == 4) return x^y;
    return (x-y+q)%q;
}
static int field_inverse(int x) {
    for(int y=1; y<q; y++) if(field_mul(x,y)==1) return y;
    throw runtime_error("zero division");
}
static int crossing_rank(int i) {
    int b[7][7] = {};
    int rows=i+1, cols=n-i, rank=0;
    for(int r=0;r<rows;r++) for(int c=i;c<n;c++) b[r][c-i]=a[r][c];
    for(int c=0;c<cols;c++) {
        int pivot=rank;
        while(pivot<rows && !b[pivot][c]) pivot++;
        if(pivot==rows) continue;
        for(int j=c;j<cols;j++) swap(b[pivot][j],b[rank][j]);
        int inv=field_inverse(b[rank][c]);
        for(int j=c;j<cols;j++) b[rank][j]=field_mul(b[rank][j],inv);
        for(int r=rank+1;r<rows;r++) if(b[r][c]) {
            int factor=b[r][c];
            for(int j=c;j<cols;j++)
                b[r][j]=field_sub(b[r][j],field_mul(factor,b[rank][j]));
        }
        rank++;
        if(rank==rows) break;
    }
    return rank;
}
static long long binom(int nn,int k) {
    if(k<0||k>nn)return 0;
    long long r=1;
    for(int j=1;j<=k;j++) r=r*(nn-j+1)/j;
    return r;
}
static array<long long,6> expectation() {
    long long v=q-1, Q=q;
    return {
        binom(n,4)*v*v*v*v,
        (n-1)*binom(n-2,2)*Q*Q*v*v*v,
        binom(n-2,2)*Q*Q*Q*Q*v*v,
        (n-2)*(n-3)*Q*Q*Q*Q*v*v,
        (n-3)*Q*Q*Q*Q*Q*Q*v,
        (n-2)*Q*Q*(Q*Q-1)*(Q*Q-Q)
    };
}
static void verify(int dim,int size) {
    n=dim;q=size;positions.clear();
    for(int i=0;i<n;i++) for(int j=i;j<n;j++) positions.push_back({i,j});
    long long number=1;
    for(size_t j=0;j<positions.size();j++) number*=q;
    array<long long,6> actual={};
    for(long long id=0; id<number; id++) {
        long long value=id;
        for(auto [i,j]: positions) { a[i][j]=value%q;value/=q; }
        int weight=0, largest_rank=0;
        for(int i=0;i<n;i++) {
            int r=crossing_rank(i);
            weight+=r;
            largest_rank=max(largest_rank,r);
            if(weight>4) break;
        }
        if(weight != 4) continue;
        int max_band=0, first_super=0;
        for(auto [i,j]:positions) if(a[i][j]) {
            max_band=max(max_band,j-i);
            if(j-i==1) first_super++;
        }
        int type;
        if(largest_rank==2) type=5;
        else if(largest_rank>2) throw runtime_error("unexpected rank profile");
        else if(max_band==0) type=0;
        else if(max_band==1 && first_super==1) type=1;
        else if(max_band==1 && first_super==2) type=2;
        else if(max_band==2) type=3;
        else if(max_band==3) type=4;
        else throw runtime_error("unclassified radius-four matrix");
        actual[type]++;
    }
    auto target=expectation();
    if(actual!=target) {
        cerr<<"mismatch at n="<<n<<" q="<<q<<"\n";
        for(int j=0;j<6;j++)cerr<<j<<" actual="<<actual[j]<<" expected="<<target[j]<<"\n";
        throw runtime_error("sphere census mismatch");
    }
    long long total=0;
    for(auto x:actual)total+=x;
    cout<<"n="<<n<<" q="<<q<<" s4="<<total<<" six_categories=";
    for(int j=0;j<6;j++)cout<<(j?",":"")<<actual[j];
    cout<<" PASS\n";
}
int main() {
    verify(3,2);verify(4,2);verify(5,2);verify(6,2);
    verify(3,3);verify(4,3);
    verify(3,4);verify(4,4);
    cout<<"FLAG_RANK_RADIUS_FOUR_EXACT_CHECK_OK\n";
}
