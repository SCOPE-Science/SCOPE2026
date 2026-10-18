# The exact rank-invariant Krein–Milman spectrum of real rectangular cube operator balls

## Finding
For positive integers \(m,n\), let \(\mathcal B_{m,n}=\mathcal L(\ell_1^n(\mathbb R),\ell_\infty^m(\mathbb R))\). Say that \(\mathcal B_{m,n}\) has the *rank-invariant Krein–Milman property of order* \(r\) if every norm-one operator of rank exactly \(r\) is a finite convex combination of norm-one extreme contractions of rank exactly \(r\). Then, for every integer \(1\le r\le\min\{m,n\}\),
\[
\boxed{\mathcal B_{m,n}\text{ has this property of order }r\quad\Longleftrightarrow\quad r=1.}
\]
For every \(r\ge2\) the failure already occurs at each strict interior point of an edge joining extreme contractions of ranks \(r-1\) and \(r\), respectively. The classification includes one-row and one-column cases, where only rank one is admissible.

## Assumptions and scope
All vector spaces, linear maps, ranks, and convex combinations are over \(\mathbb R\). The operator norm is the usual induced norm, and "extreme" means an extreme point of the closed operator unit ball. A norm-one operator is one of operator norm exactly \(1\). In the negative direction, \(m,n\ge r\ge2\) are arbitrary integers, and the edge parameter is any real \(0<t<1\). No Hilbertian assumptions or restrictions on equal domain and codomain dimensions are made. No assertion is made about complex operator spaces or about other pairs of Banach spaces.

## Proof
**Operator cube.** If \(A=(a_{ij})\) acts from \(\ell_1^n\) to \(\ell_\infty^m\), then
\[
\|A\|_{1\to\infty}=\max_{1\le i\le m,\,1\le j\le n}|a_{ij}|.
\]
Indeed the upper bound follows by the triangle inequality and equality follows at a coordinate basis vector. Hence the unit ball is the entrywise cube \([-1,1]^{mn}\). Its extreme points are exactly the matrices whose entries all belong to \(\{-1,1\}\), here called *sign matrices*.

**The positive rank-one assertion.** Write a norm-one rank-one matrix as \(A=uv^\top\), normalized so that \(\|u\|_\infty=\|v\|_\infty=1\). Let \(\varepsilon\in\{-1,1\}^m\) and \(\delta\in\{-1,1\}^n\) be independent random sign vectors, with independently chosen coordinates and
\[
\mathbb P(\varepsilon_i=s)=(1+s u_i)/2,\qquad
\mathbb P(\delta_j=s)=(1+s v_j)/2\quad(s\in\{-1,1\}).
\]
These are nonnegative probability weights summing to one. Independence gives \(\mathbb E[\varepsilon_i\delta_j]=u_iv_j\), so
\[
A=\mathbb E[\varepsilon\delta^\top]
 =\sum_{\varepsilon,\delta}
 \mathbb P(\varepsilon)\mathbb P(\delta)\,
 \varepsilon\delta^\top.
\]
Every matrix in the sum is a rank-one sign matrix, hence a rank-one extreme contraction. This finite convex representation proves the property for \(r=1\), including all boundary cases.

**Adjacent extreme ranks.** Fix \(2\le r\le\min\{m,n\}\). Let \(\mathbf 1\in\mathbb R^m\) be the all-ones vector and \(e_1,\ldots,e_m\) the standard basis. Define an \(m\)-by-\(n\) sign matrix \(S\) with column \(c_1=\mathbf1\), columns \(c_j=\mathbf1-2e_{j-1}\) for \(2\le j\le r-1\), and all remaining columns \(c_j=\mathbf1\). Its column span is
\[
\operatorname{span}\{\mathbf1,e_1,\ldots,e_{r-2}\},
\]
which has dimension \(r-1\), since the last two coordinates of \(\mathbf1\) are equal and those of \(e_1,\ldots,e_{r-2}\) vanish. Let \(S'\) agree with \(S\) except that its entry in row \(r-1\), column \(r\) is \(-1\) instead of \(+1\). This introduces the column \(\mathbf1-2e_{r-1}\). Since \(e_{r-1}\) is independent of the displayed column span (its coordinate \(r-1\) differs from coordinate \(r\)), \(\operatorname{rank}S'=r\).

For any \(0<t<1\), set \(A_t=(1-t)S+tS'\). The first \(r-1\) columns retain their span, and column \(r\) equals \(\mathbf1-2t e_{r-1}\), proving \(\operatorname{rank}A_t=r\). Precisely one entry of \(A_t\) is strictly between \(-1\) and \(+1\), namely \(1-2t\), so \(\|A_t\|=1\). All other entries are saturated at \(\pm1\).

**Exposed-edge obstruction.** Suppose \(A_t\) is a convex combination of sign matrices. Every sign matrix appearing with positive coefficient must agree with every saturated entry of \(A_t\): a proper average of signs equals \(1\) or \(-1\) only when every summand has that sign. Thus the only possible summands are \(S\) and \(S'\), and the differing entry forces their coefficients to be \(1-t\) and \(t\). Both coefficients are positive, while \(S\) has rank \(r-1\). Consequently \(A_t\) cannot be a convex combination of extreme contractions all of rank \(r\). This proves failure for each admissible \(r\ge2\) and completes the equivalence. \(\square\)

## Verification
The self-contained Python 3 script `verify_rank_spectrum.py` tests the explicit sign-edge construction by exact rational Gaussian elimination for every \(2\le m,n\le7\), every \(2\le r\le\min\{m,n\}\), and parameters \(t\in\{1/4,1/2,3/4\}\) (273 exact edge tests). It additionally evaluates the independent-sign rank-one decomposition for 64 small rational instances. Run from this file's directory with `python3 verify_rank_spectrum.py`. These finite checks supplement; they do not replace or establish the universally quantified proof above.

## Relationship to prior work
Sohel, Sain, and Paul, arXiv:2208.10184v1 (2022), remark on the identification of \(\mathcal L(\ell_1^n,\ell_\infty^m)\) with the cube \(\ell_\infty^{mn}\) and enumerate its extreme contractions. The exact same operator balls are therefore classical; the result here concerns a different, rank-restricted convexification assertion not supplied by their extreme-point count. Sain, Sohel, and Paul, *Extreme contractions on finite-dimensional Banach spaces* (public journal online October 24, 2022; later arXiv:2407.05545v1), define rank-invariant Krein–Milman properties, establish order-one results for certain classes, and give a rank-two failure example for a coordinate cube-to-cube operator space. Those statements do not imply the full order-by-order result for all real rectangular \(\ell_1\)-to-\(\ell_\infty\) operator spaces: in particular the matrices in the present theorem have an entrywise cube operator unit ball, unlike general \(\ell_\infty\)-to-\(\ell_\infty\) operator norms. The proof above relies on the explicit edge whose endpoints have consecutive ranks.

## Limitations
This is a real finite-dimensional statement; the complex case and other operator geometries remain outside scope. The check script covers only finitely many instances. The originality assessment rests on identified and accessible sources and targeted scholarly searches, so an equivalent unindexed or differently named result remains possible. No independent scientific audit has been conducted.

## References
1. S. Sohel, D. Sain, and K. Paul, *On subspaces of \(\ell_\infty\) and extreme contraction in \(\mathbb L(\mathbb X,\ell_\infty^n)\)*, arXiv:2208.10184v1, August 22, 2022. https://arxiv.org/abs/2208.10184.
2. D. Sain, S. Sohel, and K. Paul, *Extreme contractions on finite-dimensional Banach spaces*, published online October 24, 2022, DOI:10.4064/cm8803-7-2022; subsequent version arXiv:2407.05545v1. https://doi.org/10.4064/cm8803-7-2022.
