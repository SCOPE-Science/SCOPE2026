# Mathematical review

## Correctness — PASS

**Claim tested:** the globally minimal second-largest eigenvalue modulus over all reversible nearest-neighbor plus holding kernels on a \(2m\)-cycle with stationary masses alternating in ratio \(0<r\le1\), and the exact if-and-only-if condition for simple symmetric-proposal Metropolis--Hastings to attain that minimum. The proof verifies the stationary-flow feasible cone, global convexity of the centered symmetric norm, preservation of the target masses under the edge-transitive subgroup, and exact Bloch eigenvalues for all \(m\ge2\). The minimum and maximum nonzero Fourier rates are attained. The resulting constrained scalar minimax is solved exactly, with the radical-boundary conjugate positive for the whole domain. Both threshold-side formulas agree at equality. The finite tests, including 4,585 diagonalization/flow checks and 25 unrestricted numerical optimizations, are supplementary and do not substitute for the complete proof.

## Originality — PASS on inspected sources, with residual risk

Boyd--Diaconis--Xiao (2004) give the general FMMC SDP, including prescribed stationary distributions, and Boyd--Diaconis--Parrilo--Xiao (2007) give symmetry reduction and a **uniform-stationary** cycle formula. Both are credited, not presented as discoveries. In the latter the symmetric kernel assumption imposes uniform stationary masses, so its known \(r=1\) result does not imply the new two-mass criterion for \(r<1\). The full-text 2005 symmetry manuscript and 2010 symmetric cyclic multipartite study supply methodological background but not an identical statement. A previous exact alternating-*edge-price* combinatorial-Laplacian spectral gap problem has a different stationary normalization and a different eigenvalue objective. Relevant indexed search and prior research records comparisons are recorded in `AUDIT.json`. No novelty claim is based merely on a failed text search; specialist overlap remains possible.

## Value — PASS

The theorem gives a natural complete answer to when a standard Metropolis--Hastings walk is not merely feasible but truly fastest in the SLEM sense for a nonuniform structured stationary target. It identifies a sharp mass-ratio transition, an explicit optimal lazy alternative when the heuristic fails, and a concrete long-cycle asymptotic. These are usable kernel-selection and spectral-gap diagnostics rather than an unmotivated small-case table.

## Scope and residual limitations

The objective is spectral modulus, not every finite-time mixing measure. The Markov chain is reversible with fixed alternating stationary masses and can use only nearest-neighbor edges plus self-loops. Numerical tests are finite and cannot prove universal results. No uniqueness of all nonsymmetric minimizers is established, and the historical literature may contain another formulation. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
