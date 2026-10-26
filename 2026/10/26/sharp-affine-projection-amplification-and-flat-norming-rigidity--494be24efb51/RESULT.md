# Sharp affine-projection amplification and flat norming rigidity on superquadratic \(\ell_p\) balls

## Finding
Fix a real \(p\) with \(2<p<\infty\). For every integer \(d\ge1\), let
\[
B_p^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|^p\le1\}
\]
carry normalized Lebesgue measure \(\mu_{d,p}\). Denote by \(P_{d,p}\) the \(L^2(\mu_{d,p})\)-orthogonal projection onto the affine functions \(\operatorname{span}\{1,x_1,\ldots,x_d\}\), considered as an operator on bounded real functions. Its pointwise Lebesgue function is
\[
\Lambda_{d,p}(a)=\int_{B_p^d}|K_{d,p}(a,y)|\,d\mu_{d,p}(y),
\]
where \(K_{d,p}\) is the reproducing kernel. Put
\[
R_{d,p}(a)=d^{1/p-1/2}\|a\|_2\in[0,1],\qquad
c_p=\sqrt{\frac2\pi}\,p^{-1/p}\sqrt{\frac{\Gamma(1/p)}{\Gamma(3/p)}}.
\]
Then, with \(p\) fixed,
\[
\boxed{\lim_{d\to\infty}\sup_{a\in B_p^d}
\left|\frac{\Lambda_{d,p}(a)}{\sqrt d}-c_pR_{d,p}(a)\right|=0.}
\]
In particular,
\[
\boxed{\lim_{d\to\infty}\frac{\|P_{d,p}\|_{L^\infty\to L^\infty}}{\sqrt d}=c_p.}
\]
The sharp norm is approached asymptotically by the flat boundary points \(a_i=\pm d^{-1/p}\). More precisely, a sequence \(a^{(d)}\in B_p^d\) has \(\Lambda_{d,p}(a^{(d)})/\|P_{d,p}\|\to1\) if and only if
\[
R_{d,p}(a^{(d)})\to1,
\]
and this is equivalent to
\[
\frac1d\sum_{i=1}^d\big|d^{1/p}|a_i^{(d)}|-1\big|^p\to0.
\]
No assertion of exact finite-dimensional maximization by flat points is made. The constant has the endpoint shape limits \(\lim_{p\downarrow2}c_p=\sqrt{2/\pi}\) and \(\lim_{p\to\infty}c_p=\sqrt{6/\pi}\), from the elementary gamma-function asymptotics; these parameter limits are taken *after* the dimension limit.

## Assumptions and scope
The exponent \(p\in(2,\infty)\) is fixed while the dimension \(d\) tends to infinity; the underlying measure is *uniform volume measure*, not cone or surface measure. The projector includes both constants and all first-degree coordinate functions. All integrals are real-valued and the endpoint norm uses the essential supremum on the ball. The same norm is obtained on \(C(B_p^d)\) since continuous functions approximate the sign of each continuous kernel row in the integral. This finding concerns \(L^\infty\) amplification; it is not a claim about nearest-point projection in the geometric \(\ell_p\) norm.

## Proof
**1. Exact kernel and variance.** Symmetry under coordinate sign changes and permutations gives \(\mathbb E X_i=0\), \(\mathbb E X_iX_j=0\) for \(i\ne j\), and \(\mathbb E X_i^2=s_{d,p}^2\), for \(X\sim\mu_{d,p}\). Beta integration (or the independent-coordinate representation below) gives
\[
s_{d,p}^2=\frac{\Gamma(3/p)}{\Gamma(1/p)}
\frac{\Gamma(1+d/p)}{\Gamma(1+(d+2)/p)}.
\]
Consequently \(K_{d,p}(a,y)=1+s_{d,p}^{-2}\langle a,y\rangle\), and the displayed formula for \(\Lambda_{d,p}\) is exactly the row operator norm. Gamma-ratio asymptotics show
\[
d^{1/p}s_{d,p}\longrightarrow b_p:=p^{1/p}\sqrt{\Gamma(3/p)/\Gamma(1/p)}.
\]

**2. An independent-coordinate representation.** Let \(G_1,\ldots,G_d\) be independent symmetric variables with density
\[
\frac{p}{2\Gamma(1/p)}e^{-|u|^p}\,du,
\]
and let \(E\) be an independent exponential variable with mean one. The exact representation of normalized volume measure on \(B_p^d\) is
\[
X\overset{\mathrm d}=\frac{(G_1,\ldots,G_d)}{(\sum_i|G_i|^p+E)^{1/p}}.
\]
Writing \(v_p^2=\mathbb E G_1^2=\Gamma(3/p)/\Gamma(1/p)\), the law of large numbers yields \(d^{-1}(\sum_i|G_i|^p+E)\to1/p\) in probability. Therefore
\[
Q_d:=\frac{v_p}{s_{d,p}(\sum_i|G_i|^p+E)^{1/p}}\to1
\quad\text{in probability}.
\]
This representation and its normalization are as in Barthe--Guédon--Mendelson--Naor (2005); the operator-norm conclusions below are separate.

**3. Uniform Gaussian row limit away from zero profile.** For any nonzero \(a\in B_p^d\), define \(T_{d,a}=\langle a,X\rangle/(s_{d,p}\|a\|_2)\). Its second moment is exactly one. In the above coupling,
\[
T_{d,a}=Q_d\frac{\sum_i a_iG_i}{v_p\|a\|_2}.
\]
For every fixed \(\eta>0\), if \(R_{d,p}(a)\ge\eta\), then \(\max_i|a_i|/\|a\|_2\le(\eta d^{1/2-1/p})^{-1}\to0\). Since the \(G_i\) have zero mean, variance \(v_p^2\), and a finite third absolute moment, the weighted triangular-array central limit theorem applies uniformly to every such sequence of vectors. Indeed the Lyapunov fraction is at most
\[
\frac{\mathbb E|G_1|^3}{v_p^3}\,
\frac{\max_i|a_i|}{\|a\|_2}\to0.
\]
Slutsky's lemma, using \(Q_d\to1\), gives \(T_{d,a}\Rightarrow N(0,1)\) along any such sequence. The fixed second moment gives uniform integrability of \(|T_{d,a}|\). A subsequence contradiction therefore proves
\[
\sup_{R_{d,p}(a)\ge\eta}
\left|\mathbb E|T_{d,a}|-\sqrt{2/\pi}\right|\to0.
\]

**4. Uniform small-profile control and normalization.** The elementary inequality \(\big||1+u|-|u|\big|\le1\) gives
\[
\left|\frac{\Lambda_{d,p}(a)}{\sqrt d}-
\frac{R_{d,p}(a)}{d^{1/p}s_{d,p}}\mathbb E|T_{d,a}|\right|
\le d^{-1/2}.
\]
At \(a=0\) interpret the second term as zero. For \(R_{d,p}(a)<\eta\), Cauchy--Schwarz and \(\mathbb ET_{d,a}^2=1\) give \(\mathbb E|T_{d,a}|\le1\); thus both terms in the desired comparison are bounded by a constant times \(\eta\), up to \(d^{-1/2}\). For \(R_{d,p}(a)\ge\eta\), the uniform Gaussian row limit and \(d^{1/p}s_{d,p}\to b_p\) apply. First let \(d\to\infty\), then \(\eta\downarrow0\). The uniform formula follows with \(c_p=\sqrt{2/\pi}/b_p\). Hölder's inequality gives \(R_{d,p}(a)\le1\), and equality holds for all flat sign vectors, proving the norm limit.

**5. Exact characterization of asymptotically maximizing evaluation points.** The uniform law and strictly positive \(c_p\) make near-maximization equivalent to \(R_{d,p}(a^{(d)})\to1\). Let \(z_i=d^{1/p}|a_i|\), \(y_i=z_i^p\ge0\), and \(\theta=2/p\in(0,1)\). The ball constraint says \(d^{-1}\sum y_i\le1\), while \(R_{d,p}(a)^2=d^{-1}\sum y_i^\theta\). If the latter tends to one, Jensen's inequality forces \(d^{-1}\sum y_i\to1\). The strictly positive defect
\[
\phi(y)=1+\theta(y-1)-y^\theta\ge0
\]
vanishes only at \(y=1\), and its empirical mean tends to zero. Since \(\phi(y)\) grows linearly for large \(y\), splitting at a large cutoff and then removing a neighborhood of one proves \(d^{-1}\sum|y_i-1|\to0\). The scalar inequality \(|z-1|^p\le|z^p-1|\) for \(z\ge0\) yields the claimed \(p\)-mean flatness. Conversely, this flatness forces \(\|z\|_{L^2(\{1,\ldots,d\})}\to1\) by Hölder and the triangle inequality, hence \(R_{d,p}(a)\to1\).

## Verification
The proof is self-contained once the cited independent-coordinate realization of uniform \(\ell_p\)-ball volume is given; it can alternatively be derived by polar-coordinate gamma integration. The accompanying `check.py` directly implements the exact gamma-function variance and the volume-sampling representation. It checks the Euclidean special-case variance identities and compares Monte Carlo kernel-row norms with their proven asymptotic profiles for \(p\in\{3,4,6\}\), several dimensions, and flat, sparse, and half-supported evaluation vectors. These finite diagnostics test normalization only; they neither establish the uniform limit nor certify novelty. Numerical tolerances in the checker are explicitly statistical rather than proof thresholds.

## Relationship to prior work
Barthe--Guédon--Mendelson--Naor, *A probabilistic approach to the geometry of the \(\ell_p^n\)-ball* (2005), Theorem 1, gives the independent generalized-Gaussian/exponential representation used here. Its Section 2.2 and Theorem 7 estimate Khintchine-type moments up to multiplicative constants and do not identify the present sharp affine-projection coefficient or the equivalence class of all asymptotic maximizers. Figueroa (2016) studies orthogonal polynomial projections for weighted *Euclidean* unit balls in Sobolev norms as polynomial degree varies, not the uniform-norm fixed-degree, growing-dimension asymptotic on superquadratic balls. Distinct previous sharp affine projection calculations on Euclidean balls, parallelepipeds, and cross-polytopes do not cover the continuous family of finite \(p>2\) balls via affine equivalence. A bibliographic record for Sündermann (1984) on projection constants for unit-ball polynomial spaces was located, but its full text could not be obtained; the extent of possible overlap remains an explicit uncertainty.

## Limitations
Only fixed finite \(p>2\) is proved. There is no uniformity in \(p\) as \(p\to2\) or \(p\to\infty\), no exact finite-dimensional maximizing-point classification, and no claim about higher-degree polynomial spaces or cone measure. The statistical checker is not a proof. The originality comparison is based on identified sources and accessible material; unindexed equivalent formulations and the inaccessible Sündermann paper remain possible. Independent scientific validation has not been performed.

## References
1. F. Barthe, O. Guédon, S. Mendelson and A. Naor, *A probabilistic approach to the geometry of the \(\ell_p^n\)-ball*, Annals of Probability 33 (2005), 480--513; arXiv:math/0503650, first posted 2005-03-29. Theorem 1 and Section 2.2.
2. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit ball*, arXiv:1607.00930 (first posted 2016-07-04), especially Theorem 1.1 and Section 1.
3. B. Sündermann, *On projection constants of polynomial spaces on the unit ball in several variables*, Mathematische Zeitschrift 188 (1984), 111--117, DOI:10.1007/BF01163879; bibliographic record only, full text unavailable in this comparison.
