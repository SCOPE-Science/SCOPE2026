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

Run `python3 verify.py` beside `certificate.json`.

The verifier enumerates every ternary necklace through length \(6\) and checks the necklace counts against the totient formula. It restricts to full-support circular words.

Circular Parikh matrices are computed twice. One engine averages direct scattered-subword counts for \(ab\), \(bc\), and \(abc\) over all cyclic shifts. The other multiplies the \(4\times4\) Parikh matrices of letters for every distinct conjugate and averages those matrices. The results must agree for every necklace.

The \(CE_1,CE_2\) rule graph is likewise computed twice: first by generating all legal one-step rewrites from every rotation, and second by pairwise testing every \(M\)-equivalent pair for a legal rotated decomposition. The edge sets must coincide.

The verifier checks that length \(5\) has one nontrivial full-support \(M\)-class and no disconnected class; length \(6\) has eight nontrivial classes, five connected classes, and exactly the three exceptional classes listed in the result. It also verifies that every exceptional word has zero legal rule moves.

Independent audit has not been performed.
