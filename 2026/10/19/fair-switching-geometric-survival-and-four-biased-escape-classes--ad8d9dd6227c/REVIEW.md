# Independent mathematical audit

## correctness

PASS

For independent fair digits and independent hole choices at each observation, the allowed weight on edge ij is w_ij, one of 1-p, p, or 1. Summing weighted digit paths gives S_n=(1/2,1/2)(w/2)^n(1,1)^T, including n=0, and S_1=3/4. At fairness the two same-type cases have constant row sum; in a mixed pair the two decreased entries share a row or column, making the matrix rank one with trace 3/4. For bias, complementation and transpose preserve survival, or one can directly compute trace and determinant of every orientation. Cayley–Hamilton then gives the table of recurrences, the generating functions, and S_2. The S_2 gaps factor as (2p-1)(1-p)/8, (2p-1)^2/8, (2p-1)(1-p)/8. The resultants are nonzero on the whole open bias interval: the A/B and C/D polynomial differences have sole zero at (2-p)/2, and the B/C difference has sole zero at 1-p+p². Substitution gives the reported resultants. At p=3/4 the listed radicals satisfy λA>25/32>λB>3/4>λC>7/10>λD by squaring positive rational bounds. Continuity and nonvanishing resultants give strict ordering everywhere stated. Positivity of the matrices, starting and ending vectors gives nonzero Perron contributions and the survival-root limits. Unequal S_2 off fairness and hole-label interchange prove uniqueness of the all-pair fair law. The simultaneous-relabeling language in the proof does not by itself identify the two opposite loop/cross orientations, but transpose or direct substitution does; it does not alter any claimed result.

## originality

PASS

The known annealed transfer operator covers exactly this kind of two-hole ensemble. Credit that method and the earlier uniform-leak calculation. The distinct result is the complete two-cylinder classification: exact fair universality without pointwise constant leakage, and the explicit four different biased sequences together with strict orderings on the full bias interval. None of the inspected stronger or equivalent formulations supplies these conclusions as a stated result or direct instance of the existing constant-leak law.

## value

PASS

Length two is the first binary cylinder scale where adjacent observations share a digit. At that scale the result separates an exact ensemble survival law from a constant spatial leakage law, and shows that its degeneracy is genuinely broken by bias into different finite-time and asymptotic profiles, with strict order throughout the whole bias interval. This is a natural complete test case for annealed escape, not merely a computation of one sample spectral radius.

The dated certificate retains the supplied scientific assessment, sources and limitations.
