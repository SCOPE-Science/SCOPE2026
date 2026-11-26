# Independent mathematical audit

## correctness

PASS

The frozen Finding is correct, but the original Limitations claimed a false two-step exact-CG bound for both systems. For m=2, λ=3, μ=1 and ω=(1,1,0), a direct generalized eigensolve independently gave 1, 2, 16/7, also obtained in exact arithmetic from the rank-one plane determinant. The complete repaired RESULT.md replaces the wrong claim by the generic three-eigenvalue conclusion for m≥2, and states the sign-symmetric block reduction explicitly. Fresh check: N=A^(1/2)qqᵀA^(1/2), so A−N has rank one in the invariant two-plane and the symmetric preconditioned matrix has one eigenvalue 1 there. Its other eigenvalue is det(H)/det(I+N) restricted to the plane, giving K(t); the orthogonal bulk has m−1 eigenvalues h₂. For positive finite t, h₂<K(t)<h₁ and K decreases. The limits t=0,∞ give h₁,h₂. For m=1 the bulk complement is absent, so the repaired statement correctly gives two eigenvalues. CG can need as many iterations as distinct eigenvalues with nonzero initial-residual projections, so even a strict improvement (e.g. λ=7, μ=1, t=1, m=2, giving K=64/29<4) can leave three instead of two generic steps. The spectral comparison gives λ(h₁−h₂²)t>μ²h₂; equality/lower regimes cannot give strict improvement, including exact spike alignment when h₁=h₂². The independent χ² variables give t=rX²/Z and the beta complement. A direct survival-function computation for the displayed example gives 1.8853445e−14, 0.59663954, 0.70137020. For fixed μ, Z/m→1 and thresholds for X² scale as μ²h₂m/λ², μ³h₂²m/λ⁴ and μ⁴h₂m/λ⁴; normal-square continuity and absence of an atom at zero give both critical windows and their zero/one sides. Variance ratios are ordered since λ>μ, so the probability ordering is strict in the improvement-possible regime only. The frozen verifier was inspected, not executed, and does not test the incorrect former CG assertion.

## originality

PASS

The repaired result retains the exact finite success event and critical dimension windows at fixed unscaled θ=1, not the construction of the sketches, the beta identity, or a generic third-eigenvalue observation. The closest exact probability comparisons use either oracle-scaled Nyström at fixed dimension two or a different Ritz preconditioner. Neither contains the unscaled obstruction and growing-bulk windows together as a parameter specialization. Correcting the CG caveat does not add an originality claim.

## value

PASS

A dominant spike over a repeated positive bulk is a motivated calibration model for distinguishing Gaussian sketches downstream of approximation quality. The exact all-orientation obstruction and the two different dimension exponents quantify when increasing alignment reliably changes the actual spectral conditioning; the precise critical probabilities allow meaningful comparisons. The repaired interpretation explicitly recognizes that even strict condition-number improvement need not improve exact CG steps and establishes no runtime, practical EDA, or optimized-scaling guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
