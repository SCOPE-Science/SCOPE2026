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

# Verification of the ternary singleton-deck classification

Execute `python3 verify.py` from the directory containing the embedded files. Only the Python standard library is required.

The checker enumerates all words over a three-letter alphabet of lengths \(1\) through \(12\). It constructs each adjacent-pair composition vector literally, groups words by the actual observation and reversals, and tests the independently implemented graph-support/loop criterion against the literal number of reversal orbits in every fiber. It also compares the full-deck count and singleton-deck count with their derived formulas for every tested length.

Observed output ends with:

```
VERIFY_OK ternary_source_words=797160 examined_profiles=9901 singleton_profiles=1392 n_range=1..12
```

The positive-edge-length singleton counts for \(m=1,\ldots,11\) are \(6,12,30,51,81,108,144,177,219,258,306\). At word length one the unique empty edge deck has three non-reversal-equivalent sources, so its singleton count is zero.

**Mathematical proof checks:** The Euler criterion handles every realizable observation; ordinary-edge supports of sizes zero through three are exhaustive; the one- and two-edge-support skeletons are unique precisely in the cases asserted; three-edge-support decks always have multiple skeleton orbits. The enumerating families are disjoint. The generating functions are finite products of geometric series, and their coefficients give the stated formula. These analytic arguments, rather than the finite enumeration, establish all lengths.

**Unproved scope:** No classification for four or more letters, no noisy channel, no aggregate number of source words per nonsingleton deck, and no independent scientific assessment is asserted.
