// Standalone C++17 prefix-exhaustion check for maximal ternary curling images.
#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Pair { string w, c; };
static bool new_overlap(const string &s) {
    int n=static_cast<int>(s.size());
    for(int p=1; 2*p+1 <= n; ++p)
        if(memcmp(s.data()+n-2*p-1,s.data()+n-p-1,p+1)==0) return true;
    return false;
}
static bool square_at_end(const string &s) {
    int n=static_cast<int>(s.size());
    for(int p=1;2*p<=n;++p)
        if(memcmp(s.data()+n-2*p,s.data()+n-p,p)==0) return true;
    return false;
}
int main(){
    vector<Pair> layer = {{"0","1"}};
    map<string,int> fibers;
    for(int n=2;n<=85;++n){
        vector<Pair> next;
        for(const auto &old:layer){
            for(char symbol='0';symbol<='2';++symbol){
                string w=old.w+symbol;
                if(new_overlap(w)) continue;
                string c=old.c+(square_at_end(w)?'2':'1');
                if(new_overlap(c)) continue;
                next.push_back({std::move(w),std::move(c)});
            }
        }
        layer.swap(next);
        if(n==84){
            assert(layer.size()==2016);
            for(const auto &a:layer)++fibers[a.c];
        }
        if(n==85)assert(layer.empty());
    }
    assert(fibers.size()==2);
    vector<int> sizes;
    for(auto &kv:fibers){
        assert(kv.first.size()==84);
        sizes.push_back(kv.second);
        cout << kv.second << ' ' << kv.first << '\n';
    }
    sort(sizes.begin(),sizes.end());
    assert((sizes==vector<int>{672,1344}));
    cout << "PASS: exhaustive normalized depth 85 empty, image counts 672 and 1344\n";
}
