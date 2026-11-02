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
# Verification record

The exact symbolic coefficient checker is the standalone `verify.py`. Running `python verify.py` with standard-library Python produces:

```
EXACT_MOMENT_TESTS_PASSED 4048
TOTAL_CHECKS_PASSED 4060
```

It compares constant Laurent coefficients for all distinct coprime pairs with \(1\le p,q\le8\), two positive coefficient pairs, and every mixed moment below total degree \(p+q\). It verifies the first defect coefficient \(b^pc^q\). Twelve deterministic angular midpoint integrals check the independently derived radial CDF, including the equal-weight central case.

The proof, not these finite checks, establishes the infinite-dimensional and all-parameter claims. Independently reconstruct the logarithmic unitary transform, apply Kronecker density and the primitive character relation, then derive both CDF and flat-torus covering bound. No external independent audit has been performed.
