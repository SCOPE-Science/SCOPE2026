// Exhaustive checks of the finite-field idempotent law in characteristic two.
// Build: g++ -std=c++17 -O3 verify.cpp -o verify
// Run: ./verify
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int mul_table[8][8];
int size_field;

int field_product(int a, int b, int irreducible) {
    int result=0;
    while(b) {
        if(b&1) result^=a;
        b>>=1; a<<=1;
        if(a&size_field) a^=irreducible;
    }
    return result;
}
void initialize_field(int q) {
    size_field=q;
    const int poly=(q==2?3:(q==4?7:11));
    for(int a=0;a<q;a++) for(int b=0;b<q;b++)
        mul_table[a][b]=field_product(a,b,poly);
}
bool nonsingular(vector<int> a,int n) {
    int rank=0;
    for(int j=0;j<n;j++) {
        int pivot=rank;
        while(pivot<n && a[pivot*n+j]==0) pivot++;
        if(pivot==n) continue;
        for(int k=j;k<n;k++) swap(a[rank*n+k],a[pivot*n+k]);
        int inv=1;
        while(mul_table[inv][a[rank*n+j]]!=1) inv++;
        for(int k=j;k<n;k++) a[rank*n+k]=mul_table[inv][a[rank*n+k]];
        for(int row=rank+1;row<n;row++) {
            int coeff=a[row*n+j];
            for(int k=j;k<n;k++) a[row*n+k]^=mul_table[coeff][a[rank*n+k]];
        }
        rank++;
    }
    return rank==n;
}
uint64_t run(int n,int q,const map<int,uint64_t>& expected) {
    initialize_field(q);
    uint64_t ambient=1;
    for(int i=0;i<n*n;i++) ambient*=q;
    uint64_t vector_count=1;
    for(int i=0;i<n;i++) vector_count*=q;
    map<int,uint64_t> observed;
    uint64_t invertibles=0;
    for(uint64_t id=0;id<ambient;id++) {
        uint64_t z=id;
        vector<int> matrix(n*n);
        for(int j=0;j<n*n;j++) { matrix[j]=z%q; z/=q; }
        if(!nonsingular(matrix,n)) continue;
        invertibles++;
        int fixed=0;
        for(uint64_t v=0;v<vector_count;v++) {
            uint64_t w=v;
            int x[4]={},square[4]={};
            for(int j=0;j<n;j++) {
                x[j]=w%q; w/=q;
                square[j]=mul_table[x[j]][x[j]];
            }
            bool is_fixed=true;
            for(int i=0;i<n;i++) {
                int transformed=0;
                for(int j=0;j<n;j++)
                    transformed^=mul_table[matrix[i*n+j]][square[j]];
                if(transformed!=x[i]) {is_fixed=false;break;}
            }
            fixed+=is_fixed;
        }
        assert(fixed>=1 && (fixed&(fixed-1))==0);
        observed[fixed-1]++;
    }
    assert(observed==expected);
    printf("n=%d q=%d invertible=%llu histogram=",n,q,(unsigned long long)invertibles);
    for(auto const& kv:observed)
        printf("%d:%llu,",kv.first,(unsigned long long)kv.second);
    printf("\n");
    return invertibles;
}
int main() {
    uint64_t total=0;
    total+=run(2,2,{{0,2},{1,3},{3,1}});
    total+=run(2,4,{{0,60},{1,90},{3,30}});
    total+=run(2,8,{{0,1176},{1,1764},{3,588}});
    total+=run(3,2,{{0,48},{1,98},{3,21},{7,1}});
    total+=run(3,4,{{0,51840},{1,105840},{3,22680},{7,1080}});
    total+=run(4,2,{{0,5824},{1,11640},{3,2590},{7,105},{15,1}});
    assert(total==205482);
    printf("VERIFY_OK cases=6 matrices=%llu\n",(unsigned long long)total);
}
