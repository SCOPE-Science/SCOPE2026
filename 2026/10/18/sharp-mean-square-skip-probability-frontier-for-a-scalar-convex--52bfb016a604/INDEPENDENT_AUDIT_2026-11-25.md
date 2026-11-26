# Independent mathematical audit

## correctness

PASS

Substituting the two quadratic prox maps into Algorithm 5 gives the frozen M0 and M1, including the 1/p correction. Independently checked the claim's drift and W determinant with exact integer arithmetic: put A=pW and U_i=4p M_i. Each entry of 16p²(A−2pD I)−(1−p)U0^T A U0−p U1^T A U1 has degree at most six and vanishes at p=1,…,7. The determinant identity for A has degree at most five and likewise vanishes at those nodes after subtracting 4p²(3p+1)(15p²+10p+23). Evaluation outside the probability domain is only polynomial identity checking. This verifies the all-p algebra, not a finite-horizon extrapolation. The first principal minor and determinant give W positive definite. The unique positive root of D is the stated p*. Independence gives the conditional drift of z^T W z exactly as −2D E||z||² in expectation. Eigenvalue comparability gives an upper geometric bound above p*, a strictly growing geometric lower bound for every nonzero start below p*, and exact conservation with two-sided positive bounds at equality. At p=1 the argument still applies; p=0 is not defined. Also reconstructed the symmetric second-moment lift from (x²,xu,u²); with the same U_i, the cleared determinant of I−B is a polynomial of degree at most nine and gives 256p^6D at ten distinct positive integer nodes, verifying the supplementary D/16 determinant formula. The frozen verifier was inspected, not executed.

## originality

PASS

The algorithm and standard second-moment/Lyapunov tools are prior work. The inspected convergence theory and catalogue records do not give this fixed-unit scalar stability boundary, its geometric lower bound for every nonzero initial condition, or its critical conserved energy.

## value

PASS

Fixing the steps as the frequency of a costly proximal update varies is a concrete tuning question. This canonical scalar case isolates the 1/p correction and supplies a sharp test of the gap between the known sufficient bound and actual stability, including a rigorously unstable region and a genuinely bounded nondecaying critical case. It is a useful benchmark and counterexample to unconditional fixed-step skipping rather than a general convergence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
