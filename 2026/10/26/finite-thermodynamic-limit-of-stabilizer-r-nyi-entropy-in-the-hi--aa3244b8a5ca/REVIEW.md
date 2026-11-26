# Independent mathematical audit

## correctness

PASS

The down-before-up inversions give area n²−2d and are exactly the size of a partition in the n-staircase. Every partition of size less than n fits, giving the claimed q^(n/2) bound on the normalization tail. Centered padding preserves the partition and adds only pure stabilizer ancillas, so squared overlap is Z_n/Z_m and the density-matrix Hilbert–Schmidt error is at most √(2P(√q))q^(n/4). For real α>1, the mean-value bound on |a|^(2α), normalized Pauli Parseval and Cauchy–Schwarz give the dimension-independent moment error 4α times that distance. The diagonal Pauli family alone gives F_α≥(sum_x p_x²)^α≥P(q)^(−2α) by Jensen; F_α≤F_1=1. Taking logarithms thus gives both stated constants, including the exponential Cauchy bound. Independently, at n=2 the paths 0011 and 0101 have amplitudes 1 and √q up to normalization. The Pauli fourth powers sum to (1+[(1−q)/(1+q)]^4+[2√q/(1+q)]^4)/2, agreeing with the stated finite identity. The frozen enumeration was inspected, not executed; the analytic argument verifies the limit. No positivity of the limit or endpoint uniformity is inferred.

## originality

PASS

The supported claim is a rigorous finite limit, with explicit size error for all real α>1, for the same colorless weighted state previously studied numerically. The inspected partition bound is old; the new conclusion uses control of centered state overlap together with a dimension-independent Pauli-moment bound and uniform control of the logarithm. No equivalent theorem or dominating result was identified in the bounded comparison.

## value

PASS

The result resolves a natural thermodynamic-limit question raised by measured saturation in the high-area Fredkin phase. Boundedness alone would allow oscillation; exponential convergence and coverage of real orders beyond the replica calculations add concrete information. The size-independent Pauli-moment step is useful precisely where moment estimates that grow with the padded Hilbert-space dimension would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
