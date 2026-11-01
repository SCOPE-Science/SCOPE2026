# Sharp forward-completeness and two-coordinate escape laws for polynomial Liénard oscillators

## Finding

Consider the classical polynomial Liénard plane flow
\[
\dot x=y-F(x),\qquad \dot y=-x,
\]
where \(F\) is an arbitrary real polynomial. The following classification holds without coefficient restrictions beyond those stated:

**(A) Sharp completeness dichotomy.** Every real initial state has a solution on the full interval \([0,\infty)\) if and only if either \(\deg F\le1\) (including the zero polynomial), or \(\deg F=m\ge3\) is odd and its leading coefficient is positive. For every other polynomial, namely even degree \(m\ge2\) with either leading sign or odd degree \(m\ge3\) with negative leading coefficient, there is a nonempty open set of initial states with finite forward escape time.

**(B) Quantitative sector law.** In each incomplete case choose \(\sigma\in\{-1,+1\}\) such that
\[
P(z):=-\sigma F(\sigma z)=az^m+bz^{m-1}+O(z^{m-2}),\qquad a>0.
\]
There exists \(R>0\) such that every initial state in the interior of
\[
\mathcal S_R=\{z\ge R,\ -z\le v\le z\},\qquad z=\sigma x,\quad v=\sigma y,
\]
escapes at a finite forward time \(T\), with \(z(t)\to+\infty\). With
\[
Z(t)=[a(m-1)(T-t)]^{-1/(m-1)},
\]
all such solutions obey the **two-term time-domain expansion**
\[
\boxed{z(t)=Z(t)-\frac{b}{am}+o(1).}
\]
In the quadratic case \(m=2\), there exists a finite, initial-state-dependent \(C\) such that
\[
\boxed{v(t)+\frac1a\log z(t)\longrightarrow C},\qquad v(t)\to-\infty.
\]
For every \(m\ge3\), there is instead a finite \(v_\infty\) such that
\[
\boxed{v(t)\longrightarrow v_\infty,\qquad
v(t)-v_\infty\sim\frac{z(t)^{2-m}}{a(m-2)}.}
\]
Thus the secondary coordinate switches sharply from **logarithmic divergence in degree two** to **finite limiting memory in every higher escaping degree**.

**(C) The sextic family in the motivating literature.** For every real \(\alpha\), let
\[
F(x)=\alpha x+x^3+x^6.
\]
Its left-escape sector has \(z=-x\), \(v=-y\), \(P(z)=z^6-z^3-\alpha z\). Write \(Z(t)=[5(T-t)]^{-1/5}\). Then
\[
\boxed{x(t)=-Z(t)-\tfrac18 Z(t)^{-2}-\tfrac{\alpha}{10}Z(t)^{-4}+O(Z(t)^{-5}),}
\]
\[
\boxed{y(t)\to y_\infty\in\mathbb R,\qquad y_\infty-y(t)\sim\tfrac14 Z(t)^{-4}.}
\]
Here the sextic's lower-order cubic and linear terms are individually visible in the sharp escape-time expansion. None of these assertions counts its periodic orbits.

## Assumptions and scope

The initial state is arbitrary in \(\mathbb R^2\) for completeness, and belongs to the explicitly constructed open sector \(z>R\), \(|v|<z\) for the quantitative escape law. The coefficients are arbitrary real numbers, \(m\ge2\) is the precise polynomial degree, \(a\) and \(b\) are the first two coefficients of the **oriented** polynomial \(P\), and \(T\) is the finite maximal forward existence time. The notation \(\sim\) denotes a ratio tending to one, and the remainder constants can depend on the polynomial and initial state. No statement about the entire basin of finite-time escape is made.

## Proof

**1. Complete systems.** If \(F\) is constant or affine, the vector field is affine and all its solutions are global. Otherwise define \(E=(x^2+y^2)/2\). Direct differentiation gives
\[
\dot E=x(y-F(x))+y(-x)=-xF(x).
\]
If the exact degree \(m\ge3\) is odd with positive leading coefficient, then \(-xF(x)\to-\infty\) as \(x\to\pm\infty\). Hence \(\dot E\le C\) globally for some finite real \(C\). It follows that \(E(t)\le E(0)+Ct\) on every bounded forward interval. The standard continuation theorem for locally Lipschitz polynomial vector fields excludes finite-time escape.

**2. The escaping sectors.** In the remaining cases \(m\ge2\), select \(\sigma\in\{\pm1\}\) satisfying \(a=-c\sigma^{m+1}>0\), where \(c\) is the leading coefficient of \(F\). This is always possible for even \(m\), and for odd \(m\) exactly when \(c<0\). Then
\[
\dot z=P(z)+v,\qquad\dot v=-z.
\]
For sufficiently large \(R\), \(P(z)>2z\) and \(P(z)-z\ge(a/2)z^m\) whenever \(z\ge R\). On the right boundary \(v=z\), \((v-z)'=-P(z)-2z<0\); on the left boundary \(v=-z\), \((v+z)'=P(z)-2z>0\); and on \(z=R\), \(\dot z\ge P(R)-R>0\). Therefore \(\mathcal S_R\) is forward invariant for as long as the solution exists, and
\[
\dot z\ge (a/2)z^m>0.
\]
Comparison with the scalar power law shows that the maximal forward time is finite. Since the entire trajectory stays inside \(\mathcal S_R\) and its strictly increasing \(z\) cannot remain bounded at a maximal finite time, necessarily \(z(t)\to+\infty\). The strict inequalities give a nonempty open escaping sector.

**3. The second coordinate.** Reparameterize by the monotonically increasing \(z\):
\[
\frac{dv}{dz}=-\frac{z}{P(z)+v}.
\]
Throughout the sector \(|v|\le z\), the denominator equals \(az^m(1+O(z^{-1}))\), uniformly for all its trajectories. Thus
\[
\frac{dv}{dz}=-\frac1a z^{1-m}(1+O(z^{-1})).
\]
For \(m=2\), integration gives \(v(z)=-(1/a)\log z+O(1)\). Substituting this estimate back improves the derivative to \(dv/dz=-(az)^{-1}+O(z^{-2})\); integration of the integrable residual proves the finite limit \(v+(1/a)\log z\to C\). For \(m\ge3\), the derivative is integrable at infinity, so \(v\to v_\infty\), and integration from \(z\) to infinity gives the displayed positive tail \(v-v_\infty=z^{2-m}/[a(m-2)](1+o(1))\). In particular, \(v=o(z)\) in all degrees.

**4. The original-time two-term expansion.** Since \(v=O(\log z)\) for \(m=2\) and \(v=O(1)\) for \(m\ge3\), the exact remaining time is
\[
T-t=\int_{z(t)}^\infty\frac{ds}{P(s)+v(s)}.
\]
With \(P(s)=as^m+bs^{m-1}+O(s^{m-2})\) and the established bounds on \(v(s)\), uniform expansion yields
\[
T-t=\frac{z^{1-m}}{a(m-1)}-\frac{b z^{-m}}{a^2m}+o(z^{-m}).
\]
Asymptotic inversion gives \(z=Z-b/(am)+o(1)\), including the case \(b=0\).

**5. The sextic refinement.** For \(P(z)=z^6-z^3-\alpha z\), the convergent \(v(z)\) satisfies \(v(z)=v_\infty+O(z^{-4})\). Hence
\[
\frac1{P(z)+v(z)}=z^{-6}(1+z^{-3}+\alpha z^{-5}+O(z^{-6})),
\]
so
\[
T-t=\frac1{5z^5}+\frac1{8z^8}+\frac{\alpha}{10z^{10}}+O(z^{-11}).
\]
Substitution of \(z=Z+(1/8)Z^{-2}+(\alpha/10)Z^{-4}+O(Z^{-5})\) into this relation verifies the inversion (the omitted nonlinear products first contribute at the stated remainder order). Finally, \(v(z)-v_\infty\sim z^{-4}/4\) and \(y=-v\), giving \(y_\infty-y\sim Z^{-4}/4\).

## Verification

The standalone `verify.py` reconstructs the oriented sector boundary inequalities for several degrees, checks the universal coefficient on the exact scalar example \(\dot z=(z+1)^m\), symbolically expands the sextic reciprocal field and inverts its flight-time series, and numerically integrates the **exact** orbit-graph equation for degrees \(2,3,6\) to test the logarithmic and finite-limit regimes. Its execution completed successfully. These finite and symbolic diagnostics support, but do not substitute for, the preceding general proof.

## Relationship to prior work

Cao, Chen and Tang (2026, arXiv:2610.30417), which first appeared publicly on October 21, 2026, studies upper bounds and uniqueness for periodic Liénard orbits, explicitly **without assuming completeness**, and identifies the sextic polynomial \(F=\alpha x+x^3+x^6\) as outside its common-sign criteria. Its statements neither classify global continuation nor assert the physical-time escape expansions here.

Dumortier and Herssens (1999) classify qualitative dynamics near infinity in polynomial Liénard systems. Luca and Dumortier (2009) study bounded and unbounded limit periodic sets. Both are essential context: a topological infinity portrait is not itself a precise original-time blow-up law, and neither inspected material supplies the stated quadratic logarithmic/finite-limit transition or the sextic coefficient expansion. The full text of the 1999 work remained inaccessible, so overlap risk is explicitly retained. The earlier known qualitative infinity classification is not claimed as new.

## Limitations

The escaping sectors are sufficient domains, not an exhaustive description of escaping initial states. Forward completeness does not imply boundedness as time tends to infinity. The theorem concerns the restoring law \(g(x)=x\), not arbitrary nonlinear restoring forces. The 1999 classification and other specialized references may contain related asymptotic consequences not verifiable from the accessible material; priority requires independent review. The original source's open sextic **limit-cycle counting** problem is not solved by this result.

## References

1. C. Cao, H. Chen, Y. Tang, *New criteria for upper bounds on the number of limit cycles in Liénard systems*, arXiv:2610.30417, first submitted 2026-10-21; version 2 dated 2026-10-23. https://arxiv.org/abs/2610.30417
2. F. Dumortier and C. Herssens, *Polynomial Liénard equations near infinity*, Journal of Differential Equations 153 (1999), 1–29. https://doi.org/10.1006/jdeq.1998.3543
3. S. Luca and F. Dumortier, *Limit periodic sets in polynomial Liénard equations*, Qualitative Theory of Dynamical Systems 7 (2009), 339–366. https://doi.org/10.1007/s12346-008-0019-9
