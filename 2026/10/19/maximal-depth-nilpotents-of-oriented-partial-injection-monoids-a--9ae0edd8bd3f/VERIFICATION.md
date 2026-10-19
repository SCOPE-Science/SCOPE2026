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

Run `python checker.py` with Python 3, no nonstandard dependencies. It independently enumerates all \(n!\) directed paths for \(2\le n\le8\), constructs their partial injections, checks cyclic and anti-cyclic images directly, and compares counts to the closed formula. It separately checks the exact first-return successor cycle count for every admissible denominator pair through \(m=30\). Successful execution prints `VERIFY_OK`.

The exhaustive enumerations establish only these finite cases. The general theorem relies on the chain decomposition, successor/first-return lemma, Farey gap characterization and opposite-parity circle-order argument in the proof. Independently conducted external scientific audit has not occurred.
