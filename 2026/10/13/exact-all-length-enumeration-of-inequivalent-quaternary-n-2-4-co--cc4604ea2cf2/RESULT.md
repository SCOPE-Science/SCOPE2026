# Exact all-length enumeration of inequivalent quaternary \([n,2]_4\) codes by Hermitian hull dimension
## Finding

For each integer \(n\ge 2\), let \(I_{n,\ell}\) be the number of monomial-equivalence classes of quaternary \([n,2]_4\) linear codes whose Hermitian hull has dimension \(\ell\in\{0,1,2\}\). Zero coordinates are allowed, as they are for unrestricted linear codes.

Define \(B_r(x)=[y^r]B(x,y)\), where
\[
B(x,y)=\frac1{60}\left[
\left(\frac{1+xy}{1-x^2}\right)^5
+15\frac{1+xy}{1-x^2}\left(\frac{1+x^2y^2}{1-x^4}\right)^2
+20\left(\frac{1+xy}{1-x^2}\right)^2\frac{1+x^3y^3}{1-x^6}
+24\frac{1+x^5y^5}{1-x^{10}}
\right].
\]
Then
\[
\sum_{n\ge0}I_{n,0}x^n=\frac{B_2(x)+B_3(x)}{1-x},
\]
\[
\sum_{n\ge0}I_{n,1}x^n=\frac{B_1(x)+B_4(x)-x/(1-x^2)}{1-x},
\]
and
\[
\sum_{n\ge0}I_{n,2}x^n=\frac{B_0(x)+B_5(x)-1/(1-x^2)}{1-x}.
\]
In particular,
\[
I_{n,0}>I_{n,1}>I_{n,2}\qquad(n\ge4).
\]
The first triples \((I_{n,0},I_{n,1},I_{n,2})\) are
\[
(1,0,0),(2,1,0),(4,2,1),(6,5,2),(11,7,4),(16,13,5),(25,17,9),(34,28,11)
\]
for \(n=2,3,\ldots,9\), respectively.

## Assumptions and scope

Equivalence means ordinary monomial equivalence over \(\mathbb F_4\): coordinate permutations and multiplication of coordinates by nonzero field elements. Semilinear equivalence is not being counted. The Hermitian product is \(\langle u,v\rangle_H=\sum_i u_i v_i^2\).

The result concerns all quaternary dimension-two linear codes, not only LCD codes and not only codes satisfying a dual-distance restriction. A zero column contributes one coordinate to the length and does not change the Hermitian Gram matrix.

## Proof

Choose the five projective representatives
\[
(1,0),(0,1),(1,1),(1,\omega),(1,\omega^2)
\]
of \(\operatorname{PG}(1,4)\), where \(\omega^2+\omega+1=0\). Any full-rank \(2\times n\) generator matrix is, after coordinate scalings, encoded by the number \(z\) of zero columns and a multiplicity vector \((m_1,\ldots,m_5)\) on these five projective points. Row operations induce \(\operatorname{PGL}(2,4)\cong A_5\), in its natural action on five points. Hence monomial-equivalence classes are exactly \(A_5\)-orbits of multiplicity vectors, together with the invariant \(z\).

For every nonzero \(c\in\mathbb F_4\), \(c c^2=c^3=1\). Therefore coordinate scaling does not alter a column's contribution \(v\overline v^{\mathsf T}\) to the Hermitian Gram matrix. Since the characteristic is two, only the parity of each \(m_i\) matters. Let \(S\) be the set of projective points having odd multiplicity. The five rank-one contributions sum to zero. A single contribution has rank one, while the sum of two distinct contributions has rank two because the two projective representatives are linearly independent. Taking complements in the five-point sum gives
\[
\operatorname{rank}(G\overline G^{\mathsf T})=
\begin{cases}
0,&|S|\in\{0,5\},\\
1,&|S|\in\{1,4\},\\
2,&|S|\in\{2,3\}.
\end{cases}
\]
Since \(\dim(C\cap C^{\perp_H})=2-\operatorname{rank}(G\overline G^{\mathsf T})\), the parity-set size determines the hull dimension exactly.

The natural five-point action of \(A_5\) has cycle types \(1^5\), \(1\,2^2\), \(1^2\,3\), and \(5\), occurring with multiplicities \(1,15,20,24\). On a cycle of length \(L\), a fixed multiplicity contributes
\[
\frac{1+x^L y^L}{1-x^{2L}},
\]
because an odd multiplicity contributes \(L\) odd projective points and an even multiplicity contributes none. Burnside's lemma therefore gives exactly the displayed bivariate series \(B(x,y)\).

A dimension-two code must use at least two distinct nonzero projective points. Among multiplicity-vector orbits with support of size at most one, there is exactly one orbit for each positive total multiplicity. Odd totals lie in the \(|S|=1\) sector, giving the subtraction \(x/(1-x^2)\); even totals, including zero, lie in the \(|S|=0\) sector, giving the subtraction \(1/(1-x^2)\). Finally, the independent number of zero columns contributes the factor \(1/(1-x)\). This proves the three generating functions.

For strict monotonicity, put \(D_{01}(x)=\sum_n(I_{n,0}-I_{n,1})x^n\) and \(D_{12}(x)=\sum_n(I_{n,1}-I_{n,2})x^n\). Exact simplification of the displayed rational functions shows that every pole has order at most six and order dividing sixty. The bundled certificate records the integer polynomials \(P_{01},P_{12}\) satisfying
\[
(1-x^{60})^6D_{ij}(x)=P_{ij}(x).
\]
For each residue class \(r\pmod{60}\), writing the nonzero terms of \(P_{ij}\) as \(p_{r+60u}\), the coefficient at \(n=r+60t\) is
\[
\sum_u p_{r+60u}\binom{t-u+5}{5}.
\]
After the finite shift \(t=s+U_r\), where \(U_r\le5\) is the largest occurring \(u\), this is a degree-five polynomial in \(s\) whose six ordinary coefficients are all strictly positive. The finite values preceding the shift are also positive whenever \(n\ge4\). Thus both differences are strictly positive for every \(n\ge4\). The verifier reconstructs this certificate from exact integer data and checks all residue classes.

## Verification

The standalone verifier uses only the Python standard library. It checks the \(\mathbb F_4\) Gram-rank rule for all \(32\) parity subsets, reconstructs the Burnside fixed-point counts from the four cycle types, recovers the initial orbit counts, verifies the rational identities in the monotonicity certificate by exact polynomial arithmetic, and proves positivity on all sixty residue classes by exact rational polynomial coefficients. Its successful terminal output is `VERIFY_OK`.

## Relationship to prior work

Ishizuka's 2026 paper derives monotonicity for the total number of Hermitian-hull-graded codes and explicitly identifies a Hermitian analogue of inequivalent-code monotonicity over \(\mathbb F_4\) as an open direction. The present result solves the complete dimension-two slice of that inequivalent-code problem, with exact generating functions rather than only an inequality.

Araya and Harada's 2026 classification work uses the same five projective multiplicities for quaternary dimension-two codes, but its classification target is Hermitian LCD codes, namely hull dimension zero. Their dimension-two data therefore support the projective-multiplicity model but do not determine the hull-one and hull-two orbit counts, the all-length three-way generating functions, or the strict inequalities proved here.

## Limitations

The equivalence relation is monomial, not semilinear. The result is complete only for code dimension two; no claim is made for higher dimensions. Zero coordinates are included, so the counts differ from classifications imposing \(d(C^{\perp_H})\ge2\). The novelty comparison cannot exclude an unindexed or inaccessible manuscript containing the same five-point cycle-index computation.

## References

1. Keita Ishizuka, *Comparative monotonicity of linear codes by Hermitian and symplectic hull dimensions*, arXiv:2605.29204v1, first public 28 May 2026. MSC 2020: 94B05, 81P70, 11T71.
2. Makoto Araya and Masaaki Harada, *On the classification of quaternary Hermitian LCD codes*, Computational and Applied Mathematics, published online 13 August 2026, DOI 10.1007/s40314-026-03875-2.
