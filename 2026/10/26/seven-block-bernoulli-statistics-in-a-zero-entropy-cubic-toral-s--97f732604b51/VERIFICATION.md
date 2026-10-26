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

# Verification and limits

The standalone `verify.py` uses only the Python standard library. It checks exact binomial coefficient expansions for fourth differences, directly checks the zero-or-odd coefficient obstruction in a symmetric integer sample, and constructs the first admissible degree-seven all-odd relation as a **boundary for the obstruction**, not as proof of an eighth-order nonzero correlation.

An independent finite phase-grid check enumerates every one of the \(32^4\) phase points at drift \(\alpha=0\), obtaining exactly \(8192\) occurrences for each of the \(128\) seven-bit output words. This finite check cannot prove the statement for Haar-distributed real phases or all rotation parameters; the Fourier–Fejér argument in `RESULT.md` proves that statement without numerical assumptions.

Full mathematical claims audited here are limited to seven consecutive sign observations, their exactly uniform 128-cell distribution, stationarity, and zero entropy rate. No eight-block threshold or independent external validation is asserted.
