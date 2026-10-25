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

The accompanying standalone Python checker is `verification/check.py` and requires only the standard library. Its `direct_dynamic_programming` builds each word explicitly, fills a palindrome table from the substring symmetry recurrence, and counts all minimum-cost predecessor cuts. That oracle does not reuse the transition-structure argument of the proof.

The checker returned:

```
VERIFY_OK dp_five_run=7776 large_instances=400 gf_coefficients=455 lengths=5..30
```

Here 7776 counts all \(6^5\) choices of positive run lengths at most six. Another 400 seeded choices have each run length at most 23. Counts in the generating-function regime and the claimed sharp maximum were compared with full five-part-composition enumerations for every length 5 through 30. These computations are finite checks only; they cannot establish an infinite theorem or novelty. The proof in `RESULT.md` supplies the required infinite arguments.

The core enumerative identity can be reproduced by expanding
\[
\frac{2z^8v^3}{(1-z)^3(1-z^2)(1-z^3v)}
\]
in formal power series. Its \(v\)-derivative at one, compared with \(\binom{n-1}{4}\), gives the leading expectation \(n/45\). The density integrates to \(1/3\), and its first moment is \(1/45\).

No independent external review or certification has been performed.
