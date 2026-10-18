# Scientific review: An exact two-step relaxation frontier for uniformly sampled Kaczmarz

## Correctness — PASS

For the two normalized row directions, the error operators are \(U=I-uu^{\mathsf T}\), \(V_0=I-vv^{\mathsf T}\) and \(V_\delta=I-(1+\delta)vv^{\mathsf T}\). Exhaustively expanding the four ordered products gives a symmetric matrix \(D_2\) with the trace and determinant in RESULT.md. The monotonicity of \(t^4+s^2t(t+2)\) proves uniqueness of the phase transition. The real symmetric spectral theorem gives all positive/negative/equality conclusions. Exact rational arithmetic checks 1,729 sample parameter sets and the stated witness; the algebra, not the sampling checks, proves the real-parameter result.

## Originality — PASS

The primary 2026 volume-sampling paper defines the exact relaxation and proves a one-step bound, but not its two-update difference, sign classification or quartic threshold. Wang–Agaskar–Lu provide general exact MSE tools for unrelaxed Kaczmarz. Marshall–Mickelin address time-varying scheduled rates in a different noisy setting. General deterministic diagonal-relaxation theory does not compare this particular iid two-step law. Semantic searches also returned nearby work on cyclic-order bias, residual selection, and related stochastic sampling models, each with a different object or quantifier. These comparisons do not establish absolute novelty; a historical specialized equivalence, including in an inaccessible early conference paper, remains a residual risk.

## Value — PASS

The result resolves a natural discrepancy between a method's locally weaker one-step guarantee and observations that the relaxed method can perform better after repeated updates. An exact full phase diagram and rational witness at the first noncommuting dimension identify the mechanism and its limit. The result does not assert uniform benefit, asymptotic speedup or a general guarantee in larger systems.

## Closest scientific literature and limitations

Entezari–Banerjee–Kalantari, arXiv:2610.12346v1, Theorem 2 and experiments; Wang–Agaskar–Lu, arXiv:1502.00190v1, exact MSE formulas; Marshall–Mickelin, arXiv:2202.12224v4, scheduled rates; Censor–Elfving–Herman–Nikazad, DOI:10.1137/050639399, diagonally relaxed projections. Full comparisons and residual risks are detailed in AUDIT.json. The theorem covers only the exact two-row, two-update, iid sampling setting.

Self-review: passed. Independent audit: not yet performed.
