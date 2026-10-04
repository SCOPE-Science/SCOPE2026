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
The verifier starts only from the seven hexadecimal rows printed for the new optimal binary LCD \([55,7,25]\) code.

It expands each hexadecimal digit most-significant-bit first, confirms that the final displayed bit is the source padding zero, removes that one padding column, and checks rank \(7\) and a full-rank binary Gram matrix. It then exhausts all \(128\) codewords to recover the complete Hamming weight enumerator.

For the higher-support profile, the verifier generates every subspace of \(\mathbb F_2^7\) in unique reduced-row-echelon form. The per-dimension counts are checked against \(1,127,2667,11811,11811,2667,127\). It recomputes the maximum number of generator columns in each subspace dimension, verifies the stored maximizing witnesses, and derives the generalized Hamming weight hierarchy from the column-subspace formula. No floating-point arithmetic, heuristic search, or optimizer status is used.
