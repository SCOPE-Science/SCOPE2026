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

Execute the included `verify.py` with standard Python 3; no third-party modules or external data are required. It computes the three-state transfer in integer arithmetic and independently enumerates the exact valuation pair for each integer \(0\leq n<2^L\) at every \(0\le L\le14\). For each integer, it computes the second valuation both from binary digit sums and from the factorial-valuation formula. It compares full joint-count dictionaries, not samples.

It also computes all expectations, variances and covariance as exact rational numbers for every \(0\leq L\leq15\), comparing each with the closed formulas. A separate Hankel matrix evaluation at \(u=2\), \(v=3\) yields the exact determinant \(-2304\), proving nonzero generic Hankel rank once the symbolic factorization in the proof is verified. The expected successful output begins:

```
VERIFY_OK complete_direct_dyadic_levels=0..14 moment_levels=0..15
HANKEL_NONZERO u=2 v=3 det=-2304
```

The theorem for all lengths is proven by the explicit transition and formal rational generating identities, not by enumeration. The verifier does not claim to inspect historical literature, establish priority, or provide independent mathematical certification.
