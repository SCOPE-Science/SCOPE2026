# Complete quartet obstruction for five-row dyadic harmonic Fourier minors

## Finding
For every integer \(a\ge3\), set \(N=2^a\), \(\omega=\exp(2\pi i/N)\), and define the \(5\times N\) complex Fourier submatrix
\[
F_{r,c}=\omega^{rc},\qquad r\in R=\{0,1,2,4,5\},\quad c\in\mathbb Z/N\mathbb Z.
\]
For every five-element column set \(C\), the corresponding square minor is singular **if and only if** \(C\) contains an entire coset of the unique subgroup of order four:
\[
Q_t=\{t,t+N/4,t+N/2,t+3N/4\}\pmod N.
\]
Every singular square minor has complex rank exactly \(4\), and the exact number of singular five-column sets is
\[
\boxed{\frac N4(N-4)}.
\]
All other five-column sets give invertible minors. Thus all rank losses of this fixed five-row harmonic frame are completely classified, including their incidence and exact multiplicity.

## Assumptions and scope
The modulus is a power of two with \(N\ge8\); the five Fourier rows are exactly \(R\). Column subsets are unordered and contain five distinct residue classes. Matrix rank and singularity are computed over \(\mathbb C\), not by modular reduction. The discrete Fourier phase may equally be taken with negative sign, by conjugation. No statement is made about arbitrary five-row patterns or odd moduli.

## Proof
**Step 1: the precise determinant obstruction.** For five distinct nonzero numbers \(x_1,\ldots,x_5\), the alternant/Schur identity for exponents \((0,1,2,4,5)\) is
\[
\det(x_j^{r_i})_{i,j=1}^5
 =\Bigl(\prod_{1\le i<j\le5}(x_j-x_i)\Bigr)
   e_2(x_1,\ldots,x_5),\qquad
 e_2=\sum_{1\le i<j\le5}x_ix_j.
\]
The Vandermonde factor never vanishes at five distinct \(N\)-th roots of unity. It therefore remains to classify the five-element sets of dyadic roots with \(e_2=0\).

**Step 2: exact cancellation pairing.** If \(N=2^a\), the cyclotomic polynomial is \(\Phi_N(T)=T^{N/2}+1\). Therefore any finite sum of \(N\)-th roots of unity with nonnegative integral multiplicities can vanish only when, for each \(t\in\{0,\ldots,N/2-1\}\), the numbers of occurrences of \(\omega^t\) and \(-\omega^t\) coincide. In particular its terms admit a partition into opposite pairs, including repeated terms. Apply this to the ten products \(x_ix_j\) indexed by the edges of the complete graph on five vertices.

**Step 3: when two selected roots are opposite.** Suppose \(x_1=u\), \(x_2=-u\); denote the other roots by \(v,w,z\). Then
\[
0=e_2=-u^2+vw+vz+wz.
\]
The four displayed root-of-unity terms must partition into two opposite pairs. Hence one among \(vw,vz,wz\) equals \(u^2\), and the other two are opposite. As two products share one factor, the latter forces two of \(v,w,z\) to be opposite, say \(w=-v\). The five-element set now contains \(u,-u,v,-v,z\), giving
\[
0=e_2=-u^2-v^2.
\]
Thus \(v=iu\) or \(v=-iu\), so the set contains the entire quartet \(\{u,iu,-u,-iu\}\). Because \(N\) is divisible by four, this is exactly one coset \(Q_t\) under exponent indexing.

**Step 4: no opposite selected roots.** Suppose instead none of the five \(x_i\) is the negative of another. Every partition of the ten edge products into five opposite pairs must pair disjoint edges: shared-vertex edges \(x_ix_j\) and \(x_ix_k\) could be negatives only if \(x_j=-x_k\). Each opposite edge pair is therefore a matching of size two on five vertices, omitting exactly one vertex. Each vertex participates in four edges, and so is omitted from exactly one of the five matchings. The five omitted vertices are consequently all distinct.

Write \(x_i=\omega^{c_i}\). For the pair of disjoint edges omitting vertex \(\ell\), the opposite-product condition is
\[
c_i+c_j-c_k-c_m\equiv N/2\pmod N,
\qquad \{i,j,k,m\}=\{1,\ldots,5\}\setminus\{\ell\}.
\]
Reducing modulo two (using that \(N/2\) is even) shows \(\sum_{i\ne\ell}c_i\equiv0\pmod2\). Since all five possibilities for \(\ell\) occur, these congruences force \(c_1,\ldots,c_5\) to have the same parity. Hence, for some \(\varepsilon\in\{0,1\}\), write \(c_i=\varepsilon+2d_i\), where the five residues \(d_i\) are distinct modulo \(N/2\). The equation reduces to
\[
 e_2(\omega^{c_1},\ldots,\omega^{c_5})
 =\omega^{2\varepsilon}
 e_2(\omega_{N/2}^{d_1},\ldots,\omega_{N/2}^{d_5})=0,
\]
where \(\omega_{N/2}=\omega^2\). Iterate this argument by strong induction on \(a\); the base moduli \(2\) and \(4\) cannot accommodate five distinct roots. A vanishing set at the lower modulus, if it exists, therefore contains an order-four coset by induction, and lifting the five exponents through \(c_i=\varepsilon+2d_i\) preserves the order-four coset in the original modulus. This proves that every vanishing set contains a quartet.

**Step 5: sufficiency.** A quartet \(\{u,iu,-u,-iu\}\) has first and second elementary symmetric sums both zero. Adding any fifth root \(v\) outside it preserves the vanishing of \(e_2\), since \(e_2(Q\cup\{v\})=e_2(Q)+v e_1(Q)=0\). Thus the quartet condition is necessary and sufficient.

**Step 6: exact rank.** From a vanishing five-column set take the four columns \(\{u,-u,iu,v\}\), where \(v\) lies outside its quartet. The four-row minor with exponents \(\{0,1,2,4\}\) factors as its nonzero Vandermonde product times \(e_1(u,-u,iu,v)=iu+v\). It is nonzero because \(v\ne-iu\), the missing quartet member. The singular five-row minor therefore has rank at least four, hence exactly four.

**Step 7: enumeration.** The subgroup of order four has \(N/4\) distinct cosets, with \(N-4\) choices for the fifth column. A five-element set cannot contain two distinct four-element cosets, so no set is counted twice. The number is exactly \((N/4)(N-4)\).

## Verification
The standalone script `verify_dyadic_5minor.py` tests the cyclotomic pair-multiplicity condition against quartet incidence for **every** five-column subset at \(N=8,16,32\) using integer arithmetic, obtaining respectively \(8\), \(48\), and \(224\) singular sets from \(56\), \(4368\), and \(201376\) tested sets. It separately verifies the generalized-Vandermonde determinant identity on four five-tuples of integer nodes without floating-point arithmetic. Execute `python3 verify_dyadic_5minor.py`; the expected output is embedded in `verification_output.txt`. These finite checks accompany, but do not replace, the proof for all powers of two.

## Relationship to prior work
Malikiosis and Oussa, *Full Spark Frames in the Orbit of a Representation* (arXiv:1909.06223, first available 2019-09-13), recalls the prime-power uniform-distribution criterion for **whether any** maximal Fourier minor can vanish and explains Schur/alternant factorization. For this row set, the criterion already detects absence of full spark; it does not determine **which** five-column sets fail, their number, or exact rank. Needham and Shonkwiler, *Toric Symplectic Geometry and Full Spark Frames* (arXiv:2110.11295), studies the geometry of full-spark frames, not this fixed dyadic erasure pattern. Hidaka and Itoh, *The Schur polynomials in all primitive nth roots of unity* (arXiv:2403.10817), concerns a different evaluation domain consisting of all primitive roots, rather than arbitrary five-element subsets. A related four-row harmonic-frame minor result has a two-antipodal-pair obstruction; the five-row second-elementary-symmetric obstruction is not implied by that four-column statement.

## Limitations
The theorem treats the single row aperture \(\{0,1,2,4,5\}\) over cyclic powers of two. It does not assert an optimality property among all five-row apertures, stability of nonsingular minors, or a classification at odd or mixed moduli. The computational checker exhausts only \(N=8,16,32\); completeness for all \(N=2^a\) comes from the dyadic cancellation and induction proof. The novelty comparison is best knowledge and cannot exclude an older unindexed equivalent result on dyadic Schur-polynomial zeros.

## References
1. R.-D. Malikiosis and V. Oussa, *Full Spark Frames in the Orbit of a Representation*, arXiv:1909.06223 (first public version 2019-09-13), https://arxiv.org/abs/1909.06223.
2. J. Needham and C. Shonkwiler, *Toric Symplectic Geometry and Full Spark Frames*, arXiv:2110.11295, https://arxiv.org/abs/2110.11295.
3. H. Hidaka and J. Itoh, *The Schur polynomials in all primitive nth roots of unity*, arXiv:2403.10817, https://arxiv.org/abs/2403.10817.
