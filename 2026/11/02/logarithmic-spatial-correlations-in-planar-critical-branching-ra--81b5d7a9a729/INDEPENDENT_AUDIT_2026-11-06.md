# Independent mathematical audit

## correctness

PASS

For the explicit aperiodic five-move walk with mean-one offspring and finite positive offspring variance, the ordered distinct-particle factorial moment follows from first-generation branching: F_n(x,y)=sigma² sum_{s=1}^n sum_z p_{n-s}(z)p_s(x-z)p_s(y-z). Off-diagonal covariance subtracts the mean product; on the diagonal add p_n(x). The convolution p_s*p_s=p_{2s} and two-dimensional local CLT with variance 2/5 per step yield the log window s between |x-y|² and n: coefficient (5 sigma²/(8 pi))g_1(u)(1-2 theta). Boundary theta=1/2 removes this log window; the noncoincident diffusive limit is a two-Gaussian convolution, with correct log singularity. Independent private exact finite branching check, normalized variance approximants at n=50,100,200 (ratios 1.294,1.255,1.224), and source verifier were inspected. Those finite checks do not prove n→infinity, which follows from the early/late bound and dominated CLT argument. No survival conditioning or Gaussian-offspring assumption.

## originality

PASS

One-site factorial second moment and conditional clustering are known and not the asserted novelty. Primary Lalley–Zheng Proposition 25 has the diagonal sum; Section 6 concerns occupied-site clustering, not unconditional Pearson correlations for distance n^{theta+o(1)}. Bai–Chen–Lin addresses site survival/Yaglom. The final exact logarithmic two-site profile plus matching distinct-diffusive covariance asymptotic was not found among these comparisons, but general many-to-two identities make implicit antecedents a genuine priority risk.

## value

PASS

Precisely quantifies loss of common ancestry between two population counts over all subdiffusive polynomial separation scales; a natural spatial-correlation observable and a sharp decorrelation boundary, not just the known factorial-moment identity or numerical sampling. The matching macroscopic kernel provides a cross-scale normalization benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
