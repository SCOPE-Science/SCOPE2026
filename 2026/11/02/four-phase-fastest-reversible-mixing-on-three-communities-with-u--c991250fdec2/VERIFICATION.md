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

# Reproduction and scope

Run `python3 verify.py` with Python 3. No third-party Python modules are required. It constructs full transition matrices with rational stationary probabilities, verifies nonnegativity, exact row sums, exact detailed balance, the four distinct spectral subspaces, all displayed rational formulas and optimal symmetric flow intervals. Actual replay completed successfully: **18,663 counted exact rational validation components** across **599 rational stationary masses**, including **54 complete transition matrices**. The component count is reported by the executed standalone script `verify.py`.

The finite battery is diagnostic, not a proof for every real class mass or every chain. Global optimality is proved in `RESULT.md` using convex averaging and exact scalar minimax inequalities. Literature noncoverage is a qualified search assessment, not a theorem of uniqueness. Independent audit is not performed.
