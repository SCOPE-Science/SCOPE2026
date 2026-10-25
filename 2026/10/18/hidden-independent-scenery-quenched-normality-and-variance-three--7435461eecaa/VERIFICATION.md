---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The frozen Bernoulli coefficients transform under the lower-unitriangular mod-2 Pascal matrix into iid fair scenery f_s, independent of base signs under the joint law. Number of negative increments S has iid geometric(1/2) holding times G_s with EG=2, EG²=6, so regenerative SLLN Cn/n→0 joint; Borel–Cantelli handles maximum incomplete holding block; Fubini yields almost-sure quenched bracket vanishing for typical fixed coefficient environment. Bounded martingale increments then give independent Brownian coordinates under conditional law. E[f_{S_i}f_{S_j}]=2^{−(j−i)} gives exact variance 3n−4+2^{2−n}; q0=1 correction gives 3n−7+2^{3−n}. Iid block vector (G−2,Gf) covariance diag(2,6) and clock2 gives annealed covariance diag(1,3), with negligible maximal geometric overshoot. Independently recomputed n≤10 exact variance and read full actual checker.py; finite tests not used as infinite proofs.

## originality

PASS

Hamza–Tournier Section 4.3 studies the exact frozen-cardinality model and already proves annealed convergence; its quenched question is explicitly unresolved there. The current result is only the fair-parameter quenched case and an exact annealed second-order fluctuation law; general bootstrap FCLT theorems are proof ingredients, not published verification of the environmental condition.

## value

PASS

Settles a distinguished fair-coefficient special case of an explicitly posed frozen-environment quenched normality question and explains why persistent coefficient reuse still yields independent Brownian coordinates. The exact predictable-bracket variance and variance-three second-order limit are additional useful probability invariants, not rote simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
