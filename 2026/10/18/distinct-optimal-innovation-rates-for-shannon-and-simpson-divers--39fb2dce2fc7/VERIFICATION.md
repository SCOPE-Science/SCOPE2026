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
# Reproduction of formula checks

Run `python verify.py` (Python standard library, no additional packages). The program checks finite-time normalized frequency updates against the limiting relative-age moments for seven choices of fitness advantage and five innovation multipliers, plus exact-fraction identities for fitness advantage two. It reports 128 passing assertions. A tolerance is used only for numerical finite-time convergence; at the incumbent critical rate convergence is algebraic and the program accordingly uses a looser finite-horizon threshold.

The infinite-time \(\ell^1\) convergence, uniqueness of the two optimizers, and strict ordering for **all** real \(a>1\) depend on the analytical proof in `RESULT.md`, not on this finite grid. No external independent verification is claimed.
