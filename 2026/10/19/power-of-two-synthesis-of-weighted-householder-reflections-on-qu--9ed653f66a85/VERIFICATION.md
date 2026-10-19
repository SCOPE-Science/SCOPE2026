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
# Verification and limits

The full theorem follows from the invariant radial subspace and \((k-1)\)-fold angular subspace, the identification of these operators with the even and odd reflection sectors of the normalized path \(P_{2L+1}\), and established path endpoint transfer theorems. The exact matrix identity \(\|e^{-itH}-R\|=\|e^{-it\mathcal L(P_{2L+1})}-J\|\) is all-time, not an asymptotic approximation. Orthogonal decomposition proves the all-time cross-terminal amplitude identity and sharp probability bound.

Run `python VERIFY.py` with NumPy. The program independently constructs weighted adjacency/degree matrices, checks 378 propagator pairs covering positive random weights, different arm counts and lengths, and compares all cross-terminal amplitudes. It tests the exactly realizable length-one gate and one sequence of improving approximations for length two. Passing numerical tests do not prove the criterion for all lengths; non-power-of-two impossibility follows from the published path classification.

No independent audit, formal proof certification, or experimental validation has been performed. The published normalized-path transfer classification is treated as an explicit input, and the full thesis PDF was not accessible in this examination.
