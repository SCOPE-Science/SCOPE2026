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

# Exact computations and limits

Run `python3 verify.py` from this directory; no packages other than Python 3's standard library are required. The verifier reports:

```
VERIFY_OK formula_n=1..6 paired_partitions_n=1..5 raw_semigroup_n=2,3
n=1 ranks=(0, 1) total=1
n=2 ranks=(1, 4, 2) total=7
n=3 ranks=(1, 9, 90, 6) total=106
n=4 ranks=(1, 16, 3672, 2112, 24) total=5825
n=5 ranks=(1, 25, 141800, 157800, 59400, 120) total=359146
n=6 ranks=(1, 36, 6202350, 10245600, 7635600, 2034720, 720) total=26119027
```

The first method evaluates the symbolic finite sum with exact integers. The second, logically different finite method enumerates paired set partitions and block bijections, using a local polynomial to count matching marked-point pairs. The third directly constructs all generator partial maps on \(T_n\) and closes under composition for \(n=2,3\); it finds 7 distinct generators at \(n=2\), and 88 distinct generators closing to 106 elements at \(n=3\). The corank-one formula is additionally checked for \(3\leq n\leq6\).

Finite computation cannot establish the formula for arbitrary \(n\). Its infinite proof uses the structural classification in arXiv:2605.00041, Theorem 5.9, and the counting proof in RESULT.md. The older antecedent manuscript arXiv:2301.04252 was not exhaustively compared at every historical version. No independent audit is claimed.
