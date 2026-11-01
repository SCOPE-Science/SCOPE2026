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

# Verification and scope

Reproduce with `python3 verify.py` from the extracted package. It uses Python standard-library exact fractions and factorials to confirm beta-tail/binomial-CDF equality for many dimensions, block splits, thresholds and degrees; exact multiplicity totals; a closed finite-degree determinant; and the analytically evaluated three-dimensional coefficient. Additional numerical checks compare the finite-degree negative log-determinant to the predicted rate at increasing degrees.

The analytic inference is separate: for each binomial lower tail, the method-of-types point mass yields a lower exponential bound up to \(N+1\), and Chernoff gives the matching upper exponential bound. Above the mean the CDF includes a binomial mode. Uniform entropy continuity and bounded-variation Riemann sums then give the stated remainder. Tests do not independently validate the infinite proof, and no independent audit has been conducted.
