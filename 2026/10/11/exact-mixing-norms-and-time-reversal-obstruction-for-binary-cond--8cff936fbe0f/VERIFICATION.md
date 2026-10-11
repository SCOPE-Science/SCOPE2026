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

# Verification of the exact operator formula

The identity \(P_A=E+u_A\otimes\ell_A/[\mu(A)(1-\mu(A))]\) follows directly by evaluating the two atoms of \(\sigma(A)\). Every adjacent product contributes the scalar covariance of the corresponding centered indicators. The standard rank-one operator norm is the product of the output \(L^p\) norm and the input \(L^q\) dual norm, with equality in Hölder attained by the explicitly stated test vector.

The exact rational verifier `verify_binary_products.py` was executed using Python 3 and the standard library only. Its output was:

```
BINARY_EXPECTATION_EXACT_IDENTITIES_OK 2744
```

The verifier checks all \(14^3\) ordered triples of nontrivial events on a fixed rational four-atom law and compares the operator to its claimed rank-one expression and the square to its claimed scalar multiple, using exact rational arithmetic. It checks two non-Hilbert norms against constructed Hölder equality vectors, and it checks three-atom reversal and four-atom finite-time-mixing examples. Those finite tests do not establish universality; the proof in `RESULT.md` supplies the general argument. Unproved: any nonbinary-sigma-algebra extension, any \(p=1\) or \(p=\infty\) claim, or any statement of independent external mathematical certification.
