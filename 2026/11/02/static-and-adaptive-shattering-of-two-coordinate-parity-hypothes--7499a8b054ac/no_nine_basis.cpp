// Exhaustive finite check of nine-point two-bases of the 5-dimensional binary space.
// Translation lets us require that the first point be zero. There are C(31,8) cases.
#include <cstdint>
#include <cstdio>
int main() {
    uint64_t checked = 0;
    const uint64_t end = uint64_t(1) << 31;
    for (uint64_t mask = (uint64_t(1) << 8) - 1; mask < end;) {
        unsigned a[9] = {0};
        int used = 1;
        for (unsigned bit = 0; bit < 31; ++bit)
            if (mask & (uint64_t(1) << bit)) a[used++] = bit + 1;
        if (used != 9) return 3;
        uint32_t covered = 0;
        for (int i=0; i<9; ++i)
            for (int j=i+1; j<9; ++j)
                covered |= uint32_t(1) << (a[i] ^ a[j]);
        if (covered == UINT32_C(0xfffffffe)) {
            std::printf("COUNTEREXAMPLE mask=%llu\n", (unsigned long long)mask);
            return 1;
        }
        ++checked;
        uint64_t low = mask & (~mask + 1);
        uint64_t nxt = mask + low;
        mask = (((nxt ^ mask) >> 2) / low) | nxt;
    }
    if (checked != UINT64_C(7888725)) return 2;
    std::printf("NO_NINE_POINT_BASIS_PASS %llu\n", (unsigned long long)checked);
    return 0;
}
