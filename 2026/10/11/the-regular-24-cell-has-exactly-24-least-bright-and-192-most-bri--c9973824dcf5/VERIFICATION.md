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

The fundamental input, checked directly in the cited primary article, is that the standard regular 24-cell has 24 facets with equal 3-volume \(\sqrt2/3\) and unit normals \((\varepsilon e_i+\eta e_j)/\sqrt2\), with \(i<j\) and \(\varepsilon,\eta\in\{-1,1\}\).

Cauchy's projection formula gives
\[
b(u)=\frac{1}{3}\sum_{i<j}\left(|u_i+u_j|+|u_i-u_j|\right).
\]
The identity \(|x+y|+|x-y|=2\max(|x|,|y|)\) yields the sorted-coordinate formula exactly.

For a unit vector with sorted absolute coordinates \(a_1\ge a_2\ge a_3\ge a_4\ge0\), the sharp upper bound follows from
\[
3a_1+2a_2+a_3\le\sqrt{14}\|a\|.
\]
Equality fixes \(a=(3,2,1,0)/\sqrt{14}\).

The four nonnegative fundamental-cone generators \(g_j\) satisfy
\[
L(g_j)/\|g_j\|\in\{3,5/\sqrt2,2\sqrt3,3\}.
\]
The triangle inequality gives \(L(a)\ge3\|a\|\), with equality only along the first or fourth generator ray. The full signed-permutation counts are 24 and 192.

Run the standalone exact checker with `python verify.py`. It uses the Python standard library only and reports `VERIFY_OK` after checking all 24 root-facet inequalities and octahedral facet structure, as well as the closed-form extremal values and enumeration. The code does not attempt to prove the global inequalities by sampling; the preceding analytic arguments establish them for every unit direction.

A separate numerical convex-hull volume cross-check of the explicit projected vertices agreed with the analytic formula at representative unit directions, including generic directions. Floating-point tests are limited corroboration and not used to justify exhaustive coverage.
