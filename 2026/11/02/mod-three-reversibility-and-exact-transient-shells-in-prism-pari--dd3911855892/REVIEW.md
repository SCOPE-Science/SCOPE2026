# Mathematical review

## Correctness — PASS

The exact update is the block matrix with cyclic adjacency \(A=z+z^{-1}\). Conjugation in characteristic two gives a double Jordan block with diagonal \(B=1+A=z^{-1}(z^2+z+1)\). This proves the mod-three invertibility criterion. The square-free odd component and its power-of-two multiplicity give a canonical primary/complementary decomposition. The primary block's even-power identity and odd-power local Smith factors establish the complete cumulative first-entry sizes, including the exceptional odd-multiple-of-three case. The independent dyadic computation of kernels of \(F^{2^j}-I\) proves all primitive orbit counts, with direct enumeration used solely to catch implementation or boundary mistakes.

## Originality — PASS (qualified)

The nearest accessible literature addresses general additive automata, periodicity, and point-count methods rather than the specified two-ring rung-coupled system. Ward (2000), Cordovil et al. (1986), Boyle–Lee (2007), and Dennunzio et al. (2012) are individually compared in AUDIT.json. Search comparisons also cover published parity-automaton results for distance-two Boolean cubes and complete multipartite graphs, which do not imply the prism formula under a graph isomorphism or restriction. The unavailable full text of Chin–Cortzen–Goldman (2001) and unindexed equivalent formulas are genuine residual historical risks. The argument does not claim the known polynomial-algebra methods themselves are novel.

## Mathematical value — PASS

The arithmetic criterion \(3\mid n\) separates complete reversibility from irreversible finite-state convergence. In the singular case, exact populations reveal \(16\)-fold successive transient shells and a sharp \(2\)-adic stopping threshold. For dyadic lengths, adding one rung per site converts two eventually zero systems into a bijection supporting maximal periods, with exact primitive-orbit counts. These finite-size and all-size structural invariants are natural diagnostics for the effect of coupling on cellular-automaton dynamics, not arbitrary chosen data points.

## Limits and validation status

Only the claimed graph family and rule are covered. Originality is subject to historical-access limitations; no independent mathematical audit is asserted. All displayed counts have direct algebraic derivations and accompanying reproducible finite checks.

Self-review: passed. Independent audit: not yet performed.
