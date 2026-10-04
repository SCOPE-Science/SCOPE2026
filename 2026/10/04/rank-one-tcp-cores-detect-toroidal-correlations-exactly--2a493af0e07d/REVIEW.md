# Review

## Correctness
PASS. The proof starts from the stated TCP factorization and uses the rank-one identity \(J_d=\sum_k z_kz_k^*\) to force every \(z_k\) into \(\operatorname{span}\{\mathbf 1\}\). The coordinatewise modulus identity then converts the third TCP factor into a convex combination of unimodular rank-one correlation matrices. The converse is exactly the toroidal TCP-core construction. Positive scaling connects \((J_d,J_d,Z)\) to \((J_d/d,J_d/d,Z/d)\). The DOC endpoint reduction follows from \(r_1=1\), \(s_1=4\), \(M_1=J_4\), together with the published DOC EB/TCP equivalence. The explicit \(Z_*\) is checked as a rank-two Gram correlation matrix, and its extremality is proved by eliminating every Hermitian face perturbation.

## Originality
PASS. The recent source proves that its family is non-EB for \(a\ne1\) but leaves \(a=1\) outside that conclusion; its toroidal-core lemma supplies only the sufficient direction at the endpoint. The earlier LDOI/TCP paper likewise gives sufficiency for \(X^{(3)}_{(J_d,B,C)}\) when the coherence correlations lie in the convex hull of rank-one correlations, but no converse specialized to \(B=J_d\) was located. The mixed-unitary Schur literature characterizes the toroidal correlation set itself, not the TCP necessity proved here. Searches using TCP, LDOI separability, rank-one core, all-ones core, toroidal correlation, mixed-unitary Schur, and the exact endpoint parameters found no covering theorem. Residual risk remains that an older equivalent statement exists under terminology not captured by the searched indexes.

## Value
PASS. The endpoint \(a=1\) is the unique parameter value excluded by the recent source's non-EB argument, so its status is a natural structural gap rather than an arbitrary slice. The iff theorem shows that the endpoint genuinely bifurcates according to a standard, independently meaningful convex set of correlation matrices, and the explicit extreme rank-two witness proves that PPT non-EB channels occur exactly at the omitted endpoint. The general \(d\)-dimensional rank-one-core equivalence is reusable beyond this one family.

Closest literature: arXiv:2609.32979v1, arXiv:2010.07898v2, and arXiv:2306.04077v1. The principal limitation is that the result does not extend the iff classification to general population cores or resolve the full four-dimensional PPT-squared problem.

Same-model review: passed. Independent audit: not yet performed.
