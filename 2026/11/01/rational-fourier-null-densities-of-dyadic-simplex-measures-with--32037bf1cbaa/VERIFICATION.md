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

The standalone `verify_density.py` checker recomputes all binomial transition probabilities with exact rational numbers, solves the finite recursive hitting equations, and checks the density \(11197/35433\). Direct enumeration of all integer frequencies modulo two and four verifies first-zero counts \(35\) and \(5075\) out of \(128\) and \(16384\), respectively. An additional exhaustive modulus-eight residue test gave first-hit counts \(573440,76160,11795\), agreeing with the first three rational generating-function coefficients.

The analytic argument establishes infinite-product nonvanishing when there is no zero factor, the prime-power cyclotomic cancellation criterion, and geometric decay of live-state mass. The checker validates specified exact finite computations but is not an infinite proof. Source comparisons remain bounded, and independent mathematical audit has not been performed.
