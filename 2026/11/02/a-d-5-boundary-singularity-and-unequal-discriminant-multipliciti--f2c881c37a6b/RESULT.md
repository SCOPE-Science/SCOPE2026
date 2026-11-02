# A \(D_5\) boundary singularity and unequal discriminant multiplicities for the characteristic-five Picard rank-zero surface

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\). For the coefficient-marked Picard quartics
\[
C_{a,b,c}:\quad y^3=x^4+a x^2+b x+c,
\]
put
\[
A=c^2+a^2c+ab^2,\qquad H=V(A)\subset\mathbb A^3_{a,b,c},
\]
and let \(\Delta=\operatorname{disc}_x(x^4+ax^2+bx+c)\). The following statements hold **as geometric statements over \(k\)**:

1. The reduced closure in the coefficient space of the smooth-fiber Jacobian \(5\)-rank-zero locus is precisely \(H\). The smooth-fiber part is \(H\cap\{b\ne0\}\). Every other smooth fiber has \(5\)-rank \(2\); all smooth fibers have Jacobian \(a\)-number \(1\).
2. The surface \(H\) is geometrically integral and normal, and its only singular point is the origin. There the hypersurface germ has the exact \(D_5\) rational-double-point normal form
\[
z^2+ab^2+a^4=0,\qquad z=c+3a^2.
\]
3. If \(L_0=V(b,c)\subset H\) and \(L_1=V(b,c+a^2)\subset H\), then the **Weil divisor** cut out by the quartic discriminant on the normal surface \(H\) is
\[
\boxed{\operatorname{div}_{H}(\Delta)=6L_0+2L_1.}
\]
In particular, the discriminant meets \(H\) set-theoretically only in these two rational curves, with unequal orders of vanishing \(6\) and \(2\). The open rank-zero locus is a nonempty smooth geometrically irreducible surface.

The new content assessed here is the geometry and intersection multiplicities of this naturally defined coefficient-space rank-drop surface. The known general Cartier–Manin methods and the auxiliary \(a\)-number value are not claimed as new.

## Assumptions and scope

The base is an algebraically closed field of characteristic \(5\). A coefficient triple is *smooth* exactly when \(\Delta\ne0\), since the degree-four right-hand polynomial must be squarefree. Smooth compactifications of these affine models are genus-three Picard curves. The coefficients are marked: the statements concern the displayed affine parameter space, **not** a claim that distinct triples give nonisomorphic curves. The divisor equation is on the complete reduced surface \(H\), including its singular vertex, with Weil multiplicities computed at generic codimension-one points. It is not a claim about a stable moduli-space compactification.

## Proof

**1. Cartier computation and identification of the geometric locus.** A basis of regular differentials for a smooth curve is
\[
\omega_0=dx/y^2,\qquad \omega_1=x\,dx/y^2,\qquad \omega_2=dx/y.
\]
Writing \(f=x^4+ax^2+bx+c\), the characteristic-five Cartier rule for monomials gives
\[
\mathcal C(\omega_0)=\omega_2,\quad \mathcal C(\omega_1)=0,\quad
\mathcal C(\omega_2)=(3A)^{1/5}\omega_0+(3b)^{1/5}\omega_1.
\]
Indeed, the only relevant coefficients in \(f^3\) are \([x^4]f^3=3(c^2+a^2c+ab^2)\) and \([x^9]f^3=3b\), reduced modulo five. The first formula follows separately from \([x^4]f=1\). The Cartier action is inverse-Frobenius-semilinear; the indicated roots exist uniquely in the perfect field \(k\).

If \(A\ne0\), Cartier is invertible on the two-dimensional quotient by the killed line \(k\omega_1\), so its stable image has dimension two. If \(A=0\), it is nilpotent of index at most three, hence has stable image zero. This proves the stated \(5\)-rank dichotomy. Its rank is two on every smooth fiber once we show that \(A=0\) and smoothness imply \(b\ne0\); consequently the \(a\)-number is one.

**2. Exact discriminant restriction.** Direct quartic resultant calculation gives, in characteristic five,
\[
\Delta=c^3+2a^2c^2+a^4c-ab^2c+a^3b^2-2b^4
\]
and the exact polynomial identity
\[
\boxed{\Delta=(a^2+c)A-2b^2(ac+b^2).}\tag{1}
\]
On \(H\) we also have
\[
a(ac+b^2)=-c^2.\tag{2}
\]
Thus a point of \(H\) with \(\Delta=0\) and \(b\ne0\) would satisfy \(ac+b^2=0\). Equation (2) then forces \(c=0\), which contradicts \(b\ne0\). Conversely \(b=0\) makes \(\Delta=0\) by (1). Consequently
\[
H\cap\{\Delta=0\}=H\cap\{b=0\}=L_0\cup L_1
\]
set-theoretically, since \(A|_{b=0}=c(c+a^2)\). This also proves the smooth rank-zero locus is exactly \(H\cap\{b\ne0\}\). For example, \((a,b,c)=(0,1,0)\) lies in it.

**3. The unique \(D_5\) singularity.** Put \(z=c+3a^2\). A calculation modulo five transforms \(A\) *exactly*, not just to initial order, into
\[
A=z^2+ab^2+a^4.
\]
This is the standard \(D_5\) hypersurface form in characteristic different from two. Its derivatives are \(2z,2ab,b^2+4a^3\). They vanish simultaneously only at \((a,b,z)=(0,0,0)\). To establish geometric integrality directly, regard the equation as quadratic in \(z\). Its prospective square factor has square \(-a(b^2+a^3)\), which has odd valuation at the prime \((a)\) in \(k(a,b)\); hence the quadratic is irreducible over \(k(a,b)\), and the defining polynomial is absolutely irreducible. The hypersurface is Cohen–Macaulay and regular in codimension one, hence normal.

**4. The scheme-theoretic boundary divisor.** On the dense chart \(a\ne0\), combining (1) and (2) gives the equality of functions on \(H\)
\[
\Delta=2b^2c^2/a.\tag{3}
\]
At the generic point of \(L_0\), \(a\) is invertible, \(c=0\), and \(\partial A/\partial c=a^2\ne0\). Thus \(b\) is a uniformizer and the implicit equation \(c^2+a^2c+ab^2=0\) implies \(\operatorname{ord}_{L_0}(c)=2\). By (3), \(\operatorname{ord}_{L_0}(\Delta)=2+2\cdot2=6\). At the generic point of \(L_1\), \(c=-a^2\) is a unit and \(b\) is again a uniformizer, so \(\operatorname{ord}_{L_1}(\Delta)=2\). There are no further codimension-one zeros by the set-theoretic argument in part 2. Since \(H\) is normal, these generic orders determine the complete Weil divisor, proving the asserted \(6L_0+2L_1\) formula.

## Verification

Run `python3 verify_symbolic.py` and `python3 verify_primefield.py` with Python 3 and SymPy installed. The symbolic program verifies the relevant Cartier coefficients, exact discriminant identity, \(D_5\) change of variables, and the resultant \(\operatorname{Res}_c(A,\Delta)=-b^8\). The independent prime-field script constructs the Cartier coefficient matrix afresh, computes its third iterate and linear-algebra rank directly for every coefficient triple over \(\mathbb F_5\), and independently checks squarefreeness by the Euclidean algorithm. It counts \(84\) smooth rank-two curves, \(16\) smooth rank-zero curves, and \(25\) singular quartics; every smooth curve has \(a\)-number one. These finite checks support, but do **not** replace, the geometric proofs above.

## Relationship to prior work

Bouw–Koutsianas–Sijsling–Wewers, first publicly posted February 25, 2019, develop quartic Picard normal forms and discriminants; their project concerns models and arithmetic conductor/discriminant, not the reduced characteristic-five rank-drop surface and its intrinsic \(D_5\) point. Nourozi–Rahmati, first publicly posted June 13, 2023, give a general Cartier-matrix framework and an \(a\)-number assertion for Picard curves, so neither the general matrix method nor the value \(a=1\) is claimed as original. Their examined Section 3 does **not** state the special coefficient-space divisor \(\operatorname{div}_H(\Delta)=6L_0+2L_1\), the isolated \(D_5\) germ, or its smooth geometric rank-zero complement.

Estrada-Sarlabous (1991) develops general ordinary/supersingular tests for Picard Jacobians; its accessible abstract makes it a plausible antecedent for the rank calculation, but the full article could not be inspected. Kazemifard–Tafazolian (2015) analyze Newton polygons for particular Picard curves, not visibly this three-parameter boundary. Those uninspected and unindexed sources leave a specific priority risk for the boundary result. Mere absence of search hits is not a proof of novelty.

## Limitations

This work classifies only the displayed **coefficient-marked characteristic-five** family. The singular vertex represents a singular quartic, not a smooth Jacobian. The \(D_5\) type and multiplicities belong to this coefficient surface and its quartic-discriminant intersection, not to an unspecified compactification or quotient by coordinate changes. The computation does not determine geometric isomorphism classes, full Newton polygons, conductors of degenerations, or characteristic other than five. No independent mathematical audit has been performed.

## References

- I. I. Bouw, A. Koutsianas, J. Sijsling, S. Wewers, *Conductor and discriminant of Picard curves*, arXiv:1902.09624 (first posted 2019-02-25), https://arxiv.org/abs/1902.09624 ; *Journal of the London Mathematical Society* **102** (2020), 368–404, DOI 10.1112/jlms.12323.
- V. Nourozi, F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, arXiv:2306.07823 (first posted 2023-06-13), https://arxiv.org/abs/2306.07823 ; *Discrete Mathematics, Algorithms and Applications* **17** (2025), 2450028.
- J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic \(p>0\)*, *Mathematische Nachrichten* **152** (1991), 329–340, DOI 10.1002/mana.19911520125 (full text not inspected).
- A. Kazemifard, S. Tafazolian, *A note on some Picard curves over finite fields*, *Finite Fields and Their Applications* **34** (2015), 107–122, DOI 10.1016/j.ffa.2014.12.002 (accessible abstract and portions of introduction).
