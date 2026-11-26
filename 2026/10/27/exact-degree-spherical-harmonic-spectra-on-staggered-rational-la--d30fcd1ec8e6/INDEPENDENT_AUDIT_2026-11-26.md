# Independent mathematical audit

## correctness

PASS

In longitude order the normalized Gram matrix is circulant with displacement entry P_ell((1-c²)cos(πd/N)+(-1)^d c²), by the probability-measure addition theorem. A harmonic of order m occupies discrete frequency (N+1)m+N ell modulo 2N and contributes eigenvalue weight 2N a_(ell,m). The multiplier N+1 has gcd 2 with 2N for odd N and gcd 1 for even N; this gives the claimed alias sums with their zero multiplicities. The Rodrigues coefficients of the k-th derivative, relative to the leading coefficient, are (-1)^j binom(ell-k,2j)(2j-1)!! divided by the product of the j descending odd factors from 2ell-1. Thus every such ratio is 2-adically integral. Since v_2(c)<0, the leading evaluated term has uniquely least valuation (the constant derivative case also holds). This establishes strict positivity at every allowed order, so counting attained residue classes proves the rank formulas and sharp onsets, including degree zero and one degree below each onset. The Gram diagonal is P_ell(1)=1; at N=3, c=1/2, ell=1 the weights 1/4, 3/8, 3/8 give the stated example. Dyadic heights give density. The frozen check.py and check_output.txt were inspected, not executed; the recorded 130 numerical spectral comparisons and 2,520 exact amplitude tests are corroborative only. The conclusion rests on the analytic argument, not on numerical agreement or formal certification.

## originality

PASS

The best verified overlaps cover half-step geometry, Fourier block separation, and related interpolation or conditioning, not the complete fixed-configuration exact-degree spectrum and parity-sharp rank for every degree at even-denominator heights. No priority claim is made for circulant diagonalization, the special-function identities, or the denominator argument in isolation.

## value

PASS

For points that are fixed across degrees, knowing the exact alias weights and the parity-dependent sharp reachability threshold is materially stronger than a generic-rank or cumulative-bandlimit result. The even-denominator criterion gives an explicit dense choice of heights rather than exceptions defined separately at each degree. The spectral formula gives usable multiplicities and eigenvalues while correctly not promising uniform conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
