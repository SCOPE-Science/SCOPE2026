# Independent mathematical audit

## correctness

PASS

Direct substitution of \(\nabla f(x,\xi)=\lambda x+\xi\) into the source update gives \(e_{t+1}=(1-a)e_t+a\varepsilon_{t+1}\) and \(x_{t+1}=(1-s)x_t-se_t\), so Schur stability is exactly \(0<s<2\). Solving the scalar autoregression and the two stationary covariance equations reproduces \(\operatorname{Var}(e)=a\tau^2/(2-a)\) and the packaged formula for \(\operatorname{Var}(x)\). Dividing by the exact SGD variance yields the stated ratio, and algebra gives a strictly positive \(1-R\) whenever \(0<a<1\). Independent symbolic reconstruction of the variance, ratio and derivative agrees with the package verifier.

## originality

PASS

The original STORM paper gives the corrected-momentum update and motivates the momentum/learning-rate tradeoff, but its inspected complete text analyzes adaptive nonconvex complexity rather than the stationary covariance of this constant quadratic benchmark. The exact triangular decoupling, unchanged SGD stability interval, closed stationary variance and strict variance-ratio comparison were not found in the inspected STORM/STORM+ or hybrid-estimator sources. General linear-systems theory can solve the resulting Lyapunov equation once the specialization is made, but no prior implication was located that states this source-specific benchmark.

## value

PASS

This is a canonical exact-noise benchmark for the estimator architecture that separates deterministic stability from stationary variance reduction. It shows that the correction preserves the full SGD stability interval while lowering long-run iterate variance and quantifies the opposing memory-speed limit as \(a\downarrow0\), information directly useful for interpreting the algorithmic template.

The dated certificate retains the supplied scientific assessment, sources and limitations.
