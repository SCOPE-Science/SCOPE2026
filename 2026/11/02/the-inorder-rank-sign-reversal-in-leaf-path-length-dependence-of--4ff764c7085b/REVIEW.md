# Scientific review

## Correctness — PASS
The uniform-priority Cartesian-tree representation correctly characterizes leaves as strict local maxima and root–descendant pairs by endpoint interval minima. Conditioning on a leaf event yields two elementary beta-polynomial neighbor densities, and all potentially affected intervals are exhausted by their intersection with the local three-key neighborhood. The one-sided finite sums telescope, giving the full finite-size rank profile, exceptional small sizes, phase signs, and global covariance. A direct permutation enumerator through eight keys, a separate root-split mixed-moment recurrence through 120 keys, and exact finite identities check critical computations without being substituted for the proof. Limit: this is only for unbalanced uniform BSTs, no ties.

## Originality — PASS (historical-priority uncertainty)
The exact statement is the covariance of an *inorder-key-specific leaf indicator* with *total internal path length*, including the unexpected positive-only-at-near-endpoints sign reversal. In Bóna–Pittel 2014, the term rank denotes distance to leaves, not key order. In Chern–Fuchs–Hwang–Neininger 2016, the closely related mixed analysis is global and asymptotic, and does not give the exact position profile or sign boundaries in the inspected material. Neininger–Straub 2020 concerns joint node-type counts rather than total path length. Published research-record searches for equivalent rank-specific covariance, conditional priority-time formulations, and global coverage found no implication of this precise statement. Some relevant full-text sections and historical specialized work remain a residual risk; a search failure does not establish historical uniqueness.

## Mathematical value — PASS
A locally determined leaf event can correlate in *opposite directions* with global insertion cost at neighboring inorder ranks. The sharp phase separation, exact all-size profile, and recovery of a nontrivial global dependence law provide useful structural joint information for unbalanced BST analysis and distinguish boundary effects from bulk behavior. The statement is not merely an elementary renaming of a known marginal expectation or a routine finite evaluation.

## Closest prior research and limits
See the sources and comparison in `RESULT.md`. The strongest overlap concern is the general joint subtree-count/path-length framework of Chern et al.; the new localized position-dependent sign law is not an immediate stated corollary of its inspected global results. The result is analytical and exact under uniform-permutation insertion but does not claim new algorithms, tail laws, or universality across other tree models.

Self-review: passed. Independent audit: not yet performed.
