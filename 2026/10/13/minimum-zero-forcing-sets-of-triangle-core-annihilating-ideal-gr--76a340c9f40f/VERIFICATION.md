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

For every
\[
1\le n\le6,
\qquad
1\le m\le4,
\]
the checker constructs \(F_n(m)\), enumerates every vertex subset in increasing cardinality, and computes all minimum zero forcing sets. It verifies both the claimed cardinality and the exact support-profile classification of every minimizer.

It separately constructs \(K_3(1,1,1)\) and verifies that its nine minimum pairs are exactly:
\[
\text{two leaves},
\]
or
\[
\text{one core vertex plus a nonincident leaf}.
\]

The checker also evaluates the closed forms on representative members of each infinite finite-ring family in the Yu–Wu list.

Exact replay output:

```text
F_1(1): Z=2, minimum_sets=5
F_1(2): Z=2, minimum_sets=4
F_1(3): Z=3, minimum_sets=6
F_1(4): Z=4, minimum_sets=8
F_2(1): Z=3, minimum_sets=12
F_2(2): Z=3, minimum_sets=8
F_2(3): Z=4, minimum_sets=12
F_2(4): Z=5, minimum_sets=16
F_3(1): Z=4, minimum_sets=28
F_3(2): Z=4, minimum_sets=16
F_3(3): Z=5, minimum_sets=24
F_3(4): Z=6, minimum_sets=32
F_4(1): Z=5, minimum_sets=64
F_4(2): Z=5, minimum_sets=32
F_4(3): Z=6, minimum_sets=48
F_4(4): Z=7, minimum_sets=64
F_5(1): Z=6, minimum_sets=144
F_5(2): Z=6, minimum_sets=64
F_5(3): Z=7, minimum_sets=96
F_5(4): Z=8, minimum_sets=128
F_6(1): Z=7, minimum_sets=320
F_6(2): Z=7, minimum_sets=128
F_6(3): Z=8, minimum_sets=192
F_6(4): Z=9, minimum_sets=256
K3(1,1,1): Z=2, minimum_sets=9
YU_WU_SPECIALIZATIONS_OK
VERIFY_OK
```

These finite computations corroborate but do not replace the arbitrary-\(n,m\) proof. The proof itself rests on the twin-class lower bounds and an exhaustive equality-case split.
