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

# Verification and reproducibility

Run `python3 verify.py` using Python 3, without third-party dependencies. This checks the sextic's polynomial and gradient by exact arithmetic at every projective rational point of \(\mathbf P^2(\mathbf F_3)\) and \(\mathbf P^2(\mathbf F_9)\), for every parameter pair satisfying the stated nonvanishing hypotheses. Expected terminal line: `VERIFY_OK`.

Observed admissible pairs: four over \(\mathbf F_3\), 58 over \(\mathbf F_9\). In both fields the four sign points are the entire *rational* singular set. The proof in `RESULT.md`, not finite enumeration, covers geometric singularities over algebraically closed characteristic-three fields, irreducibility, ramification and genus. This verification does not check every geometric point over the closure, parameter strata excluded by the theorem, or unpublished literature.

Independent audit and independent validation have not been performed.
