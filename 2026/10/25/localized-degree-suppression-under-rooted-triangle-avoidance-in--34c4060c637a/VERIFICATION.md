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

For a deterministic root in G(n,c n^{-alpha}), conditioning on its exact neighbor set gives the stated tilted binomial joint law, and the strictly decreasing successive ratios give exponentially small relative tails on the Lambert scale, not just mode convergence. The cost below alpha=1/2 follows by a binomial lower-tail split; uniform Stirling and exponential tightness give the critical normalization and full conditional LDP. Above alpha=1/2 a binomial relative-degree band proves the diverging-cost case, bounded expectations prove the constant-cost case, and rooted-triangle Bonferroni bounds prove the vanishing-cost equivalence. The nonroot concentration is uniform after conditioning on the neighbor set because its size is o(n) and np is larger than log n. Two minor points in the proof text do not change the conclusion: positivity of the critical minimum follows from the disjoint zero sets of the Poisson entropy and the quadratic penalty, not from the two observations at the end of Step 4 alone; the fixed root-incident edges in Step 6 are deterministic and are not among the edges left Bernoulli. The displayed marginal laws there are correct. Independent derivation: /workspace/proof_check_5.md. The bundled finite checks were inspected, not used as proofs of any limit.

## originality

PASS

The exact mass is an elementary starting point; the supported distinct result is its root-conditioned phase diagram with explicit rates and uniform localization. The nearest same-day indexed result conditions on an additional forbidden cycle, which changes the weight and critical scaling. No examined theorem with the same event or a stronger theorem implying this package was identified; the verdict is bounded, not a priority determination.

## value

PASS

No rooted triangle is the simplest nontrivial local cycle exclusion. The result resolves when its cost comes with a macroscopic relative root-degree change, identifies an explicit critical saddle and good rate function, and shows that even the maximum relative deviation outside the root vanishes. The small-cost regime is controlled at its actual scale, not only by convergence of the event probability to one. These conclusions go beyond the elementary exact mass and do not rely on a global triangle-free analogy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
