# Scientific review

## Correctness — PASS

For a one-generation-infectious single-seed process on a tree, each potential infection has a unique parent path, giving an exact Bernoulli bond-percolation representation. The expected peak-indexed cumulative infection statistic is therefore the finite bond polynomial in `RESULT.md`. Its derivative has the explicitly derived Bernstein representation. The provided standalone program exhaustively enumerates all labeled trees through seven vertices using Prüfer codes, identifies the 85 rooted types via canonical recursive child codes, enumerates every edge-state mask, and rederives all integer/rational profile coefficients in `rooted_tree_certificate.tsv`. All 36 rooted types of orders at most six have nonnegative Bernstein differences; among 48 seven-vertex types exactly two have negative terminal differences. Their formulas are also reconstructed by elementary event conditioning independently of the exhaustive enumeration; Descartes' rule proves unique interior peaks. Program and certificate were executed and compared from their actual packaged paths. Limitation: finite enumeration does not imply anything for larger graphs.

## Originality — PASS (best-knowledge, not independent priority certification)

The closest source, Ozbay–Nielsen–Nguyen, arXiv:2212.06995, establishes that a peak-indexed epidemic statistic can be nonmonotone in discrete-time SIR models and offers simulated large-network examples; that observation is acknowledged as prior. Our additional statement is the sharp *smallest rooted-tree size*, the census of two exceptional rooted shapes, and their exact probability polynomials and peak thresholds. Sharkey–Kiss–Wilkinson–Simon, DOI:10.1007/s11538-013-9923-5, analyze continuous-time Markovian SIR on trees, establishing exact fixed-time means but no earliest-sample-peak functional. Curran-Sebastian–Pellis–Hall–House, arXiv:2301.07058, approximate peak-time uncertainty through branching/deterministic dynamics, not the present exact rooted-tree census. Semantic research-record searches and own-claim deduplication identified no stronger implication, matching enumeration, or equivalent published claim. Residual publication-priority risk from broader combinatorial epidemic-functionals literature remains explicit.

## Value — PASS

The motivating model highlights a paradox in peak-indexed epidemic severity estimates without pinpointing the smallest contact networks needed to realize it. A natural and complete sharp threshold within rooted trees, including the exact number and shape of first exceptions, clarifies which topology and tie-sensitive peak shift first permit the phenomenon. The two exact polynomial examples provide reproducible benchmarks for finite stochastic epidemic modelling. The precise mathematical motivation is the natural peak-indexed statistic and first-obstruction census, not a policy effect size or a claim about general networks.

## Scope and risks

The result assumes a predetermined single seed, independent identical edge probabilities, synchronized generations, immediate removal after one infectious generation, and the **first** maximum of prevalence. Changing those assumptions can change the classification. The independent novelty audit and external scientific validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
