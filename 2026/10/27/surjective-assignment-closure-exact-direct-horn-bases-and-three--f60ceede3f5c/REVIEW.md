# Scientific review: surjective-assignment direct bases

## Correctness — PASS

The central feasibility equivalence \(q-|p(D)|\le n-|D|\) is necessary and sufficient. An extendible partial assignment cannot force an unassigned value unless exactly one input and one colour remain. A minimally impossible partial map without positional conflict has deficiency one and no singly used colour, because removing a singleton-used colour preserves deficiency and removing a repeat-used colour reduces deficiency by one. These facts classify every inclusion-minimal premise with a new entailed atom. For the full-domain shortage premises the proof explicitly exhibits an atom that is not implied by any proper subset, which establishes the nontrivial direct-basis lower bound. Counting is by labeled positions, used colours, and partitions into blocks of size at least two. The three-colour lattice count uses a disjoint infeasibility decomposition. A separate bitmask-based checker reconstructed the exact closure of all subsets for four small cases and completed larger deterministic samples. Finite tests only corroborate the unlimited-parameter proof.

## Originality — PASS, qualified

Wild's 2016 survey already proves that the stem family yields a minimum-cardinality direct basis; this general principle is prior art, not a new theorem. The 2024 D-base paper of Adaricheva, Nourine and Vilmin develops algorithms and complexity results for arbitrary closure systems, and the 2024 preprint of Baixeries and Napoli compares minimal and direct bases. Their inspected relevant sections do not display the onto-function stem classification, the exact associated-Stirling count, or the three-colour lattice cardinality. The bijective boundary \(n=q\) is a narrower, previously investigated assignment context and is explicitly excluded: it cannot settle the nonbijective shortage structures. A title/abstract/term search is insufficient to prove historical uniqueness, so equivalent results under alternative constraint-satisfaction, database or Horn-minimization terminology remain a priority risk. No independent novelty certification has been performed.

## Mathematical value — PASS

For the elementary but genuinely global constraint of using every value at least once, the result supplies the complete minimal positive antecedents for one-round logical consequence and a sharp minimum number of multi-head Horn rules for infinitely many genuinely nonbijective contexts. The associated-Stirling sum distinguishes multiplicity-based inconsistency circuits from the ordinary same-position conflicts. The three-colour formulas give two different exact invariants—optimal direct-basis size and the full number of concept intents—with nontrivial exponential growth. The exact restriction to direct rather than arbitrary iterative bases is mathematically material. This is a structural enumeration, not a presentation-only reformulation of generic direct-basis existence.

## Closest literature and limitations

- M. Wild, *The joy of implications*, arXiv:1411.6432, Section 3.3 and Theorem 2: general stem-minimality principle, credited and used only as context.
- K. Adaricheva, L. Nourine, S. Vilmin, *Computing the D-base and D-relation in finite closure systems*, arXiv:2404.07037 (2024-04-10): general algorithms and hardness of the D-relation, not an identified specialized onto-map census.
- J. Baixeries, A. Napoli, *A minimal base or a direct base?*, arXiv:2404.12229 (2024-04-18): direct-versus-minimal basis algorithms and experiments, not an identified onto-map family formula.

The mathematical claim is limited to \(n>q\ge3\), positive assignment literals, original-set simultaneous rule evaluation, and freely multi-atom conclusions. It does not prove minimality for iterative or unit-conclusion Horn bases, nor establish priority against all possible aliases.

Self-review: passed. Independent audit: not yet performed.
