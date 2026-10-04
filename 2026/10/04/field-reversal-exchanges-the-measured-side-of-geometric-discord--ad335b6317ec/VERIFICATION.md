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

The exact proof checks the operator identity \(SXH(B,b)XS=H(-B,b)\), propagates it through the Gibbs functional calculus, and then applies local-unitary invariance together with subsystem-swap covariance of one-sided Hilbert--Schmidt geometric discord. The claim is therefore analytic and does not depend on numerical sampling.

The accompanying `artifacts/verify.py` independently evaluates the \(4\times4\) Hamiltonian and both directional Bloch-matrix GQD formulas. Its stored output reports `VERIFY_OK` for 80 random state-covariance checks, 160 directional-discord exchange checks, and 40 homogeneous-field evenness checks. The largest reported floating-point discrepancy is \(2.225\times10^{-16}\).

The numerical checks are finite and are not treated as an infinite proof. The theorem is limited to \(T>0\) and the Hamiltonian and directional Hilbert--Schmidt GQD specified in the result.
