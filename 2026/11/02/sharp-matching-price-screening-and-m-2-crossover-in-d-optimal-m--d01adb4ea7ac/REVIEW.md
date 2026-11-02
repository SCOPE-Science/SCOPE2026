# Scientific review: priced Möbius-ladder weighted spanning-tree design

## Correctness — PASS

The weighted matrix-tree theorem gives a positive-definite reduced Laplacian on every connected support. Injectivity of edge conductances into this matrix, plus strict matrix-logdet concavity, proves a unique global optimizer and justifies edge-orbit symmetry without imposing it. A Fourier decomposition separately treats even and odd modes, including the low-order check, with the claimed theorem beginning at \(m=4\), and gives exactly \(m a^{2m-1}[T_m(1+b/a)+1]\). Differentiation along the budget segment gives the threshold \(q_c=m^2/(2m-1)\), equality is handled by strict concavity, and the two limits follow by proved derivative brackets. The standard-library verifier independently checks exact determinants and finite asymmetric feasible perturbations (815 assertions). It cannot certify the infinite claim by enumeration and is not presented as doing so.

## Originality — PASS on inspected evidence, with residual risk

The excluded small graphs \(m=2,3\) are already subsumed by prior priced complete-graph and complete-bipartite results; the new all-size range begins at \(m=4\). The nearest primary literature is Jakobson–Rivin's general optimal valuation and effective-resistance characterization (arXiv:math/9907050 and math/0001169). Those papers explicitly mention the eight-vertex Möbius graph but do not establish the all-size two-price threshold, complete price-indexed optimizer, or singular asymptotic crossover. Tzeng–Wu (cond-mat/0001408) treat differently constructed nonorientable lattice generating functions. Khosoussi et al. (arXiv:1604.01116) study general weighted spanning-tree edge-selection algorithms rather than this exact continuous allocation law. Known Möbius-ladder tree numbers, including OEIS A020871, cover only the unweighted specialization of the product identity. Comparison with existing weighted-ladder edge-kernel results does not show the same optimization claim. Search absence is not a novelty certificate; a specialist equivalent not indexed or not accessible remains possible.

## Mathematical value — PASS

The object is a classical cubic network with two economically distinct edge orbits, and the natural invariant is the weighted spanning-tree determinant used in D-optimal network design. The exact price cutoff grows as approximately half the number of antipodal pairs, unlike constant cutoffs in other families. More significantly, a price of order one maintains a positive asymptotic rung-to-rim ratio, whereas price of order network size forces a nontrivial \(m^{-2}\) boundary profile governed by a hyperbolic level-set equation. This is a structural allocation phase transition, not merely a reformulation of the generic matrix-tree or KKT conditions.

## Closest literature and limits

The earliest focal source is Jakobson–Rivin, first publicly posted 1999-07-08. Distinct later sources are listed in RESULT.md. The theorem does not address independently heterogeneous edge prices, topology changes beyond the specified matching, or operational reliability probabilities. Independent priority and proof validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
