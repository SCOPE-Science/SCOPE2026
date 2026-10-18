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

For an SPD A with eigenvalues in [mu,L], the delayed Rayleigh quotient r lies in [mu,L], so h=p/r and every spectral product h*lambda is in [p/kappa,p*kappa]. Since p>=1, max(abs(1-p/kappa),abs(1-p*kappa))=p*kappa-1. The same squared modal bound controls Euclidean gradient norm and A^-1-weighted objective gap. In the actual exact-line-search warm-up A=diag(kappa,1), g0=(sqrt(e),1), the next gradient lies in the large-eigenvalue mode as e->0 while h1->p, so both ratios tend to (p*kappa-1)^2, proving a sharp supremum. For p*kappa>2 sufficiently small positive e yields strict increases. Endpoint p*kappa=2 ensures nonincrease, not necessarily exact attainment. Independent rational iterates tested kappa=5/1.5/2 and p=1.5/1.2/1 with multiple scales; universal analytic proof remains separate.

## originality

PASS

PASS best-of-knowledge for this precise fixed-p extension and sharp compatible warm-up, not for operator spectral norm inequalities or generic delayed gradient methods. The closest published BB-interval theorem has different step-domain and parameter. Xu full primary text supplies method and asymptotic stability but not the transient frontier.

## value

PASS

The natural question is whether locally/stochastically stable longer-than-BB1 steps can transiently increase energy or gradient. The sharp condition-number and p-dependent pointwise boundary answers this with an algorithmically compatible witness. It is an exact finite-horizon safety limit beyond asymptotic rates, not just a renamed spectral inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
