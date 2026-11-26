---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Putting t=x², the branch polynomial divided by t² is Q(t+t⁻¹) with Q(z)=z²+az+b-2. Since no root t is zero and t→t+t⁻¹ ramifies only over z=±2, Q must have distinct roots and avoid those two values. Disc(Q) and Q(±2) give exactly the three excluded factors in characteristic 5. The coefficients of f² at degrees 2,4,8,12,14 give the indicated 3-by-3 matrix: the 4 and 12 entries are a²+2b, 2 and 14 are 2a, and 8 is b²+2a²+2. Its ± basis on the outer indices and its middle vector are defined over F_5; thus every nonzero Hasse scalar stays nonzero under the twisted iterations and both rank formulas follow. Eliminating b via H_+=0 gives b=2a²+4a and H_0=4(a-1)³(a+2), with the symmetric formula for H_-. The triple intersections in the eliminant sense are at excluded boundary points; the other roots are simple, so the two smooth divisors cross transversally at each surviving point. H_+ and H_- cross at (0,0) with independent gradients, and H_0 there is nonzero. This also verifies there is no point with three vanishing factors. The Newton rows follow independently of the isogeny citation: rank is at least one, leaving at most four slopes between 0 and 1; any non-half slope and its dual require total multiplicity at least six. For counts, the three boundary graphs have q points each, three rational pairwise crossings and no triple point. On H_+, the boundary parabola and one boundary line give only (1,1), and the other line gives a²+a+1=0. H_- follows by a→-a. On H_0 insertion of the boundary parabola gives (a²-1)², while the lines give (a±1)², so only (±1,1) are lost in the affine chart. At infinity the smooth projective conic loses two points exactly when 3 is a square, i.e. in even extension degree, the same parity as square discriminant 2 for the other two intersections. Hence each retained divisor has q-1-2δ_n points. Subtract the three rational crossing points twice from the divisor incidence count to count points on precisely one divisor, then subtract from |U|. This establishes the three formulas for marked pairs in every extension.

## originality

PASS

Pass for the combined stratification with the exact all-extension marked census. The equation and quotient setup are not new; the same rank strata and rank-one points are covered in a distinct indexed record, which additionally compares the curves up to geometric isomorphism. The inspected matching claims do not give the parity-dependent marked counts for arbitrary extensions. The assessment credits the geometric overlap without inferring priority solely from dated paths.

## value

PASS

On a standard genus-three reciprocal Howe family, the rank strata are described by an explicit transverse Hasse-divisor arrangement and an exact marked census. The parity correction pinpoints field-of-definition effects invisible in a geometric census, and gives a reproducible benchmark for the frequency of ordinary and mixed-slope behaviors over every extension. This is material arithmetic information even after crediting the prior geometry and the isomorphism of the rank-one fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
