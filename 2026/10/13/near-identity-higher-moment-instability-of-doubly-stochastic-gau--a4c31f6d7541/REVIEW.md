# Independent mathematical audit

## correctness

PASS

Write S=2(1+rho^2). In the conditional squared norm, multiplying the cross term by the entry-square sampling weight and summing over j yields −2 alpha ||Ax||^2/S; the squared update yields 2 alpha^2 ||Ax||^2/S because both entries in each row are nonzero. The least singular value 1−rho gives the stated theta in (0,1), and iteration, Jensen for orders at most two, and summable Markov bounds followed by Borel–Cantelli establish all the decay assertions. For the two rare choices of weight rho^2/S each, the updated coordinates jointly form W x with W having diagonal 1−alpha and off-diagonal −alpha/rho. The conditional pth moment is at least (rho^2/S) 2^(1−p/2) ||W x||^p. For rho<alpha/(1−alpha) the least singular value is alpha/rho−(1−alpha), giving exactly L_p and a uniform-in-state lower bound at each step. For fixed p>2, L_p tends to infinity as rho tends to zero, while rho<epsilon/(2+epsilon) enforces the strict condition-number bound. This verifies the quantifier order and finite-time finiteness (four finite update matrices). Independent exact arithmetic gave 11/9, 323/404, and 6561/6464 and checked the quadratic-form identity at the rational example on the two basis vectors and their sum.

## originality

PASS

The entry-weighted rule and mean-square convergence are prior results. The inspected fourth-moment Resultary theorem is a close companion, but neither it nor the other sources establishes or entails the joint all-orders, arbitrary-relaxation, near-identity positive-definite result with a uniform-in-initial-state arbitrarily large lower factor.

## value

PASS

The example identifies the threshold order across solver instances: mean-square convergence and almost-sure convergence coexist with arbitrarily fast pth-moment growth for any requested order above two, even when the SPD matrix is arbitrarily close to the identity. This rules out a condition-number-based inference of tail or moment control for this sampling scheme and isolates the concrete cause, rare division by tiny entries, uniformly over initial directions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
