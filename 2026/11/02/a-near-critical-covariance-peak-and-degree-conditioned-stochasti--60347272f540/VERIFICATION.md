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

# Reproduction and verification

Run `python verify.py` with Python 3 and no external packages. The code enumerates all independent parent assignments and retention masks for a uniform recursive tree. It checks exact rational conditional tails, first and second moments, and original-root-degree/root-cluster covariance at each of 16 finite rational parameter models: sizes \(3\)–\(7\) at retention \(1/3,1/2,2/3\), plus size \(8\) at retention \(1/2\). It also checks 294 rational pairs of finite covariance recurrences through size \(100\), and prints three numerical critical-window diagnostics.

The root degree in the computation is measured before edges are deleted. Weighted enumeration uses denominator \((n-1)!b^{n-1}\) when \(p=a/b\). The increasing conditional upper-tail comparisons are checked with exact fractions. The two mixed-moment recursions are formulated separately, reducing shared implementation assumptions.

Passing the checker demonstrates only the stated finite test coverage. The all-\(n\) coupling and the global maximizing-window limit require the symbolic arguments in `RESULT.md`. Numerical convergence is not an infinite proof. No external or independent validation is claimed.
