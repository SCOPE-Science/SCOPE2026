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

Summing the shift autocorrelations gives T²=(3+S)/3. Odd extension degree excludes a quadratic subfield and hence forces T rational; a reduced denominator s would satisfy s²|3, so T is integral. S=3(T²−1) is odd with |S|≤17; T must be even, leaving 0 or ±2 and respectively seven or thirteen positive signs. The symmetric circulant Gram spectrum has constant mode T² and paired modes k,35−k with 3λ_k=3+∑σ_a cos(2πka/35). For nonzero k, the full root sum gives the equivalent 3λ_k=7/2+2∑_(a∈P) cos(2πka/35), also for nonunits. Independently replayed all combinations with python3 /workspace/replay/shift35_review.py, using alternating arctangent brackets for π, a rational Taylor bound plus cosine's Lipschitz bound, and outward rounding at scale 10^18. The 19,448 and 2,380 candidates gave 19 and zero survivors with no ambiguous signs. The 19 have λ₀=0 and all other λ_k≥67924701873905317/1500000000000000000, exceeding the frozen common bound. Independent orbit grouping verified disjoint sizes 12,3,4 and the three frozen representatives. Real shift-only realizability follows by Fourier inversion of the symmetric coefficients sqrt(λ_k), with the forward transform unnormalized and inverse divided by 35; this gives the autocorrelation and squared norm one. It does not realize a prescribed field degree or impose any nonzero modulation equation. The bundled rational code at verification/spectral_census.py was inspected, not executed; its positive-definite print label means strict positivity on the nonconstant subspace for survivors, not on the whole space.

## originality

PASS

The distinct claim is the complete dimension-35 shift PSD census and resulting exclusion of T=±2 under the necessary field-degree restriction, not the general sign identity, odd-degree dimension criterion, circulant diagonalization, or spectral factorization. The strongest inspected primary passages supply the general restrictions but not the finite classification. Neither the local catalogue comparisons nor the searched primary passages establish covering evidence for this census. This is a bounded judgement, not a priority guarantee.

## value

PASS

Dimension 35 is the first dimension above three admitted by the stated odd-degree necessary sieve, making it a motivated exact instance. Reducing 21,828 discrete possibilities to three multiplier templates and ruling out the nonzero sum branch gives a usable, exact constraint for further fiducial or sign-subsystem work. The classification is complete for the stated real shift-only PSD relaxation; its value does not depend on claiming full WH realizability or nonexistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
