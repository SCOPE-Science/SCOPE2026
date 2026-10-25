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

Run `python3 verify_first_close.py` with Python 3 and no third-party packages. The program enumerates all perfect matchings with \(2n\) ordered endpoints for every \(2\le n\le7\). It computes \(T_n\) as the minimum larger endpoint, counts alternating-endpoint chord crossings, and checks each exact conditional mean, survival probability, survival-conditional crossing mean, and unconditional mean with exact rational arithmetic. The largest case has \(135{,}135\) matchings and the six cases together have \(146{,}598\). All checks passed in the reviewed run. The exact all-size proof and all asymptotic statements are mathematical, not certified by this finite test. No independent audit has been performed.
