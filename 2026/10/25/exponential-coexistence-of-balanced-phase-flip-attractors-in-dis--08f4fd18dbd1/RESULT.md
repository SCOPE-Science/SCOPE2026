# Exponential coexistence of balanced phase-flip attractors in discrete Huygens stars

## Finding

For an unweighted star with an even number \(m\ge4\) of labeled leaves, a common phase-quotient sinusoidal update has at least
\[
N_m=\frac12\binom{m}{m/2}
\]
distinct attracting prime-period-two cycles throughout a *sharp shared step-size window* \(h_m<h<\pi\). The window opens above the familiar small-step gradient regime. The cycles coexist with disjoint open local basins, and the entire family persists when the individual positive edge weights are perturbed sufficiently little.

Let \(q=m+1\). The lower endpoint is
\[
h_m=\frac{2\delta_m}{\sin\delta_m},\qquad
q\delta_m\cot\delta_m=1,\quad0<\delta_m<\frac\pi2.
\]
The root is unique. For even \(m\to\infty\), the window shrinks as
\[
\pi-h_m=\frac4{\pi(m+1)}+O(m^{-2}).
\]
The multiplicity grows as \(N_m\sim2^{m-1}\sqrt{2/(\pi m)}\). These numbers count the explicitly constructed balanced orbits, *not* all orbits of the map.

## Assumptions and scope

Let \(m\) be an even integer, \(m\ge4\). Orient all \(m\) edges of a unit-weight star from its center to its labeled leaves. After quotienting common phase, its edge differences \(z\in\mathbb T^m=(\mathbb R/2\pi\mathbb Z)^m\) evolve by
\[
F_{m,h}(z)=z+hK_m\sin z\pmod{2\pi},\qquad
K_m=I_m+\mathbf1\mathbf1^{\mathsf T},\qquad h>0.
\]
The sine is applied coordinatewise. A sign vector \(s\in\{\pm1\}^m\) is *balanced* when \(\sum_{i=1}^m s_i=0\). A prime period-two orbit means a two-point orbit whose points are distinct modulo \(2\pi\). Local exponential attraction means attraction from an open neighborhood, with a geometric convergence rate for the second iterate.

## Proof

**Step 1: a unique balanced branch.** The scalar function \(H(\delta)=2\delta/\sin\delta\) is strictly increasing on \((0,\pi)\), since \(\sin\delta-\delta\cos\delta>0\) there: this difference starts at zero and has derivative \(\delta\sin\delta>0\). Its endpoint limits are \(2\) and \(+\infty\). Thus for each \(h>2\), there is a unique \(\delta\in(0,\pi)\) with \(h\sin\delta=2\delta\).

For each balanced \(s\), \(K_ms=s\), and for \(z_s^{\pm}=\pi\mathbf1\pm\delta s\) we have \(\sin z_s^\pm=\mp\sin\delta\,s\). Hence
\[
F_{m,h}(z_s^\pm)
=\pi\mathbf1\pm(\delta-h\sin\delta)s
=\pi\mathbf1\mp\delta s=z_s^\mp\pmod{2\pi}.
\]
The two points are distinct because \(0<\delta<\pi\). If two such cycles coincide, their balanced signs agree up to an overall reversal: coordinate differences between \(\delta\) and \(-\delta\) are nonzero modulo \(2\pi\) in this interval. Consequently the number of distinct cycles is exactly \(\binom{m}{m/2}/2\) *within this construction*.

**Step 2: exact spectral stability.** Both orbit points have \(\cos z_i^\pm=-\cos\delta\) for every \(i\), so
\[
DF_{m,h}(z_s^\pm)=I_m-h\cos\delta\,K_m.
\]
The real symmetric matrix \(K_m\) has eigenvalue \(1\) on \(\mathbf1^\perp\), with multiplicity \(m-1\), and eigenvalue \(q=m+1\) on the span of \(\mathbf1\). The derivatives at both orbit points coincide, yielding two-step eigenvalues
\[
\mu_{\mathrm{bal}}=(1-h\cos\delta)^2 \quad (m-1\text{ times}),
\qquad
\mu_{\mathrm{col}}=(1-qh\cos\delta)^2 \quad (1\text{ time}).
\]
For \(0<\delta<\pi/2\), \(h\cos\delta=2\delta\cot\delta\) decreases strictly from \(2\) to \(0\). Thus \(0<\mu_{\mathrm{bal}}<1\) throughout \(2<h<\pi\). The collective factor has modulus below one exactly when \(0<q h\cos\delta<2\), equivalently \(q\delta\cot\delta<1\). The map \(\delta\mapsto q\delta\cot\delta\) decreases strictly from \(q>1\) to zero, giving a unique \(\delta_m\in(0,\pi/2)\) and its threshold \(h_m=H(\delta_m)\in(2,\pi)\). For \(2<h<h_m\), exactly the collective multiplier exceeds one; for \(h_m<h<\pi\), both lie strictly inside the unit circle. The standard contraction argument applied to a sufficiently high iterate of the second-return map proves local exponential attraction. For \(h>\pi\), \(\delta>\pi/2\), so \(h\cos\delta<0\) and every two-step multiplier is greater than one: the cycles are repelling. At \(h=h_m\) and \(h=\pi\) at least one multiplier equals one, so neither boundary is strictly linearly attracting.

**Step 3: sharp large-star window.** Write \(\varepsilon_m=\pi/2-\delta_m\). The threshold equation is
\[
q(\pi/2-\varepsilon_m)\tan\varepsilon_m=1.
\]
As \(q\to\infty\), it forces \(\varepsilon_m=2/(\pi q)+O(q^{-2})\). Therefore
\[
h_m=\frac{\pi-2\varepsilon_m}{\cos\varepsilon_m}
=\pi-\frac4{\pi q}+O(q^{-2}),
\]
as asserted. Stirling's formula gives the displayed exponential count.

**Step 4: robustness under positive weight perturbations.** Let \(A=\operatorname{diag}(a_1,\ldots,a_m)\), with every \(a_i>0\), and consider \(F_{m,h,A}(z)=z+hK_mA\sin z\pmod{2\pi}\). At unit weights and \(h_m<h<\pi\), the derivative of \(F_{m,h,I}^2-\mathrm{id}\) at each \(z_s^+\) has no zero eigenvalue, because all two-step multipliers lie strictly inside the unit disk. In local torus charts, the implicit-function theorem continues each fixed point of the second iterate for all \(A\) sufficiently close to \(I\). Continuity preserves the strict multiplier bounds. Their partner images remain distinct by continuity, hence each continued point belongs to a genuine attracting period-two orbit. Finitely many disjoint small neighborhoods around the unperturbed orbits give one common perturbation radius and preserve their distinctness. This is persistence for each *fixed* \(m,h\), not a uniform radius as \(m\to\infty\).

## Verification

The accompanying Python checker enumerates balanced sign assignments for \(m=4,6,8,10,12\), calculates thresholds numerically, tests both orbit exchanges, and independently checks entries of the one-step Jacobian by finite differences. It obtains respectively \(3,10,35,126,462\) distinct cycles and passes 1,272 orbit tests. The proof above, not the finite computations, establishes the universal statements and weight robustness.

## Relationship to prior work

Buescu, D'Aniello, and Oliveira (2026) derive the intrinsic discrete Huygens graph reduction and prove small-step Morse–Smale criteria. Their original analysis applies explicitly to paths and the three-leaf star, with weights restricted to a small-step regime. Here the same established update is examined on even-leaf stars at \(h>2\), beyond its guaranteed gradient-descent region. The balanced sign eigenspace supports a combinatorially growing family of robust attracting two-cycles; it is distinct from the all-equal synchronized eigendirection and from the small-step fixed-point results. Prior abstract descriptions of the repulsive complete-graph dynamics also involve a different interaction matrix; they do not imply the star-specific collective multiplier or stability window.

## Limitations

This theorem constructs and classifies the stability of one natural, exactly defined family of cycles. It does not exhaust the global periodic-orbit set or assert global attraction. It requires equal unperturbed star-edge weights and even \(m\), though persistence allows sufficiently small positive heterogeneity at a fixed interior parameter. Boundary multiplier equality is not a nonlinear stability classification. Full general historical priority among results on high-step discrete phase maps remains subject to further literature assessment.

## References

Buescu, J.; D'Aniello, E.; Oliveira, H. M. (2026). *Morse–Smale dynamics in discrete Huygens networks*. arXiv:2610.10993v1, publicly submitted 7 October 2026. https://arxiv.org/abs/2610.10993.
