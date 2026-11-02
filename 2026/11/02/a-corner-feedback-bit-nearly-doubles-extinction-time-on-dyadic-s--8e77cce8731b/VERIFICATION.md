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

# Verification scope

The proof is in `RESULT.md`. Running `python3 corner_grid_verify.py` with a standard Python 3 interpreter reconstructs the binary update matrix from four-neighbor grid adjacency and optional feedback at \((0,0)\), with no precomputed matrices. It computes and compares binary ranks for all powers until stabilization at \(a=2,3,4,5\), separately for the unperturbed and modified dynamics. The corresponding numbers of sites are \(9,49,225,961\). The code also directly follows every one of the \(512\) configurations on the smallest grid and checks the exact first-entry census \((2,6,8,16,32,64,128,256)\); \(4000\) further pseudorandom trajectory checks cover the next grid size.

`verification_output.txt` records the successful execution. Finite testing cannot prove the all-parameter rank formula or establish literature originality. The characteristic-two module quotient, corner moment cancellation, and power-rank proof must be checked on their own mathematical merits. There is no independent expert or formal verification in this package.
