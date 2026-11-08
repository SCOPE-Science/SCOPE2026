# Independent mathematical audit

## correctness

PASS

For the continuous-time tight-binding walk from +R, summing the Bessel occupation probabilities yields the finite nonnegative kernel c_R(t)=J0^2+2 sum_{j=1}^{R-1} Jj^2+JR^2 and 1-c_R(t)=JR^2+2 sum_{j>R} Jj^2. The conditional reset sign leads to scalar renewal F=e^{-lambda t}c+lambda(e^{-lambda .}c)*F. For fixed R, c~2R/(pi gamma t), so positive C_R(q) diverges at q downarrow0 and lambda C_R(lambda)<1, yielding unique q in (0,lambda). Exponential tilting gives a nonlattice probability renewal kernel with finite mean; key renewal theorem gives sharp A=1/(lambda^2 int t exp(-qt)c(t)dt) and positive gap lambda-q. Since c_{R+1}-c_R=JR^2+J_{R+1}^2>0, q grows and gap decreases in R. Small-t Bessel expansion and large-t logarithmic Laplace asymptotic give respectively the stated binomial strong-reset power and weak-reset lambda log(gamma/q)->pi gamma/(2R). Independent Bessel quadrature for R=1,2,3 at lambda=gamma=1 reproduced q=(.65354089123,.91552188219,.97483404609) and prefactors (1.14595260285,1.11201786909,1.05398549492).

## originality

PASS

Acharya–Gupta fully inspected source studies the SAME conditional two-site reset tight-binding dynamics, general site occupations and stationary distribution; these are definitively prior. The primary text does not explicitly establish the unique positive sign-memory exponent and prefactor, strict distance monotonicity for all R, or both sharp asymptotic constants. Its general transforms may permit derivation of the new result, creating a significant qualified priority risk, but merely being derivable after nontrivial renewal/Bessel analysis does not itself make the precise theorem previously stated. Perfetto supplies general conditional renewal machinery, Rose spectral shift for unconditional resets: neither inspected statement directly dominates this sign-sector law.

## value

PASS

For a physically natural reset-distance parameter, the theorem determines the exact slow memory mode and its amplitude rather than just numerical relaxation, proves a strict monotone rate hierarchy, and identifies both strong-reset Zeno power and exponentially small complementary root under weak resetting. These are reusable exact invariants for the specified conditional quantum renewal process; not a routine normalization or merely a finite simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
