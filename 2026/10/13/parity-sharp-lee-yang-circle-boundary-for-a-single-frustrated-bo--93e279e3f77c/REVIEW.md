# Scientific assessment of the sharp single-defect Ising-ring Lee–Yang boundary

## Correctness: PASS

The finite-spin partition function and fugacity normalization are explicit. Cayley–Hamilton yields a degree-\(n\) Chebyshev polynomial with defect parameter \(\lambda=(e^{-2(K+L)}-1)/(1-e^{-4K})\). For \(\lambda\le0\), a symmetric Jacobi realization and a boundary-sign exclusion force every polynomial root to remain in the physical real interval. For positive parameter, an imaginary-axis sign argument establishes failure on even cycles; Chebyshev interlacing proves the additional allowed interval \(0<\lambda\le1/(n-1)\) for odd cycles and the failure beyond it. The origin multiplicities are checked from exact coefficients. Explicit-spin numerical tests and independent transfer identities agree, but are corroboration rather than infinite proof.

## Originality: PASS, subject to independent priority verification

The 1952 ferromagnetic circle theorem does not cover a negative edge. Matveev--Shrock (1995) study uniform complex-coupling Ising zeros, not this mixed-sign finite-ring sharp criterion. Peters--Regts (2018) and Bencs et al. (2019) concern uniformly signed edge weights and do not give this threshold. Closest: Tonchev--Dantchev (2026), Theorem 1, Eq. (23), supplies the same transfer-matrix/Chebyshev partition polynomial for a defective ring. That formula is explicitly credited, not claimed new. Their discussion treats real magnetic field, partition functions and magnetizations rather than a necessary-and-sufficient confinement of all complex-field zeros; the interlacing and parity thresholds are additional analytical conclusions. Residual risk: an equivalent root-location analysis may exist in the broader Ising-defect literature, including works not retrieved.

## Value: PASS

The Lee--Yang circle property is a natural global zero-geometry invariant with thermodynamic and analytic meaning. The result locates the precise strength at which a single frustrating edge invalidates the circle theorem and exhibits a nontrivial finite-size parity distinction, proving both admissibility and failure with exact collision multiplicities. It is a complete classification for every cycle length and coupling, not an arbitrary sample or a mere restatement of a partition function.

## Limitations and verification

The proof addresses a single defect on a finite cycle, with strictly ferromagnetic remaining bonds; it does not classify multiple defects or individual zero angles. The accompanying NumPy verifier checks 135 numerical zero-locus instances, 135 transfer-identity evaluations and 27 boundary-multiplicity parameter pairs. Independent auditing and complete bibliographical priority search remain unperformed.

Self-review: passed. Independent audit: not yet performed.
