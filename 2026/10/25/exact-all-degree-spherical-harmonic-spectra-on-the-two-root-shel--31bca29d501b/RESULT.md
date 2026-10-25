# Exact all-degree spherical-harmonic spectra on the two root shells of type B

## Finding
Fix an integer \(n\ge3\). Let \(X_n\subset S^{n-1}\) consist of the \(2n\) short-root directions \(\{\pm e_i\}\) and the \(2n(n-1)\) long-root directions \(\{(\pm e_i\pm e_j)/\sqrt2:i<j\}\); thus \(|X_n|=2n^2\). For every integer \(\ell\ge0\), form the full degree-\(\ell\) spherical-harmonic sampling Gram matrix
\[
G_{n,\ell}(x,y)=p_{n,\ell}(\langle x,y\rangle),\qquad
p_{n,\ell}(t)=\frac{C_\ell^{(n-2)/2}(t)}{C_\ell^{(n-2)/2}(1)},\qquad x,y\in X_n.
\]
Here \(C_\ell^\alpha\) is the standard Gegenbauer polynomial. This normalization equals the Gram matrix of evaluation of an orthonormal degree-\(\ell\) spherical-harmonic basis divided by the square root of its dimension, with probability surface measure.

The entire spectrum, including multiplicities and zeros, is determined by the following three values:
\[
u=p_{n,\ell}(0),\qquad v=p_{n,\ell}(1/2),\qquad w=p_{n,\ell}(1/\sqrt2).
\]
For a real symmetric matrix \(T\), let \(\operatorname{Eig}(T)\) mean both eigenvalues, counted with multiplicity.

For odd \(\ell\), the spectrum consists of \(n^2\) zero eigenvalues, the scalar eigenvalue \(2-4v\) with multiplicity \(n(n-2)\), and the two eigenvalues of
\[
T_o=\begin{pmatrix}2&2\sqrt{2(n-1)}w\\2\sqrt{2(n-1)}w&2+4(n-2)v\end{pmatrix},
\]
each with multiplicity \(n\).

For even \(\ell\), put \(E=\binom n2\). The spectrum consists of \(n^2\) zero eigenvalues, the scalar eigenvalues
\[
2(1-u)\quad(E\text{ copies}),\qquad
2+6u-8v\quad(E-n\text{ copies}),
\]
and the two eigenvalues of each of the following matrices:
\[
T_s=\begin{pmatrix}
2(1-u)&2\sqrt{2(n-2)}(w-u)\\
2\sqrt{2(n-2)}(w-u)&2+(14-4n)u+4(n-4)v
\end{pmatrix},
\]
with multiplicity \(n-1\) for *each* eigenvalue, and
\[
T_c=\begin{pmatrix}
2+2(n-1)u&4\sqrt{n-1}\bigl(w+(n-2)u/2\bigr)\\
4\sqrt{n-1}\bigl(w+(n-2)u/2\bigr)&2(1+u)+8(n-2)v+2(n-2)(n-3)u
\end{pmatrix},
\]
with multiplicity one for *each* eigenvalue. A scalar branch with multiplicity zero is omitted. The formulas remain valid if separate branches coincide or one of the displayed eigenvalues vanishes.

A notable exact rank consequence for every \(n\ge5\) is the nonmonotone parity-compatible sampling law
\[
\operatorname{rank}G_{n,5}=n^2,\qquad
\operatorname{rank}G_{n,6}=n^2-1.
\]
Thus all odd-compatible sampled data can be interpolated in exact harmonic degree five, whereas degree six has exactly one additional compatible output constraint, for every dimension at least five. Sharp positive evaluation singular values are the square roots of the positive displayed eigenvalues; sharp constants therefore require no matrix of size growing with \(n\).

## Assumptions and scope
The ambient dimension is an arbitrary integer \(n\ge3\), and \(\ell\) is any nonnegative integer. Both lengths of type-\(B_n\) roots are individually normalized to the unit sphere; each signed direction appears once. The root set is antipodal. The result concerns *one exact harmonic degree*, not the degree-at-most-\(\ell\) band, and the Gram matrix is unweighted over sample points. All multiplicities are for the full \(2n^2\)-by-\(2n^2\) Gram matrix, not for a half-size antipodal quotient.

## Proof
**Addition kernel.** For an orthonormal basis \(\{Y_j\}_{j=1}^{d_{n,\ell}}\) with normalized spherical surface measure, the addition formula reads \(\sum_jY_j(x)\overline{Y_j(y)}=d_{n,\ell}p_{n,\ell}(\langle x,y\rangle)\). Hence \(G_{n,\ell}\) is positive semidefinite and has the stated sampling normalization.

**Sign-character decomposition.** Independently change the signs of all \(n\) coordinates. On each axis orbit \(\{\pm e_i\}\), the permutation module has Walsh characters \(\varnothing\) and \(\{i\}\). On each four-point long-root orbit supported on \(\{i,j\}\), the Walsh characters are \(\varnothing,\{i\},\{j\},\{i,j\}\). The zonal Gram matrix commutes with these sign changes and therefore preserves the associated character spaces. Because \(p_{n,\ell}(-t)=(-1)^\ell p_{n,\ell}(t)\), precisely one antipodal-parity half of the sample space has eigenvalue zero. Its dimension is \(n^2\). For odd degrees the surviving characters are exactly the \(n\) singletons; for even degrees they are the empty character and the \(E\) two-element characters. These exhaust the \(2n^2\) sample coordinates.

**Odd block.** Fix a singleton character \(\{i\}\). Its normalized Walsh basis consists of the antisymmetric short-root vector supported on \(\pm e_i\), together with one signed-long-root vector on each edge \(\{i,j\}\). Direct averages of the Gegenbauer kernel over the signs give a diagonal short-root entry \(2\), every short-to-edge entry \(2\sqrt2 w\), an edge diagonal \(2\), and distinct-edge entries \(4v\). The \(n-2\)-dimensional edge-standard complement therefore has scalar eigenvalue \(2-4v\); on the short-root direction plus the normalized all-ones edge direction the compression is \(T_o\). There are \(n\) singleton characters, giving the odd spectrum with the stated multiplicities.

**Even blocks.** For each two-element sign character \(\{i,j\}\) the only supported Walsh basis vector lies on its own four-point long-root orbit. Its self-entry is \(p(1)+p(-1)-2p(0)=2(1-u)\), accounting for \(E\) identical eigenvalues. In the empty character, take the normalized sign averages \(a_i\) of each short-root pair and \(b_{ij}\) of each long-root quadruple. Let \(M\) be the \(n\)-by-\(E\) unsigned vertex-edge incidence matrix of the complete graph. Sign averaging gives the block matrix
\[
\begin{pmatrix}A&C\\C^T&D\end{pmatrix},\quad
A=2(1-u)I+2uJ,\quad
C=2\sqrt2\,[uJ+(w-u)M],
\]
\[
D=(2+6u-8v)I+4(v-u)M^TM+4uJ.
\]
Here each \(J\) is the all-ones matrix of the indicated rectangular size. The incidence identity \(MM^T=(n-2)I+J\) has full row rank when \(n\ge3\). Thus \(\ker M\) has dimension \(E-n\) and yields the scalar \(2+6u-8v\). The normalized constant vertex and constant edge vectors span a two-dimensional invariant space, with matrix \(T_c\). The \(n-1\)-dimensional standard vertex space is paired via \(M^T/\sqrt{n-2}\) with the standard edge space; its identical two-dimensional compressions give \(T_s\). These spaces have dimensions \((E-n)+2+2(n-1)=n+E\), so no eigenvalues remain unaccounted for.

**Rank change.** At degree five the exact Gegenbauer evaluations give
\[
2-4v=\frac{15(n-2)(n+4)}{8(n-1)(n+1)}>0,
\]
and
\[
\det T_o=\frac{5(n-2)(n+4)(n+6)}{4(n-1)(n+1)^2}>0.
\]
The first principal entry of \(T_o\) is \(2\), hence \(T_o\) is positive definite and all \(n^2\) compatible eigenvalues are positive.

At degree six, exact evaluation yields
\[
2+6u-8v=\frac{15(n-4)(n+4)(n+6)}{8(n-1)(n+1)(n+3)}>0\quad(n\ge5),
\]
\[
\det T_s=\frac{15n(n-3)(n+4)^2(n+6)(n+8)}{8(n-1)^2(n+1)^2(n+3)^2}>0,
\]
where the first principal entry of \(T_s\) equals \(2(1-u)>0\). The pair-character scalar is also strictly positive. Finally
\[
\det T_c=0,\qquad
\operatorname{tr}T_c=\frac{(n-2)(n+6)(n^2-16n+240)}{8(n-1)(n+1)(n+3)}>0.
\]
Thus the constant block has rank exactly one, while all other parity-compatible blocks are invertible. This proves the stated rank change for every \(n\ge5\).

## Verification
The standalone program `checks/check_bn.py` constructs the signed root sets independently, evaluates Gegenbauer polynomials from SymPy, constructs the *full* direct Gram matrices, and compares their numerical eigenspectra to the block formulas for every dimension \(3\le n\le7\) and every degree \(0\le\ell\le12\). All 65 cases passed; the largest absolute spectral discrepancy was \(4.546\times10^{-14}\). The same program symbolically factors the degree-five and degree-six positivity/rank expressions as exact identities in the ambient dimension. Run `python checks/check_bn.py` with Python, NumPy, and SymPy. The proof of the all-degree formula is the sign-character/incidence argument; finite tests alone are not an infinite-dimensional proof.

## Relationship to prior work
Delsarte, Goethals and Seidel developed the spherical-code/Gegenbauer addition-kernel framework. Dunkl studied \(B_n\)-invariant spherical harmonics and Gram determinants for **invariant harmonic polynomial bases**. These are different Gram matrices from point evaluation on the mixed short-/long-root set considered here. Previously investigated harmonic sampling on the **long-root-only** \(D_n\) orbit treats a strict subset of the sample geometry; knowing its standalone spectrum does not determine the mixed short/long coupling, the \(T_o,T_s,T_c\) blocks, or the full parity-compatible ranks. The present calculation uses sign characters and complete-graph incidence to establish the complete two-shell spectrum and degree-five/degree-six transition.

## Limitations
The result gives explicit spectral formulas for exact-degree spherical harmonics; it does not treat arbitrary unions of root shells, nonuniform sample weights, spherical bandlimits, or spectral inequalities outside this set. The returned spectrum may have additional equalities between numerical branches, which are interpreted with algebraic multiplicity. The work has not received independent validation. Although available close literature does not visibly imply the particular two-shell formulas, an older general association-scheme calculation may overlap with this result; publication priority is not certified.

## References
1. Charles F. Dunkl, *Symmetric Functions and \(B_N\)-Invariant Spherical Harmonics*, arXiv:math/0207122, first posted July 15, 2002. https://arxiv.org/abs/math/0207122
2. Ph. Delsarte, J. M. Goethals and J. J. Seidel, *Spherical Codes and Designs*, Geometriae Dedicata 6 (1977), 363–388. DOI:10.1007/BF03187604.
3. D. G. Mixon, *Spherical Codes and Designs*, lecture-note exposition, September 7, 2019. https://dustingmixon.wordpress.com/2019/09/07/spherical-codes-and-designs/
