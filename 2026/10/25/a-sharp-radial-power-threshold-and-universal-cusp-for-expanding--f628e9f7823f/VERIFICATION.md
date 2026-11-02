---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS. Reconstructed scaling E_p=omega r^(n-1+p) G_p(a/r). For p>=0 positive weights are subharmonic (or constant), and for 2-n<=p<0 spherical potential Gp decreases in offset, making E increase. For subcritical 1-n<p<2-n, p<0, Gp prime is negative for t>1 while a positive-source Poisson identity for t<1 yields Gp prime asymptotic (1-t)^(q-1) blowing up; hence E increases up to r=a and decreases just afterwards, while E~omega r^q at infinity. Rescaled polar-cap difference integral has convergent beta value Gamma(n/2)Gamma(1-q/2)/(sqrt(pi) q Gamma(-p/2)); r^q and (1-a/r)^q cancel offset exactly. Independent exact three-dimensional formula checks at p=-3/2 and p=-5/4 converge two-sided to C=1 and C=2/3. Newtonian p=2-n reduces to shell theorem.

## originality

PASS

PASS best of knowledge with substantial prior dependence. Chafaï et al. 2025 Appendix C Lemma C.3 and equations C.7-C.8 already give the whole spherical Riesz-potential hypergeometric profile and derivative formulas; the profile/formula itself is NOT new. Inspected Appendix C.3.1 smoothness analysis gives finite-derivative ranges at contact, but does not explicitly state the fixed-center weighted surface-monotonicity iff threshold plus exact scale-free cusp coefficient. Those require extra sign, beta-limit and radius-scaling analysis. A short prior derivation of precisely these consequences is a material residual risk.

## value

PASS

PASS. A clean necessary-and-sufficient all-dimensional threshold and universal positive non-Lipschitz contact-cusp constant is an informative sharp boundary for weighted-perimeter monotonicity and regularity, even though the underlying potential has a classical hypergeometric expression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
