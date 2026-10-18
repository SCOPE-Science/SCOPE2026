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

# Reproducibility and limits

Run `python verify.py` with a standard Python 3 interpreter and SymPy installed. The script rebuilds the exact normalized third-iterate polynomial by symbolic rational arithmetic, verifies all seven coefficients and the discriminant factorization, and checks six exact sign-change intervals at \(\mu=23/4\). It also verifies \(P_\mu(0)\), \(P_\mu(1)\), and \(P_\mu((\mu-1)/(\mu+1))\) exactly, together with rational signs bracketing the unique relevant quartic root.

This is an exact finite symbolic checker, not an exhaustive scan of a real-parameter continuum. The analytic proof in `RESULT.md` supplies the missing infinite step via discriminant nonvanishing, root-continuity, endpoint exclusion, and the cyclic symmetry of repeated roots. No independent audit or external certification is represented by these computations.
