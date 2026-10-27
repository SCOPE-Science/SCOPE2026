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

Run `python3 verify_spider_ideals.py` with a standard Python 3 interpreter. The script independently constructs the partial order of a rooted spider, enumerates every subset that is a downset, derives vertex-membership masks, and computes the exact full binary Littlestone recurrence on the finite version space. It then evaluates the displayed formula and verifies both rank and number of ideals. No third-party package is needed.

The included execution output reports 183 checked arm vectors, specific test cases, and `ALL_FORMULA_CHECKS_PASS`. The cases range over nondecreasing vectors of zero through five arms of lengths one through eight, restricted to at most thirteen total vertices. Checking one nondecreasing vector suffices for each permutation of arm lengths because permuting arms gives an isomorphic poset.

The infinite-family theorem is established by the exact split recurrence and dyadic induction in RESULT.md; this program is a finite cross-check, not an exhaustive enumeration of all finite spiders or an independent scientific audit. No external validation has been performed.
