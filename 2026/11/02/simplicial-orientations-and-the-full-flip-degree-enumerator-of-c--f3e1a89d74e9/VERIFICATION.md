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

# Verification and limits

The finite verification programs `verify_blocks.py` and `verify_matrices.py` require only Python 3 standard library. They are standalone and have no external data, network, or hidden run dependencies. Execute each script with `python verify_blocks.py` and `python verify_matrices.py` from the directory containing those files. The former constructs canonical ordered labelled blocks and tests the falling-factorial simple-vertex count; the latter exhaustively enumerates binary edge-orientations and tests directed four-cycle avoidance and legal one-bit flips. Their outputs include the exact passed messages `ORDERED_BLOCKS_CERTIFICATE_PASS` and `LONESUM_MATRIX_CERTIFICATE_PASS`.

Finite verified cases include \(K_{2,2}\), \(K_{2,3}\), \(K_{3,3}\), \(K_{3,4}\), \(K_{4,4}\), and \(K_{1,4}\) in the ordered-block script. The \(K_{4,4}\) polynomial has coefficient vector at degrees seven through sixteen \((1472,2304,1056,1248,192,408,64,96,32,30)\), summing to \(6902\). The checker does not certify an infinite proposition merely by experiment: the general assertion is proved in `RESULT.md` by exhaustive classification of symbolic block forms and their tree cases. No external or independent audit has been performed.
