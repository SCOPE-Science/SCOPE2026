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

# Reproducibility and limitations

`verification/check.py` requires Python 3.8 or later and only the standard library. Run `python verification/check.py` from the package root. It prints a minimum-distance check for a 20-word classical binary code, exact branch-and-bound results for lengths one to four, exhaustive direct one-edit error-ball comparisons for row counts one to four and column counts one to two, and terminates in `VERIFY_OK`. The recorded output is `verification/check-output.txt`.

Proof Step 1 is exact: output row lengths rule out confusion across edit types, and the XOR dependency recovers a deleted or inserted row from the remaining rows. Step 2 reduces substitution confusability to two codewords differing in one column by Hamming distance one or two. Steps 3 and 4 match a packing upper bound in every fixed-prefix section with a row-parity-code lower bound for all positive parameters. Step 5 yields the necessary maximum-section property for arbitrary optimum codes.

The classical \(A_2(8,3)=20\) value uses independent published coding tables. The checker proves that the transcribed 20-word *witness* has distance three, not that a 21-word classical code cannot exist; the latter is external mathematical prior work. Likewise, finite direct error-ball tests do not certify the infinite theorem, which is supported by the displayed proof. Nothing here constitutes an independent external mathematical audit.
