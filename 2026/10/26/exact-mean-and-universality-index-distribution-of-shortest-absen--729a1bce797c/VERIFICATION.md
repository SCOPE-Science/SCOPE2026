---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The greedy binary arch decomposition consists of words a^m opposite(a) and a residual unary/empty suffix. The exact earliest-match condition for a shortest absent subsequence gives a two-coordinate transfer: if m=1 the own-initial-letter count propagates, and if m>=2 that coordinate vanishes; the opposite-initial-letter count equals the sum of suffix coordinates. Summing all arches gives a symmetric 2x2 transfer with eigenvector (1,1), eigenvalue u*z^2*(3-z)/(1-z), and residual vector (1,1)/(1-z); formal geometric inversion proves H exactly. Coefficient extraction and singularity analysis yield the finite sum, recurrence, and positive exponential mean. Independently generated all 2047 words n<=10 and brute enumerated subsequences, matching the bivariate coefficients and scalar totals. Empty/unary ambient alphabet convention retained.

## originality

PASS

Best-of-knowledge mathematical comparison: The exact bivariate theorem does not follow from a mere substitution in the unweighted generating function. A more comprehensive weighted-automaton formula could cover it, but none was located.

## value

PASS

The weighted joint statistic is natural because universality index alone misses the number of shortest missing scattered strings. The complete bivariate rational law and mean exponential growth quantify a distribution not captured by known maximum or unweighted index counts; it is not simply recomputation of the pre-existing scalar OEIS sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
