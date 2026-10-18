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

# Reproducibility and scope

Run `python3 verify.py` with Python 3.10 or later; no external packages or files are needed. Successful execution prints `VERIFY_OK`. The script derives coefficients using two independent exact-integer calculations, checks \(156\) coefficient agreements, checks Catalan valuations for \(140\) indices, checks the proposed conductors for \(49\) powers of two, and verifies the published four-class exclusion for \(34\) precisions. These checks do not replace the formal proof for all indices and exponents in `RESULT.md`.

The critical infinite steps are the exact formal-series identity, the Legendre valuation formula for Catalan numbers, and uniqueness of the top-degree contribution from the largest surviving summand. The theorem concerns eventual divisibility of the specified sequence only. No independent mathematical validation has been performed.
