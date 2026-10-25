# Independent mathematical audit

## correctness

PASS

For any d≥1 and 0<ρ<1 the SPD star A has eigenvalues 1−ρ,1+ρ,1^(d−1). Writing diagonal squared scales x=g0² and y_i=g_i² makes F=(x−1)²+Σ(y_i−1)²+(2ρ²/d)xΣy_i. Hessian Schur complement 1−ρ^4/d>0 gives unique positive minimum a=(1−ρ²)/(1−ρ⁴/d), b=(1−ρ²/d)/(1−ρ⁴/d), with b>a for d≥2. The extremal eigenvectors w±=(1,±1_d/√d)/√2 share z=w±^T G^(−2)w±; Rayleigh quotient gives κ(GAG)≥(1+ρ)/(1−ρ), equality implies G²w+ collinear with w+ and therefore scalar diagonal G. Frobenius minimizer nonscalar at d≥2 strictly worsens κ. The 2×2 {center,leaf-mean} block has determinant ab(1−ρ²), λ+=1+o(1), while a~d(1−ρ²)/(d−1), b→1 for d≥2, hence κ_F~(d−1)/(d(1−ρ²)²) and κ_F/κ_A²→(d−1)/(16d). At d=1, a=b scalar and penalty vanishes. Independent SymPy verified stationary equations symbolically, eigenvalues and asymptotic coefficients, plus d=1,2,5 sample numerical checks near ρ=.999 showing quadratic ratios .0316255 at d=2 vs target .03125, .05037535 at d=5 vs target .05. This is a rigorous direct proof with diagnostic finite checks only.

## originality

PASS

Frobenius-residual preconditioning and diagonal-condition-number optimization are well studied, but the precise normalized SPD star all-d parameter family is solved globally for Frobenius scaling and compared exactly to scalar-unique condition-number optimization. The limiting quadratic distortion with constant (d−1)/(16d), strictness and dimension boundary were not identified in the materially inspected sources; no claim is made that diagonal scaling itself or qualitative Frobenius-vs-spectral tension is new.

## value

PASS

A diagonally scalable SPD star is a natural minimal graph-based preconditioning test bed. The closed-form unique Frobenius optimum exhibits a severe, sharp κ² degradation despite strictly reducing Frobenius loss, a concrete conditioning caution directly relevant to surrogate-objective design. Dimension d=1 contrast and exact leading constant make it substantive rather than a generic warning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
