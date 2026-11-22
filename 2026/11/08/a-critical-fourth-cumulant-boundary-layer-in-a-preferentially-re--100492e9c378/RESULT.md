# A uniform finite-time fourth-cumulant threshold for an active memory-reset particle

## Finding: the moving threshold

Let \(X_t\) be the one-dimensional active particle with constant speed \(v>0\), independent velocity reversals at rate \(\gamma>0\), and Poisson resetting at rate \(r>0\) to **both** its position and velocity at a time sampled uniformly from \([0,t]\). Initially \(X_0=0\), and the velocity sign is equally likely to be positive or negative. Write \(\rho=r/\gamma\), \(h=\log(\gamma t)\), \(\kappa_j(t;\rho)\) for its cumulants, and \(\gamma_E\) for Euler's constant.

The fixed-\(\rho\) fourth-cumulant asymptotic, including its order-one coefficient and the positive critical limit at \(\rho=2\), was established in *Critical fourth-cumulant cancellation in an active memory-reset walk* [2]. Neither that limit nor the exact characteristic function of Boyer--Majumdar [1] is claimed here. The additional result is **uniform differentiation in the resetting rate**, with the following finite-horizon consequences.

For \(I=[3/2,5/2]\), some \(\eta>0\), and \(j=0,1\), the errors below have \(\partial_\rho^j\)-norm \(O(t^{-\eta})\) uniformly on \(I\):

\[
\kappa_2(t;\rho)=\frac{v^2}{\gamma^2}\left[\frac{h+\log\rho+\gamma_E}{\rho}-\frac12\right]+O(t^{-\eta}),
\tag{1}
\]
\[
\kappa_4(t;\rho)=\frac{3v^4}{\gamma^4}\left[\frac{2-\rho}{\rho^2}(h+\log\rho+\gamma_E)
+\frac54-\frac{2+\pi^2/6}{\rho^2}\right]+O(t^{-\eta}).
\tag{2}
\]

For all sufficiently large \(t\), the function \(\rho\mapsto\kappa_4(t;\rho)\) is **strictly decreasing throughout \(I\)** and has exactly one zero \(\rho_c(t)\in I\). Thus the cumulant is positive below \(\rho_c(t)\), negative above it, and

\[
\boxed{\quad\rho_c(t)=2+\frac{3-\pi^2/6}{\log(\gamma t)}+O\!\left(\log^{-2}(\gamma t)\right).\quad}
\tag{3}
\]

For the standardized excess kurtosis \(\mathcal K=\kappa_4/\kappa_2^2\), a simultaneous moving-rate limit holds, uniformly for bounded real \(\xi\):

\[
\boxed{\quad\lim_{t\to\infty}h^2\mathcal K\!\left(t;2+\frac{\xi}{h}\right)
=9-\frac{\pi^2}{2}-3\xi.\quad}
\tag{4}
\]

Here the argument of \(\mathcal K\) is the dimensionless ratio \(\rho\), not the dimensional rate \(r\). The positive displacement coefficient \(3-\pi^2/6\) shows that the unique *finite-observation* zero lies above \(r=2\gamma\), although the leading fixed-rate cumulant cancels there. Claims (3)--(4) and the uniform rate derivative in (1)--(2), rather than the already known fixed-rate coefficients, constitute the result assessed here.

## Scope and normalization

The process is as in [1,2]: between reset events \(dX_t/dt=v\sigma_t\) with \(\sigma_t\in\{-1,1\}\), switching at rate \(\gamma\); at an independent rate-\(r\) reset at time \(t\), draw \(U\) uniformly from \([0,t]\) and set \((X_t,\sigma_t)=(X_U,\sigma_U)\). The parameters \(v,\gamma\) remain fixed while \(t\to\infty\); only \(r/\gamma\) varies over the compact interval \(I\), or within an \(O(h^{-1})\) neighborhood of 2. We assert uniqueness **only on \(I\)**, not among all \(r>0\), and make no explicit claim for small \(t\). Symmetric initialization ensures odd cumulants vanish.

## Proof

**1. Exact analytic input and rate-uniform amplitude.** For \(z=v^2k^2/\gamma^2\), set
\[
\ell(z)=1-\sqrt{1-z},\quad a(z,\rho)=\frac{\ell(z)}{\rho+\ell(z)},\quad
c(z)=\frac{1+(1-z)^{-1/2}}2.
\]
The characteristic function \(Q(k,t)=\mathbb E e^{ikX_t}\) is the sum of two confluent-hypergeometric terms [1, Eq. (9)]: the slowly decaying term has rate \(\lambda_-(z)=\gamma\ell(z)\), parameter \(a=\lambda_-/(r+\lambda_-)\), and coefficient \(c(z)\); the other has \(\lambda_+=\gamma(1+\sqrt{1-z})\), parameter \(a_+=\lambda_+/(r+\lambda_+)\), and coefficient \(1-c(z)\). Both hypergeometric terms are \({}_1F_1(a_\pm;1;-[r+\lambda_\pm]t)\).

The exact formula is **prior work**. To make the extra uniform-rate assertion precise, choose a small complex disk \(|z|\le\varepsilon\) and a thin complex neighborhood of the real interval \(I\). These can be chosen so that the square root and all denominators are analytic and nonzero, \(\operatorname{Re}a(z,\rho)\) is arbitrarily close to 0, and \(\operatorname{Re}a_+(z,\rho)\) is uniformly bounded away from 0. The arguments \((r+\lambda_\pm)t\) remain in a common closed sector about the positive real axis and are comparable to \(t\) in magnitude. Applying Kummer's transformation and its uniform positive-argument expansion [3] to the two branches gives
\[
Q(k,t)=e^{-a(z,\rho)[h+\log\rho]} C(z,\rho)[1+E(z,\rho,t)],
\tag{5}
\]
\[
C(z,\rho)=c(z)\left(1+\frac{\ell(z)}\rho\right)^{-a(z,\rho)}
\Gamma(1-a(z,\rho))^{-1},\qquad C(0,\rho)=1.
\tag{6}
\]
The slow branch has a relative expansion error of order \(t^{-1}\) times harmless bounded holomorphic factors. The fast branch has a strictly positive uniform decay-exponent gap; possible powers of \(\log t\) are absorbed by choosing a smaller \(\eta>0\). Thus \(E=O(t^{-\eta})\) jointly uniformly in those complex \(z,\rho\) neighborhoods. In particular, \(Q\) is nonzero near \(z=0\) for large \(t\), and applying Cauchy's formula on slightly smaller complex polydisks gives the same power bound for \(\partial_z^j\partial_\rho^m E\), \(0\le j\le2\), \(0\le m\le1\). This is the rate-uniform differentiability step not asserted in the fixed-parameter result [2].

**2. Cumulant coefficients.** Taking the branch of \(\log Q\) vanishing at \(z=0\), and using the standard Taylor series of \(\log\Gamma\), gives
\[
a(z,\rho)=\frac{z}{2\rho}+\frac{\rho-2}{8\rho^2}z^2+O(z^3),
\tag{7}
\]
\[
\log C(z,\rho)=\left(\frac14-\frac{\gamma_E}{2\rho}\right)z
+\left[\frac5{32}-\frac{2+\pi^2/6}{8\rho^2}
-\frac{\gamma_E(\rho-2)}{8\rho^2}\right]z^2+O(z^3).
\tag{8}
\]
Comparison with \(\log Q=-\kappa_2k^2/2+\kappa_4k^4/24+O(k^6)\) proves (1)--(2), and the preceding complex-neighborhood bound makes both remainders uniform with their first rate derivative. The *values* of these fixed-rate coefficients match [2] exactly and are not new; here their differentiated uniform remainder is the necessary additional claim.

**3. Unique finite-horizon threshold.** Put \(g(\rho)=(2-\rho)/\rho^2\). On \(I\),
\[
g'(\rho)=\frac{\rho-4}{\rho^3}<0.
\]
By the differentiated estimate (2), uniformly on \(I\),
\[
\frac{\gamma^4}{3v^4}\partial_\rho\kappa_4(t;\rho)
=g'(\rho)h+O(1)<0
\]
for large enough \(t\). At the endpoints \(3/2\) and \(5/2\), the leading \(g(\rho)h\) terms have strictly opposite signs; the bounded terms cannot overcome them. By continuity and strict monotonicity there is exactly one zero in \(I\), with the stated sign orientation. At \(\rho=2\), (2) has limiting value \(v^4(18-\pi^2)/(8\gamma^4)>0\), **already known from [2]**. The root therefore satisfies \(\rho_c=2+O(h^{-1})\). Substituting \(\rho_c=2+\delta\) into (2) yields
\[
0=-\frac{h\delta}{4}+\frac{3-\pi^2/6}{4}+O(h^{-1}),
\]
which gives (3).

**4. Moving-rate excess-kurtosis profile.** Set \(\rho=2+\xi/h\) with bounded \(\xi\). Equations (1)--(2) imply, uniformly for such \(\xi\),
\[
\kappa_4=\frac{v^4}{4\gamma^4}\left(9-\frac{\pi^2}{2}-3\xi\right)+O(h^{-1}),
\qquad \kappa_2=\frac{v^2}{2\gamma^2}h+O(1).
\]
Dividing proves (4). This shows that a change in the reset rate of order \(\gamma/\log(\gamma t)\) alters the **sign** of the first non-Gaussian correction for long but finite observations, which the fixed-rate result [2] alone does not quantify uniformly.

## Verification and limits

An independent exact Taylor calculation of \(a\) and \(\log C\) gives precisely (7)--(8) and the coefficient \(3-\pi^2/6\). Direct numerical differentiation of the source Kummer formula yields finite-time zeros \(\rho_c(200)\approx2.42487\), \(\rho_c(2000)\approx2.29077\), and \(\rho_c(20000)\approx2.20817\) for \(v=\gamma=1\); these are diagnostics, not a substitute for the uniform proof. The unchanged `checker.py` provides separate symbolic and finite-time moment checks. No explicit threshold time \(t_0\), all-reset-rate uniqueness, or trajectory-sampling uncertainty bound is proved.

## Relationship to literature

[1] D. Boyer and S. N. Majumdar, *An active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439 (2023), especially exact Fourier Eq. (9), variance Eq. (13) and large-deviation asymptotics, https://arxiv.org/html/2312.13439v1 .

[2] *Critical fourth-cumulant cancellation in an active memory-reset walk*, published 2 November 2026, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-critical-fourth-cumulant-cancellation-in-an-active-memory-reset--ec2c64764980/RESULT.md . It already establishes the full fixed-rate \(O(1)\) fourth-cumulant asymptotic, positive critical constant and inverse-log-squared critical kurtosis. This work adds only the rate-uniform differentiated estimate and the resulting unique finite-time threshold and moving-rate profile; no priority is claimed for [2]'s conclusions.

[3] NIST Digital Library of Mathematical Functions, §13.7 (Kummer large-argument expansion and uniform-sector conditions), https://dlmf.nist.gov/13.7 .

[4] D. Boyer and C. Solis-Salas, *Random walks with preferential relocations to places visited in the past and their application to biology*, arXiv:1403.6069 (2014), passive discrete preferential-revisit moments.

[5] D. Boyer, M. R. Evans and S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743 (2016), passive Brownian memory-resetting.
