# Independent mathematical audit

## correctness

PASS

For the absolutely continuous stationary law use X=2^(−J)U with geometric J of ratio r=q/p and independent uniform U. The reflected walk leaves this law stationary, and a doubling at depth zero is exactly one shift of U. Fair binary digits give E[U{2^k U}]=1/4+2^(−k)/12. This splits C_n into the centered depth term for P_1 and the uncentered term for P_{1/2}, with zero-loop weight b. To check the required spectral bound, conjugate by sqrt(π) to a symmetric half-line tridiagonal with off-diagonal c=sqrt(pq) and boundary diagonal a=pb. Outside [−2c,2c] an ℓ² eigenmode must decay geometrically with factor c/a, so it exists only when a>c and then has eigenvalue a+c²/a. For b=1 it is the simple constant mode at 1 before conjugation; for b=1/2 it exists only for p>4/5 and is strictly below 1. This gives absolute summability and the resolvent identity on the required subspaces. Substitution at both j=0 and j≥1 verifies the two Poisson solutions in RESULT.md; the first is in L²(π) and the second bounded. Contracting with the indicated weights gives S=(51p³−51p²+17p−1)/[3(3p−1)³(5p−1)], C_0=s/3−m²/4 and σ²=2S−C_0 by the stationary variance sum and absolute summability. At p→1/2 the rational σ² tends to 4, geometric J escapes, and C_0=(16/9)(p−1/2)+O((p−1/2)²). At p=1 the uniform doubling covariance is 2^(−n)/12, giving 1/4. There is no critical-state CLT or variance assertion. RESULT.md lines 25–78 are the all-time analytic replay; verify.py and VERIFICATION.md were inspected, not executed, and their finite tests do not prove the infinite result.

## originality

PASS

Best of the inspected evidence, the explicit integrated stationary coordinate variance and its critical constant are distinct. The invariant law, latent reflected walk, general tilted propagation and short stationary lag formulas are prior. Monthus's exact correlation is for uniform initial position, while the closest exact stationary covariance transform in the catalogue is later-dated. The priority assessment is for the evaluated stationary statistic, not for all-lag calculability or the method.

## value

PASS

The coordinate is a standard observable of this map. The exact variance separates equilibrium collapse from a surviving time-integrated fluctuation, fixes the critical constant 4 and quantifies the divergence relative to C_0. Neither stationary moments alone nor short-lag correlations resolve that distinction, and the resolvent gives a useful exact benchmark for fluctuation and crossover analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
