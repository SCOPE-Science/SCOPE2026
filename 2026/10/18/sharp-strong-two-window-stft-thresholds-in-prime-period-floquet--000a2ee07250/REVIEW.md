# Independent mathematical audit

## correctness

PASS

For exponential band window with m<p≤N/2, its STFT ambiguity is nonzero exactly on cyclic lags |a|≤m, so magnitudes recover phase products along those support edges; failure iff cyclic support graph has ≥2 separated zero gaps of length ≥m. Fourier covariance converts recovery with Fourier window to recovery of transformed signal. Every Floquet sector is modulated repetition of a p-periodic vector; two spatial/frequency disconnections yield |supp u|≤p-m and |supp Fu|≤p-2⌊m/q⌋, contradicting Tao prime uncertainty p+1 unless m+2⌊m/q⌋≤p-1. Explicit polynomial with roots in two length-h blocks constructs counterexamples at every admissible smaller m. The Euclidean closed threshold follows. Recomputed threshold for p≤13 q≤6 and polynomial Fourier zero sets for each witness.

## originality

PASS

Bartusel supplies the phase-product graph characterization, dual Fourier-window criterion and a general composite-size sufficient bound; Tao supplies prime support uncertainty. Neither the general composite condition nor prime-only corollary determines the exact necessary-and-sufficient threshold inside each prime-period Floquet eigenspace of pq with unrestricted comparison signals.

## value

PASS

The exact sector-specific bandwidth transition, elementary closed formula and matching witnesses give a motivated improvement over generic composite STFT thresholds in an invariant signal class; the necessary-versus-sufficient window quantifier is precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
