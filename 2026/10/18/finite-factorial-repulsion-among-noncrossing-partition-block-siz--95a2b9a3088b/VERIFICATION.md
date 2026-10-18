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

# Reproduction and limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses no third-party dependencies. It prints `PASS 83058 exact assertions; exhaustive NC partitions n<=8` after performing independent restricted-growth-string enumeration of all set partitions up to eight elements, Catalan filtering, single and mixed falling-factorial-moment comparisons, finite pairwise strict inequality tests through thirty elements, and the weak-composition local inequality across indicated sizes.

The universal proof is the explicit Lagrange-inversion and elementary polynomial inequality in RESULT.md. The finite script does not prove any infinite quantifier. The exact n=3 distributions separately test the distinction between count covariance and monotone threshold-event covariance. No independent audit has been performed.
