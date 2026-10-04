# Complete full-spark classification for the order-\(12\) DFT
## Finding
Let \(\mathcal F_{12}=(\omega^{mn})_{m,n\in\mathbb Z_{12}}\), where \(\omega=e^{-2\pi i/12}\), and let \(\mathcal F_{12}[\mathcal M,:]\) be the rows indexed by a nonempty proper subset \(\mathcal M\subset\mathbb Z_{12}\). This row-selected harmonic frame is full spark if and only if \(\mathcal M\) is uniformly distributed over the divisors of \(12\) and neither \(\mathcal M\) nor its complement is affinely equivalent, under \(x\mapsto ax+b\) with \(a\in\{1,5,7,11\}\), to either \(\{0,1,2,3,5\}\) or \(\{0,1,2,3,5,10\}\). Equivalently, among uniformly distributed proper row sets, the only non-full-spark sets are the 48 affine images of \(\{0,1,2,3,5\}\), their 48 complements, and the 12 affine images of the self-complementary orbit \(\{0,1,2,3,5,10\}\).

Among uniformly distributed row sets, the exact cardinality table \(m=1,\ldots,11\) for (uniformly distributed, full spark, non-full-spark) is
\[
(12,12,0),(24,24,0),(24,24,0),(24,24,0),(72,24,48),(36,24,12),(72,24,48),(24,24,0),(24,24,0),(24,24,0),(12,12,0).
\]

## Assumptions and scope
A row set \(\mathcal M\subset\mathbb Z_{12}\) is uniformly distributed over the divisors of \(12\) when, for every divisor \(d\mid12\), each residue class modulo \(d\) contains either \(\lfloor |\mathcal M|/d\rfloor\) or \(\lceil |\mathcal M|/d\rceil\) elements of \(\mathcal M\). Two row sets are affinely equivalent when one is the image of the other under \(x\mapsto ax+b\) with \(a\in\mathbb Z_{12}^{\times}=\{1,5,7,11\}\).

The claim is an exact finite classification for Fourier order \(12\) only. It does not assert a general criterion for arbitrary composite Fourier order.

## Proof
Alexeev--Cahill--Mixon prove that uniform distribution over every divisor is necessary for any row-selected DFT to be full spark, even when the DFT order is composite. Thus only uniformly distributed row sets need be considered.

Affine changes of row indices preserve full spark: translation multiplies columns by nonzero diagonal factors, while multiplication by a unit modulo \(12\) permutes the columns. Complementation also preserves the property for a square invertible Fourier matrix by the complementary-minor identity: a minor is nonzero exactly when the complementary minor is nonzero, up to a nonzero scalar factor.

It therefore suffices to classify uniformly distributed row sets of sizes at most \(6\) up to affine equivalence. Exhaustive residue-count enumeration gives exactly the following representatives:
\[
\begin{array}{c|l}
|\mathcal M|&\text{affine representatives}\\
1&\{0\}\\
2&\{0,1\}\\
3&\{0,1,2\}\\
4&\{0,1,2,3\}\\
5&\{0,1,2,3,4\},\;\{0,1,2,3,5\}\\
6&\{0,1,2,3,4,5\},\;\{0,1,2,3,5,10\}.
\end{array}
\]
Every consecutive representative is full spark by the Vandermonde determinant argument.

The remaining two representatives are not full spark. For rows \(\{0,1,2,3,5\}\), the columns \(\{0,1,4,7,8\}\) give a zero determinant. For rows \(\{0,1,2,3,5,10\}\), the columns \(\{0,1,2,4,7,8\}\) give a zero determinant. These vanishings are checked exactly in \(\mathbb Z[z]/(z^4-z^2+1)\), so no floating-point decision is involved. The first bad affine orbit has size \(48\); the second has size \(12\), and translation by \(6\) maps the second representative to its complement. Complement symmetry supplies the size-\(7\) obstruction orbit and closes all sizes above \(6\).

## Verification
The standalone verifier `verify_z12_fullspark.py` performs four finite checks: it enumerates every uniformly distributed subset and its affine orbit; it verifies the two displayed zero determinants with exact cyclotomic-integer arithmetic; it counts all zero maximal minors of the two bad representatives as \(12\) and \(120\), respectively; and it reduces the consecutive representatives modulo \(1009\) at a primitive twelfth root to certify that every maximal minor has nonzero image. The final output is `VERIFY_OK`.

## Relationship to prior work
Alexeev--Cahill--Mixon give the prime-power iff theorem, prove uniform distribution is necessary at arbitrary order, and exhibit the order-\(10\) uniformly distributed counterexample. Osgood--Siripuram--Wu formulate the same maximal-minor property as a universal sampling set and develop the prime-power theory. Achanta et al. revisit row-selected DFT spark, prove coprime/arithmetic-progression and one-missing-row results, and only partially address orders that are products of two distinct primes. None of those inspected statements gives a complete order-\(12\) row-set classification.

## Limitations
The classification is finite and order-specific. Literature search cannot rule out an unindexed or differently phrased prior order-\(12\) classification. The computational verifier certifies the finite orbit and determinant claims, but it does not replace the cited general necessity and complementary-minor facts.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public 2011-10-17.
2. B. Osgood, A. Siripuram, W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992.
3. H. K. Achanta, S. Biswas, S. Dasgupta, M. Jacob, B. N. Dasgupta, R. Mudumbai, *Coprime Conditions for Fourier Sampling for Sparse Recovery*, DOI:10.1109/SAM.2014.6882460.
