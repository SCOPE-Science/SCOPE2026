# Independent mathematical audit

## correctness

PASS

PASS: Every cyclic factor of length at most n in the two-one circle has 0, 1 or 2 ones. Distinct zero-only palindromes contribute max(a,b), one-one centered palindromes contribute min(a,b)+1, and two-one palindromes contribute floor(a/2)+floor(b/2)+2 when a!=b, or floor(a/2)+1 when a=b because the two gap families coincide. Summation proves exact P(w). For odd n, a+b odd forces distinct opposite-parity gaps and P=(3n−1)/2; for even n=2m, unordered gap pairs classify H=3m (A=floor(m/2)), H−1 (B=ceil(m/2)−1) and unique antipodal H−D, D=floor(m/2)+1. Orbit sizes n except antipodal n/2 establish labeled probabilities and exact mean/variance, with even variance n/16+O(1) and odd variance identically zero. Independently generated distinct cyclic palindromic substrings for 1,275 ordered gap cases through n=51, including tiny boundary n=2, and matched formula. Infinite identities rest on gap proof, not finite tests.

## originality

PASS

Simpson establishes general global upper bound <5n/3 and extremal families; OEIS A247000 tabulates global maxima. Those do not imply the complete fixed-Hamming-weight-two gap classification, exact necklace distribution or parity-dependent variance. The 2017 cyclic squares paper concerns square factors, not palindromes. Best-of-knowledge PASS with priority risk for overlooked special cases in early literature.

## value

PASS

PASS: Weight two is the first genuinely nontrivial circular binary support pattern, and the complete necklace-level classification has a surprising exact parity rigidity: all odd lengths have zero variance while even lengths have linearly diverging variance from one antipodal orbit. This is a motivated structural counting result, not an arbitrary small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
