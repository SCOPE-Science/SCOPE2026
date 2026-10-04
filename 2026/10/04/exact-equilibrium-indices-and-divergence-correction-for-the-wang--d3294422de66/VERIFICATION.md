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

Run `python3 verify.py` from the same directory. The script uses only the Python standard library and exact `Fraction` arithmetic.

It proves \(e^{2.83}<17<e^{2.84}\) with rational Taylor bounds, hence \(2.83<\log 17<2.84\) and \(1.68<\sqrt{\log 17}<2\). These bounds are then used to verify \(B_->0\) and the strict inequality \(AB_\sigma-C<0\) for both base cubics. The script also verifies the signs needed for the fiber eigenvalues. Successful replay prints `VERIFY_OK`.

The checker does not integrate trajectories, estimate Lyapunov exponents, or certify basin geometry. Those are outside the accepted claim.
