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

The proof was checked against the exact cube edge normalization \(d(x,x^{(i)})=1\), the factor \(\tfrac12\) in the coordinate derivative, the Fourier normalization \(2^{-n}\), and the basepoint subtraction in each Walsh character. Each of the upper-bound, sign-extremizer, translation-averaging, and two-endpoint dimension cases has an explicit argument in `RESULT.md`.

Run `python3 check.py`. It computes Walsh transforms with integers, coordinate-shadow kernel averages as exact rational numbers, and the explicit sign extremizer for 585 arbitrary nonempty spectral families; it also checks 23 exact binomial first-moment identities. Successful output:

```text
PASS 585 nonempty arbitrary-spectrum witness checks; 23 exact degree-two moment identities
```

The exhaustive scope is \(n\le3\); the dimension-four to dimension-six tests are sampled, not exhaustive. The analytic proof, rather than finite enumeration, establishes the universal theorem. The computation does not constitute an external certification or independent audit.
