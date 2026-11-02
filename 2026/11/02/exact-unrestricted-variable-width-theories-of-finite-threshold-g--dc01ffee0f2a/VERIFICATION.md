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

# Reproducible verification and proof boundaries

Run the two included Python 3 programs with `python3 check_vicinal.py` and `python3 check_pebbles.py`. They require only the standard library. Compare their exact standard output, including trailing newlines, with `check_vicinal.out.txt` and `check_pebbles.out.txt` respectively.

The first enumerates all \(511\) threshold graph construction words through nine vertices, checks the vicinal total-preorder condition and preservation of ordered twin skeleton under truncation at widths three and four, and checks the four star lower bounds at widths three to six. It reports:

```
structural instances: 511
maximum twin classes: 8
compression invariants at widths 3 and 4: PASS
sharp star boundaries for widths 3,4,5,6: PASS
```

The second is a separate noncounting \(k\)-pebble tuple-color fixed-point implementation, not a replay of the proof's inductive argument. It computes stable logical types for all construction words through seven vertices at width three (\(127\) graphs, \(8{,}001\) comparisons), and through five vertices at width four (\(31\) graphs, \(465\) comparisons). It reports:

```
width 3 n<= 7 graphs 127 pairs 8001 rounds 5 tuple colors 6337 theories 87 : PASS
width 4 n<= 5 graphs 31 pairs 465 rounds 5 tuple colors 2901 theories 29 : PASS
```

This is finite exact corroboration, not an exhaustive certificate for infinite graph orders. The unrestricted theorem instead rests on the explicit three-variable recursive class formulas and permanent \(k\)-pebble strategy in `RESULT.md`. No external independent audit has been conducted.
