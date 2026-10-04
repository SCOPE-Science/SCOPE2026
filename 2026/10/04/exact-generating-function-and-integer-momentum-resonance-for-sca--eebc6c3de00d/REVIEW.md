# Review

## Correctness

PASS. Equal averaging gives \(z_t=t x_t-(t-1)x_{t-1}\), which reduces the scalar Schedule-Free SGD state to an exact second-order nonautonomous recurrence. Summation yields
\[
(1-q)(1-Aq)G'(q)+s\beta G(q)=x_1.
\]
The displayed generating function satisfies this equation and the initial condition. For \(|A|<1\), singularity analysis at \(q=1\) gives the noninteger polynomial tail, while integer \(r=\beta/(1-\beta)\) removes that branch and leaves a rational pole, giving geometric decay. At \(A=0\) the generating function is a finite polynomial and the binomial termination formula follows exactly. The strict full-state frontier is \(|A|<1\), or \(0<s<2/(1-\beta)\); the \(A=-1\) boundary is excluded because the base sequence fails to converge even when averaging can make \(x_t\to0\).

Risks: the theorem uses exact real arithmetic and exact parameter identities. It does not claim robustness of finite termination to floating-point or stochastic perturbations.

## Originality

PASS. The primary Schedule-Free SGD paper gives the exact update and an empirical quadratic stability diagram showing that interpolation permits larger learning rates, but its inspected text does not provide the scalar generating function, exact stability ceiling, arithmetic rate dichotomy, or finite-termination resonance. The later nonconvex theory paper proves optimal complexity and parameter guidance without this constant-step scalar classification.

Focused semantic searches over schedule-free quadratic stability, exact learning-rate ceilings, generating functions, rational momentum, and finite termination returned nearby results on other averaging, momentum, and quadratic methods but no statement implying the complete claim. The principal residual risk is equivalent analysis under older primal-averaging or special-function terminology.

## Value

PASS. The source paper explicitly highlights enlarged quadratic learning-rate stability as an empirical feature of Schedule-Free momentum. The exact ceiling \(2/(1-\beta)\) resolves that scalar phenomenon, while the generating function explains a qualitatively unexpected arithmetic transition: the common exact values \(\beta=0.8,0.9,0.95,0.99\) correspond to integer \(r\) and therefore replace the generic polynomial tail by geometric decay. The special midpoint \(s=1/(1-\beta)\) even gives finite termination in exact arithmetic. These statements provide a sharp benchmark for implementations and broader theory rather than an arbitrary scalar invariant.

Same-model review: passed. Independent audit: not yet performed.
