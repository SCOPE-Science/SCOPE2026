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

Run `python3 verify.py` using the standard Python library. It recomputes every binomial coefficient and its gcd directly for \(2\le k\le140\). Independently, for each \(3\le n\le2000\) and every prime \(p\mid n\), it calculates the minimum factorial-valuation formula over the entire finite multiplier range; those independent values match the stated formula.

Expected successful output: `VERIFY_OK: 139 direct exact gcd cases and 4453 prime-power valuation cases`.

Finite tests are not an infinite proof. The proof in `RESULT.md` uses Kummer's and Lucas's theorems plus the precise published prime-support and zero-valuation lemmas from [2]. No independent audit or formal proof certification has been performed.
