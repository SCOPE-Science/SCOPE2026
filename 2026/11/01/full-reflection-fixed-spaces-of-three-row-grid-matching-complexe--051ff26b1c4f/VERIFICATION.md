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
# Verification record

The all-width mathematical proof is the group-orbit barycenter PL triangulation, the independent pairwise-conflict analysis, and the path independence suspension recurrence in `RESULT.md`. It explicitly includes the exceptional empty width-three fixed set. This is not a machine-checked proof or independent mathematical certification.

Run `python3 verify_fixed.py` in the package directory. The program uses only Python 3's standard library and constructs the three-row grid graph edges directly, then constructs the complete action of row and column reflections on those edges. It tests each generated edge orbit for the matching condition; checks all distinct admissible-orbit pairs against two path conflict graphs through width 90; enumerates all candidate orbit subsets through width 13 and compares their face predicate with the predicted independent-set condition; constructs mod-two boundary matrices of the finite fixed complexes through width 12 and checks their reduced Betti ranks. The observed final output is:

```
VERIFY_OK: widths 2..90; orbit classes 6119 ; checked candidate faces 6825 ; homology widths 2..12
```

The finite mod-two checks do not establish the integral homology theorem, whose infinite proof follows from the explicit sphere homotopy classification. The search comparison consulted the full available primary arXiv PDF and the complete published RESULT.md texts of the two closest symmetry studies; residual risks of other equivalent sources remain.
