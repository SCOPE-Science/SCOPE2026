# Arithmetic Galois splitting and exceptional reductions of three nodal-cubic osculating conics

## Finding
Let \(\omega\) be a primitive cube root of unity. Consider the three conics
\[
\begin{aligned}
Q_1&=21(X^2+Y^2)-22XY-6(X+Y)Z+Z^2,\\
Q_2&=21(\omega X^2+\omega^2Y^2)-22XY-6(\omega^2 X+\omega Y)Z+Z^2,\\
Q_3&=21(\omega^2X^2+\omega Y^2)-22XY-6(\omega X+\omega^2Y)Z+Z^2.
\end{aligned}
\]
These are three hyperosculating conics of the nodal cubic \(X^3+Y^3-XYZ=0\) in the literature cited below. Their union \(D=V(Q_1Q_2Q_3)\) is defined over \(\mathbb Q\).

**Arithmetic classification.** The twelve geometric ordinary nodes of \(D\) have minimal common field of definition
\[
K=\mathbb Q(\omega,\sqrt{13}),\qquad [K:\mathbb Q]=4,
\]
with Galois group \(C_2\times C_2\) and node-orbit sizes \(1,1,2,2,2,4\). Exactly two individual nodes are rational over \(\mathbb Q\).

Put \(T[X:Y:Z]=[\omega X:\omega^2Y:Z]\). The complete set of geometric nodes, without multiplicity, is
\[
\left\{T^j(P):j=0,1,2,\quad P\in\big\{[-7:5:7],[5:-7:7],
[1:1:-3+2\sqrt{13}],[1:1:-3-2\sqrt{13}]\big\}\right\}.
\]

**Every prime field.** For every prime \(p\ge5\) other than \(7\) and \(13\), the reduced union has three distinct smooth conic components and exactly twelve geometric ordinary nodes, without other singularities. Its number \(N_p\) of \(\mathbb F_p\)-rational singular points is
\[
N_p=\begin{cases}
12,&\left(\frac{-3}{p}\right)=1,\ \left(\frac{13}{p}\right)=1,\\
6,&\left(\frac{-3}{p}\right)=1,\ \left(\frac{13}{p}\right)=-1,\\
4,&\left(\frac{-3}{p}\right)=-1,\ \left(\frac{13}{p}\right)=1,\\
2,&\left(\frac{-3}{p}\right)=-1,\ \left(\frac{13}{p}\right)=-1.
\end{cases}
\]
All four cases have natural density \(1/4\) among primes. The exact set of exceptional reduction primes at least five is \(\{7,13\}\).

## Assumptions and scope
All characteristic-zero assertions concern the stated fixed rational sextic, and its projective nodes (not points on the original nodal cubic). For the reduction theorem use the integral polynomial \(4Q_1Q_2Q_3\in\mathbb Z[X,Y,Z]\); the scalar \(4\) is invertible for every prime in scope. The quadratic-symbol formula excludes the ramified primes \(3,13\); the geometric theorem excludes \(2,3,7,13\). Every conic is considered over a geometric algebraic closure. The observed generic number of twelve geometric nodes itself is established in the 2023 originating literature; the claims here are their explicit Galois scheme and all-prime arithmetic classification.

## Proof
**1. Explicit pair intersections.** In \(\mathbb Z[\omega][X,Y,Z]\), direct subtraction factors as
\[
Q_2-Q_3=3(\omega-\omega^2)(X-Y)\bigl(7(X+Y)+2Z\bigr).
\]
On \(X=Y=t\), either conic reduces to
\[
Z^2+6tZ-43t^2=0,
\]
whose two projective solutions are \([1:1:-3\pm2\sqrt{13}]\). On the other line \(7(X+Y)+2Z=0\), either conic restricts to
\[
-\tfrac14(5X+7Y)(7X+5Y),
\]
giving \([-7:5:7]\) and \([5:-7:7]\). The two lines in the factorization meet at a point where the conic has value \(-36t^2\), nonzero for the allowed characteristics. The roots on the first line are separate outside characteristic \(13\); those on the second are separate outside \(2,3\). Thus for every prime \(p\ge5\), \(p\ne13\), this pair has four simple distinct geometric intersections.

**2. Twelve and only twelve nodes.** The projective diagonal map \(T\) cyclically permutes the three conics. It therefore takes the four nodes above to the other two pairs, giving twelve candidate pairwise intersections. Every quadratic-form determinant is \(-256\); hence all conics are smooth in odd characteristic. At either rational base point, the third conic has value
\[
Q_1([-7:5:7])=Q_1([5:-7:7])=2457=3^3\cdot7\cdot13.
\]
At the two quadratic base points the two third-conic values multiply to
\[
\prod_{\epsilon=\pm1}Q_1([1:1:-3+2\epsilon\sqrt{13}])=-3^5\cdot13.
\]
Therefore for \(p\ge5\), \(p\notin\{7,13\}\), none of the three conics passes through the four intersection points of the other two. There are no triple-component points, and the twelve simple pairwise intersections are precisely the singularities, each with two transverse smooth branches. In characteristic \(7\), the rational pair nodes acquire a third conic and the incidence type changes; in characteristic \(13\), the two quadratic intersection points coalesce. This proves that the two stated exceptional primes are genuine and that no others occur within the specified range.

**3. Splitting field and orbit decomposition.** All twelve coordinates lie in \(K=\mathbb Q(\omega,\sqrt{13})\). The presence of the distinct conjugate quadratic nodes forces \(\sqrt{13}\) into a common field of definition. The node \(T([-7:5:7])\) has projective coordinate ratio \(-7\omega/(5\omega^2)\), which generates \(\mathbb Q(\omega)\); hence both subfields are necessary. They are disjoint quadratic fields, so the common field has degree four. Conjugating \(\sqrt{13}\) exchanges the two quadratic base nodes; conjugating \(\omega\) inverts \(T\). Their commuting action gives the orbit sizes \(1+1+2+2+2+4\). The four group elements \((1,1)\), \((1,\sigma_{13})\), \((\sigma_{-3},1)\), \((\sigma_{-3},\sigma_{13})\) have exactly \(12,6,4,2\) fixed nodes, respectively.

**4. Frobenius counts and density.** For each unramified prime in the geometric stability range, the two quadratic Frobenius characters are the Legendre symbols \(\left(\frac{-3}{p}\right)\) and \(\left(\frac{13}{p}\right)\). Fixed points under arithmetic Frobenius are exactly the rational geometric nodes. The four group fixed-point counts give the four-row formula. The distinct quadratic fields are linearly disjoint, and the associated biquadratic abelian extension has all four Frobenius conjugacy classes of size one; Chebotarev (equivalently quadratic-character equidistribution) gives natural density \(1/4\) for each row.

## Verification
A standalone Python-standard-library program, `verify.py`, verifies the exact node equations using arithmetic in the rank-four ring \(\mathbb Z[\omega,\sqrt{13}]\), confirms 12 distinct projective nodes and the four fixed-node counts, and checks direct Jacobian singular-point counts for the rational defining sextic over 20 distinct prime fields. Execute `python3 verify.py`; expected terminal marker: `VERIFY_OK`.

Specifically, let
\[
R=-21(X^2+Y^2)-44XY+6(X+Y)Z+2Z^2,\quad
S=21(X^2-Y^2)+6(X-Y)Z.
\]
The integral sextic is \(F=Q_1(R^2+3S^2)=4Q_1Q_2Q_3\). The program computes projective zeroes of \(F\) and all three formal partial derivatives over each listed prime field, without relying on the closed-form Frobenius count as its Jacobian test. These computations are cross-checks only: the factorization, smoothness, absence of threefold intersections, and Galois proof above establish the infinitely many prime assertions.

## Relationship to prior work
Dimca–Ilardi–Malara–Pokora (arXiv:2311.08913), Section 3, give these same three hyperosculating conics and their cyclic transformation, and prove the **geometric** statement that each pair meets at four nodes. Bromboszcz (arXiv:2401.06560), Sections 2–3, also gives their explicit equations in a study of cubic/conic/line arrangements. These geometric and characteristic-zero incidence facts are not claimed as new. The present arithmetic theorem goes beyond either geometric statement by determining all node coordinates and their minimal common field, the six arithmetic Galois orbits, all fixed-point counts, and the complete prime-exception/frobenius spectrum. Targeted searches for the same splitting field, equivalent Galois orbits, node schemes and reduction classifications found no covering arithmetic result; an unindexed arithmetic study remains a limitation of the originality assessment.

## Limitations
This is a theorem for one canonical union of three conics and the specified integral model, not a family of all sextactic conics or the entire arrangement including the original cubic. No assertion about the singularity basket in characteristics \(2\) or \(3\), or the full finer singularity types at the exceptional primes \(7\) and \(13\), is made. The prime-field enumeration is finite supporting evidence, not a substitute for the algebraic all-prime proof. The literature comparison is limited to material examined and searchable publications; it is not an independent audit or a guarantee of exhaustive publication coverage.

## References
1. A. Dimca, G. Ilardi, G. Malara and P. Pokora, *Construction of free curves by adding osculating conics to a given cubic curve*, arXiv:2311.08913v1 (first publicly posted 2023-11-15), especially Section 3, Theorem 3.3. https://arxiv.org/abs/2311.08913
2. M. Bromboszcz, *Arrangements of inflectional lines, hyperosculating conics, and plane cubics*, arXiv:2401.06560v1 (first publicly posted 2024-01-12), especially Sections 2–3. https://arxiv.org/abs/2401.06560
