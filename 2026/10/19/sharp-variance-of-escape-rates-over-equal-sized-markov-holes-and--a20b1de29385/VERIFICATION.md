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

# Verification details

The accompanying standard-library-only `checker.py` was run with Python 3 and returned `VERIFY_OK; K_2=0.823295689936509`. The checks enumerate every word for binary lengths three through nine, ternary lengths three through five, and quaternary lengths three and four, solve the exact physical escape-rate polynomial numerically by bisection, verify a uniform error bound against the correlation-polynomial approximation, and compute the normalized cross-hole variance. They also check exact avoidance counts by exhaustive enumeration at short lengths for binary words, against coefficients of the rational generating function, and compare independent Möbius/primitive-block summations for the binary constant.

To reproduce in a directory containing the two files, run:

```
python checker.py
```

Scientific verification beyond finite computations consists of: (i) deriving the exact first-occurrence generating function and its first real pole; (ii) proving the word-uniform \(O_q(nq^{-n})\) normalized escape-rate error; (iii) grouping by least self-overlap period and obtaining a square-summable uniform tail; (iv) counting primitive periodic blocks and showing convergence within each fixed-period class; and (v) controlling the centering correction and deriving the limiting probability law. Every step is given in `RESULT.md`.

Finite enumeration does not establish the infinite-\(n\) theorem or external historical originality; it checks independent finite consequences. No independent audit has been performed.
