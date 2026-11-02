# A density-universal collision law and exact Gaussian positivity benchmark for affine least-squares quadrature

## Finding

For \(n\ge2\), consider unmodified minimum-Euclidean-norm weights that integrate affine functions exactly using \(n\) independently sampled nodes from a centered density \(f\). The stability norm \(\kappa_n=\sum_i|w_i|\) has a polynomial tail of **exact exponent \(n-1\)** for every bounded compactly supported density continuous almost everywhere, and for every nondegenerate centered Gaussian density. Its coefficient splits into a one-dimensional concentration integral depending on \(f\) and a universal angular integral. For Gaussian nodes, the exact three-node positivity probability of the computed weights is an incomplete elliptic integral, strictly below the probability that positive affine-exact weights merely exist.

Write \(H_n=\{a\in\mathbb R^n:\sum_i a_i=0\}\), and \(\mathbb S_n\) for its Euclidean unit sphere with unnormalized surface measure \(d\sigma\); for \(n=2\), use the counting measure on the two-point sphere. Let \(A(a)=\sum_i|a_i|\). The principal identity is
\[
\Pr(\kappa_n>t)\sim C_n(f)t^{-(n-1)},\qquad
C_n(f)=\frac{\sqrt n}{n-1}\int_{\mathbb R}|m|^{n-1}f(m)^n\,dm\int_{\mathbb S_n}A(a)^{n-1}\,d\sigma(a).
\]
All displayed constants are strictly positive and finite under the stated assumptions. For the standard-normal density \(\varphi\),
\[
C_n(\varphi)=\frac{\sqrt n\,\Gamma(n/2)}{(n-1)(n\pi)^{n/2}}\int_{\mathbb S_n}A(a)^{n-1}\,d\sigma(a),
\qquad C_2(\varphi)=\frac2\pi,\qquad C_3(\varphi)=\frac29+\frac{\sqrt3}{3\pi}.
\]
For three independent Gaussian nodes the probability that *every computed least-norm weight* is strictly positive equals
\[
P_3^+=\frac3{\pi\sqrt3}F\left(\frac\pi3\middle|\frac23\right)
=0.6542087649561548\ldots,
\quad F(\phi\mid q):=\int_0^\phi\frac{du}{\sqrt{1-q\sin^2u}}.
\]
By comparison, existence of some strictly positive affine-exact weights has probability \(3/4\), so this is a genuine solver-dependent positivity deficit, not merely a convex-hull obstruction.

## Assumptions and scope

The target measure and sampling law coincide, have known mean zero, and have either (i) a bounded, compactly supported probability density continuous Lebesgue-almost everywhere or (ii) a centered Gaussian density with arbitrary positive variance. A general noncentered target is first centered at its known mean; all statements are translation and positive-scale invariant when the target is transformed correspondingly. For integer \(n\ge2\), the nodes are independent and identically distributed. Almost surely \(S:=\sum_{i=1}^n(X_i-\bar X)^2>0\), with \(\bar X=n^{-1}\sum_iX_i\). The unique Euclidean minimum-norm exact weights solve \(\sum_iw_i=1\) and \(\sum_iw_iX_i=0\), and are
\[
w_i=\frac1n-\frac{\bar X(X_i-\bar X)}{S}.
\]
The noise statement assumes independent centered scalar evaluation errors with common variance \(0<\sigma^2<\infty\), independent of the nodes; their conditional squared error has mean \(\sigma^2\sum_iw_i^2\). No positivity correction, resampling, clipping, or regularization is applied.

## Proof

**1. Exact weights and polar coordinates.** The minimum-norm solution is the projection of zero onto the two affine constraints. The displayed formula satisfies both constraints. It lies in the span of the vectors \((1,\ldots,1)\) and \((X_1,\ldots,X_n)\); that is the normal space of the constraint affine plane, proving minimality and uniqueness. Write \(X_i=m+ra_i\), with \(m=\bar X\), \(r=\sqrt S>0\), \(a\in\mathbb S_n\). Orthogonal decomposition into the constant vector and the centered hyperplane gives the exact Lebesgue-volume element
\[
\prod_{i=1}^n dX_i=\sqrt n\,r^{n-2}\,dm\,dr\,d\sigma(a).
\]
The weights simplify to \(w_i=1/n-(m/r)a_i\), whence the deterministic two-sided bound
\[
\frac{|m|A(a)}r-1\le\kappa_n\le\frac{|m|A(a)}r+1.
\]
These inequalities are uniform for all \(m,r,a\). The set \(\kappa_n>t\), for \(t>1\), is therefore sandwiched between the regions \(0<r<|m|A(a)/(t+1)\) and \(0<r<|m|A(a)/(t-1)\).

**2. Sharp tail constant.** The joint node density in these coordinates is \(\sqrt n\,r^{n-2}\prod_{i=1}^nf(m+ra_i)\). In the bounded-compact-support case, the sample mean remains in a fixed compact interval, and \(r=O(t^{-1})\) on either sandwich region, uniformly over this interval and the sphere. For almost every \(m\), continuity of \(f\) implies \(\prod_i f(m+ra_i)\to f(m)^n\). The density product is bounded, so dominated convergence applies to the radial integral after substituting \(r=|m|A(a)u/(t\pm1)\). Integrating \(u^{n-2}\) over \([0,1]\) gives the factor \(1/(n-1)\). The two sandwich limits agree and give exactly \(C_n(f)\). For \(f=\varphi\), the factorization \(\prod_i\varphi(m+ra_i)=(2\pi)^{-n/2}\exp[-(nm^2+r^2)/2]\) supplies a direct integrable dominating function, proving the same identity on the unbounded domain. Changing Gaussian scale leaves every weight invariant. The one-dimensional Gaussian moment evaluates as
\[
\int_{\mathbb R}|m|^{n-1}\varphi(m)^n\,dm
=\frac{\Gamma(n/2)}{(n\pi)^{n/2}}.
\]
This proves the stated Gaussian constant. Positivity of \(C_n(f)\) follows because \(f\) is a nondegenerate centered probability density and \(A(a)>0\) on the compact sphere.

**3. Moment and additive-noise thresholds.** For any nonnegative random variable \(K\) and \(p>0\), \(\mathbb E K^p=p\int_0^\infty t^{p-1}\Pr(K>t)\,dt\). The proven positive finite tail limit makes this integral finite exactly for \(p<n-1\), and divergent at equality as well. The Euclidean and \(\ell^1\) norms of the weight vector obey \(\kappa_n^2/n\le\sum_iw_i^2\le\kappa_n^2\). Consequently the mean conditional noise variance is finite iff \(n>3\). This is a statement about *unconditional squared amplification*, not deterministic accuracy or all moments.

**4. Gaussian constants at two and three nodes.** In the two-point sphere, \(A(a)=\sqrt2\) at each of two points, giving \(C_2(\varphi)=2/\pi\). For three nodes set \(a_j=\sqrt{2/3}\cos(\theta-2\pi j/3)\), \(j=0,1,2\). Then \(\sum_j a_j^2=1\), and direct piecewise integration of the absolute cosine products gives
\[
\int_{\mathbb S_3}A(a)^2d\sigma(a)
=2\pi+4\int_0^{2\pi}|\cos\theta\cos(\theta-2\pi/3)|d\theta
=4\sqrt3+\frac{8\pi}{3}.
\]
Substituting into the Gaussian constant gives \(C_3(\varphi)=2/9+\sqrt3/(3\pi)\).

**5. Exact Gaussian positivity probability.** Centered Gaussian sample means \(m\sim N(0,1/3)\) and residuals \(ra\) are independent, with \(r\sim\chi_2\) and uniform angle \(\theta\) on the residual circle. Conditional on \(m>0\), positivity of all computed weights is equivalent to \(0<m<r/[3\max_ja_j]\). For \(m<0\) use the analogous \(\min_ja_j\); symmetry makes both cases equal. For any fixed positive \(k\), elementary integration using \(\Pr(\chi_2>s)=e^{-s^2/2}\) gives
\[
\Pr\left(0<\sqrt3m<\frac{r}{\sqrt3k}\right)
=\frac1{2\sqrt{1+3k^2}}.
\]
As the circle traverses one of its three symmetric sectors, \(\max_ja_j=\sqrt{2/3}\cos\theta\) for \(|\theta|\le\pi/3\). Averaging and adding both signs of \(m\) yields
\[
P_3^+=\frac3\pi\int_0^{\pi/3}\frac{d\theta}{\sqrt{1+2\cos^2\theta}}
=\frac3{\pi\sqrt3}F\left(\frac\pi3\middle|\frac23\right).
\]
Independence and symmetry show \(\Pr(\min_iX_i<0<\max_iX_i)=1-2(1/2)^3=3/4\). The strict inequality \(P_3^+<3/4\) follows, for example, by comparing integrands or from the explicit positive-probability set of mixed-sign nodes with a negative least-norm weight. The strict positivity event has no boundary mass under the Gaussian density.

## Verification

The standalone `verify.py` deterministically checks the exact affine constraints, minimal-norm orthogonality, tail sandwich, angular constants, Gaussian normalization, numerical elliptic-integral identity, and compares seeded Monte Carlo positivity with the exact probability. The script is reproducible with Python 3 standard library (`python verify.py`); it reports its own count of checks and uses no publication-status assertions. Finite tests verify special cases only; the continuum tail and positivity identities follow from the proofs above.

## Relationship to prior work

Bělík, Narayan and Turnage (arXiv:2609.09506v1; publicly posted 2026-09-08) analyze randomized least-squares quadrature with high-probability stability and positivity guarantees; their complete manuscript was not accessible in this investigation, so a potentially stronger undiscovered statement in it remains an explicit priority risk. Migliorati and Nobile (arXiv:1812.07761; Journal of Approximation Theory 275 (2022), 105706), in the available published article including Section 3.2 and Theorem 6, treat randomized and weighted least-squares cubature with positivity guarantees at larger sample sizes, not the explicit density-factorized collision law and Gaussian three-node elliptic benchmark stated here.

An earlier result already established the heavy-tail exponent, norm-moment threshold, and explicit three-node positivity probability *for iid uniform nodes on* \([-1,1]\). The present theorem **does not claim that special case as original**. Indeed substituting \(f=(1/2)\mathbf1_{[-1,1]}\) recovers exactly its constant \(\sqrt n/[2^{n-1}n(n-1)]\) times the angular integral. The new mathematical content is the broad density-independent exponent with its sharp density-geometric coefficient and the separate exact Gaussian positivity benchmark. Specialized work on Gaussian-ratio probabilities and random cubature remains a historical-priority risk.

## Limitations

The theorem addresses one-dimensional affine-exact *unmodified* minimum-Euclidean-norm weights, with sampling from the centered target law. It does not cover arbitrary higher-degree spaces, weighted or regularized least squares, positivity-enforcing replacements, dependent nodes, or noisy node locations. The density conditions are sufficient, not claimed optimal; heavy-tailed non-Gaussian sampling distributions are outside the proof. A finite-noise-variance threshold does not imply small error constants or high-probability positivity. Independent mathematical review and exhaustive historical-priority confirmation have not been performed.

## References

1. F. Bělík, A. Narayan, J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1 (public 2026-09-08), https://arxiv.org/abs/2609.09506.
2. G. Migliorati and F. Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension*, arXiv:1812.07761 (2018); *Journal of Approximation Theory* 275 (2022), 105706, DOI 10.1016/j.jat.2022.105706, https://doi.org/10.1016/j.jat.2022.105706.
