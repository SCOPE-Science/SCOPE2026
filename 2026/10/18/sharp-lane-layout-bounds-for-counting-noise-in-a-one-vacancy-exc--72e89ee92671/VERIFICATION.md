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

# Reproduction and boundaries

Execute `python3 verify.py` using Python 3 and no third-party packages. The code reconstructs the complete single-vacancy cylinder generator and the jump-count Poisson equation with exact rational arithmetic. It tests arbitrary positive rate profiles as well as the two-valued extremal cases. The recorded run returned `VERIFIED: 18 complete-state rational generators; 4704 exact lane-layout comparisons`.

For generator calculations, the counting variance is recovered from the first and second derivatives of the longitudinal-jump tilted generator through a finite-state Poisson equation. Separately, the proposed formula is evaluated from cyclic prefix sums. Agreement is exact for every rational test. The layout enumeration checks exact rational bounds and rigidity for all balanced signs on cycles of size 4 through 14.

These computations are finite consistency checks, not substitutes for the analytical all-size proof. No calculation at lane-change rate zero is covered because the lane chain is then reducible. The strict sharp-bound classification assumes an even number of lanes, one vacancy, and two speed classes of equal multiplicity. Scientific originality is not mechanically certified by the verification program.
