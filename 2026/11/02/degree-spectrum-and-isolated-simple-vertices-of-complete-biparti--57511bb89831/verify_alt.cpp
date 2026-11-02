// Independently enumerate nested row-neighborhood matrices and legal bit flips.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using namespace std;

static bool nested(uint32_t x, int a, int b) {
    uint32_t mask=(1U<<b)-1;
    for(int i=0;i<a;i++) for(int j=i+1;j<a;j++) {
        uint32_t u=(x>>(i*b))&mask;
        uint32_t v=(x>>(j*b))&mask;
        if((u&~v) && (v&~u)) return false;
    }
    return true;
}
static map<int,long long> direct(int a,int b) {
    size_t total=size_t(1)<<(a*b);
    vector<unsigned char> good(total,0);
    for(size_t x=0;x<total;x++) good[x]=nested(uint32_t(x),a,b);
    map<int,long long> h;
    for(size_t x=0;x<total;x++) if(good[x]) {
        int d=0;
        for(int k=0;k<a*b;k++) if(good[x^(size_t(1)<<k)]) d++;
        h[d]++;
    }
    return h;
}
static void check(int a,int b, initializer_list<pair<const int,long long>> expected) {
    auto got=direct(a,b);
    map<int,long long> want(expected);
    if(got!=want) {
        cerr<<"FAIL K_"<<a<<","<<b<<"\n";
        for(auto [d,c]:got)cerr<<d<<":"<<c<<" ";
        cerr<<"\n";
        throw runtime_error("wrong distribution");
    }
    long long total=0, degree_sum=0;
    for(auto [d,c]:got) {total+=c;degree_sum+=d*c;}
    cout<<"K_"<<a<<","<<b<<": "<<total<<" vertices, "<<degree_sum/2<<" flip edges\n";
}
int main(){
    check(1,4,{{4,16}});
    check(2,2,{{3,8},{4,6}});
    check(2,3,{{4,24},{5,12},{6,10}});
    check(3,3,{{5,90},{6,72},{7,36},{8,18},{9,14}});
    check(4,4,{{7,1472},{8,2304},{9,1056},{10,1248},{11,192},{12,408},{13,64},{14,96},{15,32},{16,30}});
    check(4,5,{{8,6280},{9,12720},{10,7840},{11,6920},{12,2880},{13,2640},{14,840},{15,600},{16,440},{17,120},{18,140},{19,40},{20,46}});
    cout<<"ALTERNATIVE_NESTED_MATRIX_PASS 6\n";
}
