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

The proof was replayed from the published symmetric determinantal degree product. The critical algebraic steps are:

1. Consecutive degree quotient:
\[
\frac{S_{n,n-c-1}}{S_{n,n-c}}
=\frac{c!}{(2c+1)!}\prod_{j=0}^{c}(n-c+2j).
\]
2. Dividing consecutive quotients gives the exact \(Q_{n,c}\) product.
3. Dividing \(Q_{n,c+2}\) by \(Q_{n,c}\) gives the stated rational expression; cross multiplication leaves \(4n^2-1\), so strictness is symbolic and uniform.
4. The Gamma rewrite follows from the step-two products, and the asymptotic uses \(\Gamma(x+1/2)/\Gamma(x)\sim\sqrt{x}\).

`artifacts/verify_symmetric_curvature.py` independently checks 561 degree/curvature identities and 6,786 parity-step identities with exact integer and rational arithmetic. `artifacts/verification_output.txt` records the replay output. The floating-point convergence checks are regression evidence only and are not used to justify the infinite theorem.

The claim does not assert an exact finite sign on the critical asymptotic scale, and it does not claim full one-step monotonicity across alternating corank parity.
