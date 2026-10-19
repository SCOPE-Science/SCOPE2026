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

# Reproducibility and verification limits

Run `python opa_sector_verifier.py` with Python 3, NumPy, SymPy, and mpmath available. Its expected stdout is stored verbatim in `opa_sector_checks.txt`.

The checker performs exact symbolic identities for \(m=3,\dots,40\), calculates all finite roots independently for \(n=1,\dots,16\) and checks their arguments relative to the excluded \(45\)-degree cone, and uses high precision to track one zero branch over five increasing degrees. It checks the predicted value \(w_0\), first correction, and a bounded inverse-square asymptotic remainder. The result is a finite reproducibility test, not an exhaustive all-degree verification. The proof in `RESULT.md` explicitly gives the constrained Hardy projection, the strict cone inequality, and the compact-uniform convergence needed for the infinite claims.

The sharp maximum possible exclusion half-angle, the unrestricted global zero distribution, and any independent external scientific certification are outside this verification.
