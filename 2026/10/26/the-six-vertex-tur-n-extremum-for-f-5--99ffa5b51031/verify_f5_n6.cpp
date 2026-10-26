#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>

// Exhaustive finite verifier for the six-vertex F5 Turan extremum.
// F5 has edges abc, abd, cde on five distinct vertices a,b,c,d,e.
int popcount(std::uint32_t x) {
    int count = 0;
    while (x) { x &= x - 1; ++count; }
    return count;
}

int main() {
    std::vector<std::array<int, 3>> triples;
    std::map<std::array<int, 3>, int> edge_index;
    for (int a = 0; a < 6; ++a) {
        for (int b = a + 1; b < 6; ++b) {
            for (int c = b + 1; c < 6; ++c) {
                edge_index[{a, b, c}] = static_cast<int>(triples.size());
                triples.push_back({a, b, c});
            }
        }
    }
    assert(triples.size() == 20);

    auto index_of = [&](int a, int b, int c) {
        std::array<int, 3> t{a, b, c};
        std::sort(t.begin(), t.end());
        return edge_index.at(t);
    };

    // Enumerate every injection of the five labelled F5 vertices into [6].
    // Store distinct 3-edge masks, so automorphic copies are deduplicated.
    std::set<std::uint32_t> forbidden;
    for (int omitted = 0; omitted < 6; ++omitted) {
        std::vector<int> q;
        for (int v = 0; v < 6; ++v) if (v != omitted) q.push_back(v);
        std::sort(q.begin(), q.end());
        do {
            const int a = q[0], b = q[1], c = q[2], d = q[3], e = q[4];
            std::uint32_t mask = (1u << index_of(a, b, c))
                               | (1u << index_of(a, b, d))
                               | (1u << index_of(c, d, e));
            forbidden.insert(mask);
        } while (std::next_permutation(q.begin(), q.end()));
    }
    assert(forbidden.size() == 180);

    int best = -1;
    std::vector<std::uint32_t> extremizers;
    std::vector<int> histogram(21, 0);
    const std::uint32_t total = 1u << 20;
    for (std::uint32_t h = 0; h < total; ++h) {
        bool is_free = true;
        for (std::uint32_t f : forbidden) {
            if ((h & f) == f) { is_free = false; break; }
        }
        if (!is_free) continue;
        const int m = popcount(h);
        ++histogram[m];
        if (m > best) { best = m; extremizers.clear(); }
        if (m == best) extremizers.push_back(h);
    }
    assert(best == 10);
    assert(extremizers.size() == 6);

    // Verify each of the six labelled stars occurs among the extremizers.
    std::set<std::uint32_t> extremizer_set(extremizers.begin(), extremizers.end());
    for (int center = 0; center < 6; ++center) {
        std::uint32_t star = 0;
        for (int i = 0; i < 20; ++i) {
            const auto &t = triples[i];
            if (t[0] == center || t[1] == center || t[2] == center) star |= 1u << i;
        }
        assert(popcount(star) == 10);
        assert(extremizer_set.count(star) == 1);
    }

    // Canonicalize each extremizer under all 6! vertex permutations.
    std::vector<std::array<int, 20>> transforms;
    std::vector<int> p{0, 1, 2, 3, 4, 5};
    do {
        std::array<int, 20> tr{};
        for (int i = 0; i < 20; ++i) {
            const auto &t = triples[i];
            tr[i] = index_of(p[t[0]], p[t[1]], p[t[2]]);
        }
        transforms.push_back(tr);
    } while (std::next_permutation(p.begin(), p.end()));
    assert(transforms.size() == 720);

    std::set<std::uint32_t> canonical_types;
    for (std::uint32_t h : extremizers) {
        std::uint32_t canonical = total - 1;
        for (const auto &tr : transforms) {
            std::uint32_t image = 0;
            for (int i = 0; i < 20; ++i) if ((h >> i) & 1u) image |= 1u << tr[i];
            canonical = std::min(canonical, image);
        }
        canonical_types.insert(canonical);
    }
    assert(canonical_types.size() == 1);

    std::cout << "checked_hypergraphs=" << total << '\n';
    std::cout << "distinct_forbidden_patterns=" << forbidden.size() << '\n';
    std::cout << "max_edges=" << best << '\n';
    std::cout << "labeled_extremizers=" << extremizers.size() << '\n';
    std::cout << "isomorphism_classes=" << canonical_types.size() << '\n';
    std::cout << "all_extremizers_are_stars=true\n";
    std::cout << "edge_count_10_extremizers=" << histogram[10] << '\n';
}
