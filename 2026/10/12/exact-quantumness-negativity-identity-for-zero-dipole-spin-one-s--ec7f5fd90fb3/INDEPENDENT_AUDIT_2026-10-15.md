# Independent mathematical audit

## correctness

PASS

The full zero-dipole sector has Bloch X=diag(1,T), trace T=1, each eigenvalue at most 1; at most one negative eigenvalue. Antipodal symmetrization strictly removes the dipole of any coherent mixture without changing second moments, and every trace-one PSD 3x3 matrix is realized. The original squared Hilbert-Schmidt distance equals one quarter the squared Frobenius difference, not its square root. For negative eigenvalue λ, T*=T+(λ/2)I-(3λ/2)vvᵀ is rank-two PSD trace-one; stationarity inequality (3λ/2)⟨v,Sv⟩≤0 for all trace-one PSD S proves the unique global projection and Q²=3λ²/8. The three direction/weight construction has mean zero, second moment T*, and its Bloch rank three precludes fewer coherent components. Similarity of the symmetric two-qubit partial transpose with Bloch X/2 gives exactly one possible negative eigenvalue λ/2, hence N=−λ/2 and Q=√(3/2)N. At λ≥0 the state is already classical. The nonaxial rational example has Q²=3/32 and N=1/4, matching the formula. The verifier samples only finite rational states; the variational proof is continuum-wide.

## originality

PASS

The strongest directly relevant Bohnet-Waldraff–Braun–Giraud paper explicitly distinguishes its pure-state closed form from numerically studied mixed states and states mixed-state lower bounds; its partial-transpose similarity (Eq. 60) and classicality criterion do not by themselves evaluate the zero-dipole HS metric projection or its unique rank-two optimizer. The 2017 thesis is cited in the reviewed submission as reporting mixed-state bounds; that thesis was not re-read independently during this run, so its full overlap remains a specific residual risk. Primary-paper comparison of statements/feasible sets found no dominating implication from unrestricted two-qubit separability or axis-diagonal special cases. Best-of-knowledge originality with possible unindexed Bell-triplet simplex reformulation.

## value

PASS

A natural full five-real-dimensional family of unpolarized spin-one/two-photon states has an exact operational distance, equality with scaled entanglement negativity, a unique nearest classical state, and a sharp minimal three-coherent-state realization. This fills the mixed-state optimization gap left by a central primary paper, beyond a mere membership test, without claiming a formula for nonzero spin dipoles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
