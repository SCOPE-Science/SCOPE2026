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

# Verification

Run `python verify.py` (Python 3.11+; SymPy 1.14 tested). The exact program reconstructs the binary evaluation kernel, enumerates every filling form, computes the rational Jacobian masks and ambient group orbits, and checks the four affine Jacobian ideals by characteristic-two Gröbner bases. Its expected asserted outputs are 2048 filling forms, 364 rationally nonsingular nonzero forms in 22 orbits, and 66 geometrically smooth forms in 4 orbits with sizes 6,6,18,36. There are no random choices. This is an exhaustive finite algebraic certificate; no search cutoff over finite extensions is substituted for geometric smoothness. Independent audit is not performed.
