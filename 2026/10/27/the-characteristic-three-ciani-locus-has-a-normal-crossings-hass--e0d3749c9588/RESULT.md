# The characteristic-three Ciani locus has a normal-crossings Hasse divisor and exact rank-stratum counts

## Finding
Let \(q=3^n\), \(n\ge1\), and let \(U\) be the affine parameter space of smooth marked Ciani quartics
\[
 C_{r,s,t}: x^4+y^4+z^4+r x^2y^2+s y^2z^2+t z^2x^2=0
\]
over \(\mathbb F_q\). The nonordinary divisor on \(U_{\overline{\mathbb F}_3}\) is a **simple-normal-crossings union** of the three smooth irreducible surfaces
\[
D_x:\ s+rt=0,\qquad D_y:\ t+rs=0,\qquad D_z:\ r+st=0.
\]
Its pairwise intersections are the three punctured parameter coordinate axes together with their common origin; all three components meet transversely at that origin. For every smooth geometric member, the Jacobian \(3\)-rank \(f\), the \(a\)-number, and the Newton polygon are determined by how many of the three displayed expressions vanish: if \(j\) vanish, then \(f=3-j\), \(a=j\), and the Newton slopes are \(0^{3-j},(1/2)^{2j},1^{3-j}\).

The **exact number of marked parameter triples** in \(U(\mathbb F_q)\) with each Jacobian \(3\)-rank is
\[
\begin{array}{c|c}
f&\#\{(r,s,t)\in U(\mathbb F_q):f(C_{r,s,t})=f\}\\ \hline
0&1\\
1&3(q-3)\\
2&3(q-3)(q-5)\\
3&(q-3)(q^2-7q+18).
\end{array}
\]
In particular, \(\#U(\mathbb F_q)=q^3-7q^2+18q-17\). These count marked parameter triples, **not** isomorphism classes of curves or moduli-stack points.

## Assumptions and scope
The base field has characteristic \(3\). The named family is parameterized by triples \((r,s,t)\) without quotienting by coordinate symmetries. Smoothness is equivalent to
\[
(r^2-1)(s^2-1)(t^2-1)\bigl(r^2+s^2+t^2-rst-1\bigr)\ne0.
\]
All assertions about singularities of the Hasse divisor are made on this smooth-curve parameter open \(U\), not on the excluded discriminant. The \(3\)-rank and Newton polygon are geometric invariants of the Jacobian over an algebraic closure.

## Proof
**Smoothness.** Write \(F=x^4+y^4+z^4+r x^2y^2+s y^2z^2+t z^2x^2\). In characteristic three,
\(F_x=x(x^2-r y^2-t z^2)\), and cyclically. A common critical projective point with a zero coordinate exists precisely when one coefficient has square \(1\). If all coordinates are nonzero, the linear system for \((x^2,y^2,z^2)\) has matrix
\[
\begin{pmatrix}1&-r&-t\\-r&1&-s\\-t&-s&1\end{pmatrix},
\]
whose determinant is the negative of \(r^2+s^2+t^2-rst-1\). Conversely, whenever the determinant vanishes away from the coordinate boundary, a nonzero kernel vector gives a critical projective point: the matrix's diagonal minors are nonzero, so every kernel entry is nonzero, and arbitrary nonzero entries have square roots in the algebraic closure. Euler's identity \(4F=xF_x+yF_y+zF_z\) puts that point on the quartic. The displayed nonvanishing condition is therefore necessary and sufficient; the smooth plane quartic has genus three.

**Cartier and elliptic factors.** For a smooth plane quartic in characteristic three, extract the coefficient matrix of \(F^{3-1}=F^2\) in the adjoint differential basis indexed by \(x,y,z\). Every off-diagonal entry vanishes because \(F^2\) has only even exponents. Its three relevant coefficients, those of \(x^4y^2z^2\), \(x^2y^4z^2\), and \(x^2y^2z^4\), are respectively \(2(s+rt)\), \(2(t+rs)\), and \(2(r+st)\). Thus
\[
H=\operatorname{diag}\bigl(2(s+rt),2(t+rs),2(r+st)\bigr).
\]
For example the involution \(x\mapsto-x\) has a smooth elliptic quotient with equation
\[
w^2=(r^2-4)y^4+(2rt-4s)y^2z^2+(t^2-4)z^4,
\quad w=2x^2+r y^2+t z^2.
\]
The middle coefficient \(2rt-4s=-(s+rt)\) in characteristic three is its Hasse invariant up to a nonzero factor. The other coordinate involutions give the other two elliptic quotients. The classical Ciani isogeny identifies the genus-three Jacobian with the product of these elliptic curves up to an isogeny of \(2\)-power degree, prime to three. Each factor is ordinary exactly when its corresponding diagonal coefficient is nonzero, and supersingular otherwise. The \(p\)-divisible groups up to isogeny therefore give the asserted \(3\)-rank and Newton slopes. Cartier rank gives the stated \(a\)-number (alternatively use the prime-to-three elliptic-product decomposition).

**Normal crossings.** On \(D_x\), substitute \(s=-rt\). The ambient smoothness condition simplifies to \((r^2-1)(t^2-1)((rt)^2-1)\ne0\), an open condition in the affine \((r,t)\)-plane. Thus \(D_x\) is a smooth irreducible surface, and so are the others. On \(D_x\cap D_y\), substitution gives \(t(1-r^2)=0\). Since \(r^2\ne1\) on \(U\), this forces \(s=t=0\), with \(r^2\ne1\). The other pairwise intersections are the analogous axes. Along this axis, the normal derivatives of \(s+rt\) and \(t+rs\) in coordinates \((s,t)\) have determinant \(1-r^2\ne0\). At their unique triple intersection \((r,s,t)=(0,0,0)\), the three gradients are linearly independent. Hence the reduced divisor is simple normal crossings throughout \(U\).

**Finite-field census.** Fix \(q=3^n\). Every point of \(D_x(\mathbb F_q)\) corresponds to \((r,t)\in(\mathbb F_q\setminus\{\pm1\})^2\) with \(rt\ne\pm1\). There are \((q-2)^2-2(q-3)=q^2-6q+10\) such pairs. Each pairwise component intersection has \(q-2\) points and the triple intersection has one. This gives the counts with respectively three, two, or one vanished Hasse factors: \(1\), \(3(q-3)\), and \(3(q-3)(q-5)\).

To count all of \(U(\mathbb F_q)\), first exclude the three coordinate values \(\pm1\), leaving \((q-2)^3\) triples. For fixed \(r,s\notin\{\pm1\}\), the discriminant equation \(r^2+s^2+t^2-rst-1=0\) is quadratic in \(t\), with discriminant \((r^2-1)(s^2-1)\) in characteristic three. Let \(\chi\) be the quadratic character with \(\chi(0)=0\). The standard factorization count gives \(\sum_{u\in\mathbb F_q}\chi(u^2-1)=-1\), hence \(\sum_{u\ne\pm1}\chi(u^2-1)=-1\). It follows that the number of pairs \((r,s)\) for which the discriminant is a square is \(((q-3)^2+(q-1)^2)/4=(q^2-4q+5)/2\); each contributes two distinct roots \(t\). Of these roots, exactly \(q-2\) have \(t=1\), and exactly \(q-2\) have \(t=-1\). Thus the forbidden discriminant has \((q-3)^2\) triples after all coordinate exclusions. Therefore
\[\#U(\mathbb F_q)=(q-2)^3-(q-3)^2=q^3-7q^2+18q-17.\]
Subtracting the three nonordinary ranks yields the displayed ordinary-rank count.

## Verification
A standalone, standard-library-only checker `check.py` verifies the coefficient identities, exhaustively counts smooth parameter triples for \(q=3,9,27\), and checks rank witnesses and direct curve point counts for \(q=9\). Its verified rank counts are \((1,0,0,0)\) for \(q=3\), \((1,18,72,216)\) for \(q=9\), and \((1,72,1584,13392)\) for \(q=27\). These finite checks corroborate but do not replace the universally quantified algebraic proof. Running the checker requires `python3 check.py` and no external dependencies.

## Relationship to prior work
Howe–Leprévost–Poonen establish the genus-three biquadratic/Ciani construction and splitting isogenies; Auer–Top study a symmetric one-parameter genus-three subfamily; Ohashi provides the full smoothness criterion and explicit elliptic quotients, particularly for the superspecial/maximal case. Their results furnish essential ingredients and already address parts of the low-rank behavior. The additional statement assessed here is the **simultaneous three-parameter normal-crossings Hasse-divisor structure and complete all-\(3\)-power rational parameter-count formulas** (with Newton strata). No claim is made that individual elliptic-quotient tests or the superspecial Fermat example are new.

## Limitations
The equations apply only on the smooth marked Ciani parameter family over characteristic three. The counts are not weighted moduli counts or enumerations of geometric isomorphism classes. The decomposition is prime-to-characteristic, not an assertion that the principally polarized Jacobian is a product. The novelty comparison was conducted against the cited primary texts and available mathematical records; equivalent counting formulas could exist in additional literature. No independent mathematical audit has been performed.

## References
- E. Howe, F. Leprévost, B. Poonen, *Large torsion subgroups of split Jacobians of curves of genus two or three*, arXiv:math/9809210, first submitted 1998-09-08, especially §4.1 and Proposition 15.
- R. Auer, J. Top, *Some genus 3 curves with many points*, arXiv:math/0201320, first submitted 2002-01-16.
- R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996, first submitted 2022-01-31, especially Lemma 2.1 and §3.
- N. Bouw et al., *On the Conductor of Ciani Plane Quartics*, arXiv:2310.10416. Only publicly visible portions were inspected; the full conductor treatment was not used to support a noncoverage claim.
