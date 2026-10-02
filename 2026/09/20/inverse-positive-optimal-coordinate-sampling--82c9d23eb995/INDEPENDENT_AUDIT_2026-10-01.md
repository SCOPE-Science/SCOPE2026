# Independent mathematical audit

## correctness

PASS

The exact coordinate minimization gives the expected energy decrement matrix and sharp contraction parameter \(\rho(p)=\lambda_{\min}(P^{1/2}CP^{1/2})\). Let \(q=C^{-1}\mathbf1>0\) and \(S=\mathbf1^Tq\). A Rayleigh quotient with \(P^{-1/2}q\) gives \(\rho(p)\le S/(\sum_i q_i^2/p_i)\le1/S\), with equality in Cauchy--Schwarz only at \(p_i=q_i/S\). At that sampling, \(P^{1/2}CP^{1/2}\) has the claimed eigenpair, while its inverse is nonnegative and has a positive eigenvector at eigenvalue \(S\); Perron--Frobenius/Collatz--Wielandt therefore makes \(S\) the spectral radius of the inverse, proving the candidate eigenvalue is the minimum and establishing optimality. The tridiagonal Poisson inverse gives the stated parabolic probabilities and \(12/\pi^2\) asymptotic improvement. The deposited numerical script only corroborates these analytic steps.

## originality

PASS

The primary optimal-design framework does not state the audited inverse-positive E-optimal endpoint formula, and no prior research-record hit supplied it. Residual historical-equivalence risk remains in matrix-scaling/optimal-design literature.

## value

PASS

The theorem gives a closed-form unique optimizer for a natural inverse-positive SPD class and a concrete Poisson sampling law with a sharp asymptotic gain over uniform sampling. It resolves a motivated fixed-sampling optimization problem rather than proposing an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
