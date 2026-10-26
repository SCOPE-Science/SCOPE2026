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

# Reproduction and scope

A C++17 verifier enumerates every projective point over the first seven extensions of \(\mathbb F_2\) in explicit binary polynomial quotient fields. This is finite corroboration of the projective point counts, not proof of the zeta identity over all extensions. Run the two standalone included programs exactly as specified in `RESULT.md`.

The accompanying Python arithmetic checker verifies the five character weights, the single length-ten orbit in the character group of order eleven, the Fourier multiplicities, the determinant sign relation and the closed all-extension expression. It does not implement a general cohomology library: the tame fixed-point formula, Weak Lefschetz, Gauss--Bonnet, Poincare duality and Weil trace formula remain mathematical proof inputs.

The mathematical conclusions hold for the fixed smooth \(\mathbb F_2\) cubic threefold in `RESULT.md` and are not asserted for its general twists or for its line parameter space. No independent audit or certification is represented.
