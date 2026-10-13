# Review

## Correctness
**PASS.** The source identifies the sector-wise minimum with \(\dim P_I(C_Z)\) and \(\dim P_I(C_X)\). For a generalized surface code these are ranks of restricted binary incidence matrices. The left-kernel calculation is complete: relation coefficients are constant on erased-edge components; a missing vertex row or a boundary half-edge pins the corresponding constant to zero. This gives exactly \(\ell_Z=|V_I^\circ|-c_Z(I)\) and \(\ell_X=|F_I|-c_X(I)\). Deleting one row from each unpinned component produces an explicit basis. The complexity bound follows because each erased edge creates only constantly many incidences.

The proof does not use the finite checker as an infinite certificate. The checker independently replays exact binary-rank identities on random instances and validates the constructive basis rule.

## Originality
**PASS.** The closest same-object source is Matsumoto's article itself. It proves the minimum-dimension identity and then uses Gaussian elimination in \(O(n^3)\) time to find minimum vertex and face sets, explicitly stating that a faster surface-code-specific alternative is strongly desired. No connected-component rank formula or linear-time minimum local-stabilizer selection appears in the inspected source. Delfosse–Zémor provide linear-time erasure decoding but not this minimum-measurement selection; Matsumoto explicitly distinguishes that point. Connolly et al. address decoding for hypergraph-product codes rather than this minimum surface-code stabilizer basis problem. published-finding corpus searches for incidence-rank, spanning-forest, connected-component, and exact source aliases returned no implication-equivalent published finding.

The graph-incidence rank theorem is classical and is not claimed as new. The new statement is the boundary-aware specialization that exactly solves the source's newly posed minimum-measurement computation while retaining original local stabilizers.

## Value
**PASS.** The result resolves a computational bottleneck highlighted by the source: the minimum measurement set can be selected from the erasure neighborhood itself in linear time rather than by a global cubic elimination. It also gives a transparent structural interpretation of when one measurement can be omitted: precisely one per primal component not touching an omitted/open vertex and one per dual component not touching an erased boundary edge. The result is useful independently of asymptotic decoding performance because measurement count and locality are the source's stated engineering objective.

## Closest literature and limitations
The source's Theorem 5, CSS specialization, Section 5.3, and conclusion were inspected in full-text HTML. The relevant prior decoder papers were checked at their primary publication pages. The main residual originality risk is a differently phrased or newly indexed observation applying the standard incidence-rank theorem to this exact 2025/2026 measurement-minimization setup. The result does not claim a minimum for arbitrary joint/nonlocal observables or a faster algorithm for general stabilizer codes.

Self-review: passed. Independent audit: not yet performed.
