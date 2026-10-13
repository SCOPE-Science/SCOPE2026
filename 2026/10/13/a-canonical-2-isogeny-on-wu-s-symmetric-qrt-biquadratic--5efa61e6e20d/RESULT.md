# A canonical 2-isogeny on Wu's symmetric QRT biquadratic
## Finding
Let
\[
C=\mathcal Q_{\alpha,\beta,\gamma}\subset\mathbf P^1\times\mathbf P^1
\]
be the smooth projective completion of Wu's symmetric QRT curve
\[
x^2y^2+\alpha(x^2+y^2)+\beta xy+\gamma=0
\]
over a field \(k\) of characteristic different from \(2,3\). Assume Wu's smoothness discriminant
\[
\Delta_Q
=
\alpha\gamma
\bigl((2\alpha+\beta)^2-4\gamma\bigr)
\bigl((2\alpha-\beta)^2-4\gamma\bigr)
\]
is nonzero.

Then the central sign involution
\[
\tau(x,y)=(-x,-y)
\]
is fixed-point-free on \(C\). Its quotient is a genus-one curve, and on the affine chart the quotient map is
\[
q(x,y)=(u,v)=(x^2,xy),
\]
with invariant function field described by
\[
\boxed{
\alpha u^2+(v^2+\beta v+\gamma)u+\alpha v^2=0.
}
\]
Consequently
\[
q:C\longrightarrow C/\langle\tau\rangle
\]
is an etale morphism of degree \(2\).

If \(C(k)\neq\varnothing\) and \(O\in C(k)\) is chosen as the origin, then the quotient with origin \(q(O)\) is an elliptic curve and \(q\) is a degree-two isogeny. Moreover
\[
T=\tau(O)
\]
is a nonzero \(k\)-rational point of order \(2\), and
\[
\tau(P)=P+T
\]
for every \(P\in C\).

## Assumptions and scope
Wu's Section 10 studies the symmetric biquadratic
\[
\mathcal Q_{\alpha,\beta,\gamma}:
\quad
x^2y^2+\alpha(x^2+y^2)+\beta xy+\gamma=0
\]
in characteristic different from \(2,3\). Proposition 10.1 proves that its projective completion is a smooth genus-one normal quartic precisely when \(\Delta_Q\neq0\).

The fixed-point-free quotient statement needs only smoothness. The isogeny and rational two-torsion formulation additionally assumes a chosen rational point \(O\in C(k)\), exactly as is standard when a genus-one curve is turned into an elliptic curve.

No assertion is made that every smooth member has a \(k\)-rational point. Without such a point the degree-two etale quotient still exists over \(k\), but the pointed elliptic-curve formulation is omitted.

## Proof
Homogenize the affine equation using coordinates \((X_0:X_1)\) and \((Y_0:Y_1)\), with \(x=X_1/X_0\) and \(y=Y_1/Y_0\). The equation becomes
\[
X_1^2Y_1^2
+\alpha(X_1^2Y_0^2+X_0^2Y_1^2)
+\beta X_0X_1Y_0Y_1
+\gamma X_0^2Y_0^2=0.
\]
It is invariant under
\[
\tau((X_0:X_1),(Y_0:Y_1))
=
((X_0:-X_1),(Y_0:-Y_1)).
\]

The sign involution on each \(\mathbf P^1\) fixes only \(0\) and \(\infty\). Hence a fixed point of \(\tau\) on \(\mathbf P^1\times\mathbf P^1\) must be one of
\[
(0,0),\quad(0,\infty),\quad(\infty,0),\quad(\infty,\infty).
\]
Substitution into the bihomogeneous equation shows that these points lie on \(C\) only under, respectively,
\[
\gamma=0,\quad\alpha=0,\quad\alpha=0,
\]
while \((\infty,\infty)\) never lies on \(C\). Since \(\Delta_Q\neq0\) forces \(\alpha\gamma\neq0\), the involution \(\tau\) is fixed-point-free.

Because the characteristic is not \(2\), the quotient map by this free involution is finite etale of degree \(2\). Riemann--Hurwitz gives
\[
2g(C)-2
=
2\bigl(2g(C/\langle\tau\rangle)-2\bigr),
\]
and \(g(C)=1\), so
\[
g(C/\langle\tau\rangle)=1.
\]

For an explicit quotient equation, define
\[
u=x^2,
\qquad
v=xy.
\]
Both are \(\tau\)-invariant. Since \(x\) satisfies \(z^2-u=0\) and \(y=v/x\), the extension
\[
k(C)/k(u,v)
\]
has degree at most \(2\). It has the nontrivial automorphism \(\tau\), so its degree is exactly \(2\) and
\[
k(C)^{\langle\tau\rangle}=k(u,v).
\]
Substituting \(y=v/x\) into the original equation and multiplying by \(u=x^2\) yields
\[
\alpha u^2+(v^2+\beta v+\gamma)u+\alpha v^2=0.
\]
Thus the normalization of the projective closure of this affine equation is exactly \(C/\langle\tau\rangle\), and \(q(x,y)=(x^2,xy)\) realizes the quotient on the displayed chart.

Finally suppose \(O\in C(k)\). Give \(C\) origin \(O\) and the quotient origin \(q(O)\). A nonconstant morphism of genus-one curves carrying origin to origin is a group homomorphism, so \(q\) is a separable degree-two isogeny. Its geometric fibers are the \(\tau\)-orbits, hence
\[
\ker(q)=\{O,\tau(O)\}.
\]
The second point is distinct from \(O\) because \(\tau\) is fixed-point-free, and it is \(k\)-rational because both \(O\) and \(\tau\) are defined over \(k\). Therefore
\[
T=\tau(O)
\]
is a nonzero rational two-torsion point. The nontrivial deck transformation of the isogeny is translation by its nonzero kernel point, giving \(\tau(P)=P+T\).

## Verification
The source equation, projective model, discriminant, and genus-one conclusion were checked directly in Wu's Section 10 and Proposition 10.1. The discriminant visibly contains the factors \(\alpha\gamma\), which are exactly what exclude the three possible finite or mixed fixed points of the central sign involution.

The quotient calculation is symbolic and exact. The invariant pair \((u,v)=(x^2,xy)\) gives a degree-two subfield because \(x\) satisfies \(z^2-u\) and the nontrivial involution fixes \(u,v\). Direct substitution gives the displayed quotient equation. No finite search, numerical approximation, or unproved classification is used.

As a consistency check, the quotient is etale of degree \(2\), so Riemann--Hurwitz forces the quotient genus to remain \(1\). When a rational origin is chosen, the kernel has exactly the two points \(O\) and \(\tau(O)\), which independently confirms that \(\tau(O)\) has order \(2\).

## Relationship to prior work
Wu's paper develops direct group laws on the symmetric QRT model and records the two standard fiber-switching involutions. The checked Section 10 does not state the central sign involution as a fixed-point-free quotient, does not give the quotient equation above, and does not formulate a degree-two isogeny or the resulting rational two-torsion point.

Li and Takenawa treat general QRT biquadratics, including the standard decomposition of QRT dynamics into horizontal and vertical involutions and their interpretation as translations on elliptic fibers. Their checked text does not supply the central simultaneous-sign quotient for Wu's three-parameter symmetric family.

A separate 2026 paper of Wu studies model-preserving isogenies for the family \((u^2+u)(v^2+v)=d\) and a wider product family. Only its public abstract was available in this comparison. After the elementary shifts that remove the linear terms, that product family has no general \(\beta xy\) cross term, so the abstract does not cover the full three-parameter QRT family considered here. Because the full text was not available for inspection, it remains a stated residual originality risk rather than evidence of noncoverage.

Special Jacobi and Edwards models also carry classical two-isogenies, but they occupy special subfamilies or different normal forms and do not imply the displayed quotient formula for arbitrary \(\beta\).

## Limitations
The isogeny statement is conditional on a rational point used as origin. For an unpointed genus-one curve the canonical statement is the fixed-point-free degree-two etale quotient.

The argument identifies one canonical quotient and one rational two-torsion point when the curve is pointed; it does not classify all isogenies or the full torsion subgroup of a member.

A closely related 2026 paper by Wu on a different characteristic-uniform family was accessible only through its abstract during the literature comparison. It is therefore retained as a residual originality risk rather than treated as a fully inspected noncovering source.

## References
1. H. Wu, *Direct Group Laws on Classical Genus-One Models*, arXiv:2610.00029v1, first public 2026-09-02; especially Section 10 and Proposition 10.1.
2. Y. Li and T. Takenawa, *Tropical representation of QRT maps*, arXiv:2203.12319, for the general QRT involution-and-translation framework.
3. H. Wu, *A New Characteristic-Uniform Model for Elliptic Curves -- Theory, Arithmetic, and Applications*, arXiv:2608.01675, abstract inspected for related model-preserving isogeny work.
