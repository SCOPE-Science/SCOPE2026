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

# Reproducibility and scope

Use Python 3 with no third-party libraries:

```sh
python3 check_singer.py
python3 check_vector_height.py
```

Both complete with `PASS` assertions when successful. The programs reproduce the full \(2106\)-state universe, the \(126\) frozen states, the \(1980\)-state connected component, the \(6804\) recolouring edges, and the exact radius and diameter \(21\). They construct the Fano plane using genuinely different finite models: a Singer difference set and vector addition over \(\mathbb F_2\). The first checks all-root graph distances, while the second checks an all-pairs exact integer-height metric derived from the previously published height lemma.

The reproducibility claim is finite and exact, not statistical; each assertion is backed by exhaustive iteration over its explicitly enumerated domain. This package does not provide independent scholarly validation, publication priority, or a theorem for projective planes of other orders. The literature-derived height-function lemma is used as an explicitly cited prior theorem, not attributed to this work.
