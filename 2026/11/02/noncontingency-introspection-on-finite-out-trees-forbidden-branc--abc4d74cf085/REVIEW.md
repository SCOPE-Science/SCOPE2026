# Review: noncontingency introspection on finite out-trees

## Correctness — PASS
The operator is constant truth over immediate successors. At a world with at most one child, the nested consequent is vacuously true. A branching child of a branching parent is a necessary and sufficient obstruction: construct a valuation constant on the parent's children and nonconstant on two children of the branching child, while keeping a second child's own successor set constant. This gives the full iff statement. The resulting labelled-species equations are \(A=z(1+T)\) and \(T=A+z(e^A-1-A)\), with independently derived coefficient recurrence. Positive implicit-function singularity analysis yields the exponential-rarity asymptotic. The standalone exact checker enumerates all rooted labelled trees through seven vertices and exhaustively checks valuation semantics through six vertices; its finite scope is not confused with the infinite proof.

## Originality — PASS, with limits
The motivating 2026 paper develops semantic GPC-calculus completeness, while Fan's earlier primary full text addresses bimodal variants and frame definability; the exact labelled out-tree census and its asymptotic are not results observed in those inspected full texts. published-finding corpus claim-level searches compared unrelated finite-tree orbit-profile, directed-tree and modal-frame findings and found no encompassing result. Cayley's ordinary counts are strictly broader than the new subclass and do not imply the present refinement. The 2015 Fan–Wang–van Ditmarsch full text could not be inspected; an earlier equivalent correspondence or a pre-existing differently named tree enumeration remains a historical-priority risk. A negative search result is not proof of uniqueness.

## Mathematical value — PASS
The noncontingency introspection schema is a natural modal principle. Its validating tree frames admit a sharp local structural classification, an exact all-size labelled census, a minimal failing size, and a nontrivial singularity-controlled exponential rarity law. The dependence on immediate-child accessibility is essential and delineates an interpretable boundary of the finding.

## Scope and reproducibility
Results concern classical Kripke valuations on finite rooted trees with only outward parent-to-immediate-child edges, no loops and no transitive closure. The same package contains the proof, exact recurrence, all checks and a standalone standard-library checker. Numerical constants are approximations, not certified intervals. No external or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
