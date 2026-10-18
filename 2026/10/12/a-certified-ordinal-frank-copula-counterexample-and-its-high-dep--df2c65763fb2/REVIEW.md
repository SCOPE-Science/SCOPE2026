# Independent mathematical audit

## correctness

PASS

Hoeffding indicator expansion gives A=sum_{ij}(C_15(t_i,t_j)-t_i t_j) and B=sum_{ij}(min(t_i,t_j)-t_i t_j)>0 for 19 exact rational thresholds. The actual check_frank.py was inspected: it brackets exponentials and logarithms using rational truncated Taylor series with proven positive tail bounds and compares exact integer endpoints for all 361 CDF terms; certified A/B>0.93092569 and latent rho<0.92938730. An independent 65-digit evaluation reproduced ordinal 0.930925698735820068..., latent 0.929365805485040128..., gap ~0.00155989325, but is NOT substituted for the rational certificate. The general theta->infinity assertion is separately established analytically by the covariance-deficit kernel, exponential domination and theta-rescaling; g(u)=(1-cos pi u)/2 has derivative-energy/variance quotient pi² vs 12 for g(u)=u, yielding pi²(12-pi²)/6. Uniform finite quantization approximates g at each fixed sufficiently large theta. No claim of finite m uniform in theta.

## originality

PASS

Barbiero (2026) proposes attenuation of Pearson correlation for Frank-ordinal scores compared with latent Spearman correlation and reports numerical work limited to <=11 categories and latent rho<=0.9; its Theorem 2 proves sign-preservation, not magnitude attenuation. The exact twenty-category example is beyond the reported search and contradicts the universal attenuation conjecture, while the asymptotic mechanism establishes a family of witnesses. Searches did not reveal a covering counterexample; exact priority remains bounded.

## value

PASS

An explicitly certified counterexample overturns a mathematical conjecture in a contemporary primary article, and a sharp high-dependence mechanism explains why rather than merely supplying an optimized number. This matters for interpreting discretized correlation models and for the conjecture boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
