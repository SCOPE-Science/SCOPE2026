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

The two disjoint triangular blocks have no perfect matching; any added cross-edge completes one using the two residual pairs. The ten facets can therefore be removed without deleting any proper face. An independent exhaustive replay at /workspace/branches/cb6bb943-0293-41ef-b898-73fe02937ad9/independent_npm6_check.py rebuilds the 7935 faces of Y including the empty face, checks all 43920 directed Hasse incidences and recovers 3967 pairs and one critical 4-simplex. Removing the pair containing the empty face restores one critical vertex in ordinary discrete Morse theory, hence Y≃S⁴. The replay independently solves the signed integer cocycle equations, gets 52 nonzero values all ±1, checks coclosedness on all 5-simplices of Y and evaluates the ten attaching boundaries as (1,−1,1,−1,1,−1,1,−1,1,−1). These unit evaluations prove primitive attaching classes. The integral sequence of (X,Y) has just ten relative cells in degree five, giving exactly the kernel and vanishing of every other reduced group. A transposition within a fixed triple reverses the corresponding facet and therefore its primitive boundary, forcing sign on H4(Y). Normalizing each relative generator to boundary +1 makes its action a signed permutation, proving the asserted augmentation kernel by the facet coefficient map. The stabilizer is transitive on other partitions by intersection pattern, and a transposition fixes four splits; the rank-nine rational augmentation has transposition trace +3, identifying S^(4,2), and the twist gives the stated conjugate Specht type. The canonical integral map from kernel to quotient is I+J, determinant 10; rational two-transitivity makes the relevant rational Hom space one-dimensional, and an off-diagonal entry of 1 forbids a noninteger integral-map scalar. Thus no equivariant integral isomorphism of these lattices exists. The independent replay did not enumerate all 720 action matrices; the sign and lattice arguments do not require that enumeration.

## originality

PASS

The homotopy type, restricted representation and related full-group conjecture are prior. The distinct checked claim is the full integral S6 lattice for the six-label complex, with primitive attaching degrees and its geometric identification on the ten deleted facets. The closest indexed same-day lattice is an augmentation quotient for a different space, not an isomorphic integral lattice.

## value

PASS

The six-label no-perfect-matching complex is a natural case of an explicit full-group representation problem, not an arbitrary numerical cutoff. The integral form is recoverable directly from ten distinguished facet coefficients with a proven primitive normalization; it resolves an actual ambiguity between two inequivalent lattices invisible over Q. This is useful even without a general solution of the conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
