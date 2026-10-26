# Sharp limit-cycle census for a periodic absolute-value equation

## Finding
For each integer \(k\ge2\) there exists \(\varepsilon_k>0\) such that, for every real \(0<|\varepsilon|<\varepsilon_k\), the periodic scalar differential equation
\[
 x'(t)=\sin t+\varepsilon\cos(kt)|x(t)|
\]
has **exactly \(k-2\) limit cycles** on the cylinder with time period \(2\pi\). Every one is hyperbolic. Besides these isolated periodic trajectories there are precisely two half-line families of periodic one-sign solutions, including their grazing endpoints; none of those trajectories is isolated. In particular, the case \(k=2\) has no limit cycles.

The upper bound is global in the initial value, not merely a count of perturbative roots in a compact subinterval. The lower bound was established in the pioneering example of Coll, Gasull and Prohens; the new ingredient is a sharp upper bound on the number of critical points of the full Poincaré map, including control at grazing boundaries.

## Assumptions and scope
The integer \(k\) is fixed before taking the perturbation small; \(\varepsilon_k\) is not asserted to be uniform in \(k\). Solutions are unique and global since the vector field is Lipschitz in \(x\) with at most linear growth. Write \(P_\varepsilon(\rho)=x(2\pi;\rho)\), where \(x(0;\rho)=\rho\). A limit cycle is an isolated fixed point of \(P_\varepsilon\), not an entire periodic family. The argument covers positive and negative nonzero perturbations, all real initial values, and exactly the stated forcing and absolute-value coefficient; it does not assert a formula for arbitrary perturbations or all parameter magnitudes.

## Proof
**1. Two exact boundary families.** Let \(a=\varepsilon/k\). For either sign,
\[
 \int_0^{2\pi} e^{\pm a\sin(kt)}\sin t\,dt=0,
 \qquad
 \int_0^\pi \left(e^{a\sin(kt)}-e^{-a\sin(kt)}\right)\sin t\,dt=0.
\]
The first identity follows by summing translates by \(2\pi/k\). The second follows by expanding \(\sinh(a\sin(kt))\) into its convergent power series: each odd power of \(\sin(kt)\) is a linear combination of sines at positive integer multiples of \(k\), orthogonal to \(\sin t\) on \([0,\pi]\) because \(k\ge2\).

The explicit periodic solution that just touches zero at time \(0\) is
\[
 u_\varepsilon(t)=e^{a\sin(kt)}\int_0^t e^{-a\sin(ks)}\sin s\,ds.
\]
The integral grows strictly on \((0,\pi)\), decreases strictly on \((\pi,2\pi)\), and vanishes at both endpoints, hence \(u_\varepsilon(t)>0\) for \(0<t<2\pi\). Its initial value is \(0\). The analogous solution just touching zero at time \(\pi\) is
\[
 v_\varepsilon(t)=e^{-a\sin(kt)}\int_\pi^t e^{a\sin(ks)}\sin s\,ds.
\]
It is strictly negative off \(\pi\) modulo the period, and has periodic initial value
\[
 c_\varepsilon=-\int_0^\pi e^{a\sin(ks)}\sin s\,ds<0.
\]
The zero-integral identity makes both solutions periodic. Scalar comparison with these solutions implies that **every** \(\rho\ge0\) yields a nonnegative solution of the positive linear branch, whose multiplier and period translation are respectively \(1\) and \(0\); hence \(P_\varepsilon(\rho)=\rho\). Likewise \(P_\varepsilon(\rho)=\rho\) for every \(\rho\le c_\varepsilon\), using the negative linear branch. There are no other one-sign initial values, by comparison with the two grazing solutions.

**2. All remaining trajectories cross twice.** Fix \(\rho\in(c_\varepsilon,0)\). Comparison gives \(x(0;\rho)<0\), \(x(\pi;\rho)>0\), and \(x(2\pi;\rho)<0\). Since at a zero \(x'=\sin t\), there is exactly one upward zero \(t_1\in(0,\pi)\) and exactly one downward zero \(t_2\in(\pi,2\pi)\). Their crossings are transverse. As \(\rho\) increases, the first zero decreases strictly and continuously from \(\pi\) to \(0\); the map \(\rho\mapsto t_1\) is an interior smooth bijection.

On the positive part of the trajectory, the integrating factor gives
\[
 \int_{t_1}^{t_2}e^{-a\sin(ks)}\sin s\,ds=0.
\]
Introduce the strictly increasing functions on \([0,\pi]\),
\[
 A_\varepsilon(t)=\int_0^t e^{-a\sin(ks)}\sin s\,ds,\qquad
 B_\varepsilon(t)=\int_0^t e^{a\sin(ks)}\sin s\,ds.
\]
By step 1 they have the same value at \(\pi\). The substitution \(t_2=2\pi-r\) transforms the positive-segment equality into \(A_\varepsilon(t_1)=B_\varepsilon(r)\). Hence
\[
 t_2=2\pi-r_\varepsilon(t_1),\qquad
 r_\varepsilon=B_\varepsilon^{-1}\circ A_\varepsilon:[0,\pi]\longrightarrow[0,\pi].
\]
This is an increasing homeomorphism fixing the endpoints, smooth on the interior.

**3. Endpoint-controlled critical-point census.** In fact,
\[
 r_\varepsilon\longrightarrow\operatorname{id}
 \quad\text{in }C^1([0,\pi])\quad\text{as }\varepsilon\to0.
\]
To justify the endpoint regularity rather than assuming it, for \(t\) near \(0\), factor both increasing primitives into \(t^2\) times a positive smooth function of \((t,\varepsilon)\). Taking their positive square roots gives smooth local coordinates with nonzero derivative at \(0\), so the inverse-composition extends smoothly and depends smoothly on \(\varepsilon\). Near \(\pi\), apply the same argument to the deficits \(A_\varepsilon(\pi)-A_\varepsilon(t)\) and \(B_\varepsilon(\pi)-B_\varepsilon(t)\), factoring \((\pi-t)^2\); equality of the endpoint totals is essential. The interior follows from the inverse function theorem. These three patches prove the claimed \(C^1\) convergence.

Variational differentiation through the two transverse zero crossings yields the exact derivative
\[
 P_\varepsilon'(\rho)
 =\exp\left(\varepsilon\int_0^{2\pi}\cos(kt)\operatorname{sgn}(x(t;\rho))\,dt\right)
 =\exp\left(\frac{2\varepsilon}{k}\bigl[\sin(kt_2)-\sin(kt_1)\bigr]\right).
\]
There is no saltation multiplier because the vector field is continuous at zero. For nonzero \(\varepsilon\), its critical points relative to the identity are exactly the zeros of
\[
 h_\varepsilon(t):=\sin(kt)+\sin(k r_\varepsilon(t)),\qquad 0<t<\pi.
\]
The uniform \(C^1\) limit is \(h_\varepsilon\to2\sin(kt)\). The limiting function has exactly \(k-1\) simple interior zeros \(t=j\pi/k\), for \(j=1,\ldots,k-1\), and simple zeros at \(0\) and \(\pi\). Since \(h_\varepsilon(0)=h_\varepsilon(\pi)=0\), its endpoint derivatives remain bounded away from zero, preventing nearby extra roots. Around each simple interior zero the derivative retains a fixed sign; on the complementary compact set the function stays away from zero. Thus for small nonzero \(\varepsilon\), \(P_\varepsilon'(\rho)-1\) has **exactly \(k-1\) zeros** on the entire interval \((c_\varepsilon,0)\).

Set \(F_\varepsilon(\rho)=P_\varepsilon(\rho)-\rho\). We have \(F_\varepsilon(c_\varepsilon)=F_\varepsilon(0)=0\). If there were \(m\) distinct interior fixed points, Rolle's theorem on the \(m+1\) successive intervals between the boundary and interior fixed points would force at least \(m+1\) distinct interior zeros of \(F_\varepsilon'=P_\varepsilon'-1\). Consequently \(m\le k-2\), globally. No one-sign trajectory can be a limit cycle because those trajectories belong to fixed half-lines.

**4. The matching \(k-2\) simple fixed points.** At \(\varepsilon=0\), \(x(t;\rho)=\rho+1-\cos t\). On compact subintervals of \((-2,0)\), the crossings remain transverse and the normalized displacement converges in \(C^1\) to
\[
 M_k(\rho)=\int_0^{2\pi}\cos(kt)|\rho+1-\cos t|\,dt.
\]
Writing \(y=\rho+1\in(-1,1)\), direct trigonometric integration and the Chebyshev polynomial \(T_k(y)=\cos(k\arccos y)\) give
\[
 M_k(\rho)=\frac{4(1-y^2)^{3/2}}{k^2(k^2-1)}T_k''(y).
\]
This formula can be checked by splitting the integral at \(\arccos y\) and \(2\pi-\arccos y\), or using
\[
 M_k(\rho)=\frac{2}{k}\left(\frac{\sin((k-1)\arccos y)}{k-1}-\frac{\sin((k+1)\arccos y)}{k+1}\right).
\]
The polynomial \(T_k'\) has \(k-1\) distinct roots in \((-1,1)\); Rolle's theorem and the degree bound show that \(T_k''\) has exactly \(k-2\) distinct simple roots there (none for \(k=2\)). Each root of \(M_k\) is simple. The implicit-function theorem for the normalized displacement \(F_\varepsilon/\varepsilon\) therefore produces at least \(k-2\) simple fixed points for sufficiently small nonzero \(\varepsilon\), inside \((c_\varepsilon,0)\). These fixed points are hyperbolic since \(P_\varepsilon'\ne1\). Combining with the global upper bound completes the proof.

## Verification
The proof is analytic; no finite enumeration is used to establish an infinite assertion. Independently, quadrature at perturbation \(\varepsilon=0.07\), with 15,001 grid points on \([0,\pi]\), was used to form \(r_\varepsilon\) and count sign changes of \(h_\varepsilon\). For each \(2\le k\le8\), the observed interior counts were exactly \(k-1\), agreeing with the proven small-perturbation critical-point formula. A separate quadrature check for \(2\le k\le5\) at several \(y\)-values verified the Chebyshev integral identity to approximately \(10^{-15}\). These numerical checks are illustrative only: a finite grid cannot rule out additional roots, and the analytic endpoint and monotonicity arguments are decisive.

## Relationship to prior work
Coll, Gasull and Prohens (2008) established at least \(k-2\) limit cycles for this specific perturbative example and showed the first-order displacement has exactly \(k-2\) simple interior zeros. Their count does not in itself exclude additional finite-perturbation cycles approaching the two grazing endpoints. Bravo and Trinidad-Forte (2025/2026) cite the same family as providing a lower bound on cycle multiplicity while treating global-center and broad finiteness questions. Their 2026 finiteness preprint proves a general, much larger degree-dependent bound, not the present sharp count. The present proof adds an exact phase-matching correspondence and sharp \(k-1\)-critical-point bound for the *entire* crossing interval. It is a special-family exact count, not a replacement for general Hilbert-number bounds.

## Limitations
The size of the permitted perturbation may depend strongly on \(k\), and no explicit universal constant is claimed. The result concerns isolated fixed points with forcing period \(2\pi\); it does not classify subharmonic behavior at periods larger than \(2\pi\) for arbitrary initial trajectories. The novelty comparison is based on the cited full texts and searched research records; it is not an exhaustive priority certification. Independent verification has not been performed.

## References
1. B. Coll, A. Gasull, and R. Prohens, “Simple Non-Autonomous Differential Equations with Many Limit Cycles,” *Communications on Applied Nonlinear Analysis* **15** (2008), 29–34. Full author-posted text: https://www.researchgate.net/publication/289115197_Simple_non-autonomous_differential_equations_with_many_limit_cycles.
2. J. L. Bravo and R. Trinidad-Forte, “Global Centers in Piecewise Linear Equations in the Cylinder,” arXiv:2503.03247v1 (5 March 2025); *Qualitative Theory of Dynamical Systems* **25** (2026), article 26. https://arxiv.org/abs/2503.03247.
3. J. L. Bravo and R. Trinidad-Forte, “Finitude of Limit Cycles of Linear Piecewise ODEs in the Cylinder,” arXiv:2605.05805v1 (7 May 2026). https://arxiv.org/abs/2605.05805.
4. J. L. Bravo, M. Fernández, and I. Ojeda, “Hilbert Number for a Family of Piecewise Nonautonomous Equations,” *Qualitative Theory of Dynamical Systems* **23** (2024), article 119. https://doi.org/10.1007/s12346-023-00922-9.
