// Independent string-based enumeration with exact monotone admissibility pruning.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

bool primitive(const string& s) {
    for(int t = 1; t < 6; ++t)
        if((s+s).substr(t, 6) == s) return false;
    return true;
}
int hamming(const string& a, const string& b) {
    int count = 0;
    for(int i = 0; i < 6; ++i) count += (a[i] != b[i]);
    return count;
}
bool permissible(const vector<string>& existing, const string& added) {
    for(const auto& s : existing)
        if(hamming(s, added) < 3) return false;
    vector<string> all = existing;
    all.push_back(added);
    set<string> words(all.begin(), all.end());
    for(const auto& left : all)
        for(const auto& right : all)
            for(int cut = 1; cut < 6; ++cut)
                if(words.count(left.substr(cut) + right.substr(0, cut))) return false;
    return true;
}
string bitword(int val) {
    string s(6,'0');
    for(int i = 5; i >= 0; --i) { s[i] = char('0' + (val&1)); val >>= 1; }
    return s;
}
vector<string> candidates;
map<int,int> levels;
set<vector<string>> optimizers;
void enumerate(vector<string>& current, size_t start) {
    levels[(int)current.size()]++;
    if(current.size() == 6) optimizers.insert(current);
    for(size_t j = start; j < candidates.size(); ++j)
        if(permissible(current, candidates[j])) {
            current.push_back(candidates[j]);
            enumerate(current, j + 1);
            current.pop_back();
        }
}
vector<string> transformed(const vector<string>& code, bool rev, bool comp) {
    auto out = code;
    for(auto& w : out) {
        if(rev) reverse(w.begin(), w.end());
        if(comp) for(char& letter : w) letter = (letter == '0' ? '1':'0');
    }
    sort(out.begin(), out.end());
    return out;
}
int main(int argc, char** argv) {
    if(argc != 2) { cerr << "usage: verifier optimal_codes.txt\n"; return 2; }
    for(int val=0; val<64; ++val) {
        auto w = bitword(val);
        if(primitive(w)) candidates.push_back(w);
    }
    assert(candidates.size() == 54);
    vector<string> cur;
    enumerate(cur, 0);
    assert(levels == (map<int,int>{{0,1},{1,54},{2,814},{3,3042},{4,2480},{5,324},{6,16}}));
    assert(optimizers.size() == 16);
    set<vector<string>> expected;
    ifstream fin(argv[1]);
    if(!fin) { cerr << "cannot open input\n"; return 2; }
    string line;
    while(getline(fin,line)) {
        if(line.empty()) continue;
        istringstream in(line);
        vector<string> code;
        string w;
        while(in >> w) code.push_back(w);
        assert(code.size() == 6);
        assert(is_sorted(code.begin(), code.end()));
        expected.insert(code);
    }
    assert(expected == optimizers);
    set<vector<string>> visited;
    int orbits=0;
    for(const auto& code : optimizers) {
        int distance3=0, distance4=0;
        for(int a=0;a<6;++a) for(int b=a+1;b<6;++b){
            auto d=hamming(code[a],code[b]);
            if(d==3)++distance3;
            else if(d==4)++distance4;
            else assert(false);
        }
        assert(distance3 == 8 && distance4 == 7);
        if(visited.count(code)) continue;
        set<vector<string>> orb;
        for(bool rev : {false,true}) for(bool comp : {false,true})
            orb.insert(transformed(code, rev, comp));
        assert(orb.size()==4);
        for(const auto& c:orb) assert(optimizers.count(c));
        visited.insert(orb.begin(),orb.end());
        orbits++;
    }
    assert(orbits==4 && visited==optimizers);
    cout << "VERIFY_OK independent string/splice enumeration: 6731 nodes, max 6, exactly 16 optimizers and 4 orbits\n";
}
