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

Run `python verify.py` with Python 3 standard library. The script computes power-series coefficients independently from binomial/Catalan numbers and propagates the exact joint state of position, maximum height, and return count through each step, with rational arithmetic. It compares every coefficient for \(n=0,\ldots,16\) of three moment series: \(\mathbb E[M_n L_n]\), \(\mathbb E[L_n]\), and \(\mathbb E[L_n^2]\). The observed check passed for every tested coefficient.

The proof for all \(n\) is analytical, not an extrapolation from these checks. The script does not certify the Tauberian theorem or asymptotic moment uniform integrability, which are justified in the written proof. Independent scientific audit has not been performed.
