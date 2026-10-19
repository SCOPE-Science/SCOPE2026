// Independent full-alphabet exhaustive check of finite curling transforms.
// C++17. No symmetry quotient, data files or third-party libraries.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using std::string;
using State = std::pair<string,string>;

bool has_terminal_overlap(const string &s) {
    const int n = static_cast<int>(s.size());
    for (int step = 1; 2 * step + 1 <= n; ++step) {
        bool periodic = true;
        for (int k = 0; k <= step; ++k) {
            if (s[n-2*step-1+k] != s[n-step-1+k]) {
                periodic = false;
                break;
            }
        }
        if (periodic) return true;
    }
    return false;
}

char new_curl(const string &s) {
    const int n = static_cast<int>(s.size());
    for (int r = 1; 2*r <= n; ++r) {
        bool repeated = true;
        for (int k = 0; k < r; ++k) {
            if (s[n-2*r+k] != s[n-r+k]) {
                repeated = false;
                break;
            }
        }
        if (repeated) return '2';
    }
    return '1';
}

int main() {
    std::vector<State> frontier(1);
    std::map<string,int> output_counts;
    std::map<string,std::set<char>> children;
    std::map<string,std::map<char,char>> child_curls;
    for (int n = 1; n <= 85; ++n) {
        std::vector<State> next;
        next.reserve(frontier.size()*2);
        for (const auto& [w,c] : frontier) {
            for (char a = '0'; a <= '2'; ++a) {
                string nw=w+a;
                if (has_terminal_overlap(nw)) continue;
                string nc=c+new_curl(nw);
                if (has_terminal_overlap(nc)) continue;
                next.emplace_back(std::move(nw), std::move(nc));
            }
        }
        frontier.swap(next);
        if (n == 84) {
            for (const auto& [w,c] : frontier) {
                ++output_counts[c];
                children[w.substr(0,83)].insert(w.back());
                child_curls[w.substr(0,83)][w.back()] = c.back();
            }
        }
        if (n==83 || n==84 || n==85) {
            std::cout << "length=" << n << " count=" << frontier.size() << '\n';
        }
    }
    assert(frontier.empty());
    assert(output_counts.size() == 2);
    assert(output_counts.begin()->second == 4032);
    assert(std::next(output_counts.begin())->second == 2016);
    assert(children.size() == 2016);
    assert(output_counts.begin()->first.size() == 84);
    const string first=output_counts.begin()->first;
    const string second=std::next(output_counts.begin())->first;
    assert(first.substr(0,83)==second.substr(0,83));
    assert(first[83]=='1' && second[83]=='2');
    for(const auto& [parent, choices] : children) {
        assert(choices.size()==3 && choices.count('0') && choices.count('1') && choices.count('2'));
        int count_1=0, count_2=0;
        for (const auto& [symbol, last_curl] : child_curls[parent]) {
            if (last_curl=='1') ++count_1;
            if (last_curl=='2') ++count_2;
        }
        assert(count_1==2 && count_2==1);
    }
    std::cout << "extendable_83_prefixes=" << children.size() << '\n';
    for (const auto& [transform,frequency] : output_counts) {
        std::cout << "image=" << transform << " frequency=" << frequency << '\n';
    }
    std::cout << "PASS\n";
}
