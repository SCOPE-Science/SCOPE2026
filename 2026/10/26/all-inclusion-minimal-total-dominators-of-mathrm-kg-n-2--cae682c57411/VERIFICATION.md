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

# Computational verification and scope

Execute `python3 verify_edge_critical.py` and `python3 verify_kneser_direct.py` from a directory containing the two scripts. No third-party dependencies are used. The corresponding package files `verify_edge_critical_output.txt` and `verify_kneser_direct_output.txt` record expected output. Both programs completed successfully during verification.

The finite classifier generates all isomorphism classes of simple edge graphs through six edges by exhaustive edge augmentation and degree-respecting permutation canonicalization; the printed edge-count class sizes are `1,1,2,5,11,26,68`, with exactly four critical classes. This finite exhaustion is scientifically sufficient only together with the analytic \(|E(H)|\le6\) bound and the stated augmentation completeness proof in RESULT.md. The direct Kneser checker exhaustively tests selected subsets of sizes three through six for every \(n\) from \(4\) through \(8\) and confirms each coefficient; its bounded range is corroboration rather than proof for arbitrary order.

No computational proof is claimed beyond the stated exhaustiveness argument, and no independent external audit has been performed.
