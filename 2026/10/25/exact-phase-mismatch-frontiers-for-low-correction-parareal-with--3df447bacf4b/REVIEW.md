# Review: exact phase-mismatch frontiers for low-correction Parareal

## Correctness — PASS

The completed-block Parareal recurrence has the exact binomial polynomial displayed in `RESULT.md`. Commuting unitary propagators are jointly unitarily diagonalizable, so it suffices to test the scalar relative eigenphases. A symbolic calculation in `verify.py` confirms the four **free-\(N\)** polynomial identities for the squared norm defect. Their signed factors, the \(N\ge k+1\) domain and \(\Delta^2=2\max u\) give necessity, sufficiency, dimension-one attainability and the phase-window scalings. The 1,020 symbolic, recurrence and matrix assertions pass. Finite sampling is supplementary, not a proof of all-window validity.

## Originality — PASS, qualified

Staff and Rønquist already derive the exact general Parareal binomial endpoint polynomial; that formula is not claimed as new. Ruprecht analyzes phase mismatch and wave instability; Buvoli and Minion plot non-diffusive stability regions; Ariel, Nguyen and Tsai derive weighted-iteration error bounds; Rosemeier, Haut and Wingate study averaged multilevel methods. Reading their relevant original statements found no k=1 through 4 sharp unitary-terminal-norm classification or threshold comparison. The new contribution is the explicit all-\(N\) factorization and first nonzero stability window at correction count three, enlarged at four. A previously published specialized factorization or stronger equivalence may exist, and this cannot be excluded by database searching alone.

## Mathematical value — PASS

The result supplies sharp quantitative phase mismatch limits for energy-preserving time-parallel propagation with given window count and correction budget; the first two corrections are *always* expansive for mismatched phases while three may be nonexpansive. The \(N=5\) example proves a genuine reversal across correction counts at the same propagators. The exact tolerance scales as \(N^{-1}\) in phase, a useful nontrivial restriction in oscillatory simulations.

## Scope and remaining uncertainty

The theorem applies to the Euclidean norm of the **completed** block with commuting unitary fine/coarse maps. It does not bound all intermediate sweeps, establish solution accuracy/speedup, or extend to noncommuting, dissipative or nonnormal propagators. The bibliographic comparison is substantive but not an independent comprehensive publication-priority certification.

Self-review: passed. Independent audit: not yet performed.
