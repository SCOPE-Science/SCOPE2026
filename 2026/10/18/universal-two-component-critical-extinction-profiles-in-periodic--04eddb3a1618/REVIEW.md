# Independent mathematical audit

## correctness

PASS

Positive invariant rectangles exist by choosing tau/d2<r<d1/sigma, so solutions are bounded and positive. Logistic comparison with a2 positive mean bounds resident y below away from zero. For p=sigma/d2, G'=a1+p*a2 with zero mean, exact W=x*y^p*exp(-G) satisfies W'/W=-kx and (1/W)'=k exp(G)*y^-p>c>0; hence W and x are O(1/t). Log ratio h=log(y/Y) satisfies scalar forced stable equation h'=tau*x-d2*Y(e^h-1), so h=O(1/t). Integration of the exact inverse W law against periodic Q yields W=(kI*t)^-1+O(log t/t²), x=f(t)/t+same error; subtract unique positive periodic solution H(t)/t in h equation to obtain h=H/t+O(log t/t²) and y=Y+YH/t+same error. Mean(f)=1/k by normalization, rigorously proving seasonal invariance. Independent rational check for source coefficients (d1,d2,sigma,tau)=(2,3,4/5,11/10) gives k=128/75; finite RK4 output not a proof.

## originality

PASS

Garcia-Fuentes, Kalita and Langa 2024 examine forward attractors under strict average inequalities and discuss the critical cooperative equality boundary as open/not covered; their other joint 2023 arXiv work uses a positive gap. Neither previously established the entire universal periodic t^-1 asymptotic and resident above-orbit correction. A broad center-manifold reduction could imply rates but must be compared at the specific time-dependent coefficients.

## value

PASS

The theorem resolves a motivated critical-invasion boundary in a standard two-species periodically forced ecology ODE with explicit universal positive periodic profiles and forcing-independent mean coefficient, separating critical algebraic relaxation from the known strict-gap exponential regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
