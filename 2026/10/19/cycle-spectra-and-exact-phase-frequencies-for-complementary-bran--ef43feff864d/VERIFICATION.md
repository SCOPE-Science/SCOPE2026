---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At m=N-1 row i of the unshuffled integer incidence matrix omits exactly N-1-i. Shuffling columns consequently gives J-Q, with q=sigma composed with the reversal and hence all q equally represented. Constants contribute m and on the invariant zero-sum subspace the action is -Q, giving the displayed cycle polynomial after removing one t+1. Thus for d>=2 occurrence of a fixed primitive phase is equivalent to the presence of a cycle of length divisible by d. The exponential generating function for avoidance is (1-z^d)^(1/d)/(1-z), whose binomial partial sum at floor(N/d) gives the product. Order 1 is separate because one constant eigenvector was removed: exactly the single-cycle permutations lack -1/m. The coarse finite Markov eigenvalues are genuine piecewise constant BV eigenvalues (changing the row/column convention transposes without changing spectrum). The source's proven upper bound equals the essential radius 1/m in this family. A cycle of length N-1 gives a phase on the mixing-rate circle, not among the listed conjectural vertices; for even N the additional sign is itself an N-th root and for odd N the common sign cancels in the comparison. Strict convexity of the disk excludes this phase from their hull. This refutes the literal v3 hull statement and its maximal-radius consequence, not the proven rate bound or a modified statement about isolated eigenvalues outside the essential disk. The result describes the finite matrix, not the entire BV spectrum.

## originality

PASS

Credit the existing Markov reduction, the rate bound and the standard cycle-index counting formula rather than claiming them as independent discoveries. The supported contribution is the complementary-branch identification and its phase census for shuffles, especially the resulting witness against the literal hull statement in the identified primary version. No equivalent spectral census or antecedent witness for this conjecture was found in the checked sources.

## value

PASS

A falsifiable hull conjecture is resolved literally for a whole family rather than by a numerical anomaly. The example isolates the distinction between rate information and the positions of poles or eigenvalues at the essential-radius boundary. The exact counts quantify how often the counterexample phases occur and clarify what survives the constant-direction projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
