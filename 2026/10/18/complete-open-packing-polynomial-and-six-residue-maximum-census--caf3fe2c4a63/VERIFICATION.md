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

Run `python3 verify.py` using Python 3.9 or later. No external packages or datasets are required. The verifier constructs the graph-theoretic open-neighbourhood predicate, counts all labelled subsets through \(n=10\), constructs the common-neighbour graph and the explicit vertex permutation through \(n=40\), and independently counts cyclic two-bit column patterns through \(n=40\). It checks the residue-class maximum formulas through \(n=150\). The delivered `verification_output.txt` records the successful run. Exhaustive finite checks are not a proof of the infinite statement; the independent, all-\(n\) bijection and gap-count proof appear in `RESULT.md`. Independent mathematical review has not been performed.
