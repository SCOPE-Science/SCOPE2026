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

# Reproduction and verification limits

Run `python3 verify.py` with standard-library Python 3. The script minimizes the actual truncated-affine loss plus quadratic proximal model by exact-rational comparison of all model vertices and the kink, independently of the closed-form update. It checks 64 admissible rational parameter pairs and 10,112 exact proximal minimizations. It also verifies the strict branch itinerary, period-three point equalities, local multiplier criterion, and explicit rational witness.

For the universal statement, see the algebraic proof in `RESULT.md`: the exact update reduces to two affine branches on the invariant unit interval, the branch-order differences factor with strictly positive denominators, and all three orbit equations are identities. Rational grids alone cannot establish universality. The all-period and scrambled-set conclusions rely on Li and Yorke's stated 1975 interval-map theorem, not on finite enumeration. No independent audit or external formal certification has been performed.
