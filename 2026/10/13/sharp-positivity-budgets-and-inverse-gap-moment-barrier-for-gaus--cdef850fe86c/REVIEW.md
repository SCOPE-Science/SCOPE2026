# Independent mathematical audit

## correctness

PASS

Normalize u and orthogonally decompose Au into its mean direction and a residual of norm sigma. The sketch of those two orthonormal directions gives independent normal vectors; the normalized dot product conditional on the first vector is standard normal with a law independent of its chi-square length. This yields the exact location, scale and density. Spectral averaging of (lambda-m)(L-lambda)>=0 gives the stated upper variance; maximizing the variance-to-mean-square ratio gives (L-m)^2/(4mL), with endpoint masses L/(m+L), m/(m+L). The Student lower-tail beta argument reaches ((kappa-1)/(kappa+1))^2 at those masses. The endpoint integral with a=s/2, z fixed, is asymptotic to z^a/(a*sqrt(1-z)); dividing by B(a,1/2) and by 2 gives the stated prefactor. Monotone tails in s and their logarithmic asymptotic give the small-delta limit. For fixed delta the Student-to-normal limit at s/kappa -> c gives Phi(-2*sqrt(c)), and comparison of row budgets at ratios above and below the unique solution gives the second limit. K is bounded away from the spectral poles, including at infinity. Locally its singularity is d_lambda/|x-lambda|+O(1), with positive smooth density, so the stated moment cutoff is for positive orders p; zero and negative powers are trivially finite. The regularized local denominator integrates as 2[1+log(epsilon/h)] for h<epsilon, giving the summed logarithmic coefficient with bounded error. The expectation always averages over the random sketch at fixed problem data, sketch dimension and law. The independent replay `python3 /workspace/review_replay.py 2` uses the s=2 density primitive and recovers probability 1/5 and exponent-zero log coefficient 28/(3*sqrt(10)) for the (1,9) witness. The frozen verifier was inspected, not executed.

## originality

PASS

The exact one-vector Student law and its fixed-direction tail before spectral optimization are prior consequences, not standalone original here. The supported distinct contribution is the exact condition-number-optimized positivity risk and budget analysis together with the all-finite-width inverse-gap barrier and safeguard coefficient for the full shifted operator. The inspected earlier or same-day comparators do not give that classification; a later harmonic paper gives an exactly equivalent fixed-direction negativity envelope under inversion, but does not address the full shifted operator.

## value

PASS

The optimized sign probability and confidence budgets answer a concrete choice of sketch width; the inverse-gap result shows why success in that decision says nothing about making the mean full-matrix condition number finite. The exact logarithmic coefficient characterizes how a common spectral-gap regularization changes that expectation. This distinguishes two practically and mathematically different risks for a natural shift, without asserting typical numerical failure, floating-point performance or an adaptive Krylov guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
