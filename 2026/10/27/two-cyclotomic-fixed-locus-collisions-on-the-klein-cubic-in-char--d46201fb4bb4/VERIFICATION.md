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

The exact polynomial checks can be rerun with `python verify.py` using Python 3 and SymPy. The program independently constructs all six defining polynomials for the invariant-line scheme, computes two Gröbner bases (over the rationals and modulo five), checks divisibility by the proposed integral quadratic model, and verifies the point fixed polynomial and the two discriminants. It completed with the printed marker `VERIFY_OK`. The mathematical proof also uses smoothness, properness/finite fibers, Nakayama's lemma, and a tangent representation calculation; these steps are spelled out in RESULT.md and are not replaced by an experiment. No quotient-singularity computation or independent external audit was performed.
