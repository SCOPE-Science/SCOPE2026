# Independent mathematical audit

## correctness

PASS

At the first zero proposal, the negative feedback derivative is the validation projection onto the training direction divided by the training norm. Conditional on the training vector, the standardized projection has a fixed standard normal law, independent of the chi-square radius; the common sigma/sqrt(b) cancels. Projection yields the stated law and atoms. The second update uses fresh samples; at fixed p>0 the acceptance condition is a one-sided normal test at p sqrt(U_d)/2. Weighting by the true squared displacement multiplies the chi-square density by U_d, exactly d times the chi-square_(d+2) density. At p=0 the tie cannot affect risk; A_d(0)=1/2 is the continuous tail extension, not the actual tie acceptance probability. For d=1, rescale the Cauchy integral by y=eta r; the limiting coefficient is [integral_0^M A_1(y) dy+M A_1(M)]/pi, and integrating the t_3-ratio tail using (p arctan(p/2))' gives the printed positive formula. For d=2, r^2 rho_2(r)=1/(2r)+O(r^-3) above r=1; the Lipschitz tail A_2(eta r)=1/2+O(eta r) up to r=M/eta changes the clipped logarithmic contribution only by O_M(eta^2), as does the saturated tail. Above d=2 the clipped risk is dominated after eta^-2 rescaling by (R_d)_+^2, of mean 1/[2(d-2)]. Replacing the acceptance factor by one checks all proposal constants. These arguments verify RESULT.md lines 55–109 at fixed M,b,sigma,d. The self-review's 70 finite checks are reported in VERIFICATION.md; check.py was inspected, not executed.

## originality

PASS

Qualified pass for the exact accepted two-update diagnostic and its sharp dimension- and cap-dependent coefficients, not for the algorithm, Student-ratio identity, or chi-square size bias in isolation.

## value

PASS

A noisy validation null step is designed to protect the primal iterate, so its exact residual risk at a noninterpolating optimum is a natural diagnostic. Even when larger batches reduce this risk by 1/b, they do not stabilize the normalized feedback law. The critical dimensions and exact factors quantify how the safeguard and cap modify the risk, separating a heavy-tail boundary layer from a finite-moment regime. This is a specific mechanism, not a claim about eventual convergence or a new optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
