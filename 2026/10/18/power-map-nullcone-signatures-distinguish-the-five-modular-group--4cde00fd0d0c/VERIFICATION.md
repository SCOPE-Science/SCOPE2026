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

Run `python verify.py` with Python 3 and NumPy installed (tested using a NumPy 2-series runtime). The program enumerates every \(k\)-valued algebra element for \(k=\mathbb F_2\) and \(k=\mathbb F_4\), constructs each group multiplication table independently, multiplies in the group algebra, and checks the three power-map fiber cardinalities and the augmentation condition. It ends in `ALL_ORDER_EIGHT_OK`. A failure raises `AssertionError`.

All ten full algebra enumerations succeeded in the originating test environment. No finite enumeration establishes the quantified arbitrary-field theorem; the proof in `RESULT.md` does so. The first-public dates are those recorded in the primary literature. Geometric assertions are about reduced loci, not the schemes cut out by the non-radical square/cube equations. No independent audit was performed.
