# Sharp fourth-root stability of complex finite-dimensional quartic isometries

## Finding
For complex linear maps between finite-dimensional quartic sequence spaces, small uniform fourth-power norm distortion forces closeness to an exact linear isometry, **uniformly in the target dimension**, with an explicit constant and an optimal fourth-root exponent. Precisely, let \(d\ge2\), \(n\ge d\), and \(A:\ell_4^d(\mathbb C)\to\ell_4^n(\mathbb C)\) be linear. Define
\[
\varepsilon=\Delta(A):=\sup_{\|x\|_4=1}\bigl|\|Ax\|_4^4-1\bigr|,\qquad M=\binom d2.
\]
If \(\varepsilon<1/(M+1)\), there exists a linear isometry \(U\) with
\[
\boxed{\|A-U\|_{4\to4}\le d^{3/4}(M\varepsilon)^{1/4}+(M+1)\varepsilon.}
\]
Moreover, this fourth-root exponent is optimal even for maps from two coordinates to three coordinates, and remains optimal if the comparison class is enlarged to restricted isometries that are permitted to annihilate some coordinates.

## Assumptions and scope
All spaces are complex and carry the ordinary \(\ell_4\)-norm. An exact isometry is a linear map preserving the norm of every vector, not necessarily surjective. A restricted isometry preserves the norm on the span of its nonzero coordinate columns and annihilates the remaining coordinate basis vectors; equivalently, its nonzero columns have mutually disjoint supports and unit \(\ell_4\)-norm. The result holds simultaneously for all integers \(d\ge2\) and \(n\ge d\). It imposes no positivity assumption on matrix entries. The smallness condition is explicitly stated and is not claimed optimal. Operator norms are induced \(\ell_4\)-norms.

## Proof
Write the columns of \(A\) as \(u_j=(a_{ij})_{i=1}^n\), for \(1\le j\le d\). Applying the distortion hypothesis to each basis vector yields
\[
1-\varepsilon\le\|u_j\|_4^4\le1+\varepsilon.\tag{1}
\]
For two distinct columns, the elementary complex phase-averaging identity is
\[
\frac1{2\pi}\int_0^{2\pi}\|u_j+e^{it}u_k\|_4^4\,dt
=\|u_j\|_4^4+\|u_k\|_4^4+4\sum_i|a_{ij}|^2|a_{ik}|^2.\tag{2}
\]
The two-coordinate vector \(e_j+e^{it}e_k\) has fourth power of its norm equal to \(2\), so the left side of (2) lies between \(2-2\varepsilon\) and \(2+2\varepsilon\). Combining with (1), for each \(j<k\), gives the *overlap bound*
\[
S_{jk}:=\sum_i|a_{ij}|^2|a_{ik}|^2\le\varepsilon.\tag{3}
\]
In each target row \(i\), select one index \(j(i)\) of largest modulus \(|a_{ij(i)}|\), with any fixed tie-breaking rule. Form \(A_0\) by retaining only that entry of the row and replacing its other entries by zero. Its columns \(v_j=A_0e_j\) have pairwise disjoint supports. The total fourth-power mass removed is
\[
R=\sum_i\sum_{j\ne j(i)}|a_{ij}|^4
\le\sum_i\sum_{j\ne j(i)}|a_{ij}|^2|a_{i,j(i)}|^2
\le\sum_{j<k}S_{jk}\le M\varepsilon.\tag{4}
\]
For every \(x\in\ell_4^d\) of norm one, the triangle and Hölder inequalities imply
\[
\|(A-A_0)x\|_4\le\sum_j|x_j|\|(A-A_0)e_j\|_4
\le R^{1/4}\sum_j|x_j|\le d^{3/4}R^{1/4}.\tag{5}
\]
Set \(r_j=\|v_j\|_4\). Equations (1) and (4) show
\[
r_j^4\ge1-(M+1)\varepsilon>0,
\qquad |1-r_j^4|\le(M+1)\varepsilon.\tag{6}
\]
Normalize each disjoint column: \(Ue_j=v_j/r_j\). Disjointness and unit quartic norms yield \(\|Ux\|_4^4=\sum_j|x_j|^4\), so \(U\) is an exact isometry. Moreover, disjointness gives
\[
\|A_0-U\|_{4\to4}=\max_j|r_j-1|
\le\max_j|r_j^4-1|\le(M+1)\varepsilon.\tag{7}
\]
The upper bound follows from (4), (5), and (7).

To prove the exponent sharp, take \(d=2\), \(n=3\), and \(A_\delta(x,y)=(x,y,\delta(x+y))\), \(0<\delta<1\). For every \(x,y\),
\[
\|A_\delta(x,y)\|_4^4-\|(x,y)\|_4^4=\delta^4|x+y|^4.
\]
The dual norm of the functional \((x,y)\mapsto x+y\) on \(\ell_4^2\) is \(2^{3/4}\); equality occurs when the two input coordinates are equal. Hence \(\Delta(A_\delta)=8\delta^4\). Let \(\mathcal R_{2,3}\) be the class of all restricted isometries from \(\ell_4^2\) to \(\ell_4^3\), including those with zero columns. Every member with two nonzero columns has disjoint column supports, so at least one of its two entries in the third target row vanishes. The corresponding column of \(A_\delta\) has third-row entry \(\delta\), giving operator-distance at least \(\delta\). If a comparison map has a zero column, its distance is at least \(\|A_\delta e_j\|_4\ge1\ge\delta\). Thus
\[
\operatorname{dist}_{4\to4}(A_\delta,\mathcal R_{2,3})\ge\delta.\tag{8}
\]
For the matching upper bound, the two columns \(((1-\delta^4)^{1/4},0,\delta)\) and \((0,1,0)\) define an exact isometry \(U_\delta\). Their supports are disjoint, and a direct triangle estimate gives
\[
\|A_\delta-U_\delta\|_{4\to4}
\le\delta+1-(1-\delta^4)^{1/4}=\delta+O(\delta^4).\tag{9}
\]
Since exact isometries belong to \(\mathcal R_{2,3}\), (8)–(9) and \(\Delta(A_\delta)=8\delta^4\) imply
\[
\boxed{\lim_{\delta\downarrow0}
\frac{\operatorname{dist}_{4\to4}(A_\delta,\mathcal R_{2,3})}{\Delta(A_\delta)^{1/4}}
=8^{-1/4}.}
\]
No bound of order \(o(\varepsilon^{1/4})\) can hold uniformly on this fixed source-target pair. This completes the proof.

## Verification
Equations (1)–(9) independently determine the entire bound. In particular, (2) is an exact phase identity, (3)–(4) use only nonnegative overlap terms, and (8) is valid for the **larger** class of restricted isometries. The companion `CHECK.py` verifies the phase identity for a finite exhaustive family of Gaussian-integer column pairs using four-root averaging, the geometric lower bound for explicit rational perturbations, and selected row-deletion inequalities with exact rational arithmetic. These finite checks are supplementary: the universally quantified claim is proved analytically.

## Relationship to prior work
Dalfollo-Daley, Delfín, Fernández, Mars and Xia classify exact restricted isometries of finite-dimensional \(\ell^p\)-spaces by disjoint supports, including the complex case. The present assertion addresses the distinct *quantitative* problem of uniform approximation of arbitrary near-isometries by exact isometries, determines a concrete dimension-independent-in-the-target bound, and proves the power of the defect cannot be improved. Oikhberg and Tradacete study approximations to disjointness-preserving operators, including positive almost-disjointness-preserving maps; the positivity-based approximation theorem does not directly supply this arbitrary-complex finite-matrix statement or its sharp perturbation example. The direct construction here makes all constants explicit and requires no positivity.

## Limitations
This is a stability theorem for quartic norms, not an extension to every exponent \(p\), and it does not determine the optimal numerical constant or the largest permissible defect. The sharpness example is asymptotic and proves optimality of the exponent, not of the stated dimensional prefactor. Full independent mathematical checking and exhaustive priority review have not been carried out. General approximate-isometry stability theorems under other terminology remain a publication-priority risk.

## References
1. O. Dalfollo-Daley, A. Delfín, C. Fernández, C. Mars, X. Xia, *Restricted Isometries in Finite-Dimensional \(\ell^p\)-Spaces*, arXiv:2610.32615v1 (first public October 23, 2026), Theorem 3.18.
2. T. Oikhberg and P. Tradacete, *Almost disjointness preservers*, arXiv:1508.04074 (2015), Theorem 6.2 and Remark 6.4.
