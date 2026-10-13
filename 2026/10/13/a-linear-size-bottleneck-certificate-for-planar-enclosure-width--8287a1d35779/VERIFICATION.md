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

# Verification notes

Run `python3 verify_width.py` with standard Python 3 (no third-party packages). This executes direct pairwise exhaustive comparisons on all 16,900 pairs of at-most-three-point subsets of the nine-point grid, 96,000 randomized bounded-integer tests, and 1,500 exact-rational cases. The observed final line was:

```text
VERIFY_OK 16900 exhaustive subset pairs, 96000 random integer pairs, 1500 rational pairs
```

The script also validates each returned box witness, distinguishes an empty enclosure from one of width zero, and includes a nontrivial witness example. It reads no external files and requires no machine-specific path.

The mathematical verification does **not** use finite enumeration as proof for arbitrary inputs. It relies on the four proof steps in `RESULT.md`: diagonal-endpoint reduction to pairs, dominance pruning, the two-candidate bottleneck lemma, and monotonicity of crossing indices. The claimed sorting and scan bounds count exact comparisons and arithmetic on finite real coordinates. They do not quantify floating-point roundoff or running times inside a full optimization solver.

Originality is assessed by comparisons with specified published formulas and inspected primary literature; this remains a self-review, not an independent audit. Unindexed equivalent work is a residual limitation.
