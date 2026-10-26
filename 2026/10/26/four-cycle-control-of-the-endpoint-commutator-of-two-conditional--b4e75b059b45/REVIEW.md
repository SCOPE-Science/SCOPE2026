# Review of the four-cycle endpoint commutator theorem

## Correctness

**PASS.** With uniform measure on graph edges, both conditional expectations are orthogonal projections in \(L^2\). The proof writes their ordered compositions explicitly, obtains a skew matrix, and counts the nonzero entries of every row through four-cycles containing the row's edge. This establishes the exact finite-dimensional \(L^1\) and \(L^\infty\) norm by full row and column sums and sign extremizers. The equality classifications follow from the maximum possible local four-cycle count and from perfect-matching decompositions of projective-plane incidence graphs. The separate Hilbert norm uses the projective-plane incidence Gram matrix and two-projection principal-angle blocks. The standalone exact checker replayed with `ALL_CHECKS_OK 44523`; its finite cases are corroboration, not a proof of all degrees.

## Originality

**PASS within inspected evidence, with priority risk.** Walters' arXiv:1604.00699v1 was inspected in full HTML, including the Hilbert-space commutator estimates, and Abiad–Dalfó–Fiol's arXiv:1205.5913v1 was inspected through its available complete HTML. Neither states the four-cycle identity for edge-supported conditional expectations. Comparable research records on numerical radius and conditional-expectation chains were inspected at the title/summary level, with no assertion of complete full-text noncoverage. An earlier exact result for a single excluded product rectangle concerns generally irregular support; another graph-edge result concerns an orthogonal gradient projector, a different operator. The full all-regular-graph equivalence and its projective-plane endpoint/Hilbert contrast were not found in the actual checks, but historical novelty is not certified by search alone.

## Mathematical value

**PASS.** The theorem solves an all-degree exact operator-norm question using a local graph invariant and characterizes both maximal noncommutation and exact commutation. Its prime-power incidence examples exhibit qualitative non-equivalence of Hilbert and endpoint stability even though the same two conditional expectations are used throughout. The result is a natural structural classification, not an arbitrarily selected numerical graph case.

## Closest prior literature and limits

Walters (2016) treats operator norms of anticommutators and bounds for commutators on Hilbert space; the present endpoint norm is not a Hilbert commutator inequality. Abiad, Dalfó and Fiol (2012) analyze regular bipartite graph spectra and distance-regularity rather than conditional averaging commutators. Source summaries of related conditional-expectation records were not substitutes for complete primary-document review. The present statement requires regular degree and uniform edge mass; weighted or irregular generalizations are not proved. Independence of external scientific review and exhaustive historical priority are not asserted.

Self-review: passed. Independent audit: not yet performed.
