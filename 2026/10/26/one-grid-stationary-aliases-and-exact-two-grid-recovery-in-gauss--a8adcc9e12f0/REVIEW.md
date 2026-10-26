# Review of stationary Euler--Maruyama Gaussian inverse laws

## Correctness — PASS

The Gaussian linear Markov chain satisfies an exact discrete Lyapunov equation. Under the stated strict eigenvalue stability condition its geometric-series covariance is \(C_h=q(A-hA^2/2)^{-1}\). Every inverse-fiber solution is obtained by writing the symmetric square root \(S=I-hA\); conversely each symmetric square root gives an SPD stable drift. The exact one-grid feasibility boundary \(C\succeq2qhI\), sign-count regime, and Grassmann families follow from full eigenspace decompositions. Interpolating the inverse covariance at two distinct grid steps gives the exact matrices \(A/q\) and \(A^2/q\); their ratio recovers \(A\), and a trace recovers \(q\). The two-grid consistency condition is necessary and sufficient. Algebraic precision sensitivity, exact-process scaling ambiguity and the nonsymmetric rotational counterexample were checked directly. The included exact-rational checker passed 63 finite configurations; the analytic argument proves the general result.

## Originality — PASS, with recorded priority risk

Wang and Wu (arXiv:2604.14543, main theorems and invariant-measure section) prove forward numerical invariant-measure convergence, not stationary-only reconstruction at multiple discretization levels. Higham (SIAM Review, 2001) gives standard Euler--Maruyama simulation and stability foundations; the scalar AR(1) stationary variance and sign ambiguity are classical and expressly excluded from any novelty claim. Tran, Tran and Nguyen (arXiv:2601.20268, Methods Theorem 3) recover drift and noise from transition data, which provide conditional time correlations absent here. Related multilevel work operates on trajectories/posteriors. The assessed original package is the complete SPD *matrix fiber geometry*, full two-grid recovery and consistency criterion with **both** drift and diffusion unknown, and the exact limits for true continuous-time stationary data and nonsymmetric drift. Semantic searches of relevant mathematical records did not expose a directly dominating statement; they cannot establish mathematical priority. Older discrete-Lyapunov inverse literature or scalar-to-matrix generalizations remain credible equivalence risks.

## Value — PASS

Numerical invariant-measure calibration from independent long-run simulations must distinguish identifiability of the numerical model from identifiability of the underlying continuous process. The theorem gives an exact experimental-design threshold: one stationary-resolution marginal can admit exponentially many or continuously many symmetric drifts even with noise known, but two resolutions admit a unique joint drift/noise reconstruction, with a direct algebraic consistency test. The gap sensitivity and explicit circulation ambiguity mark useful failure boundaries. The result is structural rather than a numeric curiosity, though it does not furnish finite-sample inference rates or a general method for nonlinear SDEs.

## Risks and scope

Independent bibliographic priority is unverified. The one-grid square-root parametrization follows elementary matrix spectral theory once the AR(1) covariance is written; the value and novelty reside in its complete inverse-model and multi-resolution interpretation, not its elementary algebra in isolation. The conclusion is restricted to known time resolutions, symmetric SPD drift, common isotropic additive noise and exact stationary one-time marginals. The report does not present itself as an independent validation.

Self-review: passed. Independent audit: not yet performed.
