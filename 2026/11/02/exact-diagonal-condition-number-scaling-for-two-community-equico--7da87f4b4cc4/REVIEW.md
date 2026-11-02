# Scientific review

## Correctness
PASS. The stated strict positivity and Schur-complement condition make the original matrix positive definite. A two-community Fourier-type decomposition gives the quotient eigenvalues and two fluctuation eigenvalues; the diagonal semidefinite feasibility formulation permits averaging over community permutations. A Perron-positive top eigenvector forces *every* globally optimal diagonal scaling to be community-constant. The three monotone spectral branches then yield the explicit clipped minimizer and prove its uniqueness, including equality and absent-crossing cases. The symbolic rational example and verified 17,287 finite assertions are supplementary checks, not substitutes for the proof.

## Originality
PASS, with residual literature risk. Braatz and Morari (1994) give general convex optimal-conditioning machinery, and Takapoui and Javadi (2016) discuss equilibration heuristics; neither inspected source states the present two-community closed-form phase rule. Kolotilina (2004) concerns a larger class of full within-block congruences, and its optimum does not directly solve the restrictive positive-diagonal objective. The one-hub subclass has a singleton group and does not contain two independent fluctuation subspaces. Shapiro (1985) describes unnamed exact special cases but its complete text was inaccessible, so the strongest remaining risk is unverified earlier specialist coverage; neither a search miss nor this partition proves uniqueness in the literature.

## Mathematical value
PASS. The explicit preconditioner applies uniformly over all dimensions and five continuous/discrete parameters of a natural two-community correlation model. It separates quotient balancing from first- and second-community fluctuation constraints, includes a rigorous unrestricted uniqueness theorem, and identifies an infinite family in which the optimal scaling saturates while the best condition number increases. This contrasts sharply with the usual unit-diagonal Jacobi heuristic.

## Closest sources and limits
Takapoui--Javadi, arXiv:1610.03871v1; Braatz--Morari, DOI 10.1137/S0363012992238680; Kolotilina (2004), DOI 10.1023/B:JOTH.0000026285.08558.74; Shapiro (1985), DOI 10.1137/0722005 (full-text coverage uncertain); Kolotilina (2002), DOI 10.1016/S0024-3795(01)00412-8 (abstract only). Only real, strictly positive correlations, both community sizes at least two, and symmetric positive diagonal congruence are proved. Independent replication and broader prior-literature review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
