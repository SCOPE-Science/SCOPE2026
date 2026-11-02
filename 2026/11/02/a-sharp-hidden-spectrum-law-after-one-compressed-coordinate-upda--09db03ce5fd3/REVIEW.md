# Scientific assessment

## Correctness — PASS

The claim is proved for a specified symmetric block family, exact reference initialization, exact one-coordinate line minimization, and the newly untouched-entry cutoff. The line derivative is a strictly increasing cubic with root \(s\). The compressed vector exactly cancels the active cubic gradient while the full gradient on excluded coordinates is \(4s v\). A Schur complement gives the **exact** full-space secular equation. The Loewner lower bound on \(D\), the entrywise cutoff, and strict monotonicity of \(\Phi\) give the sharp ground-energy frontier; saturation is attained with \(D=\gamma I\) and equal-magnitude entries. A normalized collective leaf mode establishes the constant-norm, vanishing-cutoff sequence. The standalone verifier passed four algebraic identities, 1,050 random block-matrix sharpness/inequality cases and six sequence dimensions. Computations support rather than prove all-dimensional statements.

## Originality — PASS, subject to priority limits

The closest source is Li and Wu (2026), arXiv:2607.24319v1, which analyzes CDFCI with compression, including an \(O(\tau^2)\) result conditional on eigenvector decay. Wang, Li and Lu (2019), arXiv:1902.04592, supply the exact initial \(c=e_0\), \(b=He_0\), greedy neighbor selection and drop-on-untouched-entries rule. The 2025 multicoordinate extension also describes this active/untouched distinction. None of the inspected material states the present fully reachable **one-update** false-stationarity mechanism with its sharp \(m\tau^2\) energy frontier. The published constrained-eigenvalue zero-residual example in published-finding corpus (SCOPE-projected-eigenpair-certification-false-positive) instead has a true zero residual at the wrong spectral index. The published SM3 cover-transversal contamination example pertains to accumulated adaptive gradient statistics, not truncated Hamiltonian products. Schur-complement estimates are classical and are not claimed new in isolation. A specialist graph-star spectral estimate may cover the scalar equation, and not all historical literature is accessible; the claim is made with that priority risk disclosed.

## Value — PASS

The exact dimensional reliability calibration is motivated by a current numerical-eigensolver scheme: entrywise cutoff alone cannot certify full-space stationarity, even after a legitimate exact descent update from the specified initialization. The result identifies the aggregate parameter controlling the worst hidden eigenvalue error, gives a necessary-and-sufficient tolerance budget, and demonstrates a fixed-operator-norm counterexample when the number of discarded contributions increases. This supplies a useful boundary for interpreting decay assumptions in compressed-eigensolver accuracy theorems. It does not imply every practical implementation falsely terminates, nor does it cover molecular-specific sparsity rules.

## Limitations and residual risks

The matrix family is abstract symmetric, the omitted block is bounded below, and the one-step result does not establish multistep stopping. The sharp bound holds only for the displayed two-active-plus-leaves class. Full historical mathematical priority requires further independent scrutiny, especially classical bordered-star secular estimates and specialized eigensolver truncation results.

Self-review: passed. Independent audit: not yet performed.
