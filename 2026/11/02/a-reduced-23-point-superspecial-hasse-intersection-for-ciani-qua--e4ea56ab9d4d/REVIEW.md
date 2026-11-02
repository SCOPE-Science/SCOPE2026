# Self-review

## Correctness — PASS
The claim concerns the saturated Hasse-vanishing scheme on the smooth three-parameter coefficient space, not the full moduli stack. Smoothness is governed by the displayed discriminant; the three elliptic quotient equations follow by completing a square, and in characteristic seven the relevant quartic Hasse coefficient is \(B(B^2-AC)\). The known degree-two quotient isogeny has degree prime to seven, so all three elliptic curves supersingular is equivalent to the genus-three Jacobian being superspecial.

The saturated lexicographic Gröbner basis was recomputed from the actual formulas. Its initial ideal has exactly 23 standard monomials. Direct exact arithmetic over \(\mathbb F_{49}\) identifies 23 distinct smooth points partitioned into four claimed symmetry orbits and finds nonzero Jacobian determinants at all 23. Length 23 plus 23 distinct points proves there are no additional geometric points or embedded multiplicities. This establishes the stated finite étale and transversality results. The attached scripts reproduce both critical checks.

## Originality — PASS, with a significant historical-priority limitation
Known ingredients are separated from the new claim. Lercier–Ritzenthaler–Rovetta–Sijsling describe the parameter family and its symmetry group; Ohashi provides the smoothness, elliptic quotients, prime-to-characteristic isogeny, and theorem that all smooth superspecial Ciani coefficients belong to the quadratic extension. The latter rationality fact is **not** claimed as new. Ohashi explicitly attributes studies of superspecial Ciani curves and enumerations to Brock's 1993 thesis, which was not fully accessible. This prevents an unqualified priority claim about the number of curves or coefficient triples.

The independent mathematical target here is the **scheme structure** of the simultaneous three-Hasse-zero locus: degree 23, geometric reducedness and transverse intersection in the normalized smooth coefficient space. These are not logical consequences of the published rationality theorem, geometric isomorphism-class counts, or the known elliptic-quotient decomposition. The inspected primary material does not state the identical characteristic-seven scheme computation. A specialized earlier scheme calculation may cover it; that residual risk remains explicit. No independent literature certification has occurred.

## Value — PASS
The three quotient Hasse divisors are natural arithmetic divisors on a classical three-dimensional genus-three family. Their intersection multiplicities quantify how superspeciality imposes infinitesimal conditions and are not captured by counting isomorphism classes or rational points. Showing the intersection is everywhere transverse and computing its degree gives an exact finite enumerative geometry result with reproducible evidence and potential use in deformation and arithmetic-moduli comparisons. Four explicitly described parameter-symmetry orbits also make the result interpretable without conflating coefficient triples and isomorphism classes.

## Scope and residual risks
The characteristic is exactly seven; \(\Delta=0\) is excluded. The four orbits are for the specified parameter subgroup, not for all projective changes of coordinates. Brock's original thesis was cited but could not be fully read, so overlap with uninspected historical calculations cannot be ruled out. The checks are reproducible self-review computations, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
