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

The complete proof in `RESULT.md` applies to every integer \(n\ge2\). A separate exhaustive finite checker `verify.py` represents each partial map by its \(n\)-entry evaluation table with `-1` denoting the undefined value. It composes every ordered pair as actual partial functions and counts mutual annihilation, nonzero-product commutation, total commutation, and the four mutually exclusive shift-sign classes. The checker does **not** use the interval endpoint equations or the enumeration algorithm from the proof.

Run `python3 verify.py` in the same directory as the extracted files. It requires Python 3 and only its standard library. Actual execution completed for every \(n=1,2,\ldots,10\), printed per-size results, and ended with `VERIFY_OK 10 exact direct-map enumerations; four nonzero-product shift classes`.

Exact sample data in order \((n,|M_n|,Z_n,P_n,C_n)\):

```
(1, 2, 0, 1, 4)
(2, 6, 4, 11, 26)
(3, 15, 44, 52, 125)
(4, 31, 228, 164, 453)
(5, 56, 812, 409, 1332)
(6, 92, 2296, 875, 3354)
(7, 141, 5544, 1680, 7505)
(8, 205, 11928, 2976, 15313)
(9, 286, 23496, 4953, 29020)
(10, 386, 43164, 7843, 51778)
```

Small finite tests are consistency checks, not proofs of an unrestricted identity or of publication priority. No independent mathematical audit was performed; the review status is self-review only.
