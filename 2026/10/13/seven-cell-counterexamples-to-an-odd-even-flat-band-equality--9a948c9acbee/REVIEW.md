# Review of the seven-cell flat-band counterexamples

## Correctness — PASS

For each of the two explicit connected, simple, unweighted motifs, exact symbolic multiplication verifies that the displayed nonzero polynomial eigenvector satisfies the adjacency eigenvalue equation at every root of its asserted minimal polynomial. Direct scalar products with the nonzero binary intercell selectors vanish at those roots, so the single-cell eigenfunctions satisfy the full infinite-graph equations, including equations in adjacent cells. Both minimal polynomials are irreducible over the rationals, coprime, and have positive discriminants (\(17\) and \(316\)), giving five distinct real energies. The six-vertex obstruction uses the complete frozen \(156\)-isomorphism-class atlas of *all* six-vertex simple graphs, including disconnected motifs, and tests exact integer characteristic polynomials for divisibility by either irreducible factor. This is an exhaustive finite proof of the six-cell obstruction, not a sample over graphs or Floquet parameters. All identities and counts replay from `verify.py` and `atlas_n6.graph6`.

## Originality — PASS

Sabri--Youssef (arXiv:2304.06465), Section 4, explicitly ask whether the even/odd equality seen in the four- and five-vertex case persists. Their Theorem 4.6 gives a construction criterion but does not exhibit these two seven-vertex witnesses or prove that their five energies cannot occur in any six-vertex motif; the small-graph lists in their Appendix A stop before the decisive case. The present statement disproves that suggested equality rather than merely restating its sufficient construction criterion. The exact new irreducible polynomials, the six-versus-seven separation, cell-selection aliases, and existing broader flat-band literature were searched. No covering prior statement was found. Faust--Liu (arXiv:2503.03632) and Faust--Kachkovskiy (arXiv:2509.01927) concern generic absence under varying parameters, not this exact unweighted cell-size spectral set. Both irreducible factors are already in the spectrum of the 24-vertex McGee graph (MathWorld). That existing graph-spectrum data alone does not yield a connected seven-cell periodic realization nor an exhaustive six-cell exclusion. The principal residual risk is an equivalent construction in weakly indexed graph-spectral or compact-localization literature.

## Value — PASS

The result answers a naturally posed open equality question at the first previously untested odd stage, providing five distinct real counterexamples, direct positive constructions in connected simple periodic graphs, and a complete obstruction for smaller cells. The finite exhaustion is specifically tied to cell-size minimality, not an arbitrary table or narrow numerical phenomenon. The finding does not claim that the five values exhaust the difference or that generic absence results are contradicted.

## Scientific limits and closest literature

The five-value lower bound for \(\mathcal F_7^s\setminus\mathcal F_6^s\) is exact as stated; the full difference remains unclassified. The 156-class atlas is exhaustive only for unweighted simple six-vertex motifs, precisely the domain needed. The 2023 source contains the earlier equality observations and selector construction; two 2025 genericity theorems are broader in parameter variation but neither contains the implication required to settle the displayed odd-even question. The remaining literature risk is weak indexing of an equivalent seven-vertex example.

Self-review: passed. Independent audit: not yet performed.
