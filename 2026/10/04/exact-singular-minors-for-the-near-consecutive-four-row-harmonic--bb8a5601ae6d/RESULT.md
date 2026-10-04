# Exact singular minors for the near-consecutive four-row harmonic frame

## Finding
For every integer \(N\ge 5\), let \(\omega=e^{-2\pi i/N}\) and let \(F_N=(\omega^{mn})_{m,n\in\mathbb Z_N}\). Retain the four rows
\[
M=\{0,1,2,4\}.
\]
For any four distinct columns \(C\subset\mathbb Z_N\), the corresponding \(4\times4\) minor is singular if and only if \(N\) is even and
\[
C=\{a,a+N/2,b,b+N/2\}
\]
for two distinct residue classes \(a,b\pmod{N/2}\). Consequently the four-row harmonic frame is full spark exactly when \(N\) is odd. If \(N\) is even, the number of singular maximal minors is exactly
\[
\binom{N/2}{2}=\frac{N(N-2)}8,
\]
and every singular maximal minor has rank exactly \(3\).

The same row set is uniformly distributed over every divisor of \(N\) exactly when \(N\) is odd. Thus for this particular four-row family, the usual uniform-distribution necessary condition is sufficient for every modulus, not only prime powers.

## Assumptions and scope
The DFT is unnormalized; multiplying rows or columns by nonzero scalars does not change singularity. The statement concerns maximal minors formed from the fixed row set \(M=\{0,1,2,4\}\) and four distinct columns. The restriction \(N\ge5\) ensures that these are four distinct row indices modulo \(N\).

Full spark here means that every choice of four columns is linearly independent. Uniform distribution over a divisor \(d\mid N\) means that the occupancies of the residue classes modulo \(d\) differ by at most one.

## Proof
Let the four selected columns correspond to distinct \(N\)-th roots of unity \(z_1,z_2,z_3,z_4\). Their determinant is the generalized Vandermonde determinant
\[
D=\det\begin{pmatrix}
1&1&1&1\\
z_1&z_2&z_3&z_4\\
z_1^2&z_2^2&z_3^2&z_4^2\\
z_1^4&z_2^4&z_3^4&z_4^4
\end{pmatrix}.
\]
The Schur-factorization for the exponent pattern \((0,1,2,4)\), or a direct determinant expansion, gives
\[
D=\prod_{1\le i<j\le4}(z_j-z_i)(z_1+z_2+z_3+z_4).
\]
Because the columns are distinct, the Vandermonde factor is nonzero. Hence the minor is singular exactly when
\[
z_1+z_2+z_3+z_4=0.
\]

Suppose this sum vanishes. Let
\[
Q(t)=\prod_{j=1}^4(t-z_j)=t^4-e_1t^3+e_2t^2-e_3t+e_4.
\]
Here \(e_1=0\). Since all \(z_j\) have modulus one,
\[
e_3=e_4\sum_{j=1}^4z_j^{-1}=e_4\,\overline{\sum_{j=1}^4z_j}=0.
\]
Thus \(Q(t)=t^4+e_2t^2+e_4\) is even. Its set of roots is therefore invariant under \(z\mapsto-z\). As the four roots are distinct, they form exactly two antipodal pairs. Conversely, two antipodal pairs plainly have zero sum. Among \(N\)-th roots, an antipode is again an \(N\)-th root exactly when \(N\) is even. This proves the singularity criterion and the odd-\(N\) full-spark statement.

When \(N\) is even there are \(N/2\) antipodal pairs of \(N\)-th roots, and a singular minor is obtained by choosing exactly two of them. Hence the count is \(\binom{N/2}{2}\). The first three retained rows, with exponents \(0,1,2\), form an ordinary \(3\times4\) Vandermonde matrix. Every three of its columns are independent, so every singular maximal minor has rank exactly \(3\).

Finally, if \(N\) is even then reduction modulo the divisor \(2\) gives occupancies \((3,1)\) for the row set \(\{0,1,2,4\}\), so uniform distribution fails. If \(N\) is odd, every divisor \(d\mid N\) is odd. For \(d=1\) there is nothing to check; for \(d=3\) the occupancies are \((1,2,1)\); and for every \(d\ge5\), the residues \(0,1,2,4\) are distinct. In every case the occupancies differ by at most one. Thus uniform distribution over all divisors is equivalent to oddness of \(N\).

## Verification
The accompanying checker verifies the determinant factorization by exact multivariate integer-polynomial arithmetic. It then constructs cyclotomic polynomials exactly and exhaustively checks every four-column subset for \(5\le N\le40\), testing a root sum by reduction modulo \(\Phi_N\), with no floating-point arithmetic. Its output is

`VERIFY_OK N_max=40 subsets=749397 singular=1329 determinant_identity=exact`

The finite check corroborates the proof; it is not used to extend a finite computation to arbitrary \(N\).

## Relationship to prior work
Alexeev, Cahill and Mixon prove that for prime-power DFT sizes, a selected row set generates a full-spark harmonic frame exactly when it is uniformly distributed over the divisors of the size. They also prove the uniform-distribution condition is necessary for general sizes and explicitly note that it is not sufficient in general, giving a composite counterexample. Therefore the odd prime-power instances of the full-spark conclusion above are already covered by their theorem. The contribution here is the all-modulus classification for the specific near-consecutive row set \(\{0,1,2,4\}\), including odd composite sizes and the exact geometry, count, and rank of every bad maximal minor at even sizes.

The determinant factorization itself is a special generalized-Vandermonde identity and is used only as the mechanism for the classification; it is not claimed as new.

## Limitations
This result is specific to the row pattern \(\{0,1,2,4\}\). It does not provide a characterization of arbitrary four-row DFT subframes, nor does it replace the general composite-size full-spark problem. The literature comparison found no covering statement for this exact all-modulus family, but older notes or treatments indexed only under generalized Vandermonde determinants or roots-of-unity sums remain a residual originality risk.

## References
1. B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, Journal of Fourier Analysis and Applications 18 (2012), 1167-1194; arXiv:1110.3548.
2. I. M. Isaacs and R. Evans, *Generalized Vandermonde Determinants and Roots of Unity of Prime Order*, Proceedings of the American Mathematical Society 58 (1976), 51-54.
