# Scientific review: strict likelihood geometry for partially informed matching

## Correctness — PASS

The model has exact conditional law \(\Pr(K=k\mid L=\ell)=D_{n-k}/[(k-\ell)!(n-k)!]\), independently checked by direct enumeration for small sizes. The complete positive-matrix factorization uses established total nonnegativity of Pascal's binomial matrix and strict generalized Vandermonde minors; an explicitly positive Cauchy–Binet summand proves all orders, without extrapolating from numerical checks. The coefficient identity with \(L_k^{(n-k)}\), Rodrigues orthogonality and positive simple roots gives the exact negative second derivative. Boundary cases \(n=1\), forbidden count \(n-1\), and parameter endpoints are excluded or handled separately. The included checker passed 2,563 exact assertions; the general proof is analytic.

## Originality — PASS, qualified

The closest direct model and mass function are due to O'Neill (arXiv:2112.12442, 2021; journal DOI 10.1007/s11009-023-10067-6, 2023). The accessible complete journal article discusses likelihood-ratio monotonicity and asserts unimodality, so neither is claimed as new. The reviewed text does not establish strict positivity of minors of all orders or the positive-Laguerre-root likelihood factorization and quantitative curvature identity. NIST DLMF §18.2 and Galvin–Pacurar (arXiv:1807.08658) supply classical ingredient theorems; the claim applies them to a specific statistical kernel not covered explicitly in the inspected sources. Historical priority is qualified: older total-positivity and combinatorial likelihood literature may imply the same application, and absence from searched sources is not a uniqueness certificate.

## Value — PASS

The higher-order strict determinant theorem strengthens a previously stated order-two likelihood-ratio property, while the independent strict log-concavity theorem upgrades an asserted unimodality into an explicit Hessian certificate for every possible observation and sample. This gives exact global curvature for stable one-parameter likelihood optimization and rules out interior competing modes; it is motivated by the source paper's actual hypothesis-testing and inference problem, not by an artificial parameter slice or a recomputation of a probability table. The structural link with the rectangular-board rook/Laguerre polynomial makes both conclusions independently checkable. The work does not claim new confidence interval coverage or a new probability model.

## Residual risks and limitations

The result concerns a common recognition probability, uniform completion of the remaining permutation, and observed total fixed-point counts. It excludes the degenerate \(n=1\) model, impossible count \(n-1\), and boundary parameter matrices from strict positivity. Generic classical total-positivity and orthogonal-polynomial theorems are powerful enough that a more obscure prior explicit application cannot be ruled out. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
