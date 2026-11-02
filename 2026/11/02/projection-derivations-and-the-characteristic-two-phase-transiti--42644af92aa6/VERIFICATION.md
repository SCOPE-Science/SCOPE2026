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

# Reproducible checks and their limits

Run `python3 VERIFY/check.py` from the package root. The script constructs the ordered basis multiplication \([e_i,e_1]=e_{i+1}\), forms every candidate derivation in the established \(n+1\)-parameter space, checks the original derivation identities, computes \(D^2\) with finite-field arithmetic, counts projections, and computes their exact matrix rank distribution by row elimination. It tests eleven finite-field/dimension configurations: \((n,q)=(4,2),(4,3),(4,4),(4,5),(5,2),(5,3),(5,4),(6,2),(6,3),(6,4),(7,2)\). The field with four elements uses multiplication modulo a quadratic irreducible polynomial rather than substituting integers modulo four. In the first case it also separately exhausts all \(2^{16}\) original endomorphism matrices to independently check completeness of the derivation parametrization.

The embedded `VERIFY/output.txt` records all eleven passing configurations and ends in `FILIFORM_LEIBNIZ_IDEMPOTENT_DERIVATIONS_OK 11_CASES`. Matching these finite tests does not prove the formulas for arbitrary fields or all \(n\); the unrestricted proof is given in `RESULT.md`. No external or independent mathematical audit has been performed.
