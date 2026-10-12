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

The standalone `verify.py` artifact was read from its actual packaged path before replay.

For \(p=2,3,5,7\), it constructs the abstract \((p+2,p)\)-pineapple, examines every vertex subset, and checks equivalence between standard zero forcing and the structural white-complement condition
\[
|W\cap L|\le1,
\qquad
|W\cap Q|\le1.
\]
It then compares the exhaustive coefficient dictionary with the expansion of
\[
u^{2p-1}(u+p)(u+p+1)(u+1)
\]
and checks that the minimum-set count is \(p(p+1)\).

For \(p=2,3\), the same artifact separately constructs the additive group \(C_{p^2}\times C_p\), generates its subgroups from pairs of elements, and computes subgroup intersections directly. It recovers exactly \(p+1\) subgroups of order \(p\), \(p+1\) of order \(p^2\), one universal p-torsion subgroup, \(p\) pendant order-\(p\) vertices, and the required clique.

Exact replay output:

```text
p=2: abstract polynomial {3: 6, 4: 11, 5: 6, 6: 1}; minimum sets=6
p=3: abstract polynomial {5: 12, 6: 19, 7: 8, 8: 1}; minimum sets=12
p=5: abstract polynomial {9: 30, 10: 41, 11: 12, 12: 1}; minimum sets=30
p=7: abstract polynomial {13: 56, 14: 71, 15: 16, 16: 1}; minimum sets=56
p=2: actual subgroup census {2: 3, 4: 3}; degrees=[1, 1, 3, 3, 3, 5]
p=3: actual subgroup census {9: 4, 3: 4}; degrees=[1, 1, 1, 4, 4, 4, 4, 7]
VERIFY_OK
```

The finite checks are corroborative. The arbitrary-prime theorem is proved by the subgroup count and the two-direction forcing classification in `RESULT.md`.
