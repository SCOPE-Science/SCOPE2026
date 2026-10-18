---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each k<=n, write Sn=Sk+(Sn-Sk); centered future independent of event {Sk>0}, so E[Sn 1(Sk>0)]=E[Sk 1(Sk>0)]=E|Sk|/2 by symmetry, valid for symmetric integrable increments even with ties. Summing gives exact covariance. With continuous iid symmetric increments Sparre–Andersen yields P(An=r)=binom(2r,r)binom(2n-2r,n-r)/4^n and Var An=n(n+1)/8, hence correlation sqrt(2)*sum E|Sk|/(sigma*n*sqrt(n+1)). CLT + bounded second moments ensure uniform integrability of |Sk|/(sigma sqrt k), giving limit 4/(3sqrt(pi)); Brownian identity by Fubini/conditional mean and Var Gamma=1/8. Independent exhaustive symmetric ±1 walks n<=11 confirmed the general covariance identity, not the continuous-increment arcsine marginal.

## originality

PASS

The well-known Sparre–Andersen and Erdős–Kac laws are marginal sojourn-count laws and do not alone determine covariance with terminal displacement. Ivanovs discusses occupation-time distributions under endpoint conditioning, but its inspected propositions establish distributional identities between random times, not this first mixed moment or the all-symmetric-increment correlation constant. Brownian global-time joint laws address three times, not B1. The exact finite-n covariance for all symmetric integrable increments and universal finite-variance asymptotic survive best-of-knowledge comparison, though broad classical fluctuation literature poses residual overlap risk.

## value

PASS

Occupation fraction is a canonical arcsine functional, while terminal displacement is a canonical additive endpoint. Their exact finite-n mixed covariance and universal nonzero correlation 4/(3sqrt(pi)) quantify dependence that marginal arcsine and CLT statements leave undetermined. This is a motivated joint-statistic fact valid for a broad finite-variance universality class, not simply a renaming of the arcsine marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
