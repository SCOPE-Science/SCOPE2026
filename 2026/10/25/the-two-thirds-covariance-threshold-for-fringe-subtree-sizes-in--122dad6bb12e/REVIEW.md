# Self-review: root-imbalance/fringe-size covariance spectrum

## Correctness — PASS

The claimed finite-size formula is proved from the uniform root split, the exact fringe-count mean recurrence, and three explicitly evaluated boundary-defect moments. The covariance computation retains the potentially overlapping boundary regimes and the full quantifier range \(n\ge2\), \(1\le k<n\). Every sign follows from \(3k+1-2n\). The deterministic \(k=n\) endpoint is correctly excluded. Exact-rational execution of `verify.py` checked each insertion permutation through eight keys, and all finite sum rules through two hundred keys. The all-size conclusion is analytical, not extrapolated from those tests.

## Originality — PASS on inspected evidence

The closest prior scientific statements are Dennert and Grübel's 2010 exact marginal means, first-split conditional decomposition, and pairwise **fringe-count/fringe-count** covariance; Holmgren and Janson's 2014/2015 broad fringe additive-functional and count-count results; and the published random-BST root-imbalance/**total path length** covariance. The last scalar identity is exactly a weighted sum of this new signed spectrum and does not recover the separate components. The 2020 random binary-fringe-collection paper supplies contextual motivation rather than a claim of earlier ownership of the classical mean. Searches and full-text inspections located no prior explicit all-k formula or exact \(2/3\)-scale sign classification. Since the underlying conditional recursions are old, historical priority remains uncertain.

## Value — PASS

A complete and unexpectedly sign-changing cross-covariance profile distinguishes contributions of small fringe subtrees from those of large ones to root-level structural imbalance. The result settles every size and tree order with one elementary exact law and explains the already-known positive aggregate dependence on total path length. This is a natural complete classification of the BST subtree-size profile against root-split balance, rather than a numerical slice or a marginal recomputation.

## Closest literature and limits

Dennert and Grübel, *On the Subtree Size Profile of Binary Search Trees* (2010), DOI 10.1017/S0963548309990630, equations (2.1), (3.3), Proposition 2.1. Holmgren and Janson, arXiv:1406.6883, Theorem 1.12 and Lemma 3.3. Seelbach Benkner and Wagner, arXiv:2003.03323, Sections 1 and 4. Published record *Squared root imbalance has an exact cubic covariance with random-BST path length* in published-finding corpus, 2026/10/4. These establish familiar building blocks and the aggregate covariance, but none was found to state the signed size-resolved result. The theorem does not claim stochastic dominance, generalize to alternative insertion laws, or certify worldwide historical novelty.

Self-review: passed. Independent audit: not yet performed.
