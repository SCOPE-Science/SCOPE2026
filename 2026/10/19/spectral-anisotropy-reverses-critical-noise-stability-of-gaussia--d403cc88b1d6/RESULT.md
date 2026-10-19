# Spectral anisotropy reverses critical-noise stability of Gaussian randomized Newton

## Finding

Consider the exact Gaussian-perturbed full-Newton iteration with objective-dependent noise amplitude introduced in Huynh and Engquist (2026). On every positive-definite quadratic, its objective values admit a complete three-regime pathwise classification. At the borderline noise exponent, **rearranging the Hessian eigenvalues while preserving their sum can reverse almost-sure convergence without changing the expected objective at any iteration**.

**Theorem.** Fix an integer \(d\ge1\), a real symmetric positive-definite \(d\times d\) matrix \(A\), a nonzero deterministic \(X_0\in\mathbb R^d\), and \(\alpha\ge0\). Let \(Z_n\) be independent standard Gaussian \(d\)-vectors. For
\[
f_A(x)=\tfrac12x^{\mathsf T}Ax,\qquad
X_{n+1}=X_n-A^{-1}\nabla f_A(X_n)+f_A(X_n)^\alpha Z_n,
\]
put \(F_n=f_A(X_n)\), \(p=2\alpha\), and
\[
W=\tfrac12 Z^{\mathsf T}AZ,\qquad
\mu(A)=\mathbb E\log W,
\]
where \(Z\) is standard Gaussian in \(\mathbb R^d\). Then all of the following statements hold.

**Subcritical exponent \(0\le\alpha<1/2\).** The positive random variables \(F_n\) converge in distribution to the unique positive stationary objective law
\[
F_\infty\ \overset d=\ \exp\!\left(\sum_{j=0}^\infty p^j\log W_j\right),
\]
where the \(W_j\) are independent copies of \(W\). Almost surely, \(\liminf_{n\to\infty}F_n=0\) and \(\limsup_{n\to\infty}F_n=+\infty\): stationary behavior here is not trajectory convergence. For real \(q\),
\[
\mathbb E[F_\infty^q]=\prod_{j=0}^\infty \mathbb E[W^{qp^j}]<\infty
\quad\Longleftrightarrow\quad q>-d/2.
\]
In the isotropic case \(A=aI_d\), each product factor is exactly
\(a^{qp^j}\Gamma(d/2+qp^j)/\Gamma(d/2)\).

**Critical exponent \(\alpha=1/2\).** For every \(X_0\ne0\),
\[
\lim_{n\to\infty}\frac1n\log\frac{F_n}{F_0}=\mu(A)
\qquad\text{almost surely}.
\]
Thus \(F_n\to0\) almost surely if \(\mu(A)<0\), while \(F_n\to\infty\) almost surely if \(\mu(A)>0\). If \(\mu(A)=0\), almost surely \(\liminf F_n=0\) and \(\limsup F_n=\infty\). At this same exponent, for every integer \(n\ge0\),
\[
\mathbb E F_n=F_0\left(\frac{\operatorname{tr}A}{2}\right)^n.
\]
Hence mean objective growth is blind to eigenvalue allocation, unlike the almost-sure exponent.

**Supercritical exponent \(\alpha>1/2\).** Define the almost-surely convergent random series
\[
S=\log F_0+\sum_{j=0}^\infty p^{-j-1}\log W_j.
\]
The events \(S<0\) and \(S>0\) each have strictly positive probability and exhaust probability one. Moreover
\[
\frac{\log F_n}{p^n}\longrightarrow S\quad\text{almost surely},
\]
so \(F_n\to0\) on \(S<0\), whereas \(F_n\to\infty\) on \(S>0\). Neither outcome has probability one for a fixed nonzero initial point on the unbounded quadratic domain.

**Sharp spectral frontier at \(\alpha=1/2\).** For fixed trace \(\tau=\operatorname{tr}A\) and \(d\ge2\), \(\mu(A)\) is a strictly Schur-concave function of the eigenvalue vector. Quantitatively,
\[
\log\tau+\psi(1/2)<\mu(A)\le\log(\tau/d)+\psi(d/2),
\]
where \(\psi\) is the digamma function; the upper endpoint is attained only for \(A=(\tau/d)I_d\), and the lower endpoint is approached as the spectrum concentrates into one eigenvalue. The corresponding limiting critical traces are \(d\exp(-\psi(d/2))\) (isotropic) and \(4\exp(\gamma)\) (rank-one limit), where \(\gamma\) is Euler's constant.

In dimension two, with eigenvalues \(\lambda_1,\lambda_2>0\), the exact exponent is
\[
\boxed{\displaystyle
\mu(A)=-\gamma+2\log\!\left(\frac{\sqrt{\lambda_1}+\sqrt{\lambda_2}}2\right).}
\]
Thus, at the critical noise exponent, **almost-sure convergence occurs exactly when**
\[
\boxed{\sqrt{\lambda_1}+\sqrt{\lambda_2}<2e^{\gamma/2}.}
\]
Equality gives oscillation, and the reversed inequality gives almost-sure explosion. For any fixed trace \(\tau\) strictly between \(2e^\gamma\) and \(4e^\gamma\), the isotropic matrix is almost-surely divergent but a sufficiently anisotropic positive-definite matrix of the same trace is almost-surely convergent; both have identical exponentially growing expected objectives. For example, \(A=\operatorname{diag}(2,2)\) has \(\mu(A)\approx0.1159315\), while \(A=\operatorname{diag}(3.9,0.1)\) has \(\mu(A)\approx-0.3054725\). Starting both systems from the common vector \(X_0=(1,1)\) makes \(F_0=2\) in both, and therefore both have exactly \(\mathbb E F_n=2^{n+1}\) at every step.

## Assumptions and scope

The iteration is exactly the full-Newton stochastic rule with no projection, finite-precision error, damping, approximate Hessian, or artificial noise cutoff. The objective is the unbounded positive-definite quadratic on \(\mathbb R^d\); it is **not** an objective on the torus. The Gaussian draws are i.i.d. \(N(0,I_d)\), independent of the deterministic nonzero initial vector, and the noise amplitude uses the objective's known minimum zero. All assertions of almost-sure convergence concern the same infinite sequence of draws. The case \(X_0=0\) is excluded to avoid the distinct absorbing convention at the optimizer; for \(\alpha>0\) it is trivially absorbing.

The parameter \(\alpha\) is the exponent on the **function value** in the noise amplitude, not the exponent on the distance to the minimizer. A limiting rank-one spectrum is used only for the trace envelope, not as a singular Hessian in the theorem.

## Proof

**1. Exact log-energy representation and regularity.** For a quadratic, \(\nabla f_A(x)=Ax\), so its deterministic full-Newton step is identically zero. Since \(F_0>0\) and Gaussian vectors are nonzero almost surely, \(F_n>0\) for all finite \(n\), almost surely. Substitution gives the exact identity
\[
F_{n+1}=W_n F_n^p,\qquad W_n=\tfrac12 Z_n^{\mathsf T}AZ_n.
\]
Writing \(U_n=\log F_n\) and \(V_n=\log W_n\) reduces the entire iteration to
\[
U_{n+1}=pU_n+V_n.
\]
The \(V_n\) are i.i.d. with a continuous nondegenerate distribution of full support on \(\mathbb R\). Indeed, \((\lambda_{\min}/2)\|Z\|_2^2\le W\le(\lambda_{\max}/2)\|Z\|_2^2\), which also implies \(\mathbb E|V|^k<\infty\) for every finite \(k>0\).

**2. Subcritical regime.** When \(0\le p<1\), the explicit solution
\[
U_n=p^nU_0+\sum_{j=0}^{n-1}p^jV_{n-1-j}
\]
has the same distribution as a reversed independent partial sum converging to \(U_\infty=\sum_{j\ge0}p^jV_j\). The sum converges absolutely almost surely by \(\sum_jp^j\mathbb E|V|<\infty\). A two-sided sequence of innovations constructs a stationary ergodic realization \(U_n^*=\sum_{j\ge0}p^jV_{n-1-j}\) with \(U_n-U_n^*=p^n(U_0-U_0^*)\to0\) almost surely. Its marginal has full support, so Birkhoff's theorem applied to each integer upper and lower level yields the asserted recurrent extremes of the original forward iterates. This also proves uniqueness of the stationary law by the contraction coupling.

Near zero the density of \(W\) behaves in power order \(w^{d/2-1}\), because \(A\) is positive definite and \(W\) is bounded above and below by fixed multiples of a \(\chi_d^2\) random variable. Therefore \(\mathbb E W^q<\infty\) exactly for \(q>-d/2\). Independence gives the Mellin product first for finite sums. Since \(\log\mathbb EW^t=t\mathbb EV+O(t^2)\) near \(t=0\), the infinite product converges whenever \(q>-d/2\); a slightly larger absolute moment supplies uniform integrability for passage to the limit. If \(q\le-d/2\), the first independent factor already has infinite expectation. For \(A=aI_d\), \(W=a\chi_d^2/2\), proving the gamma factors.

**3. Critical and supercritical regimes.** When \(p=1\), the increments form a finite-variance random walk \(U_n=U_0+\sum_{j<n}V_j\). The strong law gives its almost-sure drift \(\mu(A)\). At zero drift, the classical iterated-logarithm law for nondegenerate centered finite-variance independent increments gives both infinite upper and lower excursions. Meanwhile \(\mathbb E W=\operatorname{tr}(A)/2\), so conditioning successively yields the exact finite-step expectation formula.

When \(p>1\), dividing the explicit affine solution by \(p^n\) yields
\[
p^{-n}U_n=U_0+\sum_{j=0}^{n-1}p^{-j-1}V_j\ \longrightarrow S.
\]
The series converges absolutely by its summable weights and \(\mathbb E|V|<\infty\). Its first independent summand has an absolutely continuous full-support law, so \(S\) has no atom at zero and both signs have positive probability. Its sign gives the asserted almost-sure objective outcome and rate.

**4. Spectral comparison and the two-dimensional constant.** Orthogonal invariance gives
\(\mu(A)=\mathbb E\log(\tfrac12\sum_i\lambda_iZ_i^2)\). On the positive eigenvalue cone, its directional second derivative along any nonzero real vector \(h\) is
\[
-\mathbb E\frac{(\sum_i h_iZ_i^2)^2}{(\sum_i\lambda_iZ_i^2)^2}<0.
\]
The expectation is finite locally, so \(\mu\) is strictly concave and symmetric in the eigenvalues, hence strictly Schur-concave. At fixed sum \(\tau\), averaging all eigenvalues maximizes it, while concavity forces its infimum to the simplex vertices. The chi-square log identity \(\mathbb E\log(\chi_k^2/2)=\psi(k/2)\) gives the claimed extrema; continuity in the rank-one limit follows by bounding the logarithm between the log of a one-coordinate chi-square and the log of the total chi-square with coefficients depending only on \(\tau,d\).

For \(d=2\), write \(Z=R(\cos\theta,\sin\theta)\), with \(R^2/2\) exponential of mean one and \(\theta\) uniform. Then \(\mathbb E\log(R^2/2)=-\gamma\). Put \(a=(\sqrt{\lambda_1}+\sqrt{\lambda_2})/2\) and \(b=(\sqrt{\lambda_1}-\sqrt{\lambda_2})/2\). The angular factor satisfies
\(\lambda_1\cos^2\theta+\lambda_2\sin^2\theta=|ae^{i\theta}+be^{-i\theta}|^2\), with \(|b|<a\). Expanding \(\log(1+(b/a)e^{-2i\theta})\) in its uniformly convergent Fourier series shows that the angular average of the log is \(2\log a\). This proves the closed formula. At trace \(\tau\), the isotropic exponent is \(\log(\tau/2)-\gamma\), whereas the rank-one limit is \(\log(\tau/4)-\gamma\). Their opposite signs on the interval \(2e^\gamma<\tau<4e^\gamma\), together with trace invariance of \(\mathbb E F_n\), prove the claimed stability reversal.

## Verification

The standalone file `verify.py` recomputes the Gaussian log-energy recursion, two-dimensional angular log integral, critical spectral thresholds, isotropic stationary Mellin cumulants, and the expanding-log recursion, using deterministic quadrature and fixed-seed simulation only as cross-checks. A clean execution printed `PASS: 1927 finite exact-identity and numerical checks`, with log-drift values approximately \(0.1159315156584\) and \(-0.3054725200173\) for the two trace-matched examples. These finite checks do not establish pathwise infinite-time assertions or uniqueness; those follow from the proof above.

## Relationship to prior work

Huynh and Engquist (2026, arXiv:2609.10465v1) define the same state-dependent Gaussian perturbation of full Newton and prove global almost-sure results on a **compact torus** under exponent \(\alpha>1\), with a further shrinking-tube result for \(\alpha>1/2\). Their Theorem 2.15, Lemma 2.18 and Remark 2.20 do not give the critical-exponent spectral transition, the unbounded-quadratic three-regime classification, or the same-trace reversal of almost-sure and mean behavior derived here.

The affine log recurrence, its stationary perpetuity, and the theory of random iterated functions are classical; these components are not claimed as inventions (see Diaconis and Freedman). Classical comparisons of Gaussian quadratic forms and their inverse moments likewise predate this work (Bakirov; Jones). The specific conjunction assessed here is the exact noisy-Newton stability classification and its **sharp spectral allocation criterion** at the critical noise exponent, not the Gaussian integral or autoregression in isolation.

## Limitations

The full-Newton map vanishes exactly only on homogeneous quadratic objectives, so no corresponding formula is asserted for general nonconvex functions, approximate Newton solvers, state-dependent Gaussian covariance, or other noise laws. The lack of torus wrapping is essential: supercritical exploding trajectories here do not contradict the compact-domain theorem in the motivating paper. At the critical exponent, pathwise stability and expected loss can disagree strongly; an almost-sure claim is not a mean-square guarantee. The historical overlap search cannot exclude all differently phrased or unindexed applications of affine stochastic recursions.

## References

1. E. Huynh and B. Engquist, *Convergence of a Randomized Newton Method in Nonconvex Optimization*, arXiv:2609.10465v1, first posted September 9, 2026. https://arxiv.org/abs/2609.10465
2. P. Diaconis and D. Freedman, *Iterated Random Functions*, SIAM Review 41 (1999), 45–76; accessible author preprint https://statistics.berkeley.edu/sites/default/files/tech-reports/511.pdf
3. N. K. Bakirov, *Comparison Theorems for Distribution Functions of Quadratic Forms of Gaussian Vectors*, Theory of Probability and Its Applications 40 (1996), 340–348. https://doi.org/10.1137/1140035
4. M. C. Jones, *Expressions for Inverse Moments of Positive Quadratic Forms in Normal Variables*, Australian Journal of Statistics 28 (1986), 242–250. https://doi.org/10.1111/j.1467-842X.1986.tb00604.x
