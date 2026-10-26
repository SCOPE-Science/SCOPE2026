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

# Executable checks and their limits

Run `python verify_cycle_q.py` with Python 3. The program uses only Python's standard library. It tests 42 parameter pairs with \(Q=q-1\) and \(n\) in bounded ranges, checks all edge-weight exponent tuples and their predicted cyclic invariants, and for cases with at most 3,000 tuples independently enumerates equivalence under elementary changes of natural basis and graph rotations. For each canonical invariant it enumerates the modular rotation-lift equation, checks the exact size of every rotation fiber, and compares direct existence of an order-preserving lift with the displayed greatest-common-divisor criterion. Six larger arithmetic parameter pairs are checked independently by congruence sweeps.

Expected terminal output begins with `VERIFY_OK`. These checks verify algebraic finite instances of the formulas and do not certify an infinite theorem by exhaustive computation; the proof in `RESULT.md` supplies the general argument. The tests use cyclic exponent groups, which precisely model nonzero scalar multiplication in finite fields and avoid assumptions about a particular polynomial basis for extension fields. No independent audit was performed.
