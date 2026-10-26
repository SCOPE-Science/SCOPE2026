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

Execute `python3 VERIFY.py` from the folder containing this document. No external dependencies are required. The program constructs both recurrences with arbitrary-precision integers, computes \(p\)-adic valuations and Möbius transforms independently of the symbolic derivation, and checks the exact formulas, minimal-repair divisibility implications, parity classifications, and sign obstruction. The expected result is `VERIFY_OK 27 primes; 15228 Dold modular comparisons; n<= 320`.

The checks cover 27 primes at most 103, sequence indices at most 320, and 15,228 local modular comparisons. They are finite experiments, not exhaustive over all primes or indices. The unrestricted proof appears in `RESULT.md`. No independent mathematical audit was performed.
