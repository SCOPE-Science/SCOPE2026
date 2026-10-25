# A parity-reversing isotropic comparison for Van Kampen–Flores polytopes

## Finding
For every integer \(n\ge 3\), write \(d=n-1\), \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), \(\delta_i=e_i-\mathbf1/n\), and
\[
\Omega_n=\operatorname{conv}\{\pm\delta_i:1\le i\le n\}\subset H_n.
\]
This is the canonical Euclidean realization of the maximal-volume Bier (Van Kampen–Flores) polytope, equivalently the orthogonal projection of the \(n\)-dimensional cross-polytope onto \(H_n\). The following exact formulas hold:
\[
\operatorname{vol}_{d}(\Omega_n)=\frac{\sqrt n}{d!}\binom d{\lfloor d/2\rfloor},\qquad
\operatorname{Cov}(U_n)=\lambda_n I_{H_n},\qquad
\lambda_n=\begin{cases}
\dfrac{2n-1}{n^2(n+1)}&n\text{ odd},\\[2pt]
\dfrac{2n-3}{(n-1)n(n+1)}&n\text{ even},
\end{cases}
\]
where \(U_n\) is uniformly distributed on \(\Omega_n\) with respect to intrinsic Euclidean volume.

Define the affine-invariant isotropic constant of a full-dimensional \(d\)-body \(K\) by \(L(K)^{2d}=\det(\operatorname{Cov}(U_K))/\operatorname{vol}_d(K)^2\). Let \(\Diamond_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\). Then a **strict parity-dependent comparison with exactly two exceptions** holds:
\[
\boxed{\ L(\Omega_n)>L(\Diamond_d)\ \Longleftrightarrow\ n\in\{4,6\},\qquad
L(\Omega_n)<L(\Diamond_d)\ \text{for all other }n\ge3.\ }
\]
Moreover, both isotropic constants tend to \(1/(e\sqrt2)\), while the first nonzero normalized difference has the exact limit
\[
\boxed{\ \lim_{n\to\infty}(n-1)\left[\left(\frac{L(\Omega_n)}{L(\Diamond_{n-1})}\right)^2-1\right]=\log(\pi/2)-\tfrac12<0.\ }
\]

## Assumptions and scope
All Euclidean measures, inner products, and covariances on \(H_n\) use the metric induced from \(\mathbb R^n\), not a nonorthogonal coordinate projection. Every statement is for integers \(n\ge3\); the separate one-dimensional case \(n=2\) gives equality because both bodies are segments. The comparison uses the regular cross-polytope in the **same intrinsic dimension**, and is invariant under rescaling or nonsingular affine transformations of either body. The volume formula is recalled from the geometric Bier-sphere construction; the covariance, exact comparison, and normalized limit constitute the assessed result.

## Proof
**1. A complete conical simplex decomposition.** The polar in \(H_n\) satisfies
\[\Omega_n^\circ=\{y\in H_n:|y_i|\le1\ (1\le i\le n)\}.\]
A vertex of this cube section has all but at most one coordinate at \(\pm1\). If \(n=2m+1\), its coordinates are \(m\) entries \(+1\), \(m\) entries \(-1\), and one zero. The corresponding primal facet has the \(d\) vertices \(\varepsilon_i\delta_i\) for the nonzero positions, with \(m\) positive and \(m\) negative signs; it is a simplex. There are \(n\binom{2m}{m}\) such facets.

If \(n=2m\), every polar vertex has \(m\) positive and \(m\) negative coordinates. The primal facet has those \(2m\) signed vertices. Its two groups of \(m\) vertices are simplices meeting at their common barycenter; coning the whole negative simplex over the \(m\) positive-side simplex pieces (obtained by deleting one of the positive vertices) partitions this facet into exactly \(m\) simplices of dimension \(d-1\), up to boundaries. Over all polar vertices this produces \(n\binom{2m-1}{m-1}\) boundary simplices. Each such simplex has \(d\) signed vertices, with \(m-1\) positive and \(m\) negative signs; the omitted index has no vertex. Coning all these boundary simplices to the origin decomposes \(\Omega_n\) into \(n\binom d{\lfloor d/2\rfloor}\) full-dimensional simplices with disjoint interiors.

For any omitted index \(j\), the \(d\times d\) Gram matrix of \(\{\delta_i:i\ne j\}\) is \(I_d-\mathbf1\mathbf1^T/n\), whose determinant is \(1/n\). Signs do not affect the absolute determinant, so every coned simplex has volume \(1/(\sqrt n\,d!)\). This proves the displayed intrinsic-volume formula.

**2. Exact second moment.** For a uniform point on a \(d\)-simplex with vertices \(0,v_1,\ldots,v_d\), the Dirichlet barycentric moment identity gives
\[
\mathbb E\|X\|^2=\frac{\sum_i\|v_i\|^2+\|\sum_i v_i\|^2}{(d+1)(d+2)}.
\]
Here \(v_i=\varepsilon_i\delta_i\), \(i\ne j\). Since \(\|\delta_i\|^2=d/n\), the first numerator term equals \(d^2/n\). Set \(s=\sum_{i\ne j}\varepsilon_i\delta_i\). Writing \(\sum_{i\ne j}\varepsilon_i=\sigma\), one has \(\|s\|^2=d-\sigma^2/n\). For odd \(n\), \(\sigma=0\); for even \(n\), \(\sigma=-1\). Thus each coned simplex has exactly the same radial second moment:
\[
\mathbb E\|U_n\|^2=\begin{cases}
\dfrac{(n-1)(2n-1)}{n^2(n+1)}&n\text{ odd},\\[2pt]
\dfrac{2n-3}{n(n+1)}&n\text{ even}.
\end{cases}
\]
The body is centrally symmetric, hence its mean is zero. Invariance under coordinate permutations forces covariance to be scalar on \(H_n\) (every permutation-commuting matrix has the form \(aI+b\mathbf1\mathbf1^T\)). Dividing the radial moment by \(d\) proves \(\operatorname{Cov}(U_n)=\lambda_n I_{H_n}\).

**3. Reduction to central binomial inequalities.** The regular cross-polytope has volume \(2^d/d!\), covariance \(2I_d/[(d+1)(d+2)]\), and
\[L(\Diamond_d)^2=\frac{(d!)^{2/d}}{2(d+1)(d+2)}.\]
Let \(b_m=4^{-m}\binom{2m}{m}\), \(q_m=(2m+1)b_m^2\), and \(p_m=2mb_m^2\). Direct substitution of the volume and covariance formulas yields
\[
\left(\frac{L(\Omega_{2m+1})}{L(\Diamond_{2m})}\right)^{4m}
=\frac{(1-1/(4m+2))^{2m}}{q_m},\qquad m\ge1,
\]
\[
\left(\frac{L(\Omega_{2m})}{L(\Diamond_{2m-1})}\right)^{4m-2}
=\frac{(1-1/(4m-2))^{2m-1}}{p_m},\qquad m\ge1.
\]
The Wallis product gives
\[
q_m=\prod_{j=1}^{m}\left(1-\frac1{4j^2}\right)>\frac2\pi>\frac7{11},\qquad p_m=\frac{2m}{2m+1}q_m.
\]
For odd \(n=2m+1\) with \(m\ge5\),
\[
(1-1/(4m+2))^{2m}<e^{-m/(2m+1)}\le e^{-5/11}<7/11<q_m.
\]
The penultimate comparison follows from \(e^{5/11}>1+5/11+(5/11)^2/2+(5/11)^3/6>11/7>\pi/2\). For \(m=1,2,3,4\), direct rational comparisons give the same strict inequality.

For even \(n=2m\) and \(m\ge11\),
\[
p_m>\frac{2m}{2m+1}\frac7{11}\ge\frac{14}{23}>e^{-1/2}>(1-1/(4m-2))^{2m-1}.
\]
Here \(e^{1/2}>1+1/2+1/8+1/48>23/14\). Direct exact rational comparisons give \(p_m<(1-1/(4m-2))^{2m-1}\) for \(m=2,3\) and the reverse inequality for every \(4\le m\le10\); at \(m=1\) equality holds, outside the stated range \(n\ge3\). Thus precisely \(n=4,6\) reverse the otherwise strict inequality.

**4. Sharp limit.** The Wallis product also gives \(q_m\to2/\pi\), and therefore \(p_m\to2/\pi\). Taking logarithms of either exact ratio identity and using \((2m)\log(1-1/(4m+2))\to-1/2\) and \((2m-1)\log(1-1/(4m-2))\to-1/2\) yields
\[
\lim_{n\to\infty}d\log\left(\frac{L(\Omega_n)}{L(\Diamond_d)}\right)^2=\log(\pi/2)-1/2.
\]
The logarithm is \(O(1/d)\), so exponentiation gives the asserted limit. Finally Stirling's formula and \(\binom d{\lfloor d/2\rfloor}\sim2^d\sqrt{2/(\pi d)}\) establish \(L(\Omega_n),L(\Diamond_d)\to1/(e\sqrt2)\).

## Verification
The companion `check.py` uses exact rational arithmetic to verify all exceptional finite comparisons \(m\le10\), the Wallis-product finite identity, and the two elementary exponential-bound certificates. Independently, SciPy convex-hull triangulation in orthonormal coordinates computes volumes and uniform radial moments for \(3\le n\le8\), agreeing with the formulas to \(10^{-10}\). Run with `OPENBLAS_NUM_THREADS=1 python check.py` (requires Python 3.10+, NumPy and SciPy). These finite checks do not establish the infinite ranges; the inequalities above do.

## Relationship to prior work
Jevtić and Živaljević (2021, arXiv:2108.00618), Section 2 and Theorem 13, introduce the maximal-volume Bier/Van Kampen–Flores realization, its volume decomposition, and the duality with a median hypersimplex. Those underlying geometric objects, the decomposition principle, and volume computation are prior work. Alonso-Gutiérrez, Bastero, Bernués, and Wolff (2009, arXiv:0904.2632), Sections 2–3, analyze isotropic constants for projections of cross-polytopes and establish dimensional bounds, rather than the exact one-dimensional-kernel projection covariance or parity threshold. Kipp (arXiv:2407.01353, particularly Sections 1 and 4) gives the regular cross-polytope's isotropic constant and structural optimality conditions, not this explicit projection comparison. The claimed new content is the exact covariance and parity-reversing strict comparison, including the first-order asymptotic deficit, for this canonical symmetric projection.

## Limitations
This is an exact statement only for the canonical \(n\)-vertex regular-simplex symmetrization in the induced metric, not for arbitrary projections of cross-polytopes, irregular simplices, or general Bier realizations. Novelty is assessed against accessible literature and searchable scientific records, not proven by search absence; equivalent formulas under the terminology of projected \(\ell_1\)-balls or regular-simplex symmetrizations may exist. No independent mathematical audit has been performed.

## References
1. F. D. Jevtić and R. T. Živaljević, *Bier spheres of extremal volume and generalized permutohedra*, arXiv:2108.00618 (first public arXiv version August 2, 2021), https://arxiv.org/abs/2108.00618 .
2. D. Alonso-Gutiérrez, J. Bastero, J. Bernués, and P. Wolff, *On the isotropy constant of projections of polytopes*, arXiv:0904.2632 (2009), https://arxiv.org/abs/0904.2632 .
3. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353, https://arxiv.org/html/2407.01353v2 .
4. Classical Wallis product and central-binomial asymptotics; the exact finite identities used here are reproduced in the proof and in `check.py`.
