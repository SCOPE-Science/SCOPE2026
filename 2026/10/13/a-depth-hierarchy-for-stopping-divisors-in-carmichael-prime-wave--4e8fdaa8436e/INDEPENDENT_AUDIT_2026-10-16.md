# Independent mathematical audit

## correctness

PASS

For Carmichael n, Korselt guarantees squarefree odd n. Write d_min for the least divisor with d*lcm_{p|d}(p−1)>n and p1>p2>... its descending prime factors. For j≥2, removing p_j from n leaves p1, giving lambda(n/p_j)≥p1−1>p_j because distinct odd primes differ by at least 2; hence n/p_j is stopping, so d_min≤n/p_j. But d_min≥p1...p_j>p_j^j, yielding p_j^(j+1)<n. The result is universal, not a finite exhaustive extrapolation. Independent integer enumeration of 16 Carmichael numbers through 100000 tested 18 depth inequalities and critical printed B=10^24 cutoffs.

## originality

PASS

The directly motivating 2026 prime-wavelet article proves the depth-2 cube-root bound. Its construction explicitly orders prime factors of d_min and uses a single bitmap under B^(1/3), but no higher-depth p_j^(j+1)<n hierarchy was located in inspected Sections defining the encoder. An older Carmichael tabulation bound concerns complete factorizations and does not imply least-stopping-divisor minimality.

## value

PASS

The j-th prime of the canonical least stopping divisor occupies depth j in a concrete compression structure. The theorem gives a deterministic decreasing universe for later depths and potentially reduces exact encode/decode representation cost; it is a natural reusable structural refinement beyond the published depth-two base case, without invented measured performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
