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

# Verification scope

The analytical argument derives the mixed squared-coordinate covariance from a stationary two-sided Poisson process, exact uniform-sphere fourth moments, and elementary exponential renewal recursions. The coefficient sign proof and Descartes' rule establish existence and uniqueness of a positive transition root for every allowed parameter value.

Run `python3 check.py` from the same directory. It uses only the Python standard library and performs 2,731 exact-rational assertions, independently comparing three formulas: a Markov-generator fourth-moment closure, the Poisson-interval renewal calculation, and the final explicit rational polynomial. Additional checks include axis symmetry, exact equality of the isotropic critical rate, strict pre- and post-threshold signs for rational examples, the nonpositive polynomial at the sharp lower bound, and the frozen-orientation limit.

These checks are finite parameter tests. They do not certify statements for all real parameters; that role belongs to the displayed derivation and coefficient sign argument. Thermal-noise independence follows from conditional factorization of independent Gaussian bath contributions and is not inferred from numerical checks. The uniqueness conclusion is analytical, not extrapolated from root searches. No independent audit is represented by this verification record.
