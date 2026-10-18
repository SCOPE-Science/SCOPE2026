# Scientific assessment

## Correctness — PASS

The two-level effective collision probability, parity-sensitive simultaneous modular collision count, and conditional Rademacher orthogonality are proved explicitly in `RESULT.md`. They imply the variance identity without extrapolating from finite experiments. Uniform factor magnitudes are the unique equality class by Cauchy–Schwarz and strict monotonicity. The standalone program passed 395 exact modular checks, 3190 finite extremal checks, and 8 independent direct three-layer simulation settings. The signs must meet the specified conditional fourth-moment assumptions; less independent implementations are not addressed.

## Originality — PASS, with residual uncertainty

The 2026 Khan–Pratap–Sharma estimator provides a loose degree-dependent variance upper bound, not the exact two-factor sharp law. Ahle and coauthors supply the underlying recursive construction and second-moment composition, not the exact finite input-profile classification. Pham and Pagh analyze the ordinary single TensorSketch construction, whereas Sharma and coauthors' newer paper addresses complex variants. The closest available mathematics records concern different tensor/variance objects. No equivalent or dominating complete theorem was identified after comparison of statements and implications. A relevant PMLR full text was not accessible, and an unindexed exact fourth-moment computation could potentially subsume the finding. Absence of retrieved overlap is not proof of global priority.

## Value — PASS

The exact all-width, all-factor-dimension variance and extremizer classification answers a motivated calibration question for a new recursive trace-estimation method. It exposes two-level collision inflation and the parity-sensitive self-intersection correction, establishing a sharp leading variance constant on the natural separable PSD benchmark. The claim does not purport to improve variance for every PSD input.

## Scope and limitations

Only real degree-two recursive TensorSketch, independent layers and the explicit sign/hash moments, and separable rank-one PSD inputs are included. No numerical-runtime or floating-point claim, no nonseparable theorem, and no independent external validation is asserted.

Self-review: passed. Independent audit: not yet performed.
