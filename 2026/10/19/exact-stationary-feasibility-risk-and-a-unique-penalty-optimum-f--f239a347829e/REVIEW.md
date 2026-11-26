# Independent mathematical audit

## correctness

PASS

The repaired claim retains the scalar stochastic theorem, corrects the source comparison (the source uses run-constant, horizon-dependent parameters, not an iteration-indexed diminishing schedule), and credits the already-known deterministic boundary. Reconstructed the affine scaled matrix and Schur conditions: its quadratic factor has q(1)=t and q(−1)=4−3t with constant term 1−t; the remaining eigenvalue is 1−α. At and above 4/3, exactly one simple real eigenvalue is ≤−1 and the others have modulus less than one. Independent noise contributes a sum of squared first-coordinate impulse coefficients; the stated controllability and observability determinants t and −α make the dominant coefficient nonzero, so the risk actually diverges, including at equality. For the variance, the normalized momentum variance is α/(2−α), and the two cross terms come from a linear system with determinant α²+(1−α²)t. Stationarity of λ/η, whose increment is t times the next primal iterate, gives C₁₂=tC₁₁/2. Combining that with the next primal variance yields the stated risk, with physical scale σ²/η². Independently checked the strict log second derivative by comparing 3/(4−3t) with (1−α)/(2−α−(1−α)t), and the signs at 2/3 and 1. The logarithmic derivative extends continuously in α on the closed bracket; its only zeros at the endpoint parameters are the stated limits. The optimizer holds at fixed η and α while varying β/η. The repaired auxiliary files correct garbled parameter notation, checker filename, and the description of covariance checks; the checker was inspected, not executed.

## originality

PASS

Pass for the repaired forced scalar feasibility-risk and penalty-optimum theorem. The sharp deterministic 4/3 block threshold, including the eigenvalue −1 at equality, has exact equivalent prior coverage in scalar bilinear Chambolle–Pock and is no longer treated as an independent contribution. The forced stationary risk and its optimizer are not supplied by the strongest inspected deterministic or stochastic literature. Neither the MALM recurrence nor discrete Lyapunov methodology is claimed new.

## value

PASS

This is the smallest equality-constrained model in which feasibility, a dual state and filtered gradient noise all interact. The exact stationary calculation answers how to choose the penalty against persistent oracle noise, including a strictly interior optimizer with different limits at slow refresh and near-unfiltered noise. It also separates a noiseless spectral threshold from actual divergence of forced feasibility variance. The value is in that tuning distinction and explicit risk, not in renaming the known 4/3 boundary or in extrapolating a scalar optimizer to general MALM.

The dated certificate retains the supplied scientific assessment, sources and limitations.
