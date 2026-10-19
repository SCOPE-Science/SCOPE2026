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
Run `python3 verify.py` from the directory containing the standalone script. It requires Python 3 standard library only and returns `VERIFY_OK` when all assertions succeed. The checker enumerates every linear map on \(\mathbb F_q^{N+1}\) for four low-dimensional prime-field examples, identifies Lie automorphisms by verifying the defining bracket on all ordered basis pairs, and tests the absence of fixed vectors by row reduction. It checks nonsemisimple module-centralizer cardinalities and fixed-point-free unit counts, including the Jordan partition \((2,1)\), and tests cyclic intertwiners for paired Jordan blocks of sizes \(1\) and \(2\).

Expected critical examples: over \(\mathbb F_3\), \(T=\operatorname{diag}(1,2)\) has \(72\) total automorphisms and \(18\) fixed-point-free ones. The paired nonsemisimple case \(J_2(1)\oplus J_2(2)\) has \(5832\) total and \(1458\) fixed-point-free automorphisms. The exact proofs of the formulas for all dimensions and finite fields use the block-intertwiner argument and finite-module endomorphism-ring radical; the finite tests are not claimed to prove those universal statements.
