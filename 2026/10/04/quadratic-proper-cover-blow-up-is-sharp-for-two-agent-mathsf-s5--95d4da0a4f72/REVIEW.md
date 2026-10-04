# Review

## Correctness

PASS. In a bounded morphism onto the complete \(m\)-world target, the back condition forces every source equivalence class to map surjectively onto all \(m\) target worlds, so every class has size at least \(m\). Properness for exactly two agents makes every first-agent class meet every second-agent class in at most one point. One first-agent class therefore meets at least \(m\) distinct second-agent classes, each of size at least \(m\), giving the sharp lower bound \(m^2\).

The source construction supplies the matching upper bound and preserves equivalence relations. Equality forces all inequalities in the lower-bound proof to be equalities, yielding \(m\) classes of size \(m\) for each agent and singleton cross-intersections. The bounded morphism is bijective on every row and column, exactly the Latin-square condition. The converse Latin-square construction is immediate and was replayed computationally.

## Originality

PASS. The 2025 primary note constructs a \(W\times W\) proper cover and proves its bounded-morphism properties but contains no minimum-size or optimality claim. The 2026 follow-up explicitly describes the world/perspective multiplication as substantial redundancy and discusses richer structures as a way to avoid it, but does not prove that the quadratic size is forced in any frame class.

Targeted searches for optimal proper covers, quadratic lower bounds, complete \(\mathsf{S5}\) frames, orthogonal partitions, and Latin-square descriptions did not locate an equivalent theorem. General Latin-square literature explains the resulting combinatorial object but does not connect it to proper bounded-morphic epistemic covers.

## Value

PASS. Properization is a recurring technical step in translating Kripke models to simplicial semantics, and the source itself highlights the representational redundancy it creates. The theorem settles the natural sharpness question in the basic complete two-agent case: the quadratic blow-up is unavoidable under the same semantic comparison and frame conditions. The equality classification is stronger than a size lower bound, identifying all extremal covers with Latin-square grids and thereby connecting optimal semantic simulation to a well-developed combinatorial structure.

## Closest literature and limitations

The closest source is Bjorndahl and Sink's 2025 properization note, especially its finite \(W\times W\) construction and bounded-morphism theorem. Their 2026 simplicial-belief paper republishes the construction and explicitly notes the resulting redundancy.

The theorem is not a universal lower bound for all numbers of agents or all relation classes. Richer semantic representations such as simplicial sets can evade the proper-complex requirement altogether.

Same-model review: passed. Independent audit: not yet performed.
