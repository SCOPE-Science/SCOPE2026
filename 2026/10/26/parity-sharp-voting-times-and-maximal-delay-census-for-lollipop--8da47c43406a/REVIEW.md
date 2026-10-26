# Research review: parity-sharp lollipop majority dynamics

**Correctness — PASS.** The core threshold calculation and frozen-pair propagation proof cover all integer clique sizes at least three and all pendant lengths at least two. The two even-clique maximum-delay mechanisms have disjoint explicit descriptions, and their counts sum to the stated power of two; primitive two-cycles occur immediately only at the critical threshold with a fully alternating path. The bundled independent graph simulation checks 53 finite graphs and 768,032 labelled configurations; no finite test is used as a proof for unbounded sizes.

**Originality — PASS, bounded to examined evidence.** The closest same-rule primary full text is Kaaser, Mallmann-Trenn and Natale, arXiv:1508.03519v1, whose §3 and Appendix C provide general voting-time estimates and an alternating-path example but not this lollipop sharp parity/count law. The closest same-graph text is Mertzios et al., arXiv:1404.7671v1, §5.3, which studies a stochastic three-state pairwise protocol, not the two-state synchronous map. Existing exact bridge-barbell and circular Rule-232 claims address different graph boundary conditions. The search does not prove historical uniqueness; an unindexed counterpart is possible.

**Mathematical value — PASS.** A naturally coupled dense/sparse graph changes its sharp delay and critical-population law when one changes the parity of clique size. The complete extremal census and explicit characterization expose a nontrivial front-propagation mechanism and an odd-versus-even asymptotic rarity distinction, providing sharper information than general voting-time upper bounds.

**Limitations.** Binary synchronous tie-retaining open-neighborhood majority, one clique, one terminal path, clique size at least three, path length at least two. No claims about other update conventions or graph families. Computational enumeration supports but does not logically entail the all-size theorem.

Self-review: passed. Independent audit: not yet performed.
