# Complete order-10 full-spark classification for harmonic Fourier row sets
## Finding
Let \(\mathcal F_{10}=(\omega^{mn})_{m,n\in\mathbb Z_{10}}\), where \(\omega=e^{-2\pi i/10}\), and let \(\mathcal F_{10}[\mathcal M,:]\) be the rows indexed by a nonempty proper subset \(\mathcal M\subset\mathbb Z_{10}\). This row-selected harmonic frame is full spark if and only if \(\mathcal M\) is uniformly distributed over the divisors of \(10\) and neither \(\mathcal M\) nor its complement is affinely equivalent, under \(x\mapsto ax+b\) with \(a\in\{1,3,7,9\}\), to \(\{0,1,3,4\}\). Equivalently, among uniformly distributed row sets, exactly the ten affine images of \(\{0,1,3,4\}\) and their ten complements fail full spark.

Thus the familiar uniform-distribution condition is almost sufficient at the smallest composite order where it is known to fail: the entire defect consists of one affine orbit in cardinality \(4\) and its complementary orbit in cardinality \(6\).

## Assumptions and scope
Write \(\mathbb Z_{10}=\{0,1,\ldots,9\}\). A row set \(\mathcal M\) is *uniformly distributed over a divisor* \(d\mid 10\) when the numbers of elements of \(\mathcal M\) in the residue classes modulo \(d\) differ by at most one. The row-selected matrix is *full spark* when every square submatrix using all selected rows and the same number of columns is nonsingular.

Affine equivalence means \(\mathcal M\mapsto a\mathcal M+b\) modulo \(10\), with \(a\) a unit modulo \(10\). Complement means \(\mathbb Z_{10}\setminus\mathcal M\). The statement covers every nonempty proper row set, not only a chosen cardinality.

## Proof
Alexeev--Cahill--Mixon prove two facts used here. First, full spark is preserved by translating row indices, multiplying them by a unit modulo the Fourier order, and taking complements. Second, for arbitrary Fourier order, uniform distribution over every divisor is necessary for a row-selected DFT matrix to be full spark. They also exhibit the uniformly distributed order-\(10\) set \(\{0,1,3,4\}\) with columns \(\{0,1,2,6\}\) as a singular minor.

It remains to decide the uniformly distributed row sets. Up to the affine action \(x\mapsto ax+b\), exact enumeration gives the following representatives for cardinalities at most \(5\):

\[
\begin{array}{c|c}
|\mathcal M| & \text{affine representatives}\\
\hline
1 & \{0\}\\
2 & \{0,1\}\\
3 & \{0,1,2\},\ \{0,1,3\}\\
4 & \{0,1,2,3\},\ \{0,1,3,4\}\\
5 & \{0,1,2,3,4\}.
\end{array}
\]

Every representative except \(\{0,1,3\}\) and the published exceptional set is consecutive, hence full spark by the Vandermonde determinant. For \(\mathcal M=\{0,1,3\}\), let \(x_1,x_2,x_3\) be three distinct tenth roots of unity corresponding to any three selected columns. Its determinant factors as
\[
-\,(x_1-x_2)(x_1-x_3)(x_2-x_3)(x_1+x_2+x_3).
\]
The first three factors are nonzero. If \(x_1+x_2+x_3=0\), three unit complex numbers sum to zero, so their ratios are primitive cube roots of unity. But every ratio of tenth roots is a tenth root, and no primitive cube root is a tenth root because \(\gcd(3,10)=1\). Hence this determinant is also nonzero for every three-column choice.

The second cardinality-\(4\) orbit is exactly the affine orbit of \(\{0,1,3,4\}\), and the published columns \(\{0,1,2,6\}\) give a zero determinant. Complement invariance settles cardinalities \(6,7,8,9\). This proves the stated classification.

## Verification
The accompanying `verify_z10_fullspark.py` performs exact arithmetic in \(\mathbb Z[z]/(z^4-z^3+z^2-z+1)\), where \(z\) represents a primitive tenth root of unity. It enumerates every uniformly distributed row set through cardinality \(5\), every square minor needed to test full spark, and every affine orbit; complement symmetry then covers cardinalities above \(5\).

The exact census is
\[
\begin{array}{c|c|c|c}
|\mathcal M|&\text{uniform}&\text{full spark}&\text{not full spark}\\
\hline
1&10&10&0\\
2&20&20&0\\
3&60&60&0\\
4&30&20&10\\
5&20&20&0\\
6&30&20&10\\
7&60&60&0\\
8&20&20&0\\
9&10&10&0.
\end{array}
\]
It also verifies exactly that the ten bad cardinality-\(4\) sets form the affine orbit of \(\{0,1,3,4\}\), and that the stated \(4\times4\) witness determinant is zero.

## Relationship to prior work
Alexeev--Cahill--Mixon established the general necessity of uniform distribution, a complete prime-power characterization, affine/complement invariance, and the order-\(10\) counterexample \(\{0,1,3,4\}\). Achanta--Biswas--Dasgupta--Jacob--Dasgupta--Mudumbai later analyzed coprime and one-missing-row patterns and revisited the same order-\(10\) counterexample through vanishing sums of roots of unity. Tang subsequently described the arbitrary-composite full-spark characterization as unresolved while recording the prime-power and consecutive-row regimes. The result here closes the full row-set classification at order \(10\), rather than supplying another sufficient family.

Targeted searches for the exact order-\(10\) classification, affine-orbit formulation, and equivalent full-spark statements did not locate a prior source stating this complete classification. Search failure is not a proof of novelty; the residual literature risk is recorded in the review.

## Limitations
This is an exact finite classification at Fourier order \(10\); it does not provide a general criterion for all composite orders. The originality assessment is literature-search based and may miss differently phrased or unindexed work. The exact verifier certifies the finite census and determinants, while the mathematical argument above explains why those checks cover every row set in the stated domain.

## References
1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (first public version 2011-10-17); Journal of Fourier Analysis and Applications 18 (2012).
2. H. K. Achanta, S. Biswas, S. Dasgupta, M. Jacob, B. N. Dasgupta, R. Mudumbai, *Coprime Conditions for Fourier Sampling for Sparse Recovery*, IEEE SAM 2014, DOI:10.1109/SAM.2014.6882460.
3. S. Tang, *Universal Spatiotemporal Sampling Sets for Discrete Spatially Invariant Evolution Systems*, arXiv:1702.05345 (2017); IEEE Transactions on Information Theory 63(9), 5518--5528.
