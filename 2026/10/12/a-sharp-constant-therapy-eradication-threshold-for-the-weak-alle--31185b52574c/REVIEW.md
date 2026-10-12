# Self-review

## Correctness

PASS. The source equation with constant treatment is a scalar autonomous ODE. Exact maximization of
\[
\left(1-\frac{x}{K}\right)\frac{x}{x+c}
\]
gives the unique maximizer
\[
x_*=\sqrt{c(K+c)}-c
\]
and maximum
\[
\frac{(\sqrt{K+c}-\sqrt c)^2}{K}.
\]
The resulting sign partition proves global convergence to zero exactly for \(g>g_c\), a positive critical equilibrium at equality, and two positive equilibria below threshold. The bundled checker replays the algebra independently.

## Originality

PASS. Maximum-per-capita-growth threshold reasoning is standard and is not claimed as new. The accepted contribution is the exact source-specific closed form, complete phase classification, and quantitative sharpening of the published \(g>r\) sufficient condition. Exact source, formula, threshold-alias, correction, and prior-ledger searches found no equivalent published source-specific statement.

## Value

PASS. The exact threshold is the least sustained constant treatment strength that globally attracts the deterministic single-clone model to zero. At the source's displayed \(c=K/2\), it is \(r(2-\sqrt3)\), only about \(26.8\%\) of \(r\), so the sharpening materially changes the model's treatment-intensity interpretation.

## Closest literature and limitations

Earlier tumor-Allee work establishes that density-dependent cooperation can determine tumor persistence or extinction, but in different stochastic/spatial models. It does not supply this scalar treatment threshold.

The result assumes constant continued treatment, does not solve a finite-duration optimal-control problem, and is not a clinical dosing recommendation.

Self-review: passed. Independent audit: not yet performed.
