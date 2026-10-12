// Exact unlabeled equality-pattern census for a six-symbol transmission over an arbitrary finite alphabet.
// Compile: g++ -O2 -std=c++17 verify_rgs.cpp -o verify_rgs && ./verify_rgs
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

using Word = array<int, 12>;
Word pattern{};
vector<pair<int,int>> survivor_pairs;
uint64_t bell[13]{};
uint64_t counts[13][4]{};
uint64_t max_overlap=0;

void collect_survivor_positions() {
    vector<int> base = {0,1,2,3,4,5};
    for (int i=0; i<=4; ++i) {
        vector<int> once;
        for (int j=0; j<6; ++j) if (!(i<=j && j<i+2)) once.push_back(j);
        for (int j=0; j<=2; ++j) {
            vector<int> twice;
            for (int k=0;k<4;++k) if (!(j<=k && k<j+2)) twice.push_back(once[k]);
            survivor_pairs.push_back({twice[0], twice[1]});
        }
    }
    sort(survivor_pairs.begin(), survivor_pairs.end());
    survivor_pairs.erase(unique(survivor_pairs.begin(), survivor_pairs.end()), survivor_pairs.end());
    assert((survivor_pairs == vector<pair<int,int>>{{0,1},{0,3},{0,5},{2,3},{2,5},{4,5}}));
}

void evaluate(int k) {
    ++bell[k];
    bool equal=true;
    for(int i=0;i<6;++i) if(pattern[i]!=pattern[6+i]) { equal=false;break; }
    if(equal) return;
    set<pair<int,int>> first,second;
    for (auto [a,b]:survivor_pairs) {
        first.insert({pattern[a], pattern[b]});
        second.insert({pattern[a+6],pattern[b+6]});
    }
    int overlap=0;
    for (const auto& edge:first) if(second.count(edge)) ++overlap;
    max_overlap=max(max_overlap,(uint64_t)overlap);
    if(overlap==5) {
        int type=first.size()==5&&second.size()==5 ? 1 :
                 first.size()==6&&second.size()==6 ? 3 : 2;
        ++counts[k][type];
    }
}

void enumerate(int pos, int used) {
    if(pos==12) { evaluate(used);return; }
    for(int lab=0;lab<=used;++lab) {
        pattern[pos]=lab;
        enumerate(pos+1,max(used,lab+1));
    }
}
int main() {
    collect_survivor_positions();
    pattern[0]=0;
    enumerate(1,1);
    const uint64_t expected[13][4]={
      {}, {}, {},
      {0,72,96,42},
      {0,72,288,222},
      {0,12,144,207},
      {0,0,16,55},
      {0,0,0,4}
    };
    uint64_t belltotal=0;
    for (int k=1;k<=12;++k) {
        belltotal+=bell[k];
        for (int j=1;j<=3;++j) assert(counts[k][j]==expected[k][j]);
        cout << k << ',' << bell[k] << ',' << counts[k][1] << ','
             << counts[k][2] << ',' << counts[k][3] << '\n';
    }
    assert(belltotal==4213597);
    assert(max_overlap==5);
    cout << "VERIFY_RGS_OK patterns=4213597 maximum_overlap=5 C3=210 C4=582 C5=363 C6=71 C7=4\n";
}
