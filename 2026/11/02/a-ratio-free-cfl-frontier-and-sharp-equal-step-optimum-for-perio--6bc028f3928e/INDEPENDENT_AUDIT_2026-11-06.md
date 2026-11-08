# Independent mathematical audit

## correctness

PASS

The inspected standard variable-coefficient AB2 transfer matrices B(1/r,c/(1+r)) and B(r,rc/(1+r)) have exact period trace a+d and determinant d, a=1-c+c²/2 and d=c²r/[4(1+r)²]. Thus p(1)=c(1-c/2); the factorized discriminant is nonnegative for 0<c<2 and both roots lie in (0,1), while c=2 has unit multiplier and c>2 has a multiplier exceeding one. At fixed c, d is maximal only for r=1 and the dominant root decreases in d, giving the unique minimum. The exact polynomial p_eq(3a/5)=-(3c-4)²(7c²-6c+12)/800 proves global supremal penalty 5/3 at c=4/3 with extreme ratios. The same scalar argument on SPD eigenmodes proves the stated λ_max condition. Independently reconstructed SymPy exact trace, determinant, factors and P=I/3. Strict spectral rather than transient-norm stability is essential.

## originality

PASS

A two-periodic all-positive-ratio real-negative stability frontier plus exact spectral optimization and 5/3 ratio was not identified in the compared standard formula, implementation/zero-stability results, or related published SCOPE results; earlier specialized Adams stability work is a material remaining priority risk.

## value

PASS

A sharp necessary-and-sufficient stability limit invariant under arbitrary positive step imbalance, and the exact unique optimal equal split and worst penalty, give motivated quantitative rules for a canonical variable-step integration method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
