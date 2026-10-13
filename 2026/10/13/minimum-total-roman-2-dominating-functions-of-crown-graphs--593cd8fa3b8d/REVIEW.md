# Review of Minimum total Roman {2}-dominating functions of crown graphs

## Correctness
PASS. Weight below \(4\) forces one side to have total weight \(1\), making the opposite side impossible. At weight \(4\), side weights are \(2\) and \(2\). The zero-defense inequalities force matched zero coordinates on the two sides, so the positive supports coincide; totality excludes one-index support, leaving exactly two common indices labeled \(1\). Exhaustive verification of all \(597{,}861\) ternary labelings for \(2\le n\le6\) agrees with the complete classification.

## Originality
PASS. The 2019 introducing paper was inspected in full searchable text and visually at the defining page; it contains no crown or matching occurrence. Its value-\(3\) characterization can support the scalar lower bound but does not enumerate crown optimum functions. The independent full-text study also contains no crown or matching occurrence. A 2024 survey does not report a crown result. Exact and semantic literature searches found no equivalent theorem. The nearest published results concern complete multipartite graphs or different Roman/domination variants and do not imply the deleted-matching support synchronization.

## Value
PASS. The target parameter is NP-hard even on bipartite graphs, so exact structured bipartite benchmarks are mathematically motivated. Crown graphs are the canonical perfect-matching deletion of balanced complete bipartite graphs. The theorem gives every optimum function and the exact multiplicity \(\binom n2\), not merely a scalar value.

Self-review: passed. Independent audit: not yet performed.
