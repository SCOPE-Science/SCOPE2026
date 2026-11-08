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

PASS. For a>b>0, exact rank-one Nyström quotient ab(1+z)/(b+az), oracle scaling c=m(b+az)/(b(1+a)+a(1+b)z), and trace/determinant reduce comparison kappa(B)>(1+a)/(1+b) to -Q(z)>0. Independently sympy-factored the full rational sign identity to zero; Q has coefficient signs ++--, Q(0)>0 and Q(1)=-b(a+b+2)^2<0 so exactly one crossing in (0,1). Squared independent Gaussian coordinate ratio is Cauchy-squared, proving each probability, and coefficient limit Q/a^2=z[(1+b)-bz-(1+b)z^2] gives the asymptotics. Scope only rank one, dimension two, oracle m=1+b, exact Gaussian models.

## originality

PASS

PASS (best-of-knowledge). The input EDA covariance, Nyström eigenvalue and spectral LMP are published; the sharp two-mode probability cubic and exponents p_iso~a^-1 versus p_informed~a^-2 are additional exact stochastic statements, not implied by existing matrix error or eigenpair sensitivity estimates.

## value

PASS

PASS. Gives a precise harmful-preconditioning event with exact failure probability and contrasts isotropic versus informed sketches. The two-mode benchmark is mathematically motivated by preconditioner safety; neither finite checks nor claimed field performance are used to infer a wider theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
