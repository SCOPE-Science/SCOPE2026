# The sharp two-sided imaginary-axis stability frontier for complex quadratic time integrators

## Finding

**Theorem (mixed-sign imaginary-axis frontier).** Let \(R,S>0\), and let
\[
P_c(z)=1+z+cz^2,\qquad c\in\mathbb C.
\]
There exists a coefficient \(c\) satisfying
\[
|P_c(iy)|\le 1\quad\hbox{for every }y\in[-S,R]
\]
if and only if \(R+S\le 2\). At the sharp boundary \(R+S=2\), the coefficient is **unique** and is
\[
c_* = \frac{2+i(R-S)}{R^2+S^2}.
\]
Writing \(R=1+\eta\), \(S=1-\eta\), where \(-1<\eta<1\), the unique extremal polynomial has \(c_*=(1+i\eta)/(1+\eta^2)\) and satisfies the exact identity
\[
|P_{c_*}(iy)|^2-1=\frac{y^2}{1+\eta^2}\bigl(y-(1+\eta)\bigr)\bigl(y+(1-\eta)\bigr).
\]
Consequently, the inequality is strict at each nonzero interior imaginary-axis point and becomes equality at both nonzero endpoints.

**Corollary (optimal step and cost of real coefficients).** Suppose \(A\) is a complex normal matrix with purely imaginary spectrum and with both spectral extremes \(i\Omega_+\) and \(-i\Omega_-\), where \(\Omega_+,\Omega_->0\). For methods whose stability polynomial is \(P_c\), the largest positive step making the entire spectrum contractive is
\[
h_{\rm complex}=\frac{2}{\Omega_++\Omega_-},\qquad
c_{\rm optimal}=\frac{1+i\eta}{1+\eta^2},\qquad
\eta=\frac{\Omega_+-\Omega_-}{\Omega_++\Omega_-}.
\]
If \(c\) must be real, the optimum is instead
\[
h_{\rm real}=\frac{1}{\max\{\Omega_+,\Omega_-\}},\qquad c_{\rm real}=1.
\]
Thus the exact step-size improvement of allowing complex coefficients is
\[
\frac{h_{\rm complex}}{h_{\rm real}}=
\frac{2\max\{\Omega_+,\Omega_-\}}{\Omega_++\Omega_-},
\]
which equals one for balanced frequencies and approaches two for strongly unbalanced, nonempty two-sided spectra.

## Assumptions and scope

The polynomial is a general **two-stage, first-order consistent, complex-coefficient** stability polynomial; no second-order condition is imposed. The interval includes every continuous imaginary-axis frequency between its endpoints. Both endpoint lengths are strictly positive. In the matrix corollary, normality is needed for the identification of operator-norm contractivity with spectral amplification; the spectrum is allowed to have gaps, but both indicated extremes must occur. The result is a linear absolute-stability statement, not a positivity, energy-conservation, or nonlinear-accuracy theorem.

Every such polynomial has a two-complex-Euler-factor representation: choose roots \(w_1,w_2\) of \(w^2-w+c=0\); then \(w_1+w_2=1\) and
\[
P_c(z)=(1+w_1z)(1+w_2z).
\]
The two substeps sum to the real macroscopic step, although the intermediate states can be complex. A direct complex-coefficient first-order two-stage Runge--Kutta realization is also available: evaluate \(K_1=F(u)\), \(K_2=F(u+chK_1)\), and set \(u^+=u+hK_2\).

## Proof

Write \(c=a+ib\) with real \(a,b\). Direct expansion, valid for every real \(y\), gives
\[
|P_c(iy)|^2-1
=y^2\left[(a^2+b^2)y^2-2by+1-2a\right]. \tag{1}
\]
The bracket is a convex quadratic function of \(y\). Its values at \(-S\) and \(R\) are nonpositive if and only if the bracket is nonpositive on the entire interval. Therefore **checking the two endpoints is necessary and sufficient**; the value at zero presents no exception because \(P_c(0)=1\).

For any nonzero real \(y\), endpoint contractivity can be rewritten as
\[
\left|c-\frac{1+iy}{y^2}\right|\le\frac{1}{y^2}. \tag{2}
\]
Thus \(c\) must lie in the intersection of two closed disks, with centers
\[
z_+=\frac{1+iR}{R^2},\qquad
z_- =\frac{1-iS}{S^2}
\]
and radii \(r_+=R^{-2}\), \(r_-=S^{-2}\). Direct calculation yields
\[
|z_+-z_-|^2-(r_++r_-)^2
=\frac{(R+S)^2-4}{R^2S^2}. \tag{3}
\]
Two closed disks intersect exactly when their center distance does not exceed the sum of their radii, proving existence precisely for \(R+S\le2\). If \(R+S=2\), the disks are externally tangent and intersect at exactly one point. The division point of their center segment is
\[
c_*=\frac{r_-z_++r_+z_-}{r_++r_-}=
\frac{2+i(R-S)}{R^2+S^2}. \tag{4}
\]
Substituting \(R=1+\eta\), \(S=1-\eta\) into (1), followed by algebraic factorization, yields the displayed exact identity. Since \(-S<y<R\), both nonzero factors have opposite signs for interior \(y\), proving strict contractivity there except at \(y=0\).

For the matrix corollary, scale \(R=h\Omega_+\), \(S=h\Omega_-\). The theorem gives exactly the upper bound \(h(\Omega_++\Omega_-)\le2\), with the unique complex coefficient on equality. If \(b=0\), (1) becomes
\[
y^2(a^2y^2+1-2a).
\]
Thus the largest symmetric imaginary-axis halfwidth for a real coefficient is
\[
\sup_{a\in\mathbb R,\,a>1/2}\frac{\sqrt{2a-1}}{|a|}=1,
\]
uniquely attained at \(a=1\), since \(a^2-(2a-1)=(a-1)^2\ge0\). This establishes the real-coefficient bound and equality case. The spectral theorem for a normal matrix gives \(\|P_c(hA)\|_2=\max_{\lambda\in\sigma(A)}|P_c(h\lambda)|\). The strict inequalities and the ratio formula follow.

## Verification

The supplied `verify.py` verifies (1), (3), and the factorization symbolically using SymPy, tests 5,959 exact-rational frequency/parameter pairs, and checks 198 endpoint-instability and speedup cases. Reproduction: `python3 verify.py`, with Python 3 and SymPy installed. A successful run ends with `VERIFY_OK`. The infinite-parameter theorem rests on the preceding disk-intersection proof, not on the finite tests.

As a concrete exact example, frequencies \(\Omega_+=2\), \(\Omega_-=1\) give \(h=2/3\), \(\eta=1/3\), and \(c_*=9/10+3i/10\). Both scaled endpoints \(4/3\) and \(-2/3\) are neutrally amplified, all nonzero interior points are strictly damped, and the best real-coefficient step is only \(1/2\).

## Relationship to prior work

George, Koellermeier, Jung and Mangan (arXiv:2601.07730, publicly posted January 12, 2026; version 2 dated October 23, 2026), Theorem 1, identify the unique optimal first-order quadratic complex polynomial for **one-sided** positive or negative imaginary-axis spectra: \(c=(1\pm i)/2\) and maximum interval length two. Their Theorem 2 and numerical tables also optimize one-sided intervals. The theorem here covers the distinct setting of **simultaneously present positive and negative frequencies**, determines the *entire exact two-sided feasible frontier*, and gives the unique limiting optimizer at every asymmetry, as well as its continuous exact amplification factor.

Ketcheson and Ahmadia (arXiv:1201.3035) develop general optimal stability-polynomial methods with **real polynomial coefficients**, including symmetric imaginary-axis optimization. Doehring, Gassner and Torrilhon (2024) optimize higher-stage **real-coefficient** Runge--Kutta stability polynomials. These methods provide relevant optimization context but do not state the mixed-sign, complex-coefficient disk tangency classification. The one-sided formulas of George et al. arise as limits as one of the two prescribed positive endpoint lengths approaches zero; they do not imply the mixed-sign bound or coefficient uniqueness without an additional argument.

## Limitations

This is an exact result for a first-order two-stage quadratic polynomial. It is not an order-two method, and it does not optimize total error, internal amplification, stage positivity, or nonlinear long-time behavior. The matrix consequence assumes normality and spectral containment on the imaginary axis; it does not yield Euclidean contractivity for nonnormal matrices. The optimization is for an entire interval (or for spectra including both endpoint frequencies), not a claim about every arbitrary finite set of interior frequencies. Historical priority remains subject to potentially equivalent earlier specialized complex-coefficient stability-polynomial work beyond the accessible literature inspected; no independent mathematical audit has been performed.

## References

1. J. D. George, J. Koellermeier, S. Y. Jung, and N. M. Mangan, *Explicit complex time integrators for stiff problems*, arXiv:2601.07730v1 (January 12, 2026), arXiv:2601.07730v2 (October 23, 2026). https://arxiv.org/html/2601.07730v2
2. D. I. Ketcheson and A. J. Ahmadia, *Optimal stability polynomials for numerical integration of initial value problems*, arXiv:1201.3035 (January 14, 2012), *Communications in Applied Mathematics and Computational Science* 7 (2013), 247--271. https://arxiv.org/abs/1201.3035
3. D. Doehring, G. J. Gassner, and M. Torrilhon, *Many-Stage Optimal Stabilized Runge--Kutta Methods for Hyperbolic Partial Differential Equations*, *Journal of Scientific Computing* 99, 28 (2024). https://doi.org/10.1007/s10915-024-02478-5
