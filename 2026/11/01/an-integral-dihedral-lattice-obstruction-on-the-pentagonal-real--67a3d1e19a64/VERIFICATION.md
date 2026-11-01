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

# Reproducible checks

Run `python3 verify.py` using only the Python 3 standard library. The recorded `verify_output.txt` results from execution of that program. The program exhaustively enumerates the ten disconnected induced subsets of the five-cycle, checks the signs of their order-two stabilizers, verifies the dihedral relations, and checks all ten rational characters. It then independently builds all 32 zero-cells, 80 one-cells and 40 two-cells of the cubical surface, verifies boundary composition is zero, and computes mod-101 ranks 31 and 39. It also checks that a reflection minus the identity has rank four modulo two on the ten-dimensional signed subset lattice. The proof establishes the integer module rather than inferring it from finite-field ranks.

The test does not verify originality or publication status and does not constitute independent mathematical validation.
