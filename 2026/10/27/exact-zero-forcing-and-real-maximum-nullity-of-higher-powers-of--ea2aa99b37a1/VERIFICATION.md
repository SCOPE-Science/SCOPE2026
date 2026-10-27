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
# Computational verification and limits

Execute `python3 verify.py` (Python standard library only). Observed success output:

`VERIFY_OK witness_support_rank_forcing= 83 higher_power_cases= 47 exhaustive_zero_forcing_cases= 30`

The program independently constructs every finite spider power from graph distances, then constructs the exact-support symmetric witness from the window Gram matrix and cross-arm threshold blocks. It verifies the support entry-by-entry, explicitly builds independent null vectors satisfying the window equations, and computes the complete matrix rank modulo two distinct primes. These modular ranks equal the theoretical rank in every tested instance and hence certify that rank over the rationals is at least the reported value for those instances. The stated forcing set is tested using graph adjacency alone, and brute force excludes all smaller zero-forcing sets in 30 bounded instances.

The all-parameter theorem is proved algebraically and combinatorially in `RESULT.md`. Finite checks do not by themselves prove the universal claim. No independent audit is recorded here, and historical priority beyond the inspected literature is not independently certified.
