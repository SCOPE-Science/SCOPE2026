# Independent mathematical audit

## correctness

PASS

Largest-symbol cycle insertion is bijective between S_(n-1) x [n] and S_n. Conditioning on insertion site gives M_(n,j)=(H_(n-1)+(n-j)M_(n-1,j)+1/j)/n for 2<=j<n. Centering gives d_(n,j)=(n-j)*d_(n-1,j)/n with d_(j,j)=(j-1)/j^2, solving to d_(n,j)=(j-1)/(n*j*C(n-1,j-1)) > 0. Summing yields aggregate covariance = 1/n+O(1/n^2); record and cycle marginal variances H_n-H_n^(2) give correlation asymptotic 1/(n log n). Independently enumerated all 5912 permutations S2..S7 with exact Fraction arithmetic and directly recomputed each local and total covariance. The finite test is supportive, not the all-n proof.

## originality

PASS

Gnedin-Gorin (arXiv:1202.3680) defines exactly these upper records and the fundamental bijection to cycle-weighted/Ewens measures. That bijection establishes marginal equidistribution after transforming permutations, not the covariance of records and cycles measured on the SAME permutation. Bakšajeva-Manstavičius (arXiv:1303.4540) addresses cycle-based Ewens additive statistics, not record-coordinate covariance in the inspected material. A recently indexed broad conjugation-invariant permutation paper describes marginal records but gives no directly covering same-permutation kernel in the inspected discussion. Classic older bivariate cycle/record enumerators might imply it after differentiation; residual risk remains.

## value

PASS

The joint dependence of two canonical equidistributed permutation statistics is a natural and nontrivial invariant distinct from either marginal law. The explicit local sign/binomial kernel and much smaller correlation scale 1/(n log n) characterize how the equivalence-in-law masks a weak positive same-object dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
