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

PASS. Multiplying by x gives yx=N(x)+a. For y≠0, taking norm reduces every preimage uniquely to a nonzero root r in F_q of r²+(Tr(a)-N(y))r+N(a)=0; conversely x=(r+a)/y has norm r and returns exactly y. The zero target is a q+1 norm fiber precisely for a in F_q*. For odd q the discriminant D(z)=(z-Tr(a))²-4N(a), split-character sum -1 and distinguished D(0) classes yield all zero/one/two-root norm counts; for even q absolute trace distinguishes the base/outside cases and double root z=Tr(a). Multiplying each nonzero norm class by q+1 targets and counting coefficients reproduces all table entries. An independent finite-field enumeration of every nonzero a and every nonzero x for q=2,3,5,7,11 confirmed all 5 cases, class sizes and image/fiber histograms (17,353 evaluated (a,x) pairs). The algebra proves all prime powers, not this finite experiment.

## originality

PASS

Best-of-knowledge separate statement/implication comparison supports survival of the claimed exact classification; priority is bounded by named inspected sources. Unavailable/abstract-only sections are explicitly reserved as risks, not treated as proof of novelty.

## value

PASS

PASS. A uniform full-fiber classification for the natural Frobenius-plus-reciprocal map across every coefficient and characteristic determines image size, high-multiplicity exceptional fibers, norm-square phase split, and exact rare bijections. The complete parameterized spectrum is more informative than generic degree bounds or a single value-set cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
