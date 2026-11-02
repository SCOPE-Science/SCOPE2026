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

# Verification of the length-two graph criterion

Execute `python3 verify.py` using Python 3 standard library only. The verifier independently enumerates all subsets of \(n\) distinct length-two words drawn from the \(n^2\) possibilities for \(1\le n\le5\). For each, it tests all proper nonempty vertex sets for the induced-edge sparsity and tightness inequalities; this produces rank-preserving image-set counts \(1,6,72,1274,29610\) and irreducible image-set counts \(1,1,8,48,384\).

For \(1\le n\le4\), a second method independently enumerates all generating sets using available single-letter words and target length-two words and agrees on rank preservation and irreducibility. A rational-coefficient EGF routine uses the rooted-tree and unicyclic-component formula and gives the same first five counts. The observed terminal line is `ALL_CHECKS_PASSED`.

These are exhaustive **finite** checks at the indicated ranks, not an exhaustive proof over all \(n\). General correctness rests on the generating-rank lemma, composition factorization criterion, and labeled graph decomposition proved in RESULT.md. No independent external validation or audit was performed.
