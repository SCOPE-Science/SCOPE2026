# Scientific review: rectangular detectors on weighted rook networks

## Correctness — PASS

The claim has an explicit all-parameter domain (two clique-factor sizes at least two, two positive hopping strengths, any nonempty detector rectangle, any strictly positive detector rates, and any initial site or density matrix). Contractivity of the non-Hermitian dynamics identifies eventual capture with the detector-visible Hermitian spectral span. The product of two complete-graph adjacency matrices has exactly four tensor eigenspaces; the only possible collision is the equality of weighted gaps \(am=bn\). The tensor projector proof gives the nonresonant dimension and exact diagonal capture profile. At resonance, the row/column-sum image has codimension exactly one when and only when both detector subsets are proper, and the explicitly constructed dark vector accounts for the precise projector correction. Complete-capture threshold follows from full rank. This also handles the small boundaries \(m=2\), \(n=2\), and full-factor detector sets. Independent numerical diagonalization checked 800 all-rectangle instances, and 12 non-Hermitian propagations checked survival; no finite computation is substituted for proof. See `RESULT.md` and `verify.py`.

## Originality — PASS, with residual priority risk

Ge et al. (arXiv:1009.1340) already establish Cartesian-product quantum walk constructions. Razzoli et al. (arXiv:2011.13794, §4.2 Eq. (25)) already establish one-sink capture for strongly regular graphs, which **includes the equal-weight square rook graph with one detector**. That subcase is not presented as new. Cavazzoni et al. (arXiv:2205.09408) analyze graph perturbations with one sink on different complete/bipartite/star topologies. The original contribution assessed here is the entire two-hopping, arbitrary rectangular *multi-sink* bright-rank and sitewise capture law, the exact unique resonance-dark vector, and the sharp complete-rectangle thresholds. Literature searches for rook-graph trapping, Cartesian-product multi-sink transport and aliases did not identify an equivalent evaluated classification. A larger general projector theorem could be specialized to the same result after additional calculation, and an unlocated exact evaluation is possible. Such residual priority uncertainty does not constitute independent verification.

## Value — PASS

Rectangular arrays of imperfect detectors on Cartesian-product cliques are natural finite two-coordinate network monitoring patterns. The theorem resolves for every size, placement and positive rate how much of the state space is observable/absorbed, including a fully local capture law; it identifies a sharp single-mode obstruction exactly when the two hopping gaps coincide. For full capture the minimum number of detectors constrained to form a rectangle changes from \((m-1)(n-1)\) to \(mn-\max(m,n)\), a placement-design consequence that is not just an accuracy increment or parameter renaming. It provides a testable dimension and sitewise prediction without solving any long-time differential equations.

## Risks and limits

The result is a self-review, not an independent audit or a publication-priority certificate. Its proven domain excludes nonrectangular sensor sets, disorders, phase hopping, dephasing, interacting walkers and finite-time rate estimates. An unlocated specialized multi-detector result remains possible; the finite verifier corroborates but does not establish the infinite-family theorem.

Self-review: passed. Independent audit: not yet performed.
