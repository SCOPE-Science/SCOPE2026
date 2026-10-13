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

Run `python3 verify.py` from the directory containing this document and the supplied `verify.py`. The verifier uses only Python's standard library and checks:

- Exact division of the degree-seven polynomial modulo \(2\) by all five irreducibles of degrees one through three.
- The explicit factorization modulo \(467\), including the irreducibility of its quadratic factor.
- All eight derangement-based fixed-point counts, their sum \(5040\), and the density \(103/280\).
- Exhaustive \(\mathbb F_p\)-projective point enumeration for thirteen small primes against the septic root count.

The theoretical all-primes result requires the geometric gradient identity, the primitive permutation-group argument and Chebotarev's theorem as given in `RESULT.md`; finite field testing alone does not establish it. The outcome concerns rational singularities only and does not establish geometric smoothness or independence of any external review.
