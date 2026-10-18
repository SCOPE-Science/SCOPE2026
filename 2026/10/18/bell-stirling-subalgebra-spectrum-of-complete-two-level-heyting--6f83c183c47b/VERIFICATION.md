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

Run `python3 verify.py` with Python 3 (standard library only). The program exhaustively constructs every full Heyting algebra of the complete two-layer frames for \(1\le a,b\le3\), enumerates all subsets containing both constants, and keeps exactly those closed under meet, join, and implication. Separately it generates every allowed quotient partition and compares the complete lists, their size spectra and total counts.

It additionally verifies all ordered kernel/refinement comparisons, maximal proper subalgebra counts and intersections. The observed terminal summary was:

```text
VERIFY_OK families=9 exhaustive_subalgebras=106 kernel_order_pairs=2142
```

The exhaustive finite checks include frame sizes up to six points. The assertion for arbitrary positive integers \(a,b\) is justified by the combinatorial-Esakia proof in RESULT.md, not by running the finite program. No independent external audit or formal proof certificate has been performed.
