# A critical fourth-cumulant boundary layer in a preferentially resetting active particle

## Finding

Consider a one-dimensional active particle with speed \(v>0\), velocity-switch rate \(\gamma>0\), and resetting rate \(r>0\). At a resetting event it relocates to its position **and velocity** at a uniformly sampled earlier time. Let \(X_t\) be its position and \(\kappa_j(t;r)\) its \(j\)-th cumulant. Set \(\rho=r/\gamma\), \(L=\log(rt)\), and \(\gamma_{\mathrm E}\) equal to Euler's constant. For every fixed compact interval of positive \(\rho\), uniformly with the first \(\rho\)-derivative,

\[
\kappa_2(t;r)=\frac{v^2}{\gamma^2}\left(\frac{L+\gamma_{\mathrm E}}{\rho}-\frac12\right)+O(t^{-\eta}),
\]

\[
\boxed{\;
\kappa_4(t;r)=\frac{3v^4}{\gamma^4}
\left[\frac{2-\rho}{\rho^2}(L+\gamma_{\mathrm E})
+\frac54-\frac{2+\pi^2/6}{\rho^2}\right]+O(t^{-\eta})\;}
\tag{1}
\]

for some positive \(\eta\) (with constants depending on the compact interval and on \(v,\gamma\)). In particular, at the exact cancellation rate \(r=2\gamma\),

\[
\boxed{\lim_{t\to\infty}\kappa_4(t;2\gamma)
=\frac{v^4}{4\gamma^4}\left(9-\frac{\pi^2}{2}\right)>0.}
\tag{2}
\]

Writing the excess kurtosis as \(\mathcal K(t;r)=\kappa_4(t;r)/\kappa_2(t;r)^2\), for each fixed real \(\xi\), uniformly for \(\xi\) in compact sets,

\[
\boxed{
\lim_{t\to\infty}[\log(\gamma t)]^2
\mathcal K\left(t;\gamma\left[2+\frac{\xi}{\log(\gamma t)}\right]\right)
=9-\frac{\pi^2}{2}-3\xi.}
\tag{3}
\]

Moreover, there exists \(t_0>0\) such that for every \(t>t_0\), the fourth cumulant has **exactly one zero** \(r_c(t)\) in \([3\gamma/2,5\gamma/2]\); within this interval it is strictly positive for \(r<r_c(t)\) and strictly negative for \(r>r_c(t)\). This finite-time threshold obeys

\[
\boxed{\frac{r_c(t)}{\gamma}=2+\frac{3-\pi^2/6}{\log(\gamma t)}
+O\big([\log(\gamma t)]^{-2}\big).}
\tag{4}
\]

The positive constant \(3-\pi^2/6\) shows that the finite-time fourth-cumulant threshold lies **above** the leading-order cancellation value \(2\gamma\). The limit of \(\kappa_4\) and the finite-time shift are not determined by the leading logarithmic characteristic-function exponent alone.

## Assumptions and scope

At \(t=0\), \(X_0=0\) and the velocity sign \(\sigma_0\in\{-1,+1\}\) is equiprobable. Between resets, \(\dot X_t=v\sigma_t\), where \(\sigma_t\) flips at independent exponential rate \(\gamma\). Resets occur at independent Poisson rate \(r\). At a reset occurring at time \(t>0\), choose \(U\) uniformly on \([0,t]\) and instantaneously set \((X_t,\sigma_t)=(X_U,\sigma_U)\). All rates and speed are strictly positive. The observation horizon \(t\) tends to infinity with \(v,\gamma\) fixed. In (3) and (4), \(r\) is allowed to vary with \(t\) as written. The unique-zero assertion is **restricted** to the displayed compact resetting-rate interval; no claim is made about zeros at all positive rates or at early times.

## Proof

**1. Exact source formula and the nontrivial asymptotic amplitude.** For a Fourier variable \(k\), write

\[
 s(k)=\sqrt{\gamma^2-v^2k^2},\qquad
 \lambda_\pm(k)=\gamma\pm s(k),\qquad
 a_\pm(k)=\frac{\lambda_\pm(k)}{r+\lambda_\pm(k)}.
\]

In a neighborhood of \(k=0\), use the positive square-root branch. The exact characteristic function established in Boyer--Majumdar [1, Eq. (9)] is

\[
 Q(k,t)=\frac{1-\gamma/s(k)}2\,
 {}_1F_1\big(a_+(k);1;-[r+\lambda_+(k)]t\big)
 +\frac{1+\gamma/s(k)}2\,
 {}_1F_1\big(a_-(k);1;-[r+\lambda_-(k)]t\big).
 \tag{5}
\]

We **use** (5); we do not claim it as a new result. Set \(z=v^2k^2/\gamma^2\), \(\rho=r/\gamma\), \(\ell(z)=1-\sqrt{1-z}\), and \(a(z)=\ell(z)/(\rho+\ell(z))\). The standard large-positive-argument Kummer expansion [4] yields, locally uniformly in complex \(z\) near zero and in real \(\rho\) in a compact interval such as \([3/2,5/2]\),

\[
 Q(k,t)=e^{-a(z)\log(rt)} C(z,\rho)\,[1+E(z,\rho,t)],
 \tag{6}
\]

where

\[
 C(z,\rho)=\frac{1+(1-z)^{-1/2}}2
 \left(1+\frac{\ell(z)}\rho\right)^{-a(z)}
 \frac1{\Gamma(1-a(z))},\qquad
 C(0,\rho)=1.
 \tag{7}
\]

The remainder \(E\), together with its \(z\)-derivatives through order two and its first \(\rho\)-derivative, is \(O(t^{-\eta})\) for some uniform \(\eta>0\). Here is why the parameter differentiability is legitimate, rather than a pointwise formal limit. For sufficiently small fixed complex \(|z|\), apply the Kummer transformation \({}_1F_1(a;1;-Z)=e^{-Z}{}_1F_1(1-a;1;Z)\). The transformed arguments \(Z=[r+\lambda_\pm]t\) stay in a fixed sector about the positive real ray and have magnitudes comparable to \(t\), while the parameters \(a_\pm\) range in compact subsets avoiding the poles of the reciprocal gamma prefactors. The algebraic asymptotic of the minus branch, relative corrections of order \(t^{-1}\), is uniform there. Its exponent has real part arbitrarily close to zero. The plus branch has strictly positive algebraic decay exponent, uniformly bounded away from zero because \(a_+(0)=2/(\rho+2)\). Shrinking the complex neighborhood if needed makes the minus branch strictly dominant and \(C\) nonzero. Uniformity on a slightly larger complex polydisc and Cauchy's formula give all the stated derivative bounds (derivatives introducing powers of \(\log t\) can be absorbed into a smaller exponent \(\eta>0\)). The exponentially small Kummer contributions have no effect. Hence \(\log Q=-a\log(rt)+\log C+O(t^{-\eta})\) with the required differentiated control.

**2. Exact quartic expansion.** With \(\zeta(2)=\pi^2/6\), expansion about \(z=0\) gives

\[
 a(z)=\frac{z}{2\rho}+\frac{\rho-2}{8\rho^2}z^2+O(z^3),
 \tag{8}
\]

\[
\begin{aligned}
\log C(z,\rho)={}&\left(\frac14-\frac{\gamma_{\mathrm E}}{2\rho}\right)z\\
&+\left[\frac5{32}-\frac{2+\pi^2/6}{8\rho^2}
-\frac{\gamma_{\mathrm E}(\rho-2)}{8\rho^2}\right]z^2+O(z^3).
\end{aligned}
\tag{9}
\]

For clarity, (9) follows directly by expanding

\[
 \log C=\log\left(\frac{1+(1-z)^{-1/2}}2\right)
 -a\log(1+\ell/\rho)-\log\Gamma(1-a)
\]

and using \(\log\Gamma(1-a)=\gamma_{\mathrm E}a+\zeta(2)a^2/2+O(a^3)\). Symmetry makes all odd cumulants zero. Since \(z=(v^2/\gamma^2)k^2\), compare coefficients in \(\log Q=-\kappa_2 k^2/2+\kappa_4 k^4/24+O(k^6)\). Equations (8)--(9) establish both expansions in (1), including their differentiated remainders.

**3. Critical cancellation and boundary layer.** At \(\rho=2\), the \(z^2\) coefficient of the logarithmic exponent in (8) vanishes exactly. The constant prefactor term in (9) then gives (2). For \(h=\log(\gamma t)\), take \(\rho=2+\xi/h\). Uniformly for bounded \(\xi\), \(\log(rt)=h+\log\rho\), so (1) yields

\[
 \kappa_4(t;\gamma\rho)
 =\frac{v^4}{4\gamma^4}
 \left(9-\frac{\pi^2}{2}-3\xi\right)+O(h^{-1}),
 \qquad
 \kappa_2(t;\gamma\rho)=\frac{v^2}{2\gamma^2}h+O(1).
 \tag{10}
\]

Dividing by the squared variance proves (3). In particular, the cancellation line has positive but unusually small \(O(h^{-2})\) excess kurtosis, compared with the generic \(O(h^{-1})\) correction away from cancellation.

**4. Existence, uniqueness and location of the finite-horizon zero.** For \(\rho\in[3/2,5/2]\), divide (1) by the positive factor \(3v^4/\gamma^4\) and set

\[
 H_t(\rho)=\frac{2-\rho}{\rho^2}\,[\log(\gamma t)+\log\rho+\gamma_{\mathrm E}]
 +\frac54-\frac{2+\pi^2/6}{\rho^2}+O(t^{-\eta}).
\]

The error is uniform together with its first \(\rho\)-derivative. For \(g(\rho)=(2-\rho)/\rho^2\),

\[
 g'(\rho)=\frac{\rho-4}{\rho^3}<0\quad\text{on }[3/2,5/2].
\]

Therefore \(H'_t(\rho)=g'(\rho)\log(\gamma t)+O(1)<0\) throughout this entire interval for all sufficiently large \(t\). At the left endpoint \(H_t\to+\infty\), and at the right endpoint \(H_t\to-\infty\). Continuity and strict monotonicity yield the claimed unique zero and sign orientation. Finally write \(\rho_c=2+\delta\). The uniform leading term shows \(\delta=O(h^{-1})\); substitution into \(H_t(2+\delta)=0\) gives

\[
 -\frac{\delta h}{4}+\frac54-\frac{2+\pi^2/6}{4}
 =O(h^{-1}),
\]

hence \(\delta=(3-\pi^2/6)/h+O(h^{-2})\). Since \(\mathcal K\) has the same sign as \(\kappa_4\) (strictly positive variance), this also determines the excess-kurtosis sign boundary.

## Verification

The companion `checker.py` requires Python 3.10 or later, `sympy`, `mpmath`, `numpy`, and `scipy`. Run `python checker.py` from the extracted package. It verifies the algebraic Taylor coefficients and critical shift with exact symbolic operations; evaluates the full confluent-hypergeometric characteristic function and differentiates it at zero; and independently integrates the coupled equations for the second and fourth moments and their velocity correlations. In the checked environment, it passed **39 assertions**, and the calculated critical fourth-cumulant constant was \(1.01629944986383\) for \(v=\gamma=1\). These computations support, but do not independently prove, the uniform complex-asymptotic and global-in-interval uniqueness arguments above.

The independent moment-equation checks use

\[
\begin{aligned}
 b_1'&=v-(r+2\gamma)b_1+\frac r t\int_0^t b_1(u)\,du,\\
 m_2'&=2vb_1-rm_2+\frac r t\int_0^t m_2(u)\,du,\\
 b_3'&=3vm_2-(r+2\gamma)b_3+\frac r t\int_0^t b_3(u)\,du,\\
 m_4'&=4vb_3-rm_4+\frac r t\int_0^t m_4(u)\,du,
\end{aligned}
\]

where \(m_j=\mathbb E[X_t^j]\), \(b_j=\mathbb E[\sigma_t X_t^j]\), and each starts at zero. This is a direct independent consequence of the velocity-switching and memory-resetting rules. The fourth cumulant is \(m_4-3m_2^2\).

## Relationship to prior work

The exact characteristic function (5), the known variance, the logarithmic Gaussian central limit, and the leading large-deviation exponent are already in Boyer--Majumdar [1], especially their Eqs. (9), (13), (70) and Appendix B. Those are **not** new claims. In particular, the fixed-\(\rho\) leading logarithmic part of (1) is extractable from the prior leading exponent. The contribution assessed here is the **subleading fourth-cumulant constant**, the **nonzero critical limit** (2), the **uniform near-cancellation profile** (3), and the **finite-time strict monotonicity, uniqueness and sharp shift** (4). These require the previously discarded Fourier amplitude, not only the prior leading large-deviation rate.

Boyer--Solis-Salas [2] derive higher-moment Gaussian convergence corrections for a *discrete nonactive* preferential-revisit walk; their fourth-moment correction does not treat the telegraph switching parameter or its cancellation at \(r=2\gamma\). Boyer--Evans--Majumdar [3] study *Brownian* resetting with memory, with Fourier solution and variance scaling but no active-persistence critical fourth-cumulant boundary. The Kummer expansion [4] is a standard analytic ingredient, not claimed to be novel.

## Limitations

This is a self-review, not an independent audit or a literature-priority certificate. No assertion is made about an all-rates finite-time phase diagram or experimental inference under noisy samples. The theorem depends on simultaneous position-and-velocity resetting to a uniformly sampled past time, not on resetting position alone, a fixed origin, or a weighted memory kernel. A hidden or unindexed equivalent derivation of the subleading critical layer would affect originality. The displayed uniform remainder is an asymptotic existence bound; no explicit smallest valid \(t_0\) is supplied. Numerical checks are finite-time consistency checks only.

## References

[1] D. Boyer and S. N. Majumdar, *Active particle in one dimension subjected to resetting with memory*, arXiv:2312.13439v1 (first public version 2023-12-20); *Physical Review E* **109**, 054105 (2024). https://arxiv.org/abs/2312.13439 ; https://doi.org/10.1103/PhysRevE.109.054105 .

[2] D. Boyer and C. Solis-Salas, *Random walks with preferential relocations to places visited in the past and their application to biology*, arXiv:1403.6069. https://arxiv.org/abs/1403.6069 .

[3] D. Boyer, M. R. Evans and S. N. Majumdar, *Long time scaling behaviour for diffusion with resetting and memory*, arXiv:1611.06743. https://arxiv.org/abs/1611.06743 .

[4] NIST Digital Library of Mathematical Functions, chapter 13, asymptotic expansions of Kummer's confluent hypergeometric function, https://dlmf.nist.gov/13.7 .
