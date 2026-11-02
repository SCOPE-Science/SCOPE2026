// Exact independent labeled-word enumeration. C++17, standard library only.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;
static bool forbidden_94_at_end(const string& s) {
    const int n = (int)s.size();
    for (int p=1; 9*p <= 4*n; ++p) {
        int length=(9*p+3)/4;
        if (length>n) continue;
        bool periodic=true;
        for (int i=n-length; i<n-p; ++i) {
            if (s[i] != s[i+p]) { periodic=false; break; }
        }
        if (periodic) return true;
    }
    return false;
}
static bool forbidden_overlap_at_end(const string& s) {
    const int n=(int)s.size();
    for(int p=1; 2*p+1<=n; ++p) {
        bool periodic=true;
        for(int i=n-2*p-1;i<n-p;++i) {
            if(s[i]!=s[i+p]) {periodic=false;break;}
        }
        if(periodic) return true;
    }
    return false;
}
static char direct_last_curl(const string& s) {
    int n=(int)s.size();
    for(int p=1;2*p<=n;++p) {
        bool squared=true;
        for(int i=n-p;i<n;++i) {
            if(s[i]!=s[i-p]) {squared=false;break;}
        }
        if(squared) return '2';
    }
    return '1';
}
static pair<int,int> max_exponent(const string& s) {
    int best_n=1, best_d=1;
    for(int p=1;2*p<=(int)s.size();++p) {
        int run=0;
        for(int j=0;j+p<(int)s.size();++j) {
            run = s[j]==s[j+p] ? run+1 : 0;
            if(run>=p && (p+run)*best_d > best_n*p) {
                best_n=p+run;best_d=p;
            }
        }
    }
    return {best_n,best_d};
}
int main() {
    vector<pair<string,string>> level(1,{"",""});
    const string A="112112212112122112212112211212211221211212212112211212211221211221121221211212211211";
    const string B="112112212112122112212112211212211221211212212112211212211221211221121221211212211212";
    assert(A.size()==84 && B.size()==84);
    map<pair<int,string>,int> tally;
    for(int n=1;n<=85;++n) {
        vector<pair<string,string>> next;
        for(const auto& row:level) for(char digit='0';digit<='2';++digit) {
            string w=row.first+digit;
            if(forbidden_94_at_end(w)) continue;
            string t=row.second+direct_last_curl(w);
            if(forbidden_overlap_at_end(t)) continue;
            next.emplace_back(move(w),move(t));
        }
        level.swap(next);
        if(n==84) {
            assert(level.size()==10368);
            for(const auto &row:level) {
                const auto& w=row.first;const auto& t=row.second;
                assert(t==A || t==B);
                const auto [num,den]=max_exponent(w);
                int category;
                if(num==2*den) category=2;
                else {assert(num*5==den*11);category=11;}
                ++tally[{category,t}];
                // Independently reconstruct the direct-prefix transform.
                for(int j=1;j<=84;++j) {
                    assert(direct_last_curl(w.substr(0,j))==t[j-1]);
                }
            }
        }
        if(n==85) assert(level.empty());
    }
    assert(tally[make_pair(2,A)]==4032);
    assert(tally[make_pair(2,B)]==2016);
    assert(tally[make_pair(11,A)]==2880);
    assert(tally[make_pair(11,B)]==1440);
    assert(tally.size()==4);
    cout<<"labeled terminal 10368; critical exponents 2:6048, 11/5:4320; transforms 2\n";
    cout<<"full stratified tally 4032 2016 2880 1440\n";
    cout<<"POWER94_CURLING_LABELED_VERIFY_OK\n";
}
