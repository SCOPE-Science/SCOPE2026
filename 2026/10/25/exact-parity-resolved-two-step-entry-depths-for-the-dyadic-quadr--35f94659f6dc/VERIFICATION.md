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

Run `python3 verify.py` using Python 3 standard library only. The checker constructs roots by direct enumeration independently at each modulus, verifies that \(f\) swaps the parity roots, traces the first two-step hit of all residues for every \(1\le k\le17\), and compares all cumulative parity counts for every \(0\le t\le k+1\) with the closed formulas. The exact small-level boundary cases and a middle-range histogram are printed.

The computation checks finitely many moduli and is **not** a proof for all exponents. The mathematical proof in `RESULT.md` is based on exact polynomial factorization, a universal valuation-gain lemma, and the standard power-of-two square-root count. No independent audit has been performed.
