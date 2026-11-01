# Independent mathematical audit

## correctness

PASS

For a Hermitian 3x3 K, Q_K(z)=[1,z,z^2]^*K[1,z,z^2] restricts to a real quartic on each horizontal line, whose x^4 and x^3 coefficients are identical across heights (c,2w). Four distinct zeros per line force the restrictions to be c times their corresponding monic quartics. Equality of cubic coefficients gives c*(sum r - sum s)=0. If the sums differ, c=0 and both restricted cubics vanish identically, leaving a one-dimensional real kernel spanned by H_h with determinant 2. A rank<=2 nonzero kernel is therefore impossible. If sums agree, the linear restrictions yield an independent kernel K1 with c=1; det(K1+tH_h) is an odd-degree real cubic with nonzero leading coefficient 2, hence has a real zero at a nonzero singular kernel matrix. Three distinct sample functionals span C3 by Vandermonde, excluding semidefinite nonzero kernel matrices; the singular element is indefinite rank2 and gives two genuinely distinct phaseless polynomials. Independent SymPy verification gives detH=2 and sample linear ranks 8/7 for unequal/equal centroids. The general minimality at N=8 uses Conca et al Proposition 5.4 with M=3,N<=7.

## originality

PASS

Best-of-knowledge sharp eight-node centroid criterion is not implied by general complex frame phase retrieval, arbitrary polynomial grid constructions, or uniqueness from measurements on entire lines. Minimal count and Hermitian lifting are inherited prior theory and are not credited as new. The exact necessary-and-sufficient geometric condition on a finite 4+4 parallel-line configuration is the surviving contribution.

## value

PASS

Eight is the sharp possible sample count for C3 and the centroid condition is a clean complete classification of every 4+4 parallel-line configuration, including exceptional degeneracies, with an explicit counterexample mechanism. It supplies concrete constrained sampling design beyond generic-frame existence or a large grid method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
