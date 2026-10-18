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
# Verification evidence

`verify_small_ball.py` is a standalone reproducible check requiring Python, SymPy and mpmath. It was executed from its actual source path, using deterministic random seeds and 70 decimal digits for the wedge-kernel checks. It reports:

- Exact-rational computation of the source's three-state Markov-chain covariance \(C=\frac19\bigl(\begin{smallmatrix}14&-13\\-13&14\end{smallmatrix}\bigr)\), positive definiteness and zero-sum covariance.
- 700 finite path and endpoint inclusion checks (including 100 distinct 41-point random grids and 100 constrained 121-point grids).
- 15 high-precision checks of the Bessel heat-kernel leading term at five correlation parameters, plus the exact critical exponent \(8\).
- The explicit noncyclic example exponent \(18.523774800939642819\ldots\).

These finite checks do not certify any pathwise theorem on uncountably many paths or the infinite heat-kernel series. Those parts follow from the algebra and analytic arguments displayed in RESULT.md, including the positive interior-terminal lower event. The exact prefactor for the probability of the last-passage lower tail is not determined; neither independent validation nor independent audit has been performed.
