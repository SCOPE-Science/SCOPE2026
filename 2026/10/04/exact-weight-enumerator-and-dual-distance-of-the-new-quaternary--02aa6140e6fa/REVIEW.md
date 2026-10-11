# Independent mathematical audit

## correctness

PASS

The published generator matrix of the new \([22,10,9]_4\) Hermitian LCD code was independently reconstructed over \(\mathbb F_4\). Enumerating all \(4^{10}=1,048,576\) messages reproduced every coefficient of the stated Hamming weight enumerator and minimum weight nine. The Hermitian Gram matrix has rank ten. Independently testing all \(74,613\) six-column subsets found none dependent, while exactly 88 of the \(170,544\) seven-column subsets have rank six. Hence the Euclidean dual distance is seven, and conjugation gives the same Hermitian-dual distance. A separate MacWilliams computation gives \(A_6^\perp=0\) and \(A_7^\perp=264\), agreeing with the circuit count and implying orthogonal-array strength six.

## originality

PASS

Abdukhalikov and Ho publish the explicit generator matrix and prove that this code is a new best-known \([22,10,9]_4\) Hermitian LCD code. Their complete searchable article does not contain a weight enumerator, and the inspected Example 2 states only the parameters and LCD property. The dual minimum distance, exact number of dependent seven-sets, and orthogonal-array strength are not implied by the parameter triple or LCD property without additional finite computation. Current Resultary and web searches did not locate those invariants for this code.

## value

PASS

The object is a newly identified best-known Hermitian LCD code, so its complete weight spectrum and dual strength are natural reference invariants rather than an arbitrary code sample. The dual distance seven and OA strength six provide structural information relevant to projections, designs, and comparisons that is not encoded in the headline \([22,10,9]\) parameters. The exact exhaustive certificate makes these reusable finite facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
