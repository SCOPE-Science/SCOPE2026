---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For 0<rho<1, a=(1+rho)/2, d=(1-rho)/2, eta>=1 and fixed alpha>0, independent signed binomial imbalance T has ET=0 and ET^2=1/eta. Squaring the exact coordinate update yields B=[[ (1-alpha*a)^2, alpha^2*a*d/eta ],[alpha^2*a*d/eta,(1-alpha*d)^2]]. Its strictly positive off-diagonals make the Perron eigenvalue the asymptotic kth-root mean square for every nonzero deterministic error, rather than merely a worst-case bound. Direct diagonalization gives the stated radical r_eta. det(I-B)=alpha^2*a*d[4-2alpha+alpha^2*a*d(1-eta^-2)] and strict spectral convexity give the exact stable interval alpha<4/(1+sqrt(rho^2+(1-rho^2)/eta^2)), with equality nondecay and larger alpha divergence. The conditional norm matrix E(I-alpha G)^2 gives a smaller alpha_step=4/(1+rho+(1-rho)/eta), strictly smaller when eta>1. Derivatives at alpha=1 and 2 plus strict convexity give unique alpha_opt in (1,2). An independent batch-count calculation matched the exact moment recursion and radical eigenvalue on 192 finite comparisons; this verifies representative cases, not the universal domain.

## originality

PASS

Best-of-knowledge originality after direct statement/implication comparisons against indexed findings and relevant primary sources. Known antecedents and any covered symmetric/special cases are acknowledged; no comprehensive priority certificate is claimed.

## value

PASS

Sharp disparity between first-step transient expected amplification and eventual geometric mean-square stability is a mathematically motivated spectral phenomenon. The unique optimal relaxation and exact window can guide overrelaxation even in this minimal nonorthogonal model; it is not simply a rephrased textbook one-step estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
