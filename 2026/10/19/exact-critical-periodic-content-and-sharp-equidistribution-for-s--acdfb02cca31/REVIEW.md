# Scientific assessment

## Correctness

PASS. The exact finite period bound follows from a cut-counting injection: all noncyclically-admissible length-\(n\) overlap edges cross from nonzero-initial to zero-initial vertices, and each such used edge displaces a distinct unused good crossing edge in a closed trail. The induced good-edge graph is balanced and strongly connected, giving the matching Euler cycle. A recurrence proves the gap is exactly \(r^{n-1}\), not just bounded below. The common-prefix cutoff then gives the exact asymptotic content constant. A symmetric-matrix spectral decomposition proves the claimed cylinder formulas and sharp signed discrepancy. These arguments cover all integer \(q\ge2\), all \(0<r<1\), and all sufficiently large orbit sizes; finite diagnostics do not substitute for them.

## Originality

PASS under checked evidence, subject to residual priority uncertainty. The 2026 source establishes general periodic content, its critical exponent for self-similar full shifts, and existence of de Bruijn extremizers, not the exact star-constrained constant. Restricted de Bruijn theory, including the intersection of substring-avoiding cyclic languages after relabeling the zero symbol as greatest, already implies the Euler universal-cycle existence in this model; that existence is explicitly credited. The additional cut comparison bounds arbitrary closed trails that include noncyclically admissible windows, yielding a matching sharp bound. Previously indexed related findings concern positive content in inhomogeneous similarity codes and different periodic-separation effects, not this exact Markov-constrained content and sharp cylinder discrepancy. Earlier combinatorial work could implicitly imply a part of the finite bound; it remains a priority risk rather than a disproof of the stated mathematical result.

## Value

PASS. Periodic content is a newly motivated metric invariant, for which the exact critical value is more informative than the exponent alone. The natural smallest mixing non-full-shift star family forces an obstruction absent in the full-shift de Bruijn argument: a cyclic orbit can pass through admissible but noncyclically admissible windows. The sharp cut bound determines the extremal orbit size, and the spectral cylinder formula quantifies the limiting distribution in the same extremizers. The result is family-specific, not a general theorem for arbitrary adjacency matrices.

## Remaining limitations

The metric normalization matters, the family is finite-state and symmetric, and numerical checks cover only sample parameters. Source inspection is substantial but not exhaustive; no independent audit or external mathematical certification has been performed.

Self-review: passed. Independent audit: not yet performed.
