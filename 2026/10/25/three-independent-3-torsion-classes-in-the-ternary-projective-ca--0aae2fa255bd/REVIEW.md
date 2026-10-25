# Scientific review

## Correctness — PASS

The object has a canonical coordinate definition over \(\mathbb F_3\), and the exhaustive verifier independently generates the 13 projective points, all \(\binom{13}{k}\) candidates up to size five, and the complete signed boundary maps. The resulting Smith factors are exactly \(1^{12}\) for \(\partial_1\), \(1^{66}\) for \(\partial_2\), and \(1^{165},3^3\) for \(\partial_3\). The chain identities are explicitly checked. The quotient argument in the proof deduces integral, not merely rational, homology. The graph of the one-skeleton is complete, the projective group sends every ordered quadrangle uniquely to a fixed frame, and only the 234 quadrangles have all four constituent triangles. The claimed finite certificate is reproduced from the distributed checker and its inputs without relying on a previous execution log.

## Originality — PASS (best-knowledge, with risk)

Three independently identified lines of prior work were compared by their mathematical statements. Classical matroid-shellability results cover the two-skeleton's wedge-of-two-spheres homotopy type; that does not determine whether attaching 234 three-simplices leaves an integral index-27 sublattice. Ranade–Sadanand–Sullivan's integral top-homology cycle framework is general and does not report this finite plane or its index. Ardila–Castillo–Samper's matroid shelling theorems likewise stop short of the cap complex's attaching-map Smith factors. Superdock's projective-plane-derived complexes are different: they consist of 26 facets for order three, not the 234 quadrangles used here. The closest identified separate published result concerns a neighborhood complex of the same plane's point–line nonincidence graph, a distinct simplicial object. Search failure alone is not novelty evidence; the substantive comparisons show why the inspected implications do not cover the claim. Residual risk: equivalent work outside the inspected corpus, and incomplete access to some older general matroid sources.

## Mathematical value — PASS

The index-27 obstruction quantifies an unexpected integral failure of geometric minimum-support sphere cycles to span their natural matroid homology lattice. The resulting \((\mathbb Z/3)^3\) torsion supplies new finite topological information about a canonical projective configuration, whereas shellability and rational Betti ranks alone cannot detect it. The claim treats a natural complete collection of geometric faces, not an arbitrarily selected subfamily, and the exact torsion decomposition is potentially useful for studying integral face attachments and symmetry of small finite geometries.

## Closest literature and limits

See Ranade–Sadanand–Sullivan (arXiv:1203.5288), Ardila–Castillo–Samper (DOI 10.37236/5042), and Superdock (arXiv:2110.12314). This finite computation does not classify higher-order projective planes, the cap complex's homotopy type, or its integral automorphism representation. Bibliographic originality remains subject to independent checking.

Self-review: passed. Independent audit: not yet performed.
