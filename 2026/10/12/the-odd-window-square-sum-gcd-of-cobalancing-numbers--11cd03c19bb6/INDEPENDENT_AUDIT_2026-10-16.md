# Independent mathematical audit

## correctness

PASS

For every positive odd k the affine cobalancing recurrence b_(n+2)=6b_(n+1)-b_n+2, normalized by a=b/2, yields a_(n+k)-a_n=Q_k B_(n+(k-1)/2). The square-window difference is Q_k u_n v_n. The modular recurrence for u and v restricts gcd_n(u_n v_n) to a divisor of 7, with at most one 7; possible 7 requires 3|k. An independently checked exact telescoping coboundary 64a_(n+1)^2=Delta G+5 gives 64F_0 congruent 5k mod Q_k; Pell norm excludes 5|Q_k for odd k. For k odd divisible by 3, the 7-adic identity nu_7(Q_k)=1+nu_7(k) eliminates the potential extra factor in the full-window gcd. The result is gcd_n sum_i b_(n+i)^2=4 gcd(k,Q_k). Independent recurrence-based integer computation checked every odd k<=101 over hundreds of windows, but proof—not experiments—supports universal k and n.

## originality

PASS

The result explicitly settles all odd lengths of the cobalancing-square case identified as Question 30 by Mbirika, Schrader and Spilker. Prior unsquared braid/gcd identities and a generalized homogeneous Fibonacci square-window theorem do not imply its affine-cobalancing 7-adic argument. Semantic literature search found only adjacent Pell invariants, so residual unindexed-equivalence risk remains.

## value

PASS

This is a closed expression for an infinite arithmetic family that a primary source explicitly identified as an open square-window gcd problem. Distinguishing the possible exceptional prime 7 and its exact valuation is a genuine obstruction; the result is neither a renaming of the unsquared braid formulas nor merely small-case enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
