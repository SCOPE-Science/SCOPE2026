# Exact all-degree harmonic interpolation ranks on the icosidodecahedron

## Finding
Let \(X\subset S^2\) be the 30 vertices of a regular icosidodecahedron, realized as normalized edge midpoints of a regular icosahedron. For every integer \(\ell\ge0\), let \(E_\ell\) evaluate real spherical harmonics of **exact** degree \(\ell\) at \(X\), using any orthonormal harmonic basis and the sampling normalization in the next section. Then
\[
\operatorname{rank} E_\ell=\begin{cases}
2\ell+1,&0\le\ell\le5,\\
10,&\ell=6,\\
14,&\ell\in\{8,14\},\\
15,&\ell\ge7,\ \ell\notin\{8,14\}.
\end{cases}
\]
The sharp threshold for **eventual** surjectivity onto the 15-dimensional antipodal-parity-compatible sample space is degree \(15\), although degree \(7\) and degrees \(9\) through \(13\) already attain rank \(15\). At degrees \(8\) and \(14\), the sole missing compatible sample direction is the constant vector. At degree \(6\), the compatible-sector nullity is five. These are ranks of exact-degree evaluation maps, not multidegree bandwidths.

## Assumptions and scope
Put \(\varphi=(1+\sqrt5)/2\) and form the twelve vectors
\[
V=\{(0,a,b\varphi),(a,b\varphi,0),(b\varphi,0,a):a,b\in\{-1,1\}\}.
\]
For each unordered pair \(v,w\in V\) with \(\|v-w\|^2=4\), form \(x=(v+w)/(2\varphi)\); the thirty points so obtained comprise \(X\). The normalization \(\|x\|=1\) follows from \(\|v\|^2=1+\varphi^2\) and \(v\cdot w=\varphi\). Select any one representative from each of the fifteen antipodal pairs to form \(Y=\{y_1,\ldots,y_{15}\}\).

Let \(\mathcal H_\ell\) be the real space of degree-\(\ell\) spherical harmonics, orthonormalized in the probability surface-area measure on \(S^2\). The sampling map takes \(f\in\mathcal H_\ell\) to \(\bigl(f(x)/\sqrt{2\ell+1}\bigr)_{x\in X}\). The image obeys \(f(-x)=(-1)^\ell f(x)\), and its ambient compatible-data subspace has dimension \(15\).

## Proof
**Addition formula and geometric reduction.** The normalized spherical-harmonic addition theorem identifies the \(30\times30\) sampling Gram matrix with \(P_\ell(x\cdot x')\), where \(P_\ell\) is the Legendre polynomial normalized by \(P_\ell(1)=1\). In the order \((Y,-Y)\), this Gram matrix is
\[
\begin{pmatrix}B_\ell&(-1)^\ell B_\ell\\(-1)^\ell B_\ell&B_\ell\end{pmatrix},
\qquad (B_\ell)_{ij}=P_\ell(y_i\cdot y_j).
\]
Thus \(\operatorname{rank}E_\ell=\operatorname{rank}B_\ell\). Every row of the exact dot-product matrix \(T=(y_i\cdot y_j)\) has one diagonal \(1\), exactly two zero off-diagonal entries, and exactly four entries at each of the absolute values
\[
\frac{\sqrt5-1}{4},\qquad\frac12,\qquad\frac{\sqrt5+1}{4}.
\]
This is obtained directly from the listed edge-midpoint coordinates and is also checked exactly in the accompanying construction.

**Exceptional finite ranks, without floating-point inference.** In the field \(\mathbb Q(\sqrt5)\), use \(P_0(t)=1\), \(P_1(t)=t\), and the exact recurrence
\[
(n+1)P_{n+1}(t)=(2n+1)tP_n(t)-nP_{n-1}(t).
\]
Exact Gaussian elimination on the explicitly constructed \(15\times15\) matrices \(B_\ell\) for \(0\le\ell\le14\) gives the rank sequence
\[
(1,3,5,7,9,11,10,15,14,15,15,15,15,15,14).
\]
The complete finite elimination is specified and executable in `verify.py`: algebraic numbers are represented as pairs of reduced rational coefficients, and no approximate rank tolerance is used. As a separate exact check, the Gram matrix \(2B_6\) annihilates the polynomial
\[
q(t)=t\left(t-\frac{315}{512}\right)
\left(t-\frac{165}{128}\right)\left(t-\frac{21}{4}\right).
\]
At degrees \(8\) and \(14\), direct recurrence substitution gives \(B_\ell\mathbf1=0\); the exact rank \(14\) shows this is the complete kernel. The rank \(10\) at degree \(6\) follows from independent exact elimination, not merely from the displayed polynomial.

**Finite-field certificate for the remaining bounded range.** Choose the prime \(p=1000000009\). Since \(383008016^2\equiv5\pmod p\), reduction \(a+b\sqrt5\mapsto a+383008016b\pmod p\) maps the rational-algebraic coordinates, with their denominators, into \(\mathbb F_p\). Here every Legendre recurrence denominator \(1,\ldots,200\) is invertible. The attached checker computes \(\operatorname{rank}_{\mathbb F_p}B_\ell=15\) for each of the **185** degrees \(15\le\ell\le199\) by exact modular elimination. A full modular rank certifies full rank over \(\mathbb Q(\sqrt5)\), because a nonzero reduced determinant cannot originate from a zero algebraic determinant. It does not use numerical approximation or extrapolation.

**All higher degrees analytically.** For every \(n\ge200\) and \(|t|<1\), the classical Bernstein bound is
\[
|P_n(t)|\le\sqrt{\frac2{\pi(n+1/2)}}(1-t^2)^{-1/4}.
\]
Since \((\sqrt5-1)/4<1/3\) and \((\sqrt5+1)/4<5/6\), the fourth-root factors in the three off-diagonal groups are bounded above by \(10/9,10/9,10/7\) respectively; the factor for zero is \(1\). Hence every off-diagonal absolute row sum is bounded by
\[
\sqrt{\frac2{\pi(n+1/2)}}
\left(2+\frac{80}{9}+\frac{40}{7}\right)
<\frac{1046}{63\sqrt{300}}<1,
\]
using \(\pi>3\) and \(n\ge200\). Since \(B_n\) is real symmetric with diagonal \(1\), strict diagonal dominance makes it positive definite. This proves all remaining degrees and completes the infinite classification.

## Verification
`verify.py` uses only Python's standard library. Running `python verify.py` reconstructs \(V,X,Y,T\), performs exact arithmetic over \(\mathbb Q(\sqrt5)\) through degree \(14\), verifies a sextic matrix polynomial identity, proves the stated modular ranks through degree \(199\), and prints the finite certificates reproduced in `verify_output.txt`. The elementary Bernstein inequality closes every higher degree. `crosscheck.py` independently constructs complex spherical-harmonic evaluation matrices using SciPy and checks degrees \(0\) to \(16\), with results in `crosscheck_output.txt`. This numerical cross-check is not part of the infinite proof.

## Relationship to prior work
Bannai, Okuda and Tagami introduced harmonic-index designs and explicitly noted degree-eight and degree-fourteen design phenomena for the **twelve-vertex icosahedron**, not the degree-by-degree rank classification of the **thirty-vertex icosidodecahedron**. Zhu, Bannai, Bannai, Kim and Yu extended design and tightness criteria; their general bounds do not supply the rank table of this separate orbit. Classical icosahedral-harmonic tables can potentially contain equivalent low-degree information; in particular, Cohan's representation tables through degree fourteen are a relevant historical comparison whose complete text was not accessible. Zheng and Doerschuk give an explicit invariant-harmonic construction, but only for the trivial icosahedral representation in the accessible abstract. Such invariant-sector information alone cannot determine every evaluation rank. The present claim addresses all degrees of the edge-midpoint orbit via an exact finite-field certificate plus a large-degree positivity argument. No claim of settled historical priority or independent validation is made.

## Limitations
This classification concerns one canonical orbit and exact-degree sampling; it does not determine singular values or uniform conditioning, nor sampling on arbitrary subsets, and it does not classify all icosahedrally symmetric point configurations. The computational certificate for the finite range is an integral part of the proof and must accompany the statement. Older group-harmonic tables may contain implications not identified in the accessible material. Independent specialist review has not been performed.

## References
1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1 (first public version 2013-08-23), https://arxiv.org/pdf/1308.5101.
2. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373 (first public version 2015-07-20), https://arxiv.org/pdf/1507.05373.
3. N. V. Cohan, *The spherical harmonics with the symmetry of the icosahedral group*, Math. Proc. Cambridge Philos. Soc. **54** (1958), 28–38, doi:10.1017/S0305004100033156. Full tables not inspected.
4. Y. Zheng and P. C. Doerschuk, *Explicit Computation of Orthonormal Symmetrized Harmonics with Application to the Identity Representation of the Icosahedral Group*, SIAM J. Math. Anal. **32** (2000), 538–554, doi:10.1137/S0036141098341770. Full text not inspected.
5. G. Szegő, *Orthogonal Polynomials*, 4th ed., American Mathematical Society, 1975, Theorem 7.3.3 (Bernstein-type Legendre bound).
