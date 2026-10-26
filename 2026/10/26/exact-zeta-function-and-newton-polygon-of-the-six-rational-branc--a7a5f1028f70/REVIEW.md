# Review of the exact arithmetic of the split genus-seventeen Humbert–Edge curve

## Correctness
PASS. The five independent square classes give the full \\((\\mathbf Z/2\\mathbf Z)^5\\) cover, smoothness follows from the explicit Jacobian minors, and Riemann–Hurwitz gives genus \\(17\\). Fifteen elliptic character quotients have traces \\(\\pm2\\) by rational two-torsion and Hasse bounds, with multiplicities determined exactly by the \\(16\\) rational points. The genus-two quotient \\(y^2=t^5-t\\) has \\(6\\) points over both \\(\\mathbf F_5\\) and \\(\\mathbf F_{25}\\), forcing \\(L(T)=(1-5T^2)^2\\); its Cartier–Manin matrix is zero. The prime-to-characteristic decomposition then determines all stated invariants. Exact enumeration in `verify.py` corroborates all first three field counts. No infinite statement rests solely on samples.

## Originality
PASS with historical-literature risk. The classical Humbert–Edge family, six-branch description, and genus-seventeen decomposition are expressly prior knowledge. The 2019 decomposition theorem does not provide the particular \\(\\mathbf F_5\\) branch model's elliptic trace census, complete zeta polynomial, or \\(5\\)-rank/\\(a\\)-number. The 2021 type-five geometry and 2023 generalized Fermat decomposition do not give these field-specific computations. Targeted searches for equivalent Kummer/generalized Fermat descriptions, stronger arithmetic classifications, exact zeta tables, and published mathematical findings found no matching result. Residual risk: a specialized computation not indexed by these sources might give the same zeta polynomial.

## Value
PASS. Over the smallest odd field with six rational points of the base projective line, the entire six-branch configuration is forced. For the resulting natural coordinate-split genus-\\(17\\) cover, the exact Frobenius factorization yields a particularly constrained near-ordinary Newton polygon, distinguishes superspecial genus-two behavior from the ambient Jacobian, and solves all extension-field point counts. These exact values are not numerically supplied by the known abstract decomposition.

## Limitations and relationship to literature
The result treats a fixed split model, not arbitrary twists or all characteristic-five moduli. The 2019 decomposition and 2021 six-point model framework were used as prior results. The original books and potentially unindexed computational literature have not been exhaustively verified. Reproducibility code is finite corroboration, not independent proof of infinitely many point counts.

Self-review: passed. Independent audit: not yet performed.
