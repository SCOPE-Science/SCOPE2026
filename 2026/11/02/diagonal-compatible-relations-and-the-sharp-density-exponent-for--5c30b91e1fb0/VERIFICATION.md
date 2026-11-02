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

Run `python3 checker.py` with Python 3. The program constructs group and semigroup multiplication tables, enumerates normal subgroups directly, builds the proposed relations, tests multiplication compatibility and congruence properties, and independently enumerates all compatible reflexive relations by closure-search for the trivial group, \(C_2\), \(C_3\), and \(C_2\times C_2\). It also checks the 46 constructed relations for the nonabelian group \(S_3\), without exhaustively listing all relations on its twelve-element semigroup. Gaussian-binomial recurrence tests cover three primes and five dimensions.

The run's stdout is in `checker_output.txt` and ends with `VERIFY_OK`. The checker makes no claims about untested groups or arbitrarily large ranks. The general assertions are proved symbolically in `RESULT.md`; direct computational tests are corroboration only.
