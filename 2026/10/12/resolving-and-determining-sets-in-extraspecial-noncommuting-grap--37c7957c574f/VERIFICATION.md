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

The standalone `verify.py` artifact was inspected at its packaged path before replay.

It constructs the projective symplectic quotient associated with the extraspecial commutator form for \((p,n)=(2,1),(3,1),(2,2),(3,2),(5,2)\). It checks the projective-point count, the fiber size \(p(p-1)\), and the quotient separation condition used to distinguish omitted vertices.

It separately constructs the finite Heisenberg group for \(p=2,3,5\) from its multiplication law, forms the noncommuting graph directly from commutators, and verifies that the predicted projective fibers are exactly distinct false-twin neighborhood classes in those cases. It checks the canonical minimum resolving set in each example.

For \(p=2,n=1\), all \(2^6\) vertex subsets are tested. The resolving-set size distribution is exactly
\[
8x^3+12x^4+6x^5+x^6=(2x+x^2)^3.
\]

Exact replay output:

```text
p=2, n=1: projective classes=3, class_size=2, vertices=6, beta=Det=3, bases=8
p=3, n=1: projective classes=4, class_size=6, vertices=24, beta=Det=20, bases=1296
p=2, n=2: projective classes=15, class_size=2, vertices=30, beta=Det=15, bases=32768
p=3, n=2: projective classes=40, class_size=6, vertices=240, beta=Det=200, bases=13367494538843734067838845976576
p=5, n=2: projective classes=156, class_size=20, vertices=3120, beta=Det=2964, bases=91343852333181432387730302044767688728495783936000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Heisenberg p=2: actual group twin partition and resolving basis OK
Heisenberg p=3: actual group twin partition and resolving basis OK
Heisenberg p=5: actual group twin partition and resolving basis OK
p=2, n=1 exhaustive resolving polynomial: {3: 8, 4: 12, 5: 6, 6: 1}
VERIFY_OK
```

The arbitrary-rank theorem is proved symbolically from the extraspecial commutator geometry. Finite computation is corroborative and does not replace the proof.
