# Independent mathematical audit

## correctness

PASS

For the ordered Krylov basis, sketched MGS produces V=sqrt(ell)R^-1 with positive-diagonal QR of sqrt(ell)Omega. Thus H=RAR^-1, and an independent symbolic calculation gives the exact h13 numerator/(r11*r22*r33). Bartlett QR has r33 chi_(ell-2) independent of C, while denominators r11 chi_ell and r22 chi_(ell-1) have enough inverse moments at p=ell-2. Tonelli proves divergence for p>=ell-2; chi small-ball expansion and dominated convergence give the exact tail constant. Chi concentration gives sqrt(ell)h13=r12-r23+o_P(1) and the normal limit. Sympy independent algebra and chi CDF leading constants k<=4 passed.

## originality

PASS

General randomized Arnoldi/Gram–Schmidt work supplies the algorithm, Gaussian sketching motivation and stability results, while classical Bartlett QR supplies the probabilistic ingredients. The exact unconditional heavy-tail moment cutoff and tail constant for the earliest extra Hessenberg entry of a specific SPD path matrix were not derived by the accessible analyzed sections. This is a qualified exact-distribution contribution rather than a newly invented QR theorem.

## value

PASS

The first above-superdiagonal coefficient h13 is the earliest nontrivial diagnostic of non-tridiagonality in a sketched SPD Arnoldi process. Exact unconditional moment thresholds, tail constant and Gaussian central limit together expose a mathematically motivated stability/noise-model boundary that could matter in finite-sketch error analysis. The 3x3 path matrix is minimal for that phenomenon, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
