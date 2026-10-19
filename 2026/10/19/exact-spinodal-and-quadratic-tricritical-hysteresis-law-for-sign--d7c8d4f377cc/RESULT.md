# Exact spinodal and quadratic tricritical hysteresis law for signed six-neighbor voting

## Finding

Consider the signed six-neighbor mean-field opinion equation defined below. Put \(b=1-2r\), with antagonistic-link fraction \(0\le r\le1\), and for \(0<p<1\) let \(p\) be the independent-opinion update probability. Define
\[
A_b(z)=6b-1+5b^2(4b-3)z+3b^4(2b-5)z^2-b^6z^3.
\]
For \(0\le r<1/8\), let
\[
z_s(r)=\frac{2b-5+\sqrt{(2b-5)^2+\frac53(4b-3)}}{b^2},\qquad
p_0(r)=\frac{6b-1}{6b+31},\qquad
p_s(r)=\frac{A_b(z_s(r))}{32+A_b(z_s(r))}.
\]
Then \(0<z_s(r)<1\) and \(0<p_0(r)<p_s(r)<1\). The complete physical-equilibrium diagram has three equilibria for \(0<p\le p_0\) (the two nonzero equilibria attracting and the center repelling, with cubic repulsion at equality); five equilibria for \(p_0<p<p_s\) (three attracting, two repelling); three equilibria at \(p=p_s\) (the attracting center and two nonhyperbolic, nondegenerate fold equilibria); and only the attracting center for \(p>p_s\). At \(r=0\),
\[
p_0(0)=\frac5{37},\qquad p_s(0)=\frac{74-24\sqrt6}{101}.
\]

At the previously known tricritical location \((r,p)=(1/8,7/71)\), the quadratic hysteresis-width law is sharp. Writing \(\delta=1/8-r\downarrow0\),
\[
 z_s(r)=\frac{640}{189}\delta+O(\delta^2),\qquad
 p_s(r)-p_0(r)=\frac{102400}{105861}\delta^2+O(\delta^3).
\]
The nonzero fold magnetizations therefore satisfy
\[
 |m_s(r)|=\sqrt{\frac{640}{189}}\,\delta^{1/2}+O(\delta^{3/2}).
\]
At the tricritical point every nonzero physical solution obeys the exact long-time amplitude
\[
\lim_{t\to\infty}t^{1/4}|m(t)|=\left(\frac{4544}{1701}\right)^{1/4}.
\]
This is a result for the specified deterministic mean-field ODE, not an exact result for the finite random-network stochastic process.

For completeness, when \(1/8<r<5/12\) the transition is continuous at the previously known \(p_0(r)\): two attracting nonzero equilibria exist for \(p<p_0\), only the attracting center for \(p>p_0\), and at equality the center is the only equilibrium and attracts nonzero data with the sharp ordinary critical law
\[
\lim_{t\to\infty}t^{1/2}|m(t)|=\left(\frac{6b+31}{10b^2(3-4b)}\right)^{1/2}.
\]
When \(r\ge5/12\), for every \(0<p<1\) the center is the unique globally attracting equilibrium. At \(r=1/8\), the center is similarly the unique equilibrium for \(p\ge7/71\); for \(p<7/71\), two attracting nonzero equilibria coexist with a repelling center.

## Assumptions and scope

The order parameter is \(m=2c-1\in[-1,1]\), where \(c\) is the positive-opinion fraction. An up-opinion agent regards a random neighbor as mismatched with probability \(1-\xi\), and a down-opinion agent with probability \(\xi\), where \(\xi=r+(1-2r)c=(1+bm)/2\). With probability \(1-p\), an agent flips if all six independently sampled interactions are mismatched; with probability \(p\), it selects a fair random opinion. These are the signed homogeneous mean-field assumptions of Krawiecki and Gradowski (2023), as distinguished from their finite-degree stochastic and pair-approximation models.

For every \(r\in[0,1]\), every \(p\in(0,1)\), and every initial \(m(0)\in[-1,1]\), the ODE is
\[
\dot c=(1-c)\left((1-p)\xi^6+\frac p2\right)
-c\left((1-p)(1-\xi)^6+\frac p2\right).
\]
Time is measured in the natural rate-equation units. All equilibrium statements refer to \(m\in(-1,1)\); because \(0<p<1\), both physical endpoints have strictly inward drift. Here “attracting” denotes asymptotic stability for the ODE; the saddle-node points at \(p_s\) are semistable, not attracting from both sides.

## Proof

**Exact polynomial.** Inserting \(c=(1+m)/2\) and \(\xi=(1+bm)/2\) gives
\[
\dot m=\frac m{32}\left((1-p)A_b(m^2)-32p\right).
\tag{1}
\]
The expansion is an elementary binomial identity: the coefficients of \(m,m^3,m^5,m^7\) in \(\dot m\) at \(p=0\) are respectively \((6b-1)/32\), \(5b^2(4b-3)/32\), \(3b^4(2b-5)/32\), and \(-b^6/32\). Equation (1) is odd. At \(m=1\), direct substitution yields \(\dot m=-2(1-p)r^6-p<0\); the other endpoint is inward by oddness. Thus \([-1,1]\) is invariant.

**Global equilibrium counting and stability.** Nonzero equilibria correspond exactly to \(z=m^2\in(0,1)\) satisfying
\[
A_b(z)=h(p):=\frac{32p}{1-p}.
\tag{2}
\]
Here \(h\) strictly increases from zero to infinity as \(p\) increases, while \(A_b(1)=-(1-b)^6\le0\). Its derivatives are
\[
A_b'(z)=5b^2(4b-3)+6b^4(2b-5)z-3b^6z^2,\qquad
A_b''(z)=6b^4(2b-5)-6b^6z.
\]
For \(-1\le b\le3/4\), every coefficient of \(A_b'\) on \(z\ge0\) is nonpositive; \(A_b\) is strictly decreasing unless \(b=0\), when it is constant and negative. Its initial height \(A_b(0)=6b-1\) is positive precisely if \(b>1/6\). This proves the claimed continuous-transition and no-ordering regions, including the boundary conditions.

For \(3/4<b\le1\), one has \(A_b'(0)>0\), \(A_b''(z)<0\) for \(z\ge0\), and
\[
A_b'(1)=-b^2\bigl(3(b-1)^4+4(3b^2-2b+3)\bigr)<0.
\]
Therefore \(A_b\) has precisely one maximum in \((0,1)\). Solving the quadratic \(A_b'(z)=0\) yields exactly \(z_s\) as displayed. Since \(A_b(0)>0\) and \(A_b(1)\le0\), line (2) intersects the graph once, twice, tangentially once, or never, in precisely the regimes in the Finding. At a nonzero simple equilibrium the derivative of the vector field is
\[
\left.\frac{d\dot m}{dm}\right|_{m^2=z}=\frac{(1-p)zA_b'(z)}{16}.
\]
Thus the increasing-side intersections repel and the decreasing-side intersections attract. At the center, linear stability is determined by \(p-p_0\), and at equality by the sign of \(5b^2(4b-3)\). At the upper threshold, \(A_b'(z_s)=0\) but \(A_b''(z_s)<0\); moreover, the second \(m\)-derivative of the vector field equals \((1-p)m_s^3 A_b''(z_s)/8\ne0\) at a nonzero fold point and the \(p\)-derivative is \(-m_s(A_b(z_s)+32)/32\ne0\). Each fold is nondegenerate. Global attraction of the sole equilibrium in the one-equilibrium regimes follows from the one-dimensional inward-pointing phase line. The coexistence basins are separated by the two repelling nonzero equilibria.

**Tricritical cusp.** Put \(b=3/4+2\delta\). Direct Taylor expansion gives
\[
A_b'(0)=\frac{45}{2}\delta+O(\delta^2),\qquad
\frac12A_{3/4}''(0)=-\frac{1701}{512}.
\]
Because the derivative of \(A_b'(z)\) with respect to \(z\) is strictly negative at \((b,z)=(3/4,0)\), the implicit-function theorem makes its zero \(z_s\) analytic in \(\delta\) near zero. These coefficients give \(z_s=(640/189)\delta+O(\delta^2)\) and
\[
 A_b(z_s)-A_b(0)=\frac{800}{21}\delta^2+O(\delta^3).
\]
Since \(p=A/(A+32)\) has derivative \(32/(A+32)^2\) and \(A_{3/4}(0)=7/2\), the derivative equals \(128/5041\) at the cusp. Multiplication gives \((800/21)(128/5041)=102400/105861\), proving the claimed sharp hysteresis width. Taking a square root gives the magnetization law. At \(b=1\) the derivative root is \(z_s=-3+4\sqrt6/3\) and substitution into \(p_s\) gives the displayed exact benchmark.

**Critical slowing.** At \((b,p)=(3/4,7/71)\), (1) simplifies exactly to
\[
\dot m=-\frac{243}{145408}m^5(56+3m^2).
\tag{3}
\]
Every nonzero solution retains its sign and converges monotonically to zero. Its inverse fourth power obeys
\[
\frac{d}{dt}|m|^{-4}=\frac{1701}{4544}+\frac{729}{36352}m^2
=\frac{1701}{4544}+o(1).
\]
Taking time averages shows \(|m(t)|^{-4}/t\to1701/4544\), hence the asserted fourth-root limit. For \(1/8<r<5/12\) at \(p=p_0\), the leading nonlinear drift is \(-\kappa_3m^3\), where \(\kappa_3=5b^2(3-4b)/(6b+31)>0\). The same inverse-power argument gives \(t^{1/2}|m(t)|\to(2\kappa_3)^{-1/2}\), proving the ordinary critical law.

## Verification

The accompanying `verify.py` independently expands the six-neighbor flip probabilities and compares them to (1) at exact rational sample points. It verifies the physical boundary identity, tricritical polynomial, cusp coefficients, derivative signs, and the closed-form zero-antagonism threshold, and supplies rational-parameter numerical consistency checks. Run `python3 verify.py` using Python 3 and the standard library; this produces `VERIFIED 582 assertions`. The infinite-time amplitude and full parameter classification follow from the preceding analytical arguments, not from numerical samples. Verification samples are finite consistency checks, not exhaustive sweeps of the continuous parameter domain.

## Relationship to prior work

Krawiecki and Gradowski (2023, arXiv:2309.06510, Sec. III.A, Eqs. (3)–(12)) introduced the signed \(q\)-voter mean-field equation, derived its implicit fixed-point parametrization and the general tricritical coordinates, and described hysteresis qualitatively. In particular, \(r=1/8\) and \(p=7/71\) for \(q=6\) follow from their results and are not claimed here as new. They stated that the off-center maxima defining the upper spinodal were evaluated numerically. The extension here is an exact radical upper spinodal for the first discontinuous influence-group size, a global equilibrium count with fold nondegeneracy, explicit sharp quadratic collapse of the hysteresis interval, and exact deterministic relaxation amplitudes.

Krawiecki and Gradowski (2024, arXiv:2402.16064) studied approximate master equations and finite-degree simulation comparisons, rather than closed-form fold and cusp amplitudes for the homogeneous mean-field ODE. Earlier work on nonlinear voter models establishes general first-order/continuous-transition and Landau-type behavior but does not supply the signed six-neighbor constants in this result. The source's implicit fixed-point equation determines the exact thresholds in principle; no claim is made that the phenomenon of hysteresis or the tricritical *location* is new.

## Limitations

The result is exact only for this scalar homogeneous signed mean-field rate equation. It does not prove finite-population stochastic or quenched-network transitions, spin-glass transitions, nor quantitative agreement with finite-degree pair or master-equation approximations. The exponent \(1/4\) is characteristic of a fifth-order normal-form critical drift; novelty is claimed for the exact coefficient and full model-specific phase and cusp laws, not for that general exponent. Priority risk remains that a broader analytical treatment not found in the inspected literature may already imply the explicit model-specific formulas. Independent scientific auditing has not been performed.

## References

1. A. Krawiecki and T. Gradowski, *Q-voter model with independence on signed random graphs: homogeneous approximations*, arXiv:2309.06510v1 (first public 2023-09-12), subsequently Physical Review E 109, 014302 (2024). https://arxiv.org/abs/2309.06510
2. A. Krawiecki and T. Gradowski, *Q-voter model with independence on signed random graphs: approximate master equations*, arXiv:2402.16064v1 (2024-02-25). https://arxiv.org/abs/2402.16064
3. A. Abramiuk, J. Pawłowski, and K. Sznajd-Weron, *Is Independence Necessary for a Discontinuous Phase Transition within the q-Voter Model?*, Entropy 21, 521 (2019), doi:10.3390/e21050521. Different anticonformity mechanism; included for general hysteresis/normal-form context.
