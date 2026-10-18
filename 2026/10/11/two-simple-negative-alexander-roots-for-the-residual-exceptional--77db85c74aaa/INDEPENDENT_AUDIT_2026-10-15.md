# Independent mathematical audit

## correctness

PASS

PASS on the fully supplied corrected RESULT.md: for odd m≥3 and a=2m−1, the monic Alexander representative satisfies e^(−ax) Delta_a(−e^x)=[sinh(mx)/sinh(x/2)]²−1−4m²cosh²(x/2). The frozen original erroneously had an extra minus in front of e^(−ax); directly substituting x=0 and evaluating Delta_a(−1)=−1 diagnoses it. The repaired identity is verified symbolically (also by Git blob comparison). For x>0, sinh(mx)/(m sinh x) strictly increases from 1 and its required comparison B_m decreases, hence the only negative roots are one simple reciprocal pair. Rescaling z=m²x/2 and applying a simple-root implicit-function expansion yields x_m=√3/(2m²)+9√3/(40m⁴)+O(m⁻⁶). mpmath root solving at odd m=3..101 independently corroborates the residual scaling; it is not the proof of the infinite claim.

## originality

PASS

The older complete exact-real-root theorem covers the existence, uniqueness, negativity, simplicity and reciprocity of the pair for every odd a≥3. It does NOT state or imply the new quantitative two-term logarithmic root-location asymptotic by mere specialization. The surviving asymptotic is a genuine original refinement, with disclosed qualitative prior coverage.

## value

PASS

PASS. The exceptional determinant-one pretzel family has a natural Alexander polynomial whose real-root geometry is relevant to knot invariants. The quantitative m^-2 logarithmic collapse and next coefficient measure how two known reciprocal roots coalesce at −1 across the infinite family, information absent from the stronger qualitative root-count theorem. Not a mere numeric slice or arbitrary reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
