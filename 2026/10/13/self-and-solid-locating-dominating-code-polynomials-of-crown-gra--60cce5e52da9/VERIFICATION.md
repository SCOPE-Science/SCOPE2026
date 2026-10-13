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

The verifier constructs every crown graph
\[
\operatorname{Cr}_n
\]
for
\[
3\le n\le8.
\]
For each subset \(C\), it computes every closed-neighborhood identifying set \(I(C;u)\), tests the defining solid condition by domination and all ordered identifying-set differences, and tests the self condition by the exact closed-neighborhood intersection criterion.

The direct decisions are compared with both omission classifications, every coefficient of both displayed polynomials, both minimum values, and both minimum-code counts.

Recorded output:

```text
VERIFY_OK
n=3: DLD_min=3, DLD_bases=2, SLD_min=3, SLD_bases=2
n=4: DLD_min=4, DLD_bases=8, SLD_min=4, SLD_bases=2
n=5: DLD_min=5, DLD_bases=22, SLD_min=5, SLD_bases=2
n=6: DLD_min=6, DLD_bases=52, SLD_min=6, SLD_bases=2
n=7: DLD_min=7, DLD_bases=114, SLD_min=7, SLD_bases=2
n=8: DLD_min=8, DLD_bases=240, SLD_min=8, SLD_bases=2
vertex_subsets_checked = 87360
```

The finite enumeration is corroborative only. The arbitrary-\(n\) theorem follows from the exact identifying-set formulas in the proof.
