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

# Exact verification
Run `python verify.py` with SymPy installed. The script constructs the specified rational Gram matrices and verifies every leading principal minor is positive and that the Gram forms reproduce the full eight-variable quartic moment difference exactly. Its successful execution certifies an algebraic inequality for all real coefficients; it does not determine the exact operator norm, treat complex inputs, or constitute an independent audit. The lower bound is obtained from the displayed explicit three-variable witness with its unique minimizing cubic root.
