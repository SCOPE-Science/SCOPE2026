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

The standalone `verify.py` artifact was read from its packaged path before replay.

For each \(1\le m\le12\), it constructs the graph
\[
i\sim j
\quad\Longleftrightarrow\quad
i+j\ge m+1,
\]
exhaustively tests every vertex subset for zero forcing, and separately tests the “ready” condition used in the proof.

It verifies
\[
Z(A_m)=\left\lfloor\frac m2\right\rfloor
\]
for \(m\ge2\), together with the recurrences
\[
a_{m+2}=2a_m+b_m,
\qquad
b_{m+2}=a_m+b_m,
\]
and the Fibonacci closed forms for both parity classes.

Independently, for
\[
\mathbb Z/(p^\ell),
\qquad
p\in\{2,3\},
\qquad
2\le\ell\le6,
\]
the checker computes every annihilator directly from ring multiplication, forms the equivalence classes, and verifies that their valuations are exactly
\[
1,\ldots,\ell-1
\]
with adjacency equal to \(A_{\ell-1}\).

Exact replay output:

```text
m=1: K1 boundary, Z=1, min_sets=1, mr=0
m=2: Z=1, min_sets=2, ready_min=2, ready_sets=1, mr=1
m=3: Z=1, min_sets=2, ready_min=2, ready_sets=2, mr=2
m=4: Z=2, min_sets=5, ready_min=3, ready_sets=3, mr=2
m=5: Z=2, min_sets=6, ready_min=3, ready_sets=4, mr=3
m=6: Z=3, min_sets=13, ready_min=4, ready_sets=8, mr=3
m=7: Z=3, min_sets=16, ready_min=4, ready_sets=10, mr=4
m=8: Z=4, min_sets=34, ready_min=5, ready_sets=21, mr=4
m=9: Z=4, min_sets=42, ready_min=5, ready_sets=26, mr=5
m=10: Z=5, min_sets=89, ready_min=6, ready_sets=55, mr=5
m=11: Z=5, min_sets=110, ready_min=6, ready_sets=68, mr=6
m=12: Z=6, min_sets=233, ready_min=7, ready_sets=144, mr=6
Z/2^2: classes=1, valuations=[1], anti_regular=A_1
Z/2^3: classes=2, valuations=[1, 2], anti_regular=A_2
Z/2^4: classes=3, valuations=[1, 2, 3], anti_regular=A_3
Z/2^5: classes=4, valuations=[1, 2, 3, 4], anti_regular=A_4
Z/2^6: classes=5, valuations=[1, 2, 3, 4, 5], anti_regular=A_5
Z/3^2: classes=1, valuations=[1], anti_regular=A_1
Z/3^3: classes=2, valuations=[1, 2], anti_regular=A_2
Z/3^4: classes=3, valuations=[1, 2, 3], anti_regular=A_3
Z/3^5: classes=4, valuations=[1, 2, 3, 4], anti_regular=A_4
Z/3^6: classes=5, valuations=[1, 2, 3, 4, 5], anti_regular=A_5
VERIFY_OK
```

These finite computations corroborate the recurrence and ring identification. The arbitrary finite-chain-ring theorem is proved symbolically in `RESULT.md`; the real maximum-nullity equality uses the published threshold-graph theorem cited there.
