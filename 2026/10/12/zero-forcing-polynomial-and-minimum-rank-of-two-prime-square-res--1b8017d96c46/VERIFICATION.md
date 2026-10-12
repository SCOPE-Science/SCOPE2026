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

It constructs the vertex set of
\[
\Gamma(\mathbb Z/(p^2q))
\]
directly as the nonzero residues with nontrivial gcd with \(p^2q\), and tests every edge by residue multiplication modulo \(p^2q\).

The tested small cases
\[
(p,q)=(2,3),(3,2),(2,5)
\]
are exhaustively enumerated over all vertex subsets; the resulting complete zero forcing polynomials agree exactly with the closed formula.

The larger cases
\[
(3,5),(5,2)
\]
check the direct four-class structure, every one of the \(16\) profiles that leaves at most one white representative per class, the predicted polynomial, and the rank witness.

The block witness is checked edge by edge and its rank is computed exactly over the rationals.

Exact replay output:

```text
p=2, q=3: N=7, polynomial={3: 8, 4: 20, 5: 18, 6: 7, 7: 1}, witness_rank=4
p=3, q=2: N=11, polynomial={7: 24, 8: 52, 9: 38, 10: 11, 11: 1}, witness_rank=4
p=2, q=5: N=11, polynomial={7: 32, 8: 64, 9: 42, 10: 11, 11: 1}, witness_rank=4
p=3, q=5: N=20, predicted_polynomial={20: 1, 19: 20, 18: 140, 17: 400, 16: 384}, witness_rank=4
p=5, q=2: N=29, predicted_polynomial={29: 1, 28: 29, 27: 204, 26: 496, 25: 320}, witness_rank=4
ALL_16_TYPE_PROFILES_FORCE_OK
VERIFY_OK
```

These finite calculations corroborate but do not replace the arbitrary-prime proof in `RESULT.md`.
