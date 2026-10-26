# Two-parameter Floquet rigidity and a sharp two-cycle sink window in a three-dimensional quadratic map

## Finding
Consider the real polynomial map
\[
F(x,y,z)=(a_1x+a_2y+a_3y^2,\;b_1-b_2z,\;cx),
\]
where \(a_3b_2c\ne0\). Define \(A=a_1\), \(d=b_2c\), \(Q=a_3d^2\), \(L=A-a_2d-2a_3b_1d\), \(K=a_2b_1+a_3b_1^2\), and the discriminant
\[
\Delta=(L+1)(L-3)-4QK.
\]
There is exactly one primitive real two-cycle, up to interchanging its two points, if \(\Delta>0\), and no primitive real two-cycle if \(\Delta\le0\). Whenever the cycle exists, its three multipliers, counted with algebraic multiplicity, are the roots of the **universal** cubic
\[
P_{A,\Delta}(t)=t^3-A^2t^2+2A(A+1)t+\Delta-(A+1)^2.
\]
In particular, no other parameter combinations enter its two-step Floquet spectrum.

The unique primitive two-cycle is a **hyperbolic sink** if and only if all three strict inequalities hold:
\[
\big|\Delta-(A+1)^2\big|<1,\qquad
\Delta<4A^2+4A+2,
\]
\[
J(A,\Delta):=-\Delta^2+(A^2+4A+2)\Delta-A(A+2)(2A+3)>0.
\]
Here \(\Delta>0\) is part of the existence hypothesis.

Let \(\eta\) be the unique root in \((0,1)\) of
\[
R(A)=A^4-8A^2-8A+4,
\qquad\eta\approx0.367338467842015.
\]
**Sharp feasibility theorem:** for a prescribed real value of \(a_1=A\), there exist real choices of the other five coefficients with \(a_3b_2c\ne0\) such that the map has a hyperbolic attracting primitive two-cycle **if and only if**
\[
-\frac32<A<\eta.
\]
Both endpoints are excluded. This is an existence statement for freely varying other coefficients, not a stability assertion for every choice of them.

## Assumptions and scope
All six coefficients are real and \(a_3b_2c\ne0\); neither positivity nor invertibility is assumed. A two-cycle consists of two distinct points interchanged by \(F\). A hyperbolic sink means every eigenvalue of the return derivative \(D(F^2)\) has modulus strictly below one. The real numbers \(A,Q,L,K,\Delta\) are defined in the preceding section; \(Q\ne0\) under the assumptions. No claims are made for the degenerate affine cases \(a_3b_2c=0\).

## Proof
**1. Reduction to a scalar quadratic.** On a two-periodic orbit write the first coordinates at alternating times as \(u\) and \(v\). The last two coordinates are forced: at an instant with first coordinate \(u\), they are \((y,z)=(b_1-du,cv)\). Hence \(v=\phi(u)\) and \(u=\phi(v)\) for
\[
\phi(s)=Qs^2+Ls+K.
\]
Conversely every real two-cycle \(u\ne v\) of \(\phi\) lifts to precisely one two-cycle of \(F\) with states \((u,b_1-du,cv)\) and \((v,b_1-dv,cu)\). Polynomial division gives the exact identity
\[
\phi(\phi(s))-s=(\phi(s)-s)
\big(Q^2s^2+Q(L+1)s+L+1+QK\big).
\]
The second factor has discriminant \(Q^2\Delta\). Its two roots are distinct exactly when \(\Delta>0\). Their sum and product are \(-(L+1)/Q\) and \((L+1+QK)/Q^2\). Substituting in \(\phi(s)-s\) shows neither is fixed when \(\Delta>0\): indeed the values of \(\phi(s)-s\) at those two roots are \(\mp\sqrt{\Delta}/Q\), both nonzero. [An alternative argument: both roots must be paired by \(\phi\) since a non-fixed root of \(\phi\circ\phi-s\) has orbit length exactly two; at \(\Delta=0\) the doubled root equals a fixed point.] Thus the two distinct roots form the only primitive two-cycle. When \(\Delta\le0\), there are no two distinct real cofactor roots. For \(\Delta=0\), the double root \(-(L+1)/(2Q)\) satisfies \(\phi(s)=s\), so no primitive orbit exists.

**2. Universal monodromy.** Put \(g_u=a_2+2a_3(b_1-du)\), and similarly define \(g_v\). At either state the one-step Jacobian is
\[
J_w=\begin{pmatrix}A&g_w&0\\0&0&-b_2\\c&0&0\end{pmatrix}.
\]
Direct multiplication yields
\[
\det(tI-J_vJ_u)=t^3-A^2t^2+A d(g_u+g_v)t-d^2g_ug_v.
\]
As \(\phi'(w)=A-dg_w\), the scalar two-cycle identities give
\[
\phi'(u)+\phi'(v)=-2,
\quad \phi'(u)\phi'(v)=1-\Delta.
\]
It follows that \(d(g_u+g_v)=2(A+1)\) and \(d^2g_ug_v=(A+1)^2-\Delta\). Inserting these equalities proves the stated cubic. Multiplication in reverse order gives the same characteristic polynomial at the other point.

**3. Complete sink criterion.** For a real monic cubic \(t^3+e_1t^2+e_2t+e_3\), the strict Schur/Jury criterion is
\[
|e_3|<1,\quad 1+e_1+e_2+e_3>0,\quad
1-e_1+e_2-e_3>0,\quad
1-e_2+e_1e_3-e_3^2>0.
\]
For completeness, applying the Schur reduction produces the quadratic with coefficients \(1-e_3^2,\ e_1-e_2e_3,\ e_2-e_1e_3\); its unit-disc quadratic conditions reduce to the displayed four inequalities. For the stated cubic, its values at \(+1\) and \(-1\) are \(P(1)=\Delta\) and \(-P(-1)=4A^2+4A+2-\Delta\). The final quadratic expression is precisely \(J(A,\Delta)\). Since existence already requires \(\Delta>0\), the criterion reduces to the three displayed strict sink inequalities.

**4. Sharp exclusion in the coefficient \(A\).** If three multipliers are in the open unit disk, their real sum has magnitude strictly less than \(3\); by the cubic this sum is \(A^2\). Thus \(|A|<\sqrt3\) is necessary. For \(-\sqrt3<A\le-3/2\), one has \(J(A,0)=-A(A+2)(2A+3)\le0\), and \(\partial_\Delta J(A,0)=A^2+4A+2<0\). As \(J\) is strictly concave as a function of \(\Delta\), it is negative for every \(\Delta>0\), excluding sinks. On the nonnegative half-line the maximum of \(J(A,\Delta)\) over real \(\Delta\) is attained at
\[
\Delta_v=(A^2+4A+2)/2,
\qquad J(A,\Delta_v)=R(A)/4.
\]
Moreover \(R(0)=4\), \(R(1)=-11\), and \(R'(A)=4A^3-16A-8<0\) throughout \(0\le A\le\sqrt3\). Thus \(R\) has exactly one positive root \(\eta\) on \([0,\sqrt3]\), lying in \((0,1)\), and \(J\le0\) for every \(\Delta\) if \(\eta\le A<\sqrt3\). Together with the trace obstruction this excludes all \(A\notin(-3/2,\eta)\).

**5. Existence throughout the open window.** When \(-3/2<A<0\), at \(\Delta=0\) all the strict Jury inequalities except the separate existence requirement already hold: \((A+1)^2<1\), \(4A^2+4A+2>0\), and \(J(A,0)>0\). Hence a sufficiently small positive \(\Delta\) satisfies every inequality. At \(A=0\), any \(0<\Delta<2\) works. For \(0<A<\eta\), choose \(\Delta=\Delta_v\). Then \(J=R(A)/4>0\), the constant coefficient is \(-A^2/2\), with modulus below one, and \(4A^2+4A+2-\Delta_v>0\). Finally, every prescribed real \(A\) and \(\Delta>0\) can be realized: take \(a_3=b_2=c=1\), \(b_1=0\), \(L=1-\sqrt{4+\Delta}\), and \(a_2=A-L\). This gives \(Q=1\), \(K=0\) and precisely the required discriminant. Therefore all and only the stated \(A\) admit a sink.

For an explicit rational witness, the coefficients \((a_1,a_2,a_3,b_1,b_2,c)=(1/4,3/2,1,0,1,1)\) give \(\Delta=17/16\), \(J=5/32\), and a stable two-cycle with first coordinates \((1\pm\sqrt{17})/8\).

## Verification
The standalone file `check.py` checks the scalar composition factorization, cofactor discriminant, matrix product characteristic polynomial, Schur inequalities, optimization polynomial and exact rational witness symbolically. It also compares the derived Jury test against direct numerical roots for 3,000 independently sampled parameter pairs and tests representative points inside/outside the sharp interval. Execute from the extracted package with `python check.py` using SymPy and NumPy. The analytical proof above, not the finite checks, establishes the full real-parameter theorem.

## Relationship to prior work
Ren, Zhou and Liu (2017) introduced the period-two fixed-point equation for the same map, recorded its quartic implicit form and two-iterate Jacobian, and numerically studied stabilization via a transformed map. Existence of period-two points and their generic Jacobian are therefore **not** claimed as novel here. Muni (2024), arXiv:2406.08317v1, studied period-doubling, unstable periodic orbits and hyperchaos for the same polynomial family. The new claim is the all-real-parameter **two-combination Floquet reduction**, exact **necessary-and-sufficient** sink test and the sharp projection of the sink region onto the \(a_1\)-axis. Published studies of torus doubling and polynomial perturbations concern different statements. Searches of the available mathematical findings index and the inspected primary texts did not identify an implication covering these three conclusions; this is not proof of historical uniqueness.

## Limitations
This does not classify fixed points, higher-periodic orbits, global basins, or degenerate cases where \(a_3b_2c=0\). The sharp coefficient window asserts realizability with the remaining coefficients free, not persistence for every parameter choice. The relevant 2024 torus-doubling journal article was not obtainable in full under the available access, leaving an unresolved priority risk; a statement from its unread full text is not asserted absent.

## References
1. J. Zhou, C. Liu and C. Ren, *Chaos control of a multi-dimensional chaotic mapping system by modified stability transformation method*, Journal of Vibroengineering 19(2), 1103–1115 (2017), doi:10.21595/jve.2016.17317, https://www.extrica.com/article/17317 (sections 3.1–4).
2. S. S. Muni, *Pathways to hyperchaos in a three-dimensional quadratic map*, arXiv:2406.08317v1, first posted 2024-06-12, https://arxiv.org/html/2406.08317v1 (especially equation 3.1 and sections 3–5).
3. S. S. Muni, *Ergodic and resonant torus doubling bifurcation in a three-dimensional quadratic map*, Nonlinear Dynamics 112, 4651–4661 (2024), doi:10.1007/s11071-024-09284-6 (abstract and bibliographic record inspected; complete text unavailable).
4. S. S. Muni, *Persistence of resonant torus doubling bifurcation under polynomial perturbations*, Franklin Open 10, 100207 (2025), doi:10.1016/j.fraope.2024.100207 (open-access discussion of quadratic-map perturbations).
