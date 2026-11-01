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

# Verification record

Execute `python verify_integral_petersen.py` with SymPy installed. This is a self-contained deterministic computation; the result printed by the packaged code is recorded in `verification_output.txt`. Its exact integral matrices and orbit columns are embedded in `generator_matrices.json`. No logs from other calculations, remote attestations or unprovided data are used.

The verification reconstructs the Petersen graph as \(\operatorname{KG}(5,2)\), enumerates its 331 nonempty matching simplices, checks the 160-pair Hasse acyclicity, and performs signed integer unit cancellations. It checks vanishing of the original lifted-cycle boundaries, complete cancellation projection/inclusion, Coxeter relations, and all 120 automorphism character values. For degree two the orbit basis has determinant \(-1\); for degree three the stabilized line generator is primitive and the ten-column orbit matrix has Smith factors \((1,1,1,1,3)\). These two exact lattice tests are what prove the new statements.

The executable requires Python 3 and SymPy and is finite for the specified graph. There is no claim of generalization to arbitrary graphs. The code is an ordinary mathematical checker and not an independent review or an external certification. The published background gives the model and its symmetry, while earlier nonequivariant and rational calculations are not claimed as novel.
