# Exact inertia of complete-graph root polytopes and a sharp isotropic deficit

## Finding

Let \(n\ge 2\), let \(H_n=\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\}\) carry its induced Euclidean metric, and define the full type-A root polytope
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\}\subset H_n.
\]
For a random vector \(X_n\) uniformly distributed with respect to intrinsic \((n-1)\)-dimensional volume on \(P_n\), the exact volume and covariance are
\[
\operatorname{Vol}_{n-1}(P_n)=\frac{\sqrt n}{(n-1)!}\binom{2n-2}{n-1},\qquad
\operatorname{Cov}(X_n)=\frac{4(2n-1)}{n(n+1)^2}\,I_{H_n}.
\]
Let \(L(K)=(\det\operatorname{Cov}(U_K))^{1/(2d)}/\operatorname{Vol}_d(K)^{1/d}\) be the affine-invariant isotropic constant of a \(d\)-dimensional convex body, using its intrinsic Euclidean volume and covariance, and let \(\Diamond_d=\{x\in\mathbb R^d:\sum_i|x_i|\le1\}\) be the regular cross-polytope. Then
\[
\boxed{L(P_n)<L(\Diamond_{n-1})\quad\text{for all }n\ge3,}
\]
with equality at \(n=2\). The comparison is sharp to first order:
\[
\boxed{\lim_{n\to\infty}(n-1)\left(1-\frac{L(P_n)}{L(\Diamond_{n-1})}\right)=\frac{3/2-\log\pi}{2}>0.}
\]
In particular, both constants converge to \(1/(e\sqrt2)\), yet the full complete-graph root polytope has a strictly smaller isotropic constant than the regular cross-polytope of equal intrinsic dimension in every dimension at least two.

## Assumptions and scope

All volume and covariance statements use the Euclidean metric induced from \(\mathbb R^n\) on \(H_n\); a unimodular coordinate projection does not preserve this metric. The body \(P_n\) is also the centered \(\ell_1\)-section \(\{x\in H_n:\sum_i|x_i|\le2\}\). Indeed, a nonzero \(x\) in this section has total positive and negative mass \(s\le1\), and \(x/s\) is a convex combination of positive-negative roots \(e_i-e_j\); the converse is immediate. The statement concerns the continuous uniform-volume distribution, not the uniform distribution on vertices or lattice points.

## Proof

**Orthant decomposition and volume.** Fix a sign pattern with exactly \(k\) positive and \(n-k\) negative entries, where \(1\le k\le n-1\). Write the positive entries as \(s u_1,\ldots,su_k\) and the magnitudes of negative entries as \(s v_1,\ldots,sv_{n-k}\), with \(s\in[0,1]\) and independent simplex variables \(u\in\Delta_{k-1}\), \(v\in\Delta_{n-k-1}\). Coarea on the zero-sum hyperplane gives the volume of this orthant sector as
\[
\frac{\sqrt n}{(n-1)(k-1)!(n-k-1)!}.
\]
Thus its probability is proportional to \(\binom nk\binom{n-2}{k-1}\), and Vandermonde convolution yields
\[
\sum_{k=1}^{n-1}\binom nk\binom{n-2}{k-1}=\binom{2n-2}{n-1}.
\]
The displayed formula for \(\operatorname{Vol}_{n-1}(P_n)\) follows by summation. In a fixed sector the mixing variable has density \((n-1)s^{n-2}\), hence \(\mathbb E[s^2]=(n-1)/(n+1)\), while \(u,v\) independently have uniform Dirichlet distributions.

**Continuous second moments.** For a uniform Dirichlet vector on a simplex with \(k\) components, \(\mathbb E\sum_i u_i^2=2/(k+1)\). Consequently
\[
\mathbb E[\|X_n\|_2^2\mid k]
=\frac{2(n-1)}{n+1}\left(\frac1{k+1}+\frac1{n-k+1}\right).
\]
The weighted Vandermonde identity
\[
\sum_{k=1}^{n-1}\frac1{k+1}\binom nk\binom{n-2}{k-1}
=\frac1{n+1}\binom{2n-1}{n}
\]
reduces the unconditional radial second moment to
\[
\mathbb E\|X_n\|_2^2=\frac{4(n-1)(2n-1)}{n(n+1)^2}.
\]
The mean is zero by central symmetry. Permutation invariance and the constraint \(\sum_iX_{n,i}=0\) force covariance to be a scalar multiple of the identity on \(H_n\). Division of the displayed radial second moment by \(n-1\) identifies that scalar.

**Comparison with the cross-polytope.** Write \(d=n-1\), \(C_d=\binom{2d}{d}\), and \(R_n=L(P_n)/L(\Diamond_d)\). The known simplex decomposition of \(\Diamond_d\) gives \(\operatorname{Vol}_d(\Diamond_d)=2^d/d!\) and coordinate variance \(2/((d+1)(d+2))\). Substitution into the definition of \(L\) gives the exact rational-power identity
\[
R_n^{2d}=\frac{\left(8(2n-1)/(n+1)\right)^d}{n C_d^2}.
\]
At \(n=2\) the right side is one. At \(n=3,4\) it is, respectively, \(25/27\) and \(2744/3125\), both strictly less than one. For all \(n\ge5\), gamma-function log-convexity, equivalently Cauchy--Schwarz, gives
\[
\Gamma(d+1)^2\le\Gamma(d+\tfrac12)\Gamma(d+\tfrac32)
=(d+\tfrac12)\Gamma(d+\tfrac12)^2,
\]
and the duplication formula yields
\[
C_d\ge\frac{4^d}{\sqrt{\pi(d+1/2)}}.
\]
Hence
\[
R_n^{2d}\le \frac{\pi(d+1/2)}{d+1}
\left(1-\frac3{2(n+1)}\right)^{n-1}
<\pi\left(1-\frac3{2(n+1)}\right)^{n-1}.
\]
The last powered factor is strictly decreasing for real \(n\ge5\): differentiating its logarithm and using \(\log(1-y)<-y\) with \(y=3/(2(n+1))\) proves this because \((n-1)/(n+1)<1-y\). Its value at \(n=5\) is \(81/256\), and the classical inequality \(\pi<22/7<256/81\) finishes the strict comparison.

**First-order asymptotic.** The central-binomial Stirling estimate \(C_d=4^d(\pi d)^{-1/2}(1+O(d^{-1}))\) and \(n=d+1\) show directly from the exact identity that
\[
\lim_{n\to\infty}d\log R_n^2=\log\pi-\frac32.
\]
As \(R_n\to1\), dividing by two and exponentiating gives the displayed limit for \(d(1-R_n)\). Finally, Stirling's formula in either isotropic-constant expression yields the common limit \(1/(e\sqrt2)\).

## Verification

A standalone exact-arithmetic checker, `CHECKER.py`, independently reconstructs the polytope from its root vertices in reduced coordinates, triangulates its boundary and cones it to the origin, and integrates each simplex's Euclidean quadratic form exactly for \(n=3,4,5,6\). It also checks the two Vandermonde identities and the strict rational-power comparison for every integer \(3\le n\le200\). The analytical argument above, rather than these finite calculations, proves the statements for all admissible integers. Run `python CHECKER.py` with Python 3, NumPy and SciPy available.

## Relationship to prior work

D'Alì, Delucchi, and Michałek identify symmetric edge polytopes of complete graphs with the full type-A root polytopes (their Example 3), place them in the graphical and Kantorovich--Rubinstein setting, and study Ehrhart/combinatorial invariants. Chen, Davis, and Korchevskaia establish the graph-facet correspondence for symmetric edge polytopes. Kipp studies local extremizers of isotropic constants and records the isotropic constant of the regular cross-polytope; his local optimality results are not an all-dimensional comparison for these full root polytopes. The binomial volume count, Dirichlet identities, and general formulas for isotropic constants are background tools; the asserted finding is the combined exact continuous-volume covariance, strict dimensionwise comparison, and sharp asymptotic deficit, not the underlying graph-polytope construction or standard estimates.

## Limitations

The derivation has not undergone an independent mathematical audit or computer-formalized proof. The numerical and finite exact tests do not establish novelty or infinite-dimensional validity. Equivalences under central sections of \(\ell_1\)-balls could conceal a prior moment computation outside the indexed graph-polytope literature; this remains a bibliographic risk. The comparison is only with the affine class of the regular cross-polytope, not with arbitrary centrally symmetric polytopes or every symmetric-edge polytope.

## References

1. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public 2019-10-11), Electronic Journal of Combinatorics 29(3) (2022), P3.24. https://arxiv.org/abs/1910.05193
2. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public 2021-07-26). https://arxiv.org/abs/2107.12315
3. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353 (first public 2024-07-01), Advances in Mathematics 476 (2025), 110361. https://arxiv.org/abs/2407.01353
