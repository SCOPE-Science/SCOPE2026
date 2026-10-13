# Scientific review — maximal graded-to-ordinary separation on sparse S5 grids

## Correctness — PASS

The target frame, two named reflexive equivalences, single valuation, graded thresholds and depth convention are explicit. The ordinary two-type collapse follows from the fact that every row and column has both colors for \(n\ge3\). For graded types, the proof establishes a histogram recurrence equivalent to depth-bounded counting formulas, proves by induction an alternating peeling of the endpoints of the associated bipartite path, then counts exactly three mixed Cartesian blocks at each intermediate depth. The stabilization and quotient-ratio optimality follow without numerical extrapolation. Critical boundary cases \(n=3\), \(t=0\), \(t=n-2\), and \(t=n-1\) are explicitly covered. Standard-library computations corroborate but do not replace the unlimited-\(n\) induction.

## Originality — PASS (qualified)

Ahvonen–Heiman–Kuusisto (arXiv:2401.06519, submitted 2024-01-12) develops graded multimodal types and multiset-counting automata, which supplies the general language but does not state this specific maximal separation on the S5 grid or its quadratic depth census. Comer (arXiv:2404.15421) relates graded logical equivalence to homomorphism-count vectors rather than computing the proposed marked grid. Otto (arXiv:1910.00039) supplies foundational counting-bisimulation semantics. Other quantitative results on ordinary Ferrers-marked grids and graded-versus-ordinary regular trees differ simultaneously in frame, valuation, and numerical statement. The actual targeted searches found no stronger result implying the combined exact claim. The possibility of an implicit antecedent is recorded rather than ruled out categorically.

## Mathematical value — PASS

For the natural finite two-agent epistemic square, the result quantifies the greatest possible semantic information gain from counting: the ordinary quotient has only two types, the graded quotient has every world, and the extremal ratio is exactly \(n^2/2\). A marked incidence set of only \(2n-1\) cells suffices, and the exact type count at each depth is a new finite quantitative invariant of a simple model. The proof exposes the structural reason through propagation along a bipartite Hamiltonian path; it is not a generic substitution into the message-passing equivalence theorem. No false claim of generic novelty or support-minimality is required.

## Closest prior literature and limitations

- V. Ahvonen, D. Heiman, A. Kuusisto, *Graded modal logic and counting message passing automata*, https://arxiv.org/html/2401.06519v2 — inspected graded syntax, full types, refinement algorithm, results and discussion.
- J. Comer, *Lovász Theorems for Modal Languages*, https://arxiv.org/html/2404.15421 — inspected available introduction, main contribution statements and graded modal context; no exact grid spectrum identified.
- M. Otto, *Graded modal logic and counting bisimulation*, https://arxiv.org/abs/1910.00039 — reviewed abstract and metadata; a full-text comparison of this earlier background note was not completed.

The theorem does not establish minimality of the \(2n-1\) marked cells. A precise equivalent formulation in an unindexed color-refinement source could remain undiscovered. The result has not received an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
