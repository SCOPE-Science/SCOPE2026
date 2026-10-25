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
The proof uses an exact farthest-pair component decomposition and the standard independence-complex cycle recurrence. The critical new check is the geometric-fixed-point Lefschetz argument for the antipodal half-turn, followed by the graded join-sign calculation. This establishes the infinite-family cyclic representation and does not rest on finite computation.

The included `check.py` needs Python 3 and no other packages. Running `python3 check.py` verifies all graph metric pairs in 15 rectangular-torus cases; mod-two independence-complex homology of three component cycles and the first product case; and independent fixed-simplex chain-trace formulas for every translation power in three sample rectangles. The integer module's complete validity in all parameters is proved mathematically; the script only supplies finite consistency checks.

The cycle complex formula is prior mathematics (arXiv:2307.12401), and the setting of torus-grid Vietoris–Rips complexes is motivated by arXiv:2502.07134. The full automorphism-group action, other scales, and an equivariant homotopy equivalence are not claimed.
