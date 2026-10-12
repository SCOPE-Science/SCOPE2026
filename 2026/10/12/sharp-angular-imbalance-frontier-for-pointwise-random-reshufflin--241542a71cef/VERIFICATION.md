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

# Reproduction and logical boundaries

From this package directory, run `python3 verify.py`. The script uses only the Python standard library and exact rational arithmetic, with no external datasets or downloads. It separately computes two-step updates for both protocols, compares them with closed-form formulas, checks the angular boundary against signed directional gaps, and reproduces the exact rational witness.

Analytically verified identities include the two expected Gram operators, the Loewner threshold from the invertibility of the two-functional map, the strict bisector Rayleigh-quotient comparison, and the universal factor-two envelope with its limiting witness. The proof is provided in `RESULT.md`. A finite set of rational checks is not an exhaustive verification of all real parameters, cannot establish absence of earlier literature, and does not evaluate longer trajectories or hardware numerical effects.
