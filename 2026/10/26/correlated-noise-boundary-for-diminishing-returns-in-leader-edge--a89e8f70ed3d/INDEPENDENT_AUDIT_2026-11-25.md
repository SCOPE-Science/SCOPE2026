# Independent mathematical audit

## correctness

PASS

With at least one grounded leader in a connected graph, extending a follower vector by zero on leaders gives a Dirichlet quadratic form that is positive on nonzero vectors. Thus the stable OU mean decays and the Lyapunov covariance identity gives P=tr(G Sigma)/2, G=A^(-1). Differentiate G by -G E_ii G: the first partial is -(G Sigma G)_ii/2, nonpositive even for singular PSD Sigma; the second partial is G_ij(G Sigma G)_ij. Inverse positivity follows, e.g., by integrating the entrywise-nonnegative semigroup exp(-rA) of the Metzler matrix -A. Entrywise nonnegative Sigma therefore makes all rectangular differences nonnegative, including repeated endpoints via the same-coordinate second derivative; telescoping gives the exact set inequality. Conversely choose the proposed two leaders, all followers grounded at s to the first, and the sole inter-follower edge c between the labels of any negative Sigma_ij. The two absent edges to the second leader are legitimate unit candidates. On their increment square G_ij=c/det of the positive two-by-two block, and sG tends uniformly to I; hence s^2(G Sigma G)_ij tends uniformly to Sigma_ij<0. Integration gives a negative gap for large finite s, even with other noise correlations present. For the exact two-follower boundary take x=s+c and D0=x^2-c^2, D1=x(x+t)-c^2, D2=(x+t)^2-c^2. Inversion yields the gap t/D1 times [x(x+rho c)/D0-(x+t)(x+t+rho c)/D2]; putting over the common denominator gives c t^2 [c(2x+t)+rho(x(x+t)+c^2)]/(D0 D1 D2), the displayed formula. The four stated rational values and negative gap -1/200 follow, and the covariance eigenvalues are 1/5 and 9/5. Replay proofs from RESULT.md lines 51–97; verify.py is supporting finite rational evidence, not the universal proof or an independent certificate.

## originality

PASS

The nearest prior leader-edge theorem proves inverse-trace supermodularity, i.e. independent equal noise. The inspected indexed records change either what is selected or what is varied. None inspected gives the uniform covariance-sign characterization with necessity for each fixed covariance, or the exact continuous family of two-follower thresholds.

## value

PASS

This characterizes exactly when a common edge-selection diminishing-returns guarantee survives correlated noise, rather than just giving a counterexample. The separation from monotonicity and the exact two-node transition make the condition interpretable and give concrete tests for design assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
