# Same-model review

## Correctness
PASS. The proof reduces the pedal simplex to the translated vertices \(-d_i u_i\), expands the augmented affine-volume determinant, identifies the normal-matrix cofactor vector with the facet-area kernel vector, and computes the common scale from barycentric-coordinate gradients. The coefficient has been independently replayed numerically for random simplices in dimensions \(2\) through \(6\). The vertex multiplicity argument uses independent local facet-distance coordinates and has a nonzero degree-\(n-1\) initial form.

## Originality
PASS, with explicit historical risk. Targeted published-finding corpus searches for “pedal simplex volume facet distances exact formula,” “pedal degeneracy hypersurface simplex,” “tetrahedron pedal plane cubic surface volume formula,” and “signed distances facets pedal simplex volume” returned no matching finding; the closest results concern unrelated simplex volume profiles, simplex sections, and tetrahedral Ptolemy slack. Grace (1927) covers the qualitative tetrahedral cubic coplanarity locus; Yang (2004) and Yang--Cheng (2006) cover pedal-simplex inequalities. The accessible 2006 full-text transcription does not state this exact formula. Grace's full text was not available, so the review does not claim novelty for the mere n=3 cubic equation.

## Value
PASS. The formula gives a direct computable invariant for arbitrary simplices and arbitrary points, identifies the complete pedal-degeneracy locus in every dimension, recovers the planar Simson phenomenon and the tetrahedral cubic as low-dimensional cases, and supplies the exact vertex multiplicities. This is a structural identity rather than a routine numerical refinement of an existing inequality.

The main residual risk is historical terminology: an equivalent determinant identity could exist in older work on pedal simplices or barycentric/trilinear coordinates. That risk is recorded in AUDIT.json and VERIFICATION.md.

Same-model review: passed. Independent audit: not yet performed.
