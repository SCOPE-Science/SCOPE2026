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

# Verification

The published formula uses the uniform product distribution on Boolean valuations of a complete rooted \(n\)-ary depth-two Kripke tree. To replicate the finite tests, execute `python3 checker.py` in a directory containing that file. Its checks comprise direct enumeration of one balanced pair for \(1\le n\le8\), direct enumeration of disjoint pairs for the listed \((k,n)\) up to \((3,3)\), an independent root-success-count dynamic program, and brute-force enumeration of all relevant leaf valuations for five small complete trees. It verifies exact rational probabilities for every tested threshold, including \(t>n\), and prints `ALL_CHECKS_OK` on success.

The infinite proof is analytic, not computational: a central-binomial constant coefficient, Stirling's asymptotic, and three elementary binomial limits. The checked finite instances cannot by themselves validate those limits. The comparison with the original recursive-limit construction uses Definition 26 and Conjecture 38 of arXiv:2610.26187v1. Neither historical uniqueness nor independent audit has been established.
