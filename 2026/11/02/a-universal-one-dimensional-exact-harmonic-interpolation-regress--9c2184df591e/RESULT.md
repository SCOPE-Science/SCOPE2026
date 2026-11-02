# A universal one-dimensional exact-harmonic interpolation regression on cube vertices

## Finding
For every integer \(d\ge3\), put
\[
 X_d=\{d^{-1/2}(\varepsilon_1,\ldots,\varepsilon_d):\varepsilon_i\in\{-1,1\}\}\subset S^{d-1},
\]
and let \(E_{d,k}\) evaluate all real homogeneous harmonic polynomials of exact degree \(k\) at \(X_d\). For every integer \(0\le k\le d+2\),
\[
\operatorname{rank}E_{d,k}
=\sum_{\substack{0\le j\le\min\{d,k\}\\j\equiv k\pmod2}}\binom dj
-\mathbf1_{\{k=2\}}-\mathbf1_{\{k=d+2\}}.
\]
In particular, the full antipodal-parity rank \(2^{d-1}\) occurs at degrees \(d\) and \(d+1\), but at degree \(d+2\) the rank drops to \(2^{d-1}-1\). Among degree-\(d+2\) data of the appropriate antipodal parity, the **unique extra annihilating functional up to scale** has weights
\[
 w(\varepsilon)=\prod_{i=1}^d\varepsilon_i,
 \qquad \sum_{\varepsilon\in\{-1,1\}^d}w(\varepsilon)H(\varepsilon/\sqrt d)=0
 \quad (H\in\mathcal H_{d+2}(\mathbb R^d)).
\]
For \(d\ge4\), full parity-compatible interpolation first occurs already at degree \(d-1\); for \(d=3\) the first full degree is \(3\). Thus the deficit at degree \(d+2\) is a genuine regression after full interpolation, not a low-degree dimension obstruction.

## Assumptions and scope
Here \(\mathcal H_k(\mathbb R^d)=\{H\in\mathbb R[x_1,\ldots,x_d]:H\text{ homogeneous of degree }k,\ \Delta H=0\}\), with \(\Delta=\sum_i\partial_{x_i}^2\). The rank is that of the real evaluation map into \(\mathbb R^{2^d}\). Its image consists of functions satisfying \(f(-\varepsilon)=(-1)^k f(\varepsilon)\), so the maximal allowable rank is \(2^{d-1}\). All quantifiers above include every integer \(d\ge3\) and every \(k\) in the stated interval; no assertion is made for \(k>d+2\).

## Proof
**1. Walsh reduction.** For \(S\subseteq[d]\), write \(\chi_S(\varepsilon)=\prod_{i\in S}\varepsilon_i\). The \(2^d\) characters form an orthogonal basis of functions on cube vertices. A degree-\(k\) polynomial, after evaluation at \(\varepsilon/\sqrt d\), uses only characters with \(|S|\le k\) and \(|S|\equiv k\pmod2\): expand monomials and use \(\varepsilon_i^2=1\). This proves the summation bound before the two stated corrections.

**2. Every nonempty proper Walsh level occurs.** Take \(\varnothing\ne S\subsetneq[d]\), \(j=|S|\), and an integer \(k=j+2s\) with \(s\ge0\). Select \(b\in S\), \(a\notin S\), and define
\[
 H(x)=\Bigl(\prod_{i\in S\setminus\{b\}}x_i\Bigr)
 \operatorname{Im}(x_a+i x_b)^{2s+1}.
\]
The second factor is harmonic in its two variables since \(1+i^2=0\), while the first is multilinear in disjoint variables; therefore \(\Delta H=0\). On cube vertices its value is a nonzero constant times \(\chi_S\): indeed \(\operatorname{Im}(1+i)^{2s+1}=\pm2^s\ne0\). Thus all such Walsh levels are in the evaluation image.

**3. The empty Walsh level.** For \(k=0\) the constant polynomial works. For \(k=2\), every harmonic quadratic \(H\) has zero cube average, because the second moment matrix of the uniform cube is \(I_d/d\) and the quadratic coefficient matrix of \(H\) has trace zero. For even \(k\ge4\), choose complex numbers \(z_i\) with \(\sum_i z_i^2=0\). Then \((z\cdot x)^k\) is harmonic, so a nonzero cube average of this complex harmonic supplies a real harmonic with nonzero average. If \(k\equiv0\pmod4\), take \(z=(1,i,0,\ldots,0)\). Its cube average before spatial normalization is \(\operatorname{Re}(1+i)^k=(-1)^{k/4}2^{k/2}\ne0\). If \(k\equiv2\pmod4\), necessarily \(k\ge6\). Take
\[
 z(t)=(1,i\sqrt{1+t^2},t,0,\ldots,0),\qquad
 F_k(t)=2^{-d}\sum_\varepsilon(z(t)\cdot\varepsilon)^k.
\]
The vector is null for every real \(t\) near zero, and direct binomial expansion gives
\[
 F_k(t)=\frac{k(k-2)}2(-1)^{(k-2)/4}2^{(k-2)/2}t^2+O(t^4).
\]
Its leading coefficient is nonzero, proving that the empty Walsh character is present at every even degree \(k\ge4\). Normalization of vertex coordinates multiplies these averages by the nonzero factor \(d^{-k/2}\).

**4. The top Walsh level and its exceptional disappearance.** At degree \(k=d\), the multilinear polynomial \(\prod_i x_i\) is harmonic and evaluates to a nonzero multiple of \(\chi_{[d]}\). At degree \(k=d+2\), given any harmonic homogeneous \(H\), project onto the sign character \(\chi_{[d]}\):
\[
 Q(x)=2^{-d}\sum_{\varepsilon\in\{-1,1\}^d}\chi_{[d]}(\varepsilon)
 H(\varepsilon_1x_1,\ldots,\varepsilon_dx_d).
\]
Sign changes commute with the Laplacian, hence \(Q\) is harmonic of degree \(d+2\) and is odd in each variable. Degree counting forces
\[
 Q(x)=\Bigl(\prod_i x_i\Bigr)\sum_i a_i x_i^2.
\]
Applying the Laplacian gives \(\Delta Q=6(\sum_i a_i)\prod_i x_i\), whence \(\sum_i a_i=0\). Therefore \(Q\) vanishes at every cube vertex, and the \(\chi_{[d]}\)-Fourier coefficient of each evaluated degree-\(d+2\) harmonic is zero.

**5. Assemble ranks.** Steps 1--4 give every allowed nonzero proper Walsh component, the empty component except at \(k=2\), and the top component at \(k=d\) but not \(k=d+2\). Orthogonality of characters gives the displayed rank formula and the unique parity-compatible annihilator. At \(k=d,d+1\), all parity-compatible characters occur, giving rank \(2^{d-1}\). For \(d\ge4\), this already happens at \(k=d-1\); at every smaller \(k\), at least one maximal-parity Walsh level has size greater than \(k\), so rank is smaller. For \(d=3\), the missing constant at degree \(2\) moves the first full degree to \(3\).

## Verification
The standalone Python file `check_cube_ranks.py` computes the exact rational Gegenbauer kernel eigenvalues on Walsh levels. For \(3\le d\le12\), it checks all \(0\le k\le d+2\) against the claimed support and multiplicities using the generating identity \(\sum_hK_h(j)z^h=(1-z)^j(1+z)^{d-j}\), with \(K_h(j)\) the binary Krawtchouk coefficients. It also checks the elementary nonzero witness coefficients. Run `python check_cube_ranks.py`; observed output: `CUBE_EXACT_DEGREE_RANK_OK 975 exact Krawtchouk spectral checks; 10 dimensions`. The general theorem is proved by the harmonic polynomial constructions above; the finite checks do not establish infinite-dimensional validity.

## Relationship to prior work
Bannai--Okuda--Tagami's study of harmonic-index spherical designs and Zhu--Bannai--Bannai--Kim--Yu's subsequent treatment concern when an *unweighted* sum of exact-degree harmonic evaluations vanishes. This is the empty Walsh character, whereas the degree-\(d+2\) obstruction here is the **full alternating Walsh character**, and the result also establishes interpolation of every other compatible Walsh character. The harmonic-index design results therefore do not directly imply the theorem. Classical Hamming-scheme and Gegenbauer methods supply background diagonalization machinery; this proof instead gives explicit harmonic witnesses. The full text of Lloyd's earlier work on Hamming associators could not be inspected, leaving possible historical equivalence unresolved. No unique priority or independent verification is asserted.

## Limitations
The exact rank formula is established only through degree \(d+2\), not at every higher degree. It concerns equal-radius cube corners, unweighted evaluation, and exact-degree (not cumulative-degree) real spherical harmonics. It gives no singular-value or numerical conditioning bound. The novelty comparison is bounded by available full texts and research records; an inaccessible historical source remains a risk.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first released 2013-08-23. https://arxiv.org/abs/1308.5101
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373v1, first released 2015-07-20. https://arxiv.org/abs/1507.05373
3. S. P. Lloyd, *Hamming Association Schemes and Codes on Spheres*, SIAM J. Math. Anal. 11 (1980), 488--505, doi:10.1137/0511047. Historical related source; full text was not inspected.
