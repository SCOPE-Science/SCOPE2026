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

Expanding a finite |P|² gives the lag-ℓ coefficient as the sum of a_(j+ℓ) conjugate(a_j) weighted by M_(2j+ℓ); for the frozen power weight M_n=1/(n+β+1). At the largest support gap M−m there is exactly one contributing pair, and its moment is positive. Thus the support diameter is exactly k for a nonzero single harmonic. Interior terms need not vanish in general. Put X=|a_m|²M_(2m) and Y=|a_(m+k)|²M_(2m+2k). The mean-one energy gives X+Y≤1; AM–GM bounds the amplitude by M_(2m+k)/(2√(M_(2m)M_(2m+2k))). Conversely, using just those two monomials with energies cos²u,sin²u realizes all amplitudes up to that value at any prescribed phase. This proves the moment companion (moments multiply the coefficient products, as obtained directly by integration). In the power case the ratio is 1/2 times √(1−k²/(2m+k+β+1)²), strictly increasing in m; hence m=d−k is forced at equality, along with X=Y=1/2 and absence of interior coefficients. Matching a_(m+k) conjugate(a_m) to the positive-mode phase gives the stated equality family. Solving the amplitude inequality yields the ceiling/max in the minimum degree, with no issues from squaring because 2d−k+β+1>0. The sharp bound stays below 1/2 at every finite d, while at zero a constant suffices; 1−4ε²=4δ(1−δ) gives the stated inverse-square-root asymptotic with a bounded rounding error. Separate replay `python /workspace/review_checks/frozen_probes.py` passes exact rational complex-coefficient examples at three weights and the equality-at-1/2 atomic-measure limit. No frozen script was executed. The frozen 110-instance symbolic subtotal is hard-coded while its displayed triangular-range loops actually run 120 unweighted pairs; this reporting discrepancy has no role in the proof.

## originality

PASS

For the precise one-harmonic finite-degree extremal problem, the sharp formula with equality and converse is distinct from unrestricted holomorphic inversion, weighted trace norms and boundary spectral factorization in the inspected material. The overlap with the unweighted Radon operator and energy normalization is real and is not claimed as novel.

## value

PASS

The holomorphic existence theorem leaves polynomial complexity open. Single-harmonic data are the simplest nonconstant family in which to separate that question from boundary factorization. The strict finite-degree margin, unique extremizer, all-amplitude converse and exact coefficient of the degree blow-up yield a complete benchmark near a vanishing target. This is more informative than an isolated test or the known mean identity, without claiming a result for arbitrary data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
