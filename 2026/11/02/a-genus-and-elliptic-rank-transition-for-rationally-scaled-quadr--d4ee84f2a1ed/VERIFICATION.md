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

# Exact arithmetic checks and limits

Run `python3 verify.py` with Python 3 and no nonstandard packages. Output recorded from the included file:

```
VERIFY_OK conic_points=41 elliptic_multiples=7 nonintegral_5P_x=167460/3721 binomial_checks=51 rational_arithmetic=yes
```

The script verifies 41 distinct positive-scale rational conic points for the d=6/k=3 example, seven exact multiples of the d=15/k=4 elliptic witness, the exact noninteger first coordinate of 5P, and 51 identities independently evaluating the irrational coefficient of a power. These checks are exact but finite and do not establish the smoothness or genus formula in all degrees, Faltings' theorem, Mordell–Weil, or the Nagell–Lutz theorem. The proof states where those standard theorems enter. Independent mathematical audit has not been performed.
