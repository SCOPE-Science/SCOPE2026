# Independent mathematical audit

## correctness

PASS

For iid uniform circle points the cyclic spacings have Dirichlet(1,...,1) law. Exact moments of U_k=sum D_i^k imply sigma_{33}=360, sigma_{35}=28800, sigma_{55}=3254400, and the positive Schur complement 950400. Taylor expansions S=pi-(pi^3/6)U3+(pi^5/120)U5+O_L2(n^-6), A=pi-4(pi^3/6)U3+16(pi^5/120)U5+O_L2(n^-6) justify the exact quadratic variance minimizer. Independently checked rational arithmetic establishes n^2(lambda*-1/3)->16 pi^2/3; optimized n^9 variance ->1056 pi^10 versus known fixed 3616 pi^10; determinant identity for Cov(S,A) yields n^4(1-Corr)->297 pi^4/10. Variance(B)>0 because B=A-S is nonconstant on the open gap simplex for each n>=3; no MSE or unbiasedness claim.

## originality

PASS

Fixed 1/3 cancellation and 3616 pi^10 are established in earlier Xu/Wang work; 2023 Wang–Li–Xu has full nonlinear extrapolation and joint CLT tools for U3/U5. In its accessible full article, Lemma 5 and Theorem 18 treat spacing moments and fixed/nonlinear extrapolations involving the circumscribed polygon, not the finite-n population variance optimum of the two inscribed observables or this correlation defect. The three new constants are nevertheless accessible by applying known Dirichlet covariances and a Schur complement; novelty is a specific optimization statement, not new asymptotic covariance machinery. 2018 closely related full article was inaccessible (VPN disconnected). Best-of-knowledge PASS with a strong implication/priority caveat.

## value

PASS

The established 1/3 blend cancels leading fluctuations but leaves residual variance. The natural population-variance optimizer, constrained to the same two observable geometric statistics, reduces the known leading residual variance by 80/113; its n^-2 weight shift and separate correlation decay give exact quantitative covariance geometry. This is a motivated complete two-statistic optimization, notwithstanding that the corrected coefficient contains pi and is not a standalone estimator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
