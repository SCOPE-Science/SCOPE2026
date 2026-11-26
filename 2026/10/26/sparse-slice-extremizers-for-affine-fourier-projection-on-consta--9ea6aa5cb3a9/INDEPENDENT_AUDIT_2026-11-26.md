# Independent mathematical audit

## correctness

PASS

The frozen kernel, exact row norm, equality of endpoints, complement symmetry, and asymptotic results check out. The centered-coordinate covariance is scalar on the sum-zero subspace; the absolute row sum attains the infinity norm by choosing that row's signs. Normalized kernel second moment is one, so hypergeometric weak limits pass to absolute moments. Below the sqrt(n) scale the first absolute centered moment is at most 2k^2/n; on that scale factorial moments give the Poisson limit; above it all expected hypergeometric cells diverge and the normal limit applies. Poisson peaks at consecutive half-integers decrease by the strict midpoint integral comparison, so the unique leading peak localizes all smaller maximizing widths. The repaired theorem proves the exact eventual optimizer, not asserted in the original. Within the localization window k(k-1)/(n-1) is strictly between 0 and 1, so only disjoint pairs contribute to the negative part. Dividing the two neighboring positive binomial factors gives the sign polynomial n^2-(2k^2+2k+1)n+3k^3+2k^2+k. Its discriminant 4k^4-4k^3+1 lies strictly between the squares of 2k^2-k-1 and 2k^2-k for k>=2. The smaller root is below n in the window; the larger has floor 2k^2+floor(k/2) and is never an integer, yielding a unique turning layer and excluding ties. This crossing lies inside the window for large n and leads exactly to ceil((sqrt(32n+1)-1)/8). Ran python3 /workspace/repairs/2/check_eventual_width.py: 143 exact full smaller-width scans and 48 exact adjacent transition pairs passed. Independent row-matrix and spot checks also agree with the frozen non-asymptotic formula.

## originality

PASS

Pass for the repaired exact eventual lattice threshold and finite no-ties law. The frozen leading-scale result does not survive as a distinct claim: the first-harmonic record gives all width regimes and the same unique peak, and adding the constant projector changes every norm by at most one. This is demonstrable equivalent asymptotic coverage, not a claim about which record was first. The unoptimized finite affine row expression is standard kernel evaluation and is not credited by itself. The repaired exact threshold instead uses the affine shift to get a different finite adjacent-layer comparison, whose discriminant locates precisely the step relative to integers.

## value

PASS

The finite maximizing cardinality is a natural extremal parameter already motivated by the frozen problem, which explicitly left the discrete optimizer open. The repair turns its scale into a unique exact rounding law and gives the largest norm without an all-width scan. This identifies both sides of every sufficiently large transition and answers when two neighboring smaller widths can tie, information neither the limiting constant nor finite tabulation gives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
