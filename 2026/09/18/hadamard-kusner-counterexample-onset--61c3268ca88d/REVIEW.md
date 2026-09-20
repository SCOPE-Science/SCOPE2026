# Review

## Correctness

The generalized construction was checked against the four pair types in
Xiong's proof.  The only matrix facts used in the distance count are:
distinct Hadamard rows agree and disagree equally often; a normalized column
is constant; and \(H_4\otimes H\) is again Hadamard.  These facts give the
counts in equation (17), and direct substitution of equations (16) and (18)
makes all four total \(p\)-th-power distances equal to \(2^pmR\).

The four vectors in equation (10) were checked directly to satisfy the norm
and sum/difference identities in equation (11).  The parameter existence
argument is valid because \(F_p(1)<1\), while Xiong's Lemma 4.1 gives
\(F_p(4^{1/p})=1+\Delta(p)>1\); condition \(m>1/\Delta(p)\) then supplies the
intermediate-value crossing.

The expansion at \(p=4\) was checked directly from the explicit formula (1).
The identity
\[
F_4(a)-1=-\frac{3(a^2-2)^2}{4(a^4+2)}
\]
provides an additional stress test: the threshold is tangent at the unique
point \(a=\sqrt2\), and the derivative in the exponent is the positive
constant \(c_4\) stated in equation (4).  The large-\(p\) expansion follows
from
\[
\log\frac{1+e^{(\log4)/p}}2
=
\frac{\log4}{2p}
+
\frac{(\log4)^2}{8p^2}
+
O(p^{-4}).
\]

The use of Hadamard-order density is supported by Lemma 20(3) of
Swanepoel--Villa.  The lower bound is a direct contrapositive of Swanepoel's
Corollary 1.4, followed by asymptotic inversion.  No computational
enumeration is used as a substitute for a proof.

## Originality

Xiong's arXiv:2609.14794 was read at the theorem, construction, distance
calculation, and parameter-existence sections.  It fixes \(m=2^k\), uses
Walsh matrices \(H_k,H_{k+2}\), and proves existence for sufficiently large
\(m\); it does not state the arbitrary-Hadamard transfer, a quantitative
first-counterexample dimension, or the asymptotics in equations (6)--(9).

Swanepoel--Villa's 2013 paper was checked because it is the closest
methodological precedent.  It explicitly uses arbitrary Hadamard matrices
and asymptotic density of Hadamard orders for a different construction in the
regime \(1\le p<2\).  This is prior art for the amplification method, but it
does not cover the recent \(p>4\) construction or the transition at \(p=4\).

Swanepoel's 2014 \(4\)-norm paper supplies the known stability inequality
used for the lower side of (7); that inequality is not claimed as new.
Chalmers' 2026 paper supplies a separate \(p=5\) counterexample and an
open-interval persistence result, but no all-\(p>4\) dimension law.
Ge--Xu--Zhou establish the exact \(2\le p\le4\) regime and broader upper
bounds, not a \(p>4\) counterexample-dimension estimate.

Searches using the combinations “Kusner Hadamard p>4”, “Hadamard order
8m-2 equilateral”, “counterexample dimension p-4”, the explicit constants
in (4), (6), and (9), and synonymous formulations did not locate a prior
statement of Theorem 1 or the onset window (7).  No highly relevant source
identified in this search was inaccessible.  Because Xiong's preprint is
very recent, unindexed or simultaneous work remains a material residual
originality risk.

## Value

The result turns a qualitative all-\(p>4\) existence theorem into a
quantitative statement about where counterexamples first occur in dimension.
Near the sharp boundary \(p=4\), it places the first counterexample dimension
between
\[
\asymp \frac1{(p-4)\log(1/(p-4))}
\quad\text{and}\quad
O\!\left(\frac1{p-4}\right),
\]
with explicit leading constants on both available bounds.  It also identifies
the matrix-theoretic freedom hidden in the new construction and removes the
factor-of-two granularity inherent in restricting the order to powers of two
at the asymptotic level.

The large-\(p\) consequence gives an explicit \(O(p)\) dimension bound from
the same construction.  These estimates may be useful for comparing future
low-dimensional constructions with the structured Hadamard family.

## Limitations

The logarithmic gap in (7) is unresolved.  The upper bounds are not claimed
to be optimal for \(\nu(p)\), and the large-\(p\) linear bound may be far from
the true behavior.  The arbitrary-Hadamard theorem is a transfer for Xiong's
specific two-block construction, not a classification of all equilateral
sets.  The \(58\)-point construction at \(p=5\) demonstrates that unrelated
configurations can be substantially smaller at individual exponents.

Same-model review: passed. Independent audit: not yet performed.
