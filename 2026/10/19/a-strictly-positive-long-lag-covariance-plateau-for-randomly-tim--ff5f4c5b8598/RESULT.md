# A strictly positive long-lag covariance plateau for randomly timed photosynthetic cycles

## Finding

In the scalar two-mode photosynthetic-factory model with a light/dark period drawn once from a continuous distribution, the long-time covariance at a fixed separation exists, and the **successive large-time then large-lag limit is strictly positive**:
\[
\lim_{s\to\infty}\lim_{t\to\infty}\operatorname{Cov}(X(t),X(t+s))
=\operatorname{Var}(m(H))>0.
\]
Here \(m(h)\) is the period mean of the unique positive periodic orbit at fixed period \(h\). Its exact formula is
\[
m(h)=c(1-r)+\frac{2c(1/a-1/b)}{h\{\coth(arh/2)+\coth(b(1-r)h/2)\}},
\]
which is **strictly decreasing** for \(h>0\). A continuously distributed period consequently leaves a positive memory plateau even though its oscillatory phases dephase.

## Assumptions and scope

Fix \(T>0\), \(0<a<b\), \(c>0\), and a dark fraction \(r\in(0,1)\). In each deterministic period \(h\in(0,T)\), the active photosynthetic fraction obeys
\[
\dot x(t)=-a x(t)\quad (0\le t\bmod h<rh),\qquad
\dot x(t)=b[c-x(t)]\quad(rh\le t\bmod h<h).
\]
Take the unique positive periodic solution, with initial phase the start of darkness. Let \(H\) have an arbitrary absolutely continuous probability law on \((0,T)\), with density in \(L^1\). Draw \(H\) **once** per trajectory (quenched heterogeneity); do not redraw the period each cycle. Define \(X(t)=x(t;H)\). Write
\[
m(h)=\frac1h\int_0^h x(u;h)\,du,\qquad
R_h(s)=\frac1h\int_0^h x(u;h)x(u+s;h)\,du.
\]
These assumptions correspond to the scalar reduction in the 2026 source, with \(a=-A\), \(b=-B\), \(c=-C/B\), and the source's dark fraction \(r\); in that parameterization \(b>a\). The first verified public source date is 2026-02-25. The relevant primary MSC2020 classification is 92C45 (biochemical kinetics).

## Proof

**1. Periodic orbit and mean.** Set \(u=ar>0\), \(v=b(1-r)>0\). Composition of the dark and light affine flows has multiplier \(e^{-(u+v)h}\in(0,1)\), so a unique positive periodic orbit exists. Its value at the start of darkness is
\[
x_0(h)=\frac{c(1-e^{-vh})}{1-e^{-(u+v)h}},\qquad 0<x(t;h)<c.
\]
On the dark segment \(x=x_0e^{-at}\); on the light segment \(x=c+(x_0e^{-arh}-c)e^{-b(t-rh)}\). Integrating both segments exactly gives
\[
m(h)=c(1-r)+c(1/a-1/b)
\frac{(1-e^{-uh})(1-e^{-vh})}{h(1-e^{-(u+v)h})}.
\]
The fraction is \(2/[h(\coth(uh/2)+\coth(vh/2))]\). For any \(k>0\), the derivative of \(h\coth(kh)\) has numerator \(\sinh(kh)\cosh(kh)-kh>0\), by \(\sinh(2z)>2z\). Therefore the denominator \(h[\coth(uh/2)+\coth(vh/2)]\) is strictly increasing in \(h\); because \(b>a\), the entire nonconstant term is positive and strictly decreasing. Thus \(m(h)\) is continuous and strictly decreasing. Since \(H\) has an absolutely continuous probability law, it is not almost surely constant, and hence \(\operatorname{Var}(m(H))>0\).

**2. Continuous-period phase-mixing lemma.** Suppose \(F_h(\theta)\) is a uniformly bounded family of one-periodic functions, uniformly Lipschitz in \(\theta\in\mathbb R\), and jointly measurable in \((h,\theta)\). Then
\[
\lim_{t\to\infty}\mathbb E[F_H(t/H)]
=\mathbb E\left[\int_0^1F_H(\theta)\,d\theta\right].
\]
Indeed, Fejér trigonometric polynomials approximate every uniformly Lipschitz one-periodic function uniformly, with an error bound independent of \(h\). Each nonzero Fourier term has expectation \(\int_0^T g_k(h)e^{2\pi i kt/h}f_H(h)\,dh\), where \(g_kf_H\in L^1\); substituting \(\nu=1/h\) and applying the Riemann–Lebesgue lemma makes this term vanish. First send \(t\to\infty\) in the finite polynomial and then send the polynomial degree to infinity.

Here \(x(t;h)\in[0,c]\) and its physical-time derivative on each phase is bounded by \(c\max\{a,b\}\), uniformly in \(h\). Accordingly \(\theta\mapsto x(h\theta;h)\) is uniformly Lipschitz (constant at most \(Tc\max\{a,b\}\)), as is \(\theta\mapsto x(h\theta;h)x(h\theta+s;h)\) for each fixed \(s\ge0\). Applying the lemma first to the two single-time means and then to the two-time product yields, for each fixed \(s\),
\[
C(s):=\lim_{t\to\infty}\operatorname{Cov}(X(t),X(t+s))
=\mathbb E[R_H(s)]-(\mathbb E[m(H)])^2.
\]

**3. Removal of nonzero lag harmonics.** Let \(A_n(h)\), \(B_n(h)\) denote the real Fourier coefficients of the periodic function \(x(\cdot;h)\), using the convention \(x(t;h)=m(h)+\sum_{n\ge1}[A_n(h)\cos(2\pi nt/h)+B_n(h)\sin(2\pi nt/h)]\). Autocorrelation and Parseval give
\[
R_h(s)=m(h)^2+\frac12\sum_{n\ge1}\left[A_n(h)^2+B_n(h)^2\right]\cos\left(\frac{2\pi ns}{h}\right).
\]
The sum is absolutely convergent, with \(\sum_{n\ge1}(A_n^2+B_n^2)/2=R_h(0)-m(h)^2\le c^2\). Its expectation is consequently absolutely summable in \(n\). For each fixed \(n\ge1\), the Riemann–Lebesgue lemma after \(\nu=1/h\) makes the expected cosine term vanish as \(s\to\infty\). Dominated convergence for the series yields \(\lim_{s\to\infty}\mathbb E[R_H(s)]=\mathbb E[m(H)^2]\). Subtracting \((\mathbb E[m(H)])^2\) completes the theorem.

## Verification

The accompanying `verify_photobioreactor.py` evaluates the closed period-mean formula against direct quadrature of the periodic orbit for 36 parameter/period tests, checks exact return-map closure in another 36 tests, checks strict decreases in three parameter sets, and illustrates the predicted positive lag-covariance plateau with fine deterministic quadrature. It passed 78 assertions. Numerical illustrations are not used to prove either infinite-time limit. Both limits follow from the phase-mixing and Parseval arguments above.

## Relationship to prior work

Andreu-Vilarroig, Cortés, Navarro-Quiles, Papáček, and Pérez (2026) introduce the random-period photosynthetic-factory reduction and establish explicit **single-time** asymptotic ensemble mean and variance (their Theorems 1 and 3). Their Remark 6 distinguishes between variance of the period mean and the asymptotic one-time variance. The result here concerns **two-time covariance** and proves a strictly positive, explicit long-lag remainder arising from the monotone dependence of the orbit mean on the quenched period. The generic mathematical ideas of Riemann–Lebesgue dephasing and the variance decomposition for heterogeneous periodic systems are not claimed as new; the source-specific positive plateau, its exact kinetic mean, and the full limiting lag-covariance formula are the proposed contribution.

## Limitations

The result describes the stationary-time limit of an ensemble formed by drawing **one** random period per trajectory. It is not a theorem for independently renewed light/dark periods, noisy state forcing, feedback control, or biologically interacting cells. The stated order of limits is \(t\to\infty\) first and \(s\to\infty\) second. Density of the period law is important for dephasing; an atomic law need not have the same long-lag limit. The analysis assumes the scalar reduced kinetic equation, not the full multistate biochemical model. No empirical production gain or predictive field validation is established.

## References

1. C. Andreu-Vilarroig, J.-C. Cortés, A. Navarro-Quiles, Š. Papáček and C.-L. Pérez, *A Random Differential Equation Approach for Modeling the Growth of Microalgae in Photobioreactors*, Bulletin of Mathematical Biology 88, article 47 (2026), DOI 10.1007/s11538-026-01609-3, https://doi.org/10.1007/s11538-026-01609-3 (first public online 2026-02-25).
2. Classical Riemann–Lebesgue lemma, Fejér approximation theorem, and Fourier Parseval identity (standard tools, not novelty claims).
