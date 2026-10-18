# Independent mathematical audit

## correctness

PASS

The exact E_3 distance coefficients follow from the Johnson J(n,3) intersection-number eigenvector recurrence; applying P_j(d) gives four rational eigenvalues for K=E_3∘E_3. The n−7 substituted cubic numerators and exact rational gap factors are strictly positive for every integer n≥7, making K positive definite; since all other E_j∘E_j are positive semidefinite, the full Cesàro mixing matrix has rank binom(n,3). At n=6 complement pairs force rank≤10; K has positive modes of multiplicities 1+9=10, hence exactly rank10. Inspected RESULT.md and verify.py; checked exact symbolic identities and positivity logic independent of finite n=6,7,8 matrix examples. Conventions: unweighted adjacency Hamiltonian, continuous-time infinite Cesàro average, n≥6, no assertion for higher k.

## originality

PASS

The standard average-mixing Schur-square identity and complete Johnson association-scheme eigenmatrix are acknowledged prior work, not novel results. The audited contribution is the exact sharp rank switch and a single-projector strict-positive lower-bound certificate specialized to J(n,3). Searches and inspected general treatments did not yield this all-n strict-positivity corollary. Risk: a general Krein-positive result, e.g. one implicit in Johnson scheme linearization formulae, may yield the same fact.

## value

PASS

A sharp infinite-family boundary n=6 versus n≥7 for the quantum-average-mixing rank addresses a meaningful explicit family of the open primitive-distance-regular-graph rank problem. The strictly positive lower bound is a quantitative spectral stability certificate, beyond an isolated numerical rank computation; it need not solve the general open problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
