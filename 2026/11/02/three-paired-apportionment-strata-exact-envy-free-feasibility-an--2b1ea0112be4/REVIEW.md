# Scientific review

## Correctness: PASS

The universe is six parties in three distinct integer-floor pairs with strictly ordered within-pair fractional residues, and exactly three surplus seats. The 20 admissible three-up-rounding binary words contain precisely seven without inversion. Their seven masses reduce to one all-singleton mass \(z=1-S\) and the six off-diagonal transportation variables \(x_{ij}\). The row margins are \(\ell_i\) and the column margins are \(1-h_i\), both of total \(S\). Bipartite Hall conditions reduce exactly to three singleton cuts; subsets of at least two rows reach every column. The resulting inequalities and nonnegative \(z\) are both necessary and sufficient. A cycle adjustment gives at most five positive off-diagonal outcomes. The rational standard-quota instance in RESULT.md forces at least five such outcomes plus \(z>0\), proving the support-six lower bound. The all-real claim follows analytically; exact finite checks are corroborative only.

## Originality: PASS, with residual priority risk

La Commare, Tucker-Foltz and Verdugo, *Envy-Free Randomized Apportionment* (arXiv:2610.24217v1, 2026), already provide the much more general linear-programming feasibility framework for zero envy. The present structural specialization is not a claim of a new general decision procedure or of a novel max-flow theorem. Its substantive increment is the closed form of the full feasibility chamber in the natural six-party, three-distinct-floor-pair, three-surplus-seat family, combined with an explicitly sharp minimum lottery-support witness. The generic support upper bound alone is also compatible with standard convexity arguments; the exact forcing instance is the distinctive support claim. Searches and inspected source material did not reveal this combined statement, though the full possible earlier literature is not exhausted. Related cardinality-constrained randomized rounding results are background, not a priority claim.

## Mathematical value: PASS

A natural configuration with three coupled two-party equal-floor blocks and three surplus seats has a small but nontrivial polytope of realizations. Its feasibility is captured by four transparent inequalities, its symmetric branch has the exact break point \(p=2/3\), and the minimum lottery size can genuinely be six. These facts refine the general feasibility algorithm into usable quota checks and demonstrate a natural lower bound on the number of seat-allocation outcomes needed to implement exactly proportional, zero-envy rounding. No generalization beyond the stated domain is claimed.

## Closest literature and limitations

The closest primary work is La Commare, Tucker-Foltz and Verdugo, *Envy-Free Randomized Apportionment*, https://arxiv.org/abs/2610.24217. Its general LP covers the decision problem abstractly; this result states a small-dimensional explicit classification and a sharp realization-complexity boundary. Doerr and Wahlström, *Randomized Rounding in the Presence of a Cardinality Constraint*, DOI:10.1137/1.9781611972894.16, is more general fixed-cardinality rounding background; only abstract-level material was accessible. A previously unstated corollary of either manuscript or earlier transportation-polytope work remains possible. Literal no-envy at tied residues is excluded from the theorem. Independent priority or proof audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
