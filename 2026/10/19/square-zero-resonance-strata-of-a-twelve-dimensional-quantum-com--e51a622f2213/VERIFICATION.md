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

The standalone source `verify_qci_squarezero.c` independently multiplies the six degree-two/degree-three monomial coordinates in the twelve-dimensional truncated skew algebra and exhaustively enumerates their square-zero solutions. The higher coordinates \(u,v,w\) have square zero and annihilate the degree-two ideal, so the total count is the six-coordinate count multiplied by the cardinality of \(\mathbb A^3\). The program checks the closed formulas across the prime fields of sizes \(2,3,5,13,17\), and \(\mathbb F_4\) with a polynomial-basis implementation. Each test covers all \(Q^6\) six-coordinate choices; parameter orders \(3,4,8,12\) and all other regimes are represented.

Compile using `cc -O3 -std=c11 verify_qci_squarezero.c -o verify_qci_squarezero`, then run `./verify_qci_squarezero`. The observed final marker is `VERIFY_OK` with all comparisons passing. The exact symbolic reductions and component proofs appear in `RESULT.md`; a finite test is not an infinite-field or geometric proof. No independent audit was performed.
