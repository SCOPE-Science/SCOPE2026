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

# Verification of the distance-law comparison

Run the included `VERIFY.py` with Python 3.10 or later; it requires only the Python standard library:

```bash
python3 VERIFY.py
```

The script independently enumerates point-to-lift distances over finite rational grids, checks the closed even/odd deck-path expression, tests finite cyclic sum–difference bijections, evaluates the exact CDF-gap integral numerically, and checks the two asymptotic exponents and constants. Its completed run produced:

```text
PASS: 5656 exact lift/finite-character checks; 49 deterministic CDF/asymptotic checks.
Finite tests do not replace the analytical universal proof.
```

The assertion coverage includes three positive aspect ratios for exact rational path checks, four aspect ratios for CDF support and positivity checks, and independent small-threshold and diameter-limit tests. The proof in `RESULT.md` establishes all parameters and thresholds symbolically; this file does not claim infinite certification by enumeration. No independent external validation has been performed.
