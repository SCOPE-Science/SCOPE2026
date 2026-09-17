# Critical-tolerance Gaussian fluctuations and half-step CG law on Haar power-law spectra

**Same-model review: passed. Cross-model review: not yet performed.**

## Statement

Consider the complex-Haar power-law source model
\[
A_n=U_n\operatorname{diag}(1^{-p},2^{-p},\ldots,n^{-p})U_n^*,\qquad
b_n=A_n z_n,
\]
where \(U_n\) is Haar unitary, \(z_n\) is an independent uniform unit vector in
\(\mathbb C^n\), and exact unpreconditioned conjugate gradient (CG) starts from
\(x_0=0\). Let
\[
M_{d,n}(p)
=\min_{\deg q\le d,\ q(0)=1}
\frac{\sum_{j=1}^n \lambda_j |q(\lambda_j)|^2 |\alpha_j|^2}
     {\sum_{j=1}^n \lambda_j |\alpha_j|^2},
\qquad
\alpha=U_n^*z_n,
\]
so that the relative squared \(A_n\)-norm error after \(d\) CG steps is
\(M_{d,n}(p)\), and
\[
T_{\rm CG,n}(\varepsilon,p)=\min\{d\ge0:M_{d,n}(p)\le\varepsilon\}.
\]

Fix an integer \(d\ge1\) and assume
\[
(4d+2)p<1.
\]
Define
\[
F_d(p)=\binom{p^{-1}-2}{d}^{-2}
      =\left(
        \frac{d!\,p^d}{\prod_{m=2}^{d+1}(1-mp)}
        \right)^2
\]
and
\[
\nu_p(dy)=\frac{1-p}{p}\,y^{-1/p}\,dy,\qquad y\in[1,\infty).
\]
Let
\[
\alpha_d=p^{-1}-2d-2
\]
and
\[
r_{d,p}(y)
=
\frac{y^d P_d^{(0,\alpha_d)}(2/y-1)}
     {\binom{p^{-1}-2}{d}},
\]
where \(P_d^{(a,b)}\) is the Jacobi polynomial in the standard normalization
\(P_d^{(a,b)}(1)=\binom{d+a}{d}\). Then \(r_{d,p}\) is a degree-\(d\)
polynomial with \(r_{d,p}(0)=1\), and
\[
F_d(p)=\int_1^\infty r_{d,p}(y)^2\,\nu_p(dy).
\]

### Theorem

Under the assumptions above,
\[
\sqrt n\bigl(M_{d,n}(p)-F_d(p)\bigr)
\Longrightarrow
N(0,\sigma_{d,p}^2),
\]
with
\[
\sigma_{d,p}^2
=
(1-p)\int_1^\infty
y\bigl(r_{d,p}(y)^2-F_d(p)\bigr)^2\,\nu_p(dy),
\]
and \(0<\sigma_{d,p}^2<\infty\).

Consequently, at the exact fixed-degree critical tolerance
\(\varepsilon=F_d(p)\),
\[
T_{\rm CG,n}(F_d(p),p)
\Longrightarrow
d+\operatorname{Bernoulli}(1/2).
\]
Equivalently,
\[
\Pr(T_{\rm CG,n}=d)\to\frac12,\qquad
\Pr(T_{\rm CG,n}=d+1)\to\frac12.
\]

For the real-Haar orthogonal source model, the same conclusions hold, except
that the Gaussian variance is \(2\sigma_{d,p}^2\); the limiting half-step law
is unchanged.

## Proof

### 1. Fixed-degree limit and its closed form

Write
\[
Y_{j,n}=(n/j)^p.
\]
For a uniform complex-sphere vector, the squared spectral coordinates have the
Dirichlet representation
\[
(|\alpha_1|^2,\ldots,|\alpha_n|^2)
\stackrel d=
\frac{(E_1,\ldots,E_n)}{\sum_iE_i},
\]
with independent mean-one exponential \(E_j\). The common denominator cancels
from the CG quotient. Hence
\[
M_{d,n}(p)=
\min_{\deg r\le d,\ r(0)=1}
\int r(y)^2\,\mu_n(dy),
\]
where
\[
\mu_n=
\frac{\sum_{j=1}^nY_{j,n}E_j\,\delta_{Y_{j,n}}}
     {\sum_{j=1}^nY_{j,n}E_j}.
\]
For fixed \(d\) with \((2d+1)p<1\), the moments through order \(2d\) converge
to those of \(\nu_p\), so \(M_{d,n}\to F_d\) in probability, where
\[
F_d=\min_{\deg r\le d,\ r(0)=1}\int r^2\,d\nu_p.
\]

The closed form follows by \(x=1/y\). Put \(Q(x)=x^d r(1/x)\); then \(Q\) is a
monic polynomial of degree \(d\), and
\[
\int_1^\infty r(y)^2\,\nu_p(dy)
=
\frac{1-p}{p}\int_0^1 Q(x)^2x^{p^{-1}-2d-2}\,dx.
\]
Thus \(Q\) is the monic shifted Jacobi polynomial for the weight
\(x^{\alpha_d}\). Since the coefficient of \(x^d\) in
\(P_d^{(0,\alpha_d)}(2x-1)\) is
\(\binom{p^{-1}-2}{d}\), Jacobi orthogonality gives the displayed
\(r_{d,p}\) and \(F_d=\binom{p^{-1}-2}{d}^{-2}\).

In particular,
\[
\frac{F_d}{F_{d-1}}
=
\left(\frac{dp}{1-(d+1)p}\right)^2<1
\]
whenever \((2d+1)p<1\).

### 2. A joint moment central limit theorem

For \(1\le a\le2d+1\), define
\[
A_{a,n}=\frac1n\sum_{j=1}^nY_{j,n}^aE_j.
\]
Under \((4d+2)p<1\),
\[
\sqrt n\left(
A_{a,n}-\frac1{1-ap}
\right)_{a=1}^{2d+1}
\Longrightarrow N(0,C),
\qquad
C_{ab}=\frac1{1-(a+b)p}.
\]

Indeed, the deterministic means satisfy
\[
\frac1n\sum_{j=1}^nY_{j,n}^a
=\frac1{1-ap}+o(n^{-1/2})
\]
because \(ap<1/2\) throughout the required range. For every fixed linear
combination, the centered random part is a triangular array of independent
multiples of \(E_j-1\). Its largest coefficient is \(o(1)\) at the
\(\sqrt n\) scale, while its quadratic variance converges to the corresponding
quadratic form in \(C\). Lindeberg's condition follows from uniform
integrability of \((E_j-1)^2\), giving the claim by Cramér--Wold.

### 3. Delta method for the CG polynomial minimum

As a function of the raw moments \(A_1,\ldots,A_{2d+1}\),
\[
\Phi(A)=
\frac1{A_1}
\min_{r(0)=1,\ \deg r\le d}
\sum_{a,b=0}^d c_ac_bA_{a+b+1},
\qquad r(y)=\sum_{a=0}^dc_ay^a.
\]
The limiting Gram matrix is positive definite, so the minimizer is unique and
\(\Phi\) is differentiable near the limiting moment vector. By the envelope
theorem, its first variation at the limiting minimizer \(r_{d,p}\) is the
linear functional whose grid-point influence is
\[
h_{d,p}(t)
=
(1-p)t^{-p}
\left(r_{d,p}(t^{-p})^2-F_d\right),
\qquad t\in(0,1].
\]
The multivariate delta method therefore yields
\[
\sqrt n(M_{d,n}-F_d)
\Longrightarrow N\left(0,\int_0^1h_{d,p}(t)^2\,dt\right).
\]
Changing variables back to \(y=t^{-p}\) gives
\[
\int_0^1h_{d,p}(t)^2\,dt
=
(1-p)\int_1^\infty
y(r_{d,p}(y)^2-F_d)^2\,\nu_p(dy)
=
\sigma_{d,p}^2.
\]
The integrability condition is exactly ensured by \((4d+2)p<1\). The variance
is strictly positive because \(r_{d,p}(y)^2-F_d\) is not identically zero.

For the real-Haar model the normalized squared coordinates are generated by
independent \(\chi_1^2\) variables, whose mean is one and variance is two.
Only the covariance matrix in the preceding CLT changes, by a factor of two.

### 4. Critical stopping law

The stronger hypothesis \((4d+2)p<1\) also implies that degree \(d+1\) is in
the finite-moment regime. The closed form above gives
\[
F_{d-1}>F_d>F_{d+1}.
\]
Fixed-degree convergence therefore implies
\[
\Pr(M_{d-1,n}>F_d,\ M_{d+1,n}<F_d)\to1.
\]
On this event the CG stopping time at tolerance \(F_d\) is either \(d\) or
\(d+1\). The central limit theorem gives
\[
\Pr(M_{d,n}\le F_d)\to\Pr(N(0,\sigma_{d,p}^2)\le0)=\frac12,
\]
which proves the half-step law.

## Relation to prior work

Amsel et al. formulated the Haar power-law CG/RCD problem. Chen et al.
(arXiv:2606.02484v1) introduced the finite-degree floors \(F_D(p)\), proved
fixed-degree convergence \(M_{d,n}\to F_{\min(d,K(p))}\), and analyzed the
terminal critical floor \(F_{K(p)}(p)\) through first-inactive
Schur-complement asymptotics. Their current v1 does not state a
\(\sqrt n\)-Gaussian fluctuation theorem for an interior fixed-degree floor or
the resulting \(1/2\)-\(1/2\) CG stopping law.

Orthogonal-polynomial acceleration under power-law spectra is already known:
Velikanov and Yarotsky use Jacobi-polynomial structure in their sharp
power-law convergence analysis. Accordingly, the Jacobi representation above
is used as an explicit calculation, not claimed as the conceptual novelty of
this record.

Paquette and Trogdon prove central limit theorems and almost-deterministic CG
iteration counts for broad sample-covariance ensembles. That work establishes
important precedent for fluctuation analysis of Krylov methods, but it treats a
different random-matrix regime. Here the spectrum is deterministic and
power-law, while the randomness relevant to fixed-degree CG comes from the
Haar source weights.

The contribution claimed here is the critical-tolerance fluctuation law for
this Haar power-law source model, including the explicit variance and the
two-point limiting stopping distribution.

## Limitations

- The theorem is fixed-degree and assumes \((4d+2)p<1\). It does not cover the
  variance-critical boundary \((4d+2)p=1\) or the heavier-tail regime above it.
- It concerns exact arithmetic and exact unpreconditioned CG.
- It does not sharpen the terminal-floor Schur-complement regimes already
  treated by Chen et al.; rather, it resolves fluctuation behavior at strictly
  interior fixed-degree tolerance curves where a classical square-root-\(n\)
  CLT is available.
- Originality is to the best of our knowledge. The literature search located
  related CG fluctuation theorems for other random-matrix ensembles and
  Jacobi-polynomial power-law analyses, but no theorem matching this model and
  critical-tolerance statement.

## References

1. N. Amsel et al., *Linear Systems and Eigenvalue Problems: Open Questions
   from a Simons Workshop*, arXiv:2602.05394v2, 2026.
   https://arxiv.org/abs/2602.05394
2. L. Chen, Z. Liu, W. He, B. Dong, *Iteris: Agentic Research Loops for
   Computational Mathematics*, arXiv:2606.02484v1, 2026.
   https://arxiv.org/abs/2606.02484
3. M. Velikanov, D. Yarotsky, *Tight Convergence Rate Bounds for Optimization
   Under Power Law Spectral Conditions*, JMLR 25 (2024), 1--78.
   https://jmlr.org/papers/v25/23-0698.html
4. E. Paquette, T. Trogdon, *Universality for the Conjugate Gradient and MINRES
   Algorithms on Sample Covariance Matrices*, arXiv:2007.00640.
   https://arxiv.org/abs/2007.00640
