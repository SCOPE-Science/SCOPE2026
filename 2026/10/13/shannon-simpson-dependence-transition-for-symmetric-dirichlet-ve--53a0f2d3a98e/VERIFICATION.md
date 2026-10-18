---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Dirichlet gamma-ratio mixed moments yield exact negative covariance by differentiating P_i^3 and P_i^2P_j at log exponent one, and double derivative gives Var(H). Direct fourth moments give Var(Q). Gamma representation P_i=Y_i/sumY with independent Gamma(a,1) yields the bivariate delta-method CLT; exact covariance limits agree with its gradient covariance. Integral g(x)=x² psi1(x)-x has representation with f(t)=1/(1-e^-t)-1/t strictly increasing, giving rho(a) strictly decreasing. Trigamma Taylor at a=0 gives fixed-m variances proportional to a and -sqrt(3)/(2sqrt(2zeta(3)-pi²/6)); noncommutation follows. Independent closed-moment calculations at (m,a)=(2,1),(3,1/2),(7,3) and mpmath rho tests match. Finite tests do not replace all-m proof.

## originality

PASS

Royen computes distribution of squared Dirichlet sum Q and Wolpert–Wolf gives Shannon entropy moments. These inspected primary sources separately address marginals, not the joint shape-dependent limiting correlation and order-of-limits transition. The a=1 uniform-spacing covariance was previously established and is explicitly excluded from new priority. A broader older joint Dirichlet cross-moment may imply the fixed-a finite covariance but not necessarily strict monotonicity or noncommuting limits; retained O risk.

## value

PASS

Quantifies a natural dependence transition for symmetric Dirichlet random probability vectors and the canonical spacings/Greenwood statistic, including a mathematically sharp noncommutation of sparse and high-dimensional limits and a joint CLT. The limiting shape law is a structural property independently useful for uncertainty and diversity modeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
