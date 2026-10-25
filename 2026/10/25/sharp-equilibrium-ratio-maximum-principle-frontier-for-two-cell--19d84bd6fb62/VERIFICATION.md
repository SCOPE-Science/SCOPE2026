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

Run `python3 verify_mprk_bound.py` using Python 3 standard library only. The checker performs exact coefficientwise algebra on a multivariate polynomial representation of the derivative identity, checks 5920 exact-rational parameter cases with independent formulas for the two linear implicit stages, and checks an interior witness with rational entries. The analytic sign argument and endpoint optimization in RESULT.md establish the infinite family of step sizes and initial states; the finite tests alone would not suffice.

The most delicate identities are \(B-E=(u-p)^2/(pq)\), \(N'D-ND'=-H\) with every coefficient of \(H\) strictly positive, and \(\lim_{s\to\infty}R=-1/(1+B)\). Boundary values \(u\in\{0,1\}\) and \(s=\infty\) are excluded from the claimed admissible domain and used only to calculate suprema. The benchmark fixes \(a=1/4\), \(b=3/4\), \(u=9/10\), \(h=10\). There is no external or independent verification recorded.
