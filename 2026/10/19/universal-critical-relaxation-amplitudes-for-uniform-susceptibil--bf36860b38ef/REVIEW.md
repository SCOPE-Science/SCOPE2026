# Independent mathematical audit

## correctness

PASS

The strict positive loss in each column makes e^(-Mt) a positive-cone contraction in the 1-norm and bounds total population by scalar comparison. Susceptibles are eventually bounded away from zero by comparing with S'=ν-(μ+λ_max)S, so LaSalle applies even for S(0)=0. The critical Lyapunov derivative is -μ(S-S_*)²/S; on S=S_* invariance forces λ=0, and the stable residual stage system has no nonzero bounded complete orbit. For the infected-block rank-one resolvent, K(t)=β^T e^(-Mt) P≥0 has positive integral and is positive on some interval; a strict triangle inequality rules out imaginary roots other than 0, decay rules out roots with Re z>0, and the simple-factor derivative is S_*d>0 since d=∫tK(t)dt. For w=ℓ^T x>0, λ≤Cw, so |(log w)'|→0. Choose a late starting time with this derivative bounded by ε below both stable decay rates. Ratios w(t-v)/w(t) then converge to 1 for fixed v and are bounded by exp(εv) in the late-time convolutions; initial transients divided by w vanish. Thus x/w→q/d, λ/w→1/(S_*d) and (S-S_*)/w→-1/(μd). The reciprocal derivative tends to 1/(μS_*²d²), yielding all three scaled limits and logarithmic incidence by integral comparison. If w=0 initially, λ≤Cw and a scalar differential inequality keep w=λ=0, giving exact exponential dynamics. This reasoning allows q_j=0 and does not assume irreducibility. The supplied finite check was inspected only; it does not verify the general rate or cumulative incidence.

## originality

PASS

Credit the same ODE, reproduction threshold and global threshold attraction to prior work, and the generic simple-center mechanism to standard theory. The distinct contribution is the quantitative coefficient and profile theorem with its global initial-state dichotomy, including stages not reachable from the recruitment state. No examined stronger claim yields this entire result without a fresh model-specific spectral, nonlinear and initial-face analysis.

## value

PASS

The transfer structure affects critical amplitudes through a kernel time moment not specified by the reproduction threshold. Exact global stage-vector scaling, logarithmic cumulative incidence despite vanishing prevalence, and a criterion distinguishing exponential decay in a reducible network are useful quantitative information beyond the fact of convergence. This is not a claim of a new local bifurcation mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
