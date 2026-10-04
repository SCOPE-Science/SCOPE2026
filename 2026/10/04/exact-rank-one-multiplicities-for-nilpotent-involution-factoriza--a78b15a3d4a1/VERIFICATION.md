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

The proof is symbolic and valid for every prime power \(q\). The critical checks are:

1. For rank-one \(R=u\varphi\), verify \(R^2=\operatorname{tr}(R)R\); hence nonzero rank-one nilpotence is equivalent to trace zero and implies \(R^2=0\).
2. Use the bijection between factorizations \(A=NU\) and involutions \(U\) with \(\operatorname{tr}(AU)=0\), via the forced factor \(N=AU\).
3. For odd characteristic, verify the involution/idempotent bijection \(U=I_3-2P\), count qualifying rank-one idempotents modulo \((x,\psi)\sim(cx,c^{-1}\psi)\), and use \(P\mapsto I_3-P\) for rank two.
4. For characteristic two, verify \(U=I_3+S\) with \(S^2=0\), note \(\operatorname{rank}S\le1\) in dimension three, and count nonzero rank-one square-zero \(S=x\psi\) with \(\psi(x)=0\).

`verify_factorizations.py` separately enumerates every \(3\times3\) matrix over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), tests \(U^2=I_3\), and counts the two trace conditions. Its stored output is:

```
q=2: involutions=22; trace-zero-rank1 factors=14; nonzero-trace-rank1 factors=6; OK
q=3: involutions=236; trace-zero-rank1 factors=128; nonzero-trace-rank1 factors=48; OK
q=4: involutions=316; trace-zero-rank1 factors=124; nonzero-trace-rank1 factors=60; OK
```

The computation is a check only; the all-\(q\) result is proved by the counting argument above. No claim is made for rank-two matrices or dimensions other than three.
