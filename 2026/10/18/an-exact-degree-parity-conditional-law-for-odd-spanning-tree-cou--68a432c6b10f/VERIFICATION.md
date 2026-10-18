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

# Reproducibility
Run `python verify.py` with Python 3 and its standard library. The program enumerates every labeled graph for \(2\le n\le6\), compares conditional event probabilities for all feasible degree-parity vectors using rational arithmetic and checks the binary cofactor determinant directly. It independently enumerates all symmetric matrices with prescribed diagonal in dimensions one through five and verifies the exact zero/nonzero diagonal nonsingularity probabilities. The verifier was run successfully. These checks do not, by themselves, establish the infinite family of identities; the complete proof is in `RESULT.md`. No external or independent validation was performed.
