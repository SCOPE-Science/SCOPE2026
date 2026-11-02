// Independent finite normal-form checker for radius-two Hamming balls.
// Compile: c++ -std=c++17 -O2 verify_normal_forms.cpp -o verify_normal_forms
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
long long valid = 0;
int maximum = 0;
array<int,5> capacity_left{2,2,2,2,2};
vector<int> columns;

void check_current() {
    int m=int(columns.size());
    array<int,5> row{};
    for (int j=0;j<m;++j) for(int i=0;i<5;++i)
        if(columns[j]&(1<<i)) row[i]|=1<<j;
    for(int i=0;i<5;++i)for(int k=0;k<i;++k)
        if(row[i]==row[k])return;
    ++valid;
    array<bool,32> seen{};
    for(int s=0;s<(1<<m);++s) {
        int w=__builtin_popcount((unsigned)s);
        for(int outside=0;outside<=2;++outside) {
            if(w+outside>4)continue;
            int response=0;
            for(int i=0;i<5;++i) {
                int inter=__builtin_popcount((unsigned)(s&row[i]));
                int distance=__builtin_popcount((unsigned)row[i])+w-2*inter+outside;
                if(distance<=2) response|=1<<i;
            }
            seen[response]=true;
        }
    }
    int distinct=0;
    for(int j=1;j<32;++j)if(seen[j])++distinct;
    maximum=max(maximum,distinct);
    if(distinct==31){cerr<<"FIVE SHATTERED — INVALID\n";exit(2);}
}

void recurse(int first) {
    check_current();
    for(int p=first;p<32;++p) {
        bool allowed=true;
        for(int i=0;i<5;++i) if((p&(1<<i)) && capacity_left[i]==0) allowed=false;
        if(!allowed)continue;
        for(int i=0;i<5;++i) if(p&(1<<i))--capacity_left[i];
        columns.push_back(p);
        recurse(p);
        columns.pop_back();
        for(int i=0;i<5;++i) if(p&(1<<i))++capacity_left[i];
    }
}

int main() {
    recurse(1);
    assert(valid==7260);
    assert(maximum==26);
    cout<<"INDEPENDENT_INCIDENCE_ENUM_PASS "<<valid<<" max_nonzero_patterns "<<maximum<<"\n";
}
