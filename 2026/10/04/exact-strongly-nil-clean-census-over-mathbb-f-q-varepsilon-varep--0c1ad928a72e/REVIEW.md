# Independent mathematical audit

## correctness

PASS

For \(R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2)\), the lifting argument is field-independent: a residue matrix \(A\) is strongly nil-clean exactly when its generalized eigenspaces are supported at \(0\) and \(1\), and the off-diagonal idempotent correction is solved by a Sylvester map between coprime primary blocks. Thus every dual part \(B\) lifts. For generalized one-eigenspace dimension \(r\), there are \({n\brack r}_q q^{r(n-r)}\) ordered complementary decompositions, and the two nilpotent blocks contribute \(q^{r^2-r}\) and \(q^{(n-r)^2-(n-r)}\). Multiplying by all \(q^{n^2}\) dual parts gives the stated summand. An independent brute-force check for \(n=2\) over \(q=2,3,5\) counted 14, 30 and 80 strongly nil-clean residue matrices, exactly matching the residue formula.

## originality

PASS

The complete Senturk--Ozbay paper proves for real dual matrices that strong nil-cleanness of \(A+B\varepsilon\) is equivalent to strong nil-cleanness of \(A\), and displays the Sylvester lifting mechanism, but it contains no finite-field census. Fine--Herstein supplies the nilpotent-block count, not the two-primary strong-nil-clean census. Combining the field-independent lifting with a decomposition count yields a natural all-\(n,q\) formula not found in Resultary or the inspected matrix-clean literature. The result is more than a fixed-table computation because it identifies the exact density symbolically for every prime power and every dimension.

## value

PASS

Strong nil-cleanness is a standard decomposition property, and the finite dual-number matrix ring provides a natural setting where nil-clean and strongly nil-clean behavior diverge. The all-dimension exact density, including the concrete 224/256 binary dual example, is a motivated finite-ring invariant and a useful quantitative complement to existence-only clean-ring results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
