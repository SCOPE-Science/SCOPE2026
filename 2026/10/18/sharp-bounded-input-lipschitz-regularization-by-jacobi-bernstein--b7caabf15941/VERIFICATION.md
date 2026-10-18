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

# Reproducibility and limits
Run `python3 checker.py` using Python 3 standard library only. The program performs exact rational integration of integer-parameter adjacent beta-density differences, verifies crossing-point formulas and endpoint comparisons, evaluates exact derivative-polynomial integrals, and independently approximates selected interior signed-kernel absolute integrals. Observed result: `PASS: 3202 exact and numerical finite checks`.

For arbitrary real \(a,b>0\) and unbounded degree, the claims depend on the complete analytic argument in `RESULT.md`; testing finitely many integer parameters does not certify an infinite claim. The reported norm acts on real essentially bounded measurable inputs. The maximizing point is an extremum of a derivative functional; a single input is not asserted to maximize every evaluation point simultaneously. The cited first public source date is 2009-11-22. Historical originality remains qualified by inaccessible earlier complete texts. Independent audit has not been performed.
