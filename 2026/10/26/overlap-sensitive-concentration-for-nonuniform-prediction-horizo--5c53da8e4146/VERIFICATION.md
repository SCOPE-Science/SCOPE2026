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

The analytic verification checks the following implications.

1. Each centered term satisfies \(|Z_n|\le2\) and has conditional mean zero given \(\mathcal F_{n-K_n}\).
2. The interval family has a proper coloring with \(\Delta\) colors. Within each color, the windows are disjoint, so the terms form a bounded martingale-difference sequence.
3. Conditional Hoeffding gives \(\mathbb E e^{\lambda S_c}\le e^{2\lambda^2 r_c}\).
4. Generalized Hölder with \(p_c=(\sum_d\sqrt{r_d})/\sqrt{r_c}\) gives \(\mathbb E e^{\lambda\sum_cS_c}\le e^{2\lambda^2R}\), where \(R=(\sum_c\sqrt{r_c})^2\le\Delta N\).
5. Chernoff optimization gives \(\Pr(|\sum_n Z_n|\ge x)\le2e^{-x^2/(8\Delta N)}\).

The finite-sample example is a direct count of interval overlaps, not a computational certificate for the theorem. No numerical enumeration, external certification, or independent audit is claimed. The result does not establish sharpness for all horizon patterns.
