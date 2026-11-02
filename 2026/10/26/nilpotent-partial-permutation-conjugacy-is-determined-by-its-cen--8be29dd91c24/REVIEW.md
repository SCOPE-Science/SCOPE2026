# Independent mathematical audit

## correctness

PASS

For finite nilpotent partial injections alpha, the directed components are chains of vertex lengths lambda_i. Commutation with alpha forces any nonempty restriction of beta to a source chain to be its initial segment of length l, mapped in arrow order onto the terminal l-segment of a single target chain (l<=min(lambda_i,lambda_j)). Distinct nonempty source chains cannot share one target because terminal segments intersect, hence all beta correspond bijectively to nonattacking matchings of the chain-by-chain board, with edge weight W_ij(t)=t+...+t^min(lambda_i,lambda_j). This proves the full rank polynomial formula. If c_j=#chains of length>=j and lambda<j truncates lengths at j-1, the coefficient [t^j](C_lambda-C_lambda<j)=c_j²: a length-j edge is necessarily the only matched edge contributing degree j; all shorter contributions cancel. Starting at [t]C=c_1², nonnegative square roots recover c_j inductively and every chain length multiplicity c_j-c_(j+1). Thus equality of polynomials iff conjugacy including ambient size, for every finite n>=0. Inspected verification script exhaustively enumerates commuting partial injections for partitions through n=6 and recovery through n=7; finite enumeration is corroboration only.

## originality

PASS

Best-of-knowledge PASS after comparison of theorem statements, hypotheses, reductions and implications. The inspected sources do not establish the complete final claim for this record; known components are acknowledged. Nilpotent partial-permutation conjugacy is determined by its centralizer rank spectrum retains explicit residual priority risks. An inaccessible plausible source alone is not treated as failure or as a whole-document NOT_COVERING finding.

## value

PASS

This is a complete structural reconstruction: a single univariate enumeration by ranks of the centralizer determines the entire nilpotent conjugacy partition. Explicit weighted rook matching and triangular square-root decoding make a meaningful algebraic invariant rather than merely restating known conjugacy-by-chains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
