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

# Verification of the exact quadratic norm

The argument uses two exact identities and a complete one-variable minimization. Direct substitution with normalized measures gives \(\|DF\|_{A^1}=|P(1)|/2\) and \(\|F\|_{H^1}=\int|P|dm\). The two norm-preserving symmetries plus convexity are applicable to every complex quadratic. For real palindromic coefficients, the norm is \(G(u)=\int|1-4u\sin^2(\theta/2)|dm\), globally convex. The critical point in \(1/4<u<1/2\) solves \(\arcsin v=\sqrt{1-v^2}\), and exact integration gives \(G=2\tau/\pi\).

Run `python3 checker.py` to reproduce the root and circle-integral numerical consistency checks. The code checks a finite grid and seeded random coefficients; these checks are not used as the proof of the universal assertion. All equality statements in the theorem concern the exhibited extremizer only; uniqueness is not claimed.

The statement is restricted to homogeneous quadratics at exponent one. No independent audit has been performed.
