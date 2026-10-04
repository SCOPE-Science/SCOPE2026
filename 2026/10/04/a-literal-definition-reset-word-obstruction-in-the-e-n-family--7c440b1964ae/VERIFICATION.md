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

`artifacts/verify.py` reconstructs the literal displayed transition table without relying on stored search logs. It checks the proposed reset word, its length, and its strict improvement over the stated Theorem 4 value for each tested state count. It also computes exact shortest reset lengths by breadth-first search over the complete power automaton for \(4\le n\le12\).

The recorded output is in `artifacts/verification_output.txt` and ends with `VERIFY_OK symbolic_n_max=500 exhaustive_power_n_max=12`.

The finite checks do not certify the universal quantifier. The proof in `RESULT.md` does: the image after each block \(a^2b^{n-2}\) is an initial interval with its upper endpoint reduced by two, until the final \(a^2\) collapses the remaining two or three states to state \(3\).

The verification does not claim an exact formula for the reset threshold of the literal cyclic-table automaton for arbitrary \(n\), and it does not test or certify the distinct Figure-6/intended automaton.
