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

Averaging the conjugates over coordinate and alphabet permutations preserves all constraints and cannot increase the norm, so the orbit-invariant optimum is global. Tensor characters with k nontrivial factors give normalized eigenvalues by averaging a product of one or two factors chosen from d-k copies of 1 and k copies of -1/u. The resulting spectrum includes every nonconstant mode. For d=2 uniform on all vertices is feasible and unique. For d=3 the quadratic identity 1=3λ1-3λ2+λ3 gives μ≥1/7 with unique equality contacts (1,-1,1)/7, and the corresponding masses are feasible through q=4. For q≥5, λ1≥1-2q/(3u)>0, with equality only at b=1, and the two remaining absolute eigenvalues (2u-1)/(3u²) and 1/u² are smaller. For binary d≥4, λ1≥1-4/d+2a/d and λd=1-2a; intersecting the bounds gives the unique invariant candidate and the centered quadratic λk shows that no intermediate negative eigenvalue exceeds the contact modulus. For nonbinary d≥4, λ1≥1-2q/(du)>0 with equality only at b=1. At b=1 the convex quadratic has maximum at an endpoint and F2(d)=1/u²≤F2(1). Its minimum is bounded below by -1/(d-1) via the square-minus-squares form for d≥5; the listed four values verify the d=4 cases, including the tie when q=3. Radius-one endpoint balancing gives exactly half the optimal absolute spectral gap, with averaging valid there as well. Phase statements are understood in the indicated invariant family, not as a claim that every unrestricted optimizer is uniform.

## originality

PASS

Credit the standard FMMC formulation, automorphism averaging, Hamming spectra, radius-one baseline, trivial complete-graph case, and the binary reduction to the known edge-transitive formula. The scientifically distinct part supported by this review is the nonbinary radius-two minimax phase diagram and its gap consequence, within the complete classification. The materially matching later catalog records are explicit overlap, not proof of prior coverage of the October finding.

## value

PASS

Allowing the next Hamming radius is a natural change to a canonical mixing graph. The exact minimax result identifies which transitions and holding are beneficial and quantifies the SLEM-gap gain. In three dimensions the interpolation contacts and feasibility cutoff explain why distance-one moves and then holding disappear at different alphabet sizes. That boundary information is not a trivial restatement of symmetry or of the existing distance-one optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
