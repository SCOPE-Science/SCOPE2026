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

# Verification of the two-marker minimal-absent-factor classification

Execute `python3 VERIFY.py` from this directory using Python 3 and the standard library. The script independently enumerates all contiguous factors of a word, generates every candidate whose proper prefix and suffix occur, and compares the resulting minimal-absent-factor **set** against the theorem's explicit conditional list. It includes the alphabet-letter absence case, zero gaps, and equality of gap lengths.

The fixed exhaustive grid uses all triples with \(0\le a,b,c\le10\) (1,331 words). It also checks 200 larger triples drawn from a fixed deterministic seed, compares the first 32 coefficients of the claimed rational generating function to independent gap summation, and verifies the unique maximizer for each length \(6\le n\le89\). A passing run prints `PASS: 1531 independent MAW-set comparisons, 32 GF coefficients, exact maxima for n=6..89`.

The bound is **not** proved solely by finite enumeration. The human-readable classification proof, three-case reduction, generating-series derivation and sharpness argument are in `RESULT.md`. No independent audit has yet occurred.
