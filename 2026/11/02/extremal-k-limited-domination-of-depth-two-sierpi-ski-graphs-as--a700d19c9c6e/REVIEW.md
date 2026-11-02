# Scientific assessment

## Correctness — PASS

For every admissible pair of integers, a diagonal vertex with no linking neighbour forces its row to contain a selected vertex. Any selected vertex in a row of occupancy \(t\) already has \(m-t\) unselected neighbours in its clique, proving occupancy at least \(m-k\). Symmetric cyclic-offset incidence matrices attain this bound simultaneously in every row. At equality, every selected vertex saturates its allowed unselected row neighbours, hence all selected off-diagonal linking endpoints must occur in symmetric pairs. The reverse implication is immediate; exact product and component enumerations follow. The proof covers all boundary values. Direct graph-subset and independent matrix-enumeration tests corroborate it through orders displayed in `VERIFICATION.md`.

## Originality — PASS (qualified historical priority)

The main 2026 primary paper, arXiv:2610.01584v1, Section 5, already establishes the \(k=1\) **minimum size** for every depth and the alphabet-three family. Its Conjecture 12 proposes the general minimum-size expression, but it does not state the depth-two equality classification or the exact number of optimizers. The present theorem proves the cardinality at all other admissible capacities for depth two and enumerates optimum sets at all capacities by a symmetric-matrix bijection. The foundational article arXiv:2606.22422 introduces the invariant and its alternative domination formulations but does not cover this family in its accessible full text. Ordinary Sierpiński domination is a different problem. Targeted mathematical-record searches for the parameters, aliases, coefficient enumeration, and involutions did not find equivalent coverage; negative search results are not uniqueness proofs. Residual risk: uninspected older \((0,k)\)-pitchfork or \((1,t)\)-domination literature could contain a stronger formulation.

## Mathematical value — PASS

A newly stated conjecture asks for the extremal cardinality throughout the Sierpiński family. The theorem closes all capacities for a natural nontrivial depth-two subfamily and, more importantly, gives a complete *structural* equality characterization and exact count of every optimum set. The symmetric binary row-sum model provides usable counting techniques: complementary capacity duality, involutions at the endpoints, and a labelled-path/cycle exponential generating function at row sum two. These are natural, motivated extremal invariants, not arbitrary finite census slices.

## Limitations and external verification

Depths above two and nonminimum sets are not covered. The coefficient expression need not simplify for intermediate capacities. The relevant prior paper contains a conjectured formula, not a proof for the stated unproved cases; no claim of having resolved the full conjecture is made. Historical priority is qualified; independent mathematical assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
