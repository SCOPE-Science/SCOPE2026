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

Run `python3 checker.py` with Python 3. The checker exhaustively evaluates the finite \(m\)-threshold analogue of the infinite-accumulation operation on all initial-segment topologies of ordinal sizes zero through ten, and on all subsets in those spaces. It checks the first-threshold normal form and each successive derivative against a separate direct neighbourhood count. For finite ranks it independently tests sizes up to 99 and thresholds from two to eleven. The completed run returned:

```
ALL_CHECKS_OK subsets=12282 derivative_comparisons=147450 ranks=1100
```

This finite test cannot decide any assertion involving \(\omega\) points or a nonfinite ordinal. The transfinite result is justified by the symbolic proof in `RESULT.md`: first-infinite-block lemma, exact tail step, limit-stage intersections, ordinal multiplication continuity, and strictness of the thresholds. The examples \(\theta=\omega\), \(\theta=\omega+1\), \(\theta=\omega^2\), and \(\theta=\omega^2+1\) provide hand-checkable boundary comparisons. No independent audit has been performed.
