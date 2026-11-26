# Independent mathematical audit

## correctness

PASS

Normalize c and ε by row translation, which multiplies each column by a nonzero phase, and put z_y=ζ_p^(ay). For homogeneous parity the two center rows are proportional, while any three projected columns have a nonsingular three-row minor with rows 1,z_y,z_y^(−1), by a column-scaled Vandermonde. For 3+1 the sum/difference of the center rows isolates the singleton, leaving the same Vandermonde on the other three columns. For 2+2, block differences reduce rank to 2+rank K: the two first coordinates of K are nonzero z-differences, and its second coordinate in each column is its first multiplied by −1/(z_u z_v) for that pair. Thus rank is exactly three iff the pair sums agree modulo p, otherwise four. In a balanced partner two columns of opposite parity are distinguished by the center-row ratio and two same-parity columns by the 0-to-a phase ratio; similarly the two center rows differ across parity, and rows at distinct projected coordinates have different ratios on the two columns of either parity. Homogeneous partners always have proportional center rows. The pair counts are ((p−1)/2)² per common sum, with p choices of sum and 2 binom(p,4) additional homogeneous partners; p=3 is included with none of the latter. The repeated projected residue and majority parity recover c and ε, and the remaining unordered offsets give (p−1)/2 choices. Analytic replay: frozen RESULT.md lines 32–59. The checker was inspected but not executed: it certifies determinants at finitely many primes via cyclotomic arithmetic and tests proportionality, not the all-prime theorem nor exact lower ranks by itself.

## originality

PASS

For the frozen result, the distinct part supported by the comparison is the balanced parity midpoint obstruction, its exact rank (without proportional pairs), and the resulting complete partner census for the centered aperture. The 3+1 nonvanishing and Vandermonde pieces are not claimed separately as new. A later indexed theorem does give exactly the balanced rank criterion by transposition and specialization; this is direct mathematical coverage of that stratum, not evidence that an earlier source supplied the frozen classification.

## value

PASS

The support consists of an antipodal pair together with two symmetric displaced samples in one channel, giving a motivated geometry for four-frequency interpolation. The all-prime rule specifies when interpolation fails and quantifies the failure for every partner; the balanced failures are not explained by any proportional pair. The exact resonance and census are useful structural information in the frozen setting, rather than a small-prime table or a routine matched-parity nonvanishing application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
