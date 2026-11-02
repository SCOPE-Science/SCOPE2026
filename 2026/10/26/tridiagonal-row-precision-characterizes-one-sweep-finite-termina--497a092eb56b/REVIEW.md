# Independent mathematical audit

## correctness

PASS

Writing the error update P_i=I-w_i a_i^T/(a_i^T w_i) shows each rank-(n-1) oblique projector can lower rank by at most one. Zero after n updates forces each innovation w_i to lie in the image of the preceding update product, equivalent inductively to orthogonality to all earlier a_j, j<i-1. This is precisely G_{ji}=G_{j,i-1}G_{i-1,i}/G_{i-1,i-1}. Unit lower-bidiagonal B gives BGB^T diagonal and J=B^T D^-1 B tridiagonal; SPD tridiagonal backward LDL factorization proves the converse. For n=3, P_2 P_1 is the orthogonal line projector and Schur-complement geometry yields ||T_3||²=J_13²/(J_11 J_33)<1. Independent exact rational computations show first-sweep zero propagation for AR(1) Gram matrices in dimensions 2..5 and the partial-correlation norm for two non-Markov examples. Quantification excludes positive tolerance and floating-point skips.

## originality

PASS

The original KO paper introduces the same consecutive-row oblique direction, convergence theorem and two-row exact example. It does not in the sections materially read give the all-dimensional iff or the exact three-row operator norm. A precision Markov-chain alias and backward bidiagonal LDL factorization may occur as a specialized direct-solver theorem elsewhere. A general full-memory direct projector does not automatically imply this minimal-memory criterion.

## value

PASS

The exact boundary identifies when one-previous-row memory is sufficient for universal direct solution, includes dense correlated AR(1) rows, and quantifies the first failure case by a partial correlation with a sharp near-one obstruction. This gives structural guidance for solver design beyond ordinary convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
