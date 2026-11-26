# Independent mathematical audit

## correctness

PASS

In standard CGS the first p and u equal r₀, the auxiliary update is q=u−α₀Ap, and r₁=r₀−α₀A(u+q); this is exactly (I−α₀A)²r₀ with α₀=(r₀ᵀr₀)/(r₀ᵀAr₀). SPD and nonzero r₀ ensure no first-step division by zero. In an eigenbasis with squared normalized residual coefficients as masses, the squared norm ratio is E[(X−EX)^4]/(EX)^4. With fixed mean the secant bound for x↦(x−EX)^4 is attained by the endpoint distribution; choosing its square-root weights as the two residual coordinates realizes the sharp envelope. With t the odds at the upper endpoint, this gives exactly G_κ(t). The equivalent compact probability interval ensures continuous dependence on κ; a maximizing t is positive and finite for κ>1, and each such G_κ(t) increases strictly in κ. At κ=1 the ratio is zero. For u=κt the scaled expression on u≤κ is at most u/(1+u)^4, and the remaining tail is at most 2/κ³; u=1/3 attains the limiting constant 27/256. Thus the continuous maximum crosses one exactly once. The stationarity cubic and cleared level-one equation give the independently recomputed resultant 16κ(κ²+κ+1)P(κ); the reciprocal reduction and one sign change of Q(z+2) prove just one root for κ>1. Independent SymPy/mpmath replay gives κ*=3.4428158692570749535… and t*=0.0869983437269713773… (branches/7c288f66-3721-42ef-ae71-b7b4dede58f9/independent_threshold_check.py). The κ=4 witness has residual (9/100,144/25) and exact squared ratio 331857/170000. Frozen RESULT.md, VERIFICATION.md and verify.py were inspected, not executed. The conclusion is for the exact unpreconditioned SPD first step with the specified shadow residual, not later iterations, alternate shadows, or nonnormal problems.

## originality

PASS

The squared CGS residual polynomial, qualitative irregularity and convex-secant principle are established ingredients. The distinct claim is the sharp condition-number frontier for the defined SPD first-step experiment, including its algebraic threshold and worst-case asymptote; neither the accessible CGS comparisons nor the closest distinct indexed frontier covers those quantities.

## value

PASS

Qualitative CGS irregularity does not tell when even the first residual is safe, nor how bad the first spike can be with normal, positive eigenmodes. This result identifies the precise condition-number cutoff and sharp κ^(3/2) norm growth despite SPD structure, with realizable two-mode tests. These are useful diagnostics and benchmarks for CGS studies without extrapolating to subsequent iterations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
