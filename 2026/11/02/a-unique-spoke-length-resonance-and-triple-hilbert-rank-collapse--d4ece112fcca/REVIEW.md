# Scientific assessment

## Correctness — PASS

For every integer \(n\ge4\) and common spoke length \(1/2\le t\le1\), the shortest-path distance takes only the three specified nonzero values. The zero-sum powered-distance form splits exactly into a scalar radial coefficient \(F_n(p,t)=2+(n-3)(2t)^p-2nt^p\) and Fourier sectors of the rim cycle. The latter have maximal eigenvalue \((2c_n-1)(2t)^p-2c_n\), of multiplicity one on even rims and two on odd rims. Strict monotonicity of the radial coefficient with exponent and opposite monotonicity of the two first-zero thresholds give a single simultaneous crossing. Solving their two equations gives the exact parameters; rank-nullity of the Schoenberg Gram matrix gives the claimed critical Euclidean dimensions. These arguments work for every real exponent and length in the stated range, not just enumerated samples. Independently built weighted Dijkstra distances were checked against the derived formula; 600 exact rational quadratic-form identities and 36 numerical transition signatures were checked using the standalone checker. The finite checks corroborate rather than prove the universal claim.

## Originality — PASS, with residual risk

Buckley and Harary (1988), despite the closely related title, study graph edge-unit-distance realizations rather than isometric embedding of the weighted all-pairs geodesic metric. The closest same-object literature concerns unweighted ordinary wheel distance matrices (Balaji, Bapat and Goel, arXiv:2006.02841), and generalized distance spectra of graph joins, including unweighted wheels (Alhevaz et al., DOI:10.3390/sym12010169). These do not explicitly derive the unique continuously weighted spoke-length crossing or parity-dependent multiplicity of the critical negative-type kernel in the material inspected. Li and Weston (arXiv:0901.0695) and Sánchez (arXiv:1108.0451) give general negative-type methods, not this classified wheel deformation. A separate unweighted wheel classification already covers the \(t=1\) boundary and is **not** asserted as new. The originality claim is limited to the evaluated weighted two-mode resonance, exact transition length and multiplicity result. Publisher text for the graph-join spectrum paper could not be inspected completely, and an equivalent derivation from its methods or unindexed sources remains possible.

## Mathematical value — PASS

A wheel is the minimal cyclic-spoke deformation of a star with a uniform, geometrically meaningful length parameter. Radial and rim Fourier modes are competing structural negative-type obstructions. The theorem finds a unique resonance where they fail simultaneously, and determines its sharp embedding-dimension drop by two for even rims and three for odd rims. The exact length and exponent formulas, universal two-mode phase classification and parity effect describe an entire natural family and are not single-instance computations.

## Limits

The proof does not address spoke lengths outside \([1/2,1]\), unequal spokes, electrical resistance, or publication priority in unindexed literature. Numerical checks do not independently certify the theorem for infinitely many orders or arbitrary real lengths.

Self-review: passed. Independent audit: not yet performed.
