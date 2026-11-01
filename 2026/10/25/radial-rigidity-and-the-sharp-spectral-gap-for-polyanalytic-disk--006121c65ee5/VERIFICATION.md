---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

In the full order-m closure of polyanalytic polynomials, each positive-frequency sector z^k P(|z|²) (deg P≤m−1) is finite-dimensional and its cutoff Rayleigh quotient is Q_k(P). For each nonzero P, increasing k size-biases s toward 1, strictly reducing mass on (0,R). Positivity a.e. of w gives a strictly negative covariance; compactness of projective polynomial space makes the gap uniform, and Courant–Fischer yields λ_j(k+1)<λ_j(k) for all j. Negative-frequency sectors embed into the +h polynomial sector and hence do not maximize. For m=2, w=1, exact 2×2 Gram determinants/traces give roots Λk± with product R^(2k+4); p0(R²)=−4R³(1−R)² and p1(R²)=−8R⁴(1−R)² establish leading separation from the negative mode R². Eigenvectors yield the sharp projection gap. Formal expansion gives Δ~4R as R↓0 and 3/4(1−R)^3 as R↑1. Independent SymPy replay checked tr/det and polynomial straddles.

## originality

PASS

Best-of-knowledge originality PASS limited to strict all-weight angular eigenvalue domination and sharp full bianalytic gap, not the previously known moment block formulas. Priority risk remains because the closest whole paper was inaccessible.

## value

PASS

An all-order centered-disk concentration problem is a natural norm/localization question. The strict size-bias ordering proves radial rigidity of all maximizers for arbitrary positive weights; the unweighted bianalytic second eigenvalue and cubic stability gap quantify the sharp global deficit and equality space. These conclusions are not automatic from the known individual matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
