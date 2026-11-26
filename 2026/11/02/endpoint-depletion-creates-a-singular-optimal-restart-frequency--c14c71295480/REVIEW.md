# Independent mathematical audit

## correctness

PASS

The absorbing problem has generator D d²/dx² and both endpoint data 1 for the discounted exit transform. Averaging the two exponentials over the symmetric beta law gives the stated F, and renewal with a fresh independent start gives (1-F)/(rF). In the normalized mean, reciprocal Laplace asymptotics give A_alpha k^{alpha-1}[1+alpha(alpha+1)/k+O(k^{-2})]-k^{-2}; the leading term dominates for alpha>-1. At alpha=1, integration gives F=12(k-2 tanh(k/2))/k³. The strict bound reduces to (3+z²)sinh(z)-3z cosh(z)>0, whose derivative is z(z cosh(z)-sinh(z))>0 for z>0. The r=0 mean is larger too. The exit moment boundary equations give T'(0+)=m_1²-m_2/2, with numerator proportional to p(2p²-p-7), p=alpha+1; this supplies a strict improvement at a small positive rate when 1<alpha<alpha_c, and divergence at infinity supplies attainment away from both endpoints. As epsilon=alpha-1 tends to zero, the trial point k=1/epsilon has limiting mean 1/12 in units L²/D; any bounded sequence of minimizing k would violate the strict critical inequality by joint continuity. The expansion and its derivative are uniform near alpha=1: split the beta integral at y=1/2 and Taylor-expand (1-y)^alpha at zero, with a uniform remainder, also after multiplication by y for the derivative. Stationarity then gives epsilon k plus alpha(alpha+1)(alpha-2) tending to zero for every minimizing k, so epsilon k→2. The linear expansion of A is governed by psi(2)-2psi(4)=gamma_E-8/3; alpha(alpha+1)/k=epsilon+o(epsilon) and k^epsilon=1+epsilon(log(1/epsilon)+log 2)+o(epsilon), giving the displayed constant. Independent quadrature of the Laplace transform and its derivative reproduced the local stationary branch and normalized asymptotic corrections; it was not used to prove global optimality. Replay: python3 /workspace/branches/audit_kernel_checks.py.

## originality

PASS

The general arbitrary-density ring formula and frequent-reset framework already cover the exact mean and the mechanism behind the leading large-frequency scaling. The supported distinct result is the beta endpoint-depletion optimization transition, in particular escape of every global optimizer with the 4/epsilon² law and the two corrections to the optimum value. The strongest inspected ring paper optimizes a two-site law, not this continuous family; this assessment does not claim historical priority.

## value

PASS

This gives a controlled transition from an unattained positive infimum to finite-rate optimization with an escaping scale. Distinguishing a true global optimizer from a local stationary branch and quantifying the optimized value near the threshold are useful in comparing ways of depleting reset mass at a target. The standard renewal mean alone would not merit this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
