# Sharp algebraic all-weight locking threshold for an alternating four-cycle

## Finding
For the attractive four-oscillator Kuramoto ring with alternating natural frequencies \((-1,1,-1,1)\), three unit-weight edges and one strengthened edge of relative weight \(1+a\), the exact infimum of global coupling strengths supporting a **strictly linearly attracting phase-locked state modulo uniform rotation** is \(K_c(a)\) below. It is strictly increasing for the *entire* range \(a\geq0\), not merely under a small edge perturbation, and approaches a nontrivial limit as \(a\to\infty\).

For \(a=0\), \(K_c(0)=1/2\). For \(a>0\), put \(c=a/(a+2)\), and let \(z=z(c)>1\) be the **unique** solution of
\[
(1+cz)^{3/2}=(1+c)(z^2-1).
\]
Then
\[
\boxed{K_c(a)=\left[\sqrt{\frac{z}{z+c}}\left(1+\frac{1+c}{\sqrt{1+cz}}\right)\right]^{-1}.}
\]
The equality case does not support strict transverse linear attraction; such states exist for **every** \(K>K_c(a)\) and no such state exists for \(K\leq K_c(a)\). The sharp endpoints and initial sensitivity are
\[
K_c(a)=\frac12+\frac{\sqrt2-1}{8}a+O(a^2)\quad(a\downarrow0),
\]
\[
\lim_{a\to\infty}K_c(a)=\frac{1}{(1+2u)\sqrt{1-u^2}}=0.568126105332\ldots,
\qquad u=\frac{\sqrt{33}-1}{8}.
\]
Thus the excess locking cost stays positive even when the exceptional edge becomes arbitrarily strong.

## Assumptions and scope
Phases \(\theta_i\in\mathbb R/(2\pi\mathbb Z)\) obey
\[
\dot\theta_i=\omega_i+K\sum_{j:\{i,j\}\in E}w_{ij}\sin(\theta_j-\theta_i),
\quad \omega=(-1,1,-1,1),\quad K>0,
\]
where \(E=\{\{1,2\},\{2,3\},\{3,4\},\{4,1\}\}\), \(w_{23}=1+a\), the other weights are \(1\), and \(a\geq0\). An equilibrium is strictly linearly attracting modulo phase shifts if its Jacobian has a single rotational zero eigenvalue and all remaining eigenvalues are strictly negative. No assertion is made about nonlinear stability at the nonhyperbolic threshold, global basins, or nonstationary attractors.

## Proof
**1. Every strictly stable equilibrium has equal acute angles on opposite unmodified edges.** Orient the edges cyclically and set \(\alpha_i=\theta_{i+1}-\theta_i\) (indices modulo four). The balance equations and alternating forcing give the current identity \(\sin\alpha_1=\sin\alpha_3\). Let \(Q\) be the negative Jacobian quadratic form divided by \(K\), namely
\[
Q(v)=\sum_{i=1}^4w_i\cos\alpha_i\,(v_{i+1}-v_i)^2,
\qquad(w_1,w_2,w_3,w_4)=(1,1+a,1,1).
\]
The admissible increment perturbation \((d_1,d_2,d_3,d_4)=(1,0,-1,0)\) gives \(Q=\cos\alpha_1+\cos\alpha_3\). Since the two cosines have the same absolute value, strict positivity of \(Q\) on nonconstant vectors forces **both** positive; equality, opposite signs, and two negative signs are excluded. Their equal sines and positive cosines therefore imply \(\alpha_1=\alpha_3=\phi\) modulo \(2\pi\), where \(-\pi/2<\phi<\pi/2\). After a common phase shift, each candidate equilibrium has the form \((0,\phi,\delta,\phi+\delta)\).

**2. Scalar reduction and elimination of the second branch.** The four balance equations reduce to
\[
\frac1K=\sin\phi+\sin(\phi+\delta),\qquad
\sin(\phi+\delta)=(1+a)\sin(\phi-\delta).
\]
For \(a>0\), the second relation is equivalent to \(\tan\delta=c\tan\phi\). Its two possible branches modulo \(2\pi\) are \(\delta=\delta_c(\phi):=\arctan(c\tan\phi)\) and \(\delta=\delta_c(\phi)+\pi\). On the second branch the right-hand side of the first relation equals \(\sin\phi-\sin(\phi+\delta_c(\phi))\leq1\) for every allowed \(\phi\). On the first branch a positive value greater than one forces \(\phi>0\), and writing \(t=\tan\phi>0\) gives the exact scalar function
\[
T_c(t)=\frac{t}{\sqrt{1+t^2}}\left(1+\frac{1+c}{\sqrt{1+c^2t^2}}\right).
\]
Its maximum is strictly greater than one: for example \(\phi=\pi/4\) yields \(\sin\phi+\sin(\phi+\delta_c(\phi))\geq\sqrt2\). Hence any strictly stable state with \(K<K_c\), if such a threshold is defined using \(\max T_c\), would require \(1/K>\max T_c>1\), impossible on either the negative-angle or second branch.

**3. Exact unique maximizer.** Differentiating the displayed \(T_c\) shows that the sign of its derivative is the sign of
\[
(1+c^2t^2)^{3/2}+(1+c)(1-c^2t^4).
\]
Its critical points require \(z=ct^2>1\) and
\[
(1+cz)^{3/2}=(1+c)(z^2-1).
\]
The ratio \((1+c)(z^2-1)/(1+cz)^{3/2}\) increases strictly from zero to infinity on \(z>1\), because the numerator controlling its logarithmic derivative is \(4z+cz^2+3c>0\). Thus there is a unique critical point; \(T_c(0+)=0\), \(T_c(+\infty)=1\), and \(T_c(1)\ge\sqrt2>1\), so this point is the strict global maximum. Substituting \(t=\sqrt{z/c}\) yields the displayed algebraic formula for \(K_c(a)=1/\max T_c\).

**4. Exact transverse stability.** For \(\phi>0\) on the first branch put \(g_2=(1+a)\cos(\phi-\delta)>0\), \(g_4=\cos(\phi+\delta)\), and \(h=\cos\phi>0\). In independent edge-increment coordinates \(u,v,s\) the full quadratic form is
\[
Q=2h v^2+(2h+g_2+g_4)u^2+2(g_4-g_2)us+(g_2+g_4)s^2.
\]
Here \(g_2+g_4=a\cos(\phi-\delta)+2\cos\phi\cos\delta>0\). Differentiating the balance relation in \(\phi\) gives \(\delta_c'=(g_2-g_4)/(g_2+g_4)\), and the determinant of the \((u,s)\) block is precisely
\[
2h(g_2+g_4)+4g_2g_4=2(g_2+g_4)\frac{d}{d\phi}\left[\sin\phi+\sin(\phi+\delta_c(\phi))\right].
\]
Therefore \(Q\) is positive definite modulo the uniform phase direction **exactly** on the increasing side of the unique scalar maximum, and singular at that maximum. Since \(T_c\) increases continuously from zero to its maximum, every \(K>K_c(a)\) has a strictly stable equilibrium, while the preceding branch exclusions forbid one for \(K<K_c(a)\). At \(K=K_c(a)\), the first branch can only attain the maximum with zero determinant, and the other branches are excluded because \(1/K_c=\max T_c>1\). Hence strict stability also fails at equality. For \(a=0\) the solution \((0,\phi,0,\phi)\) has \(1/K=2\sin\phi\) and all four edge cosines positive precisely when \(K>1/2\), proving the base case.

**5. Monotonicity, endpoint, and singular onset.** On \(0<c<1\) write \(\delta_c(\phi)=\arctan(c\tan\phi)\). At the unique maximizer \(\phi_c\), the angle \(\phi_c+\delta_c(\phi_c)\) lies strictly between \(\pi/2\) and \(\pi\): before the sum reaches \(\pi/2\), both terms in the derivative of \(\sin\phi+\sin(\phi+\delta_c(\phi))\) are positive. Thus the envelope derivative is strictly negative:
\[
\frac{d}{dc}\max_\phi\bigl(\sin\phi+\sin(\phi+\delta_c(\phi))\bigr)
=\cos(\phi_c+\delta_c(\phi_c))\frac{\tan\phi_c}{1+c^2\tan^2\phi_c}<0.
\]
Since \(c=a/(2+a)\) strictly increases, \(K_c(a)\) strictly increases for positive \(a\) as well. Its continuous extension at zero is \(1/2\), so strict increase holds on the closed half-line.

As \(c\uparrow1\), \(\delta_c(\phi)\to\phi\), leaving the maximization of \(\sin\phi+\sin2\phi\). Its derivative vanishes when \(\cos\phi+2\cos2\phi=0\), whose unique solution has \(\cos\phi=u=(\sqrt{33}-1)/8\). This proves the stated finite large-edge limit. At the opposite end, the implicit equation for \(z(c)\) has \(z(0)=\sqrt2\) and nonzero derivative with respect to \(z\) at \((0,\sqrt2)\). Consequently \(z(c)=\sqrt2+O(c)\), and the formula for \(\max T_c\) expands to \(2-(\sqrt2-1)c+O(c^2)\). Substituting \(c=a/2+O(a^2)\) and taking reciprocals proves the initial derivative and its quadratic remainder.

## Verification
Run `python3 verify.py` with Python 3.9+ and only the standard library. The checker evaluates the exact algebraic reduction at rational parameters, solves the unique critical scalar equation at twelve distinct edge strengths, reconstructs genuine stable equilibria at four couplings above each threshold, and checks the full four-node vector field and positive definiteness of the gauge-fixed Hessian. It also checks the predicted limiting value and initial slope. The results are recorded in `verify_output.txt`. The all-parameter and no-other-equilibria assertions depend on the analytic proof, not numerical sampling.

## Relationship to prior work
Manik, Timme and Witthaut (arXiv:1611.09825v2, Section IV.4) **already present the same alternating four-node ring with one strengthened edge** and report the Braess loss of locking through a numerical stability diagram and general cycle-flow conditions. The present result does not claim discovery of that phenomenon; it determines a new exact algebraic threshold for every proportional edge strengthening, its strict all-strength monotonicity, a nonzero strong-edge saturation, and a sharp initial derivative. Their work uses additive link capacity \(K+\kappa\); the present proportional-strength slice is \(K(1+a)\) and the exact dependence along every such ray is analyzed.

Arches, Fleurantin, Holzer, Sood and Uddin (arXiv:2608.03594v1, Section IV, "simple ring network with symmetry") revisit precisely this alternating ring. Their objective there is the first-order change in an order parameter for \(K>1/2\), and they explicitly identify the four-dimensional Jacobian kernel at its onset, which prevents directly using their simple-fold theorem. They do not state the algebraic global onset law, nonzero saturation, or its degenerate-limit slope. These specific quantitative claims are the subject here. A previously indexed four-node closing-edge result concerns natural frequencies \((-1,0,0,1)\) on a three-edge path plus a variable *new* closing edge, and its nonmonotone threshold is not an implication for the alternating four-edge ring.

## Limitations
The theorem concerns strictly stable equilibria only, not their basins, nonlinear dynamics at the nonhyperbolic threshold, finite-time synchronization, or global attractors. It fixes alternating frequencies, three equal edges, and exactly one exceptional edge; no general weighted-cycle classification is claimed. The Braess phenomenon itself was known. Although the inspected primary texts did not give the precise algebraic all-weight formula and asymptotics, they contain general cycle-flow machinery; an unexamined older specialization could affect historical priority. Independent mathematical or literature-priority review has not been performed.

## References
1. Justin Arches, Emmanuel Fleurantin, Matt Holzer, Siddhant Sood, Shakeeb Uddin, *Predicting the occurrence of Braess paradox in the synchronization threshold of coupled oscillator systems*, arXiv:2608.03594v1, first submitted 2026-08-04. https://arxiv.org/html/2608.03594v1
2. Debsankha Manik, Marc Timme, Dirk Witthaut, *Cycle flows and multistability in oscillatory networks: an overview*, arXiv:1611.09825v2, 2016, Section IV.4. https://arxiv.org/html/1611.09825v2
3. Bertrand Ottino-Löffler, Steven H. Strogatz, *Comparing the locking threshold for rings and chains of oscillators*, arXiv:1610.00296 (2016). https://arxiv.org/abs/1610.00296
