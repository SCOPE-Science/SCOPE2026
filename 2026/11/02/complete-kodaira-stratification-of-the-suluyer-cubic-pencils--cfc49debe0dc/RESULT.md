# Complete Kodaira stratification of the Suluyer cubic pencils

## Finding

Let \(a\in\mathbb C\setminus\{0,1\}\), and resolve all nine base points, counting infinitely near points, of the pencil
\[
\lambda(x-ay)(x^2+y^2-z^2)+\mu(x-y)(x^2-xy+y^2-z^2)=0.
\]
Its relatively minimal rational elliptic surface with section is denoted \(S_a\to\mathbb P^1\). Write \(t=\mu/\lambda\), with \(t=\infty\) for \([\lambda:\mu]=[0:1]\). Every singular fiber and its Kodaira type are as follows; in each row the indicated parameter polynomials are understood to be zero, and all unlisted parameters are nonspecial.

| Parameter condition | Full singular-fiber multiset | Mordell–Weil rank |
|---|---|---:|
| None of the conditions below | \(4I_2+4I_1\) | 4 |
| \(a=2\), \(a=1/2\), or \(a^2+1=0\) | \(3I_2+III+3I_1\) | 4 |
| \(4a^2-12a+7=0\) or \(7a^2-12a+4=0\) | \(3I_2+I_3+3I_1\) | 3 |
| \(a^2-a+1=0\) | \(5I_2+2I_1\) | 3 |
| \(71a^2-196a+71=0\) | \(4I_2+II+2I_1\) | 4 |

The four distinguished fibers are at \(t=0,-1,-a,\infty\). When \(a=2\), \(a=1/2\), and \(a^2+1=0\), the indicated \(III\) fiber is at \(t=-1,-a,0\), respectively. The \(I_3\) fibers for the two quadratic conditions occur at \(t=-1\) and \(t=-a\), respectively. For \(a^2-a+1=0\), the extra \(I_2\) is at \(t=(a+1)/3\). For \(71a^2-196a+71=0\), the \(II\) fiber is at \(t=-4(a+1)/13\). The exceptional parameter loci are mutually disjoint. Each multiset has total fiber Euler number \(12\).

## Assumptions and scope

All curves and surfaces are over \(\mathbb C\). The parameter \(a\) may be any complex number other than \(0\) and \(1\); the locus \(a^2-a+1=0\) is included, and its base scheme has a length-two point requiring an infinitely near blow-up. The types refer to relatively minimal *resolved elliptic surfaces*, not merely singularity types of the original plane cubic members. The Mordell–Weil rank is the geometric rank of the section group over \(\mathbb C(t)\). No claim about its torsion or a global simultaneous minimal model over the parameter line \(a\) is made.

## Proof

**(1) Projection and the Jacobian invariants.** Put \(A=x-ay\), \(B=x-y\),
\[
L=A+tB,\qquad G=A(x^2+y^2)+tB(x^2-xy+y^2).
\]
The member at finite \(t\) is \(z^2L=G\). Projection from its common smooth base point \([0:0:1]\) gives the birational quartic model \(w^2=H(x,y)\), where \(w=zL\) and \(H=LG\). This is a binary quartic over \(\mathbb C(t)\), and its leading coefficient in \(x\) is \((1+t)^2\), so the generic curve has a rational point above \(y=0\). Its Jacobian is therefore the generic cubic itself.

For \(H=\alpha x^4+b x^3y+c x^2y^2+dxy^3+ey^4\), set
\[
I=12\alpha e-3bd+c^2,\qquad
J=72\alpha ce+9bcd-27\alpha d^2-27b^2e-2c^3.
\]
The corresponding elliptic \(j\)-invariant is \(j=1728\cdot4I^3/(4I^3-J^2)\). An explicit integral Jacobian equation is \(v^2=u^3-27Iu-27J\), up to the standard nonzero constant choices of invariants. Its discriminant is a nonzero constant times \(4I^3-J^2\). The coefficient degrees in \(t\) are at most four and six, respectively.

Direct polynomial expansion gives
\[
I_a(t)=t^4+3(a+1)t^3+(11a^2-9a+11)t^2+6(a^3+1)t+(a^2+1)^2
\]
and
\[
4I_a(t)^3-J_a(t)^2
=-27(a-1)^2t^2(t+1)^2(t+a)^2Q_a(t),
\]
where
\[
Q_a(t)=3t^4+10(a+1)t^3+(59a^2-70a+59)t^2
+4(7a^3-a^2-a+7)t+4(a^2+1)^2.
\]
The formula for \(J_a\) is determined exactly by the displayed quartic-coefficient definition, so there is no implicit numerical approximation. The homogeneous discriminant has degree twelve and valuation exactly two at \(t=\infty\), since its affine expression has degree ten; the homogenized \(I\) has value one at infinity. The local Jacobian equations are minimal: every zero of the discriminant has valuation at most three, hence no common Weierstrass scaling by a local parameter is possible. Thus the stated discriminant orders are minimal fiber orders.

**(2) Exhaustion of collision parameters.** The quartic satisfies the exact identities
\[
\begin{aligned}
Q_a(0)&=4(a^2+1)^2,\\
Q_a(-1)&=(a-2)^2(4a^2-12a+7),\\
Q_a(-a)&=(2a-1)^2(7a^2-12a+4),\\
\operatorname{disc}_{t}(Q_a)&=512(a-1)^4(a^2-a+1)(71a^2-196a+71)^3.
\end{aligned}
\]
Furthermore,
\[
I_a(0)=(a^2+1)^2,\quad I_a(-1)=(a-2)^2(a-1)^2,\quad I_a(-a)=(a-1)^2(2a-1)^2.
\]
These formulas show that, away from the listed parameter polynomials, the four fixed discriminant points have type \(I_2\), while the four distinct roots of \(Q_a\) are \(I_1\). In particular, no unlisted collisions occur.

For completeness, the following table gives the exact orders in the local coordinate \(t-t_0\); each entry is obtained by polynomial remainder in \(a\) modulo its row's parameter polynomial (or by direct substitution in a linear case). The order of \(4I^3-J^2\) follows from the factored formula.

| Parameter equation | \(t_0\) | \(\operatorname{ord}I\) | \(\operatorname{ord}J\) | \(\operatorname{ord}\Delta\) | Kodaira type |
|---|---|---:|---:|---:|---|
| \(a-2=0\) | \(-1\) | 1 | 2 | 3 | \(III\) |
| \(2a-1=0\) | \(-a\) | 1 | 2 | 3 | \(III\) |
| \(a^2+1=0\) | \(0\) | 1 | 2 | 3 | \(III\) |
| \(4a^2-12a+7=0\) | \(-1\) | 0 | 0 | 3 | \(I_3\) |
| \(7a^2-12a+4=0\) | \(-a\) | 0 | 0 | 3 | \(I_3\) |
| \(a^2-a+1=0\) | \((a+1)/3\) | 0 | 0 | 2 | \(I_2\) |
| \(71a^2-196a+71=0\) | \(-4(a+1)/13\) | 1 | 1 | 2 | \(II\) |

All row parameter polynomials are pairwise coprime. For either repeated-root case, \(Q_a\) has precisely one double root at the indicated \(t_0\); the other two roots remain simple. In the first five rows, \(Q_a\) has one simple root at a fixed discriminant point, and three other simple roots. The displayed \((I,J,\Delta)\) valuations and the characteristic-zero Kodaira table determine every type. Every row's total Euler number is twelve.

**(3) Resolution and relative minimality.** The base scheme is the complete intersection of the two generating cubics and has length nine. The intersections of their factors have lengths \(1,2,2,4\). For \(a\ne0,1\), they represent nine distinct points except when \(a^2-a+1=0\), where the intersection of \(x-ay=0\) with \(x^2-xy+y^2-z^2=0\) becomes a tangency at \([a:1:0]\), giving one length-two point and eight distinct points overall. The tangent-direction base point is resolved by one further infinitely near blow-up. Thus there are nine ordinary blow-ups counting infinitely near centers, and the resulting fiber class is \(-K_{S_a}\). A vertical \((-1)\)-curve \(E\) would satisfy simultaneously \((-K_{S_a})\cdot E=0\) and \((-K_{S_a})\cdot E=1\) by adjunction, a contradiction. Hence the fibration is relatively minimal and rational. The base point \([0:0:1]\) gives a section. At \(a^2-a+1=0\), the cubic at \(t=(a+1)/3\) has an ordinary node at the tangential base point; the additional fiber component is produced by the resolution. Its elliptic fiber has type \(I_2\), although this original cubic is not an extra conic-line member.

**(4) Mordell–Weil rank.** A rational elliptic surface has Néron–Severi rank ten. The Shioda–Tate formula gives \(\operatorname{rank}MW=8-\sum_v(m_v-1)\), where \(m_v\) is the number of irreducible components in the geometric Kodaira fiber. For types \(I_2,III,I_3,II,I_1\), the component contributions are \(1,1,2,0,0\), respectively. This yields the ranks displayed above.

## Verification

The standalone `verify.py` reconstructs \(H\), \(I\), and \(J\) from the defining pencil; checks the full polynomial identity for the discriminant, the quartic discriminant and the fixed-fiber evaluations; and verifies all seven exceptional \((I,J,Q)\) local-order patterns using exact arithmetic modulo the corresponding defining polynomial. It also checks the distinguished nodal base point and pairwise disjointness of the exceptional parameter loci. Executing `python verify.py` with SymPy prints `VERIFY_OK`. These exact symbolic checks are reproducibility aids; the proof is the polynomial identity together with the local Kodaira and resolution arguments, not experimental extrapolation.

## Relationship to prior work

Suluyer's preprint *Pencils of Conic-Line Curves*, arXiv:2412.06928 (first submitted 2024-12-09), introduces the pencil and gives its four conic-line members; its Example 4.2 describes the singular fibers only at \(a=2\). The later 2026 journal version gives the same motivating family and example. Neither accessible full-text presentation states the parameter-wide quartic discriminant, the complete collision locus, or the Mordell–Weil rank table. The binary-quartic invariants, Kodaira classification, Shioda–Tate formula, and rational elliptic-surface theory are classical ingredients, not newly claimed results. An older 2024 thesis by Suluyer is cited in the preprint, but its full text was not accessible during the comparison and could overlap; this is an unresolved priority risk.

## Limitations

This classification is over \(\mathbb C\) and for the displayed marked pencil, not for all pencils with four conic-line members. It classifies geometric Kodaira fibers and free Mordell–Weil ranks, not torsion, exact sections, monodromy factorizations, or bad reduction in positive characteristic. The claim of historical priority is provisional because other equivalent descriptions may exist under changes of pencil parameter or in the inaccessible 2024 thesis. No independent mathematical audit has been performed.

## References

1. H. Suluyer, *Pencils of Conic-Line Curves*, arXiv:2412.06928, first submitted 2024-12-09, Sections 2–5, especially Theorem 4.1 and Example 4.2, https://arxiv.org/abs/2412.06928.
2. H. Suluyer, *On the Number of Conic-Line Curves in a Pencil*, Mediterranean Journal of Mathematics 23 (2026), 127, https://doi.org/10.1007/s00009-026-03125-z.
3. H. Suluyer, *Classification Problems of Multinets and Conic-Line Arrangements*, PhD thesis, Middle East Technical University (2024), https://hdl.handle.net/11511/110938 (full text not verified).
4. Classical binary-quartic invariant theory and Tate–Kodaira classification of fibers; see the invariant formulas explicitly stated above and R. Miranda, *The Basic Theory of Elliptic Surfaces* (1989), for the general theory.
