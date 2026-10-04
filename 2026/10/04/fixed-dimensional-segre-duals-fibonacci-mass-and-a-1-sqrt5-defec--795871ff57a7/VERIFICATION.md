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

The proof is symbolic. The reproducibility script `artifacts/verify.py` performs independent exact-integer checks of its discrete consequences.

It verifies for every \(2\le n\le1000\):

- \(d_n(a)=\binom{n-a+1}{a}\) on the full admissible range;
- the exact sign equivalence between \(d_n(a+1)-d_n(a)\) and \(5a^2-(5n+2)a+n^2-1\);
- strict decrease of successive ratios by cross-multiplication, with no floating-point comparison;
- the maximizing set predicted by the ratio-crossing rule;
- \(\sum_a d_n(a)=F_{n+2}-1-\mathbf 1_{n\text{ odd}}\).

The script also prints the first integer-root tie cases. These computations are finite regression checks only. The all-\(n\) statements are proved in `RESULT.md` by the tangent-space argument, Giambelli--Thom--Porteous, exact algebra, and the Fibonacci recurrence.
