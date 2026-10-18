# Independent mathematical audit

## correctness

PASS

On full-column-rank F(x)=Ax, B=A^T A is positive definite and the exact affine model gives LM update x+ = lambda(B+lambda I)^-1 x. For each nonzero iterate, spectral factors are strictly in (0,1), making predicted reduction positive; the nonmonotone window maximum M>=current residual makes the acceptance quotient 1+(M²-current²)/(current²-new²)>=1. Because the original p2<1, every first trial is accepted, with mu_{k+1}=max(mu_k/4,m) and exact closed form. The source damping formula satisfies lambda<=Lambda=mu0 exp(1/e) by t^(1/t)<=exp(1/e) for t>=1 and t^delta<1 for t<1, giving global q=Lambda/(sigma_min²+Lambda)<1. Once near zero with mu=m, delta_k=1+1/log(k+e), so ||x_{k+1}||<=C||x_k||^(2+epsilon_k). Bootstrapping ||x|| to squaring in scaled coordinates makes |log||x_k||| grow at least as 2^k, hence epsilon_k |log||x_k|||->infinity and the quadratic error ratio tends to 0. The nonterminal/zero-tolerance qualification is essential; no fixed order >2 claimed. Independent exact linear-algebra and damping-branch checks passed.

## originality

PASS

The source 2026 NMLM paper proves general quadratic-local behavior at gamma=nu=1 but does not analyze this source-specific full-rank affine exact-model subclass, every-step acceptance or vanishing quadratic ratio. Earlier LM superquadratic or cubic theorems use other trial steps and damping laws, so they do not imply this literal algorithm's recurrence. Structural insight is the ratio collapse and logarithmic-exponent asymptotic.

## value

PASS

The full-column-rank affine class is the canonical nonsingular benchmark for nonlinear-equations solvers. The exact first-trial acceptance and control-variable collapse show the nonmonotone safeguard becomes inactive, while a subtle logarithmic excess exponent causes a vanishing quadratic constant even though the exponent tends to one. This identifies a meaningful and reproducible algorithm-specific sharp behavior beyond the general theorem, not merely a renamed convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
