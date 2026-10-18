# Independent mathematical audit

## correctness

PASS

Reconstructed the two-parameter optimization from the frozen RESULT.md and source Remark 7.3: a=1-σ>0, x=√ε1, y=√ε2; on x+y≤2a the derivative of h(x)=x-x²+x⁴ is 1-2x+4x³>0 for x≤1/√2. On x+y≥2a, monotonicity of the exact product-test rejection R allows reduction to x+y=2a. With x=a+z,y=a-z the exact first-branch defect is 2z²(1-6a²-z²)>0 unless z=0 because a²≤1/8. This proves a unique symmetric maximum, and the improvement over Proposition 7.1 is a²(1-2a²)/4>0. Independently evaluated grid maxima for a=.08,.20,1/(2√2); finite grids corroborate but do not prove the continuum optimum.

## originality

PASS

The exact product-test theorem provides the nontrivial two-parameter upper bound but does not optimize it in its discussion of QMA conversion; the frozen result supplies a closed analytic high-soundness optimizer. The Harrow–Montanaro reduction is prior and uses only earlier product-test estimates. The Resultary semantic comparison did not disclose an equivalent prior closed-form maximum; this is a bounded novelty assessment, not priority certification.

## value

PASS

The analytic closed form improves the central QMA(k)→QMA(2) application for every σ=1-1/q (integer q≥3), giving rejection 1/(2q²)-1/(2q⁴) instead of 1/(4q²), doubling its leading coefficient. This is a mathematically motivated optimization of the main source, not an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
