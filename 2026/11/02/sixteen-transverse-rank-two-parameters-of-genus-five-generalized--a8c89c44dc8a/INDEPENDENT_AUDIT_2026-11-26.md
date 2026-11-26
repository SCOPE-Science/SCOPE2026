# Independent mathematical audit

## correctness

PASS

On U both degree-six branch polynomials are squarefree, their common branch set consists of the four roots of x⁴−1, and their other four branch points are distinct. Infinity is unramified. The connected degree-four biquadratic cover has inertia two at each of the eight branch points (at a common branch point the two local quadratic covers coincide); Riemann–Hurwitz gives 2g−2=−8+8·2=8. The three involution quotients have genera 2,2,1, the third given by z²=Q_u Q_v. Their Jacobians split the genus-five Jacobian by a 2-power isogeny, so the characteristic-eleven torsion and numerical invariants are read additively. The independent coefficient replay (`cd /workspace && python3 audit-evidence/howe11.py`, SymPy) verifies the Cartier matrix and determinant 3(w²−3)²(w²−4)³ in F₁₁[w]. The matrix is invertible off w=5,6 on U and zero there; taking Frobenius roots of coefficients in the semilinear Cartier action does not affect that dichotomy or the stable ranks. The elliptic block vanishes iff H vanishes. The replay verifies the two quartics H(5,v) and H(6,v), symmetry, squarefreeness, nonvanishing at the excluded or other special parameters, and the irreducibility of the respective quadratic factors over F₁₁. This proves all four line restrictions have four simple roots in U and never meet at a point on two special lines; the nonzero restricted derivative proves transversality. Each line contributes two rational and two quadratic geometric points, giving a degree-16 finite étale intersection scheme. It is the rank-two locus as a set with its stated reduced structure, not a determinantal scheme claim. H(5,6)=4 leaves two swapped rank-one parameters and no rank zero. The five exhibited rank witnesses give H-values 4,0,4,0,7 in order. This verify-by-coefficients argument applies over the algebraic closure, rather than inferring exhaustion from a finite field sample.

## originality

PASS

Credit the characteristic-eleven incidence analysis of the rank-two locus: exhaustive line intersections in the ordered open chart, their multiplicities and splitting over the ground field. The symmetric family, prime-to-characteristic decomposition, criterion for special genus-two factors, and method of computing rank from elliptic factors are not new. The rank-one and rank-zero cases are low-cost specializations of those general criteria once the one remaining elliptic coefficient is evaluated; they are not independently decisive for this pass.

## value

PASS

Characteristic eleven is a concrete characteristic with known superspecial genus-five examples in the broader Howe setting. In the symmetric chart, the rank-two points form the finite rank-drop locus where one genus-two factor loses two ranks and the remaining elliptic quotient simultaneously loses one. Knowing this locus exactly, with simple intersections and residue degrees, determines the low-rank incidence and the extension fields needed to realize its points, rather than just supplying examples. This naturally motivated exact stratum is valuable even though the decomposition is standard and the computation is finite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
