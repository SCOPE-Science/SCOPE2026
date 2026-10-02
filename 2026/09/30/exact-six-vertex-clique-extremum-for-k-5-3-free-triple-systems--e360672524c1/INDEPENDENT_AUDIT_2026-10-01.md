# Independent mathematical audit — Exact six-vertex clique extremum for K5^(3)-free triple systems

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** For a six-vertex triple system, the complete five-vertex hypergraphs are avoided exactly when the missing triples have empty total intersection. Complementing those missing triples yields a triple family covering all six vertices. If its size is f and its pair-shadow size is s, the total clique count is exactly 57 minus f plus s. A direct case split proves f plus s is at least eight, with equality only for two disjoint triples. Hence the maximum is 49 and the unique isomorphism type is the balanced three-plus-three construction; there are ten labeled partitions.

Checked sources: Assigned RESULT.md; Chen--Deng--Hou--Liu--Zhang 2026; Published-record semantic search.

Residual correctness risks: The human complement-shadow proof is complete, so exhaustive enumeration is not needed for correctness..

## Originality

**PASS.** The current primary theorem proves balanced-bipartite clique extremality only for all sufficiently large orders. It does not state an exact six-vertex base case. Targeted record searches found the audited order-six theorem but no earlier exact value and equality classification.

### Equivalent formulations

Searches/sources: Published-record search for six-vertex complete-five-free triple systems with 49 cliques; arXiv:2606.02210.

Evidence: The exact archive hit was the audited theorem. Chen et al. explicitly state an exact theorem for all sufficiently large orders, not all orders.

The finite theorem is not an equivalent restatement of an eventual theorem with an unspecified cutoff.

### Broader coverage

Searches/sources: Chen et al. eventual clique theorem; Frankl--Gryaznov--Talebanfard clique-counting conjecture.

Evidence: The eventual theorem does not cover order six. The general small-order statement is conjectural background, not prior proof.

No inspected stronger proven result includes the audited order.

### Exact database or table

Searches/sources: Published archive search for order-six complete-five-free clique count; Search for six-vertex triple-system censuses.

Evidence: The nearest finite census found forbids a different tight-cycle configuration. No prior exact table giving 49 for this predicate was located.

Different forbidden configurations do not determine this invariant.

### Claim versus prior implication

Searches/sources: Test whether a sufficiently-large theorem can be specialized to order six; Compare conjectural all-order statement with proven coverage.

Evidence: The large-order hypothesis blocks specialization to six. A conjecture is not proof coverage.

The six-vertex statement needs its own finite argument.

### Source inspections

- **Vertex-colored Turan theorems with applications in extremal hypergraph problems** — EVENTUAL_NOT_COVERING.
  Identifier: https://arxiv.org/abs/2606.02210
  Trigger: Same forbidden configuration, clique objective and proposed extremizer.
  Material read: Primary arXiv abstract and theorem-level description.
  Method: lawful open-access primary source
  Evidence: The source proves exact unique extremality only for sufficiently large order.

Residual originality risks:
- An older finite hypergraph census could contain the same order-six number under different terminology.

## Scientific value

**PASS.** This is the exact first small benchmark and equality type for a natural clique-counting problem currently proved only at sufficiently large order. The short complement-shadow proof makes the finite fact independently useful.

Residual value risks: The proof is special to six vertices and does not determine the later cutoff..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
