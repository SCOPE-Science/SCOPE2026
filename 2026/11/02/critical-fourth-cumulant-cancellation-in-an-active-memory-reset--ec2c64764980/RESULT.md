# Critical fourth-cumulant cancellation in an active memory-reset walk

## Finding
Consider the active telegraph particle with uniform preferential resetting of both its position and velocity, as defined below. Its leading fourth cumulant changes sign at the **exact** dimensionless resetting rate \(p=r/\gamma=2\). At that critical rate, the logarithmically growing term cancels and the **unscaled** fourth cumulant approaches the strictly positive constant
\[
\lim_{t\to\infty}\operatorname{cum}_4(X_t)
=\frac{v^4}{\gamma^4}\frac{18-\pi^2}{8}>0.
\]
In contrast, the variance diverges logarithmically. Thus the standardized excess kurtosis at the critical rate is
\[
\frac{\operatorname{cum}_4(X_t)}{\operatorname{Var}(X_t)^2}
\sim \frac{18-\pi^2}{2\log^2(rt)},
\qquad t\to\infty.
\]
Away from this rate the leading correction to Gaussianity is of order \(1/\log(rt)\), with sign determined by \(2-p\). This is a fourth-cumulant result, not an all-order or total-variation Gaussian approximation theorem.

For all fixed \(v,\gamma,r>0\), set \(p=r/\gamma\), \(L=\log(rt)\), and let \(\gamma_E\) denote the Euler–Mascheroni constant. More precisely,
\[
\operatorname{Var}(X_t)=\frac{v^2}{\gamma^2}
\left[\frac{L+\gamma_E}{p}-\frac12\right]+o(1)
\]
and
\[
\boxed{\quad
\operatorname{cum}_4(X_t)=\frac{v^4}{\gamma^4}
\left[\frac{3(2-p)}{p^2}L+
\frac{15p^2-12\gamma_Ep-24-2\pi^2+24\gamma_E}{4p^2}\right]+o(1).\quad}
\]
Consequently, the fourth cumulant is eventually strictly positive for \(0<p\le 2\), and eventually strictly negative for \(p>2\). If \(p\ne2\), its normalized form equals \(3(2-p)/L+O(L^{-2})\).

## Assumptions and scope
The process starts at \(X_0=0\). Its initial velocity is \(+v\) or \(-v\) with equal probability, where \(v>0\). While no reset occurs, the velocity alternates sign at independent exponential times of rate \(\gamma>0\), and position evolves at that current velocity. At the independent rate-\(r>0\) Poisson resetting times, a time \(U\) is sampled uniformly from the entire elapsed interval \([0,t)\), and the pair \((X_t,V_t)\) instantaneously becomes the past pair \((X_U,V_U)\). The process then continues from that pair. The fourth cumulant is \(\mathbb E[X_t^4]-3\mathbb E[X_t^2]^2\), since symmetry gives \(\mathbb E X_t=0\). All limits hold for fixed positive model parameters as \(t\to\infty\); no uniform-in-parameters limit is asserted.

## Proof
**1. Exact input and the two spectral branches.** The position moment-generating function is obtained by analytic continuation of the exact Fourier-space distribution of Boyer–Majumdar [1, equations (9)–(12)]. For \(z\) in a complex neighborhood of zero, define
\[
 h(z)=\sqrt{\gamma^2+v^2z^2},\qquad
 \lambda_-(z)=\gamma-h(z),\qquad \lambda_+(z)=\gamma+h(z),
\]
\[
 a_\pm(z)=\frac{\lambda_\pm(z)}{r+\lambda_\pm(z)},\qquad
 c_-(z)=\frac{1+\gamma/h(z)}2,\qquad
 c_+(z)=\frac{1-\gamma/h(z)}2.
\]
With \({}_1F_1\) denoting the confluent hypergeometric function,
\[
 M_t(z)=\mathbb E[e^{zX_t}]
 =\sum_{\sigma\in\{-,+\}}c_\sigma(z)
 \;{}_1F_1\bigl(a_\sigma(z);1;-[r+\lambda_\sigma(z)]t\bigr).
\]
The characteristic-function formula of [1] is an **input**, not part of the present novelty claim. It applies here because resetting copies both position and velocity, not just position.

**2. Locally uniform large-time expansion.** At zero, \(\lambda_-(0)=0\), \(a_-(0)=0\), \(c_-(0)=1\), whereas \(a_+(0)=2\gamma/(r+2\gamma)>0\) and \(c_+(z)=O(z^2)\). Choose a sufficiently small fixed complex disk around zero so that the Kummer negative-argument expansion is uniform and the real part of the decay-exponent gap remains positive. On that disk,
\[
{}_1F_1(a;1;-bt)
 =\frac{(bt)^{-a}}{\Gamma(1-a)}[1+O(t^{-1})]
 \quad(t\to\infty)
\]
for the slowly decaying branch, while the second branch is smaller by a fixed positive power of \(t\), up to powers of \(\log t\). Uniform analyticity permits up to four derivatives at zero via Cauchy's formula. Taking the branch of the logarithm that is zero at \(z=0\), we obtain, with a locally analytically differentiable \(o(1)\) remainder,
\[
\log M_t(z)=-a_-(z)L+C(z)+o(1),
\]
\[
C(z)=\log c_-(z)-a_-(z)\log\!\left(1+\frac{\lambda_-(z)}r\right)
 -\log\Gamma(1-a_-(z)).
\]
Here \(L=\log(rt)\), and \(r+\lambda_-(z)\) remains nonzero on the chosen disk.

**3. Expansion at the origin.** Introduce the dimensionless small quantity \(x=(vz/\gamma)^2\). Then
\[
\lambda_-(z)=\gamma(1-\sqrt{1+x}),\qquad
-a_-(z)=\frac{x}{2p}+\frac{2-p}{8p^2}x^2+O(x^3),
\]
\[
 C(z)=\left(\frac{\gamma_E}{2p}-\frac14\right)x
 +\frac{15p^2-12\gamma_Ep-24-2\pi^2+24\gamma_E}{96p^2}x^2+O(x^3).
\]
For the last identity, expand \(\log[(1+(1+x)^{-1/2})/2]\), \(\log[1+(1-\sqrt{1+x})/p]\), and \(\log\Gamma(1-a)\), using \(\log\Gamma(1+w)=-\gamma_Ew+(\pi^2/12)w^2+O(w^3)\). The enclosed standalone checker confirms these exact algebraic identities symbolically.

**4. Read off cumulants and the critical boundary.** Symmetry makes \(\log M_t(z)=\kappa_2(t)z^2/2!+\kappa_4(t)z^4/4!+O(z^6)\). Taking the second and fourth Taylor coefficients of Step 3 gives exactly the expansions in the finding. The coefficient of \(L\) in \(\kappa_4\) vanishes **if and only if** \(p=2\). At this rate, the surviving coefficient simplifies to \((18-\pi^2)/8>0\), proving the finite nonzero limit. Dividing by the squared leading variance, \([v^2L/(\gamma^2p)]^2\), proves the \(L^{-2}\) critical decay and the \(L^{-1}\) noncritical law. At \(p=2\), the constant is positive, proving the stated eventually positive sign also at the boundary.

## Verification
Run `python CHECK.py` with Python 3 and `sympy`, `numpy`, `scipy`, `mpmath` installed. It symbolically verifies four Taylor identities (including the critical constant), independently integrates the exact finite-time moment hierarchy to compare 24 moments with hypergeometric differentiation, and compares six finite large-time fourth cumulants with the asymptotic formula, plus one separate critical-limit bound. The moment hierarchy is derived directly from the motion and reset rule: for \(A_n=\mathbb E X_t^n\) and \(B_n=\mathbb E[V_tX_t^n]\),
\[
 A_n'=n B_{n-1}-rA_n+\frac r t\int_0^t A_n(s)\,ds,\quad
 B_n'=nv^2A_{n-1}-(r+2\gamma)B_n+\frac r t\int_0^t B_n(s)\,ds.
\]
The program uses this independent system up to degree four. Numerical comparisons are checks, not substitutes for the analytical proof or independent scientific audit.

## Relationship to prior work
Boyer and Majumdar [1] establish the **full exact** Fourier-space distribution, the all-time variance and its logarithmic growth, and a large-deviation principle. In particular their formula already implies the entire fourth cumulant in principle; none of those foundations is claimed as new. The present evaluated statement resolves the **previously unstated singular cancellation of fourth-cumulant growth at the precise ratio \(r/\gamma=2\)** and its nonzero finite constant, yielding a log-squared rather than log-inverse standardized fourth cumulant. Their asymptotic Fourier expression discards the prefactor needed to detect this critical constant; a local fourth-order expansion retaining that prefactor is essential. Their variance expansion agrees with the second-order calculation here.

Boyer, Evans and Majumdar [2] treat Brownian diffusion with resetting and memory, not the paired-velocity telegraph model or this fourth-cumulant critical rate. Boci and Mailler [3] prove a broad quenched large-deviation principle for preferential relocations; a logarithmic-scale rate theorem does not provide the order-one fourth cumulant surviving a cancellation of the extensive logarithmic term. A broader unpublished or undiscovered mod-Gaussian/cumulant theorem may cover this refinement; publication priority is not independently established.

## Limitations
The result classifies eventual fourth-cumulant signs for fixed parameters, **not** the sign for every finite time or the number of sign crossings. It does not claim a uniform asymptotic as \(r/\gamma\) approaches two jointly with time, nor an all-order Edgeworth expansion or total-variation rate. The proof relies on stationary symmetric velocity initialization and uniformly sampled historical relocation of both position and velocity, independent Poisson clocks, and positive rates. No extension to reset-only-position protocols, nonuniform memory kernels, or asymmetric telegraph flipping is implied. The originality assessment is literature-based, not independent publication-priority certification.

## References
[1] Denis Boyer and Satya N. Majumdar, *An active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439v1 (first public 2023-12-20), https://arxiv.org/html/2312.13439v1 ; arXiv:2312.13439v2 (2024-05-06), https://arxiv.org/pdf/2312.13439 .

[2] Denis Boyer, Martin R. Evans and Satya N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743 (2016), https://arxiv.org/abs/1611.06743 .

[3] Erion-Stelios Boci and Cécile Mailler, *Large deviations principle for a stochastic process with random reinforced relocations*, arXiv:2105.02633 (2021; later revisions), https://arxiv.org/abs/2105.02633 .
