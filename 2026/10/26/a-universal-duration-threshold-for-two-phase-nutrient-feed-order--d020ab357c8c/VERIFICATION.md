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

# Verification

The exact result has four independently inspectable analytic checks: (1) the substrate-order difference formula and its unique sign change; (2) strict monotonicity in time of the weight ratio for distinct initial nutrients; (3) the strictly positive paired-time integrand for zero initial substrate; and (4) evaluation of the large-initial-nutrient moment, whose sign changes only at \(D\tau=\log(1+\sqrt2)\). At equality the weight-ratio argument rules out a finite zero. All hypotheses and quantifiers are given in RESULT.md.

The standalone `chemostat_finite_feed_verification.py` was run with its bundled fixed pseudorandom seed. It compared the analytical two-block Monod integrals with adaptive quadrature for 1,000 random parameter tuples and checked the small-duration positive sign for 503 of those samples. All assertions passed. With 70-digit working precision it recomputed the example's unique zero as \(53.1340923371102330498336150935937076927\ldots\). The numerical tests are finite spot checks, not a proof that other parameter cases cannot fail and not a literature-originality certificate.

Reproduction: install `mpmath` and `scipy`, then run `python chemostat_finite_feed_verification.py` alongside the research notes. No network access is needed for the numerical checks. An independent scientific audit has not been performed.
