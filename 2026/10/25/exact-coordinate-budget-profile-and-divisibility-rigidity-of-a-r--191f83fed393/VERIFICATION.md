---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Coordinatewise extreme-point argument reduces vector suprema to r phases. On the circumference-pi lattice, any cluster of k columns has maximal contribution 2 sin(k pi/(2n))/sin(pi/(2n)), since the best k distances to one phase occur at k cyclic consecutive vertices and a midpoint phase attains the cosine sum. The maximum over all coordinate assignments is the maximum over integer partitions of n into at most r positive block lengths; sine is strictly increasing and concave here, so all s=min(r,n) coordinates are used and lengths differ by at most one. Consecutive balanced blocks realize all per-block upper bounds simultaneously. This yields exact formula, r=1 and r>=n boundary values, Jensen equality iff r|n for r<=n, and the explicit O_r(n^-3) Taylor residue deficit. An independently coded DP over all compositions plus explicit phase evaluation checked all 234 pairs 2<=n<=28, 1<=r<=min(n,10), including equality strictness. No finite grid substitutes for global continuous phase analysis.

## originality

PASS

The full accessible Santos–Serrano-Rodríguez 2026 paper Section 4 establishes the sharp MATRIX-UNIFORM complex two-row rectangular constant, and Remark 4.11 explicitly computes only n=3,r=2 of the same Fourier row family. The full pointwise n,r Fourier budget profile, balanced-block attainment for every n,r, and iff-divisibility gap are not stated or implied by merely taking the supremum over arbitrary matrices in their Proposition 4.6. Related Ambrus–Grundbacher signed planar sum work is one-center and does not produce multi-coordinate pointwise saturation. No Resultary indexed result matched the full profile. Priority remains qualified for possible circular quantization/facility-location aliases.

## value

PASS

The exact pointwise budget profile reveals which regular Fourier matrices attain the sharp global rectangular constant and quantifies strict arithmetic near-attainment by residue class. This is not just the known universal constant: fixed matrix, r budget, optimal block geometry, integer divisibility, and leading finite-grid deficit are new specific questions induced by that theorem, and provide an exact benchmark for endpoint tensor norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
