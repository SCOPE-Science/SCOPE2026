# Independent mathematical audit

## correctness

PASS

The Gaussian propagated noise is omega sum_{j=0}^{K-1}(I-omega B)^j A^T xi, whose covariance equals sigma² B^-1[I-(I-omega B)^K]^2. On 0<t<1 its derivative has sign of H_K(1-t)=2K(1-t)^(K-1)-(2K-1)(1-t)^K-1: H has one positive interior maximum, H(0)=-1,H(1)=0, yielding exactly one t_K and strict increasing then decreasing f_K. This proves sharp safe ordering for all spectra below t_K; select t_K<a<b<min(s,1) for any s>t_K to reverse ranking. Asymptotics follow the pointwise rescaling t=c/K and unique positive root e^c=1+2c. For even K, at t=2-epsilon the covariance weight is O(epsilon²), whereas f_K(t_K)>0; the Hadamard eigenbasis gives exact rank-one residuals and the four Rademacher outcomes give variance gamma²/(4N). The proof does not claim these ratios for whole confidence pipelines. Independent matrix spectral calculations and exact arithmetic corroborate displayed formulas.

## originality

PASS

Abhishek & Holman supply the Landweber uncertainty propagation and randomized normal-operator approximation; those are prior, not claimed. Celisse–Wahl supply the spectral filtering method and Ito–Jin randomized SVD. The new theorem optimizes spectral ranking of the finite-step covariance over all admissible normal operators, identifies its sharp uniform ceiling and quantifies residual diagonal-probe mismatch. Closest 2026 motivating paper could not be fully read here and may contain more detailed ranking analysis.

## value

PASS

For inverse-problem UQ, retaining highest normal singular values need not retain highest propagated covariance variance directions; an exact all-K safe frontier and unbounded residual probing mismatch are mathematically motivated diagnostics. This is a meaningful algorithmic spectral-order effect, not a claim of incorrect confidence intervals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
