---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility checks

The public standalone script `checks/check.py` executes under Python 3 with SymPy and independently constructs every unique tree path for sampled integer corridor/community sizes. It tests the predicted ordered-pair path scores against exact rational arithmetic across all vertices, verifies the stated middle-versus-hub polynomial coefficients and \(p=1\) formula, and checks the unique \(s=3,L=4\) witness threshold. In the scientific review it printed `PASS 3564 independent ordered-path exact-rational tests, coefficient identities, and crossover witness` and the approximate threshold `0.916188398055051`.

The script's finite parameter range is not an exhaustive proof. The arbitrary-size and full-transmissibility conclusion is established by exact score decomposition, curvature and coefficient-sign arguments in RESULT.md. The evidence assumes the symmetric tree, a single uniformly placed seed, identical independent edge transmissibilities and perfect pre-seed vertex deletion. Independent validation has not been performed.
