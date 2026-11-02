# Scientific review

## Correctness — PASS

Every proper induced subposet decomposes uniquely into cyclic runs, whose isomorphism types are isolated singletons, even paths, and odd paths distinguished by whether both endpoints are minimal or maximal. The automorphism factors are computed from these path types. The two-state run-gap transfer matrix counts proper labeled domains with the exact cyclic-rooting factor \(n/t\). Squaring type multiplicities and multiplying by component-automorphism orders counts all partial isomorphisms, with the full crown's \(2n\) automorphisms added separately. The high-rank coefficients have an independent deletion-distance calculation, and the attached verifier exhausts small cases. Risks: none of the finite enumerations alone proves the identity for arbitrary size, so the structural proof is indispensable.

## Originality — PASS relative to investigated literature

Dimitrova–Koppitz (2022, arXiv:2204.13961) study the **same** crown partial-automorphism inverse semigroup but compute its smallest generating-set size, rather than its element rank distribution or order. Their detailed membership criterion, and the accessible generating-rank proof, do not supply a cardinality formula. Dimitrova–Fernandes–Koppitz–Quinteiro (2021, arXiv:2101.12468) study undirected **paths** and compute their monoid cardinalities. Undirected-cycle partial graph isomorphisms differ from crown-poset partial order isomorphisms already at codimension one: \(8n^2\) versus \(4n^2\). A broader poset-component species enumeration could imply the formula, and unlocated literature remains a priority risk; absence of search results is not treated as proof of uniqueness.

## Mathematical value — PASS

For the inverse semigroups that were recently investigated through their generating ranks, the domain-rank profile is a distinct natural invariant: it gives the exact cardinality of the monoid and each of its canonical rank ideals, and records the relative prevalence of large-domain partial symmetries. The two-state formal matrix resolves a genuinely cyclic, parity-sensitive component-label problem that is not captured by undirected graph-run counts. A complete family-wide enumeration, with transparent small-size exceptions and top-rank formulas, is a useful finite-semigroup classification rather than a recomputation of the minimal number of generators.

## Remaining risks and scope

The result is for alternating even crowns with induced-order partial isomorphisms and includes the empty map. It is not a formula for the minimal size of a generating set, nor does it classify noninjective or one-sided order-preserving maps. Other sources with general labeled component-enumeration formalisms may overlap. The full-source comparisons are specific to the two cited arXiv papers; priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
