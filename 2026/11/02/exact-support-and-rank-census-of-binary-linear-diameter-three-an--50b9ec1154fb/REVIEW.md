# Review of exact binary linear diameter-three anticode census

## Correctness — PASS

The proof explicitly defines the counted subspaces and reduces diameter to maximum codeword weight using linearity. Pivot columns give dimension at most three. Weight averaging excludes all large supports except the possible three-dimensional support-five case; the seven-hyperplane incidence contradiction excludes that case. The remaining support-three and support-four counts use full-support hyperplane and generator-column classifications. These exhaust all cases, proving the coefficient table and binomial polynomial for every ambient length, including short lengths. `verify.py` independently enumerates every ambient subspace through dimension seven and confirms each coefficient. Finite checks are corroboration, not the infinite proof.

## Originality — PASS, qualified

The complete primary preprint arXiv:2610.31618v1 was read at its definitions, support decomposition (Proposition 4.3), fixed-diameter theorem (Theorem 4.6), proof and Remark 4.7. It proves polynomiality but leaves the exact diameter-three binary degree and the coefficients unspecified. Previously published optimal linear anticode classifications address maximum dimension, and do not by themselves enumerate all dimension-two and dimension-three subspaces of support four. Searches for aliases (maximum weight-three binary linear codes, diameter-three anticodes, support spectra) and related database records found no equivalent table or all-length polynomial. Residual risk: an older equivalent enumeration may appear with different terminology or in an unindexed source.

## Mathematical value — PASS

This resolves a specific natural uncomputed fixed-diameter instance of a recent enumeration theorem, rather than refining an arbitrary sample. It improves a degree range of three through six to the exact degree four; its key support-five incidence obstruction is structural. The rank-refined count separates six non-extremal maximum-support subspaces from the four maximum-dimension ones and gives an all-length benchmark in coding-theoretic enumerations.

Self-review: passed. Independent audit: not yet performed.
