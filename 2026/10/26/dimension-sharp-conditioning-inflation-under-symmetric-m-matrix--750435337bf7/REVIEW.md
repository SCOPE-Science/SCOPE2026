# Independent mathematical audit

## correctness

PASS

The strictly convex objective (x^T A x)/2-sum(log x_i) is coercive since the quadratic dominates d log||x||, and its interior sublevel sets are bounded away from a zero coordinate. Its unique critical point satisfies Ax=x^(-1). With lambda_-,lambda_+ the extreme eigenvalues, summing the unit row equations gives ||x||^2<=d/lambda_-, while the Z-matrix signs imply 1<=A_ii x_i^2<=lambda_+ x_i^2. These prove the spread bound. The signs and row sums give XAX=I+L for a positive-weight graph Laplacian, so its minimum eigenvalue is 1 also in reducible cases; the congruence norm bound gives the maximum at most dK. For the star, the span of hub and uniform leaves has unscaled eigenvalues 1±c and the leaf-contrast space has eigenvalue 1. The two row equations yield t^2-gamma_m t-1=0; evaluating the polynomial at sqrt(m)/c gives m(1-c^2)/c^2>0, so the positive root has q_m>0 and t>1. The scaled star is I plus the uniform-weight star Laplacian with edge weight c t/(sqrt(m) q_m), giving exactly the eigenvalues 1, 1/q_m on leaf contrasts, and (1+t^2)/q_m-1. Then t/sqrt(m) tends to c and q_m tends to 1-c^2, yielding both claimed constants. The proof requires fixed K>1 for a nonzero sharpness coefficient; K=1 and d=1 pose no problem for the inequalities.

## originality

PASS

The signed row-sum congruence objective, scaling algorithms, and use of related star inputs are not new. The supported remainder is the pair of universal dimension-order bounds with a simultaneous sharp fixed-input-condition-number witness, including its final balanced spectral conditioning. None of the inspected scaling objectives or algorithmic bounds supplies that theorem.

## value

PASS

A unique normalization selected to give a well-structured matrix need not be a good conditioning transform. The example keeps the input condition number fixed at any prescribed K>1 and simultaneously forces sqrt(d) scaling spread and linear balanced conditioning, so the loss is not explained by a nearly singular input. Matching upper dimension powers and explicit asymptotic coefficients answer a concrete limitation of this specific balancing operation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
