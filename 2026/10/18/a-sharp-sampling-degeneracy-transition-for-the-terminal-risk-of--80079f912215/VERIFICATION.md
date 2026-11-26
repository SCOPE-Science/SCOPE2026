---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Differentiating the two proximal objectives gives slopes q1=p/(p+gamma), q2=2(1-p)/(2(1-p)+gamma), with affine offsets 0 and 1-q2. Both slopes are strictly less than one; conditioning on the iid next map gives triangular first- and second-moment recurrences with diagonal factors strictly less than one, so the limiting risk exists from every prescribed start. Independently recomputed the second moment centered at 1/3 and its exact sign factorization against 1/9 (the sign of the difference is the opposite of F); the endpoint limits are 4/9 and 1/9. Descartes’ rule, positivity of F(p,0) and the negative leading coefficient give exactly one positive gamma-root for each interior p. F(4/5,1)>0, and the Bernstein certificate gives F(p,2)<0 uniformly on the closed interval. Taking a maximizing sequence of gamma-roots and passing to a convergent subsequence rules out 2 and, since the supremum exceeds 1, also rules out p=0,1. Thus F=F_p=0 at a legal contact. Recomputed the requisite resultant via quartic discriminant invariants; its positive zeros are those of the frozen quintic. That polynomial is negative up to 1 and strictly increasing thereafter by the displayed derivative bounds, with opposite signs at 1 and 2. Below the contact the risk dips strictly below both endpoint limits, so it attains its infimum inside; at contact the infimum is attained at equality; above contact the strict interior inequality and the p→1 limit give nonattainment. The frozen script was inspected, not executed; the independent exact algebra and root bracket passed with `python /workspace/reproductions/3.py` (SymPy). No finite iteration tests are needed for the continuum conclusion.

## originality

PASS

The strongest indexed analogue uses the same stationary squared-error objective and includes exactly the same quadratic pair, but omits inverse-probability scaling and varies curvature rather than the proximal parameter. The primary SPPM-NS paper supplies the actual probability-scaled update but optimizes bounds, not this exact stationary risk. The supported distinction is the sharp gamma-quintic attainment transition for the specified inverse-probability update, not the general phenomenon of sampling collapse.

## value

PASS

The inverse-probability scaling is part of a published method. On a minimal heterogeneous quadratic pair the exact stationary objective exhibits a change in whether a legal optimum exists; this addresses a question that rate and variance-bound optimization do not settle. The exact boundary and inclusion of its equality case distinguish a legally attainable optimum from a degenerate limiting prescription. The value is as a scoped analytical benchmark, not a claim about the most useful finite-time sampler or about general objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
