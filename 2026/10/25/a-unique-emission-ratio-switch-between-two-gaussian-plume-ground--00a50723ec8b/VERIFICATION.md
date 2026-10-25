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

# Reproduction and verification

Run `python3 verification/verify_plume_hotspot.py` with Python 3.9 or newer from the root of the extracted package. The script uses only the Python standard library and a deterministic random seed. It computes the stationary branches and emission-ratio balance by bracketed bisection, never by fitting the expected answer. It checks strict ordering of maxima and the intervening minimum for 450 randomized height ratios; independently checks 120 physical-to-normalized concentration formulas; tests three approaches to the cubic onset and four high-contrast cases; and reproduces the \(r=9\) benchmark.

The derivation in `RESULT.md` proves the infinite-domain root count and the unique balance. Random numerical trials, floating-point agreement, and finite tests cannot establish those universal claims, mathematical originality, empirical plume accuracy, or historical priority. The tested profile assumes steady meteorology, no deposition, and linearly growing dispersion widths.

Independent scientific validation has not been performed.
