# Independent mathematical audit

## correctness

PASS

At a complete block join exactly the starts at most i are lost from the copied block, while at most |v|-1 occurrences cross the new join. The normalized recurrence therefore has an absolutely summable tail bounded by (i+|v|)/2^(i-1). For L_i<=N<L_(i+1), the two boundary-crossing counts enter with opposite signs, so their difference has absolute value at most |v|-1. The reduced prefix length i+N-L_i is at most 2N/3, by L_i>=2i; adding O(i+|v|) at each of O(log N) reductions gives the claimed all-prefix bound, rather than just convergence along block lengths. For an allowed factor, Shallit's recurrence and language theorems give arbitrarily late starts r. The least block index t containing that occurrence is O(log r), and the occurrence and all designated copies double at each join through stage r because their starts are at least r. The normalized lower bound at stage r has numerator 2^(r-t)-(r+1)>0 for large r, even after subtracting all possible later losses. Forbidden factors never occur. Left and right extension counts differ from the parent count by only endpoint errors; these give consistency, invariance and full support, and cylinder averages give genericity. Independent finite replay checked 62 patterns at 14 joins and 1,017,482 prefix inequalities including endpoints.

## originality

PASS

Shallit's exact factor language, recurrence and one-letter density are prior. The distinct contribution is positive limiting frequency for every permitted cylinder with an all-prefix discrepancy estimate. A later indexed Brik record has equivalent frequency/discrepancy claims plus an entropy result; the intervening block-entropy record explicitly attributes the positivity and genericity result to this very frozen record, so the overlap is not evidence of antecedent coverage. This is not a claim of exclusive historical priority.

## value

PASS

For this natural non-uniformly recurrent recursion, the theorem gives an actual fully supported empirical frequency law, replaces bare recurrence by positive asymptotic density, and quantifies convergence for every prefix. The convergent dyadic formula makes individual frequencies approximable; the later block-entropy result exemplifies a use of the frequency law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
