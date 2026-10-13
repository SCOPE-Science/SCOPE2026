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

The proof was reconstructed symbolically from the standard depth-one Anderson least-squares definition. With \(A=I-\Lambda\), the residual pair is \(f_0=-Ae\) and \(f_1=\Lambda f_0\). The scalar least-squares objective is therefore \(\sum_i a_i^2e_i^2(1-\beta a_i)^2\), whose strictly positive second derivative gives the unique coefficient \(\beta=(\sum_i a_i^3e_i^2)/(\sum_i a_i^4e_i^2)\). Direct substitution yields the coordinate factorization used in the result.

The bundled `verify.py` uses only Python standard-library exact rational arithmetic. It checks the coefficient formula against an independently expanded quadratic, checks the prediction and mixed-output identities on many rational diagonal contractions, verifies the strict weighted-mean ordering whenever two active gaps differ, and exactly replays the two-dimensional witness. For that witness it verifies that the affine map sends nonnegative inputs to nonnegative outputs, that the first two Picard images are positive, and that the first accelerated coordinate is negative at both \(\omega=0\) and \(\omega=1\). Since that coordinate is affine in \(\omega\), it is negative on the entire interval.

The computation does not certify nonlinear maps, later Anderson steps, floating-point behavior, or literature novelty. Those are outside the mathematical claim. The universal claim is analytic; the finite replay is not treated as exhaustive evidence.
