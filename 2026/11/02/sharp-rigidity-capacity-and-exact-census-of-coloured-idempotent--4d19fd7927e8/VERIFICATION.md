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

# Verification evidence

Run `python3 checker.py`. The checker is standalone, requires no external package, and compares each coloured idempotent labelled map on every carrier in the finite ranges \((q,n)=(1,1..6),(2,1..5),(4,1..4)\). It independently computes the canonical multiset-of-stars key, tests rigidity from the existence of colour-preserving automorphisms, enumerates the unrestricted multiset product, expands the rigid polynomial, and checks the unrestricted divisor-sum recurrence. For all checked carrier sizes it matches unlabeled and rigid type counts, as well as the labelled enumeration's canonical type partition. It confirms reciprocal rigid coefficients, positivity up to the sharp bound, and a unique maximal rigid type for each tested colour count; it checks the unrestricted recurrence through degree \(20\). Actual replay output ended `ALL_CHECKS_OK`.

The mathematical proof establishes all \(q\), all \(n\), and the fixed-\(q\) asymptotic by rooted-star decomposition and a moment-concentration argument; a finite computer test cannot establish any of those infinite claims alone. No external independent audit was performed. Literature comparison cannot certify historical priority.
