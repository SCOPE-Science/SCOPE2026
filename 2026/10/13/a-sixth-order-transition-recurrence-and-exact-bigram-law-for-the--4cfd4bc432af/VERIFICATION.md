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

The exact verifier reconstructs the published non-erasing morphism and its output map, then forms the closed adjacent-letter-pair state space. It checks \(26\) letter states, \(68\) adjacent-pair states, and hence a \(94\)-dimensional integer linear count state.

For the morphic prefixes \(W_m\), it verifies the initial values and checks \(94\) consecutive residuals of each claimed recurrence. Because every scalar residual is a matrix coefficient of powers of the same \(94\)-dimensional linear map, Cayley--Hamilton extends the zero residuals to every later index.

The verifier also constructs the incidence matrix on the \(25\)-letter growing component and checks that its twentieth power is strictly positive. This is the finite primitivity input used with standard Perron--Frobenius substitution-frequency theory.

As a separate normalization check, the original nested recurrence is evaluated directly through \(200000\) first differences and its four adjacent-pair counts are compared with the exact limiting formulas. This finite replay is not used to infer the infinite theorem.

Limit: the verification assumes the source theorem identifying the recurrence difference word with the explicit morphic image. It does not re-prove that published identification or any statement about factors of length at least three.
