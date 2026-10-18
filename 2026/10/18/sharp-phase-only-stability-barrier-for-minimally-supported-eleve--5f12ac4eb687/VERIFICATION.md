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

The complete proof relies on finite combinatorics and a regular-eleven-gon extremal inequality, neither of which is inferred from floating-point experiments. Run `python check.py` from a directory containing the extracted standalone file. The checker enumerates all \(330\) four-element supports in \(\mathbb Z/11\mathbb Z\), verifies all fully covering supports have the exact \((2,1,1,1,1)\) difference profile, evaluates each of \(121\) ambiguity coefficients of the two explicit windows, and confirms the analytic formulas with a small tolerance. The checker does not enumerate all possible continuum phases, which are handled by the analytic regular-polygon argument. No independent audit has been performed.
