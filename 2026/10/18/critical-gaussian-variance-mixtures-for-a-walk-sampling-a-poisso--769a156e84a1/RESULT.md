# Critical Gaussian-variance mixtures for a walk sampling a Poisson particle field

## Finding

A stationary one-dimensional Poisson system of independent symmetric random walks is sampled at integer times along an independent, almost unbiased nearest-neighbor walk. At the diffusive drift scale, a first-rank polynomial statistic converges to a **non-Gaussian normal variance mixture**, jointly with the sampling walk. This identifies an explicit critical window between the fixed nonzero-drift normal approximation of Huang–Rang–Su [1] and the unresolved symmetric-sampling distribution noted in their Appendix A.

Fix an intensity \(\lambda>0\). At each \(y\in\mathbb Z\), initially place an independent \(\operatorname{Poisson}(\lambda)\) number of particles; every particle thereafter makes independent, symmetric, nearest-neighbor steps on \(\mathbb Z\). Write \(\xi(i,x)\) for the number at site \(x\) at time \(i\). Independently, for each integer \(n\ge1\), start a nearest-neighbor observer \(S^{(n)}_0=0\) whose increments equal \(+1\) with probability \((1+v_n)/2\), and \(-1\) otherwise, where \(v_n\in[-1,1]\) and \(\sqrt n\,v_n\to\kappa\in\mathbb R\). The observer may be coupled arbitrarily between different values of \(n\); only its within-row law and independence from the particle field are used.

Let \(\varphi:\mathbb N_0\to\mathbb R\) be a fixed polynomial and \(P\sim\operatorname{Poisson}(\lambda)\). Assume its first Poisson–Charlier coefficient
\[
c_1=\mathbb E[\varphi(P+1)-\varphi(P)]\ne0.
\]
Write \(\mu_\varphi=\mathbb E\varphi(P)\) and
\[
Y_n=\sum_{i=1}^{n}\bigl(\varphi(\xi(i,S^{(n)}_i))-\mu_\varphi\bigr).
\]
Linearly interpolate \(s_n(t)=S^{(n)}_{\lfloor nt\rfloor}/\sqrt n\) between successive time points. For a continuous function \(f:[0,1]\to\mathbb R\) set
\[
\mathcal V_\lambda(f)=\frac{4\lambda}{\sqrt{2\pi}}\int_{0<s<t<1}\frac{\exp\!\bigl(-(f(t)-f(s))^2/[2(t-s)]\bigr)}{\sqrt{t-s}}\,ds\,dt.
\]
Let \(B_\kappa(t)=B(t)+\kappa t\), where \(B\) is standard Brownian motion, and let \(Z\sim N(0,1)\) be independent of \(B\). Then **jointly in \(C([0,1])\times\mathbb R\)**,
\[
\boxed{\quad(s_n,n^{-3/4}Y_n)\ \Rightarrow\ (B_\kappa,c_1\sqrt{\mathcal V_\lambda(B_\kappa)}\,Z).\quad}
\]
The second coordinate is non-Gaussian for every finite \(\kappa\). Its asymptotic variance is explicitly
\[
\boxed{\quad\lim_{n\to\infty}n^{-3/2}\operatorname{Var}(Y_n)
=\frac{2\lambda c_1^2}{\sqrt\pi}\int_0^1(1-u)u^{-1/2}\exp(-\kappa^2u/4)\,du.\quad}
\]
At zero drift the last expression reduces to \(8\lambda c_1^2/(3\sqrt\pi)\), a **previously known variance constant** [1, Appendix A]; the distributional limit and the finite critical-drift crossover are the contributions asserted here.

## Assumptions and scope

The infinite particle population is stationary because its one-time occupation counts are independent \(\operatorname{Poisson}(\lambda)\) variables at every integer time. Symmetry is assumed for the **particle** walks; the **observer** has row-dependent drift with \(\sqrt n v_n\to\kappa\). The polynomial \(\varphi\) and \(\lambda\) are fixed. The coefficient \(c_1\ne0\) is essential: polynomials of Poisson–Charlier rank two or higher need a different analysis. No independence of successive sampled occupation counts is assumed. The normal variable \(Z\) in the limit is independent of the *entire* Brownian observer path, while its random variance depends on that path.

## Proof

**1. Poisson trajectory representation and exact conditional variance.** Write
\[
Q_k(z)=2^{-k}{k\choose(k+z)/2}
\]
when \(|z|\le k\) and \(k+z\) is even, and set \(Q_k(z)=0\) otherwise. For any deterministic observer positions \(x_1,\ldots,x_n\), define the occupation trace \(L(X)=\sum_{i=1}^n\mathbf 1\{X_i=x_i\}\) of one particle trajectory \(X\), and sum its starting points \(y\) with the translation-invariant Poisson trajectory intensity \(\lambda\sum_y\mathbb P_y\). Put \(T_n=\sum_{i=1}^n(\xi(i,x_i)-\lambda)\). The Poisson exponential formula and translation invariance give
\[
\mathbb E[T_n\mid x]=0,\qquad
\operatorname{Var}(T_n\mid x)=\lambda\sum_y\mathbb E_y L^2
=\lambda\Bigl[n+2\sum_{1\le i<j\le n}Q_{j-i}(x_j-x_i)\Bigr].\tag{1}
\]
More generally, for \(a\le b\le c\),
\[
\sum_y\mathbb P_y(X_a=x_a,X_b=x_b,X_c=x_c)
=Q_{b-a}(x_b-x_a)Q_{c-b}(x_c-x_b).\tag{2}
\]
The identity includes coincident indices by \(Q_0(0)=1\).

**2. Uniform conditional Gaussian approximation.** The elementary bound \(\sup_z Q_k(z)\le 2/\sqrt{k+1}\), together with (2), yields uniformly over all deterministic observer paths
\[
\sum_y\mathbb E_y L^3\le
6n\Bigl(\sum_{k=0}^{n-1}2/\sqrt{k+1}\Bigr)^2
\le96n^2.\tag{3}
\]
Indeed, group the three time indices in nondecreasing order, upper-bound their multiplicity by six, and choose their two nonnegative gaps. In the centered Poisson characteristic functional, use \(|e^{iz}-1-iz+z^2/2|\le |z|^3/6\) for real \(z\). With
\[
V_n(x)=\lambda n^{-3/2}\Bigl[n+2\sum_{i<j}Q_{j-i}(x_j-x_i)\Bigr]
\]
and fixed \(u\in\mathbb R\), (1)–(3) give
\[
\left|\mathbb E\bigl[e^{iu n^{-3/4}T_n}\mid x\bigr]
-\exp(-u^2V_n(x)/2)\right|
\le16\lambda |u|^3n^{-1/4}.\tag{4}
\]
The final step uses \(|e^a-e^b|\le|a-b|\) whenever both complex exponents have nonpositive real parts, which follows from the line-segment integral. Thus (4) is uniform in the entire observer path, not only in probability.

**3. Brownian limit of the random conditional variance.** The bounded-step triangular-array functional central limit theorem implies
\(s_n\Rightarrow B_\kappa\) in \(C([0,1])\). The parity-compatible lattice local central limit theorem gives, whenever \(k/n\ge\varepsilon>0\), uniformly for \(k\le n\) and parity-compatible \(z\),
\[
Q_k(z)=\frac{2}{\sqrt{2\pi k}}\exp(-z^2/(2k))+o(k^{-1/2}),\tag{5}
\]
where the absolute error is uniform in \(z\) (in particular over bounded rescaled paths). Because \(x_j-x_i\equiv j-i\pmod2\), all observer differences have the required parity. For small gaps the bound in step 2 gives uniformly
\[
\lambda n^{-3/2}\sum_{\substack{i<j\\j-i\le\varepsilon n}}2Q_{j-i}(x_j-x_i)
\le C\lambda\sqrt\varepsilon.\tag{6}
\]
Using (5) on the complement and converting the double sum to a Riemann integral, we obtain \(V_n(S^{(n)})\Rightarrow\mathcal V_\lambda(B_\kappa)\) jointly with \(s_n\). More formally, for any deterministically uniformly convergent sequence of interpolated paths, the long-gap Riemann sums converge; (6) permits \(\varepsilon\downarrow0\). The functional \(\mathcal V_\lambda\) is continuous in uniform norm on \(C([0,1])\), by dominated convergence and the integrable majorant \((t-s)^{-1/2}\). Apply a Skorokhod representation or the extended continuous mapping theorem. Uniform bound (6) with \(\varepsilon=1\) also shows \(0\le V_n\le C\lambda\).

**4. Joint Gaussian-mixture limit for the linear statistic.** Apply (4) conditionally on the random walk and multiply by any bounded continuous function of \(s_n\). Convergence in step 3 gives, for every real \(u\),
\[
\mathbb E\bigl[F(s_n)e^{iu n^{-3/4}T_n}\bigr]
\longrightarrow\mathbb E\bigl[F(B_\kappa)\exp(-u^2\mathcal V_\lambda(B_\kappa)/2)\bigr].\tag{7}
\]
The variance bound in step 3 implies tightness of the second coordinate. Characteristic-function uniqueness conditional on the Brownian path proves the joint convergence to \((B_\kappa,\sqrt{\mathcal V_\lambda(B_\kappa)}Z)\).

**5. Fixed first-rank polynomial reduction.** Define the monic Poisson–Charlier polynomials by the formal identity
\[
\exp(-\lambda z)(1+z)^x=\sum_{\ell\ge0}C_\ell(x;\lambda)z^\ell/\ell!.
\]
Every centered fixed polynomial has a finite expansion
\[
\varphi(x)-\mu_\varphi=c_1 C_1(x;\lambda)+\sum_{\ell=2}^d c_\ell C_\ell(x;\lambda),\qquad C_1(x;\lambda)=x-\lambda.
\]
The displayed formula for \(c_1\) in the statement follows from Poisson integration by parts. Two occupation counts at separated space–time points have the law of bivariate Poisson random variables with a shared mean \(\lambda Q_k(z)\). Their joint Charlier generating function gives exactly
\[
\operatorname{Cov}(C_\ell(\xi(i,x);\lambda),C_m(\xi(j,y);\lambda))
=\mathbf1_{\ell=m}\,\ell!\,[\lambda Q_{|j-i|}(y-x)]^\ell.\tag{8}
\]
For all sufficiently large \(n\), observer step probabilities belong to \([1/4,3/4]\), and a standard binomial local upper bound gives \(\sup_x\Pr(S^{(n)}_{i+k}-S^{(n)}_i=x)\le C k^{-1/2}\) uniformly over \(n,k\). Along with \(\sup_zQ_k(z)\le Ck^{-1/2}\), this implies for each fixed integer \(\ell\ge2\)
\[
\mathbb E\bigl[Q_k(S^{(n)}_{i+k}-S^{(n)}_i)^\ell\bigr]
\le Ck^{-\ell/2}\le C/k.\tag{9}
\]
The first inequality follows by bounding the observer probability mass function uniformly and summing the \(\ell\)-th power of the particle kernel over the lattice; for \(\ell=2\), the sum is \(Q_{2k}(0)=O(k^{-1/2})\), and for larger \(\ell\) apply the supremum bound. From (8)–(9), the variance of the sum of all \(\ell\ge2\) Charlier terms is \(O(n\log n)\), with cross-rank covariance zero. After division by \(n^{3/2}\) it vanishes. Slutsky applied to (7) proves the stated polynomial limit.

**6. Variance crossover and failure of a Gaussian limit.** Since \(V_n\) is uniformly bounded, its expectation converges to \(\mathbb E\mathcal V_\lambda(B_\kappa)\). Independent Gaussian increments give, for \(h=t-s>0\),
\[
\mathbb E\exp\left(-[B_\kappa(t)-B_\kappa(s)]^2/(2h)\right)
=2^{-1/2}\exp(-\kappa^2h/4).
\]
Integrating over the triangle and using (8)–(9) yields the asserted variance formula. Finally, \(\mathcal V_\lambda\) is positive, bounded and continuous on path space. It takes its strict maximum at the zero path, while its value along \(f(t)=at\) tends to zero as \(a\to\infty\). Brownian motion with deterministic drift has full support in continuous paths beginning at zero, so \(\mathcal V_\lambda(B_\kappa)\) is not constant. A Gaussian variance mixture with bounded, positive nonconstant mixing variance cannot itself be Gaussian: differentiating its Laplace transform, or comparing the second and fourth moments, gives strict excess kurtosis. This proves the non-Gaussian assertion.

## Verification

The standalone script `checker.py` uses only the Python standard library. Running `python3 checker.py` verifies the exact lattice-return generating-function recurrence at several rational observer biases, exhaustively enumerates particle and observer paths for lengths one through six to check the conditional second and third moment identities and the stated \(96n^2\) bound, checks the shared-component Poisson covariance, and compares four finite-length variances with independent numerical quadrature of the limit profile. A replay passed **502 exact/supplementary assertions**. The numerical tests are illustrations, not a proof of convergence or non-Gaussianity; steps 1–6 supply those proofs. No random simulation is required.

## Relationship to prior work

Huang, Rang and Su [1, Theorem 1.4] prove an annealed normal approximation at fixed nonzero observer drift, with variance of order \(n\). Their Appendix A proves superlinear variance for symmetric rank-one sampling, calculates \(8\lambda/(3\sqrt\pi)\) in the linear case, and expressly leaves whether a normal limit fails unresolved [1, Remark A.7]. The theorem here establishes the **joint** limiting law for all finite diffusive drift parameters, including zero, proves its annealed non-Gaussian character, and derives the interpolating second moment; it does not re-present the already known zero-drift variance constant as new.

Jaramillo and Murillo-Salas [2] study Poisson particle additive functionals integrated against deterministic spatial tests; their results do not formulate a randomly moving sampling path with an explicit Brownian-conditioned variance. Classical random walk in *static* random scenery [3] leads to a local-time-conditioned mixture; its noise has time-independent spatial marks and therefore a different covariance functional. The present dynamic field has the heat-kernel interaction \(\mathcal V_\lambda\). None of the inspected results contains or logically implies the displayed dynamic-field joint critical-window limit without additional analysis. An unlocated broader theorem about quenched random-path Poisson integrals remains a priority risk.

## Limitations

The claim assumes fixed positive intensity, exactly symmetric particle steps, a fixed polynomial with nonzero first Poisson–Charlier coefficient, and observer bias in the diffusive window \(\sqrt n v_n\to\kappa\in\mathbb R\). It does not address rank-two polynomials, higher-dimensional particle walks, drifting or interacting particle dynamics, diverging scaled drift, a quantitative convergence rate for the mixture, or independent scientific verification. The numerical checker cannot establish the infinite-time statements. The distinction from general conditional Poisson central-limit tools depends on the explicit new analysis of the random heat-kernel variance; no universal novelty claim is made for Gaussian variance mixtures in other models.

## References

[1] Ao Huang, Guanglin Rang, Zhonggen Su, “Normal approximation for the polynomial functionals of correlated random field sampling along random walk path in dimension 1+1,” arXiv:2603.15308v1 (public 2026-03-16). https://arxiv.org/abs/2603.15308. Especially Theorem 1.4, Lemma A.6, Remark A.7, Example A.9.

[2] Arturo Jaramillo, Antonio Murillo-Salas, “Asymptotics for additive functionals of particle systems via Stein's method,” arXiv:2512.02922v1 (2025). https://arxiv.org/abs/2512.02922. Especially Theorem 1 and Section 5.

[3] Fabienne Castell, Nadine Guillotin-Plantard, Françoise Pène, Bruno Schapira, “A local limit theorem for random walks in random scenery and on randomly oriented lattices,” arXiv:1002.1878 (2010). https://arxiv.org/abs/1002.1878. Especially Theorem 1 and the Brownian local-time functional.
