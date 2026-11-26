# Independent mathematical audit

## correctness

PASS

The unnormalized Fourier objective and support-inside convention are consistent, including N=5. For 3∤N, the quadratic with roots u,v is nonnegative at the sampled cosines and has strictly positive unscaled average 1/2+uv. The two positive dual multipliers force both zeros. Neither active level is ±1 (for even N≥8 there is a sample strictly between 2π/3 and π, and a positive-angle sample below 2π/3 for every N≥5). Nonnegativity at both signed frequencies then forces the two odd coefficients to vanish. For 3|N, the opposite third-root samples force a+b=1 and equal imaginary coefficients at the optimum. The factorization reduces the constraints to b≥L+|t|cot(θ_u/2) and b≤R−|t|cot(θ_v/2): that pair first forces |t|≤T, so monotone selection of the upper bound is only needed on that feasible interval. At b=B,t=T the relevant second-factor numerators become 1+2cos(θ∓β), vanishing at θ_u,θ_v respectively. For N≥9, β<0.7 gives T≤0.7/(3−0.7²)<1/(2√3); hence all other bounds are weaker. At N=6 only the adjacent samples matter and L=B, making (L,0) nonextreme. A separate floating-point enumeration of active quadruples in the full four-real-coordinate feasible polytope found exactly the predicted optimal vertices for N=5 through 24, including 3 vertices at 6 and 4 at 9,12,15,18,21,24. Replay: python3 /workspace/reproductions/frozen_checks.py 1. Neither this bounded numerical check nor the frozen checker is used as an all-N proof; the frozen checker does not directly enumerate the full nonresonant complex face.

## originality

PASS

Pass applies to the complete complex maximizing face, not the scalar Turán mass or even optimizer. The closest primary and indexed sources cover those ingredients, or complex geometry for a different support, but do not supply the stated cyclic equality classification. This is a best-of-evidence conclusion, not a priority certification.

## value

PASS

For the shortest interval support with two harmonic coefficients, the known optimal number does not identify which positive-definite functions attain it. The exact vertices and change from complex uniqueness to three or four extremal optimizers give the complete equality and rigidity information one needs when using the bound; the resonance is intrinsic to the Fourier sample grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
