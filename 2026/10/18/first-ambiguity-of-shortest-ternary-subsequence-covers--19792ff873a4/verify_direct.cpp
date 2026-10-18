// Exhaustive definition-based certificate for the ternary shortest-s-cover threshold.
// C++17, standard library only: g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    // Number of restricted-growth words of lengths 1,...,11 with <=3 symbols.
    const vector<int> expected{0,1,2,5,14,41,122,365,1094,3281,9842,29525};
    unsigned long long total_embeddings = 0;
    unsigned long long labeled_ambiguous = 0;
    for (int n=1; n<=11; ++n) {
        int canonical=0, ambiguous=0;
        function<void(const string&,int)> visit = [&](const string& word, int largest) {
            if ((int)word.size() < n) {
                for (int letter=0; letter<=min(2,largest+1); ++letter)
                    visit(word+char('0'+letter),max(largest,letter));
                return;
            }
            ++canonical;
            const unsigned complete=(1U<<n)-1;
            unordered_map<string,uint16_t> occupied;
            // Every nonempty position subset is an occurrence of exactly one string.
            for (unsigned mask=1; mask<=complete; ++mask) {
                string candidate;
                for (int i=0; i<n; ++i) if (mask & (1U<<i)) candidate+=word[i];
                occupied[candidate] |= static_cast<uint16_t>(mask);
                ++total_embeddings;
            }
            // OR of all occurrence masks is all-ones iff the candidate covers each position.
            int shortest=n+1; vector<string> minimizers;
            for (const auto& entry:occupied) {
                if (entry.second != complete) continue;
                const int length=(int)entry.first.size();
                if (length < shortest) { shortest=length; minimizers={entry.first}; }
                else if (length == shortest) minimizers.push_back(entry.first);
            }
            if (minimizers.empty()) throw runtime_error("word failed to cover itself");
            if (minimizers.size()>1) {
                ++ambiguous;
                // Restoring names of all present letters gives this orbit's labeled size.
                int orbit=1; for (int j=0; j<=largest; ++j) orbit*=3-j;
                labeled_ambiguous+=orbit;
                sort(minimizers.begin(),minimizers.end());
                if (!(n==11 && word=="01012021010" && shortest==6 &&
                      minimizers==vector<string>{"010210","012010"}))
                    throw runtime_error("unexpected shortest-cover ambiguity");
                cout << "EXCEPTION length=" << n << " word=" << word
                     << " covers=" << minimizers[0] << "," << minimizers[1] << "\n";
            }
        };
        visit("0",0);
        if (canonical != expected[n] || ambiguous != (n==11 ? 1 : 0))
            throw runtime_error("unexpected canonical count or exception count");
        cout << "length="<<n<<" canonical="<<canonical<<" ambiguous_orbits="<<ambiguous<<"\n";
    }
    if (labeled_ambiguous != 6 || total_embeddings != 72517166ULL)
        throw runtime_error("labeled count or total enumeration size disagrees");
    cout << "total_occurrence_subsets="<<total_embeddings
         << " ambiguous_labeled_words="<<labeled_ambiguous<<"\n";
    cout << "DIRECT_CERTIFICATE_PASSED\n";
}
