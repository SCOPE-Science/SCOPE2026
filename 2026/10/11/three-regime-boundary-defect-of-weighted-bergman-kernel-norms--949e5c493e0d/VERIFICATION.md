---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. For fixed alpha>-1 and 1<p<infinity, beta=alpha+2, a=p beta/2, c=(p-1)beta>0, d=(2-p)beta/2, the normalized radial moments are (n!)/(beta)_n; hence ||K_z||_p^p=2F1(a,a;beta;r^2). Euler transformation gives s^c||K_z||_p^p=2F1(d,d;beta;1-s). Gauss formula yields C=Gamma(beta)Gamma(c)/Gamma(a)^2 and L=C^(1/p). At 0<c<1, connection formula contributes D/C s^c where D=Gamma(beta)Gamma(-c)/Gamma(d)^2<0; at c>1 the finite derivative is C d^2/(c-1), giving -d^2 s/[p(c-1)]; at c=1 the zero-balanced derivative integrates to -d^2 s log(1/s)/p; p=2 has d=0 and exact constant 1. Independent high-precision samples across subcritical, critical, supercritical, and Hilbert parameters reproduced coefficients as s decreased. No uniformity as parameters vary with s is claimed. The theorem is a fixed-parameter analytic result, not extrapolation from numerical tests.

## originality

PASS

Best-of-knowledge PASS after exact-object and logical-implication comparison. The strongest exact-object weighted Bergman norm source gives only two-sided Forelli–Rudin bounds and sharp leading boundary constant. Classical 2F1 connection identities imply coefficients after a substantial specialization, but the particular parameter-threshold normalized Bergman norm theorem is not formulated as a prior theorem in inspected exact-object work. A general special-function reference could mechanistically imply the computation; this substantially limits claimed novelty: new formulation is operator-relevant boundary regime law, not a new 2F1 identity. An indexed-search miss alone is not treated as novelty proof.

## value

PASS

PASS. After stripping a known leading singularity from the canonical weighted Bergman reproducing kernel Lp norm, the first surviving term has three genuinely distinct boundary regularity regimes separated by (p-1)(alpha+2)=1, with exact constants and Hilbert cancellation. This supplies mathematically usable normalization error and boundary smoothness data in the same setting used by contemporary operator boundedness/compactness arguments; it is more than a renamed textbook identity, although connection formulas are classical. No downstream essential-norm theorem or parameter-uniform statement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
