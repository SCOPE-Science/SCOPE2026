# Scientific review

## Correctness — PASS
The finite graph-automaton transition definition matches the word-language definition. Breadth-first construction visits every reachable intersection state. Acceptance is an exact conjunction over all orientations, and merging all tuples with an empty component is language-preserving. The stable Myhill--Nerode refinement computes the exact minimum (not only an upper bound). `verify.py` reconstructed the four finite cases, proved class-transition invariance, and checked every strictness witness; the explicit graph homomorphism proves the general inclusion. No higher-cycle numerical extrapolation is used.

## Originality — PASS within examined evidence
The general graph-based automata framework is due to Pujol (2026, arXiv:2609.08843). A prior run-avoidance theorem covers triangles when chromatic and clique numbers coincide, and the first separating word was already noted. Neither gives the exact minimum complete-DFA sizes for cycles of orders five, seven and nine, nor the two longer-cycle strictness witnesses. Exact-parameter searches in indexed literature and mathematical records identified no covering statement. The primary 2026 paper was available only through its abstract, **not full text**, so a covering manuscript theorem or older equivalent result remains an explicit priority risk. This assessment is not independent novelty certification.

## Value — PASS
The result gives an exact first-family quantitative classification for the first imperfect cycles in a newly studied remanent-language framework: state complexity increases from \(18\) to \(102\) to \(1098\), while the languages become strictly smaller. The general homomorphism inclusion is a structural explanation of the monotonicity. All cases are natural contiguous initial odd-cycle orders, not arbitrary finite instances.

## Scientific limitations
The full originating paper could not be read; publication priority may change under independent examination. Exact state-count results beyond cycle order nine and a general formula remain open here. Reproducible exhaustive computation proves the four finite numbers but no unbounded numerical classification.

Self-review: passed. Independent audit: not yet performed.
