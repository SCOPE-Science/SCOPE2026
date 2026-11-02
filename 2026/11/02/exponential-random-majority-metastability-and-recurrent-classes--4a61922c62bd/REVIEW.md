# Scientific assessment

## Correctness — PASS

The graph has exactly \(s+4k+1\) vertices and diameter six for \(k\ge2\). Anchors with two same-colored leaves never switch. At hub support \(s=k-1\), the blue hub survives if and only if at least one of its \(k\) floating neighbors is blue, yielding the exact geometric escape law with rate \(2^{-k}\). Three successive all-white floating outcomes force total extinction irrespective of prior anchored state, so all-white is the only absorbing communicating class accessible in the anchored invariant subsystem; this supplies the required finite-expectation upper bound and makes the geometric escape a genuine lower bound on stabilization. At support \(s=k+1\), the hub's leaves force it blue and the \(2^k\) floating patterns form a closed complete one-step transition class. The independent exact-kernel code checks \(2\le k\le7\) but does not replace the infinite proof.

## Originality — PASS, conditional on the inspected literature

Zehmakan (2023; 2024 expanded version) already proves both exponential phenomena for general graphs; that priority is expressly credited. The exponential-time witness there joins multiple random-tie vertices to two common hubs, yielding four-cycles, while the recurrent-class construction has cliques. Neither construction meets the tree claim by logical implication. The deterministic, odd-degree tree results of Benjamini–Zakharov–Zhukovskii (2025/2026) have no random tie vertices, so they do not bound the present process. Closest exact comparisons, synonym searches, and residual priority risks are detailed in `AUDIT.json`. Search absence is not proof of novelty; a prior acyclic random-tie construction may be unindexed.

## Mathematical value — PASS

The original general-network exponential examples do not settle whether graph acyclicity or bounded diameter prevents the random-tie metastable bottleneck. The two explicit tree regimes show both obstructions survive on depth-three rooted trees, with simple exact probability laws and a small local support adjustment. This is a structural worst-case boundary for a natural network class, rather than a numerical parameter substitution or isolated small graph.

## Boundaries

No general bounded-degree claim, random-initial-condition claim, optimal diameter claim, or deterministic orbit length claim is made. External independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
