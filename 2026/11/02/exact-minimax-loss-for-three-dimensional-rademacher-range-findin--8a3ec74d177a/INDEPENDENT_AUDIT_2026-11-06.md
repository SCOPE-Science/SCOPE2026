# Independent mathematical audit

## correctness

PASS

The eight 3D sign columns form exactly four equally probable projective lines; every three distinct lines span R^3. Rank-one words number four, rank-two words 6(2^ell-2), hence rank deficiency 6/2^ell-8/4^ell for all positive ell. Direct orthogonal projectors give exact singleton losses T-u^T G^2 u/(u^T G u) and pair-plane losses 2/(v^T G^-1 v) over six normal directions. Both direction sets are tight frames with summed outer products 4I. Two Cauchy-Schwarz bounds yield normalized expected loss <=(2^(ell+1)-4/3)/4^ell, equality for G=A^T A scalar. Positive-probability singleton events force all four nonorthogonal sign lines to be G-eigenvectors at equality, implying scalar G uniquely. An independent rational SymPy calculation exhausted 4^ell projective words for ell=1..5 on a nonscalar diagonal Gram input, confirming the exact formula and bound; proof covers all ell and invertible real A.

## originality

PASS

Qualified best-of-knowledge originality: standard random range finding and sub-Gaussian sketch theorems provide expected/high-probability bounds but were not seen to give this dimension-three exact discrete occupancy law plus a sharp unique worst-case Gram characterization. The sign rank distribution itself is elementary and not claimed independently novel.

## value

PASS

Finite-alphabet sketches have a persistent exact-rank recovery obstruction even when oversampled beyond dimension, unlike continuous Gaussian sketches. The exact mean loss and sharp minimax extremizer capture a concrete failure probability and geometric sensitivity useful in randomized linear algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
