---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

In exact source FEPW survival S(x)=exp[1−exp((τx)^η)−(κx)^φ], η,φ>0 and defining section τ,κ≥0. On τ,κ>0, set a=τ^η>0,b=κ^φ>0: H(x)+1=exp(a x^η)+b x^φ. The exponential dominates every power at x→∞; log log(H+1)/log x→η, log(H+1)/x^η→a; subtract exp(a x^η), the positive power residual uniquely identifies φ and b. At τ=0,κ>0 η disappears and law is Weibull; τ>0,κ=0 φ disappears and exponential-power law remains; τ=κ=0 S≡1 improper as finite positive lifetime. Distinct proper strata excluded from equality by growth distinction exponential vs polynomial and positive residual. Direct independent boundary substitutions and asymptotic tests confirm; no finite computations used as proof for all x. This corrects Proposition1 if interpreted on initial nonnegative scale domain, while strictly positive Bayesian model remains identifiable.

## originality

PASS

The original Ghazal 2026 AIMS article is SAME model and its Proposition1 asserts parameter identifiability after initially allowing zero scales, but does not correctly stratify erased shape parameters. Original Bayesian positive-prior section later imposes strictly positive scales, consistent with interior theorem. The classification reconciles the conflicting domains, excludes improper double zero, and proves pairwise disjointness of proper stratum laws. Related additive Chen–Weibull papers involve similar hazards but accessible portions did not provide this FEPW four-parameter quotient. Standard boundary-identifiability principle is known, so priority limited to correcting this exact stated domain, not general identifiability theory.

## value

PASS

Specific published identifiability Proposition1 is false on its own defining closed scale domain. Full classification distinguishes two lower-dimensional valid lifetime submodels, identifies precisely which shape is unobservable, proves positive-interior injectivity, and excludes an improper limiting law. This gives practical model selection and inference-domain clarity; a cheap zero substitution alone is elementary, but reconciling all strata with rigorous interior recovery and cross-stratum noncoincidence is substantive source-specific boundary repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
