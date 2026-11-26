---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The Vandermonde difference determinant gives every pair of phase ratios once. After division by a common phase, the circle-line intersection for |c_1+c_2ω^r|=|c_3| gives at most two choices of r, each with at most one s. For two zeros, equal displacement phases at precisely two sites would force the remaining coefficient to vanish; three equal phases would give zero displacement. The nullvector of the two independent equations is the cofactor triple of root differences after rephasing, so the ratio is the longest over shortest chord. For a gap >p/2 let k<p/2 be its complement. The long-gap chord over the shorter of the other chords is at least 2cos(πk/(2p))>√2; the balanced ratio is smaller than √2 for p≥11 by sin(t)/t monotonicity and directly for p=7. For gaps below p/2 sine increases strictly. Transferring one unit from a largest gap to a smallest if they differ by ≥2 strictly improves the ratio: with three gaps at least one of those extrema is unique and improves strictly. Thus the minimum gap multiset is balanced. At p=5 the only gap multisets are (1,1,3) and (1,2,2), with equal spread. Each ordered rooted minimizing triple specifies a unique displacement; for p≥7 the exceptional gap yields p admissible subsets, three through vertex 1 and six ordered rooted choices. At p=5 the respective rooted ordered count is twelve. Each admissible pair has one nonvanishing ray, and each ray has exactly two zeros, so divide the ordered-pair count by two. Taylor at π/3 gives the stated first-order term uniformly in both residues mod 3. The packaged floating-point tests are supplemental, not exact certification.

## originality

PASS

Credit the known two-zero bound and attainment, the phase-only obstruction, and earlier balanced-gap optimizers for other objectives. The supported distinct contribution is the sharp minimum dynamic range of the two-row kernel, with its all-prime equality characterization including p=5 and the corresponding ray count. The closest conditioning statement shares the p≥7 equality set and count of zero pairs after kernel identification, but does not imply minimization of the chord spread or the fifth-root exception.

## value

PASS

The ratio answers how far one must depart from equal magnitude to realize the maximum null count on a natural sparse Fourier support. It gives a sharp obstruction, constructions for every support, and a complete extremizer census with a genuine small-prime exception. The asymptotic quantifies the vanishing size of the obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
