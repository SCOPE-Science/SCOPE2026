# Scientific review: cherry-biased pruning and PDA Sackin covariance

## Correctness — PASS

The proof is finite combinatorial for each tree size and then asymptotic by a standard central-binomial estimate. The key bijection contracts a specified pair of sibling leaves into a uniquely labeled surrogate leaf, with the exact depth change \(d+2\). Its size-biased counting prefactor is \(n(n-1)/(2(2n-3))\), including the boundary cases \(n=2,3\). The mean Sackin formula follows from an explicit Catalan generating-function recurrence, and the covariance sign follows from a strict rational ratio inequality for all \(n\ge3\). Exact finite checks compare two enumeration conventions and all distributions in the sample ranges, but are not substituted for the proof.

## Originality — PASS, with residual historical-priority risk

The closest statements are Mir–Rosselló's marginal PDA Sackin expectation (arXiv:1201.3884), McKenzie–Steel's marginal cherry laws (Mathematical Biosciences 164, 2000), Wu–Choi's *cherry/pitchfork* joint laws (arXiv:1508.03139), and Janson's fringe-count results (arXiv:1312.1211). The inspected relevant parts give neither the marked-cherry size-biased Sackin distribution nor the exact mixed cherry/Sackin covariance. In particular, the latter is not a cherry/pitchfork specialization, and the former includes a global path-length functional outside the local-fringe limit-law statements. General pruning ideas could conceivably have appeared elsewhere; searches do not establish global priority.

## Mathematical value — PASS

Cherries and Sackin's index measure complementary, widely used local and global features of phylogenetic balance under a standard sampling null model. Their exact cross-moment was not supplied by the separately known marginal means. The distributional transfer works for every test function, and its special case determines the sign for **every** admissible size, both exact zero boundaries and the natural \(n^{3/2}\) mixed-covariance scale. This is a concrete structural relation useful for assessing dependence between established summary statistics rather than a manufactured parameter slice. No joint limit theorem or test-performance benefit is claimed.

## Sources and remaining risks

Primary comparisons: arXiv:1201.3884 (Sackin mean), arXiv:1508.03139 (cherry/pitchfork joint law), arXiv:1312.1211 (conditioned-tree fringe functionals), McKenzie–Steel (2000), and Blum–François–Janson (2006). Rogers (1996) was available through its abstract, which concerns correlations among Colless, Rogers's imbalance, and Sackin indices, not cherries. The older literature may contain an uncatalogued equivalent identity; the full Rogers text was not inspected. The statement applies to PDA rooted binary leaf-labeled trees only.

Self-review: passed. Independent audit: not yet performed.
