# Spatial ear law and complete covariance spectrum of uniform convex-polygon triangulations

## Finding
Let \(E_i\) mark an ear at cyclically labeled vertex \(i\) of a uniformly random triangulation of a convex \(n\)-gon. For every \(n\ge5\), the complete joint moment law is
\[
\mathbb P(E_i=1\text{ for all }i\in S)=
\begin{cases}
0,&\text{if }S\text{ contains two cyclic neighbors},\\
C_{n-|S|-2}/C_{n-2},&\text{otherwise},
\end{cases}
\]
where \(C_m=\binom{2m}{m}/(m+1)\). In particular, all nonneighbor pairs have *positive* covariance and cyclic neighbors have *negative* covariance.

Writing \(p=C_{n-3}/C_{n-2}\), \(q=C_{n-4}/C_{n-2}\), the real symmetric covariance matrix \(\Sigma_n\) of \((E_0,\ldots,E_{n-1})\) has complete Fourier spectrum
\[
\lambda_0=\frac{(n-5)(n-4)(n-1)}{2(2n-7)(2n-5)^2},\qquad
\lambda_j=p-q-2q\cos(2\pi j/n),\quad 1\le j<n.
\]
Consequently \(\operatorname{rank}\Sigma_5=4\) and \(\operatorname{rank}\Sigma_n=n\) for every \(n\ge6\). The limiting local process is a one-dependent fair-bit pattern process \(Y_i=\mathbf 1\{B_i=0,B_{i+1}=1\}\), with independent \(\operatorname{Bernoulli}(1/2)\) bits \(B_i\).

## Assumptions and scope
The vertices are distinct, cyclically labeled \(0,\ldots,n-1\), and in convex position. Every triangulation by noncrossing diagonals is equally likely; there are \(C_{n-2}\) such triangulations. An ear at \(i\) is precisely a triangular face whose two boundary sides meet at \(i\), equivalently there is no internal diagonal incident to \(i\). The statement covers every integer \(n\ge5\), every set \(S\) of vertices, and every Fourier index. For completeness, at \(n=4\) the two possible triangulations yield covariance rank one, unlike the \(n\ge5\) regime. The limit uses any fixed finite ordered block of polygon vertices away from the chosen cyclic cut, then \(n\to\infty\).

## Proof
**Joint inclusions.** Two adjacent vertices cannot both be ears: their proposed ear diagonals cross. If \(S\) is cyclically independent and \(k=|S|\), prescribing those ears forces the \(k\) diagonals joining the respective neighboring vertices. Deleting the \(k\) ear vertices leaves a convex \((n-k)\)-gon and bijects the triangulations containing all prescribed ear faces with all its triangulations. Since \(k\le\lfloor n/2\rfloor\), this polygon has at least three vertices. There are therefore exactly \(C_{n-k-2}\) completions. Dividing by \(C_{n-2}\) proves the joint moment formula. It determines the full joint law by inclusion-exclusion; no independence assumption is used.

**Covariance.** A fixed ear has probability
\[
p=\frac{C_{n-3}}{C_{n-2}}=\frac{n-1}{2(2n-5)}.
\]
Two distinct nonneighbor ears have joint probability
\[
q=\frac{C_{n-4}}{C_{n-2}}=\frac{(n-1)(n-2)}{4(2n-5)(2n-7)}.
\]
Adjacent ears have joint probability zero. Hence, with \(i,j\) understood modulo \(n\),
\[
\Sigma_n(i,j)=
\begin{cases}
p(1-p),&i=j,\\
-p^2,&j-i\equiv\pm1,\\
q-p^2,&\text{otherwise}.
\end{cases}
\]
Direct cancellation gives the strictly positive distant covariance
\[
q-p^2=\frac{3(n-1)}{4(2n-7)(2n-5)^2}>0.
\]

**Full spectrum and rank.** Write \(J\) for the all-ones matrix and \(H\) for the adjacency matrix of the cyclic \(n\)-vertex graph. The exact decomposition
\[
\Sigma_n=(p-q)I-qH+(q-p^2)J
\]
is a polynomial in commuting circulant matrices. On the constant vector it has eigenvalue \(p+(n-3)q-np^2\), which simplifies to the stated \(\lambda_0\). On Fourier mode \(j\ne0\), \(J\) vanishes and \(H\) has eigenvalue \(2\cos(2\pi j/n)\), yielding \(\lambda_j\).

For \(n\ge8\),
\[
p-3q=\frac{(n-1)(n-8)}{4(2n-5)(2n-7)}\ge0,
\]
so \(\lambda_j=(p-3q)+2q(1-\cos(2\pi j/n))>0\) for each \(j\ne0\). For \(n=6\), \(p=5/14\), \(q=1/7\), and the maximum nonconstant cosine equals \(1/2\), implying \(\lambda_j\ge1/14\). For \(n=7\), \(p=1/3\), \(q=5/42\) and \(\cos(2\pi/7)<9/10\), which gives strict positivity. For \(n=5\), \(p=2/5\), \(q=1/5\), and \(\cos(2\pi/5)<1/2\), again yielding strict positivity. Finally \(\lambda_0=0\) only at \(n=5\), and is positive for every \(n\ge6\). This proves the ranks, including the constant-sum constraint for the pentagon.

**Local limit.** For a fixed finite subset \(S\) of cyclic positions, the joint inclusion moments are either zero (some two selected positions adjacent) or \(C_{n-|S|-2}/C_{n-2}\to4^{-|S|}\). If \(B_i\) are independent fair bits and \(Y_i=\mathbf 1\{B_i=0,B_{i+1}=1\}\), then the same joint inclusion moments hold: adjacent indicated occurrences conflict, whereas nonadjacent occurrences constrain disjoint bit pairs and have probability \(4^{-|S|}\). Möbius inversion of joint binary moments implies convergence of all finite-block laws. Therefore the limiting covariance is \(3/16\) on the diagonal, \(-1/16\) on neighboring indices, and zero elsewhere. Its Fourier symbol is \(3/16-(1/8)\cos\theta\). The total ear-count variance is exactly \(n\lambda_0\sim n/16\).

## Verification
The companion standalone script `verify_ears.py` uses only Python's standard library. Execute `python verify_ears.py`. It recursively enumerates every triangulation for \(4\le n\le11\), checks all \(\sum_{n=4}^{11}2^n=4080\) subsets of prescribed ears against exact Catalan counts, calculates exact-rational covariance matrices and their ranks, verifies each stated Fourier eigenvalue numerically on its actual eigenvector, and checks all \(256\) mixed joint moments of eight positions in the fair-bit model. It also tests illustrative Catalan-ratio convergence values. The run passed all checks (6,916 enumerated triangulations); finite enumeration does not prove the all-size statements, which follow from the above bijection and spectral calculation. The covariance-rank check uses exact rational Gaussian elimination.

## Relationship to prior work
Hurtado and Noy (1996) enumerate polygon triangulations by their **total** number of ears and give Catalan identities. Devroye, Flajolet, Hurtado, Noy and Steiger (1999) study random-triangulation degree maxima, longest diagonals and related statistics. Asinowski and Regev (arXiv:1309.0743, version 1 posted 2013-09-03) classify symmetry classes of triangulations with two and three ears and count certain disjoint triangulations. Alexandersson, Linusson, Potka and Uhlin (arXiv:2010.11157) treat Catalan and Narayana cyclic sieving, including refinements by the total ear number. Those ear-count and symmetry results are not asserted to be new here. The evaluated result concerns *labeled ear locations*, all their mixed moments, the exact full position covariance spectrum, and their local weak-limit process. General Catalan ear deletion is elementary and motivates the proof, but a total-ear distribution alone does not specify site-labeled mixed moments without additional positional arguments.

## Limitations
This concerns uniform triangulations of convex polygons, not arbitrary polygon geometry or nonuniform triangulation measures. The weak limit is finite-dimensional, not a claimed functional central limit theorem. Historical priority is not independently certified: some components could have been implicitly covered by earlier general Catalan-enumeration formulas. The 1996 Hurtado–Noy paper was available through indexed excerpts rather than a complete inspected full text, so a direct whole-document exclusion of prior coverage is not claimed. All computations corroborate but do not substitute for the infinite-size proof.

## References
1. F. Hurtado and M. Noy, *Ears of triangulations and Catalan numbers*, Discrete Mathematics **149** (1996), 319–324. Available abstract and indexed text: https://core.ac.uk/download/pdf/82091698.pdf .
2. L. Devroye, P. Flajolet, F. Hurtado, M. Noy and W. Steiger, *Properties of Random Triangulations and Trees*, Discrete & Computational Geometry **22** (1999), 105–117. DOI: https://doi.org/10.1007/PL00009444 .
3. A. Asinowski and A. Regev, *Triangulations with few ears: symmetry classes and disjointness*, arXiv:1309.0743, initial public posting 2013-09-03. https://arxiv.org/abs/1309.0743 .
4. P. Alexandersson, S. Linusson, S. Potka and J. Uhlin, *Refined Catalan and Narayana cyclic sieving*, arXiv:2010.11157 (2020). https://arxiv.org/abs/2010.11157 .
