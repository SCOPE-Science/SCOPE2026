# A two-dimensional degree-nine sampling blind spot on the regular rhombicuboctahedron

## Finding
Let \(a=1+\sqrt2\), and let \(X\subset\mathbb S^2\) be the 24 vertices obtained by all distinct coordinate permutations and independent sign choices of \((a,1,1)/\sqrt{a^2+2}\). This is the regular rhombicuboctahedron. Let \(E_\ell:\mathcal H_\ell(\mathbb S^2)\to\mathbb R^X\) evaluate real spherical harmonics of *exact* degree \(\ell\ge0\). Then
\[
\operatorname{rank}E_\ell=
\begin{cases}
2\ell+1,&0\le\ell\le5,\\
10,&\ell=9,\\
12,&\ell\ge6,\ \ell\ne9.
\end{cases}
\]
Every degree has the unavoidable antipodal-parity constraint \(f(-x)=(-1)^\ell f(x)\); hence 12 is the maximum rank. The first full-rank degree is 6, but degree 9 loses **two** additional data directions and full rank persists at all individual degrees \(\ell\ge10\). Thus the sharp persistent single-degree interpolation threshold is 10.

For explicit missing-data constraints, choose one representative of each antipodal pair by making its coordinate of magnitude \(a\) positive. Partition these 12 representatives into three four-point blocks \(X_i\) according to the location \(i\in\{1,2,3\}\) of \(+a\). Write the two remaining coordinates in increasing coordinate order as \((s,t)\in\{\pm1\}^2\) (before normalization). For every real degree-nine spherical harmonic \(f\), the three signed block sums
\[
S_i(f)=\sum_{s,t=\pm1}st\,f(x_{i,s,t})
\]
are **identical**: \(S_1(f)=S_2(f)=S_3(f)\). These two independent constraints exactly account for the degree-nine defect.

The defect is an isolated parameter resonance in the one-parameter family of configurations obtained from \((b,1,1)/\sqrt{b^2+2}\) for \(b>1\): degree-nine interpolation is full for \(b=2\), and the exceptional \(b=a\) is an isolated zero of the corresponding analytic Gram determinant. No classification of all exceptional \(b\) is claimed.

## Assumptions and scope
The sphere is the unit two-sphere with normalized surface measure. \(\mathcal H_\ell\) consists only of restrictions of homogeneous harmonic polynomials of degree \(\ell\), and \(\dim\mathcal H_\ell=2\ell+1\). The domain is the 24-point set above, not the surface, faces, graph metric, or a lower-order polynomial band. Surjectivity always means onto the 12-dimensional space of antipodal-parity-compatible real data. All degrees \(\ell\) are nonnegative integers.

## Proof
**Reduction to a twelve-point Legendre Gram matrix.** The spherical addition theorem gives, up to the positive factor \(2\ell+1\), the evaluation Gram matrix \(G_\ell=[P_\ell(\langle x_i,x_j\rangle)]_{i,j=1}^{12}\), where \(P_\ell(1)=1\) is the ordinary Legendre polynomial and the \(x_i\) are the twelve representatives selected above. Since evaluation at the antipodes is determined by parity, \(\operatorname{rank}E_\ell=\operatorname{rank}G_\ell\). The diagonal entries of \(G_\ell\) are 1. Distinct representatives have pairwise inner products drawn from
\[
\left\{\pm\frac{7+4\sqrt2}{17},\quad
\pm\frac{8\sqrt2-3}{17},\quad
\pm\frac{5-2\sqrt2}{17}\right\}.
\]
In particular their absolute values are bounded by \(t_*=(7+4\sqrt2)/17<1\).

**Finite exact ranks.** Use the Legendre recurrence
\[
P_0(t)=1,\quad P_1(t)=t,\quad
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t).
\]
The standalone `checker.py` constructs the 12 representatives in the field \(\mathbb Q(\sqrt2)\), checks two exact null vectors for \(G_9\), and evaluates all \(G_\ell\) for \(0\le\ell\le115\) modulo the prime \(p=998244353\) using the residue \(\sqrt2\mapsto116195171\). The prime is certified by \(p-1=2^{23}\cdot7\cdot17\) and the primitive-root witness 3. All recurrence denominators are invertible modulo \(p\). The modular ranks are \(1,3,5,7,9,11\) at degrees 0 through 5; they are 12 at degrees 6,7,8 and 10 through 115, and 10 at degree 9. A nonzero modular minor proves the corresponding minor is nonzero in characteristic zero. The dimension bound \(2\ell+1\) matches each low-degree rank.

**Exact upper bound at degree nine.** For \(i\in\{1,2,3\}\), let \(u_i\in\mathbb Q^{12}\) be supported on the \(i\)-th block, with four entries \((1,-1,-1,1)\) in sign order \((+,+),(+,-),(-,+),(-,-)\). Direct recurrence in \(\mathbb Q(\sqrt2)\) proves \(G_9(u_1-u_2)=G_9(u_1-u_3)=0\). The same check gives the three-by-three compression
\[
\frac14[u_i^\mathsf TG_9u_j]_{i,j=1}^3
=\frac{160453920-84575040\sqrt2}{410338673}
\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}.
\]
The two differences are independent, so the exact rank is at most 10. The modular rank-10 minor proves equality. By Gram positive semidefiniteness, a vector is in its kernel if and only if it is orthogonal to all degree-nine evaluation vectors. This yields the two stated block-sum identities.

**All remaining degrees.** The sharp classical Bernstein bound for Legendre polynomials states, for \(\ell\ge1\) and \(-1<t<1\),
\[
|P_\ell(t)|\le\sqrt{\frac{2}{\pi(\ell+1/2)\sqrt{1-t^2}}}.
\]
For the present off-diagonal arguments, \(\sqrt{1-t^2}>2/3\), since \(t_*^2<5/9\), an elementary inequality in \(\mathbb Q(\sqrt2)\). For every \(\ell\ge116\), the sum of the eleven off-diagonal absolute values in a row of \(G_\ell\) is strictly less than
\[
11\sqrt{\frac{2}{(157/50)(116+1/2)(2/3)}}<1,
\]
where \(\pi>157/50\). Thus \(G_\ell\) is strictly diagonally dominant, symmetric, and positive definite for every \(\ell\ge116\). Together with the finite exact ranks, this covers all degrees.

**Isolated exceptional parameter.** For \(b>1\) the degree-nine Gram determinant is real-analytic in \(b\). The same modular calculation at \(b=2\) gives nonzero determinant, so the analytic determinant is not identically zero. Its zero at \(b=1+\sqrt2\) is therefore isolated.

## Verification
Run `python3 checker.py` with Python 3. It requires only the standard library, and checks the quadratic-field identities, two explicit null relations at degree nine, the exact rational compression scalar, all finite modular ranks through degree 115, the primality witness and quadratic residue, the rational high-degree inequality, and full degree-nine rank at \(b=2\). The computation makes no claim that finite enumeration by itself controls higher degrees: that step is supplied by Bernstein's analytic inequality and strict diagonal dominance. The actual output ends with `ALL CHECKS PASSED`.

## Relationship to prior work
Dai and Xu (2013), Section 3, formulate the spherical-harmonic fundamental-system and zonal-Gram criterion and prove the existence of generic systems. Their statement does not determine evaluation rank degree-by-degree on the fixed rhombicuboctahedral orbit. De Rossi (2014) studies zonal-basis-plus-harmonic local interpolation of scattered spherical data, not exact-degree rank on this regular 24-node set. Wang, Le Gia, Sloan, and Womersley (2015) develop discrete needlet and cubature approximation with polynomial bands, not the present all-degree sampling classification. Other Archimedean vertex sets have different pairwise-angle multisets and their rank calculations do not imply these two degree-nine identities. The contribution is the *specific complete exact-degree rank profile* and its two-dimensional ninth-degree defect, not the addition theorem, interpolation criterion, the polyhedron itself, or generic eventual diagonal dominance.

## Limitations
Independent mathematical audit and independent validation have not been performed. The comparison to known literature is bounded and cannot rule out an earlier equivalent unindexed tabulation. The result establishes ranks and existence of interpolants but not sharp singular values or numerical conditioning of interpolation. Parameter resonance is proved isolated at the regular shape; no exhaustive classification of other shape parameters is attempted.

## References
1. F. Dai and Y. Xu, *Spherical Harmonics*, original arXiv posting 2013-04-09, arXiv:1304.2585, especially Sections 2, 3, and 6. https://arxiv.org/abs/1304.2585
2. A. De Rossi, *Hybrid spherical approximation*, original arXiv posting 2014-04-05, arXiv:1404.1475, Sections 2–5. https://arxiv.org/abs/1404.1475
3. Y. G. Wang, Q. T. Le Gia, I. H. Sloan, and R. S. Womersley, *Fully discrete needlet approximation on the sphere*, original arXiv posting 2015-02-20, arXiv:1502.05806, Sections 1 and 5. https://arxiv.org/abs/1502.05806
4. G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, 4th ed., 1975, Section 7.3 (classical Bernstein bound).
