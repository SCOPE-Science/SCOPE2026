# A finite-size sign reversal between loops and parallel-edge pairs in random configurations

## Finding

Let \(d_1,\ldots,d_m\) be nonnegative integers whose sum \(q\) is even and at least \(6\). Put \(q\) distinguishable half-edges in \(m\) prescribed groups of sizes \(d_i\), and choose a perfect matching of the half-edges uniformly. A pair matched within one group is a loop; let \(L\) count all loops. If \(M_{ij}\) is the number of matched pairs joining distinct groups \(i\) and \(j\), let \(P=\sum_{i<j}\binom{M_{ij}}2\) count pairs of parallel edges, so a triple edge contributes three.

Define
\[
 a_i=\binom{d_i}{2},\quad S=\sum_i a_i,\quad
 B=2\sum_{i<j}a_i a_j,\quad
 T=2\sum_{i<j}a_i a_j\bigl((2d_i-3)+(2d_j-3)\bigr).
\]
Then the **exact finite-size covariance identity** is
\[
 \operatorname{Cov}(L,P)=
 \frac{4BS-(q-1)T}{(q-1)^2(q-3)(q-5)}.
\]
Terms in \(T\) having \(d_i<2\) or \(d_j<2\) vanish because of the factors \(a_i a_j\).

In particular, for \(m=v\ge2\) groups each containing \(r\ge2\) half-edges, where \(vr\) is even, let \(a=\binom r2\). Whenever \(vr\ge6\),
\[
 \boxed{\operatorname{Cov}(L,P)=
 \frac{2v(v-1)a^2\bigl(vr(2-r)+2r-3\bigr)}
 {(vr-1)^2(vr-3)(vr-5)}.}
\]
Thus the covariance is **strictly positive** for \(r=2\), \(v\ge3\), and **strictly negative** for every \(r\ge3\), \(v\ge2\) with \(vr\) even. The unique regular case excluded by \(vr\ge6\), namely \((v,r)=(2,2)\), has covariance \(-4/9\). For fixed \(r\),
\[
 \operatorname{Cov}(L,P)\sim
 \begin{cases}
 (8v^2)^{-1},&r=2,\\[2pt]
 -\dfrac{(r-1)^2(r-2)}{2rv},&r\ge3.
 \end{cases}
\]
The positive degree-two covariance therefore decays one power of \(v\) faster than the negative covariance at each fixed higher degree.

## Assumptions and scope

The matching is **uniform on labeled half-edge pairings**, not uniform on unlabeled multigraphs. Loops count once, and parallel-edge pairs count with multiplicity \(\binom{M_{ij}}2\). No simplicity or connectivity conditioning is imposed. The general covariance formula holds for every nonnegative degree profile of even total \(q\ge6\), including zeros and ones. The sharp sign statement applies only to equal degrees \(r\ge2\), with \(v\ge2\), \(vr\) even. Degenerate groups of degree zero or one give no local loop or doubled-edge witnesses.

## Proof

For any prescribed collection of \(k\) disjoint pairs of labeled half-edges, the probability that all pairs appear in a uniform matching on \(q\) points is
\[
 \frac{1}{(q-1)(q-3)\cdots(q-2k+1)}.
\]
Indeed, reveal the partners of the \(k\) chosen first endpoints successively; each specified partner has reciprocal probability equal to the current number of remaining choices. Consequently the expectation of the loop count is
\[
 \mathbb E L=\frac{S}{q-1}.
\]
For an unordered pair of distinct groups \(i<j\), choose two half-edges in group \(i\) and two in group \(j\); there are exactly two ways to match the chosen four half-edges across the groups. These witnesses each have probability \(1/((q-1)(q-3))\). The sum of their indicators equals \(\binom{M_{ij}}2\), even when more than two edges are parallel. Summing yields
\[
 \mathbb E P=\frac{B}{(q-1)(q-3)}.
\]

To compute \(\mathbb E(LP)\), fix one specified double-edge witness between \(i\) and \(j\). A loop witness compatible with it must use two half-edges outside its four specified half-edges. For the two involved groups, the remaining numbers of loop witnesses are \(\binom{d_i-2}2\) and \(\binom{d_j-2}2\), respectively; the witness count elsewhere is unchanged. Therefore its total compatible loop-witness count is
\[
 S-\left(\binom{d_i}2-\binom{d_i-2}2\right)
  -\left(\binom{d_j}2-\binom{d_j-2}2\right)
 =S-(2d_i-3)-(2d_j-3).
\]
This calculation only arises for \(d_i,d_j\ge2\). A compatible loop witness and double-edge witness prescribe three disjoint matching pairs, of joint probability \(1/((q-1)(q-3)(q-5))\). Incompatible pairs have joint probability zero. Summing over the \(2a_i a_j\) double-edge witnesses for each pair of groups gives
\[
 \mathbb E(LP)=\frac{BS-T}{(q-1)(q-3)(q-5)}.
\]
Subtracting \(\mathbb E L\,\mathbb E P\), with a common denominator, proves the first claimed covariance identity:
\[
 \operatorname{Cov}(L,P)
 =\frac{(q-1)(BS-T)-(q-5)BS}
 {(q-1)^2(q-3)(q-5)}
 =\frac{4BS-(q-1)T}{(q-1)^2(q-3)(q-5)}.
\]

For regular degrees, \(S=va\), \(B=v(v-1)a^2\), and \(T=2v(v-1)a^2(2r-3)\). Substitution simplifies the numerator to
\[
 2v(v-1)a^2\bigl(vr(2-r)+(2r-3)\bigr),
\]
giving the displayed formula. At \(r=2\) the parenthesized factor is \(1\). At \(r\ge3\), \(vr(r-2)\ge2r(r-2)>2r-3\), so the factor is strictly negative. All denominators are positive for \(vr\ge6\), proving the sign classification.

For the exceptional \((v,r)=(2,2)\), of the three perfect matchings, one has two loops and no parallel-edge pair, and two have one parallel-edge pair and no loop. Thus \(\mathbb E L=\mathbb E P=2/3\), \(\mathbb E(LP)=0\), and the covariance is \(-4/9\). Finally, expanding the exact formula at fixed \(r\) proves both asserted asymptotics.

## Verification

The standalone `verify.py` enumerates all labeled pairings for all \(701\) weak degree compositions of half-edge totals \(6\), \(8\), and \(10\) into \(2\), \(3\), or \(4\) groups. Exact rational moments are compared to the three independently expressed analytic moment formulas, followed by regular-case formula and sign checks and the exceptional four-half-edge case. It reports `PASS: 2223 exact moment/formula/sign assertions`. Run `python verify.py` from the extracted package directory. These finite checks are consistency tests; the proof above, not enumeration, establishes the result for arbitrary sizes.

## Relationship to prior work

Short-cycle counts in the configuration/pairing model have long been studied. Wormald's survey describes Bollobás's asymptotic independence theorem for the counts of loops and pairs of multiple edges (Theorem 2.6). Janson (2006), Section 7, establishes a corresponding asymptotic independent-Poisson statement for prescribed degree sequences. Angel, van der Hofstad, and Holmgren (2016), Theorem 1.4 and Section 3, refine this with total-variation bounds and analysis of compatible versus incompatible indicator pairs. Those limit laws do not determine the sign of a vanishing finite covariance; the present result evaluates that finite covariance exactly and classifies the opposite signs throughout the regular family. The finite regular sign law is not stated in the inspected primary results; publication-priority confirmation remains open.

## Limitations

The sign for arbitrary irregular degree profiles is not classified; the general identity is the complete result offered for those profiles. Only labeled-pairing configurations, not uniform multigraphs or simple graphs, are covered. The asymptotic laws assume fixed \(r\) and admissible numbers of vertices. A relevant prior work may implicitly contain this sign classification via further algebra; the literature comparison is not an independent novelty certification.

## References

1. N. C. Wormald, *Models of Random Regular Graphs*, Surveys in Combinatorics (1999), Section 2.3, Theorem 2.6 and Section 2.4. https://users.monash.edu.au/~nwormald/papers/regsurvey.pdf
2. S. Janson, *The Probability That a Random Multigraph Is Simple*, arXiv:math/0609802v1 (first submitted September 28, 2006), Sections 2 and 7. https://arxiv.org/abs/math/0609802
3. O. Angel, R. van der Hofstad, and C. Holmgren, *Limit Laws for Self-Loops and Multiple Edges in the Configuration Model*, arXiv:1603.07172v1 (first submitted March 23, 2016), Theorem 1.4 and Section 3. https://arxiv.org/abs/1603.07172
