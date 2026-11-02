# Independent mathematical audit

## correctness

PASS

For actual positive Gaussian noise-first fixed exponential, E exp(Z_i)=exp(c_i h) independently of cross-coordinate covariance. Exact first-mean identity is exp(hC)exp(h(K-C))=exp(hM). Q=exp(-hC)exp(hM) is positive-spectrum upper triangular. A Metzler logarithm H=K-C with exp(hH)=Q cannot have below-diagonal positive entries (nonnegative power-series argument); its upper entries are uniquely determined by divided differences. The resolvent formula for (log Q)_13 has sign sign(sqrt(d1 d3)-d2), where d_i=exp(-hc_i), via reciprocal substitution and strict J monotonicity, equivalent to 2c2>=c1+c3. Both nearest couplings strictly positive; in 2x2 the sole logarithmic divided difference is positive. h>0 exact, including equal variances, noncommuting original matrices. Independent SciPy logm/expm checked 21 parameter-step settings, sign and exact moments; examples with (1,0,1) give K13<0. Numerical checks are secondary to integral proof.

## originality

PASS

Metzler matrix logarithms and positive integrating-factor schemes are prior art. After examining the 2026 public preprint Algorithm 1, its method uses a time-varying conjugated drift rather than this exact frozen noise-first product. Existing stochastic Markov embedding theory studies different generator constraints. The specific all-h iff variance midpoint threshold was not located in inspected primary sources; possible implicit coverage by classical triangular divided-difference theory is a priority risk.

## value

PASS

Sharp iff midpoint inequality identifies the first dimension where a positive exact-first-moment drift calibration can fail under the specified noise-first exponential splitting, uniformly for every step size. This is a structural positivity obstruction for motivated stochastic simulation, not a generic assertion about all integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
