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

The exact integer-arithmetic determinant expansion of the ten-state matrix agrees term for term with the two claimed bivariate factors (18 nonzero bivariate monomials after multiplication). A separate graph-adjacency brute force enumerator agrees with the transfer method for every cardinality at \(3\le n\le8\); total values are 13, 32, 69, 157, 361, 824. The stated first ten complementary coefficients were also checked directly by transfer recurrence for \(10\le n\le18\). The proof's infinite scope comes from the cyclic-word correspondence, determinant identity, and formal logarithmic trace, not these finite tests.

To replay, run `python3 artifacts/verify.py`. No external software packages are required. Historical priority and mathematical interpretation have not undergone independent audit.
