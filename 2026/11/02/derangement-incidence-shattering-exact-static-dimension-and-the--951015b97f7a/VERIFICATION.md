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

## Reproduction
Run `python verify_derangement_learning.py derangement_depth4_witness.json` with Python 3 and no third-party packages. The program enumerates all derangements through size eight for the fixed cyclic-support checks, exhaustively computes the VC dimension through size five, checks all 16 root-to-leaf paths of the adaptive depth-four witness, and verifies the positive root-branch bound of eleven. The expected output is embedded in `verification_output.txt`.

## Proof coverage and limits
The all-order static formula depends on the explicit Hall argument in `RESULT.md`, not on the finite verifier. The five-element adaptive lower bound depends on the complete certificate: each leaf permutation is checked against every query on its path; the upper bound follows because every possible root query leaves only eleven positive concepts and a depth-five full tree would require sixteen in that branch. The verifier is not an independent audit. Historical priority remains uncertain.
