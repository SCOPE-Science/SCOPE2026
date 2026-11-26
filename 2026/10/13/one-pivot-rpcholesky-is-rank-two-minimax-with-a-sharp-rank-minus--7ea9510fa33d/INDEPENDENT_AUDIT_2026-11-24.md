# Independent mathematical audit

## correctness

PASS

Minimizing the squared representer error over the weight gives exactly the Schur residual R_j, also for rank-deficient A. The unit-target supremum is outside the pivot expectation, so its value is the top eigenvalue of the mean residual. On range(A), write v_j=A^(1/2)e_j/sqrt(A_jj); the mean is A^(1/2)(I-D)A^(1/2) with D=sum_j p_j v_j v_j^T positive of trace one. In the positive eigenbasis, a bound z on the mean forces D_ii >= (1-z/lambda_i)_+. Their sum being at most one proves the water-filling floor t; the sum is continuous and strictly decreasing to zero up to the top eigenvalue, so t is unique. For each i!=j the trace-one budget gives t >= lambda_i lambda_j/(lambda_i+lambda_j), by adding the two necessary lower bounds on the diagonal budget (or optimizing just those two entries). The RP law has mean A-A^2/S; its i-th eigenvalue is the sum of lambda_i lambda_j/S over j!=i, at most (r-1)t, strictly less for r>2 and finite positive eigenvalues. At rank two the two positive mean-residual eigenvalues coincide with t irrespective of eigenvectors. For a diagonal kernel the simplex relaxation is exact; for diag(M,1,...,1), t=M(r-1)/(M(r-1)+1)<1, the large-coordinate RP risk is maximal for M>=1, and the ratio tends to r-1. No exact general formula for W_* at rank >=3 is asserted. Independent exact replay used a different rank-two Gram example (positive mean eigenvalues 9/7) and diagonal witnesses at ranks 2, 3, and 5; these are checks, not the proof. The frozen verifier's extra nondiagonal rank-three case checks the expectation identity, not the universal minimax inequality suggested by RESULT.md line 131; this is a nonessential overdescription of the test, not a gap in the theorem.

## originality

PASS

The RP law, expected one-step residual and optimal quadrature weights are prior. The supported distinct contribution is minimization of the worst expected squared target loss over every target-independent one-pivot law: the eigenbasis-independent rank-two solution and the sharp rank-dependent gap. No inspected statement provides that comparison; this is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

When the node is drawn before target weights are available, a standard and inexpensive pivot rule can be judged against the best implementable-in-principle target-independent distribution. Exact optimality for every rank-two eigenbasis and a sharp loss that grows with rank answer that natural robustness question; the diagonal witness isolates ill conditioning and supplies an explicit optimal replacement there. This is not just recomputing the known mean residual or changing the units of trace loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
