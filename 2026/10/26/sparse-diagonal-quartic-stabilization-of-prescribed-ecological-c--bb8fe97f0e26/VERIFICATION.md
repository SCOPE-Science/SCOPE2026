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

# Verification of the sparse diagonal stabilization theorem

Run `python verify.py` using Python 3 and the standard library. The fixed-seed generator produces 1,400 rational systems with one to seven species, including mixed-sign intrinsic and pairwise coefficients, positive rational target abundances and margins. Every instance checks the explicit parameter construction, strict coefficient signs, fixed-point equalities, two algebraically independent expressions for the Jacobian diagonal, exact row Gershgorin bounds, and a sufficiently large absorbing-box threshold. The program additionally verifies both single-monomial scalar obstructions.

Observed output:

`PASS: 1400 exact rational systems and both one-monomial obstructions`

The proof in RESULT.md, not finite sampling, establishes universal correctness. The main steps requiring mathematical rather than computational validation are: the Gershgorin half-plane implication; the upper Dini derivative of the maximum active coordinate; polynomial domination for all abundances above the threshold; and the scalar derivative obstruction for the restricted diagonal intervention class.

This is an internal scientific reproducibility check. Independent scientific audit and independent validation have not been performed.
