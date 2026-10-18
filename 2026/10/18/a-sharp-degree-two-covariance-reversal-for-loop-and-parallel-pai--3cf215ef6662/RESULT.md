# A sharp degree-two covariance reversal for loop and parallel-pair defects in random configurations

## Finding

Let \(d_1,\ldots,d_v\) be nonnegative integers with even total \(N=\sum_i d_i\geq6\). Attach \(d_i\) labeled half-edges to vertex \(i\), pair all \(N\) half-edges uniformly at random, and retain loops and parallel edges. Let \(L\) denote the total number of loops. If \(X_{ij}\) is the edge multiplicity between distinct vertices, define the *parallel-pair defect count* \(P=\sum_{i<j}\binom{X_{ij}}2\). In particular, a triple edge contributes three to \(P\).

Put \(a_i=\binom{d_i}2\), \(S=\sum_i a_i\), \(B=2\sum_{i<j}a_i a_j\), and \(T=4\sum_{i<j}a_i a_j(d_i+d_j-3)\). Then the exact covariance for every such degree sequence is

\[
\operatorname{Cov}(L,P)=\frac{4SB-(N-1)T}{(N-1)^2(N-3)(N-5)}.
\]

For a regular degree sequence \(d_i=d\) on \(v\geq2\) vertices with even \(vd\geq6\), the formula becomes

\[
\operatorname{Cov}(L,P)=\frac{2v(v-1)\binom d2^2\,[vd(2-d)+2d-3]}{(vd-1)^2(vd-3)(vd-5)}.
\]

The covariance is **strictly positive at degree \(d=2\)** whenever \(v\geq3\), but **strictly negative for every degree \(d\geq3\)** whenever \(v\geq2\) and \(vd\) is even. The regular case \((v,d)=(2,2)\), excluded by \(N\geq6\), has covariance \(-4/9\).

At fixed degree, the two signs have different asymptotic scales:

\[
\operatorname{Cov}(L,P)\sim \frac1{8v^2}\quad(d=2),\qquad
v\operatorname{Cov}(L,P)\longrightarrow-\frac{(d-1)^2(d-2)}{2d}\quad(d\geq3).
\]

Thus the first nonzero finite-size covariance has a sharp degree-two sign and rate transition, although the two defect statistics have asymptotically independent Poisson limits in the bounded-degree configuration model.

## Assumptions and scope

The probability distribution is uniform on perfect matchings of *distinguishable half-edges*, not uniform on multigraphs with the prescribed degrees. Loops consume two stubs at the same vertex, and \(P\) counts unordered pairs of distinct edges between each unordered pair of different vertices. The general identity requires an even total of at least six half-edges; zero degrees are permitted. The regular classification assumes \(d\geq2\). If there is only one vertex, or fewer than two vertices supporting at least two half-edges, then \(P=0\) deterministically.

## Proof

For each vertex \(i\), there are \(a_i\) possible pairs of its half-edges that could become loops. Therefore \(L\) is a sum of \(S\) two-stub indicators. For each unordered pair \(i<j\), choose two stubs at each endpoint and select one of the two possible cross-pairings. This gives \(2a_i a_j\) four-stub indicators for the parallel-pair count. Consequently \(P\) is a sum of \(B\) four-stub indicators. A specified pair appears in a uniform pairing with probability \(1/(N-1)\), and a specified pair of disjoint edges with probability \(1/[(N-1)(N-3)]\). It follows that

\[
\mathbb E L=\frac{S}{N-1},\qquad
\mathbb E P=\frac{B}{(N-1)(N-3)}.
\]

Consider a given parallel-pair indicator using two half-edges at each of vertices \(i\) and \(j\). The loop-pair indicators that share at least one of these four stubs number

\[
\left[\binom{d_i}2-\binom{d_i-2}2\right]
+\left[\binom{d_j}2-\binom{d_j-2}2\right]
=2(d_i+d_j-3).
\]

This expression is used only for vertices having at least two stubs. Including all \(2a_i a_j\) possible parallel pairings, the total number of incompatible (loop, parallel-pair) indicator pairs is exactly \(T\). The remaining \(SB-T\) pairs involve six different half-edges and occur together with probability \(1/[(N-1)(N-3)(N-5)]\). Thus

\[
\mathbb E(LP)=\frac{SB-T}{(N-1)(N-3)(N-5)}.
\]

Subtracting \(\mathbb E L\,\mathbb E P\), and bringing terms to a common denominator, gives the stated general formula.

For a regular sequence, \(S=v\binom d2\), \(B=v(v-1)\binom d2^2\), and \(T=(4d-6)B\). Substitution gives the claimed rational expression. Its denominator and prefactor are positive. At \(d=2\), the remaining sign factor \(vd(2-d)+2d-3\) is exactly one. For \(d\geq3\), it is \(-vd(d-2)+2d-3<0\): since \(v\geq2\), its negative term has magnitude at least \(2d(d-2)>2d-3\). This proves the complete regular sign classification. For \(v=2,d=2\), there are three stub pairings: one yields two loops and no parallel pair, and two yield one parallel pair and no loop. Direct evaluation gives \(-4/9\).

At \(d=2\), the rational formula simplifies exactly to

\[
\operatorname{Cov}(L,P)=\frac{2v(v-1)}{(2v-1)^2(2v-3)(2v-5)},
\]

whose leading term is \(1/(8v^2)\). For each fixed \(d\geq3\), comparing the leading-degree numerator and denominator gives the stated limit of \(v\operatorname{Cov}(L,P)\). No interchange of probabilistic limits is needed.

## Verification

The included `verify.py` performs direct enumeration of every perfect matching for multiple irregular and regular small degree sequences, compares exact rational covariances to the closed formula, and checks the regular sign factor for a range of dimensions and degrees. It checks the special four-stub exception directly and compares the asymptotic limits numerically at a specified large sample size. All finite comparisons use exact rational arithmetic. The analytic proof above establishes the unrestricted results; enumeration alone would not do so.

## Relationship to prior work

Janson, *The probability that a random multigraph is simple* (first posted September 28, 2006), develops the configuration model and asymptotic simplicity criteria; Janson's 2013 sequel develops mixed moment methods for the combined simplicity-defect count. Angel, van der Hofstad, and Holmgren, *Limit laws for self-loops and multiple edges in the configuration model* (first posted March 23, 2016), study **exactly** the two statistics \(L\) and \(P\) under other notation and prove Poisson approximation and asymptotic independence. In particular, their equations (1.2) and (1.6) define the statistics and evaluate their separate means. The present all-degree-sequence finite covariance formula and its strictly opposite regular-degree signs are not asserted as new Poisson limits or as a new configuration model. The evaluated degree-two sign/rate threshold is the contribution under consideration.

## Limitations

The theorem concerns the unconditioned stub-pairing model; after conditioning on simplicity, both defect counts vanish. It does not claim independence, bounds for arbitrary nonlinear observables, or a universal sign for irregular degree sequences. It distinguishes the parallel-pair statistic from the count of vertex pairs having multiplicity at least two. Source comparisons establish no direct matching finite sign classification in the inspected articles, but they do not prove global historical uniqueness: an implicit deduction from older enumerative formulas or a less obvious published identity remains possible. This is a self-review, not independent validation.

## References

1. S. Janson, *The probability that a random multigraph is simple*, arXiv:math/0609802, first posted 2006-09-28, https://arxiv.org/abs/math/0609802.
2. S. Janson, *The probability that a random multigraph is simple, II*, arXiv:1307.6344, first posted 2013-07-24, https://arxiv.org/abs/1307.6344.
3. O. Angel, R. van der Hofstad, C. Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172, first posted 2016-03-23, https://arxiv.org/abs/1603.07172.
