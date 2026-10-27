# The fractional orbifold Hodge profile of a non-symplectic Fermat-sextic quotient

## Finding
Let \(X=V(\sum_{j=0}^{5}x_j^6)\subset\mathbb P^5_{\mathbb C}\), let \(\zeta\) be primitive of order six, and let \(G=\langle g\rangle\cong C_6\) act via \(g[x_0:\cdots:x_5]=[x_0:\zeta x_1:\cdots:\zeta^5x_5]\). Set \(Y=X/G\). Define \(E_{\mathrm{CR}}([X/G];u,v)\) to be the signed, age-shifted Hodge–Deligne polynomial of the Chen–Ruan cohomology of the smooth proper quotient orbifold, with rational bidegrees allowed. Then
\[
\boxed{\begin{aligned}
E_{\mathrm{CR}}([X/G];u,v)={}&1+uv+291u^2v^2+70(u^3v+uv^3)\\
&+u^3v^3+u^4v^4+18(uv)^2\\
&+2(uv)^{3/2}(1-4u-4v+uv).
\end{aligned}}
\]
In particular, the ordinary Hodge numbers of the coarse quotient have \(h^{3,1}(Y)=h^{1,3}(Y)=70\) and \(h^{2,2}(Y)=291\); its holomorphic four-form is absent, \(h^{4,0}(Y)=0\). The age-two contribution consists of two sectors of nine points each; the age-three-halves contribution comes from two genus-four curves. Evaluating at \(u=v=1\) gives the orbifold Euler value \(441\), compared with the coarse Euler value \(435\). These two Euler totals and the reduced singular-stratum classification were previously obtained; the claim here is their *complete age-shifted Hodge refinement*.

## Assumptions and scope
Work in characteristic zero with rational singular cohomology and its pure Hodge structure. The action is faithfully projective, \(X\) is smooth of complex dimension four, and \([X/G]\) is a smooth proper Deligne–Mumford orbifold even though \(Y\) is singular. For the signed Hodge–Deligne polynomial of a smooth projective complex \(Z\), use \(E(Z;u,v)=\sum_{p,q}(-1)^{p+q}h^{p,q}(Z)u^pv^q\). For the orbifold expression, sum \((uv)^{\operatorname{age}(g)}E(X^g/G;u,v)\) over \(g\in G\), interpreting each fixed locus with its centralizer quotient. Fractional powers are formal and reflect rational Chen–Ruan grading; this is not an assertion about Hodge numbers of a crepant resolution. No crepant resolution is claimed.

## Proof
**Invariant cohomology.** Weak Lefschetz gives \(H^0,H^2,H^6,H^8\cong\mathbb Q\) as invariant ambient classes and no odd-degree cohomology. The primitive middle cohomology is identified by Griffiths residues with \(R_{6q}\cong H^{4-q,q}(X)_{\rm prim}\) for \(0\le q\le4\), where \(R=\mathbb C[x_0,\ldots,x_5]/(x_0^5,\ldots,x_5^5)\). On the residue of monomial \(x_0^{a_0}\cdots x_5^{a_5}\), the action has eigencharacter \(\zeta^{15+\sum_{j=0}^5j a_j}\), because the projective volume form contributes determinant \(\zeta^{15}\). Consequently the invariance condition is \(\sum j a_j\equiv3\pmod6\), and \(\sum a_j=6q\) with \(0\le a_j\le4\). The exact coefficient calculation
\[
[z^{6q}t^3]\prod_{j=0}^{5}(1+zt^j+z^2t^{2j}+z^3t^{3j}+z^4t^{4j})\pmod{t^6-1}
=(0,70,290,70,0)_q
\]
follows from the six-stage recurrence in the standalone checker. It also follows by direct finite expansion, which exhausts all monomials in the finite-dimensional Jacobian ring. One hyperplane-square class contributes to \(H^{2,2}\), yielding \(291\). The action multiplies \(H^{4,0}(X)\) by \(\zeta^{15}=-1\), explaining its disappearance. The cohomology of the finite coarse quotient with rational coefficients is \(H^*(X;\mathbb Q)^G\); therefore
\[
E(Y;u,v)=1+uv+291u^2v^2+70(u^3v+uv^3)+u^3v^3+u^4v^4.
\]

**Fixed sectors and ages.** The fixed locus of \(g\) or \(g^5\) is empty, since every coordinate has a distinct eigenvalue and no coordinate vertex lies in \(X\). The fixed locus of \(g^2\), also of \(g^4\), is three projective coordinate lines (each with coordinates of equal eigenvalue), intersecting \(X\) in six points per line, so comprises \(18\) points. The residual action of \(G/\langle g^2\rangle\cong C_2\) on each such set is free, giving nine stack-sector points for each of \(g^2,g^4\). At each, the four normal eigenweights for the local order-three stabilizer are \((1,1,2,2)\), so the age is \(2\).

The fixed locus of \(g^3\) is the disjoint union of the even-coordinate and odd-coordinate plane Fermat sextics. Each is smooth of genus \((6-1)(6-2)/2=10\). On each curve the residual \(G/\langle g^3\rangle\cong C_3\) acts freely: its distinct coordinate eigenvalues would fix only projective coordinate vertices, none of which lies on the sextic. Riemann–Hurwitz makes each quotient curve genus \(1+(10-1)/3=4\). At a fixed-curve point the involution is \(-1\) on three normal directions and \(+1\) on the tangent, yielding age \(3/2\). No fixed sets intersect across the order-two and order-three strata.

**Inertia summation.** The untwisted component contributes \(E(Y;u,v)\). The two nonidentity order-three elements contribute \(9(uv)^2\) each. The unique involution contributes \(2(uv)^{3/2}E(C_4;u,v)\), where \(E(C_4;u,v)=1-4u-4v+uv\). Adding these three terms proves the displayed expression, including all degrees and all sectors. Evaluation at \(1,1\) gives \(435+18+2(2-8)=441\), independently confirmed by the commuting-pair fixed-point formula.

## Verification
Run `python3 verify.py` with Python 3 standard library. It computes the entire six-variable Jacobian monomial character distribution by exact integer dynamic programming, checks degrees, applies the fixed-locus Euler counts in Burnside and commuting-pair formulas, and verifies the Hodge and age bookkeeping. It prints `VERIFY_OK` with invariant multiplicities \((0,70,290,70,0)\), coarse Euler \(435\), and orbifold Euler \(441\). The *geometric* fixed-stratum and age arguments above, rather than the program alone, establish the formula for all terms.

## Relationship to prior work
Billi–Palomino–Sarti (arXiv:2610.21752v1, first public October 15, 2026) introduced the non-symplectic cyclic quotient and described the exceptional fixed-point behavior. An existing explicit calculation of this very quotient already determined the two genus-four singular curves, nine isolated singularities, their local types, coarse Euler \(435\), and commuting-pair Euler \(441\); these are **not** presented as new here. Braun–Fortin–Lopez Garcia–Villaflor Loyola (arXiv:2401.00470, Section 5.3 and Table 8) tabulated Hodge-invariant dimensions for diagonal automorphism groups *preserving* the holomorphic top-form, requiring sum of weights \(0\) modulo six. Our weights sum to \(15\equiv3\), so that table does not determine the Hodge action for this non-symplectic quotient. Its occurrence of the numerical pair \((70,291)\) for other groups does not supply a result for \(Y\) or the fractional sectors. The contribution is the exact global Chen–Ruan Hodge refinement, not a new orbifold-Euler calculation or a novel general orbifold-cohomology formula.

## Limitations
This computes rational graded Hodge dimensions, not the cup product, integral torsion, stringy motivic class, or a crepant resolution. In particular, nonintegral age shifts cannot be read as integral-weight Hodge numbers of an ordinary smooth variety. The statements are for the displayed diagonal order-six action only, not every order-six subgroup of the Fermat automorphism group. Exact equalities for monomial counts are independently reproducible; literature originality remains conditional on the accessible primary sources and indexed overlap records, with possible unindexed prior orbifold-Hodge calculations a residual risk.

## References
1. S. Billi, A. J. Palomino, A. Sarti, *Quotients of Calabi–Yau Generalized Fermat manifolds and Log Enriques varieties*, arXiv:2610.21752v1 (2026).
2. A. P. Braun, H. Fortin, D. Lopez Garcia, R. Villaflor Loyola, *More on G-flux and General Hodge Cycles on the Fermat Sextic*, arXiv:2401.00470v2 (2024), especially Section 5.3 and Table 8.
3. W. Chen, Y. Ruan, *A New Cohomology Theory of Orbifold*, Communications in Mathematical Physics 248 (2004), 1–31 (age-shifted orbifold cohomology).
4. P. Griffiths, *On the Periods of Certain Rational Integrals*, Annals of Mathematics 90 (1969), 460–541 (hypersurface residue description).
