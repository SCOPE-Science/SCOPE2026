# Sharp Picard solver-cycle threshold for a one-node nonlinear heat step

## Finding

A positivity-preserving nonlinear backward-Euler step can have a nonconvergent *positive* frozen-coefficient inner solver. For a standard one-node centered-flux discretization of quadratic-conductivity heat flow, the exact failure threshold is \(T=4\), with globally attracting nonzero oscillation at larger parameters and universal inverse-square-root critical relaxation at equality. A constant damping weight of at most \(2/3\) restores local stability for every finite stiffness (not asserted globally).

More precisely, with \(T>0\), define \(F_T(z)=1/(1+Tz^2)\), and start at \(z_0=1\). The unique positive root \(s\) of \(s+Ts^3=1\) is the correct normalized backward-Euler state. If \(0<T<4\), then \(z_j\to s\). If \(T=4\), then \(s=1/2\), \(z_j\to s\), and
\[
\lim_{j\to\infty}j(z_j-1/2)^2=\frac12.
\]
If \(T>4\), the subsequences instead converge to
\[
\lim_{j\to\infty}z_{2j}=p_+=\frac{1+\sqrt{1-4/T}}2,\qquad
\lim_{j\to\infty}z_{2j+1}=p_-=\frac{1-\sqrt{1-4/T}}2.
\]
They form the sole positive prime two-cycle, with the exact two-step multiplier \(4/T<1\), and neither is the implicit solution. The onset gap is \(p_+-p_-=\sqrt{1-4/T}\).

## Assumptions and scope

For spatial mesh size \(h>0\), take the one-dimensional quadratic-conductivity heat equation \(u_t=\partial_x(u^2u_x)\) on \([0,2h]\), with fixed zero boundary values at the endpoints and one interior unknown \(y(t)\) at \(x=h\). Define each interface conductivity as the square of the arithmetic average of its adjacent nodal values. Apply the standard centered finite-volume divergence of fluxes. Both boundary nodal values are zero, so the resulting ODE is exactly
\[
\dot y=-\frac{y^3}{2h^2}.
\]
For a backward-Euler step of size \(\tau>0\) from \(b>0\), the exact next value solves \(y+\tau y^3/(2h^2)=b\) and lies in \((0,b)\). The linear-solve Picard iteration freezes the diffusion coefficient at its preceding iterate:
\[
y^{(j+1)}=\frac{b}{1+\tau(y^{(j)})^2/(2h^2)},\qquad y^{(0)}=b.
\]
The dimensionless variables \(z_j=y^{(j)}/b\) and \(T=\tau b^2/(2h^2)\) yield the stated map. We consider exact arithmetic and convergence in the nonlinear inner-iteration index \(j\), not refinement of the physical timestep.

## Proof

**Discretization and implicit state.** At the right interface the centered flux is \(-y^3/(4h)\), and at the left it is \(+y^3/(4h)\); dividing their difference by \(h\) gives \(-y^3/(2h^2)\). The strictly increasing function \(s\mapsto s+Ts^3\) crosses \(1\) exactly once on \((0,1)\).

**Two-step factorization.** Direct rational simplification, valid for every \(z>0\) and \(T>0\), yields
\[
F_T(F_T(z))-z=-\frac{(Tz^2-Tz+1)(Tz^3+z-1)}{T^2z^4+2Tz^2+T+1}.
\]
The cubic \(Tz^3+z-1\) is strictly increasing and vanishes exactly at \(s\). The quadratic \(Tz^2-Tz+1\) is positive for all real \(z\) if \(T<4\), a perfect square at \(T=4\), and has precisely the two roots \(p_-<p_+\) given above if \(T>4\). In the last case, \(p_-<s<p_+\): using \(p_-+p_+=1\) and \(Tp_-p_+=1\) gives \(F_T(p_-)=p_+\) and vice versa; their order about \(s\) follows from strict decrease of \(F_T\).

Since \(F_T\) is strictly decreasing, \(F_T^2\) is continuous and increasing. Every even subsequence is monotone after its initial step, remains in a compact interval bounded by fixed points of \(F_T^2\), and converges to one such fixed point. The sign of the factored displacement shows convergence to \(s\) for \(T\le4\). For \(T>4\), initial state \(z_0=1>p_+\) decreases under \(F_T^2\) toward \(p_+\), while odd iterates tend to \(F_T(p_+)=p_-\). These signs also show every positive initial state other than \(s\) is attracted to the same cycle, with parity determined by its side of \(s\). No other prime two-cycle exists, because the factorization lists all fixed points of \(F_T^2\).

**Sharp multiplier and critical law.** Along the two-cycle, \(F'_T(z)=-2Tz/(1+Tz^2)^2\) and \(Tp_-p_+=1\); substitution yields \(F'_T(p_-)F'_T(p_+)=4/T\). At \(T=4\), expanding around \(s=1/2\), with \(v=z-1/2\), gives
\[
F_4^2(1/2+v)-1/2=v-2v^3+O(v^4).
\]
For a nonfixed positive initial state, the even deviations keep one sign and approach zero. Their reciprocal squares therefore satisfy \(v_{2(j+1)}^{-2}-v_{2j}^{-2}=4+o(1)\). Stolz averaging gives \(jv_{2j}^2\to1/4\). Because \(F'_4(1/2)=-1\), the same limit in the original index is \(j(z_j-1/2)^2\to1/2\).

**Damping.** For \(0<\omega\le1\), let \(G_{T,\omega}(z)=(1-\omega)z+\omega F_T(z)\). It has the same unique fixed point \(s\). Since \(Ts^3=1-s\), differentiation gives
\[
G'_{T,\omega}(s)=1-\omega(3-2s).
\]
The strict local linear stability inequality \(|G'_{T,\omega}(s)|<1\) is equivalent to \(0<\omega<2/(3-2s)\). Since \(s\in(0,1)\), every fixed \(0<\omega\le2/3\) satisfies it for all finite \(T\). For every \(\omega>2/3\) up to \(1\), choosing \(T\) sufficiently large makes \(s\to0\) and violates it. Thus \(2/3\) is the sharp stiffness-uniform local linear stability ceiling. This does not imply a uniform convergence rate or global damping convergence.

## Verification

The accompanying standalone `verify.py` checks the exact symbolic factorization and critical Taylor expansion, exact rational two-cycle identities, exact multiplier identity, and numerical trajectories across and near the threshold. The analytical proof, not finite numerical tests, establishes the universal statements.

## Relationship to prior work

Botchev's 2026 study formulates quadratic-conductivity nonlinear heat flow and the frozen-coefficient nonlinear solver in equations (6), (7), and (10). Its principal contribution compares time-integration strategies; the exact one-node solver map, its global cycle classification, its critical limit, and the stiffness-uniform local damping ceiling are not stated there. Classical Picard fixed-point theory provides local sufficient convergence criteria, and general order-reversing-map dynamics can predict equilibrium/period-two alternatives. Neither general observation alone supplies the complete coefficients and exact threshold for this explicitly discretized nonlinear heat step. General rational-map theory could contain an equivalent normalized recurrence; this remains an originality risk.

## Limitations

Only one interior spatial degree of freedom, the specified arithmetic-interface-conductivity flux discretization, zero Dirichlet data, positive previous-time state, fixed timestep and exact arithmetic are covered. The source's higher-dimensional code need not employ precisely this face-conductivity convention. The damping conclusion is local, not global; the theorem concerns nonlinear solver convergence, not the stability of an exactly solved backward-Euler time step. Independent scientific validation has not been performed.

## References

1. M. A. Botchev, *Are implicit schemes needed in adaptive time stepping for PDEs?*, arXiv:2610.14884v1 (first posted 10 October 2026), section 4, equations (6), (7), (10). https://arxiv.org/html/2610.14884v1
2. E. Camouzis and G. Ladas, *Dynamics of Third-Order Rational Difference Equations with Open Problems and Conjectures*, CRC Press (2007), broad background on rational recurrences; not asserted to cover this map.
