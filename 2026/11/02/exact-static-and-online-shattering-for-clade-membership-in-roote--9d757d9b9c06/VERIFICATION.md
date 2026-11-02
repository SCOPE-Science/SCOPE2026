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

# Verification of the clade-membership theorem

Run `python3 verify_hierarchy.py` from this directory using Python 3.10 or newer; only the standard library is needed. The program independently enumerates all rooted binary labeled phylogenies on two through seven leaves, constructs every laminar subfamily on two through six leaves, computes the exact recursive Littlestone depth from incidence vectors, checks the full prefix-shattering construction, and checks positive-branch Cartesian-product identities through five leaves.

Expected final marker: `CLUSTER_QUERY_ALL_CHECKS_PASS`. Binary hypothesis counts at leaves \(n=2,3,4,5,6,7\) are respectively \(1,3,15,105,945,10395\); all-hierarchy counts through six leaves are \(1,4,26,236,2752\). Expected dimensions in both versions are \(n-2\).

The unbounded theorem rests on the five independently stated mathematical proof steps in `RESULT.md`; no finite computation can establish it alone. The recursive tester performs exact integer/mask operations, with no floating-point tolerances or stochastic claims. This does not constitute independent third-party audit, and historical novelty cannot be certified by exhaustive finite tests.
