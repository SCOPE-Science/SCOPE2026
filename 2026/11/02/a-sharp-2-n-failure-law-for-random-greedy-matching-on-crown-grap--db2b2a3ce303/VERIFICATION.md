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

The proof in `RESULT.md` establishes the all-size statement analytically, including the positivity of all denominators, the conditional transition law, the first-moment telescope and the factorial-moment contraction. The factor \(16\) in the uniform error follows from \(k^2/(k-1)^2\le4\) for integers \(k\ge2\).

Run `python3 checker.py`. It executes exact rational overlap-chain recurrences for sizes \(2\)–\(10\), independent bit-mask dynamic programming for sizes \(2\)–\(6\), and direct examination of all \(720\) edge orders on the three-pair crown graph. It also tests the polynomial inequality at sizes \(2\)–\(200\) and prints float diagnostics for larger graphs. The completed run reported 5,330,825 successful deterministic assertions. These are finite cross-checks and do not certify the theorem independently.

No mathematical result outside the stated graph family, and no independent audit or exhaustive historical-priority check, is asserted.
