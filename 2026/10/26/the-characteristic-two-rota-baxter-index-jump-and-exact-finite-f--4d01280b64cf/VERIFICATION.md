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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 interpreter. The checker uses no third-party packages. It directly enumerates every linear map \(P:A\to A\) over the prime fields \(\mathbb F_2\), \(\mathbb F_3\) for \(n=1,2\), and over \(\mathbb F_2\) for \(n=3\), and checks the weight-zero Rota–Baxter identity on basis pairs. It separately evaluates the algebraic classification condition, the Gaussian-binomial enumerator, and the rank/flag orbit partition under conjugation by the full finite general linear group.

Expected exact output:

```
q= 2 n= 1 operator_count= 2 orbit_types= 2 predicted= 2
  P^2=0: 2 P^2 !=0: 0
q= 3 n= 1 operator_count= 3 orbit_types= 2 predicted= 3
q= 2 n= 2 operator_count= 16 orbit_types= 5 predicted= 16
  P^2=0: 10 P^2 !=0: 6
q= 3 n= 2 operator_count= 33 orbit_types= 4 predicted= 33
q= 2 n= 3 operator_count= 176 orbit_types= 6 predicted= 176
  P^2=0: 92 P^2 !=0: 84
VERIFY_OK
```

These finite checks do not certify the theorem over arbitrary fields, all prime powers, or unbounded dimensions. Those assertions are proved algebraically in `RESULT.md`. No independent mathematical audit has been performed.
