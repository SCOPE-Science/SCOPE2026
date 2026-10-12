// Independent exact verification directly against every binary test word.
// Build: c++ -std=c++17 -O2 verify_words.cpp -o verify_words && ./verify_words
#include <array>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>
#include <cassert>

int main() {
    constexpr int target_size[12] = {0,0,0,0,16,10,9,7,7,6,6,6};
    constexpr int target_count[12] = {0,0,0,0,1,2,50,8,52,10,14,30};
    for (int length = 4; length <= 11; ++length) {
        std::vector<uint16_t> present;
        for (int w = 0; w < (1 << length); ++w) {
            uint16_t present_patterns = 0;
            for (int j = 0; j <= length - 4; ++j) {
                int four_mer = (w >> j) & 15;
                present_patterns |= uint16_t(1u << four_mer);
            }
            present.push_back(present_patterns);
        }
        int best = 17;
        int nbest = 0;
        for (int set_mask = 0; set_mask < 65536; ++set_mask) {
            int n = __builtin_popcount(unsigned(set_mask));
            if (n > best) continue;
            bool covers_all = true;
            for (uint16_t mask : present) {
                if ((mask & uint16_t(set_mask)) == 0) {
                    covers_all = false;
                    break;
                }
            }
            if (covers_all) {
                if (n < best) { best = n; nbest = 0; }
                ++nbest;
            }
        }
        assert(best == target_size[length] && nbest == target_count[length]);
        std::cout << length << " " << best << " " << nbest << "\n";
    }
    std::cout << "DIRECT_WORD_CENSUS_PASS\n";
}
