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

## Exact finite checks

`python3 verify.py` (with `certificates.json` next to it) recomputes the asserted first-occurrence test over all relevant smaller consecutive triples and determines the exact types, genus values, Frobenius numbers, and pseudo-Frobenius sets for the example. It uses unbounded-integer arithmetic.

Each candidate Frobenius cutoff is **certified**, rather than guessed: the proposed largest gap is absent, and every integer in the next full interval of length equal to the smallest generator is present. Closure under addition of that generator then proves no larger gaps exist. Every remaining gap is tested against every generator, so pseudo-Frobenius enumeration is exhaustive. A separately implemented residue-shortest-path method checks the entire explicit Apéry certificate.

Observed output:

`VERIFY_OK independent_dp=yes independent_dijkstra=yes complete_cases=14 first_delayed_m=8 type_profile=1,1,7 F_profile=31,519,5791 genus_profile=16,260,3072`

## Limits

These are finite proofs for the explicitly listed semigroups, not empirical extrapolations or a general theorem for all parameters. The mathematical justification of the finite reductions is in `RESULT.md`. The status of independent scientific audit remains not performed.
