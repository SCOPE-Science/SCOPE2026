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

# Reproducible verification

Run `python3 verify.py` using the standard Python library; the output should identify 2,741 deterministic finite coefficient and Gram checks. The checks cover: normalized source/target coefficient formulas for five choices of indices; exact Gram matrices of three polynomial phase examples (up to 30 columns); Fourier coefficients of the polyphase Hardy symbols; and exact distinction between \(P(z)=1+z\) and \(P(z)=1+z^2\) for \(q=2\).

The infinite-dimensional proof is contained in `RESULT.md`. Finite data cannot certify infinite essential spectral sets, Fredholm status, the universal singular-value inequalities, or publication priority. Those claims rest on the displayed analytic argument and literature comparisons, not on the checker. No independent audit is represented.
