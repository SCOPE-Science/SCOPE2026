# Independent mathematical audit

## correctness

PASS

The exact formula and unique maximizing pair are correct. The frozen Finding's unqualified claim that the maximizer is not an edge composition is false for 3 <= N <= 6; repairs/3/RESULT.md states the correct cutoff N >= 7 without changing the theorem. Omitting a success/failure gives Q masses p and 1-p. The two P atoms both equal the Bin(N,p) mean atom. On L <= floor(N/2) the successive ratio is C_(N-k-1)/A_k, with C_m=(1+1/m)^(m-1) strictly increasing by the logarithmic derivative and A_k=(1+1/k)^k. At m=3k+1 the comparison after kth roots and clearing positive denominators leaves 2k+1 in favor of A_k. At m=3k+2 the second-order Taylor lower bound after kth roots exceeds 1+1/k by (k+1)/(2k^2(3k+2)^2). Thus increase occurs iff N >= 4k+3, with strict decrease otherwise. The half-range peak is floor((N+1)/4), and reflection yields distinct maximizers, including the no-adjacent-comparison case N=3. The corrected edge cutoff follows directly from that floor. Independent exact checks from the defining laws reproduced both winners and both strict adjacent signs at N=3..80 via python -B reviews/check_hypergeometric.py; the finite check is not the proof. The frozen script was inspected, not executed.

## originality

PASS

The supported distinct result is the exact outer composition optimizer in the one-omission, directed maximal-density-ratio regime, not the fixed-composition count maximization or the binomial atom reduction. The corrected small-N edge qualification does not enlarge that claim.

## value

PASS

This is an exact, sharp composition extremum for a natural near-census endpoint of a published approximation problem. It exhibits a qualitative change from edge maximizers to asymptotically quarter/three-quarter proportions and quantifies the cutoff, including small boundary cases. It does not claim an intermediate-sample phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
