# Review of the wheel-metric negative-type classification

## Correctness — PASS

The zero-sum decomposition into rim-zero-mean and hub/rim-radial subspaces is orthogonal and invariant under the powered distance quadratic form. Every Fourier eigenvalue is derived explicitly; the radial eigenvalue is compared by a rigorous positive inequality for all rim lengths. This gives the sharp quotient for all real exponents \(p\ge0\), not only finite samples. The Schoenberg Gram criterion and an exact nullspace multiplicity count give the critical Euclidean ranks. A reproducible standard-library checker passed 10,009 exact-arithmetic and floating-point comparisons; these are supplementary evidence, not an infinite proof.

## Originality — PASS, with residual risk

Primary inspected literature supplies general negative-type interval criteria, matrix methods, or classical cycle-gap formulas but does not state the wheel-specific all-exponent spectral law or the parity-sensitive critical rank. In particular, the cycle path metric computed by Wolf is not the wheel's rim restriction once the hub introduces two-edge shortcuts, and the gap normalizations differ. Sánchez treats complete bipartite examples rather than the wheel cone. Murugan's vertex-transitivity assumption excludes wheels. published-finding corpus searches using wheel/cone/negative-type/Fourier aliases returned graph polytopes, wheel topology, and cycle inequalities rather than the same metric claim. General Fourier diagonalization is acknowledged as standard, and no database absence is treated as proof of novelty.

Residual risk: Full texts of Deza–Maehara (1990) and Buckley–Harary (1988) could not be checked, though the latter uses the different unit-edge Euclidean dimension concept. The former is a plausible source of general reductions that could contain an implicit stronger specialization. The available evidence did not indicate decisive coverage; this assessment is provisional and not an independence claim.

## Mathematical value — PASS

The exact supremal negative type is a natural invariant of finite metric geometry and controls the first exponent at which Hilbert snowflake realization becomes impossible. The wheel is a canonical one-hub extension of a cycle, and the odd/even rim transition gives a structural classification throughout an infinite graph family. The sharp normalized gap also supplies a quantitative stability margin for every exponent, while the critical embedding-rank defect distinguishes two independent degeneracy geometries. No wider graph-family classification or downstream theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
