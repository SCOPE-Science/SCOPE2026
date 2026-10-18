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
# Reproducibility

Execute `python3 verify_folded_reflection.py` and `python3 verify_path_period.py`, both with only Python 3's standard library. The first program enumerates all finite simple labeled base graphs on 2–4 vertices with a nonempty edge set (71 graphs), each strip parity and k=1,2,3, and independently constructs both the reflection edge-orbit conflict graph and the claimed graph-strip matching model. It checks 426 exact simplicial flag-complex identifications, 5,550 qualifying orbit vertices in aggregate, and exhaustive face vectors in 16 cases. The captured output is `verification_fold_output.txt`. The second program computes mod-two boundary ranks for all path independence complexes with n=2,…,14; its captured output is `verification_path_output.txt`. Both terminate with `VERIFY_OK`.

Finite graph tests and finite-field homology do not prove an all-graph PL homeomorphism or an integral homotopy classification. Universal correctness instead follows from a barycentric-orbit proof, complete edge taxonomy under strip reversal, and a separate standard path independence suspension induction presented in RESULT.md. No independent scientific audit has been performed. The accessible nearest 2026 primary source was not inspected beyond abstract and bibliographic data, and overlap with an unexamined generalized lemma is unresolved.
