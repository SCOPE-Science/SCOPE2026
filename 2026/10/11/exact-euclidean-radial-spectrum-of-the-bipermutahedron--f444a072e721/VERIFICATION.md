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
The theorem is proved for arbitrary \(n\ge2\) in `RESULT.md`; finite computation is corroborative only.

`verify.py` performs four checks using exact integer arithmetic:

1. It enumerates every Dyck bar pattern for \(2\le n\le8\) and confirms that the statistic \(A=\sum_j(u_j-j)\) takes every integer value from \(0\) through \(n(n-1)/2\).
2. It checks that substituting \(s=2A-n^2\) into the vertex norm produces distinct levels and that the largest level agrees exactly with \(2n(n-1)(3n^2+7n+1)/3\).
3. It brute-forces all labeled bipermutations for \(2\le n\le4\), reconstructs Ardila's expanded odd-integer coordinates, and compares the actual squared norms with the closed formula.
4. It verifies that the brute-force number of outer-shell vertices equals \(n((n-1)!)^2\) in those dimensions.

The checker does not prove the infinite statement; the arbitrary-\(n\) Dyck and symmetry arguments in `RESULT.md` do.
