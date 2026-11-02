# Arithmetic tangents to the nonordinary locus of a characteristic-eleven Picard family

## Finding
Let \(k=\overline{\mathbb F}_{11}\). In the smooth two-parameter family of genus-three Picard curves
\[C_{a,b}:\ y^3=x^4+a x^2+b x+1,\qquad \Delta(a,b)\ne0,\]
the nonordinary (indeed geometric \(p\)-rank-zero) divisor has just one singular point, \((a,b)=(0,0)\), in the smooth parameter base. There it has twelve smooth geometric branches crossing with distinct tangents. In the indicated affine coefficient coordinates the tangent slopes \(r=b/a\) satisfy
\[r^{12}=3.\]
Arithmetic Frobenius permutes the twelve branches with cycle lengths \((1,1,2,2,2,2,2)\). Hence there are two rational first-order nonordinary deformation directions and five conjugate pairs over \(\mathbb F_{121}\). Precisely five of the \(111\) smooth pairs \((a,b)\in\mathbb F_{11}^2\) are nonordinary: \((0,0),(4,1),(4,5),(4,6),(4,10)\).

## Assumptions and scope
The characteristic is eleven; \(a,b\) range over \(k\), except that the final enumeration ranges over \(\mathbb F_{11}\). The smoothness condition is separability of the quartic, equivalent to
\[\Delta=5a^4-4a^3b^2+4a^2+ab^2-5b^4+3\ne0.\]
All polynomial expressions and equalities in the proof are interpreted modulo eleven. The nonordinary parameter scheme is the zero locus of the explicitly defined Hasse polynomial \(H\); its ordinary twelve-fold singularity is described on its reduced support. The claimed cycle structure is for the chosen \(\mathbb F_{11}\)-model and coefficient coordinates.

## Proof
A basis of regular one-forms is \(\omega_1=dx/y^2\), \(\omega_2=x\,dx/y^2\), \(\omega_3=dx/y\). Write \(f=x^4+a x^2+b x+1\), \(c=[x^{10}]f^7\), and \(d=[x^{21}]f^7\). The Cartier operator, taking eleventh roots of the displayed scalar coefficients, acts by
\[\mathcal C(\omega_1)=(3a)^{1/11}\omega_3,\quad \mathcal C(\omega_2)=(3b)^{1/11}\omega_3,\quad \mathcal C(\omega_3)=c^{1/11}\omega_1+d^{1/11}\omega_2.\]
The coefficient identities are
\[c=-a^5-5a^4b^2+2a^3b^4-3a^3+3a^2b^2+ab^4-5a-4b^6+b^2,\]
\[d=-5a^2b-2b.\]
The stable image of the semilinear Cartier operator has dimension two if \(H=a^{11}c+b^{11}d\ne0\), and zero if \(H=0\). The rank at one iteration is two on the smooth base except at the origin, where it is zero: the possible extra vanishing points of its two blocks are on \(\Delta=0\). This proves the asserted \(p\)-ranks and \(a\)-numbers.

The polynomial \(H\) has total degree eighteen and its initial ordinary homogeneous part at the origin is
\[-5a^{12}-2b^{12}.\]
Its twelve tangent directions therefore satisfy \(r^{12}=3\). These roots are distinct because eleven does not divide twelve; hence the germ is an ordinary twelve-fold point and each direction determines exactly one smooth geometric branch.

To exclude other singular points on the smooth base, eliminate from \((H,\partial_aH,\partial_bH)\). An exact lexicographic Gröbner basis contains \(b^{11}(b^4-3)^{11}\), \(b(a+4b^2)^{11}\), and the specialization at \(b=0\) forces \(a^{11}(a^2-4)=0\). Direct substitution gives the complete geometric critical support: \((0,0)\), \((\pm2,0)\), and \((a=-4b^2,b^4=3)\). All points outside the origin in this support satisfy \(\Delta=0\). Thus the nonordinary curve is smooth away from the origin in the smooth parameter base, and is geometrically reduced there and at the ordinary multiple point.

For any root \(r\) of \(r^{12}=3\), arithmetic Frobenius gives \(r^{11}=3/r\), hence its square fixes \(r\). The fixed points of Frobenius have \(r^2=3\), yielding exactly two elements of \(\mathbb F_{11}\); the remaining ten form five two-cycles. Exhaustively evaluating \(\Delta\) and \(H\) on the \(121\) elements of \(\mathbb F_{11}^2\) leaves \(111\) smooth pairs, of which precisely the five listed in the finding have \(H=0\).

## Verification
The accompanying standalone Python program `verify.py` uses exact coefficient arithmetic, finite-field enumeration, and Gröbner bases over \(\mathbb F_{11}\). Run `python3 verify.py` with `sympy==1.14.0`. It asserts the Cartier coefficients, the degree and initial form of \(H\), its complete geometric critical support, the rank conditions, the five enumerated rational parameters, and the Frobenius cycle decomposition. Its final line is `VERIFY_OK`. Computational identities here are over explicit finite polynomial rings; the infinite geometric statements additionally use the elimination and ordinary-multiple-point arguments above.

## Relationship to prior work
Superspeciality of the Fermat Picard quartic in characteristic eleven was previously known. The universal theorem that the supersingular locus on an appropriate inert Picard modular surface has \(p+1\) transverse geometric branches at a superspecial point was also previously known. This is **not** a new claim of twelve-branch geometry in abstract moduli. The present arithmetic contribution is the explicit equation and Frobenius descent of the tangent branches in this fixed coefficient slice, and the exhaustive \(\mathbb F_{11}\)-parameter classification. It is a concrete twist-sensitive calculation not supplied by the geometric local-normal-form statement alone. Earlier general Cartier formulas also cover the underlying coefficient-extraction technique. A complete historical-priority proof is not claimed.

## Limitations
This result does not classify all Picard curves or the whole Picard modular surface. The normalized coefficient family is a two-dimensional slice, not a fine moduli space, and two coefficient pairs can represent isomorphic curves. The tangent arithmetic refers to this specific rational slice. The 1991 Jacobian study was available through bibliographic and abstract information, not its full text; it may contain related specializations, so a historical-priority risk remains. No independent scientific audit is asserted.

## References
- E. de Shalit and E. Z. Goren, *A theta operator on Picard modular forms modulo an inert prime*, first posted December 17, 2014; https://arxiv.org/abs/1412.5494.
- E. de Shalit and E. Z. Goren, *Supersingular curves on Picard modular surfaces modulo an inert prime*, first posted July 14, 2016; https://arxiv.org/abs/1607.04170. In particular, the local \(p+1\)-branch theorem.
- A. Kazemifard and S. Tafazolian, *A note on some Picard curves over finite fields*, Finite Fields and Their Applications 34 (2015), 107–122, DOI 10.1016/j.ffa.2014.12.002; Fermat superspeciality is prior art.
- J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic p > 0*, Manuscripta Math. (1991), DOI 10.1002/mana.19911520125. Full text not available in this investigation.
- V. Nourozi and F. Rahmati, *The Rank of the Cartier Operator on Picard Curves*, 2023; https://arxiv.org/abs/2306.07823. General Cartier coefficients are prior art.
