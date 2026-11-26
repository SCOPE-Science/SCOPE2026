# Independent mathematical audit

## correctness

PASS

With the stated zero-based digit rule, f_{2j}=j mod 2 and f_{2j+1}=f_j. No factor of length four alternates: its two even-indexed letters differ. For length at least eight each parity track has length at least four; the track from even positions alternates and the other is a contiguous factor, so a factor recognizes the parity of its start. When n≥16, same-parity equality is equivalent to equality of the odd-index track, of length floor(n/2) for even starts and ceil(n/2) for odd starts. The reverse implication holds because equality of those shorter factors, still of length ≥8, forces the same phase on the alternating track. Thus the earliest second start is the smaller of 2R(floor(n/2)) and 2R(ceil(n/2))+1, necessarily the even one by monotonicity under extension. Its earlier matching start likewise doubles and is unique because all starts before the first duplicate are pairwise distinct. For a reproducible finite base, generate indices 0–38 by stripping powers of 2 from i+1 and compare exact slices of lengths 1–15 in increasing start order. The short (R,q) sequence is (1,0),(3,0),(3,0),(8,3),(8,3),(12,4),(12,4); the 24 length-eight factors at starts 0–23 are distinct, and the slices of length fifteen at 8 and 24 both equal 001101100010011. This proves the base for all 8≤n≤15, and the decimation proves all larger n. The independent bounded witness check for n=8,…,8191 also agrees, but the infinite conclusion does not rely on it or on executing the supplied verifier. The dyadic block endpoints give limit inferior 3/2 and limit superior 3; Allouche's 4n count for n≥7 then gives 3/8 and 3/4.

## originality

PASS

The supported distinct claim is the exact paperfolding first-duplicate law together with the earlier matching position, rather than the definition of initial non-repetitive complexity, factor equality by automata, or ordinary and appearance complexity. The closest available paperfolding comparisons involve the last new occurrence or a different equivalence/counting procedure; the closest exact initial-complexity catalogue entry treats a different sequence. Canonical-position full-text coverage remains a named risk.

## value

PASS

The first duplicate is a natural prefix analogue to global factor complexity and to the latest first occurrence. Its exact position is not given by the total number of distinct factors or the covering endpoint. The dyadic law and unique location of the partner identify exactly how long the initial scan remains injective, and the parity/decimation argument explains why both positions scale together. This supplies a useful exact word-combinatorics invariant rather than a finite list of collisions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
