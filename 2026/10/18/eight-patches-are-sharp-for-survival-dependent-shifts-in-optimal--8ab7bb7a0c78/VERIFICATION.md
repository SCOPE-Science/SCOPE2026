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

# Reproducibility and boundaries

Run `python vertex_criticality_verify.py` with Python 3.9+; the only imports are standard-library modules. It reconstructs each tree from every Prüfer word for orders 1–8; checks nonisomorphism using tree-center encodings; computes all ordered-pair path polynomials; derives integer coefficient certificates for global optimality on the full interval; verifies that both remaining shapes have disjoint exact-rational winner sets at \(p=1/2\) and \(p=9/10\); and proves the two explicit factorization identities. It also independently verifies the protection-gain formula by enumerating the 128 configurations of the other seven surviving sites for each protected vertex on the first example at two rational probabilities.

Expected final output: `VERIFY_OK unlabeled_counts=1,1,1,2,3,6,11,23 exceptions=2 exact_bernstein=PASS witness_polynomials=PASS direct_state_count=PASS`. The displayed output was reproduced from this packaged verifier before delivery. The proof is exhaustive only through eight vertices, not for larger trees. No ecological field data or independent audit has been used.
