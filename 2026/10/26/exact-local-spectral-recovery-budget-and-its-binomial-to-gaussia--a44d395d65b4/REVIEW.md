# Scientific review: exact local spectral-recovery budget

## Correctness — PASS
The matrix-unit superoperator is triangular under total excitation number, giving the complete algebraic spectrum. The first damping-only population class has gradient \((1,0)\), while the first dephasing-bearing coherence class has gradient \((1/2,2)\). Counting population multiplicities before that first coherence proves both necessity and local sufficiency of the claimed exact prefix lengths. The compact-rate maximum is a finite binomial identity; the moving-ratio limit follows from the binomial central limit theorem. Exact-rational enumerations, independent direct Lindbladian diagonalizations, and finite-size asymptotic diagnostics corroborate the proof.

## Originality — PASS (best knowledge, not independent certification)
Ji–Chakraborty, arXiv:2608.29302v1, supply the spectrum and discuss two extreme non-identification regimes; these portions are prior knowledge. The new statement gives the fully resolved generic rate-ratio staircase, the **necessary and sufficient local** prefix budget, a nontrivial degree-20 maximal-budget cutoff for the original positive rate box, and its Gaussian large-array scaling. Torres, arXiv:1403.3686v2, supplies a general eigensystem method, not this sorted-inverse-prefix classification. Neither directly inspected work states these joint conclusions. Additional broad Liouvillian inverse-problem theory might imply some statements; global priority has not been proved.

## Mathematical value — PASS
The full phase diagram replaces two coarse extreme-regime statements by the exact first point at which decay-only spectral measurements distinguish damping and dephasing *locally*. The finite-rate design region unexpectedly changes from an exponentially large to a polynomial spectral observation budget; the Gaussian window quantifies the crossover when the dissipation ratio itself scales with system size. This is a structural and operational threshold, not a trivial finite enumeration, though it does not address inference under noise.

## Closest sources and residual risks
Y. Ji and S. Chakraborty, *A Spectral Identifiability Threshold for Dissipative Rate Recovery from Truncated Liouvillian Spectra* (2026), arXiv:2608.29302v1, provides the spectral model and previously known limiting cases. J. M. Torres, *Closed form solution of Lindblad master equations without gain* (2014), arXiv:1403.3686v2, is an earlier general spectral framework. Uninspected work could have an equivalent binomial-budget corollary, and eigenvalue ties, unknown multiplicities, noisy data and non-diagonal couplings require separate analysis.

Self-review: passed. Independent audit: not yet performed.
