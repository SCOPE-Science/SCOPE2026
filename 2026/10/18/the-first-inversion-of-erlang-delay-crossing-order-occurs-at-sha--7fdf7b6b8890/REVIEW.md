# Review

## Correctness — PASS
The finite-dimensional Erlang linear-chain characteristic polynomial follows directly from the mean-preserving transform. The imaginary-axis condition and transversality derivative are reconstructed in RESULT.md, including all quantifiers and the \(\tau>0\) boundary. The finite but exhaustive order-minimality argument is backed by the exact rational certificate `interval_certificate.py`, which checks all 66 earlier even-index comparisons, the first possible inversion, and the stated complete order at the illustrative ratio. `spectral_check.py` independently confirms selected unstable counts, without purporting to prove all cases.

## Originality — PASS, with risks
The nearest exact family is Bîrdac et al. (2026), which establishes the base characteristic equation, generic phase-root condition, and Gamma shapes one/two plus Dirac results. The present result does not repackage that reduction: it proves a **sharp first Erlang shape for reversal of chronological crossing order**, an explicit threshold, and a new unstable-pair-count chronology. Zhang–Stépán (2019) cover discrete-delay force feedback; an all-order Gamma-memory study of a cognitive-map PDE has a distinct characteristic factorization, though only its indexed summary was examined. General theory may contain indirect implications, and nonaccess to some full papers prevents a conclusive historical priority assertion.

## Value — PASS
Ordering thresholds determines actual stability windows. A concrete first loss of chronological phase-index order at a natural minimal integer shape gives testable, exact predictions: two destabilizing pairs before an intervening restoring crossing and an equality boundary carrying two different imaginary frequencies. This behavior is invisible in low-order Gamma comparisons and cannot be inferred from phase crossing parity alone.

## Scientific limitations
The conclusions concern linear spectra for \(a>b>0\) and Erlang integer shape, not nonlinear branch existence, nonlinear Hopf type, arbitrary delay densities, or comprehensive priority certification. Finite eigenvalue diagnostics supplement the analytic and exact-integer-interval reasoning.

Self-review: passed. Independent audit: not yet performed.
