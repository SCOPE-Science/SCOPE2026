# Independent mathematical audit

## correctness

PASS

Theorem 1(iii) in the author-hosted 2018 text requires distinct even β_i and Σα_i/β_i=1 for bounded GPEs (continuity on every hyperplane, not just every line). The preceding paragraph excludes odd β_i. The denominator degree is max β_i; there is no common variable factor with the monomial numerator. The frozen witness has distinct positive even β_i, max 30 and the sum is exactly 1. For degree≤28 put d_i=β_i/2. The 2002 nine-subsets of {1,…,14} are exhaustive. The bundled bitset proof is valid: positivity bounds α_i by 2d_i−1, the shifts encode all increments x_i=α_i−1, and truncating above target cannot discard a future solution because increments are nonnegative. Independently, for any integer sum Σα_i/d_i, the reduced denominator of α_i/d_i divides lcm(d_j:j≠i), so its allowed values are exactly positive integer multiples of 1/gcd(d_i,lcm(d_j:j≠i)). Tightening all denominators this way preserves the existence equation and can be repeated to stability. An exact rational census of all 2002 sets leaves only 13 with tightened all-ones sum ≤2. A separate recursive rational enumeration of nonnegative increments up to the residual exhausts those 13 and finds no solution. The independent replay also confirms the witness: python3 -B /workspace/audit-evidence/2_prime_constraints.py; /workspace/audit-evidence/2_replay.txt. Degree 29 is excluded by evenness, so the bound is exact.

## originality

PASS

The author-hosted primary text itself distinguishes unrestricted D(9)=22 from the blank bounded D_b(9) in Table 3. Its defining arithmetic characterization, general bounds and proposed questions do not resolve this exact case. The predecessor reaches the bounded n=4 value; no later materially matching result was identified in the targeted literature and Resultary checks.

## value

PASS

Nine is the first dimension with a blank bounded value in the initiating table, not a dimension chosen after searching. The exact minimum fills one gap in the published bounded sequence and resolves both feasibility at 30 and exclusion below it; it also distinguishes the bounded degree from the known unrestricted value 22. This is a useful exact finite benchmark, not a general asymptotic, monotonicity, or classification theorem for all dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
