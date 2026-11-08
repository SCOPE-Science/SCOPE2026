---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Re-derived Kirchhoff index n tr((L+J/n)^-1)-n; graph simple ensures any nonzero conductance perturbation gives H≠0, and second derivative 2n tr(Q^-1 H Q^-1 H Q^-1)>0. Reflection symmetry excludes paired ordinary-edge zeros, and a hypothetical opposite ordinary zero (even n) has path-end voltage gain/budget multiplier at least 2n/(n-1)>1, contradicting unit-price KKT. The closing-zero path is optimized by Cauchy–Schwarz with w_k=B sqrt(k(n-k))/S_n. The missing closing edge derivative is multiplier times n Σ(T_j-mean T)^2, giving iff via strict convexity and complementary slackness, including equality. Symmetric endpoint-singular Riemann sums converge to 2 arcsin√x, and the centered squared integral is pi^2/4-2. Independent numerical values give r_c(3)=3 and r_c(4)=11/3+4/sqrt3; at n=600 normalized value approaches the stated limit. Finite checks do not prove all n.

## originality

PASS

Ghosh–Boyd–Saberi 2006/08 already prove convexity, global KKT framework and square-root tree allocations. Those parts are not new. The inspected primary sections do not give the one-price cycle support theorem, closing-edge threshold or quadratic asymptotic; distinct 2026 graph augmentation treats a different fixed-base/edge-choice setting. Best-of-knowledge PASS despite possible older specialized optimal-design derivation.

## value

PASS

A complete support phase transition for an economically natural one-exceptional-price electrical-network design, with a sharp explicit decision rule and an unexpected quadratic size dependence. The all-ordinary-active statement is a genuinely structural classification beyond a KKT restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
