---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Campbell Lemmas 3, 4 and 6 have the needed hypotheses: arbitrarily large odd d with a size-(r+3) product-minimizer, existence of three distinct primes for all sufficiently large odd d, and complement optimality for prime p>d with strict next gap >11M. Both deletion sets lie in the prefix, and unique factorization makes the product optimizer unique. Fixed H excludes only O_H(y/log^2 y) primes by summing the unconditional two-linear-form upper-bound sieve (the two roots are distinct modulo every prime not dividing h for each fixed even shift h; odd shifts give only finite exceptions). A cross-prefix collision would force p''<=max|d_i-d_j|, already excluded by p''>max d_i; same-prefix collisions are impossible. Partial summation gives Sigma(y)~y^2/(2 log y), so with at most one boundary prime per translate the count is (2J+o(1))sqrt(X/log X). For every arbitrarily large fixed J this bounds the normalized liminf below by 2J, proving divergence without any growing-J uniformity. The frozen verification notes are analytic, not a computational certificate; its no-rate qualification is not a theorem about how slowly the actual count grows.

## originality

PASS

Credit Campbell's one-offset construction and discrepancy infinitude completely. The supported contribution is the explicit density-one prime-prefix count for arbitrarily many fixed distinct translates and the resulting divergent normalized lower bound. The strongest distinct indexed comparison proves residue-class infinitude and contains a material but unattributed reference to a multiplicity theorem; its verified statements neither identify a separate exact antecedent nor give the stated 2J asymptotic. No equivalent earlier or otherwise distinct proved statement of this scope was located. This is a bounded judgment, not a priority certification.

## value

PASS

This gives a natural quantitative strengthening of an exact-sum partition problem: not just one infinite subsequence, but arbitrarily many asymptotically full translates of the benchmark prime-prefix sequence, with an explicit factor 2J and divergent normalized exceptional count. The proof is economical and the claim does not pretend to determine the complete exceptional set or a natural density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
