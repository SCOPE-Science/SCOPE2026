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

# Reproduction and limits

Run `python3 check.py` with the standard Python library. This computes the proposed exact gcd formula and independent factorial-valuation minima for all \(3\le n\le1200\), computes the *original* large-integer defining gcd for all \(3\le n\le80\), and verifies 1,295 choices of the explicit binomial witness identity at eligible parameters up to \(n=400\).

Expected final line: `CERTIFICATE_OK n_formulas= 1198 direct_gcd_cases= 78 witness_identity_cases= 1295`.

The proof of the infinite statement uses Kummer's theorem, Legendre's digit-sum formula, and Guo et al. arXiv:2606.22997v1 Lemmas 4 and 9, not extrapolation from finite experiments. No independent mathematical audit or formal certification is asserted.
