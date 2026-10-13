// Independent exhaustive certificate: first enumerate *all* size-16 binary
// seven-bit one-deletion codes, then filter the adjacent-swap property.
// Unlike verify_direct.py, the search graph does NOT contain swap constraints.
#include <array>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int N = 7, Q = 1 << N;
using B = bitset<Q>;
array<uint64_t,Q> descendants;
array<array<uint64_t,2>,Q> swaps;
array<B,Q> edges;
long long visits = 0, deletion_16 = 0, mixed_16 = 0, deletion_17 = 0;

int getbit(int x, int at) {return (x >> (N - 1 - at)) & 1;}
int remove_at(int x, int at) {
    int y = 0;
    for (int i = 0; i < N; ++i) if (i != at) y = (y << 1) | getbit(x,i);
    return y;
}
int adjacent_swap(int x, int at) {
    int y = 0;
    for (int i = 0; i < N; ++i) {
        int k = (i == at ? at+1 : (i == at+1 ? at : i));
        y = (y << 1) | getbit(x,k);
    }
    return y;
}
void initialize() {
    for (int x = 0; x < Q; ++x) {
        for (int i = 0; i < N; ++i) descendants[x] |= uint64_t(1) << remove_at(x,i);
        swaps[x][x/64] |= uint64_t(1) << (x%64);
        for (int i = 0; i < N-1; ++i) {
            int z = adjacent_swap(x,i);
            swaps[x][z/64] |= uint64_t(1) << (z%64);
        }
    }
    for (int x = 0; x < Q; ++x)
      for (int y = 0; y < Q; ++y)
        if (x != y && (descendants[x] & descendants[y]) == 0)
            edges[x].set(y);
}
int first(B bits) {
    for (int i = 0; i < Q; ++i) if (bits[i]) return i;
    throw runtime_error("empty bitset");
}
void colors(B candidates, vector<int>& order, vector<int>& upper) {
    int color = 0;
    while (candidates.any()) {
        ++color;
        B independent = candidates;
        while (independent.any()) {
            int v = first(independent);
            order.push_back(v); upper.push_back(color);
            candidates.reset(v);
            independent.reset(v);
            independent &= ~edges[v];
        }
    }
}
void search(B candidates, vector<int>& chosen, int target) {
    ++visits;
    if (int(chosen.size()) == target) {
        if (target == 17) {++deletion_17;return;}
        ++deletion_16;
        bool valid = true;
        for (int i = 0; i < target && valid; ++i) for (int j = i+1; j < target; ++j) {
            int a = chosen[i], b = chosen[j];
            if ((swaps[a][0] & swaps[b][0]) || (swaps[a][1] & swaps[b][1])) {
                valid = false; break;
            }
        }
        if (valid) ++mixed_16;
        return;
    }
    if (!candidates.any()) return;
    vector<int> order, upper;
    colors(candidates, order, upper);
    for (int i = int(order.size()) - 1; i >= 0; --i) {
        if (int(chosen.size()) + upper[i] < target) break;
        int v = order[i];
        chosen.push_back(v);
        search(candidates & edges[v],chosen,target);
        chosen.pop_back();
        candidates.reset(v);
    }
}
int main() {
    initialize();
    B all;all.set();vector<int> chosen;
    search(all,chosen,17);
    search(all,chosen,16);
    if (deletion_17 != 0 || deletion_16 != 408 || mixed_16 != 28) {
        cerr << "Unexpected census: " << deletion_17 << " " << deletion_16
             << " " << mixed_16 << "\n";
        return 1;
    }
    cout << "VERIFY_OK length=7 deletion_size17=" << deletion_17
         << " deletion_size16=" << deletion_16 << " mixed_size16=" << mixed_16
         << " nodes=" << visits << "\n";
}
