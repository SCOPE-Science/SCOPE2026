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

# Computational verification
The standalone `verify.py` directly enumerates all pairs \((u,S)\) over the specified finite fields, reconstructs the original Lie brackets, checks the bilinear weight-zero Rota–Baxter equation on basis pairs, and checks the graph-restricted \(p\)-power equation for every element of the Lie algebra. The point counts are then compared with the independently implemented Gaussian-binomial formula. The extension field \(\mathbb F_4\) uses the polynomial \(t^2+t+1\), not integer arithmetic modulo four.

Executed checks returned:

```
PASS n=1 q=2 p=2 T=[1] ordinary=2 restricted=2 rank_distribution={0: 2}
PASS n=2 q=2 p=2 T=[1, 1] ordinary=16 restricted=10 rank_distribution={0: 4, 1: 6}
PASS n=3 q=2 p=2 T=[1, 1, 1] ordinary=176 restricted=92 rank_distribution={0: 8, 1: 84}
PASS n=2 q=4 p=2 T=[1, 1] ordinary=256 restricted=76 rank_distribution={0: 16, 1: 60}
PASS n=2 q=3 p=3 T=[1, 2] ordinary=81 restricted=81 rank_distribution={0: 9, 1: 72}
PASS n=2 q=5 p=5 T=[1, 2] ordinary=625 restricted=625 rank_distribution={0: 25, 1: 600}
VERIFY_OK
```

The code tests finitely many cases. The unrestricted all-field proof is the bracket and semidirect-power calculation in `RESULT.md`; the finite tests cannot establish arbitrary-dimensional or infinite-field correctness by themselves. Historical priority and independent review remain unperformed.
