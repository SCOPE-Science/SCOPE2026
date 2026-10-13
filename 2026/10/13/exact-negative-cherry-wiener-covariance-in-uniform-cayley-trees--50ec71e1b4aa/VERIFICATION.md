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

# Verification instructions and limits

Run `python3 verify.py` in a directory containing this file and the standalone checker. It uses only the Python standard library, with arbitrary-size integers and `fractions.Fraction`; no data downloads, random sampling, or mathematical packages are required.

The verifier checks exactly all \(624\) sizes \(3\le n\le626\), including the zero boundary and every negative-case size \(4\le n\le626\). The independent Prüfer-enumeration comparison counts \(3+16+125+1296+16807=18{,}247\) complete uniform-labelled trees for \(3\le n\le7\), computing their leaf pairs, all-pair distances, means and exact covariance separately from the closed formula. A few sizes \(n\ge627\) are additionally checked as sanity tests, without pretending that they certify an infinite range. The infinite tail inequality and asymptotic Gaussian-product estimates are mathematically derived in `RESULT.md`, not inferred from these checks.

Expected success ending: `CHECKER_OK`. Deterministic sample exact covariances: \(n=4\), \(-9/16\); \(n=5\), \(-696/625\); \(n=6\), \(-440/243\). These are tests, not substitutes for the proof. Independent audit has not been performed.
