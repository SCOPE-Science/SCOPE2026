# The four-node and ten-singularity strata of the generalized Wiman–Edge sextic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(p\ge5\). For \(a,b\in k\), consider the plane sextic
\[
S_{a,b}:\ X^6+Y^6+Z^6+a(X^4Y^2+Y^4Z^2+Z^4X^2)+b(X^2Y^4+Y^2Z^4+Z^2X^4)-3(a+b+1)X^2Y^2Z^2=0.
\]
Set \(L=a+b+3\), \(R=a^2+ab+b^2\), and
\[
\Delta=a^2b^2-4(a^3+b^3)+18ab-27.
\]
On the exact open set \(LR\ne0\), the sextic is geometrically integral. Its full geometric singularity classification is:

1. If \(\Delta\ne0\), it has exactly four ordinary nodes, at \([\pm1:\pm1:1]\), and its normalization has genus six.
2. If \(\Delta=0\) and \((a,b)\ne(3,3)\), it has exactly ten ordinary nodes: the four above plus six on the coordinate axes. Its normalization is rational.
3. At \((a,b)=(3,3)\), it has the four ordinary nodes and exactly six ordinary cusps, again with rational normalization.

The equality \((a,b)=(3,3)\) means the images of the integers \(3,3\) in \(k\). In particular, the exact locus of geometrically integral sextics with precisely four ordinary nodes is \(LR\Delta\ne0\); the discriminant divisor within \(LR\ne0\) is a rational degeneration, with its one cuspidal special parameter.

## Assumptions and scope
All claims are over an algebraically closed field of characteristic at least five. The parameter space is the affine plane with ordered coefficients. The curves are projective plane sextics; genus refers to smooth projective normalization. The theorem makes no claim about parameters with \(LR=0\) or about ground-field point counts, isomorphism classes, or stable models. “Ordinary cusp” means a plane \(A_2\) singularity; “ordinary node” means \(A_1\).

## Proof
**The nodal cubic.** Write \(U=X^2,V=Y^2,W=Z^2\), and define
\[
Q_{a,b}=U^3+V^3+W^3+a(U^2V+V^2W+W^2U)+b(UV^2+VW^2+WU^2)-3(a+b+1)UVW.
\]
The sextic is its pullback by the finite coordinate-squaring map. The cubic has a singular point \(P=[1:1:1]\). With \(W=1,U=1+u,V=1+v\), its equation is exactly
\[
L(u^2-uv+v^2)+u^3+au^2v+buv^2+v^3=0.
\]
As \(p\ne2,3\), if \(L\ne0\) this is an ordinary node with two distinct tangent slopes satisfying \(t^2-t+1=0\). Substituting \(v=tu\), the cubic coefficient modulo the tangent equation is \((a+b)t-b\). The product of these two tangent coefficients is \(R\). A nodal plane cubic is reducible precisely when at least one of its two tangent lines at the node is a component: if reducible, its singular point lies in the intersection of two components and a line component passes through it. Thus \(Q_{a,b}\) is geometrically integral with exactly the one node \(P\) if and only if \(LR\ne0\).

**The coordinate axes.** For \(LR\ne0\), the node \(P\) is off the axes, so the cubic is smooth at each of its nine axis-intersection points counted with multiplicity. On each axis the intersection is described, up to swapping \(a,b\), by the monic cubic \(h(T)=T^3+aT^2+bT+1\). Its discriminant equals \(\Delta\), which is symmetric in \(a,b\). The roots are nonzero, and the three coordinate axes have no common points on \(Q\). If \(\Delta\ne0\), the three intersections with each axis are transverse. If \(\Delta=0\), the cubic has either one double and one simple root on each axis, or one triple root on each axis (the latter case is characterized below).

**Irreducibility of the pullback.** The normalization \(\widetilde Q\) of the irreducible nodal cubic is \(\mathbf P^1_k\). The function field of the normalization of \(S\) is obtained from \(k(\widetilde Q)\) by adjoining \(\sqrt{U/W}\) and \(\sqrt{V/W}\). These squareclasses are independent: on the axis \(U=0\), at least one intersection point has odd multiplicity (indeed the partition of three is \((1,1,1)\), \((2,1)\), or \((3)\)); there \(V/W\) has valuation zero. Likewise \(V/W\) has an odd valuation at a point on \(V=0\) where \(U/W\) is a unit. Hence the two classes are independent modulo squares; the cover is connected of degree four. This proves geometric integrality of \(S\) for \(LR\ne0\).

**All singularities.** Away from the coordinate axes, coordinate squaring is étale. The nodal point \(P\) has exactly four preimages, \([\pm1:\pm1:1]\), all ordinary nodes. There are no other singularities in the torus. On an axis, choose a local coordinate \(s\) along the smooth cubic and a normal coordinate \(U\). If the axis intersection multiplicity is \(m\in\{1,2,3\}\), smoothness of \(Q\) gives a local equation \(U=c s^m\) times a unit with \(c\ne0\). Under squaring, the local equation of \(S\) becomes analytically \(x^2=s^m\), because the map is étale in the other nonzero coordinate. Each base axis-intersection point has two preimages. For \(m=1\) these are smooth, for \(m=2\) they are ordinary nodes, and for \(m=3\) they are ordinary cusps. Thus simple axis intersections yield only the four original nodes; a double root yields two further nodes per axis, making ten nodes total; a triple root yields two cusps per axis, making four nodes and six cusps.

**Triple-root uniqueness on \(LR\ne0\).** If \(h(T)=(T-r)^3\), then \(r^3=-1\), \(a=-3r\), \(b=3r^2\). Modulo \(r^3+1\), we have \(L=3(r^2-r+1)\) and \(R=9(r^2-r+1)\). Since \((r+1)(r^2-r+1)=r^3+1\), \(LR\ne0\) forces \(r=-1\), whence \(a=b=3\). Conversely these values give \(h(T)=(T+1)^3\) and \(LR\ne0\), as \(p\ne3\).

**Normalization genus.** A degree-six plane curve has arithmetic genus ten. Ordinary nodes and ordinary cusps each have \(\delta\)-invariant one. The three cases therefore give geometric genus \(10-4=6\), \(10-10=0\), and \(10-4-6=0\), respectively. A smooth integral genus-zero curve over algebraically closed \(k\) is rational.

## Verification
The included standalone Python verifiers are `verify_symbolic.py` and `verify_f25.py`; both run using Python 3 (the symbolic checker additionally requires SymPy). The symbolic verifier checks the pullback identity, the cubic's nodal expansion, the tangent-line remainder, the symmetric discriminant, the resultant identity \(-L^3R\) from the published genus-two quotient, and the triple-root reduction. The finite-field verifier independently enumerates the 651 projective points over \(\mathbb F_{25}\) using an explicit quadratic extension of \(\mathbb F_5\). For every \((a,b)\in\mathbb F_5^2\) with \(LR\ne0\), it counts singular points and separates Hessian-nondegenerate nodes from the cuspidal cases: 15 parameter pairs have four nodes; four pairs have ten singular points, exactly one with six Hessian-degenerate cusps. The infinite classification follows from the preceding proof, **not** from finite-field enumeration.

## Relationship to prior work
Kawakita (2017, Proposition 1) introduced the underlying two-parameter sextic and the genus-two quotient decomposition. Its paper, and Iezzi–Kawakita–Timpanella (2023, Section 4), give sufficient conditions for genus six involving \(a+b+2\), the discriminant of a cubic, and a resultant. Their resultant factors as \(-L^3R\). The present statement classifies *all* integral parameters with \(LR\ne0\), removes the unnecessary condition \(a+b+2\ne0\) for this geometric question, and identifies both the maximal ten-node rational locus and the exceptional six-cusp member. In particular, the two-dimensional discriminant boundary and singularity types are not consequences of a mere genus-six sufficiency condition without additional arguments. Earlier work on Edge's four-nodal pencil concerns a one-dimensional subfamily, not this complete two-parameter statement; a complete text comparison with Edge (1981) was unavailable.

## Limitations
No assertion about \(LR=0\), arithmetic rational-point counts, fields of definition of singular points, or stable reduction is included. An unindexed previous degeneration classification remains an originality risk. The finite-field checks are corroboration, not a substitute for the all-characteristic proof. No independent external validation has been performed.

## References
- M. Q. Kawakita, *Certain sextics with many rational points*, Advances in Mathematics of Communications **11** (2017), 289–292, DOI: `10.3934/amc.2017020`, full text: https://www.researchgate.net/publication/316820130_Certain_sextics_with_many_rational_points.
- A. Iezzi, M. Q. Kawakita and M. Timpanella, *New sextics of genus 6 and 10 attaining the Serre bound*, arXiv:2306.01928v1, first publicly posted 2023-06-02: https://arxiv.org/html/2306.01928v1.
- W. L. Edge, *A pencil of four-nodal plane sextics*, Mathematical Proceedings of the Cambridge Philosophical Society **89** (1981), 413–421.
