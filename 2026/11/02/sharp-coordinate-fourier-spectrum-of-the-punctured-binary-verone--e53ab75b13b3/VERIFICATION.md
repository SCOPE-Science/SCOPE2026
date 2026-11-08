---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The diagonal of vv^T equals v over F2, so rank-one map injective; b_ij=(1+chi_i+chi_j-chi_ij)/2 makes invertible triangular transformation from the intrinsic Walsh band. Full-cube Walsh orthonormality and removal of zero yields W=(QI-11^T)/(Q-1), giving positivity and determinant for 2^d>1+d+binom(d,2). Direct moments produce the complete-graph unsigned vertex-edge incidence block G0; BB^T=(d-2)I+J yields orthogonal 3+(2(d-1))+(m-d) decomposition. The standard 2x2 block and edge kernel give all eigenvalues. A Rayleigh quotient for vector (-sqrt(m)/2,-sqrt((d-1)/2),1), plus strict diagonal/trace comparison for the top, locates both extrema in symmetric H_d for every d>=3. H0 has eigenvalue 1 and quadratic pair product 1/4, its rank-one puncture correction is O(d^2/2^d), so largest ~d^2/8, smallest ~2/d^2, ratio ~d^4/16. Independently built exact Gram for d=3..8 and tested sector eigenvalues; exact determinant checked for d=3..5. Those small dimensions do not prove the infinite limit.

## originality

PASS

The broad association-scheme P/Q-number machinery of Schmidt provides character sums for all symmetric forms but the inspected paper does not state the coordinate-selected nonorthogonal Gram spectrum, extremal three-sector inequalities, determinant and d^4/16 conditioning. Resultary nearby odd-characteristic symmetric Veronese results omit diagonal and use other fields; rectangular rank-one and binary symplectic groups concern different varieties. A specialization of general tables remains possible but is not established as a covering theorem.

## value

PASS

A complete exact Fourier frame/Riesz spectrum and sharp conditioning for a canonical binary symmetric rank-one algebraic variety, showing the ambient-coordinate character choice creates a quartic penalty absent from intrinsic Walsh coordinates. It answers a motivated spectral-design question, beyond an arbitrary finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
