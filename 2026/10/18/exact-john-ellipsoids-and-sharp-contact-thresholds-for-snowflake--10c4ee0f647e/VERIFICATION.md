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

# Reproducible verification and scope

Run `python3 check_john.py` from this package in a Python environment with the standard library. The expected result is:

```
PASS 2580 full rational matrix, support, and KKT checks; phases {1: 900, 2: 780, 3: 900}
```

The checker uses `fractions.Fraction` and independently forms the three projector blocks in \(\mathbb Q^{N\times N}\). For all tested parameter pairs \(2\le p\le11\), \(p\le q\le13\) it samples both transition values, both endpoints and 10 interior fractions per nonempty branch. It checks (i) strictly positive squared semiaxes; (ii) every actual squared facet support; (iii) the cross-distance equality; (iv) a nonnegative multiplier for every constraint; (v) stationarity and complementarity. Its matrices are formed without using the closed-form support-vector values in the proof.

The universal theorem is independently established in `RESULT.md` using the invariance of the unique John ellipsoid and the strict concavity/KKT argument, not inferred from any finite enumeration. This verification does not certify full bibliographic novelty, complex-scalar analogues, arbitrary coordinate changes, or independent external audit.
