---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For nonzero linearly independent g1,g2 let a,b>0, rho∈(−1,1), H=GᵀG. Source Aligned-MTL has uniform d=(sigma_min(G)/2)G H^(−1/2)1, so (g1·d,g2·d)=(sigma_min(G)/2)H^(1/2)1. The exact positive-definite 2×2 square root is (H+ab sqrt(1−rho²)I)/sqrt(tr H+2ab sqrt(1−rho²)). Its two component signs are those of a+b(rho+sqrt(1−rho²)) and b+a(rho+sqrt(1−rho²)). When rho≥−1/sqrt2 both are positive; otherwise tau=−rho−sqrt(1−rho²)∈(0,1), and both positive iff tau<a/b<1/tau, with exact neutrality/harm at boundaries. For a=b,rho≤0 the all-ones Gram eigenvector belongs to sigma_min, so d=(g1+g2)/2; when rho>0 the scalar is sqrt((1−rho)/(1+rho)). Independently evaluated exact rho=−4/5, tau=1/5 and q=1/10,1/5,1,5,10 to confirm full sign transitions; source eigenvalue verifier inspected. This is instantaneous original-task first-order descent only, not whole optimization convergence.

## originality

PASS

Senushkin et al. (2023) introduced the SVD isotropization with uniform weights, including the aligned column norm/orthogonality objective, but do not give this original-gradient full-rank sign phase diagram. Quinton–Rey (2024/25) prove Aligned-MTL not universally non-conflicting using an explicitly rank-deficient example; that wider negative claim is credited and does not imply the full-rank quantitative threshold and symmetry identity. Resultary semantic search returned other MTL/normalization entries with different algorithms and metrics. The exact two-task formula requires an explicit Gram square-root and solving both original derivatives.

## value

PASS

Full-rank conflict is a natural and practical boundary for a method designed to resolve task-gradient interference. A sharp threshold in both cosine and norm imbalance, including neutral endpoint classification and a surprising no-change regime at equal norms, is a substantive motivated diagnostic beyond generic non-conflict failure. No unsupported multi-task global trajectory claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
