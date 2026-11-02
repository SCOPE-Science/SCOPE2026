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

# Reproducibility and limits

From the directory containing `RESULT.md` and `checker.py`, run `python3 checker.py`. The script uses the Python standard library only and successfully printed `PASS: 7584 finite assertions; independent spherical grid integration included.` The direct spherical-grid integration counts physical detection events using uniformly gridded surface coordinates and does not call the spherical-cap formula. It is compared against the derived analytic expression at six nontrivial parameter choices. The script also tests boundary regimes, the exact lens derivative, symmetry, and worst-orientation envelopes.

The proof is not a computer enumeration. Continuous monotonicity follows from the exact derivative of equal spherical lens area; the optimizer's equality cases follow from its support. The deterministic numerical tests cannot verify an uncountable set of orbit orientations or all real parameters. The complete analytic statement, assumptions, and critical-limit argument appear in `RESULT.md`.

Only a self-review has been performed. Independent audit and observational verification have not been performed. Existing published methods address more realistic missions with photometric and operational constraints, to which the exact optimality statement must not be generalized.
