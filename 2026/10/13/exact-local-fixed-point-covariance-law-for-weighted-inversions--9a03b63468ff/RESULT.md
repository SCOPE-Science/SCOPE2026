# Exact local fixed-point covariance law for weighted inversions
## Finding
Let \(\Pi\) be uniform on \(S_n\), with \(n\ge2\). For each position \(i\), define the fixed-point indicator
\[
F_i=\mathbf 1\{\Pi(i)=i\}.
\]
For deterministic real weights \(w_{ab}\), \(1\le a<b\le n\), define the weighted inversion score
\[
T_w=\sum_{1\le a<b\le n}w_{ab}\mathbf 1\{\Pi(a)>\Pi(b)\}.
\]
Write
\[
L_i=\sum_{a<i}w_{ai},
\qquad
R_i=\sum_{b>i}w_{ib}.
\]
Then the exact local covariance is
\[
\boxed{
\operatorname{Cov}(F_i,T_w)
=
\frac{n+1-2i}{2n(n-1)}(L_i-R_i).
}
\]
Equivalently,
\[
\boxed{
\mathbb E[T_w\mid \Pi(i)=i]-\mathbb ET_w
=
\frac{n+1-2i}{2(n-1)}(L_i-R_i).
}
\]
Thus fixing one position affects every weighted inversion score only through the imbalance between weights incident to that position from the left and from the right.

For the ordinary inversion count
\[
I_n=\sum_{a<b}\mathbf 1\{\Pi(a)>\Pi(b)\},
\]
one has \(L_i=i-1\) and \(R_i=n-i\), and therefore
\[
\boxed{
\operatorname{Cov}(F_i,I_n)
=
-\frac{(n+1-2i)^2}{2n(n-1)}.
}
\]
The corresponding conditional mean is
\[
\boxed{
\mathbb E[I_n\mid \Pi(i)=i]
=
\frac{n(n-1)}4
-
\frac{(n+1-2i)^2}{2(n-1)}.
}
\]
The profile is an exact negative parabola in the fixed-point position. When \(n\) is odd, fixing the central position \(i=(n+1)/2\) leaves the ordinary inversion mean unchanged.

More generally, at this central position the prefactor \(n+1-2i\) vanishes, so every weighted inversion score has zero covariance with the central fixed-point indicator, regardless of its weights.

Let
\[
F_n=\sum_{i=1}^nF_i
\]
be the total number of fixed points. Summing the local law gives
\[
\boxed{
\operatorname{Cov}(F_n,I_n)
=
-\frac{n+1}{6}.
}
\]
For \(n\ge2\),
\[
\operatorname{Var}(F_n)=1
\]
and
\[
\operatorname{Var}(I_n)=\frac{n(n-1)(2n+5)}{72},
\]
hence
\[
\boxed{
\operatorname{Corr}(F_n,I_n)
=
-\frac{\sqrt2(n+1)}
{\sqrt{n(n-1)(2n+5)}}.
}
\]
In particular,
\[
\operatorname{Corr}(F_n,I_n)\sim-\frac1{\sqrt n}.
\]

## Assumptions and scope
The permutation is uniform on \(S_n\). The weights \(w_{ab}\) are deterministic real numbers attached to ordered position pairs with \(a<b\).

The result is finite-sample and exact for every \(n\ge2\). It concerns covariance and conditional means, not independence. A zero covariance at the central position does not imply that the corresponding random variables are independent.

The aggregate formulas for \(F_n\) and \(I_n\) are corollaries of the local weighted theorem. The principal claim is the position-resolved law for arbitrary deterministic pair weights.

## Proof
For every pair \(a<b\),
\[
\mathbb P(\Pi(a)>\Pi(b))=\frac12,
\]
so
\[
\mathbb ET_w=\frac12\sum_{a<b}w_{ab}.
\]

Fix \(i\) and condition on \(\Pi(i)=i\). The remaining \(n-1\) values are a uniformly random bijection from
\[
[n]\setminus\{i\}
\]
to the remaining positions.

If \(a<b\) and neither endpoint equals \(i\), the two remaining values at \(a\) and \(b\) are exchangeable. Therefore
\[
\mathbb P(\Pi(a)>\Pi(b)\mid \Pi(i)=i)=\frac12.
\]
Such pairs produce no conditional shift.

For \(a<i\),
\[
\mathbb P(\Pi(a)>\Pi(i)\mid \Pi(i)=i)
=
\mathbb P(\Pi(a)>i\mid \Pi(i)=i)
=
\frac{n-i}{n-1}.
\]
Its deviation from \(1/2\) is
\[
\frac{n+1-2i}{2(n-1)}.
\]
For \(i<b\),
\[
\mathbb P(\Pi(i)>\Pi(b)\mid \Pi(i)=i)
=
\mathbb P(i>\Pi(b)\mid \Pi(i)=i)
=
\frac{i-1}{n-1},
\]
whose deviation from \(1/2\) is
\[
-\frac{n+1-2i}{2(n-1)}.
\]
Summing the incident pairs yields
\[
\mathbb E[T_w\mid \Pi(i)=i]-\mathbb ET_w
=
\frac{n+1-2i}{2(n-1)}(L_i-R_i).
\]
Because
\[
\mathbb P(\Pi(i)=i)=\frac1n,
\]
the identity
\[
\operatorname{Cov}(\mathbf1_A,X)
=
\mathbb P(A)\bigl(\mathbb E[X\mid A]-\mathbb EX\bigr)
\]
gives the stated covariance law.

For ordinary inversions all pair weights equal one, so
\[
L_i-R_i=(i-1)-(n-i)=2i-n-1=-(n+1-2i).
\]
This proves the local parabolic formula.

Finally,
\[
\sum_{i=1}^n(n+1-2i)^2=\frac{n(n^2-1)}3,
\]
so summing over \(i\) gives
\[
\operatorname{Cov}(F_n,I_n)
=
-\frac{n+1}{6}.
\]
The fixed-point count satisfies
\[
\mathbb EF_n=1,
\qquad
\mathbb E[F_n(F_n-1)]=1,
\]
and hence \(\operatorname{Var}(F_n)=1\) for \(n\ge2\). Combining this with the classical inversion variance
\[
\operatorname{Var}(I_n)=\frac{n(n-1)(2n+5)}{72}
\]
gives the correlation formula.

## Verification
The accompanying `checker.py` exhaustively enumerates all permutations through \(n=9\). It verifies the ordinary local covariance and conditional-mean formulas at every position, checks the aggregate fixed-point/inversion covariance, and independently checks the weighted theorem for three deterministic nonconstant weight systems.

The exhaustive checks are finite consistency tests. The proof above establishes the result for every \(n\ge2\) and arbitrary deterministic real weights.

## Relationship to prior work
Hultman's work treats inversion number and several cycle statistics through conjugacy-class averaging, giving a broad representation-theoretic framework for expectations of permutation statistics. It does not formulate conditioning on a specified fixed position.

Diaconis, Evans, and Graham study the random set of fixed points itself and identify another random set with the same distribution. Their paper places fixed-point-set questions squarely in random-permutation probability and is classified under MSC \(60C05\).

Pinsky gives the closest direct comparison: exact inversion expectations and pair-order probabilities for permutations conditioned to have exactly \(k\) fixed points. That conditioning fixes only the number of fixed points, not their locations. The local event \(\Pi(i)=i\), the position-resolved parabolic effect, and the arbitrary weighted inversion law are not stated in the inspected theorem statements or searched full text.

The aggregate covariance
\[
\operatorname{Cov}(F_n,I_n)=-(n+1)/6
\]
should be viewed as a corollary of the local law rather than as the sole originality claim.

## Limitations
The argument uses uniformity of the permutation. Under conjugacy-class conditioning, Mallows weighting, pattern avoidance, or other nonuniform laws, pairs not incident to \(i\) need not remain unbiased after conditioning on a fixed position.

The theorem controls first conditional moments and covariance only. It does not determine the conditional distribution of the inversion score.

Recent work on inversion number under a prescribed fixed-point count is very close in subject matter, and older joint-enumeration literature may contain an equivalent aggregate identity. The principal residual originality risk is therefore an older or differently parameterized statement of the local fixed-position formula.

## References
1. A. Hultman, “Permutation statistics of products of random permutations,” arXiv:1301.0430, first submitted 3 January 2013.
2. P. Diaconis, S. N. Evans, and R. Graham, “Unseparated pairs and fixed points in random permutations,” arXiv:1308.5459, first submitted 25 August 2013.
3. R. G. Pinsky, “The inversion statistic in derangements and in other permutations with a prescribed number of fixed points,” arXiv:2505.02058; *The Electronic Journal of Combinatorics* 33 (2026), #P2.36, DOI: 10.37236/14250.
