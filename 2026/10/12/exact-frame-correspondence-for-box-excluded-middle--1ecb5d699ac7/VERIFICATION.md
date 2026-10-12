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

The general equivalence was checked by replaying both semantic directions from the definitions.

For sufficiency, a world \(z\) falsifying \(\varphi\) and accessible from \(x\) remains an obstruction to every \(y\ge x\): the exact condition would otherwise produce \(u\) with \(yRu\) and \(u\le z\), contradicting persistence of \(\varphi\).

For necessity, failure of the exact condition at \(x\le y\) and \(xRz\) gives the persistent atomic valuation
\[
V(p)=\{v:\exists u\,(yRu\wedge u\le v)\}.
\]
Then \(y\Vdash\Box p\), while \(x\nVdash\Box p\) because \(z\notin V(p)\). Since \(y\ge x\), also \(x\nVdash\neg\Box p\). Thus the excluded-middle instance fails.

`artifacts/verify_small.py` was executed from its packaged path. It reported:

```text
n=1: frames=2, exact_vs_atomic_mismatches=0, exact_not_BEM=0
n=2: frames=34, exact_vs_atomic_mismatches=0, exact_not_BEM=2
n=3: frames=2942, exact_vs_atomic_mismatches=0, exact_not_BEM=270
two_point_witness=OK
published_four_point_example=OK
```

The enumerator ranges over all labeled partial orders and all modal relations satisfying the basic birelational compatibility condition. It checks only the atomic instance \(\Box p\vee\neg\Box p\), which is a finite sanity check and is not used to infer the arbitrary-formula theorem.

The first public source date is the arXiv v1 submission date, 2025-10-20. The journal's Mathematics Subject Classification lists 03B45 as primary.
