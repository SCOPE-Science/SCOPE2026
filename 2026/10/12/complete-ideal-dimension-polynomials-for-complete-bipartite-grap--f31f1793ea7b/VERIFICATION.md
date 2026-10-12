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

Run `python3 verify.py` from the extracted file directory. The code needs only the Python standard library. It constructs every RREF subspace and directly checks Lie-ideal closure under the full vertex generator basis, comparing the resulting dimension profile with the formula evaluated separately. Cases are (a,b,q)=(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2), with 6, 7, 26, 45, and 247 ideals, respectively. Symmetry under swapping the two bipartite part sizes was also checked numerically. The successful run prints `VERIFY_OK`.

The finite-field enumerations are not a substitute for the general proof by bijections. All counts include the zero ideal and the whole algebra and are over finite fields. Independent scientific review is not performed.
