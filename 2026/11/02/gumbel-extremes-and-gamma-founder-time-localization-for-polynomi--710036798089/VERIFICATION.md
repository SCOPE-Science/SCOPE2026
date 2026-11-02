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

# Reproducibility and verification

Extract `checker.py` and `verification_output.txt` from this package into the same directory and run `python3 checker.py`. Python standard library only; no network or external data required. The reported execution completed successfully with **3,214 exact-rational and numerical assertions**. The exact tests check repeated offspring pgf composition at rational values, geometric law normalization and tails, exact first/second factorial moments, and finite-product to Poisson comparison inequalities. Numerical tests check root solving and sample exceedance intensities for three parameter pairs at sizes 512–32768.

The accompanying `verification_output.txt` preserves the displayed output of a completed replay. A small finite grid is not proof of a Poisson point process, an asymptotic Gamma mark, a universal error bound, or priority. The infinite conclusions follow from the explicit probability law, summable envelopes, Riemann-sum rare-event intensity and exact variance computation in `RESULT.md`.

No independent audit or outside verification is claimed.
