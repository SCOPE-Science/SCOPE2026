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

# Reproducibility and limits

The standalone script `verify_sparse.py` (Python 3 standard library only) independently enumerates all nonempty contiguous substrings and tabulates their composition counts. It checks the displayed polynomial formulas for every four-gap tuple with all coordinates between 0 and 7; it then tests the up-to-reversal inverse decoder on every binary word having exactly three ones and total length from 3 through 21. The verifier additionally checks the five-symbol top-layer counterexample and the eight-symbol classical full-spectrum collision. The successful actual execution reported:

`VERIFY_OK gap_tuples=4096 weight3_words=7315 top_layer_counterexample=1 weight4_full_collision=1`

The finite tests alone are not an all-length certificate. The proof of all-length reconstruction, including the polynomial-domain noncancellation argument and recovery of unordered gap pairs, is in `RESULT.md`. The literature search supports but cannot mathematically establish priority; external independent scientific audit has not been performed.
