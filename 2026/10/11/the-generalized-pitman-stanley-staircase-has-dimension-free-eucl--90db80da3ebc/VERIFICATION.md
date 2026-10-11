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
The theorem is proved symbolically in `RESULT.md`; finite computation is corroborative only.

Critical checks:
- the generalized all-ones polytope is the nonnegative matrix region with \(0\le s_{im}\le\cdots\le s_{i1}\le i\);
- coordinate, prefix, and inter-column prefix normals have Euclidean norms \(1\), \(\sqrt i\), and \(\sqrt{2i}\);
- the first-row radius inequalities telescope to \(1\ge r(2+(m-1)\sqrt2)\);
- the profile \(y_m=r\), \(y_j-y_{j+1}=r\sqrt2\), \(y_1=1-r\) repeated in every row satisfies every higher-prefix radius constraint;
- equality in the first-row telescope forces the first row of every incenter;
- for \(n\ge2\), a uniform positive perturbation of every later row leaves all non-first-row inequalities strict when the perturbation is chosen below the displayed bound, proving affine dimension \(m(n-1)\).

`verify.py` checks all normalized inequalities for \(1\le n\le100\) and \(2\le m\le50\), including the strict-slack witness for the dimension statement. It does not assess originality.
