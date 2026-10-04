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

The mathematical proof is the induction in `RESULT.md`. The standalone `verify.py` is a finite consistency check only.

Running `python3 verify.py` evaluates the recurrence with the admissible constant function \(f(m)=1\) for every \(2\le n\le10000\) and checks that every value equals \(-1\). It also verifies the smallest composite witness \(n=4\).

Expected terminal line:

`VERIFY_OK f=constant_one range=2..10000 first_composite=4 all_star=-1`

The computation does not certify the infinite range; that range follows from the exact induction. No independent audit has been performed.
