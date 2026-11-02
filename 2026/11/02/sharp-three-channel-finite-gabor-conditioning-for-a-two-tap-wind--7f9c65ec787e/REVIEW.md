# Self-review — sharp three-channel finite Gabor conditioning

## Correctness — PASS

For each integer \(N\ge4\), generator spacing \(s\), and three distinct modulations, the normalized Fourier calculation gives the exact \(N\) frame eigenvalues in RESULT.md. Their minimum is positive. The exact trace-square identity reduces frame potential to the sum of three roots, while the condition-number proof needs the additional strict gap \(\rho_N^{(2)}>4\rho_N/3\). The proof shows this with an integer log-cosine smoothing argument and elementary angle estimates, handling the low orders \(4,5,8\) explicitly; it then compares the optimal balanced ratio against every nonbalanced triple using sampled-cosine extrema. Both asymptotic constants follow by first-order trigonometric expansions. The standalone `CHECK.py` exhaustive enumeration for \(4\le N\le40\) and direct frame-operator construction for \(4\le N\le11\) succeeded (102701 assertions). Those tests supplement the analytic proof and are not substituted for its universal steps.

## Originality — PASS relative to inspected sources

Asipchuk--De Carli--Rodriguez, arXiv:2605.16139v2 (read in full), supply the diagonalization theorem for all translations but no global sharp optimization over precisely three modulation frequencies. The complete published RESULT.md of *Sharp Riesz conditioning for consecutive triples on finite cycles* was inspected: it optimizes a different \(3\times3\) restricted Fourier Gram matrix, and its balancing conclusion does not imply the present \(N\times N\) Gabor condition-number formula. *Prime-field simplex tight sampling has a unique ternary optimizer orbit* (full published RESULT.md inspected) studies a four-point restriction over a different group. Several further published-finding corpus queries covered cyclic Gabor frames, two-tap designs, near-equilateral root sets, frame conditioning, and possible equivalent formulas, including tomography and local spectrogram Jacobian results. Root-of-unity sum minimization and structural diagonalization are credited and not claimed as new. The conclusion is relative to inspected evidence, not proof of absolute novelty.

## Value — PASS

The problem selects the best frame stability among all minimal nontrivial three-modulation-channel designs for a normalized two-tap window. Its exact optimal spectral ratio, every minimizing choice, sharp tightness divisibility criterion, explicit potential defect, and \(1/N\)-conditioning asymptotic are natural structural and reconstruction-quality invariants. This is not merely a frame existence test or an arbitrary small numerical example.

## Limitations and residual risks

The theorem requires a generating two-tap separation, equal tap magnitudes, all translations and exactly three distinct equally weighted modulations. The comparison to the classical 2000 Gabor article was bibliographic rather than complete full-text inspection. An older unindexed or inaccessible equivalent three-channel optimization may exist. The root-of-unity fact is classical. Exact finite tests do not establish infinite claims, which rely on the provided proof. Independent mathematical audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
