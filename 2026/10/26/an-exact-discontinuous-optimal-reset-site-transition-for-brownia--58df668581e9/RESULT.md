# An exact discontinuous optimal reset-site transition for Brownian interval cover times

## Finding

Consider the complete cover time of a reflected Brownian searcher in a closed interval with Poisson resets to its **initial position**, and treat the reset site as a design parameter while holding the reset rate fixed. The entire set of globally optimal reset sites can be classified exactly. The optimizing site jumps from a boundary to the midpoint at a finite critical reset rate; no off-center interior site is ever optimal.

Write \(\kappa=L\sqrt{r/D}\), \(a=x/L\), and \(c=\cosh(\kappa/2)\). For \(r>0\), let \(M_r(x)\) denote the mean time needed to visit **both** endpoints of \([0,L]\) when the particle both starts and resets to \(x\). Then
\[
rM_r(x)=
\frac{\cosh\kappa}{\cosh(\kappa a)}
+\frac{\cosh\kappa}{\cosh(\kappa(1-a))}
-\frac{\cosh(\kappa/2)}
{\cosh(\kappa(a-1/2))}-1.
\tag{1}
\]
Equation (1) itself is **not claimed as a new result**: it is algebraically equivalent to the general asymmetric constrained-Brownian formula (38) of Linn and Lawley [2].

The new reset-site minimization theorem is
\[
\mathop{\rm argmin}_{x\in[0,L]}M_r(x)=
\begin{cases}
\{0,L\},&0<r<r_*,\\
\{0,L/2,L\},&r=r_*,\\
\{L/2\},&r>r_*,
\end{cases}
\tag{2}
\]
where the **exact**, dimensionless crossover is
\[
c_*=\frac{1+\sqrt{17}}4,\qquad
r_*=\frac{4D}{L^2}\operatorname{arcosh}^2(c_*),
\qquad
\frac{r_*L^2}{4D}=0.537080373233492\ldots.
\tag{3}
\]
There are no other global minimizers, including at the threshold. The minimum value is
\[
\min_x M_r(x)=\frac1r\min\left\{
\cosh\kappa-1,\,
3\cosh(\kappa/2)-\frac2{\cosh(\kappa/2)}-1
\right\}.
\tag{4}
\]

A separate exact local-shape threshold occurs at
\[
r_{\rm loc}=
\frac{4D}{L^2}\operatorname{arcosh}^2
\left(\sqrt{1+\frac1{\sqrt5}}\right)
<r_*.
\tag{5}
\]
For \(0<r<r_{\rm loc}\), the mean cover time decreases strictly from the midpoint toward either edge. For \(r>r_{\rm loc}\), the midpoint is a strict local minimum, the edges remain strict one-sided local minima, and exactly two symmetric interior local **maxima** separate them. At \(r=r_{\rm loc}\) the midpoint is a degenerate local maximum, not an additional minimum. Therefore the midpoint becomes locally favorable before it becomes globally optimal.

## Assumptions and scope

Take \(L,D,r>0\). Between resets \(X_t\) is a continuous one-dimensional reflected Brownian motion on \([0,L]\) with generator \(D\,\partial_{xx}\); both endpoints are instantaneously reflected and counted as visited upon contact. Independently, a homogeneous rate-\(r\) Poisson clock returns the particle instantaneously to the deterministic starting and resetting site \(x\in[0,L]\). Resetting the particle **does not erase** its already visited endpoint set. With
\[
\tau_0=\inf\{t\ge0:X_t=0\},\qquad
\tau_L=\inf\{t\ge0:X_t=L\},
\]
define \(T_{\rm cov}=\max(\tau_0,\tau_L)\) and \(M_r(x)=\mathbb E_xT_{\rm cov}\). Endpoint starting/reset positions are allowed and the initially occupied endpoint is already covered. The rate \(r\) is fixed when minimizing over \(x\).

## Proof

**1. Exact mean through independent endpoint hitting problems.** For any no-reset positive hitting time \(\tau\) with \(\phi(r)=\mathbb E[e^{-r\tau}]\), resetting to the same starting point yields mean \((1-\phi(r))/(r\phi(r))\) by geometric-renewal conditioning. The no-reset Laplace transforms for hitting the left and right endpoints with reflection at the opposite endpoint are, respectively,
\[
\phi_0(r;x)=\frac{\cosh(\kappa(1-a))}{\cosh\kappa},
\quad
\phi_L(r;x)=\frac{\cosh(\kappa a)}{\cosh\kappa}.
\]
The no-reset Laplace transform for hitting **either** endpoint, with both endpoints treated as absorbing for this single question, is
\[
\phi_{\{0,L\}}(r;x)=
\frac{\cosh(\kappa(a-1/2))}{\cosh(\kappa/2)}.
\]
These solve the elementary boundary-value problem \(D\phi''=r\phi\) with the relevant absorbing values and reflecting derivatives. Since
\[
\Pr(T_{\rm cov}>t)=\Pr(\tau_0>t)+\Pr(\tau_L>t)
-\Pr(\min(\tau_0,\tau_L)>t)
\]
for the **same reset process**, inclusion-exclusion and integration give (1). The calculation remains valid because resetting preserves the visited-set memory: inclusion-exclusion concerns the actual first hitting times over the full run, not a reset of that memory.

**2. Global shape reduction.** By reflection symmetry it suffices to consider \(a\in[0,1/2]\). Put \(b=c^2-1>0\) and
\[
t=\cosh(\kappa(a-1/2))\in[1,c].
\]
The sum of the two reciprocals in (1) simplifies by the hyperbolic addition formula. Consequently
\[
F_c(t):=rM_r(x)=
\frac{2c(2c^2-1)t}{t^2+b}-\frac ct-1.
\tag{6}
\]
Differentiation shows
\[
F_c'(t)=
\frac{c\,P_c(t^2)}{t^2(t^2+b)^2},
\quad
P_c(w)=(3-4c^2)w^2+4c^2(c^2-1)w+(c^2-1)^2.
\tag{7}
\]
Because the leading coefficient of \(P_c\) is negative and its constant term is positive, its two real zeros have opposite signs. Thus \(P_c(w)\) is positive up to its **single positive root**, and negative afterward. In particular \(F_c\) can have at most one interior stationary point on \([1,c]\), and any such stationary point is a **maximum**, never a minimum. Therefore the global minimizers on \([0,L]\) belong to \(\{0,L/2,L\}\), independently of any numerical search.

**3. Exact crossing and uniqueness.** Evaluating (1) at the edge and midpoint gives
\[
rM_r(0)=rM_r(L)=2(c^2-1),\qquad
rM_r(L/2)=3c-\frac2c-1.
\]
Their difference factors exactly as
\[
r\bigl(M_r(0)-M_r(L/2)\bigr)
=\frac{(c-1)(2c^2-c-2)}c.
\tag{8}
\]
For \(c>1\), the sign in (8) changes precisely at the unique positive root \(c_*=(1+\sqrt{17})/4\) of the quadratic. By (7) there are no competing interior minima. This proves the complete classification (2)–(4), including exactly three minimizers at equality.

**4. Local morphology.** At the midpoint \(t=1\), the sign of the second derivative of \(M_r\) with respect to \(x\) is the sign of \(F_c'(1)\), hence of
\[
P_c(1)=5(c^2-1)^2-1.
\tag{9}
\]
The unique sign change at \(c_{\rm loc}=\sqrt{1+1/\sqrt5}\) gives (5). Also \(P_c(c^2)=1-2c^2<0\), so once \(P_c(1)>0\), the single positive root of \(P_c\) lies strictly between \(1\) and \(c^2\), producing exactly two off-center local maxima. At equality in (9), \(P_c(t^2)<0\) for \(t>1\) close to one; hence the center is a degenerate maximum. Direct substitution gives \(c_{\rm loc}<c_*\), completing the claimed local-to-global transition.

## Verification

The supplied standalone script `verify_reset_site.py` uses the Python standard library. It checks the formula (1) independently against the asymmetric constrained-interval formula in [2], verifies the rational reduction, root and factor identities, derivative agreement by centered differences, near-zero-reset expansion and finite-grid global minima across a nontrivial parameter range. Its executed result was **7,159 deterministic comparisons passed**. Numerical checks corroborate the formulas and are not used as a substitute for the all-parameter derivative argument.

For \(L=D=1\), the threshold is \(r_*=2.14832149293397\ldots\). At \(\kappa=1.4\) the boundary and midpoint mean cover times are \(0.5871930946\) and \(0.5980082127\); at \(\kappa=1.6\), they are \(0.6161970591\) and \(0.5925410166\). These values independently illustrate the switch.

As \(r\downarrow0\), the mean tends to
\[
M_0(x)=\frac{L^2+Lx-x^2}{2D},
\]
whose minimizers are the endpoints. The \(r=0\) statement is a consistency limit rather than part of theorem (2), which assumes \(r>0\).

## Relationship to prior work

Linn and Lawley [2, Section 4.1, equation (38)] already derived a **fully asymmetric exact mean cover-time formula** for reflected Brownian search on an interval with resetting to the initial position; by translation and algebra their expression coincides with (1). Their main analysis addresses cover-time formulas, frequent-reset asymptotics, and **reset-rate** optimization. The current claim does **not** present (1), its midpoint specialization, or its large-rate asymptotics as new. Its claimed addition is the global **reset-position** optimization theorem (2), the exact algebraic discontinuity (3), and the separate local shape threshold (5). These conclusions require proving the sign structure of the derivative over the complete continuum of possible reset sites rather than simply evaluating the known mean at one or two prescribed points.

Ghosh and Sabhapandit [1] investigate the same reflected search at the **fixed midpoint** and optimize the reset rate, obtaining a distinct optimal dimensionless rate of approximately \(1.76976\). They do not vary the initial/reset location in their model. The rate \(0.53708037\ldots\) in (3) is a **switching rate for the optimal location**, not the optimum reset rate for the midpoint protocol. General single-target optimal-reset-location literature [3] concerns first passage to one target rather than visiting both reflecting endpoints.

## Limitations

All conclusions require spatially homogeneous diffusion, perfectly reflecting interval endpoints, exact resetting to the common deterministic start site, preserved coverage memory and an independent Poisson reset clock. Resetting to a distribution, a separate point from the initial site, partly absorbing boundaries, finite detection radii or simultaneous optimization of reset location **and** rate are outside the theorem. No claim is made that the known exact mean formula (1) is original. Since its site-optimization consequences are obtained from an earlier exact formula, priority risk remains that the transition may be implicit in other treatments of that formula; independent assessment is not performed here.

## References

[1] A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting*, arXiv:2605.31207v1 (first public May 29, 2026), https://arxiv.org/abs/2605.31207.

[2] S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154v2, Section 4.1 and equation (38), https://arxiv.org/abs/2406.12154 (first public 2024; later Chaos 35, 043124 (2025)).

[3] V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, Phys. Rev. E 109, 044134 (2024), arXiv:2401.01125, https://arxiv.org/abs/2401.01125.
