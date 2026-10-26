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

`verify.py` reconstructs the sixteen stationary correlation equations from the finite model and computes exact Cramer determinants, reproduces the published two- and three-site formulas, verifies the full four-site initial-dephasing derivative and its positive denominator, and proves the unique threshold via positive coefficients. In the equal-coupling case it checks every coefficient sign of the current derivative and uses disjoint rational isolation brackets plus Descartes' rule to certify one positive optimizer. Its large-field limit is symbolically checked.

`crosscheck_lindblad.py` independently constructs the full four-spin Hilbert-space Lindblad generator, solves the stationary density matrix, and compares spin currents at five parameter choices including different boundary couplings. The largest absolute disagreement in the checked values was below \(10^{-10}\). These are finite exact-symbolic and finite-state numerical validations of an analytic theorem, not independent scientific audit.

Neither script checks any longer chain, uniqueness of the contact value maximizing critical tilt, nor global unimodality for boundary couplings other than \(G=1\). No external independent audit was performed.
