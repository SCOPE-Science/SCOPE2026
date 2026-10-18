# Independent mathematical audit

## correctness

PASS

For any irreducible real 2x2 A with bc≠0, positive diagonal similarity scales b↦bs and c↦c/s. Left/right eigenvectors for each simple λ give χ² proportional to (|b|²s²+|τ|²)(|c|²/s²+|τ|²); AM-GM yields a common unique minimum at s²=|c/b|, precisely row/column 2-norm balance. For B_t (t>0) opposite off-diagonal absolute values match, so B_t is balanced; its spectrum is {1,2t+1,2t+2}. With D_t=diag(1,1,sqrt(2t+1)), A_t=D_t B_t D_t^-1 has χ_A=(2t+3)/(2t+1), χ_B=sqrt(3(4t²+4t+3))/(2t+1), hence squared difference 8t²/(2t+1)²>0, damage tending sqrt3. Frobenius squared norm difference 8t²/(2t+1)>0. Independently symbolically verified char polynomial, eigenvector identities and all rational comparisons; theorem only for exact balancing.

## originality

PASS

Watkins 2006 already demonstrates harmful balancing in larger numerical examples; James–Langou–Lowery 2014 explicitly distinguish norm reduction from improved eigenvalue conditioning. However inspected primary sources do not prove the exact simultaneous 2x2 optimum or identify 3x3 as minimal harmful dimension with this positive-spectrum analytic family and asymptotic factor. Prior harmful-balancing existence is explicitly credited.

## value

PASS

Exact smallest dimension and a closed-form continuous witness clarify a practical numerical-linear-algebra caveat. The comparison quantifies harm while a matrix norm strictly improves, and the universal 2x2 protection proves minimality—distinct useful structural facts not implied by large-dimensional experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
