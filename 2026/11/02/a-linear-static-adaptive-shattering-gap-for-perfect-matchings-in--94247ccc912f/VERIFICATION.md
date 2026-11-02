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

# Verification record

`check.py` uses graph-based exhaustive perfect-matching generation rather than simply trusting the domino-composition list. It checks all eight local matchings, edge incidences and the complete adaptive depth-three tree, then verifies the two-block connected example has 64 matchings and no bridge occurrence. The precise output from execution is supplied in `check_output.txt`.

The mathematical infinite-family certificate is a proof by parity of each even-even separating bridge and independent product choices. These steps do not require exhaustive computation for every \(m\). No general unrestricted classification of all perfect-matching graph concept classes is claimed. Scientific priority cannot be certified by keyword searches or finite checking.
