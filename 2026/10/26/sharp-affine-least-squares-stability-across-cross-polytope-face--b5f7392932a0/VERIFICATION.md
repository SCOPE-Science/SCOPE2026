---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The included `verify.py` is standalone and uses only Python's standard library. Running `python verify.py` printed `PASS: 1984 exact checks`.

The checker independently evaluates the signed beta positive-part integral by a binomial expansion with exact rational fractions, compares it with the claimed closed form over all integer pairs \(2\le d\le31\), \(1\le s\le d\), verifies coordinate moment normalization, strict monotonicity, and uniform dimension bounds, and checks four small exact instances. The complete parameter ranges outside these finite calculations are proved in RESULT.md by a Dirichlet covariance identity, strict convexity argument, direct beta integration, a derivative inequality and a two-sided Taylor bound. There is no claim of infinite computational certification or of an independent audit.

The main discovery applies only to the intermediate skeletons \(2\le s<d\). The vertex case is elementary, and the full-facet case is consistent with an earlier radial limiting formula; neither endpoint is asserted as independently new.
