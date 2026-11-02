// Independent exact enumeration using binary-vector lines and upper/lower toggles.
// C++17: g++ -std=c++17 -O2 -Wall -Wextra verify_fano_alt.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
int pc(int x){return __builtin_popcount((unsigned)x);}
int main(){
    set<int> line_set;
    // Each line consists of p,q,p XOR q in F_2^3, with p != q nonzero.
    for(int p=1;p<=7;p++)for(int q=p+1;q<=7;q++){
        int r=p^q;
        line_set.insert((1<<(p-1))|(1<<(q-1))|(1<<(r-1)));
    }
    vector<int> line(line_set.begin(),line_set.end());
    assert(line.size()==7);
    for(int a:line) assert(pc(a)==3);
    auto ideal=[&](int x){
        int p=x&127,l=x>>7;
        for(int k=0;k<7;k++)if((l>>k)&1)if((p&line[k])!=line[k])return false;
        return true;
    };
    // Distinct construction of rowmotion: upper toggles followed by lower toggles.
    auto successor=[&](int x){
        for(int k=0;k<7;k++){
            int t=1<<(7+k);
            if(x&t)x^=t;
            else if((x&line[k])==line[k])x^=t;
        }
        for(int i=0;i<7;i++){
            int t=1<<i;
            if(!(x&t)){x^=t;continue;}
            bool blocked=false;
            for(int k=0;k<7;k++)if((x>>(7+k)&1) && (line[k]&t))blocked=true;
            if(!blocked)x^=t;
        }
        assert(ideal(x));
        return x;
    };
    set<int> states;
    for(int x=0;x<(1<<14);x++)if(ideal(x))states.insert(x);
    assert(states.size()==458);
    set<int> seen;map<int,int> counts;map<pair<int,int>,int> size_sums;
    for(int x:states){
        if(seen.count(x))continue;
        int y=x, len=0, weight=0;
        do{
            assert(states.count(y) && !seen.count(y));
            seen.insert(y);len++;weight+=pc(y);
            y=successor(y);
        }while(y!=x);
        counts[len]++; size_sums[{len,weight}]++;
    }
    assert(seen==states);
    assert((counts==map<int,int>{{3,29},{5,35},{7,28}}));
    assert((size_sums==map<pair<int,int>,int>{{{3,18},14},{{3,21},1},{{3,24},14},{{5,32},7},{{5,35},21},{{5,38},7},{{7,49},28}}));
    cout<<"INDEPENDENT_VERIFY_OK states="<<states.size()<<" orbit_counts=3:29,5:35,7:28 order=105\n";
}
