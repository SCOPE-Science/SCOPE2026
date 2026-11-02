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

Execute `python3 verify.py` in the same directory. The actual run completed with output `VERIFY_OK pairs=1000000 n_with_omega_le_2=467`. The program independently evaluates reciprocal polynomial divisibilities for all ordered \((a,b)\) with \(1\le a,b\le1000\) and evaluates the rational gcd-reciprocal sum directly for every \(n\le1000\) having \(\Omega(n)\le2\).

The calculations cover finite ranges only. The proof of the universal assertion is the descent and multiplicative-factor argument in RESULT.md. The authorship and novelty are not independently certified.
