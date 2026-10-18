# Independent mathematical audit

## correctness

PASS

A k-digit unpatterned integer contains no 1. Split into E: gcd(n,210)=1 and three mutually exclusive F_p classes excluding one more prime digit p=2,3,7 under their congruence conditions (nu2=1, nu3=1, or 7|n). Counting fixed first/last digits and equidistribution of free middle digits modulo 21 and 63 yields E=(96/7)9^(k-2)+O(rho^k), F2=(3/32)8^k+O(rho^k), F3=(1/24)8^k+O(rho^k), F7=(1/48)8^k+O(rho^k). Their 8^k coefficients total 5/32. Every other unpatterned number omits 1 plus at least two other digits, O(7^k). Fourier inversion has nontrivial character magnitude theta<8 for each required alphabet/modulus, in particular theta(A,21) is about 6.251 and theta(A3,63) about 7.682; positivity of the secondary coefficient is therefore separated from the error. Independently checked exact counts for k=2..6 and the spectral radii; finite checks do not prove the uniform limit.

## originality

PASS

Campbell introduced the exact digit/divisor property and counted examples but did not give this two-scale asymptotic; Maynard counts a different prime restriction. The four-class decomposition and precise 8^k coefficient are not implications of the statements inspected.

## value

PASS

A natural integer family introduced with finite frequency questions admits a nontrivial asymptotic scale separation. The 8^k coefficient 5/32 quantifies three mathematically distinct prime-adic obstructions, rather than merely supplying a routine leading-density constant. It is useful for precise enumeration even without a sharp third-order rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
