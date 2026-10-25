# A bounded-order-tail counterexample for empirical \(W_1\) concentration

## Finding

Fix any finite \(R\ge2\). There exists a dependent triangular array \(\{Y_{i,n}:1\le i\le n,\ n\ge1\}\) for which every individual variable has a uniformly bounded truncated \(\Psi_R\) norm, every fixed empirical power moment has variance of order \(n^{-1}\), yet the expected \(1\)-Wasserstein distance between the empirical measure and its mean measure converges to a strictly positive constant. The constant is exactly one half of the \(W_1\) distance between two distinct lognormal Stieltjes-class distributions.

More precisely, let
\[
f(x)=\frac{1}{\sqrt{2\pi}\,x}\exp\!\left(-\frac{(\log x)^2}{2}\right),\qquad x>0,
\]
and define probability measures \(\mu_+\) and \(\mu_-\) with densities
\[
f_\pm(x)=f(x)\bigl[1\pm\sin(2\pi\log x)\bigr].
\]
Then all their integer moments agree, while \(\mu_+\ne\mu_-\). Let \(S\) be a fair sign and, conditionally on \(S=+\) or \(S=-\), sample the \(n\) variables in row \(n\) independently from \(\mu_+\) or \(\mu_-\), respectively. With \(\mu_n=n^{-1}\sum_{i=1}^n\delta_{Y_{i,n}}\) and \(\bar\mu_n=\mathbb E\mu_n\), the exact limit is
\[
\lim_{n\to\infty}\mathbb E W_1(\mu_n,\bar\mu_n)
=\frac12W_1(\mu_+,\mu_-)>0.
\]

## Assumptions and scope

For \(r\ge2\), use the truncated function
\[
\Psi_r(t)=\sum_{j=1}^{\lfloor r/2\rfloor}\frac{t^{2j}}{j!}
\]
and its associated Orlicz norm
\[
\|X\|_{\Psi_r}=\inf\{K>0:\mathbb E\Psi_r(|X|/K)\le1\}.
\]
The statement concerns any fixed finite order \(R\), or any bounded sequence of controlled orders \(r_n\le R\). Since every \(\mu_\pm\) has moments of all orders and every \(Y_{i,n}\) has the same unconditional law \((\mu_++\mu_-)/2\), the \(\Psi_R\) norms are uniformly bounded. Dependence across a row is created only by the shared latent sign \(S\); conditional on \(S\), observations within a row are iid.

This is a boundary counterexample, not a claim that growing-order tail control is the only possible sufficient condition. It does not rule out concentration under moment determinacy, stronger tail assumptions, or other structural hypotheses.

## Proof

**1. The two laws are distinct and moment-equivalent.** For every integer \(k\ge0\), if \(Z\sim N(0,1)\), then
\[
\begin{aligned}
\int_0^\infty x^k f(x)\sin(2\pi\log x)\,dx
&=\operatorname{Im}\mathbb E\exp\!\bigl((k+2\pi i)Z\bigr)\\
&=\operatorname{Im}\exp\!\left(\frac{(k+2\pi i)^2}{2}\right)\\
&=\exp\!\left(\frac{k^2-4\pi^2}{2}\right)\sin(2\pi k)=0.
\end{aligned}
\]
Consequently \(f_\pm\ge0\), each integrates to one, and
\[
\int_0^\infty x^k f_\pm(x)\,dx=e^{k^2/2}\qquad(k=0,1,2,\ldots).
\]
The densities differ on a set of positive measure, so \(\mu_+\ne\mu_-\). In particular, both have finite moments of all orders and the same second moment \(e^2\).

**2. Bounded-order tail control holds.** Each \(Y_{i,n}\) has unconditional law \(\bar\mu=(\mu_++\mu_-)/2\), independent of \(i,n\), and \(\bar\mu\) has finite moments of every order. For any fixed \(R<\infty\), the finite sum \(\mathbb E\Psi_R(|Y_{i,n}|/K)\) tends to zero as \(K\to\infty\). Hence \(\sup_{n,i}\|Y_{i,n}\|_{\Psi_R}<\infty\). If \(r_n\le R\), monotonicity of \(\Psi_r\) in \(r\) gives the same bound for \(\Psi_{r_n}\).

**3. Every fixed empirical moment concentrates at order \(n^{-1}\).** Put \(M_{k,n}=n^{-1}\sum_{i=1}^nY_{i,n}^k\). Conditional on \(S=\pm\), its mean is the common moment \(m_k=e^{k^2/2}\), and its conditional variance is \(\operatorname{Var}_{\mu_\pm}(X^k)/n\). The law of total variance therefore yields
\[
\operatorname{Var}(M_{k,n})
=\frac{\operatorname{Var}_{\mu_+}(X^k)+
\operatorname{Var}_{\mu_-}(X^k)}{2n}=O_k(n^{-1}),
\]
because the \(2k\)-th moments are finite.

**4. The Wasserstein gap does not vanish.** The mean measure is the fixed mixture \(\bar\mu=(\mu_++\mu_-)/2\). Given \(S\), the row is iid from \(\mu_S\), so the empirical measure converges to \(\mu_S\) in expected \(W_1\), since \(\mu_S\) has a finite first moment. The reverse triangle inequality for \(W_1\) gives
\[
\left|W_1(\mu_n,\bar\mu)-W_1(\mu_S,\bar\mu)\right|
\le W_1(\mu_n,\mu_S).
\]
Taking expectations shows that \(\mathbb E W_1(\mu_n,\bar\mu)\) converges to \(\mathbb E W_1(\mu_S,\bar\mu)\). In one dimension, \(W_1\) is the integral of the absolute difference of distribution functions. Since \(F_{\bar\mu}=(F_++F_-)/2\),
\[
W_1(\mu_+,\bar\mu)=W_1(\mu_-,\bar\mu)
=\frac12W_1(\mu_+,\mu_-).
\]
Thus the claimed limit follows. It is strictly positive because \(\mu_+\ne\mu_-\) and both belong to \(\mathcal P_1(\mathbb R)\).

## Verification

The proof uses the Gaussian moment-generating identity, the law of total variance, conditional iid empirical-measure convergence in expected \(W_1\), and the one-dimensional distribution-function formula for \(W_1\). Each displayed implication follows from the stated assumptions; no finite numerical experiment is used as a proof. The construction establishes failure for bounded controlled order, not for every possible alternative tail or determinacy hypothesis.

## Relationship to prior work

Amini and Vinas prove expected \(W_1\) concentration from empirical-moment variance decay together with a uniform \(\Psi_{r_n}\) condition where \(r_n\to\infty\). Their proof explicitly chooses a polynomial approximation degree and then requires the controlled moment order to exceed that degree. The present construction gives a concrete obstruction to replacing that growing-order condition by a fixed finite-order bound alone.

The underlying moment-equivalent lognormal perturbation is classical, and the general warning that moment convergence need not determine weak convergence for a moment-indeterminate limit is also classical. The contribution claimed here is narrowly the explicit dependent empirical-measure construction satisfying all fixed-moment variance bounds and bounded-order \(\Psi_R\) control, together with its exact nonzero limiting \(W_1\) gap. No broader historical-priority claim is made.

## Limitations

The observations are dependent unconditionally because of the shared latent sign; this dependence is essential to the construction. The result is a counterexample to a proposed weakening of the tail assumption, not a contradiction of the recent concentration theorem, whose growing-order hypothesis is not met. It does not establish failure when the controlled order tends to infinity, nor does it identify the optimal replacement assumptions.

## References

1. A. A. Amini and L. Vinas, “Wasserstein Concentration of Empirical Measures for Dependent Data via the Method of Moments,” arXiv:2601.07228v1 (first submitted 2026-01-12), Theorem 3 and proof.
2. G. D. Lin, “Recent developments on the moment problem,” *Journal of Statistical Distributions and Applications* 4, article 5 (2017), DOI:10.1186/s40488-017-0059-2; discussion of the Fréchet–Shohat theorem and the lognormal Stieltjes class.
3. C. Kleiber, “The generalized lognormal distribution and the Stieltjes moment problem,” arXiv:1301.1277v1 (2013).
