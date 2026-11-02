# Scientific assessment

## Correctness

**PASS (self-review).** Frequencywise Plancherel produces the multiplication operator with scalar \(F_a\) on the full \(L^2(\mathbb R)\). The critical-point equations reduce exactly to \(t=a\coth(at)\) on \(t>a\) and \(t=a\tanh(at)\) on \(0<t<a\), each with a proved unique positive root on its stated domain. Envelope differentiation proves strict monotonicity of the central-minus-outer height after \(a=1\), yielding a single global crossing. Piecewise analytic changes of variables give an absolutely continuous spectral type and the claimed multiplicities. Exact normalizations and boundary cases are documented in the proof; a standard-library numerical checker supplements, but does not replace, the analytic proof.

## Originality

**PASS, conditional on inspected primary literature.** Abreu–Speckbacher (2018, arXiv:1808.02258v1) develop Hermite STFT large-sieve concentration and local disk reproducing formulas, but do not state this unbounded-strip norm bifurcation or its complete spectral multiplicity. Keller–Luef (2019, arXiv:1905.07741v1) treats general polyanalytic Toeplitz isomorphisms and symbol calculus, not this exact spectral profile. Closely related Hermite-band matrix concentration and bounded-disk concentration have different domains/operators, and their statements do not imply the present full \(L^2\) infinite-strip operator classification. The full-frequency marginal follows from standard Plancherel; what is specifically compared for originality is the two-threshold global phase diagram together with the exact spectral-fiber changes. Residual risk: the same sliding-window phase classification may be recorded in less visible probability or localization literature.

## Mathematical value

**PASS.** The first excited Hermite window is a canonical time-frequency object with two separated intensity lobes. The exact concentration profile shows that the appearance of a central local optimum and its victory in the global competition occur at *different* critical widths; the global optimizer jumps, while a sixfold absolutely continuous spectral multiplicity region emerges. This solves a natural sharp localization and spectral problem throughout the entire continuum of strip widths, not a single arbitrary numerical slice. It complements rather than reparameterizes previously studied compact disk-localization and finite Hermite-band problems.

## Limitations and closest comparisons

The theorem applies to the full-frequency strip and the first Hermite window only. It makes no statement about finite-frequency rectangles, higher Hermite levels, discretization stability, or nonlinear spectral inversion. The norm is a supremum, not an attained \(L^2\) eigenvalue. Source searches cannot certify historical uniqueness, and the judgement has not been independently validated.

Self-review: passed. Independent audit: not yet performed.
