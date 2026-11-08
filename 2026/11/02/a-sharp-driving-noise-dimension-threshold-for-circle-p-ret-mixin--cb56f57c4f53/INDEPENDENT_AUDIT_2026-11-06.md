# Independent mathematical audit

## correctness

PASS

For r redundant identical fields sigma_j=r^-1/2 ∂theta on circle, the exact p-Ret angular step is sqrt(rh)U with U first coordinate of uniform S^{r-1}, same covariance generator 1/2 ∂theta². Fourier characteristic function rho_{r,k}=E cos(k sqrt(rh)U) has the stated Bessel integral, including cos(k sqrt h) at r=1, J0(k sqrt(2h)) at r=2 and sinc(k sqrt(3h)) at r=3. For r>=2, U has an interval density, so |rho_{r,k}|<1 for each nonzero k and rho->0 by Riemann–Lebesgue; supremum q<1 is achieved and ||P^n−Π||=q^n. Bessel decay O(|k|^{-(r−1)/2}) makes the two-step point-start density L² (sum |rho|^4<∞), yielding exponential total variation convergence and bounded inverse of I−P on mean-zero L². At r=1 cos multipliers have supremum modulus 1 by rational resonance or irrational Kronecker density, point-start laws atomic hence TV=1, rational cases nonergodic and irrational cases strong L² but no norm mixing; small divisors exhibit continuous mean-zero forcing with no L² Poisson solution. Inspected actual check.py; independent reasoning verified the sphere-coordinate moment E U²=1/r and r1/r3 special multipliers. The r=1 fair sign is a mathematical edge case, not an assertion of paper sampler implementation.

## originality

PASS

Qualified PASS for the new cross-factorization comparison of the same generator under the p-Ret *discrete* scheme, not for classical circle random-walk Fourier facts alone. Original He et al. paper establishes p-Ret and finite-time weak/RQMC error; its accessible abstract does not claim the sharp fixed-step r=1 vs r>=2 ergodic/Poisson threshold. Full original manuscript inaccessible through arXiv HTML in this run; an implicit long-time observation remains a priority risk.

## value

PASS

Sharp qualitative non-invariance of long-time mixing under redundant noise factorization despite exactly equal limiting heat generators: threshold at two driving coordinates, with norm mixing, total variation and discrete Poisson solvability consequences. It is a motivated numerical-analysis warning, not a restatement of isolated irrational rotations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
