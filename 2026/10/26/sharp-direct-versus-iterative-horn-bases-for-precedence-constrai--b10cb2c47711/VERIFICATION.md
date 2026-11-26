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

Acyclic input gives exactly strict reachability: when a pair is not reachable, adjoining its reverse does not create a cycle and a topological order witnesses nonentailment. Cyclic input has no models and closes to all oriented pairs. Each two-edge directed path missing its shortcut, and each opposite-arrow pair, forces an exact premise in any iterative basis: no proper subset allows the first nontrivial inference. These rules suffice. For simultaneous directness a path's endpoints force its entire simple-path premise, and a proper cycle forces its entire premise by choosing a conclusion incident to an outside vertex. A spanning directed cycle needs only its proper path premises, which already supply every missing oriented pair. Counting the distinct path and cycle premises gives the two displayed sums; the cycle sum divided by n! tends to zero by splitting at n/2. Midpoint subdivision adds comparisons along paths of length at most 2^t in t rounds. A proper cycle yields an opposite-arrow pair by L−1 using forward cyclic distances at most ceil((n−1)/2), whereas a spanning cycle yields all pairs by L without explosion. A spanning path forces L rounds in the stated iterative basis. An independent finite closure-from-models calculation counted minimal nonclosed sets and premises compelled in one round for n=3 and 4, giving (9,9) and (30,62). The combinatorial proof, not this enumeration, covers all n.

## originality

PASS

The supported distinct contribution is the exact paired minimum counts and depth for the oriented-comparison closure, in particular the precise proper-cycle versus Hamiltonian-cycle boundary for the minimum direct basis. Generic minimum/direct basis theory, transitive closure and parallel doubling are established background. None of the inspected closest statements supplies the specialized path/cycle classification or its counts.

## value

PASS

Linear precedence constraints are a natural closure model with consistency and transitivity. On exactly the same attributes the result quantifies the cost of insisting on one simultaneous pass: factorial many grouped premises instead of cubic many with logarithmic depth. The reason proper cycles but not spanning cycles require new direct premises identifies which inconsistent inputs cause additional rules; this is not just standard transitive-closure doubling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
