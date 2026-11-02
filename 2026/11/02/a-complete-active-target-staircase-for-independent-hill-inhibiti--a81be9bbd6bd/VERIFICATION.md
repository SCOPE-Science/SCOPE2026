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

# Verification and proof limits

The complete proof in `RESULT.md` covers all integers \(n\ge2\), all real \(h>0\), all positive total doses and common scale factors, and all nonnegative real allocations. The core nonstandard inequality rules out *unequal positive coordinates* at any global maximum, and strict unimodality of \(\log(1+t^h)/t\) proves the complete sequential transition structure.

Run `python3 check.py` with standard Python 3. It deterministically tests 52,569 exact-rational allocations on finite grids for cooperative integer Hill exponents, 21,600 random allocations for a range of real Hill exponents, and 56 strictly ordered crossing brackets. The numerical tests were executed successfully. These checks do **not** prove the infinite parameter domain and do not provide a clinical efficacy assessment.

General nonlinear resource-allocation literature has not been exhaustively ruled out as prior coverage. The 1970, 1974 and 1980 general allocation works were available only through abstracts/bibliographic accounts, not as completely inspected primary papers. The 1974 paper explicitly reports a solution for identical plants, so it is a substantive historical-priority risk. The theorem is not independently audited.
