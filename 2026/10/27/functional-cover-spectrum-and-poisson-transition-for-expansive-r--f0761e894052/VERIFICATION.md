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

# Reproduction

The accompanying `checker.py` runs with standard Python 3; execute `python checker.py`. It enumerates all total row relations on two rooted stars for each pair of leaf counts \(1\le k,\ell\le3\). The tests compare direct confluence against the two-case normal form, verify that every proposed isotone-map graph is a subrelation, prove computationally that their union is exact, and compare all rank-count predictions against the enumeration. For \(k,\ell\le2\), an exhaustive dynamic-programming set-cover calculation independently verifies rank minimality. A numerical sanity test probes the critical-window Poisson approximation. The observed terminal line is `ALL_CHECKS_OK 88784`.

# Limits

Finite enumeration through three leaves is not a proof for arbitrary parameters. The symbolic normal-form, cover-construction, counting and normalized-generating-function arguments provide the unrestricted proof. No external or independent audit is asserted. Research on older multivalued order-preserving relations may reveal an equivalent earlier result.
