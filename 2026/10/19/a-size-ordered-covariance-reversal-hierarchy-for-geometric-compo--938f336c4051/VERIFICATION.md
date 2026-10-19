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

# Mathematical verification

The companion file `verify.py` is a standalone Python 3 script using only the standard library. Execute it with `python verify.py` in the same directory as the result. It emits `PASS; verification groups (416, 540, 10944, 224) total 12124` if all assertions succeed.

The four check groups are: 416 uniform-word conditional regressions for all prescribed counts in finite cyclic lengths; 540 exact rational comparisons of independently inclusion–exclusion-enumerated binary gap events against the closed mixed moment; 10,944 direct breadth-first-search connected-component comparisons on finite rational point placements and radii; and 224 numerical limiting-formula and critical-scale checks.

The script does not certify the infinitely quantified asymptotic theorem. That conclusion requires the symbolic Dirichlet simplex-translation identity, finite inclusion–exclusion, uniform finite-order asymptotic expansions, and analytic positivity argument written in `RESULT.md`. Finite numerical approximation and exhaustive tests over bounded input sizes are not used as impossibility or uniqueness proofs.
