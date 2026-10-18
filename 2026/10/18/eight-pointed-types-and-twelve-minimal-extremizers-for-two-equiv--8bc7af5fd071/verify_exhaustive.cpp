// Exhaustive second finite check for pairs of set partitions.
// Fix one E-partition of each integer block-size pattern and enumerate
// all restricted-growth encodings of F. This covers every isomorphism
// type, with possible repetitions inside a fixed E-pattern.
#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>

static int n, e_mask[16], f_mask[16], f_class[16], col_mask[16];
static long long examined, complete_hits;
static int max_types, distinct_signatures;
static std::array<unsigned char, 65536> seen;
static std::vector<int> sizes;

static void evaluate() {
  for (int i = 0; i < n; ++i) f_mask[i] = col_mask[f_class[i]];
  const int universe = (1 << n) - 1;
  unsigned int signature = 0;
  for (int i = 0; i < n; ++i) {
    const int a = (e_mask[i] & f_mask[i] & ~(1 << i)) != 0;
    const int b = (e_mask[i] & ~f_mask[i]) != 0;
    const int c = (f_mask[i] & ~e_mask[i]) != 0;
    const int d = (universe & ~(e_mask[i] | f_mask[i])) != 0;
    const int type = (a << 3) | (b << 2) | (c << 1) | d;
    signature |= 1u << type;
  }
  if (!seen[signature]) {
    seen[signature] = 1;
    ++distinct_signatures;
  }
  const int population = __builtin_popcount(signature);
  if (population > max_types) max_types = population;
  if (n == 12 && signature == 0xAAAAu) ++complete_hits;
  ++examined;
}

static void enumerate_F(int position, int last_class) {
  if (position == n) {
    evaluate();
    return;
  }
  for (int c = 0; c <= last_class + 1; ++c) {
    f_class[position] = c;
    col_mask[c] |= (1 << position);
    enumerate_F(position + 1, std::max(c, last_class));
    col_mask[c] ^= (1 << position);
  }
}

static void enumerate_E_size_patterns(int remaining, int min_block_size) {
  if (remaining == 0) {
    int position = 0;
    for (int size : sizes) {
      const int mask = ((1 << size) - 1) << position;
      for (int j = 0; j < size; ++j) e_mask[position++] = mask;
    }
    f_class[0] = 0;
    col_mask[0] = 1;
    enumerate_F(1, 0);
    col_mask[0] = 0;
    return;
  }
  for (int k = min_block_size; k <= remaining; ++k) {
    sizes.push_back(k);
    enumerate_E_size_patterns(remaining - k, k);
    sizes.pop_back();
  }
}

int main() {
  const int expected_max[] = {0,1,1,3,4,4,5,5,6,6,7,7,8};
  const int expected_signature_totals[] = {0,1,4,10,27,55,100,156,209,247,270,279,280};
  for (n = 1; n <= 12; ++n) {
    seen.fill(0);
    examined = complete_hits = 0;
    max_types = distinct_signatures = 0;
    enumerate_E_size_patterns(n, 1);
    if (max_types != expected_max[n] ||
        distinct_signatures != expected_signature_totals[n]) {
      std::fprintf(stderr, "Unexpected count at n=%d: max=%d, signatures=%d\n",
                   n, max_types, distinct_signatures);
      return 1;
    }
    if (n == 12 && complete_hits != 2448) {
      std::fprintf(stderr, "Unexpected twelve-point witness count: %lld\n", complete_hits);
      return 1;
    }
    std::printf("n=%d enumerated=%lld types_max=%d spectra=%d\n",
                n, examined, max_types, distinct_signatures);
  }
  std::puts("EXHAUSTIVE_OK first_eight_pointed_types_at_n=12 labeled_partition_hits=2448");
  return 0;
}
