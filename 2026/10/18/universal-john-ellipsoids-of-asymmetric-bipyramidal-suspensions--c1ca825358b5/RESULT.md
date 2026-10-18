# Universal John ellipsoids of asymmetric bipyramidal suspensions and a sharp imbalance law

## Finding

**Theorem.** Fix an integer \(d\ge 2\). Let \(B\subset\mathbb R^{d-1}\) be a centrally symmetric convex body with center at the origin, and let \(a,b>0\). Write \(J(B)=A\mathbb B_2^{d-1}\), with \(A\) positive definite and \(\mathbb B_2^k\) the closed unit Euclidean ball. Consider the double pyramid
\[
K_{a,b}(B)=\operatorname{conv}\bigl((B\times\{0\})\cup\{(0,-a),(0,b)\}\bigr).
\]
Set
\[
T=a^2+b^2,\qquad
q=\frac{T+\sqrt{T^2+4(d^2-1)a^2b^2}}{2(d^2-1)},\qquad t=\sqrt q,
\]
\[
X=\sqrt{a^2+t^2},\quad Y=\sqrt{b^2+t^2},\quad
u=\frac{a+b}{X+Y},\quad v=ut,\quad c=uX-a=b-uY.
\]
Then the **unique** maximum-volume ellipsoid inside \(K_{a,b}(B)\) is
\[
\boxed{J(K_{a,b}(B))=\left\{(x,z):
\frac{\|A^{-1}x\|_2^2}{u^2}+\frac{(z-c)^2}{v^2}\le1\right\}.}
\]
With \(\kappa_k=\operatorname{Vol}_k(\mathbb B_2^k)\), its volume is
\[
\boxed{\operatorname{Vol}_d J(K_{a,b}(B))
=\frac{\kappa_d}{\kappa_{d-1}}\operatorname{Vol}_{d-1}J(B)\,u^{d-1}v.}
\]
In particular, all axial parameters \(u,v,c\) are independent of the shape of \(B\), and \(\operatorname{sign}(c)=\operatorname{sign}(b-a)\).

**Strict imbalance law.** Hold the total height \(H=a+b>0\), the base \(B\), and \(d\) fixed. The John-ellipsoid volume is strictly decreasing with \(|a-b|\) for \(a,b>0\). The host volume remains exactly
\[
\operatorname{Vol}_d K_{a,b}(B)=\frac{H}{d}\operatorname{Vol}_{d-1}B.
\]
Thus the John filling fraction also strictly decreases with apex-height imbalance. At the symmetric maximum, \(a=b=H/2\),
\[
u=\sqrt{\frac{d-1}{d}},\qquad v=\frac{H}{2\sqrt d},\qquad c=0.
\]
As one apex height decreases to zero, the limiting (one-sided cone) profile is
\[
u\longrightarrow\sqrt{\frac{d-1}{d+1}},\qquad
v\longrightarrow\frac{H}{d+1}.
\]
Consequently the sharp ratio of the symmetric maximum to the limiting infimum, independent of \(B\), is
\[
\boxed{\frac{d+1}{2\sqrt d}\left(\frac{d+1}{d}\right)^{(d-1)/2}}
\sim\frac{\sqrt{e d}}2\quad(d\to\infty).
\]
The infimum is not attained while both apex heights are required positive.

## Assumptions and scope

The base is any compact, convex, origin-symmetric, full-dimensional subset of \(\mathbb R^{d-1}\); no smoothness, strict convexity, polyhedrality, or Euclidean rotational symmetry is assumed. The apices lie on the line through the symmetry center, on opposite sides of the base hyperplane; \(a,b\) are strictly positive. The ellipsoid is unrestricted: its orientation, center, and shape are not prescribed. The same formulas apply under arbitrary nonsingular horizontal affine changes of the base. The final comparison holds for fixed dimension, fixed base, and fixed sum of heights, not for arbitrary changes of the base.

## Proof

**1. Symmetry removes all horizontal translation and tilt.** John's ellipsoid exists uniquely for each convex body with interior. Because \(B=-B\), the transformation \((x,z)\mapsto(-x,z)\) preserves the suspension. By uniqueness it preserves its John ellipsoid. This forces its horizontal center to be zero and its horizontal–vertical shape-matrix cross-block to vanish. Thus every possible John ellipsoid has sections of the form
\[
E_{H,c,v}=\{(x,z):z=c+vs,\ x\in\sqrt{1-s^2}\,H,\ -1\le s\le1\},
\]
where \(H\) is an origin-centered full-dimensional ellipsoid in the horizontal hyperplane, \(v>0\), and \(c\in\mathbb R\).

**2. The horizontal section must be a copy of \(J(B)\).** The horizontal section of \(K_{a,b}(B)\) at height \(z\in[-a,b]\) is \(m(z)B\), where
\[
m(z)=\min\{1+z/a,\ 1-z/b\}.
\]
Let \(u>0\) be the least number with \(H\subseteq u B\). Inclusion of the ellipsoid is equivalent to
\[
u\sqrt{1-s^2}\le m(c+vs)\qquad(-1\le s\le1),
\]
because the bodies are nested homothetic copies of \(B\). Replacing \(H\) by \(uJ(B)\) preserves these inequalities and maximizes the horizontal determinant among centered ellipsoids inside \(uB\), with equality only when \(H=uJ(B)\). (Uniqueness of the John ellipsoid of \(uB\) gives strictness.) Thus the unrestricted global maximizer necessarily has horizontal ellipsoid \(uJ(B)\). This argument does not require a rotationally symmetric base.

**3. The inclusion constraints reduce to two scalar inequalities.** For the candidate ellipsoid with horizontal scale \(u\), the two affine cone inequalities, required for all \(-1\le s\le1\), are
\[
a u\sqrt{1-s^2}\le a+c+vs,\qquad
b u\sqrt{1-s^2}\le b-c-vs.
\]
Maximizing a linear functional on the unit semicircle gives their exact equivalents
\[
\sqrt{a^2u^2+v^2}\le a+c,\qquad
\sqrt{b^2u^2+v^2}\le b-c. \tag{1}
\]
Therefore such a center \(c\) exists precisely when
\[
F_{a,b}(u,v):=\sqrt{a^2u^2+v^2}+\sqrt{b^2u^2+v^2}\le a+b. \tag{2}
\]
At a maximum with \(u,v>0\), inequality (2) must be an equality: otherwise both semiaxis scales could be increased slightly, increasing volume. Equality also fixes the center uniquely through (1).

**4. Explicit optimization and uniqueness.** Put \(t=v/u>0\). The only possible maximal horizontal scale at that ratio is
\[
u(t)=\frac{a+b}{\sqrt{a^2+t^2}+\sqrt{b^2+t^2}}.
\]
The volume, apart from the base constant in the theorem, is
\[
G(t)=\frac{(a+b)^d t}{(\sqrt{a^2+t^2}+\sqrt{b^2+t^2})^d}.
\]
Writing \(X(t)=\sqrt{a^2+t^2}\) and \(Y(t)=\sqrt{b^2+t^2}\), differentiation gives
\[
\frac{G'(t)}{G(t)}=\frac1t-\frac{dt}{X(t)Y(t)}.
\]
The ratio \(X(t)Y(t)/t^2=\sqrt{(1+a^2/t^2)(1+b^2/t^2)}\) decreases strictly from infinity to one as \(t\) increases. Since \(d>1\), the stationarity condition \(X(t)Y(t)=dt^2\) has exactly one solution. Moreover \(G(t)\to0\) as \(t\to0^+\) or \(t\to\infty\), so this critical point is the unique global maximum. Squaring its stationarity equation yields
\[
(d^2-1)t^4-(a^2+b^2)t^2-a^2b^2=0,
\]
whose unique positive solution is the displayed \(q=t^2\). Equation (1) now fixes \(c=uX-a=b-uY\). Since
\[
(bX)^2-(aY)^2=(b^2-a^2)t^2,
\]
and \(c=(bX-aY)/(X+Y)\), its sign equals that of \(b-a\). The volume formula follows from the determinant of the ellipsoid's block-diagonal parametrization, completing the uniqueness proof.

**5. Strict height-imbalance order and endpoints.** Fix \(H=a+b\) and \(u,v>0\). The function \(s\mapsto\sqrt{s^2u^2+v^2}\) has strictly positive second derivative \(u^2v^2/(s^2u^2+v^2)^{3/2}\). Thus \(F_{a,H-a}(u,v)\) is strictly increasing as \(|a-H/2|\) increases. A pair \((u,v)\) optimal for a more imbalanced apex pair satisfies (2) with equality, but is strictly feasible for every less imbalanced pair; multiplying both positive scales by a sufficiently small factor larger than one then gives a strictly larger feasible ellipsoid volume. This proves the strict inequality for the globally optimized volumes. Integrating the two conical sections shows \(\operatorname{Vol}(K)=\operatorname{Vol}(B)H/d\), so the same strict order holds for volume fractions.

For \(a=b=H/2\), the quartic yields \(t^2=a^2/(d-1)\) and consequently \(u^2=(d-1)/d\), \(v=H/(2\sqrt d)\). In the limit \(a\to0\) or \(b\to0\), the stationary equation gives \(t^2\to H^2/(d^2-1)\), \(u^2\to(d-1)/(d+1)\), and \(v\to H/(d+1)\). Dividing the two axial volume factors \(u^{d-1}v\) gives the stated sharp factor. Its asymptotic follows from \((1+1/d)^{d-1}\to e\).

## Verification

The bundled standard-library program `verify.py` independently evaluates the radical formulas, both sharp containment equalities, the stationary determinant identity, off-optimal aspect ratios, the strict sampled imbalance profiles, and endpoint ratios in dimensions 2 through 15. It prints the number of passing finite checks when run with Python 3. A separate numerical constrained optimization over all centered or tilted three-dimensional ellipsoids for five rectangular-base suspensions agreed with the predicted parameters within a maximal absolute error below \(2\times10^{-8}\). These experiments corroborate but do not replace the preceding analytic proof; all universal quantifiers follow from that proof.

## Relationship to prior work

John's classical uniqueness and contact criteria underpin the reduction but do not supply this double-pyramid formula. Jerónimo-Castro and McAllister (2012) characterize ellipsoidal cones rather than maximum-volume ellipsoids of oppositely joined cones. Gruber and Schuster (2012 preprint) provide a proof of the general John characterization. Ivanov, Lángi, Naszódi, and Sagmeister (2025) treat ellipsoids of revolution and general extremal conditions, including conical examples, without the explicit arbitrary-base asymmetric bipyramid law and fixed-height strict monotonicity given here. These observations distinguish the stated explicit claims from their inspected statements; they are not a guarantee of historical priority.

## Limitations

The two apices must be axial over the base's symmetry center, and the base must be centrally symmetric. No formula is asserted for offset apices or nonsymmetric bases. The strict comparison holds at fixed total altitude; the endpoint with a vanishing apex height is a limiting cone and is not an admissible positive-height double pyramid. No independent mathematical audit has been performed. Earlier uncatalogued special-case calculations (particularly planar kites, symmetric double cones, and cone limits) might overlap some formulas; the general shape-universality and strict imbalance statement require separate priority verification.

## References

1. J. Jerónimo-Castro and T. B. McAllister, *Two characterizations of ellipsoidal cones*, arXiv:1204.3947, first posted 18 April 2012. https://arxiv.org/abs/1204.3947
2. P. M. Gruber and F. E. Schuster, *An Arithmetic Proof of John's Ellipsoid Theorem*, arXiv:1207.7246, preprint posted 31 July 2012; earlier journal history acknowledged. https://arxiv.org/abs/1207.7246
3. G. Ivanov, Z. Lángi, M. Naszódi, and Á. Sagmeister, *John Ellipsoids of Revolution*, arXiv:2507.06947, first posted 9 July 2025. https://arxiv.org/abs/2507.06947
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948 (classical uniqueness and optimal-contact framework).
