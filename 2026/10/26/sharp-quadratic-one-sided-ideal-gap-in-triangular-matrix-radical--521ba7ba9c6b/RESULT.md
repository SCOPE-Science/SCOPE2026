# Sharp quadratic one-sided ideal gap in triangular matrix radicals

## Finding
Let \(k\) be any field, \(n\ge 2\), \(T_n(k)\) the algebra of upper triangular \(n\times n\) matrices, and \(J_n(k)\) its strictly upper triangular radical. For \(X\in J_n(k)\) of ordinary matrix rank \(r\), define the one-sided principal-ideal asymmetry
\[
\Delta(X)=\dim_k(XT_n(k))-\dim_k(T_n(k)X).
\]
Then \(0\le r\le n-1\), and **every integer** in the interval
\[
-r(n-r-1)\ \le\ \Delta(X)\ \le\ r(n-r-1)
\]
is attained by some rank-\(r\) matrix, over every field. Consequently,
\[
\max_{X\in J_n(k)}|\Delta(X)|=\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.
\]
For fixed \(r\), equality at the positive endpoint holds **if and only if** every row of \(X\) after row \(r\) is zero and the first \(r\) superdiagonal entries are nonzero:
\[
X_{ij}=0\quad(i>r),\qquad X_{i,i+1}\ne0\quad(1\le i\le r).
\]
This endpoint locus is isomorphic as a reduced algebraic variety over \(k\) to
\[
(\mathbb G_m)^r\times\mathbb A^{rn-r(r+3)/2}.
\]
Over \(k=\mathbb F_q\), the exact number of positive-endpoint matrices of rank \(r\) is
\[
(q-1)^r q^{rn-r(r+3)/2}.
\]
The negative-endpoint locus is the image under reflection across the anti-diagonal followed by transposition, and has the same cardinality. For the global positive endpoint, the permissible ranks are precisely the integers maximizing \(r(n-r-1)\), namely \(\lfloor(n-1)/2\rfloor\) and \(\lceil(n-1)/2\rceil\) (count a repeated value only once).

## Assumptions and scope
All one-sided ideals are taken in the *unital* algebra \(T_n(k)\), not in its nonunital radical. Dimensions are vector-space dimensions over \(k\). Ordinary matrix rank is used. The interval assertion concerns **possible integer values** of \(\Delta\) at fixed rank, not their multiplicities. The geometric assertion refers to the reduced endpoint locus, presented explicitly as a torus times affine space; no scheme-theoretic statement about rank-determinantal intersections is required.

## Proof
**1. Principal-ideal dimensions from rank profiles.** Write \(X^{[j]}\) for the upper-left \(j\times j\) principal submatrix and \(X_{[i]}\) for the lower-right \((n-i+1)\times(n-i+1)\) principal submatrix. Independently varying column \(j\) of the triangular right factor shows that column \(j\) of \(XB\) ranges over the column space of \(X^{[j]}\). Likewise, independently varying row \(i\) of the triangular left factor shows that row \(i\) of \(BX\) ranges over the row space of \(X_{[i]}\). Thus
\[
\dim_k(XT_n)=\sum_{j=1}^{n}\operatorname{rank}(X^{[j]}),\qquad
\dim_k(T_nX)=\sum_{i=1}^{n}\operatorname{rank}(X_{[i]}).
\]

**2. Sharp rank-conditioned bound.** Since \(X\) is strictly upper triangular and has rank \(r\),
\[
\operatorname{rank}(X^{[j]})\le\min\{r,j-1\}.
\]
Consequently,
\[
\dim(XT_n)\le\sum_{j=1}^{n}\min\{r,j-1\}
=rn-\frac{r(r+1)}2.
\]
Deleting the first \(i-1\) rows reduces rank by at most \(i-1\); the remaining rows have their first \(i-1\) columns zero. Hence
\[
\operatorname{rank}(X_{[i]})\ge\max\{r-i+1,0\},
\quad\dim(T_nX)\ge\frac{r(r+1)}2.
\]
Subtracting gives \(\Delta(X)\le r(n-r-1)\). The map \(X\mapsto FX^{\mathsf T}F\), where \(F\) is the anti-diagonal permutation matrix, is an involutive algebra anti-automorphism of \(T_n(k)\), preserves the radical and rank, and exchanges the two principal-ideal dimensions. This proves the negative bound.

**3. Necessity and sufficiency at the positive endpoint.** Equality in the bound requires equality separately in the upper and lower estimates. The leading \((r+1)\times(r+1)\) strictly triangular corner must have rank \(r\). Its only possibly nonzero maximal minor is formed from its first \(r\) rows and columns numbered \(2,\ldots,r+1\), and this minor has determinant \(\prod_{i=1}^{r}X_{i,i+1}\). Therefore those \(r\) superdiagonal entries are nonzero. Equality in the lower-rank sum forces \(\operatorname{rank}(X_{[r+1]})=0\); equivalently, every row after row \(r\) vanishes. Conversely, these two conditions force \(\operatorname{rank}(X)=r\), every leading principal rank to be \(\min\{r,j-1\}\), and every trailing principal rank to be \(\max\{r-i+1,0\}\), so the upper bound is attained. There are \(rn-r(r+1)/2\) strictly upper triangular positions in the first \(r\) rows. Precisely \(r\) of their coordinates must be invertible, giving the torus-affine product and the stated finite-field count.

**4. No gaps in the spectrum.** For a partial-permutation matrix with \(r\) nonzero entries in distinct rows \(i_a\) and distinct columns \(j_a\), all satisfying \(i_a<j_a\), the two profile formulas reduce to
\[
\Delta(X)=\sum_{a=1}^{r}(n+1-i_a-j_a).
\]
Begin with the placements \((i_a,j_a)=(a,a+1)\) for \(1\le a\le r\); they have \(\Delta=r(n-r-1)\). Move the columns, one unit at a time, in descending order of \(a\), from \(a+1\) to \(n-r+a\). Then move the rows, one unit at a time, in descending order of \(a\), from \(a\) to \(n-r+a-1\). At every move the row and column coordinates remain distinct and satisfy \(i_a<j_a\), so matrix rank stays \(r\), while \(\Delta\) decreases by exactly one. The final placements \((n-r+a-1,n-r+a)\) yield \(-r(n-r-1)\). The construction works over every field (take all nonzero entries equal to \(1\)) and also covers \(r=0\) or \(r=n-1\) with an empty move sequence. All intermediate integer values occur. Maximizing \(r(n-r-1)\) for integer \(0\le r\le n-1\) gives the global formula.

## Verification
The accompanying standalone `check.py` enumerates all strictly upper triangular matrices in thirteen field-and-size instances, including extension-field arithmetic over \(\mathbb F_4\). It independently constructs spans of products with triangular matrix units in the smaller instances, compares them with the principal-corner rank formulas, and checks the rank-wise interval, both endpoint counts, and the necessity of the positive endpoint conditions. The successful output is `TRIANGULAR_ONE_SIDED_GAP_OK 13 exhaustive field-and-size cases`. Exhaustive finite cases corroborate but do not substitute for the unrestricted-field proof.

## Relationship to prior work
Rahimi-Alangi and Yahaghi (2015), Corollary 2.5, already give the componentwise row/column descriptions of principal one-sided ideals of upper triangular matrix rings. Our leading/trailing rank-profile identities in Step 1 are an elementary dimension consequence of that prior result and **are not claimed as new**. Their Theorem 2.6 classifies which one-sided nest submodules are principal. It does not state the **joint fixed-matrix-rank extremal difference** between the left and right principal-ideal dimensions, the gap-free spectrum of all attainable integer differences, or the torus-affine equality locus and its exact count. Arias-Castro, Diaconis and Stanley analyze the left-right unitriangular action on the radical via superclass labels and sparse representatives; this also supplies relevant structural background, but does not state the extremal difference result. Yip develops finite-field rank and Jordan-type counts through nonattacking rook placements; rank and Jordan type alone do not determine the sign of the gap (in size four, the rank-one matrix units \(E_{12}\) and \(E_{34}\) have gaps \(+2\) and \(-2\)). Ferraz, Polcino Milies and Taufer analyze one-sided ideals of *full* matrix rings, whose left/right principal-ideal dimensions coincide. Our claimed addition is the sharp gap law, its full rank-conditioned spectrum, and the complete equality classification; no absolute publication priority is asserted.

## Limitations
The theorem concerns generators in the radical of the *full* triangular algebra and does not address arbitrary pattern subalgebras, general radical elements in nonchain incidence algebras, or the exact number of matrices at **intermediate** gap values. The algebraically defined endpoints are reduced smooth loci; possible scheme-theoretic enhancements elsewhere are not considered. Existing nest-module principal-ideal classifications, as well as superclass/rook frameworks, may permit indirect reconstructions of the new extremal statements, so their priority should receive independent literature review.

## References
1. E. Arias-Castro, P. Diaconis and R. P. Stanley, *A super-class walk on upper-triangular matrices*, Journal of Algebra **278** (2004), 739–765, DOI: 10.1016/j.jalgebra.2004.04.005; openly accessible manuscript: https://www.math.ucsd.edu/~eariasca/papers/UniRW.pdf.
2. M. Yip, *q-Rook placements and Jordan forms of upper-triangular nilpotent matrices*, DMTCS Proceedings (FPSAC 2013), DOI: 10.46298/dmtcs.2362; openly accessible conference article: https://sites.math.washington.edu/~billey/classes/561.fall.2021/past.articles/Yip.2013.pdf.
3. R. A. Ferraz, C. Polcino Milies and E. Taufer, *Left ideals in matrix rings over finite fields*, preprint first posted 2017-11-25, arXiv:1711.09289, https://arxiv.org/abs/1711.09289.
4. M. Rahimi-Alangi and B. R. Yahaghi, *On nest modules of matrices over division rings*, Bulletin of the Iranian Mathematical Society **41** (2015), 47–63, arXiv:1508.00041; original manuscript https://arxiv.org/pdf/1508.00041, especially Corollary 2.5 and Theorem 2.6.
