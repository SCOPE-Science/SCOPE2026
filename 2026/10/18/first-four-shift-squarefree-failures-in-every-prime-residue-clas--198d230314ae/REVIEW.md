# Independent mathematical audit

## correctness

PASS

I reproduced all twelve minima by independently marking multiples of every integer square ≥4 through B=6165527, and separately marking odd composites using all odd factors up to sqrt(B). Marking composite-base squares adds no false positives, since their bases themselves have prime divisors; an odd composite has a smaller odd factor at most its square root. The exhaustive increasing candidate scan starts at p=9, ensuring positive shifts, and reaches a verified witness in every reduced class. Every displayed prime, each prime-square witness and every forced-offset count f(r) was checked from the frozen table. The prime units 5 and 7 below the positivity cutoff could not create extra cases even if one allowed nonpositive shifts, because their p−2 remainders are 3 and 5. There is no density claim for other classes and no inference for exponents beyond 0,1,2,3.

## originality

PASS

This passes for the complete twelve-class profile, not for claiming novelty of each row. Harman–Paquin explicitly give the r=7 minimum 4851151 and the same four prime-square witnesses; this is verified prior coverage, not merely a possible overlap. The frozen contribution is the joint exact classification, with the other eleven minima not implied by the r=7 proof or census. No inspected source gives the full classification. The frozen discussion already singles out possible prior coverage of r=7; for any subsequent use, credit it as confirmed prior work.

## value

PASS

The four shifts come from the initial exponent window in a studied squarefree-plus-power-of-two question, and 36 is the combined modulus of the two smallest prime squares. The partition is exhaustive over the prime classes and naturally separates the offsets already forced to fail, rather than selecting strata after the scan. The resulting exact thresholds distinguish the genuinely unforced classes (including the verified r=23 threshold 6165527), and provide benchmarks for residue-sensitive searches. No statistical law or causal conclusion is drawn from the finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
