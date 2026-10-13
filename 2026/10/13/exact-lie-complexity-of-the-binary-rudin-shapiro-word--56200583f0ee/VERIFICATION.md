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

Run `python3 verify.py` beside `certificate.json`; Python's standard library is sufficient.

The finite exact factor enumerator closes the four-letter substitution under two-letter factors, constructs all possible factors of a prescribed length from pairs of legal supertiles, and retains the starting-position parity. At length eight it produces exactly \(24\) even-start and \(32\) odd-start factors, with empty intersection. The complete sets are in `certificate.json` and are independently recomputed.

A second check reconstructs the first \(65536\) Rudin–Shapiro bits directly from the parity of adjacent \(11\) binary digit pairs, compares them to the morphic coding, and checks complete factor sets for lengths through \(24\). Exhaustive factor-set tests verify Lie complexity for every length through \(128\). The cyclic witness argument is checked for all four substitution letters and doubling levels \(1\) through \(9\).

The infinite theorem does not follow from finite enumeration. Its correctness uses the proven exact phase lemma, injective two-bit desubstitution, four-letter parity desubstitution, and explicit legal-boundary witnesses described in `RESULT.md`. The checker is a reproducible regression and critical-lemma certificate, not a substitute for those symbolic arguments.
