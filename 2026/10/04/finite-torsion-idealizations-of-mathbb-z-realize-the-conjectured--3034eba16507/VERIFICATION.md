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

The proof has four independent checkpoints.

1. **Zero-divisor criterion.** For \((a,m)\in\mathbb Z\ltimes M\), a common prime divisor of \(a\) and the exponent of \(M\) supplies a nonzero annihilated module element. If the two integers are coprime, Bézout gives an inverse for scalar multiplication by \(a\) on \(M\), forcing every annihilator to be zero.

2. **Upper bound.** First-coordinate representatives \(0,1,\ldots,p-1\) dominate because one makes the first-coordinate sum divisible by the smallest prime \(p\mid n\).

3. **Lower bound.** For fewer than \(p\) proposed dominators, every prime \(q\mid n\) has at least one residue class avoiding all forbidden negatives. The Chinese remainder theorem combines these choices into a first coordinate whose sum with every proposed dominator is coprime to \(n\).

4. **Annihilator-index comparison.** A nonzero element with nonzero integer coordinate has an annihilator of infinite index. For \((0,y)\) with \(y\) of order \(d\), the annihilator is exactly \(d\mathbb Z\ltimes M\); maximal proper annihilator ideals with finite index therefore correspond to prime-order elements.

The accompanying script checks the finite residue-covering reduction exhaustively for small exponents:

```text
VERIFY_OK
checked_exponents=2..30
statement=minimum translate-cover number of nonunits in Z/nZ equals the smallest prime divisor
```

The script is a stress test only. The theorem for arbitrary finite abelian \(M\) and arbitrary exponent \(n>1\) rests on the symbolic arguments above.
