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

The mathematical claim is the exact recurrence for surjective bounded morphisms of finite rooted trees under the single reflexive descendant relation. The proof is by coverage of the immediate children of every target cone, followed by inclusion–exclusion and induction on source subtree size. The independent checks below are finite tests and do not certify an infinite statement on their own.

**Executed checks.** `count_pmorphisms_dp.py` checks two independently coded recurrences for 28,016 source–target rooted-tree shape pairs of source order at most eight, and 100 star-to-star counts. `verify_pmorphisms_bruteforce.py` exhaustively checks 22,132,644 total functions over 936 pairs up to source order six, including direct evaluation of the cone-image condition and explicit surjectivity/root conditions. `verify_rooted_automorphisms.py` independently checks 2,807 same-order rooted shape pairs through order seven against direct root-preserving bijection enumeration. Reproducible execution records are in `dp_output.txt`, `bruteforce_output.txt`, and `automorphisms_output.txt`.

**Limits.** The FPT bound counts big-integer operations and has exponential dependence on target maximum outdegree. Tests cover finite orders stated, not arbitrary orders. No independent audit or human literature certification has been performed.
