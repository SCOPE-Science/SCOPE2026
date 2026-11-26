# Independent mathematical audit

## correctness

PASS

Each affine inverse word maps [0,1] into itself, has a unique fixed point a/(1-s), and contributes |s|(1-a/(1-s)) to the strict comparison; the ties form a finite set. Expanding 1/(1-s) and factoring over letters gives A_k=p^(k+1)+(-1)^k q^(k+1) and B_k=(-1)^k q^(k+1). The k=0 term cancels the constant, k=1,2 give the two stated convolutions, and the absolute k>=3 tail is at most n sigma^(n-1) times sum |B_k|=q^4/p. This estimate is for every lag, not a uniform estimate over all p. I checked the partial fractions and beta-alpha=q(2-3p), beta+alpha=p(3p-1), and sigma<beta. At 1/3 the coefficients -1/6 and 2/21 are both needed; at 2/3 the equal-mode convolution gives (n/3)3^(-n) and the other retained terms give (3^(-n)+(5/27)^n)/4. Locally 3 sigma stays below 1, so the remainders vanish in both rescalings. Taylor expansion gives the stated parity-dependent exponentials at 1/3 and the divided difference at 2/3, with the exact resonant convolution at lambda=0. No even-lag sign at the leading zero is asserted. In the symmetric case, grouping k=2j,2j+1 sums the full series as a geometric series in 4^(-n) for n>=2. Direct forward integration checks W_1(p)=p/[2(2-p)] and W_2(1/2)=1/30. Read the frozen rational checker and its recorded output; neither was used as proof or executed during review.

## originality

PASS

The supported distinction is the evaluated same-orbit two-time probabilities with explicit error and critical windows. The same skew tent family and general ordinal and periodic-point frameworks are prior. No inspected statement establishes the lag spectrum or the two windows.

## value

PASS

This is a natural two-time statistic for a deterministic stationary map. Separating a sign-changing competition from a positive resonance, with a uniform-in-lag bound and different critical-window profiles, explains why rates and parity can change even in this simple full-branch family. The exact symmetric case supplies a useful benchmark, not the sole contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
