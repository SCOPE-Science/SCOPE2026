# A unique spectral outlier for the Bergman diameter trace

## Finding

Let \(A^2(\mathbb D)\) be the analytic Bergman space with normalized area norm \(\|f\|_{A^2}^2=\pi^{-1}\int_{\mathbb D}|f(z)|^2\,dA(z)\). Define the diameter trace form
\[
Q(f,g)=\int_{-1}^{1}f(t)\overline{g(t)}(1-|t|)\,dt.
\]
It induces a bounded, positive, self-adjoint operator \(T\) on \(A^2(\mathbb D)\). The following all hold.

1. The restriction of \(Q\) to the codimension-one space \(\{f:f(0)=0\}\) obeys the sharp inequality \(Q(f,f)\le\|f\|_{A^2}^2\). Its best constant is \(1\), and equality holds there only for the zero function.
2. The essential norm is exactly \(\|T\|_{\mathrm{ess}}=1\).
3. Exactly one point of the spectrum lies in \((1,\infty)\). It is a simple isolated eigenvalue \(\Lambda=\|T\|\), satisfying
\[
\frac35+\frac{\sqrt{219}}{30}\le\Lambda
\le 1+\sqrt{4\log2-1-\frac{\pi^2}{6}}.
\]
In particular, the full diameter trace is **not** contractive, although the restriction to \(f(0)=0\) is sharply contractive. The result concerns precisely the boundary-distance trace weight \(1-|t|\) and the specified normalized Bergman norm.

## Assumptions and scope

Throughout \(f\) and \(g\) are holomorphic on the disk and square-integrable with respect to normalized planar area; no boundary continuity is needed. The form is initially defined for polynomials and subsequently extended continuously to all \(A^2\). The parameter-free line density is the Euclidean distance from \(t\in[-1,1]\) to the nearest endpoint. The Hilbert-space essential norm is distance to compact operators; spectral multiplicities are Hilbert-space multiplicities. The assertion concerns the entire infinite-dimensional Hilbert space, not a finite polynomial truncation.

## Proof

**Exact matrix.** The vectors \(e_n(z)=\sqrt{n+1}z^n\), \(n\ge0\), form an orthonormal basis. Direct integration gives the exact Gram matrix
\[
A_{nm}:=\langle Te_m,e_n\rangle
=\begin{cases}
\displaystyle\frac{2\sqrt{(n+1)(m+1)}}{(n+m+1)(n+m+2)},&n+m\text{ even},\\
0,&n+m\text{ odd}.
\end{cases}
\]
In particular, \(A_{00}=1\), \(A_{02}=\sqrt3/6\), and \(A_{22}=1/5\). This matrix is positive because it is a Gram matrix of restrictions.

**Sharp contraction away from the constant.** Let \(A'\) denote the compression to indices \(n,m\ge1\). Its entries are nonnegative and symmetric. Apply the weighted Schur criterion with the strictly positive weights \(w_n=(n+1)^{-1/2}\). Define \(F_n(x)=((n+x+1)(n+x+2))^{-1}\), which is strictly convex and positive on \([0,\infty)\). If \(n\ge1\) is odd, the admissible column indices are odd and midpoint convexity on intervals \([2k,2k+2]\) implies
\[
\frac{(A'w)_n}{w_n}
=2(n+1)\sum_{k\ge0}F_n(2k+1)
\le(n+1)\int_0^\infty F_n(x)\,dx
=(n+1)\log\frac{n+2}{n+1}<1.
\]
For even \(n\ge2\), the columns are \(m=2,4,\ldots\); midpoint convexity on \([2k-1,2k+1]\) gives
\[
\frac{(A'w)_n}{w_n}
=2(n+1)\sum_{k\ge1}F_n(2k)
\le(n+1)\int_1^\infty F_n(x)\,dx
=(n+1)\log\frac{n+3}{n+2}<1.
\]
The symmetric Schur estimate therefore yields \(\|A'\|\le1\). Moreover, for every nonzero \(x\in\ell^2(\{1,2,\ldots\})\), the weighted inequality \(|\langle A'x,x\rangle|\le\sum_n((A'w)_n/w_n)|x_n|^2\) is strictly below \(\|x\|^2\), because every row ratio is strictly less than one. Hence nonzero equality is impossible. This proves boundedness of the compressed trace form.

**One supercritical eigenvalue.** The coupling between \(e_0\) and the other indices is the square-summable vector \(b\), with \(b_{2j}=1/((j+1)\sqrt{2j+1})\) for \(j\ge1\), and all odd coordinates zero. Its exact squared norm is
\[
\|b\|^2=\sum_{j\ge1}\frac1{(j+1)^2(2j+1)}
=4\log2-1-\frac{\pi^2}{6}.
\]
Thus the full matrix is \(\operatorname{diag}(1,A')\) plus a rank-two self-adjoint off-diagonal coupling, so it defines a bounded positive operator with \(\|T\|_{\mathrm{ess}}\le1\) and \(\|T\|\le1+\|b\|\). On the other hand, the compression to \(\operatorname{span}\{e_0,e_2\}\) is
\[
\begin{pmatrix}1&\sqrt3/6\\\sqrt3/6&1/5\end{pmatrix},
\]
whose top eigenvalue is \(3/5+\sqrt{219}/30>1\). Consequently \(\|T\|>1\). Since its essential spectrum is confined to \([0,1]\), a top eigenvalue \(\Lambda>1\) is isolated and has finite multiplicity. Two linearly independent eigenvectors with eigenvalues above one would generate a two-dimensional subspace on which the trace quadratic form exceeds the norm squared. That subspace necessarily intersects the codimension-one subspace \(e_0^\perp\), contradicting the compression estimate. The eigenvalue is therefore unique and simple.

**Exact essential edge and sharpness.** Put \(I_M=\{M,M+1,\ldots,M^2\}\) and define \(v^{(M)}\) by \(v_{2i}^{(M)}=(2i+1)^{-1/2}\) for \(i\in I_M\), with every other coordinate zero. As \(M\to\infty\), elementary sum–integral comparisons give
\[
\|v^{(M)}\|^2=\sum_{i=M}^{M^2}\frac1{2i+1}=\tfrac12\log M+O(1),
\]
\[
\langle Tv^{(M)},v^{(M)}\rangle
=\sum_{i,j=M}^{M^2}\frac{2}{(2i+2j+1)(2i+2j+2)}
=\tfrac12\log M+O(1).
\]
Indeed the double summand differs from \(1/[2(i+j)^2]\) by \(O((i+j)^{-3})\); the double sum of \((i+j)^{-2}\) is \(\log M+O(1)\), as seen by integration over \([M,M^2]^2\). Normalize \(v^{(M)}\) to unit norm. These unit vectors converge weakly to zero because their supports escape to infinity, while their Rayleigh quotients tend to one. For every compact \(K\), \(\langle Kv^{(M)},v^{(M)}\rangle/\|v^{(M)}\|^2\to0\); thus \(\|T-K\|\ge1\). We conclude \(\|T\|_{\mathrm{ess}}=1\). The same vectors lie in \(e_0^\perp\), proving that the constant one in the restricted inequality is sharp.

## Verification

A standalone Python 3 checker, \(\texttt{CHECK.py}\), implements the exact matrix formula, symmetry/parity checks, finite-dimensional leading-eigenvalue computations, explicit Schur majorants, finite Weyl-sequence Rayleigh quotients, and the off-diagonal series identity. In the recorded execution it passed 8,705 deterministic numerical assertions. Numerical checks verify finite instances only; the arguments above establish the infinite-dimensional conclusions. The Weyl sequence is analyzed mathematically, not inferred from an apparent numerical trend.

## Relationship to prior work

Ghiloufi and Zaway, *Meromorphic Bergman spaces* (arXiv:2309.00552, version 1 dated 2023-09-01), develop Fejér–Riesz type trace inequalities and Toeplitz boundedness in meromorphic Bergman settings. Their inspected sections concerning those inequalities and operators do not state the normalized classical Bergman diameter form's codimension-one sharp constant, essential spectral norm or unique outlier. These are structurally stronger than existence of a trace bound, and our weight and full-diameter normalization are explicitly fixed.

Kasuga, *Fejér–Riesz Type Inequalities for Weighted Bergman Spaces* (2025), discusses general weighted line inequalities and quotes Zhu's Euclidean boundary-distance Fejér–Riesz inequality; the inspected article estimates trace norms, not the spectrum of the particular positive operator here. Andreev's 2012 work on Fejér–Riesz type inequalities for Bergman spaces is relevant, but its full text was not obtainable during this comparison; its complete coverage remains a historical-priority risk. Classical Hilbert/Cesàro operator estimates and work on weighted harmonic circle traces concern different operators, spaces or geometries. Absence of a search hit is not a proof of priority.

## Limitations

The result pertains to the fixed weight \(1-|t|\), the entire symmetric diameter, Hilbert exponent two, and normalized unweighted analytic Bergman space. It does not determine the eigenvalue \(\Lambda\) in closed form, establish a numerical enclosure better than the proven two-sided bounds, or extend to other trace weights. Historical novelty is subject to the unread full text of Andreev (2012) and possible earlier spectral results. No independent mathematical verification has been performed.

## References

1. N. Ghiloufi and M. Zaway, *Meromorphic Bergman spaces*, arXiv:2309.00552v1 (2023-09-01), https://arxiv.org/abs/2309.00552 ; https://arxiv.org/pdf/2309.00552 .
2. K. Kasuga, *Fejér–Riesz Type Inequalities for Weighted Bergman Spaces*, 2025, https://doi.org/10.17654/0972087125014 ; https://pphmjopenaccess.com/index.php/fejms/article/download/2751/1571 .
3. V. Andreev, *Fejér–Riesz type inequalities for Bergman spaces*, 2012, https://doi.org/10.1007/s12215-012-0097-z (full text not accessed).
4. Y. Feng, *Generalized Hilbert Operator Acting on Weighted Bergman Spaces and on Dirichlet Spaces*, arXiv:2207.11176 (2022), https://arxiv.org/abs/2207.11176 .
