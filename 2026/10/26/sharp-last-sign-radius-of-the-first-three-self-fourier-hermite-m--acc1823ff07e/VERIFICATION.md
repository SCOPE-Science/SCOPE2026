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

Run `python verify.py` with Python 3 and SymPy. The script checks the Hermite expansions, exact congruence modulo the defining cubic, the two boundary contact equations, the discriminant and root bracket, and a high-precision evaluation of the radius. The output is archived as `verification.log`. It is a local symbolic check, not an independent audit.

The analytical proof establishes all real parameters by evaluating a competing polynomial at one of two exact contact points. Numerical roots provide only a readable approximation. The proof does not require a finite grid search, nor does the checker certify any claim beyond the displayed identities and verified inequalities.
