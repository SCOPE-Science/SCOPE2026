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

# Verification and limits

Run `python3 verify_isolation.py` with Python 3.10 or newer. No third-party packages are required. The actual run printed:

```
PASS: 680 exact assertions; connected labeled graphs: {3: 4, 4: 38} ; full enumeration: 128 configurations per probability
```

The checker exhaustively constructs the 42 connected labeled simple graphs on three and four vertices and checks each off-diagonal inverse-matrix cofactor as an exact integer polynomial in a strictly positive variable. It checks the general closed book-family formula at ten sizes and five rational retention parameters each. It also independently calculates the five-vertex witness's exact covariance matrices by enumerating all 128 retained-edge states at each of three rational values. All tests use integer or rational arithmetic; no floating-point sign tests determine the conclusions.

The unrestricted bipartite sign law and the book-family phase threshold are established by the mathematical proof in `RESULT.md`, not inferred from finite computations. Historical priority and scientific merit await independent assessment. The computed partial correlations have the **linear regression** meaning; a vanishing value is not a binary conditional-independence certificate.
