# Independent mathematical audit

## correctness

PASS

The theorem concerns the normalized ideal algebraic subtraction state as defined, with natural parity after subtraction, not a probability of implementing the filter. A Gaussian overlap with the positive trace-one thermal kernel (1-z)z^N gives the displayed generating function; its number series is analytic about ±1, and the factorially weighted parity is exactly G^(m)(-1)/G^(m)(1). The numerator coefficient sign follows from the common sign of terms with index k congruent to m modulo two in (1+ct-dt²)^(-1/2), and c vanishes exactly at the given threshold. I independently verified the simultaneous coefficient expansion via an arcsine moment: (1+A t)^(-1/2)(1-B t)^(-1/2) generates moments of the arcsine law on [-A,B], for A,B>0. Splitting the signed moment at zero, its positive contribution is B^(m+1/2)/(pi sqrt(A+B)) times the integral of (1-y)^m y^(-1/2)(1-By/(A+B))^(-1/2) over [0,1]; the negative piece is the reflected formula with sign (-1)^m. The beta integral and the O(y) remainder give relative O(1/m) for each magnitude, uniformly when A,B range over a compact positive set. This establishes the additive bound through the parity cancellation without needing a relative bound on the numerator. At +1 the positive branch dominates; division gives the two stated sqrt(R) prefactors using 4vw(alpha+beta)=b+e in the proof notation. Differentiation of half the log-ratio gives -2/sinh(2r), and the uniform error survives geometric-mean rescaling for bounded s. Both bases are <1 for fixed positive nu in the stated domain, and at nu=0 parity is exactly (-1)^m from even input number support. Independent replay `python /workspace/branches/independent_audit_replay.py` uses arcsine quadrature at six high-order test points, not an infinite-order certificate. The scope text's description of the unscaled map a^m rho (a†)^m as trace-decreasing is inexact: its trace factor can exceed one. This does not enter the conditional algebraic theorem, and it supplies no success probability; a physical implementation needs a bounded, appropriately attenuated Kraus operation.

## originality

PASS

Only the sharp large-subtraction-order central parity and its moving-thermal-population boundary layer are credited. The state, exact finite-order Wigner values and photon generating function, and the single-photon threshold are prior art. The closest general asymptotic formulation inspected has a different stated uniformity domain; broader specialist complex Legendre literature may reduce the novelty further.

## value

PASS

For a specified optical observable the exact sign is not enough to characterize the persistence of contrast. The parity-resolved crossover scale and absolute multiplicative contrast distinguish odd sign reversal from the competing positive contributions and the exponential loss at fixed thermal population. The co-scaled profile addresses a natural limit of the known central-negativity threshold, without implying global Wigner positivity, negativity volume or an experimental calibration/error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
