# Review: sharp spectral-peak onset in inhibitory delayed telegraph noise

## Correctness — PASS

The positive stationary spin process is constructed by a Poisson update scheme with strictly positive fresh-sign probability. The compensated-jump martingale has linear delayed drift and orthogonal increments, giving a positive spectral numerator and the exact transfer-function denominator. The uniform bound on \(1-\cos u\) and \(\sin u\) proves the sharp *global* zero-frequency regime, including its equality boundary. A nondegenerate quartic expansion and a compactness argument give precisely two global peaks immediately above the threshold and the square-root coefficient. The accompanying standalone numerical verifier passes 48 selected checks of global peak status, variance normalization, and onset scaling. Numerical testing is corroboration, not the proof.

## Originality — PASS, subject to priority risk

The 2024 original article already gives the delta-memory process and exact stationary correlations. The 2025 general-memory article already covers the Fourier spectrum formula through its Eq. (22). The assessed statement is **not** the derived power spectral denominator, but rather the globally sharp threshold \(T_*\), the zero-frequency versus nonzero-frequency classification, and the unique near-critical pair with a computed square-root onset. Neither paper's inspected relevant material supplies this optimization. Searches for spectral-resonance equivalents and comparisons with related delayed-noise and telegraph models found no decisive dominating statement. This does not prove global publication novelty; broader delayed stochastic-feedback literature poses residual priority risk.

## Value — PASS

The most prominent spectral frequency is a natural observable for a noise source with delay. The theorem provides a sharp if-and-only-if delay threshold and a critical scaling law while the stationary dynamics remain stable. This differentiates fluctuation resonance from dynamical loss of stationarity and is a substantive exact phase boundary rather than a chosen numerical example or mere reexpression of an old formula.

## Limits and comparison

Results apply to symmetric binary signals with one inhibitory discrete delay and \(0<h<c\). An exact global count of high-delay sidelobe peaks, arbitrary memory kernels, asymmetric switching, and independent specialist priority assessment lie outside the claim. Key comparisons: Apostolov et al., arXiv:2402.11038v1 (2024), delta-delay definitions and correlation equations; Melnyk et al., *Physical Review E* 112, 014127 (2025), general Fourier transfer Eq. (22).

Self-review: passed. Independent audit: not yet performed.
