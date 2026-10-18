# Exact crossing-cut Green kernel and Gaussian bridge for uniform pairings

## Finding

Let \(M=2n\ge4\) and choose a perfect matching uniformly from all \((M-1)!!\) pairings of the ordered sites \(\{1,\ldots,M\}\). For \(0\le k\le M\), let \(H_k\) be the number of matching edges with exactly one endpoint in the prefix \(\{1,\ldots,k\}\). Thus \(H_0=H_M=0\), while \(H_1=H_{M-1}=1\) deterministically. The profile counts open chords when the matching diagram is scanned from left to right.

**Exact second-order law.** For all \(0\le k,l\le M\), set \(u=\min(k,l)\) and \(v=\max(k,l)\). Then
\[
\mathbb E H_k=\frac{k(M-k)}{M-1},\qquad
\operatorname{Cov}(H_k,H_l)
=\frac{2u(u-1)(M-v)(M-v-1)}{(M-3)(M-1)^2}.
\]
In particular, the covariance \(\Sigma_M\) indexed by \(k=2,3,\ldots,M-2\) is strictly positive definite. Its inverse is tridiagonal, with the following exact quadratic form. Put
\[
V_2=\frac{4(M-2)}{(M-1)^2},\quad
 a_k=\frac{M-k-2}{M-k},\quad
 q_{k+1}=\frac{4k(M-k-1)(M-k-2)}{(M-k)(M-3)(M-1)}
\]
for \(2\le k\le M-3\). For every real column \(y=(y_2,\ldots,y_{M-2})\),
\[
y^{\mathsf T}\Sigma_M^{-1}y
=\frac{y_2^2}{V_2}
+\sum_{k=2}^{M-3}\frac{(y_{k+1}-a_k y_k)^2}{q_{k+1}}.
\]
The sum is empty at \(M=4\). Its determinant is
\[
\det\Sigma_M
=\frac{2\,4^{M-3}(M-3)!(M-4)!}
{(M-3)^{M-4}(M-1)^{M-2}}>0.
\]
The precision matrix has negative entries only in its immediate off-diagonal positions; they are strictly negative when such positions exist. Here “precision” refers to the inverse covariance, **not** to a claim of finite-sample Gaussianity or conditional independence.

**Functional fluctuation law.** As \(M\to\infty\) through even integers, linearly interpolate the values
\[
Z_M(k/M)=\frac{H_k-\mathbb E H_k}{\sqrt M},\qquad 0\le k\le M.
\]
Then \(Z_M\) converges weakly in \(C([0,1])\) to the continuous, centered Gaussian process
\[
G(t)=\sqrt2\,(1-t)^2 W\!\left(\frac{t^2}{(1-t)^2}\right)
\quad(0\le t<1),\qquad G(1)=0,
\]
where \(W\) is standard Brownian motion. Its covariance is the explicit Green kernel
\[
\operatorname{Cov}(G(s),G(t))
=2\min(s,t)^2[1-\max(s,t)]^2.
\]
Consequently, if \(A_M=\sum_{k=1}^{M-1}H_k\) denotes the aggregate linear span of all matching chords, then
\[
\mathbb E A_M=\frac{M(M+1)}6,
\qquad
\frac{A_M-\mathbb E A_M}{M^{3/2}}
\ \Rightarrow\ \mathcal N(0,1/45).
\]

## Assumptions and scope

The matching is **uniform** on the fixed ordered set of \(M\) labeled endpoints; \(M\ge4\) must be even. The prefix size ranges over all integers \(0\le k\le M\). In the limit theorem, only even sizes tend to infinity, and convergence refers to the polygonal interpolation in the uniform topology. The exact covariance and precision laws hold for every admissible finite \(M\). The limit concerns unweighted open chords, not crossings among the chords.

## Proof

**1. Exposure process and conditional regression.** Scan the endpoints in increasing order. After the first \(k\) have been exposed, every unmatched endpoint in the prefix has a partner at one of the remaining \(M-k\) sites. Uniform symmetry of the unexposed matching gives the exact transitions
\[
\Pr(H_{k+1}=h-1\mid H_k=h)=\frac{h}{M-k},\qquad
\Pr(H_{k+1}=h+1\mid H_k=h)=1-\frac{h}{M-k}
\]
for \(0\le k<M\) and every attainable \(h\). These conditional probabilities remain valid given the *whole* exposed partial matching. It follows that
\[
\mathbb E(H_{k+1}\mid H_k)=\left(1-\frac2{M-k}\right)H_k+1.
\]
Solving the mean recurrence with \(H_0=0\) gives \(m_k:=\mathbb E H_k=k(M-k)/(M-1)\). For \(Y_k=H_k-m_k\), write
\[
Y_{k+1}=a_kY_k+\xi_{k+1},\qquad
a_k=\frac{M-k-2}{M-k},
\]
where the innovations \(\xi_{k+1}\) have zero conditional mean and \(\operatorname{Var}(\xi_{k+1}\mid\mathcal F_k)=4p_k(1-p_k)\) with \(p_k=H_k/(M-k)\).

**2. Exact covariance from prescribed matching edges.** Let \(X_k\) count matching edges with both endpoints in the prefix. Then \(H_k=k-2X_k\). Each prescribed edge occurs with probability \(1/(M-1)\); two disjoint prescribed edges occur together with probability \(1/[(M-1)(M-3)]\), while edges sharing an endpoint cannot coexist. If \(k\le l\), then
\[
\mathbb E(X_kX_l)
=\frac{\binom{k}{2}}{M-1}
+\frac{\binom{k}{2}\binom{l-2}{2}}{(M-1)(M-3)}.
\]
The first term counts coinciding prescribed edges; the second counts ordered disjoint choices. Since \(\mathbb EX_k=\binom{k}{2}/(M-1)\), expansion and factorization yield
\[
\operatorname{Cov}(H_k,H_l)
=4\operatorname{Cov}(X_k,X_l)
=\frac{2k(k-1)(M-l)(M-l-1)}{(M-3)(M-1)^2}
\quad(k\le l).
\]
The cases at deterministic endpoints follow from the zero factors.

**3. Inverse and determinant.** The centered recursion has uncorrelated innovations, because each \(\xi_{k+1}\) is orthogonal to the past. The first nonconstant variable \(Y_2\) has variance \(V_2\). For \(2\le k\le M-3\), the innovation variance computed from the covariance in step 2 is
\[
\operatorname{Var}(\xi_{k+1})
=\operatorname{Var}(Y_{k+1})-a_k^2\operatorname{Var}(Y_k)
=q_{k+1}>0.
\]
The triangular transformation
\[
(Y_2,Y_3,\ldots,Y_{M-2})
\longmapsto
(Y_2,Y_3-a_2Y_2,\ldots,Y_{M-2}-a_{M-3}Y_{M-3})
\]
has determinant one. Its output covariance is diagonal with entries \(V_2,q_3,\ldots,q_{M-2}\). Therefore the original covariance is positive definite, its inverse has the asserted nearest-neighbor quadratic form, and
\[
\det\Sigma_M=V_2\prod_{k=2}^{M-3}q_{k+1}
=\frac{2\,4^{M-3}(M-3)!(M-4)!}{(M-3)^{M-4}(M-1)^{M-2}}.
\]

**4. Functional central limit theorem.** For \(1\le k\le M-2\), define \(g_k=(M-k)(M-k-1)\) and the scaled process
\[
U_{M,k}=\frac{M^{3/2}Y_k}{g_k}.
\]
The identity \(a_k=g_{k+1}/g_k\) makes \(U_{M,k}\) a martingale. On every fixed interval \(0\le k\le(1-\varepsilon)M\), its jumps are bounded by a constant depending on \(\varepsilon\) times \(M^{-1/2}\). The explicit variance formula and Doob's maximal inequality give
\[
\max_{k\le(1-\varepsilon)M}\frac{|Y_k|}{M}\ \xrightarrow{\Pr}\ 0.
\]
Hence uniformly on compact subintervals of \([0,1)\), the conditional closing probability satisfies \(p_k=k/M+o_{\Pr}(1)\). The predictable quadratic variation of the martingale converges uniformly on \([0,1-\varepsilon]\) to
\[
\int_0^t\frac{4u}{(1-u)^3}\,du
=\frac{2t^2}{(1-t)^2}.
\]
The bounded-jump martingale functional central limit theorem applies and gives
\[
U_{M,\lfloor Mt\rfloor}\Rightarrow
\sqrt2 W\!\left(\frac{t^2}{(1-t)^2}\right)
\quad\text{on every }[0,1-\varepsilon].
\]
Multiplying by \(g_{\lfloor Mt\rfloor}/M^2\to(1-t)^2\) gives the stated limit on those intervals. To control \(t\uparrow1\), use the exact reversal symmetry \((H_{M-k})_k\overset d=(H_k)_k\). Doob's inequality for the martingale near the opposite endpoint gives, for each fixed \(\eta>0\),
\[
\lim_{\varepsilon\downarrow0}\limsup_{M\to\infty}
\Pr\!\left(\max_{0\le k\le\varepsilon M}\frac{|Y_k|}{\sqrt M}>\eta\right)=0,
\]
and reversal yields the same bound for \(k\ge(1-\varepsilon)M\). Therefore the convergence extends to the full interval. The polygonal interpolation differs from the step process by at most \(2/\sqrt M\), since each centered increment is bounded by two. This yields convergence in \(C([0,1])\). The proposed Brownian time-change has the displayed covariance by the standard Brownian covariance identity.

**5. Aggregate chord span.** Each matching edge between sites \(i<j\) contributes once to \(H_k\) for each \(i\le k<j\). Thus \(A_M=\sum H_k\) is precisely the sum of all linear endpoint spans. Summing \(m_k\) gives its expectation. The continuous mapping theorem applied to the integral of \(Z_M\) gives the central limit theorem, whose limiting variance is
\[
\int_0^1\!\int_0^1 2\min(s,t)^2[1-\max(s,t)]^2\,ds\,dt=\frac1{45}.
\]

## Verification

The standalone script `verify.py` enumerates every labeled perfect matching for each \(M\in\{4,6,8,10,12\}\). With exact rational arithmetic it checks all means, the entire interior covariance kernel, the tridiagonal inverse, the determinant identity, and every attainable one-step closing probability. The 5 enumerations involve respectively 3, 15, 105, 945, and 10,395 matchings; 450 exact assertions passed. Execute `python verify.py` using Python 3 standard libraries only. Exhaustive small cases support the algebra but do not establish the functional limit, which is proved by the martingale argument above.

## Relationship to prior work

The 2015 preprint of Acan studies chord crossings and the degree of a *fixed random chord* in a uniform matching. Its Section 2 computes conditional means and variances for interior chords of a fixed arc and derives a limiting one-chord degree law. Its Section 6 studies growth by adding entire chords. Neither statement gives the complete time-indexed prefix-boundary covariance kernel or the pinned Gaussian process proved here.

Berkooz, Narayan, and Simón (2018) use a transfer-matrix recursion for weighted histories of open chords in applications to spin-glass correlators. This is strong combinatorial background: the open/close structure is already known. The evaluated two-time covariance, finite covariance inverse and determinant, and functional limit in the unweighted uniform pairing ensemble are the distinctions assessed here. These results should not be presented as novelty of the general chord-history representation or Markov exposure principle.

## Limitations

The theorem is restricted to uniformly random pairings of ordered endpoints. Its inverse-covariance sparsity does not imply finite-dimensional Gaussianity or full conditional independence for the discrete profile. The functional limit is a centered fixed-scale central limit theorem, not a large-deviation principle. The exact finite covariance could conceivably be extracted from a general earlier enumeration or transfer-matrix treatment; priority beyond the inspected sources remains subject to further independent literature assessment.

## References

1. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489v1 (7 January 2015), especially Sections 2 and 6. https://arxiv.org/abs/1501.01489
2. M. Berkooz, P. Narayan, and J. Simón, *Chord diagrams, exact correlators in spin glasses and black hole bulk reconstruction*, JHEP 08 (2018), article 192, DOI: 10.1007/JHEP08(2018)192, especially Section 3.1 and the chord-history transfer recursion. https://doi.org/10.1007/JHEP08(2018)192
