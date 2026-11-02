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

The real-parameter proof is given in `RESULT.md` and relies on explicit branch identities, not sampled data. `check_exact.py` is a standalone Python 3 script requiring SymPy for exact symbolic matrix identities. To reproduce: `python3 check_exact.py`.

The script actually ran and printed `EXACT_ARITHMETIC_REGRESSION_OK 11817`. It uses rational arithmetic to replay 30 strictly positive parameter pairs on an entire 17-by-17 rational state grid, constructs a nonzero fourth iterate on resonance, and compares exact off-resonance return sequences through multiple iterations. It additionally checks the symbolic rank-one resonance identity.

These finite regressions cannot prove the universal claim over arbitrary real parameters. The analytical proof separately establishes all quantifiers and handles boundary conditions. Independent scientific audit, publication-priority certification, and numerical-noise robustness have not been performed.
