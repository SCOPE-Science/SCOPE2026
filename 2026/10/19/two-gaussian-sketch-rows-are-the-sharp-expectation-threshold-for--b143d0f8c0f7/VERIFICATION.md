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

On the two-dimensional column span the sketch difference form aaᵀ−bbᵀ has trace δ and determinant −h. Its positive and negative eigendirections give independent χ²_s variables by Gaussian rotation, and the negative difference event is a symmetric beta lower tail at the stated x. Schur complements give the two projection losses h/α and h/β and the optimal loss h/Λ. At fixed unequal column norms, x increases strictly as the absolute correlation decreases, giving the sharp orthogonal maximum and collinear infimum. On [0,1/2] the beta tail decreases with s: folding about 1/2 gives a density ratio decreasing in distance from the center for larger s, hence a smaller folded upper tail. Thus p_s≤x≤β/(α+β) for s≥2, yielding E_s≤2h/(α+β)<2h/Λ on full-rank inputs. The equal-norm near-parallel family has ratio 1+cos θ irrespective of the pivot; the orthogonal family with small squared norm t has one-row error ratio 1+(t⁻¹−1)(2/π)arctan√t, which diverges. Integrating the endpoint beta density gives the additional fixed-s anisotropy law. Recorded code corroborates the finite cases and laws; no simulation is needed for the theorem.

## originality

PASS

The supported distinct claim is the sharp worst-case expectation theorem for arbitrary real rank-two two-column inputs, with the full correlated beta law at arbitrary sketch width. Exact catalogue overlaps cover the two-row correlated pivot probability and orthogonal subfamilies, not that full conclusion. Gaussian pivoting, chi-square laws and deterministic projection identities are not themselves new.

## value

PASS

The minimal-width result gives an exact expectation boundary for a standard randomized pivot mechanism, not just a rephrasing of the beta distribution. The one-row failure arises from rare orthogonal mispivots; with more rows the persistent sharp factor of two instead comes from nearly collinear equal-norm columns. Distinguishing these mechanisms clarifies what oversampling can and cannot improve in this narrow setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
