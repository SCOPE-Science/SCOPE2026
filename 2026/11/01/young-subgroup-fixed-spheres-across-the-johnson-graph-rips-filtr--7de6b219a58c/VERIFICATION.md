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

Run `python3 verify.py` in a directory containing `verify.py`, using Python 3 with no external packages. The program checks the original Johnson orbit distance inequalities by enumerating real \(k\)-subsets for \(1\le k\le6\), tests each individual open-neighborhood containment in the explicit fold sequence for all \(1\le m,t\le60\), and independently builds chain matrices over \(\mathbb F_2\) for all fixed-space band complexes with \(1\le k\le12\), \(0\le r<k\).

Completed output:

```
PASS: exact full-orbit distance extrema: 83 index pairs for 21 radii
PASS: explicit neighborhood folds: 198880 deletions across 3600 band graphs
PASS: independent mod-2 chain-rank calculations: 78 fixed-space complexes
```

The all-parameter proof, rather than these finite tests, establishes the theorem. Integral homotopy follows from a certified sequence of simplicial folds to a cross-polytope boundary, not merely from mod-two ranks. No claim is made about the inclusion-induced persistence maps or about independent validation.
