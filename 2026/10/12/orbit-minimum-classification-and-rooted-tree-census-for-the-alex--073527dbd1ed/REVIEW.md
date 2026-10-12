# Self-review of the finite-chain Alex classification

## Correctness — PASS

The claim specifies every \(n\ge1\), arbitrary total temporal endofunctions, the upset Alexandrov chain topology, all propositional valuations, and zero-inclusive eventuality. The proof derives equivalence between \(\mathsf{Alex}\) and monotonicity of the attained orbit minimum by singleton valuations and the reverse witness construction. It proves that the orbit minimum is a regressive idempotent, so in the monotone case it is the floor map onto its fixed-point set. Its fibers are consecutive blocks; every nonroot edge stays in its block and reaches its root, while each root may point to any later or equal world. The converse explicitly shows that all future orbits stay above their first root. Cayley's rooted labeled tree count and independent choices then yield the exact enumeration. The source-code verifier checks all maps through seven worlds, and direct modal valuations through five worlds, plus recurrences through ten. There is no inference from tested sizes to the universal result.

## Originality — PASS, with residual risks

The closest 2026 primary result [1] defines and validates \(\mathsf{Alex}\) for **monotone** dynamics, while this theorem classifies **all** (possibly discontinuous) maps that validate it on finite chains. The displayed two-point map witnesses that its scope is strictly wider, so it is not a corollary merely of the older implication continuity \(\Rightarrow\mathsf{Alex}\). Papers [2–3] also assume continuous dynamics or use Cantor derivatives; their full relevant definitions and results address different questions. The construction depends on classical Cayley enumeration, but that formula alone does not identify the axiom-valid mapping class or its block-dependent independent factors. Targeted published mathematical and research-record searches disclosed no equivalent finite-chain characterization or sequence; older equivalent results in different terminology and unindexed tables remain possible.

## Value — PASS

The 2026 motivation highlights \(\mathsf{Alex}\) as the modal bridge between spatial closure and temporal reachability. The proof isolates its exact strength when the continuity assumption is intentionally removed, distinguishes it from full monotonicity, and gives an explicit structural parametrization of the resulting finite models. It computes an entire natural invariant \(A_n\) with a fast recurrence, not an arbitrary fixed small case: at five worlds \(1825\) maps satisfy the axiom, compared with only \(126\) monotone maps. Such a map classifier can be used to construct semantic stress tests and enumerate finite countermodel candidates for temporal-topological implication problems; this possible use is not a theorem about proof-system decidability.

## Closest literature and limits

[1] Vooijs–Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, DOI 10.4230/LIPIcs.LICS.2026.81, specifically Introduction and Example 2.10.

[2] Konev–Kontchakov–Wolter–Zakharyaschev, *Dynamic Topological Logics over Spaces with Continuous Functions*, Advances in Modal Logic 6, 2006.

[3] Fernández-Duque–Montacute, *Untangled: A Complete Dynamic Topological Logic*, AAAI 2023, DOI 10.1609/aaai.v37i5.25782.

This theorem is restricted to the axiom \(\mathsf{Alex}\) on finite chains with arbitrary total maps. It does not extend to general preorders or all DTL formulas. Old literature under alternate notions of weak continuity has not been fully ruled out, and no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
