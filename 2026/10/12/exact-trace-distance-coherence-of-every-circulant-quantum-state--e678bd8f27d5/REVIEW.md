# Self-review

## Correctness

PASS. For every diagonal density matrix, averaging over cyclic shifts gives exactly the maximally mixed diagonal state. Because every circulant density matrix is fixed by that action, convexity and unitary invariance of the trace norm prove the global lower bound against every incoherent competitor. Fourier diagonalization gives the exact eigenvalue deviations and therefore the exact trace norm. No enumeration, asymptotic approximation, or numerical certificate is needed.

## Originality

PASS. The closest primary papers were compared at statement and implication level. arXiv:1410.8327 treats special qutrit classes rather than all circulant states. arXiv:1511.01854 covers qubits, \(X\)-states, pure states, and general semidefinite optimization but does not state the Fourier-spectrum formula. arXiv:1610.07330 assumes one common real off-diagonal entry, which is narrower and structurally different from general complex circulant matrices. arXiv:2109.05552 studies trace-norm Birkhoff–James orthogonality and modified trace-distance resource quantities; its unrestricted-diagonal condition does not imply this optimization over the trace-one incoherent simplex. Focused searches for Fourier-diagonal, circulant, cyclic-shift, and closest-incoherent formulations found no covering theorem. The remaining risk is an equivalent later group-symmetry lemma phrased outside coherence terminology.

## Value

PASS. Circulant states form a natural \((d-1)\)-dimensional simplex in every dimension, not an arbitrary low-dimensional slice. The theorem turns a quantum state-space optimization into an exact classical total-variation invariant and supplies a phase-sensitive closed qutrit formula beyond the single-edge and equal-real-off-diagonal classes emphasized in early work. It is a structural exact classification for a natural symmetry family.

## Closest literature and limitations

The result does not address arbitrary states, strong monotonicity, or uniqueness of the closest incoherent state. The strongest residual originality risk is a general symmetry-reduction theorem whose cyclic trace-norm specialization was not indexed under the searched coherence/circulant terminology.

Self-review: passed. Independent audit: not yet performed.
