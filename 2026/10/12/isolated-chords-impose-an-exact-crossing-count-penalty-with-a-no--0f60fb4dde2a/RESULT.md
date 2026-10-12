# Isolated chords impose an exact crossing-count penalty with a nonvanishing rare-event correction

## Finding

Let \(\mathcal C_n\) be a uniformly chosen perfect matching of \(2n\) labeled points in circular order, for each integer \(n\ge 2\). Its intersection graph has one vertex per chord and one edge per pair of crossing chords. Write \(I_n\) for the number of degree-zero vertices (all isolated chords, not only adjacent-endpoint chords), \(S_n\) for the number of chords joining circularly consecutive endpoints, and \(X_n\) for the number of crossing pairs. Put
\[
M_0=1,\qquad M_j=(2j-1)!!\quad(j\ge1).
\]
Then the following exact finite-size identity holds:
\[
\boxed{\operatorname{Cov}(I_n,X_n)
=-\frac{n}{3M_n}\sum_{k=0}^{n-1}M_k M_{n-1-k}
\bigl[n-1+k(n-1-k)\bigr]<0.}
\]
Its comparison with the simple-chord covariance is exact:
\[
\operatorname{Cov}(S_n,X_n)=-\frac{2n(n-1)}{3(2n-1)},\quad
\operatorname{Cov}(I_n-S_n,X_n)<0\quad(n\ge3),
\]
with equality in the second relation only at \(n=2\). Moreover,
\[
\boxed{\mathbb E(I_n-S_n)=\frac{1}{2n}+O(n^{-2}),\qquad
\operatorname{Cov}(I_n-S_n,X_n)=-\frac13+O(n^{-1}).}
\]
Consequently \(\operatorname{Cov}(I_n,X_n)=-n/3-1/6+O(n^{-1})\). The final pair of estimates isolates a second-order effect: non-simple isolated chords have expected count tending to zero at rate \(1/n\), yet their crossing-count covariance has a nonzero limit.

## Assumptions and scope

The endpoint set is \(\{1,\ldots,2n\}\), taken in circular order, and all \(M_n\) perfect matchings have probability \(1/M_n\). Two chords cross when their endpoints alternate in cyclic order. An isolated chord means a chord with zero crossing degree, including nested or enclosing chords; a simple chord specifically joins consecutive circular endpoints. No independence is assumed between isolated-chord indicators. All expectations and covariances refer to this finite uniform distribution. The \(O(\cdot)\) estimates are as the integer \(n\) tends to infinity.

## Proof

**1. Unconditional crossing mean.** For any two chords selected symmetrically from the matching, the induced matching on their four cyclically ordered endpoints has three equally likely pairings, exactly one crossing. Therefore
\[
\mathbb E X_n=\frac13\binom n2=\frac{n(n-1)}6.
\]

**2. An isolated distinguished chord splits the matching.** Distinguish the unique chord incident to endpoint \(1\). If its other endpoint is \(2k+2\), then the intervening arc contains \(2k\) points and the complementary arc contains \(2r\), where \(r=n-1-k\). This chord is isolated if and only if all remaining pairs lie wholly within one of these two arcs. There are exactly \(M_kM_r\) such matchings, out of \(M_n\) uniformly possible matchings. Under this conditioning, the two arc matchings are independent and uniform; no chord in one arc crosses a chord in the other arc. Consequently
\[
\mathbb E[X_n\mid \text{distinguished chord isolated and arc size }2k]
=\frac{k(k-1)+r(r-1)}6.
\]
There is one eligible partner of endpoint \(1\) for every integer \(k\in\{0,\ldots,n-1\}\). Every diagram with \(I_n\) isolated chords has \(2I_n\) endpoints belonging to isolated chords, so rotational symmetry gives the exact rooted expectation identity
\[
\mathbb E[I_nX_n]
=n\sum_{k=0}^{n-1}\frac{M_kM_r}{M_n}
\frac{k(k-1)+r(r-1)}6,
\qquad
\mathbb E I_n=\frac{n}{M_n}\sum_{k=0}^{n-1}M_kM_r.
\]
Subtract the product of the means. Since \(k+r=n-1\),
\[
\frac{k(k-1)+r(r-1)-n(n-1)}6
=-\frac{(n-1)+kr}{3}.
\]
Substitution proves the boxed covariance identity; each summand is positive before the minus sign, so the sign is strict for every \(n\ge2\).

**3. Separate simple and non-simple isolates.** The distinguished isolated chord is simple precisely for \(k=0\) or \(k=n-1\). The corresponding two terms yield
\[
\mathbb E S_n=\frac{2n}{2n-1},\qquad
\operatorname{Cov}(S_n,X_n)=-\frac{2n(n-1)}{3(2n-1)}.
\]
Subtracting the endpoint terms of the general formula leaves positive summands for \(1\le k\le n-2\), establishing strict negativity of \(\operatorname{Cov}(I_n-S_n,X_n)\) for \(n\ge3\); for \(n=2\) the residual sum is empty.

**4. First non-simple layer and the tail.** For \(n\ge4\), the terms \(k=1\) and \(k=n-2\) contribute exactly
\[
\mathbb E(I_n-S_n)=\frac{2n}{(2n-1)(2n-3)}+R_n^{(E)},\qquad
\operatorname{Cov}(I_n-S_n,X_n)
=-\frac{2n}{3(2n-1)}-R_n^{(C)},
\]
where the two remainders collect \(2\le k\le n-3\) and are nonnegative. To bound them, define
\[
a_{n,k}=\frac{M_kM_{n-1-k}}{M_n},\quad
\frac{a_{n,k+1}}{a_{n,k}}=\frac{2k+1}{2n-3-2k},\quad
 a_{n,2}=\frac{3}{(2n-1)(2n-3)(2n-5)}=O(n^{-3}).
\]
By symmetry it suffices to consider \(2\le k\le\lfloor(n-1)/2\rfloor\). For sufficiently large \(n\) and \(k\le\lfloor n/4\rfloor\), the displayed ratio is at most \(1/2\), hence the weighted sum \(\sum(1+k)a_{n,k}\) over this range is \(O(a_{n,2})\). Up to the midpoint the sequence \(a_{n,k}\) is nonincreasing, so on the remaining interval it is bounded by \(a_{n,2}2^{-\lfloor n/4\rfloor+2}\); its polynomially weighted sum is likewise \(O(a_{n,2})\). Thus
\[
\sum_{k=2}^{n-3}a_{n,k}=O(n^{-3}),\qquad
\sum_{k=2}^{n-3}\bigl[n-1+k(n-1-k)\bigr]a_{n,k}=O(n^{-2}).
\]
(The finitely many small \(n\) only alter constants.) Multiplying by the prefactor \(n\) in the expectations and covariance gives \(R_n^{(E)}=O(n^{-2})\) and \(R_n^{(C)}=O(n^{-1})\). The two limit formulas follow. Finally, expanding the simple-chord term gives \(\operatorname{Cov}(S_n,X_n)=-n/3+1/6+O(n^{-1})\), and adding the non-simple correction proves \(\operatorname{Cov}(I_n,X_n)=-n/3-1/6+O(n^{-1})\).

## Verification

Run \(\texttt{python3 verify.py}\) with an ordinary Python 3 interpreter. The standalone script enumerates every labeled matching for \(2\le n\le7\) and computes its crossing count, isolated count, and circular-adjacency count directly, without using the conditional arc formula. It verifies all three expectations and the two exact covariances using exact rational arithmetic, and checks the distinguished-chord conditional crossing means for each even arc split. It enumerates \(146598\) matchings and checks \(27\) conditional arc-size cases. It separately checks \(499\) higher-size instances of exact sign and decomposition identities for \(2\le n\le500\). These finite computations are consistency checks, not the proof for all \(n\); that is the preceding argument.

## Relationship to prior work

Flajolet and Noy [1] give generating-function descriptions of component count and moments of the total crossing count separately, including the exact crossing mean. Acan [2] studies chord degree, simple chords, isolation asymptotics, monolithic diagrams, and the intersection graph in the same uniform-matching model; the inspected sections do not formulate the mixed isolated-vertex/crossing-edge covariance. Paguyo [3] obtains convergence rates for crossings and for *simple chords*, rather than mixed moments with all degree-zero vertices. The connected-crossing count table [4] records crossings among connected diagrams, not this two-observable joint moment. The identity for simple chords does not determine the present result because non-simple isolates contribute an additional covariance approaching \(-1/3\) even though their expectation is \(O(1/n)\).

## Limitations

The result is for a uniform perfect matching on labeled circular endpoints, not arbitrary random circle graphs, nonuniform chord models, or the conditional fixed-crossing model. The asymptotic remainder is an order bound, not an independently proved full expansion. A broad search and inspection of the closest sources did not locate the stated mixed-moment identity, but unindexed older joint generating functions, tables, or equivalent formulations remain a possible prior-art risk.

## References

[1] P. Flajolet and M. Noy, *Analytic Combinatorics of Chord Diagrams*, INRIA Research Report 3914 (March 2000), author-hosted full text: https://algo.inria.fr/flajolet/Publications/FlNo00.pdf .

[2] H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (first public submission 2015-01-07), full text: https://arxiv.org/html/1501.01489v1 . Its original manuscript identifies primary MSC 60C05.

[3] J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, full text: https://arxiv.org/html/2104.01134v2 .

[4] OEIS A322456, *Triangle of Touchard's chord enumerating polynomial coefficients*: https://oeis.org/A322456 .
