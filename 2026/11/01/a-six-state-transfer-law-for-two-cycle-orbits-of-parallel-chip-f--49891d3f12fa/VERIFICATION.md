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

# Exact arithmetic and finite-state verification

Run `python3 verify.py` in this directory with Python 3.10 or newer; it requires only the standard library. The run's recorded standard output is in `verification_output.txt` and terminates with `LADDER_CHIPFIRE_EXACT_VERIFY_OK`.

The program generates the sixteen ordered binary rung pairs from scratch, constructs their six orbits under global color complementation and row interchange, and rebuilds every one of the 36 transfer-matrix entries and both boundary vectors from the local opposite-neighbour degree formula. It checks a polynomial matrix identity matching \((x-1)^3(x+1)(x^2-12x+1)\) and six scalar annihilator seeds, which suffice for the complete fourth-order recurrence given the degree-six characteristic identity. It calculates the first 25 terms of the proposed transfer sequence and verifies recurrence agreement.

Separately, it sums the local phase weight directly over all \(87{,}376\) binary assignments for all ladders with two through eight rungs, comparing with the transfer values. It constructs and executes the actual two-step chip-firing transition independently on every chip assignment in the box \(0\le c(v)<2d(v)\) on ladders with two, three and four rungs: \(341{,}248\) configurations in total. The primitive two-cycle counts agree exactly with the theorem. This box contains every primitive two-cycle by the phase-interval lemma; it is not an enumeration of every unbounded chip configuration.

The all-length proof does not rely on these finite examples: it relies on the phase-interval bijection, local transfer factorization and exact rational-matrix identity in `RESULT.md`. The program does not evaluate longer primitive periods, classify transient states outside primitive two-cycles, or provide external validation. No independent audit has been conducted.
