# Squared root imbalance has an exact cubic covariance with random-BST path length

## Finding

Let \(\mathcal B_n\) be the binary search tree obtained by inserting a uniformly random permutation of \(n\ge2\) distinct keys. Let
\[
I_n
\]
be the number of keys in the root's left subtree, and let
\[
P_n
\]
be the internal path length, the sum of all root-to-node depths. Equivalently, \(P_n\) has the distribution of the number of key comparisons made by standard Quicksort with a uniformly random first pivot and recursive random pivots.

Define the squared root imbalance
\[
Q_n=\bigl(2I_n-(n-1)\bigr)^2.
\]

Write
\[
H_k=\sum_{j=1}^k\frac1j,
\qquad
H_k^{(2)}=\sum_{j=1}^k\frac1{j^2},
\]
with \(H_0=0\). The classical mean path length is
\[
\mu_k=\mathbb E P_k=2(k+1)H_k-4k.
\]

The first split gives the exact conditional regression
\[
\boxed{
\mathbb E[P_n\mid I_n=i]
=
\mu_i+\mu_{n-1-i}+n-1,
\qquad
0\le i\le n-1.
}
\tag{1}
\]

For \(n\ge3\), the right-hand side is a strictly increasing function of \(Q_n\) on the support of \(Q_n\). Consequently, for every nondecreasing nonconstant function \(f\) on that support,
\[
\boxed{
\operatorname{Cov}\!\bigl(f(Q_n),P_n\bigr)>0.
}
\tag{2}
\]

In particular, the quadratic imbalance has the exact covariance
\[
\boxed{
\operatorname{Cov}(Q_n,P_n)
=
\frac{(n-2)(n-1)(n+1)}9.
}
\tag{3}
\]

Its variance is
\[
\boxed{
\operatorname{Var}(Q_n)
=
\frac{4(n-2)(n-1)(n+1)(n+2)}{45}.
}
\tag{4}
\]
Hence the least-squares slope in the regression of \(P_n\) on \(Q_n\) is especially simple:
\[
\boxed{
\beta_n
=
\frac{\operatorname{Cov}(Q_n,P_n)}{\operatorname{Var}(Q_n)}
=
\frac5{4(n+2)}.
}
\tag{5}
\]

The classical exact variance of the internal path length is
\[
V_n
=
7n^2+13n
-
2(n+1)H_n
-
4(n+1)^2H_n^{(2)}.
\tag{6}
\]
Therefore
\[
\boxed{
\operatorname{Corr}(Q_n,P_n)
=
\frac{\sqrt5}{6}
\sqrt{
\frac{(n-2)(n-1)(n+1)}
{(n+2)V_n}
}.
}
\tag{7}
\]

Since
\[
\frac{V_n}{n^2}
\longrightarrow
7-\frac{2\pi^2}{3},
\]
the correlation has a nonzero limit:
\[
\boxed{
\operatorname{Corr}(Q_n,P_n)
\longrightarrow
\frac{\sqrt5}
{6\sqrt{7-2\pi^2/3}}
\approx0.5748741694.
}
\tag{8}
\]

Equivalently, the fraction of path-length variance explained by the best linear predictor using only the squared imbalance of the root split converges to
\[
\boxed{
\frac5{36(7-2\pi^2/3)}
\approx0.3304803106.
}
\tag{9}
\]

Thus the first pivot is not washed out by the later recursive splits: its squared rank imbalance alone retains about one third of the eventual Quicksort-comparison variance in linear prediction.

## Assumptions and scope

The random tree is the standard random-permutation binary search tree. Conditional on \(I_n=i\), the left and right subtrees are independent random BSTs of sizes \(i\) and \(n-1-i\).

The path length \(P_n\) counts edges from the root, so the root has depth zero. With this convention it is distributionally identical to the standard Quicksort comparison count.

The statistic \(Q_n\) is a quadratic measure of the first split only. Equation (2) is a regression-mean statement; it does not claim stochastic ordering of the entire conditional laws of \(P_n\).

For \(n=2\), \(Q_n\) is constant and the covariance is zero. The strict statements begin at \(n=3\).

## Proof

The rank of the first inserted key is uniform on \(\{1,\ldots,n\}\), so
\[
I_n\sim\operatorname{Unif}\{0,\ldots,n-1\}.
\tag{10}
\]
Put
\[
N=n-1.
\]

Conditional on \(I_n=i\), the two recursive subtrees are independent random BSTs of sizes \(i\) and \(N-i\), and every subtree node is one level deeper than it is inside its own subtree. Therefore
\[
P_n
\overset d=
P_i+P'_{N-i}+N,
\]
conditionally on \(I_n=i\), and taking means gives (1).

The classical mean formula implies
\[
\mu_{k+1}-\mu_k
=
2(H_{k+1}-1).
\tag{11}
\]
Let
\[
m_n(i)=\mu_i+\mu_{N-i}+N.
\]
Then
\[
m_n(i)=m_n(N-i),
\]
and, whenever \(i\ge N/2\) and \(i<N\),
\[
\begin{aligned}
m_n(i+1)-m_n(i)
&=
2(H_{i+1}-1)-2(H_{N-i}-1)\\
&=
2(H_{i+1}-H_{N-i})\\
&>0.
\end{aligned}
\tag{12}
\]
Thus \(m_n(I_n)\) is a strictly increasing function of
\[
Q_n=(2I_n-N)^2
\]
on the distinct values in the support. Because
\[
\mathbb E[P_n\mid Q_n]=m_n(I_n),
\]
with the right-hand side well defined by the symmetry \(i\leftrightarrow N-i\), equation (2) follows from
\[
\operatorname{Cov}(f(Q_n),P_n)
=
\operatorname{Cov}\!\left(f(Q_n),\mathbb E[P_n\mid Q_n]\right)
\]
and the elementary fact that two nonconstant increasing functions of the same nondegenerate finite random variable have positive covariance.

For the exact covariance, write
\[
q_i=(2i-N)^2.
\]
Symmetry gives
\[
\operatorname{Cov}(Q_n,P_n)
=
2\operatorname{Cov}(q_{I_n},\mu_{I_n}).
\tag{13}
\]
Elementary power sums give
\[
\frac1{N+1}\sum_{i=0}^Nq_i
=
\frac{N(N+2)}3.
\tag{14}
\]
Using
\[
\mu_i=2(i+1)H_i-4i
\]
and the standard finite harmonic-sum identities
\[
\sum_{i=1}^N H_i=(N+1)H_N-N,
\]
\[
\sum_{i=1}^N iH_i
=
\frac{N(N+1)}2H_N-\frac{N(N-1)}4,
\]
\[
\sum_{i=1}^N i^2H_i
=
\frac{N(N+1)(2N+1)}6H_N
+
\frac{N(-4N^2+3N+1)}{36},
\]
and
\[
\sum_{i=1}^N i^3H_i
=
\frac{N^2(N+1)^2}{4}H_N
+
\frac{N(N+1)(-3N^2+5N-2)}{48},
\]
one obtains
\[
\sum_{i=0}^N\mu_i
=
(N+1)(N+2)H_N-\frac{N(5N+7)}2,
\tag{15}
\]
and
\[
\sum_{i=0}^Nq_i\mu_i
=
\frac{N(N+2)}{18}
\left(
6(N+1)(N+2)H_N
-
14N^2-21N-1
\right).
\tag{16}
\]
Substitution of (14)--(16) into (13) cancels every harmonic term and yields
\[
\operatorname{Cov}(Q_n,P_n)
=
\frac{N(N-1)(N+2)}9,
\]
which is (3).

Similarly,
\[
\mathbb E Q_n^2
=
\frac{N(N+2)(3N^2+6N-4)}{15}.
\]
Together with (14), this gives
\[
\operatorname{Var}(Q_n)
=
\frac{4N(N-1)(N+2)(N+3)}{45},
\]
equivalent to (4). Division proves (5).

The variance formula (6) is the classical random-BST path-length variance. Combining (3), (4), and (6) gives (7). Finally,
\[
H_n^{(2)}\to\frac{\pi^2}{6},
\qquad
\frac{H_n}{n}\to0,
\]
so
\[
V_n/n^2\to7-2\pi^2/3.
\]
This proves (8), and squaring (8) proves (9).

## Verification

The accompanying checker exhaustively enumerates every insertion permutation through \(n=9\).

For each permutation it reconstructs the first-pivot rank and the complete Quicksort comparison count. It verifies the conditional mean formula, strict monotonicity of the conditional mean across the support of \(Q_n\), the exact covariance (3), the imbalance variance (4), the least-squares slope (5), and the classical path-length mean and variance.

A separate exact-rational loop verifies the harmonic-sum reduction used in (15)--(16) through hundreds of sizes, and a high-\(n\) numerical check confirms convergence of (7) to the constant in (8).

Finite enumeration is supplementary. The all-\(n\) result is proved by the root decomposition and the harmonic identities above.

## Relationship to prior work

Prodinger gives a full treatment of the random-BST path length, beginning from the recursive identity
\[
P(t)=P(t_L)+P(t_R)+|t_L|+|t_R|,
\]
and recovers the classical exact expectation and variance used here. The inspected full paper does not retain the root split size as a joint statistic and does not state a covariance or regression with root imbalance.

Drmota and Hwang study covariance and correlation phenomena for random-BST level profiles. Their full public text defines the random-permutation BST, develops covariance formulas for level sizes, and relates profile limits to total path length. Their inspected BST results concern correlations among level populations; searches of the full text found no root-imbalance statistic or root-split/path-length regression.

Standard Quicksort analysis conditions on the uniformly random first pivot and therefore contains the conditional recursion underlying (1). The accepted contribution is not that recursion or the classical marginal path-length moments. It is the exact local-to-global dependence law: strict monotone regression in squared root imbalance, the closed cubic covariance, the exact linear-regression slope, and the nonvanishing asymptotic correlation and explained-variance constant.

## Limitations

The result uses the random-permutation BST, equivalently uniformly random pivot ranks at every recursive call. Median-of-sample pivots and other split-tree models have different root-rank laws.

The quadratic imbalance was chosen because it is the simplest symmetric polynomial of the root split with a clean exact covariance. No claim is made that it is the optimal nonlinear predictor of path length.

The derivation is elementary once the first split is retained. Older analysis-of-algorithms literature or textbooks may contain the same mixed moment as an unstated exercise or easy corollary; this remains the main originality risk.

## References

1. H. Prodinger, “A q-Analogue of the Path Length of Binary Search Trees,” arXiv:math/9910070, first submitted 1999-10-14; *Algorithmica* 31 (2001), 433–441, DOI 10.1007/s00453-001-0058-y.
2. M. Drmota and H.-K. Hwang, “Profiles of random trees: correlation and width of random recursive trees and binary search trees,” manuscript dated 2004-10-25; *Advances in Applied Probability* 37 (2005), 321–341, DOI 10.1239/aap/1118858628.
3. F. M. Dekking and L. E. Meester, “An almost sure result for path lengths in binary search trees,” *Advances in Applied Probability* 35 (2003), 363–376, DOI 10.1239/aap/1051201652.
