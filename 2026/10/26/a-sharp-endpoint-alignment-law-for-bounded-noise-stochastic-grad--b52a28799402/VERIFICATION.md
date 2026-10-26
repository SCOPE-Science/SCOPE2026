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

# Verification record

The exact domain is arbitrary Euclidean dimension \(d\ge1\), radius \(q>0\), true vector \(g\), and conditionally centered error supported on the closed radius-\(q\) ball. The theorem does not require symmetric noise or coordinate independence.

The critical proof checks are: the affine pointwise support inequality for \(0<\|g\|_2/q\le1\), strict concavity of the one-variable function \(F_r\) on \([-r/2,1]\), expectation eliminating the noise projection, and projection monotonicity for larger gradients. Antipodal noise supplies equality. The subthreshold counterexample uses exact clipping saturation, not a first-order approximation.

Run `python3 check_clipping.py` from the extracted package directory using Python's standard library. The test checks 96,000 random pointwise configurations, exact rational endpoint extremizers, rational subthreshold drift identities, and the explicit variance/Doob certificate. The last checked execution printed `CHECK_OK 96000 pointwise samples; rational extremizers, deadzone and Doob bound passed`.

The positive-probability pathwise statement relies on the analytical inequality \(\mathbb P(\sup_n|S_n|\ge\delta)\le V/\delta^2\), martingale convergence and Gaussian non-atomicity. The checker does not simulate infinitely many steps or certify those analytic theorems. The zero-drift example itself is already present in the 2020 literature; the new positive endpoint alignment bound is the central contribution. External independent audit has not been performed.
