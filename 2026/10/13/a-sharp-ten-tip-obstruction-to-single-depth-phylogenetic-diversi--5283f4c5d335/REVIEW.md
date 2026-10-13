# Self-review

## Correctness — PASS

The proved assertion has a finite, explicit domain: rooted nonplane fully binary trees with unit edges and at most ten leaves. The polynomial recurrence counts every selected-tip subset exactly; attaching each child edge contributes one precisely when that child is selected. Root-size ordering and recursive child indices generate each tree shape once. The included checker enumerates 192 shapes and their 131,726 tip subsets, compares an independent direct branch-union algorithm against the polynomial for every shape, and tests all required injectivity and collision-set intersections. The two displayed witness shapes have distinct root partitions yet exactly the same two-tip law. These are exhaustive integer certificates for the stated finite limit, not support for an infinite statement.

## Originality — PASS, with documented risk

Pachter and Speyer's full arXiv preprint treats individually indexed subtree-weight maps and requires tip identities; removing those identities can destroy their reconstruction argument. Faller, Pardi and Steel's inspected complete-text Sections 2 and 4 derive forward rooted-PD distributions on known trees under random extinction, not inverse identification of unlabeled unit-edge shapes. Nipperess and Matsen examine rarefaction means and variances rather than the complete distribution. Searches for rooted-PD distribution inverse reconstruction, pairwise histogram tree-shape ambiguity, subtree weights, and exact ten-tip identification did not reveal the same all-shape depth-design classification. Public-index search hits on zero forcing, spectral tree classification and graph phylogenetic rank use different invariants and do not imply this theorem. Residual risk: an unindexed or differently titled homometric-tree or polynomial census might cover the enumeration; no universal novelty guarantee is inferred from negative searches.

## Value — PASS

The natural idealized experiment randomly selects a fixed number of taxa and records only total rooted phylogenetic diversity rather than taxon identities. The sharp ten-tip obstruction and exact nine minimal depth pairs quantify when that coarsened information fails and exactly how a second depth resolves the first ambiguity. The finite result is a motivated identifiability boundary and sampling-design classification, not an arbitrary slice of a larger tabulation. It makes no claims about finite-replicate efficiency, natural branch lengths, or practical experimental feasibility.

## Scope and independent status

The finite checker is supplied in full and was run on the packaged code. Independent external review remains outstanding. Literature coverage is limited to accessible and indexed sources; published mathematical work was compared for possible overlap.

Self-review: passed. Independent audit: not yet performed.
