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

Fix D,ell,kappa>0 finite and real drift mu. The renewal probability of absorption before exponential reset gives T=(ell^2/D)[(1+eta*w)e^{w+sigma*m}-1]/z^2 with eta=2D/(kappa*ell), m=|mu|ell/(2D), w=sqrt(m^2+z^2), z=ell sqrt(r/D). Set y=w-m, q=e^{-(sigma+1)m}; the derivative of F(y)/[y(y+2m)], F=(1+eta(m+y))e^y-q, has N(y)/y^2 strictly increasing from -infinity to +infinity (positive Taylor coefficients above order two and derivatives of negative reciprocals). At m=0 the analogous F/y^2 derivative also has one crossing. Coercivity proves the single positive nondegenerate global optimum. Exact identity tau_+=e^{2m}tau_-+(e^{2m}-1)/z^2 and unique derivative crossing imply r_away>r_toward. Uniform compactness and the nondegenerate limiting profile eta e^y/(2y) imply y_+=1-1/(2m)+O(m^-2), y_-=1-(1/2+1/(e eta))/m+O(m^-2), hence r_away=v/ell+O(v^-1), r_toward=v/ell-kappa/(e ell)+O(v^-1). Verified sign and O(1/m) offset numerically from independent bisection for m=1,10,100,2000, finite checks only. The singular kappa=infty regime excluded.

## originality

PASS

Best-of-knowledge novel complete positive optimizer uniqueness and exact nonzero strong-drift orientation gap for a finite delta-killing sink; the MFPT formula, related perturbation and numerical evidence are expressly prior. The same-model Mazzolo paper was not read fully, leaving a significant risk of stronger appendix coverage.

## value

PASS

Finite reactivity changes the qualitative optimizer behavior versus perfect absorption; proving all-drift uniqueness, strict orientation ordering and the asymptotic constant gap is a motivated complete optimization answer for a physical first-passage model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
