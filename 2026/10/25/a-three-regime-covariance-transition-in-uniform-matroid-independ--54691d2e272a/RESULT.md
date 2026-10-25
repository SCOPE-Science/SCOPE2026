# A three-regime covariance transition in uniform-matroid independence polytopes

## Finding
For integers \(n\ge2\) and \(1\le k\le n\), let the full-dimensional uniform-matroid independence polytope be
\[
P_{n,k}=\operatorname{conv}\{\mathbf1_A:A\subseteq[n],\ |A|\le k\}=[0,1]^n\cap\{x:\sum_i x_i\le k\}.
\]
Let \(X\) be uniform with respect to Euclidean \(n\)-volume on \(P_{n,k}\), \(S=\sum_iX_i\), and let \(\lambda_{\perp}(n,k)\) and \(\lambda_{\parallel}(n,k)\) denote its covariance eigenvalues on the zero-sum hyperplane and on the span of \(\mathbf1\), respectively. The former has multiplicity \(n-1\). The following complete large-dimensional regimes hold for integer sequences \(k=k_n\).

**Central window.** If \(t_n=(k_n-n/2)/\sqrt{n/12}\to t\in\mathbb R\), then
\[
\lambda_{\perp}(n,k_n)\to1/12,\qquad
\lambda_{\parallel}(n,k_n)\to[1-t r(t)-r(t)^2]/12,
\quad r(t)=\varphi(t)/\Phi(t).
\]
The second limit is positive and strictly below \(1/12\). At the **exact balanced integer cut** \(n\) even, \(k=n/2\), the stronger all-dimensional identity is
\[
\boxed{\lambda_{\perp}(n,n/2)=1/12},\qquad
\boxed{\lambda_{\parallel}(n,n/2)=1/12-\frac{[\mathbb E|T_n-n/2|]^2}{n}},
\]
where \(T_n\) is a sum of \(n\) independent \(\operatorname{Unif}[0,1]\) variables. Consequently the balanced transverse-to-parallel anisotropy tends to \(1/(1-2/\pi)\).

**Subcritical window.** Suppose \(k_n/n\ge\epsilon>0\), \(k_n/n<1/2\), and define the unique \(\theta_n<0\) by \(\mu(\theta_n)=k_n/n\), where
\[
M(\theta)=\frac{e^\theta-1}{\theta},\quad
\mu(\theta)=\frac{d}{d\theta}\log M(\theta),\quad
v(\theta)=\frac{d^2}{d\theta^2}\log M(\theta)>0.
\]
If \(|\theta_n|\sqrt n\to\infty\), then
\[
\boxed{\lambda_{\perp}(n,k_n)=v(\theta_n)+o(1)},\qquad
\boxed{n\theta_n^2\lambda_{\parallel}(n,k_n)\to1}.
\]
In particular, for \(k_n/n\to a\in(0,1/2)\), \(\lambda_{\parallel}\sim [n\theta_a^2]^{-1}\), whereas \(\lambda_{\perp}\to v(\theta_a)>0\). Thus the covariance becomes asymptotically singular in precisely the global-sum direction, while its other \(n-1\) directions retain positive variance. Moreover \(\lambda_{\perp}/\lambda_{\parallel}\sim n\theta_n^2v(\theta_n)\) in this regime.

**Supercritical window.** If \((k_n-n/2)/\sqrt n\to+\infty\), then both eigenvalues converge to \(1/12\).

There is also an affine-invariant consequence. Define \(L(P)=(\det\operatorname{Cov}(X))^{1/(2n)}/\operatorname{Vol}_n(P)^{1/n}\). For fixed \(a\in(0,1/2)\) and \(k_n/n\to a\),
\[
\boxed{L(P_{n,k_n})\to \sqrt{v(\theta_a)}\exp\{\theta_a a-\log M(\theta_a)\}}.
\]
The right-hand side tends to \(1/e\) as \(a\downarrow0\) and to \(1/\sqrt{12}\) as \(a\uparrow1/2\). For any integer sequence \(k_n/n\to a\ge1/2\), \(L(P_{n,k_n})\to1/\sqrt{12}\), even though the global-direction covariance has a nontrivial limiting deficit in the central window.

## Assumptions and scope
All volumes are ordinary Lebesgue volumes in \(\mathbb R^n\). The cap \(k\) is an **integer** rank, so \(P_{n,k}\) is the independence polytope of the uniform matroid; its equality with the capped cube follows from the totally unimodular single-row rank inequality (or by observing that all vertices are Boolean). All limits are taken as \(n\to\infty\), with \(\epsilon\) fixed where indicated. \(\Phi,\varphi\) are standard-normal distribution and density. At \(\theta=0\), the analytic continuations are \(M(0)=1\), \(\mu(0)=1/2\), \(v(0)=1/12\). The isotropic constant uses the normalization in the displayed definition; no volumetric or moment normalizations are suppressed.

## Proof
**1. Exact covariance splitting.** The polytope is coordinate-permutation invariant, so \(\operatorname{Cov}(X)=\lambda_{\perp}(I-J/n)+\lambda_{\parallel}J/n\), with \(J=\mathbf1\mathbf1^T\). Since \(\operatorname{Var}(S)=n\lambda_{\parallel}\) and \(\mathbb E(X_1-X_2)^2=2\lambda_{\perp}\),
\[
\lambda_{\parallel}=\operatorname{Var}(S)/n,\qquad \lambda_{\perp}=\mathbb E(X_1-X_2)^2/2.
\]
Both are positive for every \(1\le k\le n\). For independent \(U_i\sim\operatorname{Unif}[0,1]\), the joint law of \(X\) is exactly \((U_1,\ldots,U_n)\) conditioned on \(T_n=\sum_iU_i\le k\). This proves the claimed geometric-to-probabilistic equivalence, not merely equality of one statistic.

**2. Exact balanced cut.** When \(k=n/2\), the reflection \(U_i\mapsto1-U_i\) interchanges \(\{T_n<n/2\}\) with its complement and fixes \((U_1-U_2)^2\). Its conditional expectation on the lower half therefore equals its unconditional expectation \(1/6\), giving \(\lambda_{\perp}=1/12\). Reflection similarly fixes \((T_n-n/2)^2\), whose conditional expectation is \(n/12\). Writing \(A_n=\mathbb E|T_n-n/2|\), reflection implies \(\mathbb E[T_n-n/2\mid T_n\le n/2]=-A_n\). Thus the conditional variance of \(T_n\) is \(n/12-A_n^2\), proving the exact identity. The ordinary CLT and uniform integrability of \((T_n-n/2)/\sqrt{n/12}\) give \(A_n^2/n\to (2/\pi)/12\), and hence the anisotropy limit.

**3. Central window.** Let \(Z_n=(T_n-n/2)/\sqrt{n/12}\). The CLT, bounded fourth moments, and truncation at \(Z_n\le t_n\) imply convergence of the first two conditional moments to those of a standard normal \(Z\) conditioned on \(Z\le t\). Direct Gaussian integration gives \(\mathbb E(Z\mid Z\le t)=-r(t)\) and \(\operatorname{Var}(Z\mid Z\le t)=1-t r(t)-r(t)^2\). This proves the longitudinal formula. For any fixed number of coordinates, their effect on \(Z_n\) is \(O(n^{-1/2})\), while the sum of the other coordinates converges to an independent Gaussian; consequently conditioning on \(Z_n\le t_n\) does not change their weak limit from independent uniforms. Boundedness upgrades convergence of squared coordinate differences to expectation convergence, giving \(\lambda_{\perp}\to1/12\).

**4. Strictly subcritical window.** Put \(a_n=k_n/n=\mu(\theta_n)\) and tilt each \(U_i\) to independent density \(q_{\theta_n}(u)=e^{\theta_n u}/M(\theta_n)\) on \([0,1]\). Because \(a_n\in[\epsilon,1/2)\), the parameters \(\theta_n\) lie in a fixed compact subinterval of \(( -\infty,0]\), and their variances remain bounded above and below. Let \(p_{m,\theta}\) be the density of a sum of \(m\) tilted variables. Uniform density local limit estimates, for \(m=n\) and \(n-r\) with fixed \(r\), follow by Fourier inversion: the centered characteristic functions of this compact family are uniformly quadratic near the origin, uniformly bounded away from one on fixed annuli, and \(O(1/|u|)\) at infinity, hence their \(m\)th powers have uniformly integrable tails. In particular,
\[
p_{n,\theta_n}(k_n-y)/p_{n,\theta_n}(k_n)\to1
\quad\text{uniformly for }0\le y=o(\sqrt n),
\]
with the ratio uniformly bounded on \(y\ge0\) by a constant. Under the conditioned original uniform law, the cap deficit \(Y_n=k_n-T_n\ge0\) consequently has density proportional to \(e^{\theta_n y}p_{n,\theta_n}(k_n-y)\). Since \(|\theta_n|\sqrt n\to\infty\), the scaled deficit \(|\theta_n|Y_n\) converges, including its first two moments, to a unit-rate exponential: \(\operatorname{Var}(T_n)=\operatorname{Var}(Y_n)\sim1/\theta_n^2\). For the first two original coordinates the same conditioning integral, replacing \(n\) by \(n-2\) and shifting its argument by the bounded coordinate sum, proves convergence of their joint law in total variation to the product of two tilted laws \(q_{\theta_n}\), with error tending to zero uniformly. Therefore \(\mathbb E[(X_1-X_2)^2]/2=v(\theta_n)+o(1)\). These statements give both subcritical limits.

**5. Supercritical window.** Hoeffding's bound gives \(\mathbb P(T_n>k_n)\le\exp[-2(k_n-n/2)^2/n]\to0\). The fourth moments of \((T_n-n/2)/\sqrt n\) are uniformly bounded; hence its first two moments conditioned on \(T_n\le k_n\) converge to their unconditional counterparts. Fixed-coordinate bounded observables likewise converge. This gives both eigenvalue limits.

**6. Isotropic constant.** For fixed \(a\in(0,1/2)\), standard exponential tilting as in step 4, or the elementary Chernoff upper bound together with a tilted central-limit lower bound, yields
\[
\lim_{n\to\infty}-n^{-1}\log\operatorname{Vol}_n(P_{n,k_n})=I(a):=\theta_a a-\log M(\theta_a).
\]
Meanwhile \(\det\operatorname{Cov}(X)=\lambda_{\perp}^{n-1}\lambda_{\parallel}\), with \(n^{-1}\log\lambda_{\parallel}\to0\) because \(\lambda_{\parallel}\asymp n^{-1}\). Thus the claimed isotropic-constant limit follows. As \(a\downarrow0\), \(\theta_a\sim-1/a\), \(v(\theta_a)\sim a^2\), and \(M(\theta_a)\sim a\), giving \(1/e\); continuity at \(\theta=0\) yields the other endpoint. For \(k_n/n\to a>1/2\), the cap has volume tending to one. If \(k_n/n\to1/2\), the volume fraction has logarithm \(o(n)\) (a fixed-width central strip supplies a lower bound \(e^{-o(n)}\)); further, the transverse eigenvalue tends to \(1/12\). In all sequences with \(k_n/n\to1/2\), this last claim follows by splitting into bounded, positive-diverging, and negative-diverging standardized cap subsequences using steps 3–5. The longitudinal eigenvalue contributes \(o(n)\) to the logarithmic determinant: for negative-diverging standardized caps approaching half rank, step 4 gives \(\lambda_{\parallel}\asymp[n\theta_n^2]^{-1}\), and for bounded or positive-diverging caps it has a positive limit. The fixed-rank boundary \(k\ge1\) never causes an exponential log-determinant effect at half rank. Hence \(L\to1/\sqrt{12}\).

## Verification
The companion standard-library script `check_covariance.py` independently evaluates the exact Irwin–Hall spline integrals for cube volume, the first two moments of \(S\), and the first two moments of \(X_1\) using rational arithmetic. On the integer parameter grid \(2\le n\le9\), \(1\le k\le n\), all \(44\) exact calculations yield positive eigenvalues and agree with the full-cube and simplex volume boundaries. Three independent rejection samples check the moments numerically; their counts, tolerances, and fixed seeds are in the checker. Reflection also gives an exact all-dimensional analytical check of the balanced eigenvalue. Numerical tests are corroborations only; the asymptotic statements depend on steps 3–6, not on finite sampling.

For a direct exact computational reconstruction, the Irwin–Hall formula at integer \(k\) is
\[
F_n(k)=\operatorname{Vol}(P_{n,k})=\frac1{n!}\sum_{j=0}^{k-1}(-1)^j\binom nj(k-j)^n.
\]
The unnormalized moments of \(S\) come from integrating \(s\,dF_n(s)\) and \(s^2\,dF_n(s)\) up to \(k\); those of \(X_1\) come from \(\int_0^1 x^p F_{n-1}(k-x)\,dx\) for \(p=0,1,2\). The checker implements these integrals exactly by binomial expansion, and reconstructs the two eigenvalues from the moment identities in step 1.

## Relationship to prior work
Ferroni's 2020 source [1] establishes the uniform-matroid independence polytope and studies its lattice-point enumerator through half-open hypersimplices; its quoted results concern Ehrhart coefficients rather than continuous uniform-volume covariance. Lasoń and Michałek [2] investigate algebraic properties and classifications of matroid polytopes. Ferroni [3] treats Ehrhart-positivity phenomena. Broniatowski and Caron [4, Sections 2 and 4] give far more general Gibbs-conditioning approximations and exponential boundary-overshoot laws for conditioned sums; these cover the fixed-coordinate tilt and exponential-deficit ingredients at method level. The independent-sum Gaussian central limit theorem, Irwin–Hall formula, exponential tilting, and local limit methods are classical; those ingredients and the generic overshoot phenomenon are **not** claimed to be new. The present claim is the geometric combination: exact balanced transverse rigidity, full longitudinal critical-window profile, the sharp subcritical order gap, and the affine-invariant isotropic limit within this polytope family. Conditional-limit/probability literature may contain equivalent components and merits additional specialist bibliography scrutiny; originality is limited to the precise package stated here.

## Limitations
The integer cap and Euclidean uniform-volume hypotheses are essential to the matroid-polytope identification; no result for arbitrary real caps, nonuniform measures, arbitrary matroids, or quantitative rates of the stated asymptotic errors is asserted. The subcritical theorem excludes cap proportions tending to zero, even though the endpoint limit of the fixed-proportion isotropic formula is computed. The local-limit proof is supplied in compact Fourier-inversion form rather than as a standalone quantitative error-bound lemma. The literature survey does not establish formal uniqueness, and independent mathematical validation has not been performed.

## References
1. Luis Ferroni, *Integer point enumeration on independence polytopes and half-open hypersimplices*, arXiv:2012.04711, first public 8 December 2020. https://arxiv.org/abs/2012.04711
2. Michał Lasoń and Mateusz Michałek, *Gorenstein matroids*, arXiv:2005.08359, first public 17 May 2020. https://arxiv.org/abs/2005.08359
3. Luis Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465, first public 10 May 2021. https://arxiv.org/abs/2105.04465
4. Michel Broniatowski and Virgile Caron, *Long runs under a conditional limit distribution*, Annals of Applied Probability 24 (2014), arXiv:1202.0731 (first submitted 3 February 2012). https://arxiv.org/abs/1202.0731
