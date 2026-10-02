# Independent audit — Soft repairing is NP-hard for two common-left functional dependencies

Audited: 2026-10-01 UTC

## Correctness — PASS

For one common \(A\)-block, the two unit-weight FD penalties reduce exactly to a quadratic degree objective on a bipartite incidence graph. With \(D_0=2m+1\) and the specified uniform deletion weight, every retained cardinality different from \(rD_0\) loses more than the maximum shared-edge bonus, and at cardinality \(rD_0\) every nonsaturated degree vector also loses more than that bonus. Thus every optimum is exactly a union of \(r\) complete left stars. The remaining bonus is the number of original edges induced by the selected \(r\) vertices, so the threshold distinguishes a clique. The construction and weight bit-length are polynomial. The committed exhaustive script was inspected; its finite checks are corroborative rather than the proof.

Risks: The artifact checks only two three-vertex examples; the general hardness rests on the analytic cardinality-lock argument.

## Originality — PASS

Carmeli et al. explicitly list \(\{A\to B,A\to C\}\) as one of the simplest unresolved soft-repairing FD sets. The later approximation and degree-sequence papers located do not solve this unrestricted fixed-FD optimization problem. No earlier or published-archive result located implies the cardinality-lock reduction.

Equivalent-formulation search: The search separated the two-FD soft semantics from the logically equivalent hard FD \(A\to BC\), which is not equivalent under soft penalties.

Broader-coverage search: Approximation or fixed-cardinality quadratic hardness does not imply exact unrestricted soft-repair hardness without the cardinality lock.

Database/table check: The prior classification for hard repairs does not transfer to soft semantics.

Claim-versus-prior implication: The reduction supplies a genuinely new implication from CLIQUE.

### Source inspections

- **Database Repairing with Soft Functional Dependencies** — Full HTML text, including definitions, the single-FD and matching algorithms, Conclusions, and Open Problems. Assessment: The paper explicitly lists \(\{A\to B,A\to C\}\) as an open case and distinguishes it from the single FD \(A\to BC\).

## Scientific value — PASS

The theorem closes an explicitly named complexity-classification gap under a restrictive fixed schema and unit FD weights. The common-left pair is structurally natural in database theory, and resolving its exact hardness is materially useful for the sought dichotomy.

## Limitations

The theorem concerns tuple-deletion soft repairs with pairwise FD-violation penalties. The reduction uses one uniform positive tuple weight depending polynomially on the input; it does not prove hardness with unit tuple weights or determine an approximation threshold. Originality is to the best of current knowledge.
