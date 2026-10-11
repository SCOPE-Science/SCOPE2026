# Direction-resolved half-normal fluctuations of random central cube sections

## Finding
For the cube \(Q_n=[-1,1]^n\), choose a hyperplane through its centre with uniformly random unit normal. Let \(V_{n,i}\) be the number of vertices of its generic section lying on cube edges parallel to coordinate axis \(i\). Fix an integer \(r\geq1\). Under a common coupling of all dimensions, for \(n>r\),
\[
\left(\frac{\sqrt{n-1}\,V_{n,i}}{2^{n-1}}\right)_{i=1}^{r}
\xrightarrow[n\to\infty]{L^2}
\sqrt{\frac2\pi}\,(|Z_1|,\ldots,|Z_r|),
\]
where \(Z_1,\ldots,Z_r\) are independent standard Gaussians. More quantitatively, for every \(n\geq2\) and \(1\leq i\leq n\),
\[
\mathbb E\!\left[\left(\frac{\sqrt{n-1}\,V_{n,i}}{2^{n-1}}-\sqrt{\frac2\pi}|Z_i|\right)^2\right]
\leq\frac2\pi\arctan\frac1{\sqrt{n-1}}+\frac5{6\pi(n-1)^2}.
\]
Consequently the directional counts are *not* asymptotically concentrated on their means, even though each count involves exponentially many possible edges. Specifically,
\[
\lim_{n\to\infty}\frac{(n-1)\operatorname{Var}(V_{n,i})}{4^{n-1}}
=\frac2\pi-\frac4{\pi^2}>0,
\]
and the corresponding limits for covariances between two distinct fixed directions are zero. The normalized direction count converges in distribution to a unit-mean half-normal variable:
\[
\frac{V_{n,i}}{\mathbb E V_{n,i}}\Longrightarrow\sqrt{\frac\pi2}|Z_i|.
\]
These assertions are one direction-resolved limit theorem and its consequences, not a claim about a complete finite-dimensional face-vector law.

## Assumptions and scope
Fix an infinite sequence \((Z_j)_{j\geq1}\) of independent real \(N(0,1)\) random variables. In dimension \(n\), take the central hyperplane
\[
H_n=\{x\in\mathbb R^n:\sum_{j=1}^n Z_jx_j=0\}.
\]
This hyperplane is Haar-uniform among unoriented central hyperplanes because its normal has rotationally invariant Gaussian law. With probability one, it avoids every vertex of \(Q_n\), simultaneously for all positive integers \(n\). For such a generic section, each section vertex lies in the relative interior of exactly one cube edge, so \(V_{n,i}\) is unambiguously defined. For dimension \(n\), axis \(i\) has exactly \(2^{n-1}\) cube edges. We assert convergence only for a fixed finite collection of coordinate axes \(i=1,\ldots,r\), not uniformly over a number of axes growing with \(n\).

## Proof
**1. Edge characterization.** Put \(m=n-1\) and condition on \(Z_i=x\). An edge parallel to axis \(i\) is specified by a sign vector \(\varepsilon\in\{-1,1\}^m\) in the remaining coordinates. Its endpoints have opposite signs under the linear functional defining \(H_n\) if and only if
\[
\left|\sum_{j\ne i}\varepsilon_j Z_j\right|<|x|.
\]
Consequently, setting \(U_\varepsilon=m^{-1/2}\sum_{j\ne i}\varepsilon_jZ_j\),
\[
X_{n,i}:=\frac{V_{n,i}}{2^m}
=2^{-m}\sum_{\varepsilon\in\{-1,1\}^m}
\mathbf{1}\!\left\{|U_\varepsilon|<\frac{|Z_i|}{\sqrt m}\right\}.
\]
Conditional on \(Z_i=x\), each \(U_\varepsilon\) is standard Gaussian and the conditional mean is
\[
p_m(x):=\mathbb E[X_{n,i}\mid Z_i=x]
=2\Phi\!\left(\frac{|x|}{\sqrt m}\right)-1.
\]
This is an identity for every \(m\geq1\); the many indicators are dependent, so an independent-binomial argument would be invalid.

**2. Exact second-moment control despite dependence.** For sign vectors \(\varepsilon,\delta\), the conditional correlation of their Gaussian sums is
\[
\rho_{\varepsilon,\delta}=\frac1m\sum_{j=1}^m\varepsilon_j\delta_j.
\]
At fixed \(x\), the centered threshold function \(u\mapsto\mathbf{1}\{|u|<|x|/\sqrt m\}-p_m(x)\) is even in standard Gaussian \(L^2\), and thus has no odd Hermite coefficients and no constant coefficient. The covariance identity for the orthonormal Hermite expansion of correlated Gaussians gives
\[
0\leq \operatorname{Cov}\!\left(\mathbf{1}\{|U_\varepsilon|<a\},\mathbf{1}\{|U_\delta|<a\}\mid Z_i=x\right)
\leq\rho_{\varepsilon,\delta}^2 p_m(x)(1-p_m(x))
\leq\rho_{\varepsilon,\delta}^2p_m(x),
\]
with \(a=|x|/\sqrt m\). This remains valid at correlations \(\rho=\pm1\) by \(L^2\) continuity. The exact signed-pair average is
\[
4^{-m}\sum_{\varepsilon,\delta}\rho_{\varepsilon,\delta}^2
=\frac1{m^2}\sum_{j,k=1}^{m}\mathbb E_\varepsilon[\varepsilon_j\varepsilon_k]\mathbb E_\delta[\delta_j\delta_k]
=\frac1m.
\]
Therefore
\[
\operatorname{Var}(X_{n,i}\mid Z_i=x)\leq\frac{p_m(x)}m.
\]
There is no assumption of independence among the cube-edge indicators.

**3. Quantitative convergence.** Let \(c=\sqrt{2/\pi}\). Direct Gaussian integration gives
\[
\sqrt m\,p_m(x)=c\int_0^{|x|}e^{-t^2/(2m)}\,dt,
\qquad
0\leq c|x|-\sqrt m\,p_m(x)\leq\frac{c|x|^3}{6m},
\]
where the second inequality follows from \(1-e^{-u}\leq u\) for \(u\geq0\). Since \(\mathbb E|Z_i|^6=15\), the squared bias averaged over \(Z_i\) is at most \(5/(6\pi m^2)\). By the conditional variance decomposition,
\[
\mathbb E[(\sqrt m X_{n,i}-c|Z_i|)^2]
=m\mathbb E[\operatorname{Var}(X_{n,i}\mid Z_i)]
+\mathbb E[(\sqrt m\,p_m(Z_i)-c|Z_i|)^2].
\]
Moreover, for independent standard Gaussians \(A,B\), the Cauchy ratio \(A/B\) gives
\[
\mathbb E p_m(Z_i)
=\mathbb P(|\sqrt m A|<|B|)
=\frac2\pi\arctan\frac1{\sqrt m}.
\]
Combining these identities proves the displayed mean-square inequality. Its right-hand side tends to zero; summing it over fixed \(r\) proves joint \(L^2\) convergence on the shared Gaussian probability space. Independence in the limiting vector is inherited from \((Z_1,\ldots,Z_r)\).

**4. Variance and normalization.** The exact directional mean, previously implicit in known expected face-count formulas, is
\[
\mathbb E V_{n,i}=2^{n-1}\frac2\pi\arctan\frac1{\sqrt{n-1}}.
\]
Convergence in \(L^2\) implies convergence of first and second moments. As \(\mathbb E|Z_i|=c\) and \(\operatorname{Var}(|Z_i|)=1-2/\pi\), the limiting variance is \(c^2(1-2/\pi)\), which is \(2/\pi-4/\pi^2\). For distinct fixed indices, limiting covariance vanishes by the joint convergence and independence of the limit. Dividing by the exact mean yields the normalized half-normal limit.

## Verification
Run the standalone file `verify.py` with Python 3 and NumPy. It independently enumerates actual cube edges and compares crossing signs with the threshold-sum formulation for generic integer normal vectors in dimensions \(3\) through \(9\). A seeded Gaussian experiment compares the empirical mean-square errors with the proven upper bound for dimensions \(3,5,8,12\). The recorded local execution returned `DIRECTIONAL_CUBE_SANITY_OK`. This finite check detects indexing and normalization mistakes; the proof of the all-dimensional limit is the analytic Hermite and conditional-variance argument above, not the simulation.

## Relationship to prior work
Brandenburg and Meroni [1] classify combinatorial types of central cube sections in dimensions up to seven, and identify intercepted edges as the vertices of generic sections. They report Lonke's earlier expected-vertex formula [2]. The present result instead studies the *random vector of counts grouped by coordinate direction* as dimension tends to infinity, giving its nondegenerate joint limiting law and an explicit \(L^2\) bound. Lonke [2] establishes the expectation for the total number of vertices; it does not give this directional fluctuation law. Calkin and collaborators [3] investigate probabilities that one or two specified cube edges are intersected by random hyperplanes, as well as multihyperplane covering problems. Those fixed-event probabilities do not state or imply the directional joint half-normal limit without the additional dependence control and scaling argument above. The exact one-edge probability and the total-mean identity are established prior work and are **not claimed as new**.

## Limitations
The result concerns Haar-uniform **central codimension-one** sections only. It does not address noncentral hyperplanes, different distributions of normals, growing numbers of designated coordinate directions, other face dimensions, or the full law of the total number of section vertices. The \(L^2\) error bound is explicit but not claimed to be sharp. The literature comparison supports, but cannot establish absolutely, the absence of an equivalent unindexed result; independent review remains outstanding.

## References
[1] M.-C. Brandenburg and C. Meroni, *Combinatorics of slices of cubes*, arXiv:2510.09265v1 (first posted 10 October 2025), https://arxiv.org/abs/2510.09265.

[2] Y. Lonke, *On random sections of the cube*, arXiv:math/9812123v1 (21 December 1998); *Discrete & Computational Geometry* 23 (2000), 157–169, https://arxiv.org/abs/math/9812123.

[3] N. Calkin, K. James, J. B. Light, R. Myers, E. Riedl, and V. Thomas, *Cuts of the Hypercube* (3 July 2008), https://www.researchgate.net/publication/254361748_Cuts_of_the_Hypercube.
