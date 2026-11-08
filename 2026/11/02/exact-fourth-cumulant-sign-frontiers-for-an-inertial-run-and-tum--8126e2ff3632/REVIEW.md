# Independent mathematical audit

## correctness

PASS

PASS: Generator identities for M_ij and L_ij follow from telegraph flip rate u/2 (decay of sign mean u) and stable damped linear flow. An independently written SymPy moment-equation solver for mixed moments through degree four reproduces exactly M20=(1+u)/[k(k+u+u^2)], M02=u/(k+u+u^2), and both rational Kx=-6Px/(kH), Kv=-6uPv/H. For u>0, Bv,Cv>0 and d(Pv/k^2)/dk=-9-Bv/k^2-2Cv/k^3<0 with opposite endpoint signs; unique simple Kv crossover. For Px, Bx,Cx>0, leading coefficient 12-9u gives no positive root at u<=4/3 and a single simple root when u>4/3 via d(Px/k)/dk=12-9u-Cx/k^2<0. The exact variance scaling yields the stated k->infinity standardized excess kurtoses. Finite rational substitutions are corroboration, not the root-count proof.

## originality

PASS

Best-of-knowledge originality of the stated final claim (not preceding methods or special cases), with explicitly bounded access and implication risks. Equivalent formulation means stationary fourth cumulants or excess kurtosis of this same dichotomous telegraph oscillator; changing normalization preserves signs. The generic stationary recurrence is prior art, but it does not state or trivially imply the global strict polynomial root count without further analysis.

## value

PASS

PASS: Defines a mathematically motivated sharp threshold u=4/3 and separate single-crossing phase structure for fourth cumulants of one canonical inertial telegraph oscillator. Unlike routine moment substitution, the parameter-global one-root and no-root regimes exclude spurious positive oscillations and distinguish velocity and position, a useful exact boundary for non-Gaussian stationary statistics; modality and Gaussianity are NOT inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
