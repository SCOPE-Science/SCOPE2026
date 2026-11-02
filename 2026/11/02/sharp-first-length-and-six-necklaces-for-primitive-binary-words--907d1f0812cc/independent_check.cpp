// Independent exhaustive binary-word and cyclic Abelian-border enumeration.
// Build: c++ -std=c++17 -O2 independent_check.cpp -o independent_check
// Run: ./independent_check
#include <algorithm>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

string least_rotation(const string& w) {
    string best = w;
    for (size_t j = 1; j < w.size(); ++j)
        best = min(best, w.substr(j) + w.substr(0, j));
    return best;
}

bool primitive(const string& w) {
    const int n = static_cast<int>(w.size());
    for (int d = 1; d < n; ++d) if (n % d == 0) {
        bool repeating = true;
        for (int i = d; i < n; ++i)
            if (w[i] != w[i % d]) { repeating = false; break; }
        if (repeating) return false;
    }
    return true;
}

bool every_rotation_abelian_bordered(const string& w) {
    const int n = static_cast<int>(w.size());
    for (int start = 0; start < n; ++start) {
        int prefix_ones = 0, suffix_ones = 0;
        bool bordered = false;
        for (int k = 1; k <= n / 2; ++k) {
            prefix_ones += w[(start + k - 1) % n] == '1';
            suffix_ones += w[(start + n - k) % n] == '1';
            if (prefix_ones == suffix_ones) { bordered = true; break; }
        }
        if (!bordered) return false;
    }
    return true;
}

int main() {
    const set<string> expected = {
        "0010101100110011", "0010101100110101",
        "0010101101010011", "0010110011001101",
        "0010110100110011", "0011001100110101"
    };
    for (int n = 1; n <= 16; ++n) {
        unsigned total = 0;
        set<string> necklaces;
        for (unsigned v = 0; v < (1u << n); ++v) {
            string w(n, '0');
            for (int i = 0; i < n; ++i) if ((v >> i) & 1u) w[i] = '1';
            if (!primitive(w)) continue;
            if (!every_rotation_abelian_bordered(w)) continue;
            ++total;
            necklaces.insert(least_rotation(w));
            if (n == 16 && count(w.begin(), w.end(), '1') != 8)
                throw runtime_error("unexpected content at length 16");
        }
        if (n < 16 && total) throw runtime_error("shorter witness");
        if (n == 16 && (total != 96 || necklaces != expected))
            throw runtime_error("length-16 census mismatch");
    }
    cout << "FIRST_LENGTH 16\nPRIMITIVE_LABELED 96\nCYCLIC_CLASSES 6\nVERIFY_OK\n";
}
