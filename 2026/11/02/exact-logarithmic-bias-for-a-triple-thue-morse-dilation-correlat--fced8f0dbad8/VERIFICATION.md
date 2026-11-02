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

# Reproducing the integer certificate

Run `python3 verify.py` from this directory with Python 3.8 or later; no third-party modules are needed. The executed program regenerated the seven-state, fourteen-branch carry transfer, checked every entry of the integer identity \(M(M^2-I)^3=0\), checked the terminal parity signs and first twenty transfer sums, and independently computed the original signed sum for every exponent \(0\le r\le15\). The observed output was:

```
PASS: 7 states, 14 transition branches, 7x7 annihilator, 20 transfer evaluations, 65535 direct summands
```

The 65,535 direct summands are finite checks, not a proof for arbitrarily large exponents. The exact matrix annihilator combined with the proven binary-carry interpretation yields the all-exponent recurrence, and the seven base cases complete the mathematical proof.

No independent scientific audit was performed. Historical uniqueness and literature priority cannot be certified by a finite search.
