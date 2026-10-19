# Self-review

## Correctness — PASS

The exact identity follows from conditioning on the first coordinate: both procedures have identical first-step distributions; only the expected second-step decrease differs. The coordinate decrease is \(\omega(2-\omega)r_i^2/2\). A two-term expansion of the updated gradient gives the displayed gap, while the two eigenvalues of its quadratic form give the sharp if-and-only-if threshold and both signs beyond it. Diagonal normalization covers all SPD \(2\times2\) matrices, and invertibility realizes every witness gradient. The standalone exact-rational script checks 5,880 trajectory/formula and normalization identities plus the threshold and explicit witness. Finite checks complement, but do not replace, the complete analytical proof.

## Originality — PASS, with priority risk

The 2018 Gürbüzbalaban–Ozdaglar–Vanli–Wright work compares sampling designs only under exact coordinate minimization; its worst-case and rate theorems do not entail the sharp overrelaxed statewise two-update comparison. Oswald–Zhou (2016) treats relaxed shuffled SOR and gives bounds versus the original ordering, with an independent-sampling bound quoted separately, not the present necessary-and-sufficient paired ordering. Sun–Luo–Ye studies permutation-based rate operators in coordinate descent/ADMM, not the exact overrelaxed two-coordinate objective gap. Published index summaries concerning two-coordinate Gauss–Seidel transient error concern Euclidean norm and coordinate ordering, not this expectation comparison. Alternate older SOR terminology remains a residual priority risk; absence of a located formula is not a uniqueness proof.

## Value — PASS

The threshold \(\omega_*=1+1/\kappa\) gives an exact and sharp safe-relaxation boundary for preferring reshuffling to independent coordinate sampling after the same computational budget. The minimal SPD example disproves a tempting unconditional extrapolation from exact-coordinate descent. Both strict reversal directions occur at fixed matrix and stepsize. The result is narrow but is a complete natural classification, not an arbitrary parameter sweep: it distinguishes sampling-order benefit from overrelaxation effects. It makes no claim about subsequent epochs or practical runtimes.

Self-review: passed. Independent audit: not yet performed.
