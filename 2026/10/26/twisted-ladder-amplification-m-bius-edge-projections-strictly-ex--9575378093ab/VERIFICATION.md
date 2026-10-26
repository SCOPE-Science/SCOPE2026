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

# Reproducibility and scope of verification

Execute `python check.py` in an environment with SymPy installed. The script constructs the incidence matrix from the vertex/edge definitions, inverts the shifted full graph Laplacian over exact rationals, checks projection and matrix identities, independently computes antiperiodic and periodic Green functions, compares every edge-row absolute sum, tests both edge orbits and the strict topology comparison for every size from three through twelve, and checks the symmetric threshold-block identity. The current package run returned `PASS 713 exact assertions`.

This computation establishes exact finite consistency only. The all-size inequalities, sharp attainment, parity-asymptotic expansions, and logarithmic deficit are proved analytically in `RESULT.md`. No external validation or independent audit was performed.
