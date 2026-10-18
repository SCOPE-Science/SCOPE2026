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

Run `python verify.py` in the same directory. The script uses only the Python standard library, evaluates the explicitly defined quadrature at every integer \(4\le N\le1000\), checks positivity and endpoint occupation, and tests cancellation of the two complex Fourier moments to a numerical tolerance of \(10^{-10}\). The odd-grid exclusion certificate is checked on every interior node at the immediately narrower window; six symbolic-style test equalities are evaluated with exact rational fractions.

Observed execution:

`VERIFY_OK 997 cyclic orders, 1994 complex moments, 6 exact rational cancellation identities`

The universal proof is the semicircle obstruction, the cubic nonnegative arc certificate, and the exact algebraic construction in `RESULT.md`. Floating-point calculations and finite loops are not independent proof of the all-\(N\) statement. An independent scientific audit has not been performed.
