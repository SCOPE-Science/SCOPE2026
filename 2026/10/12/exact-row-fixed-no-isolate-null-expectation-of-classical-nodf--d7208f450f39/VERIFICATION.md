---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Directly reconstructed the labeled row-subset ensemble and Z=Σ_j(-1)^j C(n,j)∏_i C(n−j,r_i), positive when Σ r_i≥n. A marked column shared by rows i,k gives n H_ik; a two-marked-column polynomial with factors C(n−2−j,r_i)+C(n−2−j,r_i−1)(u+v)+C(n−2−j,r_i−2)uvw counts both degrees and overlap. Restrict a,b≥1 and a≠b, divide c by min(a,b), add normalized row terms and divide by K Z. Ties correctly contribute zero. The O(m^3) coefficient states updated over m factors and n exclusions justify O(nm^4) exact arithmetic, not bit time. An independent 3×4 (1,2,3) full enumeration gives 60 covered matrices and mean 7/15. The finite checker is only corroboration; inclusion-exclusion is the all-parameter proof.

## originality

PASS

Best-of-knowledge original closed expectation for the *row-only hard-constrained, all-columns-positive* ensemble and degree-sorted NODF with tied degrees. The nearest ecological papers treat metric definition, randomized simulations, independent-edge soft degrees or fully fixed row-and-column degrees. These distinct probability laws cannot be specialized by matching expected margins. A generic coefficient-algorithm counterpart remains an honest residual risk.

## value

PASS

The conditional row-hard null is motivated by ecological bipartite-network baselines with observed row abundances and no empty guild members; exact tied-column-degree handling removes simulation error for a statistically meaningful expectation. Arbitrary heterogeneous row sums and polynomial exact coefficients add reusable analytic value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
