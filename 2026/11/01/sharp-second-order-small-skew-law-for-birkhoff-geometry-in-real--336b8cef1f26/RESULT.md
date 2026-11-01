# Sharp second-order small-skew law for Birkhoff geometry in real \(\ell_4^2\)

## Finding
For the real Banach plane \(X=\ell_4^2(\mathbb R)\), let \(x\perp_B y\) mean \(\|x+\lambda y\|_4\geq\|x\|_4\) for every real \(\lambda\). For \(t>0\) put
\[
D_t^B(X)=\sup_{\substack{\|x\|_4=\|y\|_4=1\\x\perp_B y}}
\frac{\|x+ty\|_4-\|tx-y\|_4}{t}.
\]
Define \(c=(4/27)^{1/4}\) and \(r_0=2-\sqrt3\). The full right-hand expansion through its second correction is
\[
\boxed{D_t^B(\ell_4^2)=c+\frac{t}{\sqrt3}
+c\left(1-\frac{13\sqrt3}{18}\right)t^2+O(t^3)
\qquad(t\downarrow0).}
\]
For every sufficiently small \(t>0\), all maximizing ordered unit pairs form one orbit under the signed-coordinate permutations of \(\ell_4^2\). A representative is
\[
 x_t=\frac{(1,r_t^{1/4})}{(1+r_t)^{1/4}},\qquad
 y_t=\frac{(-r_t^{3/4},1)}{(1+r_t^3)^{1/4}},
\]
where the *unique* optimal ratio satisfies the sharper displacement law
\[
\boxed{r_t=r_0+(3\sqrt3-6)t^2+O(t^3).}
\]
The linear displacement vanishes. The first term \(c\), which is an optimal reverse Birkhoff-support-functional residual, is not claimed as a new standalone geometric invariant; the new assertions are the two nonconstant coefficients and uniqueness/displacement for the actual finite-skew supremum.

## Assumptions and scope
All scalars are real, the norm is \(\|(u,v)\|_4=(|u|^4+|v|^4)^{1/4}\), and \(t\) tends to zero through positive values. The \(O(t^3)\) remainders mean absolute bounds independent of \(t\) on some interval \((0,\epsilon)\). No result is asserted for large \(t\), other exponents, or higher-dimensional spaces. A signed-coordinate permutation simultaneously acts on both members of an ordered pair; reversing just one vector generally changes the objective.

## Proof
**1. Global one-parameter reduction.** The real \(\ell_4^2\) norm is smooth. Its support functional at \(x=(x_1,x_2)\in S_X\) is \(j(x)(z)=x_1^3z_1+x_2^3z_2\). Thus \(x\perp_B y\) exactly when \(x_1^3y_1+x_2^3y_2=0\). By simultaneous sign changes and coordinate swap, a unit \(x\) can be written \(x=(1,s)/(1+s^4)^{1/4}\), with \(0\le s\le1\). There are exactly two possible unit partners, \(y=\pm(-s^3,1)/(1+s^{12})^{1/4}\). Set \(r=s^4\in[0,1]\). For the indicated sign put
\[
 J(r)=\sum_{i=1}^2 x_i y_i^3
 =\frac{r^{1/4}(1-r)}{(1-r+r^2)^{3/4}}\ge0,
 \qquad S(r)=\sum_{i=1}^2x_i^2y_i^2
 =\sqrt{\frac{r}{1-r+r^2}}.
\]
The other sign replaces \(J\) by \(-J\) and leaves \(S\) unchanged. At \(s=0\) and \(s=1\), \(J=0\); the expression extends continuously there.

**2. Exact quartic identity and uniform skew expansion.** Since \(\sum x_i^3y_i=0\), the binomial formula gives the identities
\[
 \|x+ty\|_4^4=1+6S(r)t^2+4J(r)t^3+t^4,
\qquad
 \|tx-y\|_4^4=1-4J(r)t+6S(r)t^2+t^4.
\]
In particular the objective for the indicated orientation is the exact scalar function
\[
 F(r,t)=\frac{(1+6St^2+4Jt^3+t^4)^{1/4}
 -(1-4Jt+6St^2+t^4)^{1/4}}t.
\]
The fourth roots are positive for all sufficiently small \(t\), uniformly over \(0\le r\le1\). Their binomial expansions, with uniform remainder, yield
\[
F(r,t)=J(r)+\frac32J(r)^2t+P(r)t^2+O(t^3),\quad
P(r)=J(r)-\frac92J(r)S(r)+\frac72J(r)^3.
\]
The same formula applies to the opposite orientation after replacing \(J\) by \(-J\). On every compact interval inside \((0,1)\), the expansion may be differentiated any fixed number of times in \(r\), because the exact roots are jointly analytic there.

**3. A unique nondegenerate leading maximizer.** We have
\[
 J(r)^4=\frac{r(1-r)^4}{(1-r+r^2)^3},\qquad
 \frac{J'(r)}{J(r)}=
 -\frac{(r+1)(r^2-4r+1)}{4r(r-1)(r^2-r+1)}.
\]
For \(0<r<1\) the derivative has the sign of \(r^2-4r+1\). Hence \(J\) rises strictly up to its only interior maximizer \(r_0=2-\sqrt3\) and falls strictly thereafter. Direct substitution gives
\[
 J(r_0)=c,\quad S(r_0)=\frac1{\sqrt3},\quad
 \frac{J''(r_0)}{c}=-\frac72-2\sqrt3<0.
\]
The negative-orientation branch converges uniformly to \(-J\) and therefore cannot maximize the objective for sufficiently small positive \(t\). Uniform convergence of \(F(\cdot,t)\) to \(J\) and compactness force every maximizing ratio to converge to \(r_0\). In a fixed neighborhood of \(r_0\), \(F_{rr}(\cdot,t)<0\) for all sufficiently small \(t\). Consequently the implicit function theorem provides the unique global maximizing critical point \(r_t\), analytic in \(t\) near zero. This proves the asserted isometry-orbit classification without assuming an extremizer pattern.

**4. Coefficients and displacement.** At the leading maximizer,
\[
 J(r_0)^2=\frac2{3\sqrt3},\quad
 \frac{P(r_0)}{c}=1-\frac{13\sqrt3}{18}.
\]
Since the coefficient \(\frac32J(r)^2\) has zero first derivative at \(r_0\), differentiating \(F_r(r_t,t)=0\) once yields \(r'_0=0\). The quadratic displacement comes from the next equation:
\[
 r_t-r_0=-\frac{P'(r_0)}{J''(r_0)}t^2+O(t^3),\qquad
 -\frac{P'(r_0)}{J''(r_0)}=3\sqrt3-6.
\]
Finally, \(r_t-r_0=O(t^2)\) implies that substituting \(r_t\) into \(F\) does not affect the coefficients through \(t^2\). Thus
\[
D_t^B(X)=F(r_t,t)=c+\frac32c^2t+P(r_0)t^2+O(t^3),
\]
with \(\frac32c^2=1/\sqrt3\) and the displayed value of \(P(r_0)\), as required.

## Verification
The accompanying `verify.py` verifies symbolically the exact quartic reduction, the one-critical-point derivative polynomial, the exact radical coefficients, and the second-order stationary displacement. It also checks normalizations and orthogonality directly from representative pairs, and compares direct norm evaluations with scalar formulas on deterministic sample ratios and small positive \(t\). Run `python verify.py` with the packages in `requirements.txt`. Finite samples are consistency checks, not proofs of the quantified global and asymptotic assertions; those follow from the exact reduction, strict leading maximum, uniform expansion and implicit function theorem above.

## Relationship to prior work
Qi, Li, Yin, Liu, Bi, Fu and Li introduced \(D_t^B\) in their 2026 preprint and established universal bounds, non-square-space consequences, a nonsmooth example, and relations with the modulus of convexity. Their inspected Section 3 (pp. 10–15), Section 4 and references contain no higher-order small-\(t\) calculation for real \(\ell_4^2\). At \(t=1\), \(D_1^B\) is the older Ji–Wu difference-of-chords constant \(D'\); neither this special case nor the universal upper bound implies the present asymptotics.

The leading limit \(\sup_{x\perp_B y}|j(y)(x)|\) is the reverse norming-functional residual underlying published results on sharp approximate Birkhoff symmetry in real \(L_p\) spaces. In particular, the previously established dimension-free scalar variational formula covers the \(t=0\) limit in \(\ell_4^2\), but contains no finite-skew norm difference. The \(t\) and \(t^2\) coefficients and quadratic movement of the maximizing pair require the fourth-power expansions and stationary perturbation analyzed here. Other existing exact invariants of \(\ell_4^2\) (Birkhoff i-angle, geometric-mean and generalized rectangular constants) are defined by distinct objective functions.

## Limitations
This is a one-sided local asymptotic law for a real two-dimensional space. It does not determine \(D_t^B\) globally over all \(t\), nor does it supply higher-dimensional or complex analogues. The leading asymmetry value was known under another formulation; publication priority of the higher-order coefficients remains subject to independent verification. The maximizing-pair classification is only asserted for sufficiently small positive \(t\), with no explicit numerical threshold \(\epsilon\).

## References
1. J. Qi, Q. Li, Z. Yin, Q. Liu, J. Bi, Y. Fu, Y. Li, *Skew geometric constants related to Birkhoff orthogonality in Banach spaces* (arXiv:2602.13974, v1 first public 2026-02-15, v2 2026-02-18), especially Section 3, https://arxiv.org/abs/2602.13974.
2. J. Chmieliński and P. Wójcik, *Approximate symmetry of Birkhoff orthogonality*, Journal of Mathematical Analysis and Applications 461 (2018), 625–640, doi:10.1016/j.jmaa.2018.01.031.
3. J. Chmieliński, T. Stypuła and P. Wójcik, *Approximate orthogonality in normed spaces and its applications*, Linear Algebra and its Applications 531 (2017), 305–317, doi:10.1016/j.laa.2017.06.001.
4. *Dimension-free \(C\)-approximate Birkhoff symmetry of real \(L_p\) spaces* (2026), published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dimension-free-c-approximate-birkhoff-symmetry-of-real-l-p-space--5f371e82ef77.
5. P. L. Papini and S. Wu, *Measurements of differences between orthogonality types*, Journal of Mathematical Analysis and Applications 397 (2013), 285–291.
