# Independent mathematical audit

## correctness

PASS

The pure one-particle two-site concurrence is 2|psi_i psi_j|; summing unordered pairs and using unit L² norm gives (sum |psi_i|)^2−1. In the two-sided continuum ansatz the squared norm before scaling is xi, so the peak amplitude scales as xi^(−1/2). The cutoff used in source Eq. (8) gives an L¹ integral 2 sqrt(xi)(1−e^(−1)), and the whole line gives 2 sqrt(xi). These are continuum model expressions, not exact discrete concurrences for small xi. For the discrete model the geometric sums give S_L²/Z_L−1, and their fixed-xi limits give (1+r)^3/[(1−r)(1+r²)]−1, equal to the reported rational form. With t=1/xi, K_infty+1=coth²(t/2)tanh(t); expansion gives 4/t−2t/3+59t³/180+O(t^5). At fixed finite L the growth saturates; the order of limits matters. Independent direct pair sums and the symbolic series corroborate the proof (record5_discrete_check.py, record5_full.txt and record5_series_check.py, record5_series.txt under /workspace/branches/8753c010-e247-4ba9-847a-6c399c9a4293). The source's artifacts/verification_output.txt is a recorded computation, not independent proof or attestation.

## originality

PASS

Distinct claim: the quadratic inference in a specific prior calculation fails under normalization of that calculation's own envelope, with an exact discrete model confirming the corrected asymptotic. Neither the general pair-concurrence identity nor exponential localization itself is new.

## value

PASS

The normalization check changes the exponent of the analytical law used in a paper's interpretation, not merely a prefactor or notation. The discrete limit shows the correction is not an artifact of replacing sums by integrals, and clarifies where finite-size saturation intervenes. It does not claim a universal scaling for actual Anderson eigenstates or that the qualitative localization trend is reversed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
