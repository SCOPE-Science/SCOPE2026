# Independent review status

Independent audit completed on 2026-10-01 UTC.

Correctness: PASS. For one common \(A\)-block, the two unit-weight FD penalties reduce exactly to a quadratic degree objective on a bipartite incidence graph. With \(D_0=2m+1\) and the specified uniform deletion weight, every retained cardinality different from \(rD_0\) loses more than the maximum shared-edge bonus, and at cardinality \(rD_0\) every nonsaturated degree vector also loses more than that bonus. Thus every optimum is exactly a union of \(r\) complete left stars. The remaining bonus is the number of original edges induced by the selected \(r\) vertices, so the threshold distinguishes a clique. The construction and weight bit-length are polynomial. The committed exhaustive script was inspected; its finite checks are corroborative rather than the proof.

Originality: PASS to the best of current knowledge. Carmeli et al. explicitly list \(\{A\to B,A\to C\}\) as one of the simplest unresolved soft-repairing FD sets. The later approximation and degree-sequence papers located do not solve this unrestricted fixed-FD optimization problem. No earlier or published-archive result located implies the cardinality-lock reduction.

Scientific value: PASS. The theorem closes an explicitly named complexity-classification gap under a restrictive fixed schema and unit FD weights. The common-left pair is structurally natural in database theory, and resolving its exact hardness is materially useful for the sought dichotomy.

Residual limitations: The theorem concerns tuple-deletion soft repairs with pairwise FD-violation penalties. The reduction uses one uniform positive tuple weight depending polynomially on the input; it does not prove hardness with unit tuple weights or determine an approximation threshold. Originality is to the best of current knowledge.

Detailed evidence, searches, source inspections, and risks are recorded in `AUDIT.json` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model assessment evidence is retained in `AUDIT.json` where it existed.
