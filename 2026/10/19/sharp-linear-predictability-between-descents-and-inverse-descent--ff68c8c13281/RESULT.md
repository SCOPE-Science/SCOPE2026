# Sharp linear predictability between descents and inverse descents of a uniform permutation

## Finding

Let \(\pi\) be uniform on the symmetric group \(S_n\), for every integer \(n\ge2\). For \(1\le i,j\le n-1\), let \(D_i=\mathbf 1\{\pi(i)>\pi(i+1)\}\) and \(E_j=\mathbf 1\{\pi^{-1}(j)>\pi^{-1}(j+1)\}\). Put \(m=n-1\), \(c_n=1/[2n(n-1)]\), and \(A_n\) for the \(m\)-by-\(m\) matrix with diagonal \(1/4\), immediate off-diagonal \(-1/12\), and all other entries zero.

The full covariance blocks satisfy
\[
\operatorname{Cov}(D_i,E_j)=c_n\quad\text{for all }i,j,
\qquad \operatorname{Cov}(D)=\operatorname{Cov}(E)=A_n.
\]
In particular the cross-covariance has rank one, and every zero-sum weighted contrast of descent positions is uncorrelated with every inverse-descent indicator.

For nonzero real coefficient vectors \(a,b\in\mathbb R^{m}\), the **sharp** maximum of
\[
\operatorname{Corr}\left(\sum_i a_i D_i,\sum_j b_j E_j\right)
\]
is \(\rho_n\), where, with \(r=(3+\sqrt5)/2\),
\[
\rho_n=\frac{6}{n(n-1)}\left[n-1-
\frac{2(r^{n}-r)}{(r-1)(1+r^{n})}\right].
\]
Equality holds precisely when \(a\) and \(b\) are **positive multiples** of the same vector \(w\), where
\[
w_i=12\left(1-\frac{r^i+r^{n-i}}{1+r^n}\right),\qquad 1\le i\le n-1.
\]
The maximum absolute correlation has the same value; there the two nonzero multipliers can have either signs. In particular, \(\rho_2=\rho_3=1\), \(\rho_4=13/14\), \(\rho_n<1\) for \(n\ge4\), and \(n\rho_n\to6\).

All inverse-descent indicators have the **same** best affine least-squares prediction from the vector of ordinary descent indicators:
\[
\operatorname{Proj}_{\operatorname{span}\{1,D_1,\ldots,D_m\}}E_j
=\frac12+c_n\sum_{i=1}^{m}w_i(D_i-\tfrac12),\quad 1\le j\le m.
\]
The projection is linear, not a claim about conditional expectations or independence. Its coefficient profile has an explicit boundary layer: for each fixed positive integer \(i\), \(w_i\to12(1-r^{-i})\) as \(n\to\infty\), whereas for positions whose distance from both boundaries tends to infinity, \(w_i\to12\).

## Assumptions and scope

All probabilities refer to the uniform law on \(S_n\), with \(n\ge2\) and no conditioning. Position descents \(D_i\) compare adjacent **positions**, whereas inverse descents \(E_j\) compare the order of adjacent **values**. Coefficient vectors are deterministic real vectors and must be nonzero to define a correlation. For \(n=2\) the matrix has size one. The outcome is exact at each finite size; no joint Gaussianity or conditional independence is asserted.

## Proof

**Cross-covariance.** Fix \(i,j\). Let \(\tau_j\) interchange the values \(j\) and \(j+1\) of a permutation, without changing any other values. This involution is measure-preserving and flips \(E_j\). Unless those two values jointly occupy positions \(i,i+1\), the inequality of the entries at positions \(i,i+1\) is unchanged, since no integer lies strictly between \(j\) and \(j+1\). Pairing each permutation with its image under \(\tau_j\), the contributions of \((D_i-1/2)(E_j-1/2)\) cancel outside that exceptional event. On the event both values occupy those two positions, \(D_i=E_j\), so the product is \(1/4\). The event has probability \(2/[n(n-1)]\). Therefore \(\operatorname{Cov}(D_i,E_j)=1/[2n(n-1)]\) uniformly in both indices.

**Marginal covariance.** For each \(i\), \(D_i\) is Bernoulli with mean \(1/2\) and variance \(1/4\). When \(|i-k|\ge2\), the two comparisons depend on disjoint sets of ranks and are independent, hence covariance zero. For adjacent positions \(\Pr(D_i=D_{i+1}=1)=1/6\) by the six equally likely orders of three ranks. Therefore the covariance is \(1/6-1/4=-1/12\). The inverse permutation is also uniform, giving the identical block \(A_n\) for \(E\). The matrix \(A_n\) is strictly positive definite: it is \(1/12\) times the symmetric tridiagonal matrix with diagonal three and neighboring entries minus one, whose quadratic form is strictly positive.

**The sharp optimization.** For arbitrary nonzero vectors \(a,b\), the previous formulas yield
\[
\operatorname{Corr}(a\cdot D,b\cdot E)
=c_n\frac{(\mathbf 1^{\mathsf T}a)(\mathbf 1^{\mathsf T}b)}
{\sqrt{(a^{\mathsf T}A_n a)(b^{\mathsf T}A_n b)}}.
\]
Cauchy–Schwarz in the positive definite quadratic form \(A_n\) gives
\[
(\mathbf 1^{\mathsf T}a)^2\le
(\mathbf 1^{\mathsf T}A_n^{-1}\mathbf 1)(a^{\mathsf T}A_n a),
\]
with equality exactly at \(a=tA_n^{-1}\mathbf 1\). Thus the maximum is \(c_n\mathbf 1^{\mathsf T}A_n^{-1}\mathbf 1\), with the stated equality cases. The best-linear-prediction formula is the ordinary normal-equation identity \(A_n\beta=c_n\mathbf 1\).

**Explicit inverse and boundary profile.** The vector \(x=A_n^{-1}\mathbf1/12\) uniquely solves
\[
3x_i-x_{i-1}-x_{i+1}=1,\qquad x_0=x_n=0.
\]
The homogeneous characteristic equation \(z^2-3z+1=0\) has reciprocal positive roots \(r\) and \(r^{-1}\). Substituting and applying the two boundary conditions gives
\[
x_i=1-(r^i+r^{n-i})/(1+r^n).
\]
Hence \(w=12x\) and, by a geometric sum,
\[
\mathbf 1^{\mathsf T}w
=12\left[n-1-\frac{2(r^n-r)}{(r-1)(1+r^n)}\right].
\]
This establishes the formula for \(\rho_n\). Since \(0<x_i<1\), it follows that \(\rho_n<6/n<1\) for \(n\ge7\). Direct exact substitution gives \(\rho_2=\rho_3=1\), \(\rho_4=13/14\), \(\rho_5=21/25\), and \(\rho_6=34/45\), proving all finite strictness assertions. The displayed formula also immediately gives \(n\rho_n\to6\) and the boundary-layer limits.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It exhaustively enumerates the \(n!\) permutations for every \(2\le n\le8\), computes all ordered entries of the three covariance blocks with exact fractions, independently inverts the descent covariance matrix, and checks the stated sharp correlation and test-weight inequalities. It passes 497 exact assertions. This finite verification supports, but does not substitute for, the proof valid at all \(n\).

To reproduce: run `python3 verify.py` in a directory containing this file and the script. No third-party packages or random seeds are required.

## Relationship to prior work

The joint distribution of the total numbers of descents and inverse descents is classical. Visontai (arXiv:1210.3799, Section 2) develops the two-sided Eulerian recurrence. Chatterjee and Diaconis (arXiv:1608.01666, Sections 3 and 5) derive the covariance of the **total** descent counts and study their joint Gaussian limit; the uniform individual cross-covariance here is consistent with their total covariance. Gessel and Zhuang (DOI 10.1017/fms.2024.89, Section 2.1) recall Foulkes's exact enumeration of all prescribed pairs of descent compositions through ribbon Schur scalar products. Thus no novelty is claimed for the underlying joint descent-set distribution or the aggregate covariance.

The result here is the evaluated *position-by-value* covariance block and, in particular, the closed-form solution of the sharp finite-dimensional linear-correlation optimization, including its unique optimizer, projection profile, and asymptotic boundary layer. These optimized linear-prediction statements are not stated in the inspected papers. Foulkes's broad counting formula can in principle recover all required finite moments, so implicit earlier derivation is a genuine priority risk. Related published results on inversion-indicator precision and fixed-point–descent cross-covariances concern different random vectors and do not give this optimizer.

## Limitations

Only deterministic **linear** scores and affine least-squares projections are optimized; nonlinear dependence between the two descent sets may be stronger. A zero cross-covariance for a contrast does not imply independence. The conditional law and all higher-order mixed moments are not classified here. The result uses uniform permutations; nonuniform permutation measures are not covered. Historical originality remains provisional pending independent specialist review, particularly given the classical full descent-set enumeration.

## References

1. M. Visontai, *Some remarks on the joint distribution of descents and inverse descents*, arXiv:1210.3799 (initial public posting 2012-10-14); Electronic Journal of Combinatorics 20(1), P52 (2013), DOI: 10.37236/2135.
2. S. Chatterjee and P. Diaconis, *A central limit theorem for a new statistic on permutations*, arXiv:1608.01666 (2016); Indian Journal of Pure and Applied Mathematics 48, 561–573 (2017).
3. I. M. Gessel and Y. Zhuang, *Two-sided permutation statistics via symmetric functions*, Forum of Mathematics, Sigma 12 (2024), DOI: 10.1017/fms.2024.89; especially Theorem 2.1 on Foulkes's descent-composition enumeration.
4. H. O. Foulkes, *Enumeration of permutations with prescribed up-down and inversion sequences*, Discrete Mathematics 15 (1976), 235–252; accessed via the statement and attribution in Reference 3.
