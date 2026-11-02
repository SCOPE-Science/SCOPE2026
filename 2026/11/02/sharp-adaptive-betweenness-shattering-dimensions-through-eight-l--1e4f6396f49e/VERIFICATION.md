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

# Finite certificates and replay

The exact adaptive dimensions for orders of sizes three through eight are obtained by a universal counting upper bound and six complete lower-bound trees. Each tree is stored in `certificates.json` using zero-based indices into deterministically ordered lists of ternary queries and reversal-canonical permutations. The executable verification checks every root-to-leaf path from the decoded certificates, not a sample.

Run `python verify_certificate.py certificates.json`. This must print `BETWEENNESS_CERTIFICATE_AND_STATIC_CHECKS_PASS`. A fresh `python build_witnesses.py --out rebuilt.json` reproduces the certificate, whose SHA-256 should equal that of `certificates.json`.

The exact verified leaf counts by increasing label count are \(2,8,32,128,1024,8192\), totaling \(9386\) complete root-to-leaf paths. At each internal node the verifier independently evaluates the ternary predicate on the canonical permutation carried by each descendant leaf. It separately checks that every query has exactly \(n!/6\) positive concepts. The static part completely backtracks over query-index supports for \(n=3,4,5,6\), halting an extension whenever its next query fails to split a current trace cell.

The finite certificates do not prove the upper bound for all sizes: the latter has the analytic root-count proof in `RESULT.md`. This replay is a reproducibility check rather than independent expert validation.
