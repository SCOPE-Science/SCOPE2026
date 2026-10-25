# Löwner ellipsoids of rectangular fixed-cardinality assignment polytopes and a sharp saturation anisotropy transition

## Finding
For every integer pair \(2\le m\le n\) and \(1\le k\le m\), let \(\mathcal A_{m,n,k}\) be the convex hull of \(m\times n\) zero-one matrices with exactly \(k\) ones and at most one one in any row or column. Equip its affine hull with the ambient Frobenius Euclidean metric. Its unique minimum-volume **enclosing** (Löwner) ellipsoid is given explicitly below, including the dimension-dropping saturation cases.

Let \(H_s=s^{-1}\mathbf1_s\mathbf1_s^{\mathsf T}\), \(F_s=I_s-H_s\), \(C=(k/(mn))\mathbf1_m\mathbf1_n^{\mathsf T}\), and define orthogonal matrix-space projections
\[
R(Y)=F_mYH_n,\qquad Q(Y)=H_mYF_n,\qquad I(Y)=F_mYF_n.
\]
Their ranks are respectively \(m-1\), \(n-1\), and \((m-1)(n-1)\). Define
\[
\lambda_R=\frac{k(m-k)}{mn(m-1)},\qquad
\lambda_Q=\frac{k(n-k)}{mn(n-1)},\qquad
\lambda_I=\frac{k((m-1)(n-1)+k-1)}{mn(m-1)(n-1)}.
\]
Discard any zero-eigenvalue summand, and let \(\mathcal T\) denote the remaining labels, with the preceding multiplicities \(r_R,r_Q,r_I\). Put \(d=\sum_{T\in\mathcal T}r_T\); explicitly \(d=mn-1\) for \(k<m\), \(d=m(n-1)\) for \(k=m<n\), and \(d=(n-1)^2\) for \(k=m=n\). Then
\[
\boxed{\quad
\mathcal E_{m,n,k}=\left\{C+Y:\ Y\in\operatorname{aff}(\mathcal A_{m,n,k})-C,
\quad\sum_{T\in\mathcal T}\frac{\|T(Y)\|_F^2}{d\lambda_T}\le1\right\}.
\quad}
\]
Its squared semiaxes are \(d\lambda_T\), with the specified multiplicities, and **every one** of the \(\binom{m}{k}\binom{n}{k}k!\) vertices is a contact point. Its exact intrinsic Euclidean volume is
\[
\boxed{\operatorname{vol}_{d}(\mathcal E_{m,n,k})=
\frac{\pi^{d/2}}{\Gamma(1+d/2)}
\prod_{T\in\mathcal T}(d\lambda_T)^{r_T/2}.}
\]

The ratio of largest to smallest *positive squared semiaxis*, denoted \(\mathfrak a_{m,n,k}\), has the complete closed form
\[
\boxed{\mathfrak a_{m,n,k}=\begin{cases}
\displaystyle\frac{(m-1)(n-1)+k-1}{(n-1)(m-k)},&1\le k<m,\\[5pt]
\displaystyle\frac{n}{n-m},&k=m<n,\\[5pt]
1,&k=m=n.
\end{cases}}
\]
For fixed \(m,n\), this ratio is strictly increasing on the nontrivial interval \(1\le k<m\). The final step \(k=m-1\to m\) has a **sharp direction classification**: it increases whenever \(m=2<n\), whenever \(m\ge3\) and \(n=m+1\), and for \((m,n)=(3,5)\); it decreases whenever \(m=n\ge3\), or \(m=3,n\ge6\), or \(m\ge4,n\ge m+2\). The only equality is \((m,n)=(2,2)\). In particular, at each fixed \(m\ge3\), as \(n\to\infty\) the last-step ratio tends to \(1/(m-1)\): saturation strictly improves spectral roundness by a finite factor even though all previous ranks worsened it.

## Assumptions and scope
The matrix entries are real in the enclosing ellipsoid, but the polytope's vertices are exactly the specified fixed-cardinality partial permutation matrices. Its full halfspace model, independently known from the work of Gill–Linusson and Torres, consists of nonnegativity, row/column sums at most one, and total sum \(k\). For \(k=m<n\), every row sum is an affine equality; for \(k=m=n\), every row and column sum is an affine equality. The metric is the *intrinsic* Frobenius metric on that changing affine hull; an ambient full-dimensional ellipsoid would be undefined at saturation.

The theorem concerns the *minimum-volume ellipsoid containing* the polytope. It does not describe the maximum-volume ellipsoid contained in it (the different John problem), which has been treated separately for square parameters. No assertion is made for arbitrary sparse bipartite graphs or nonuniform edge weights.

## Proof
**Step 1: exact orthogonal modes and vertex energies.** The four projections \(Y\mapsto H_mYH_n\), \(R\), \(Q\), and \(I\) are mutually Frobenius-orthogonal and sum to the identity on matrix space. For a vertex \(V\), its row sums form an indicator vector of \(k\) occupied rows, and its column sums form an indicator vector of \(k\) occupied columns. Consequently, for **every** vertex, not merely in expectation,
\[
\|R(V-C)\|_F^2=\frac{k(m-k)}{mn},\qquad
\|Q(V-C)\|_F^2=\frac{k(n-k)}{mn},
\]
\[
\|I(V-C)\|_F^2
=k-\frac{k^2}{mn}-\frac{k(m-k)}{mn}-\frac{k(n-k)}{mn}
=\frac{k((m-1)(n-1)+k-1)}{mn}.
\]
The first two identities follow from the squared norms of centered occupied-row/occupied-column indicators; the third follows by Pythagoras from \(\|V-C\|_F^2=k-k^2/(mn)\). These identities remain valid at \(k=m\) and \(k=n\), exactly where one or two subspaces become absent.

**Step 2: covariance, ranks, and affine hull.** Choose a vertex \(V\) uniformly. Row permutations and column permutations act transitively on vertices, fix \(C\), and preserve each of the three projected matrix spaces. Their joint action forces the covariance operator \(\Sigma=\mathbb E[(V-C)\otimes(V-C)]\) to be scalar on each space and to have no cross terms (the standard/trivial tensor representations are pairwise inequivalent). One can avoid representation theory entirely: \(\mathbb EV_{ij}=k/(mn)\), \(\mathbb EV_{ij}V_{i\ell}=\mathbb EV_{ij}V_{h j}=0\) for distinct entries sharing a row or column, while for \(i\ne h\) and \(j\ne\ell\),
\[
\mathbb E[V_{ij}V_{h\ell}]=\frac{k(k-1)}{m(m-1)n(n-1)}.
\]
These four index-equality cases directly diagonalize the covariance in the displayed orthogonal modes. Taking traces on the three modes and using Step 1 yields \(\Sigma=\lambda_RR+\lambda_Q Q+\lambda_I I\), with precisely the three eigenvalues in the finding. The range of \(\Sigma\) is the linear span of all \(V-C\), since a vector has zero covariance quadratic form exactly when its inner product with every \(V-C\) vanishes. Hence \(\operatorname{aff}(\mathcal A_{m,n,k})=C+\operatorname{ran}\Sigma\) and its dimension is the stated sum of positive-eigenvalue multiplicities.

**Step 3: enclosing ellipsoid is globally optimal.** Work on the \(d\)-dimensional affine-hull direction space \(L=\operatorname{ran}\Sigma\), where \(\Sigma\) is positive definite. A general ellipsoid containing the vertices has arbitrary center \(c\in C+L\) and positive definite shape operator \(A\) on \(L\), with defining inequality \(\langle Y-c,A^{-1}(Y-c)\rangle_F\le1\). Averaging the containment inequalities over vertices gives
\[
\operatorname{tr}(A^{-1}\Sigma)+\langle C-c,A^{-1}(C-c)\rangle_F\le1.
\]
Arithmetic–geometric mean for the \(d\) eigenvalues of \(A^{-1/2}\Sigma A^{-1/2}\) gives
\[
\operatorname{tr}(A^{-1}\Sigma)\ge
 d\left(\frac{\det\Sigma}{\det A}\right)^{1/d}.
\]
Therefore \(\det A\ge d^d\det\Sigma\), so no enclosing ellipsoid has smaller volume than the one with center \(C\) and shape \(A_*=d\Sigma\). Conversely, Step 1 and the eigenvalue definitions show that **each vertex** satisfies
\[
\langle V-C,A_*^{-1}(V-C)\rangle_F
=\sum_{T\in\mathcal T}\frac{r_T\lambda_T}{d\lambda_T}
=\frac1d\sum_{T\in\mathcal T}r_T=1.
\]
Thus \(A_*\) encloses their convex hull, contacts every vertex, and attains the determinant bound. Equality in both the average inequality and matrix AM–GM forces \(c=C\) and \(A=d\Sigma\), proving uniqueness among arbitrary ellipsoids, not merely symmetry-invariant candidates. Multiplicities then give the volume formula.

**Step 4: extremal semiaxes and the saturation reversal.** Suppose \(k<m\). Direct subtraction of the formulas shows \(\lambda_R\le\lambda_Q\le\lambda_I\) for \(m\le n\), with equality throughout exactly at \(k=1\). Indeed \(\lambda_Q-\lambda_R\) has the sign of \((n-m)(k-1)\), and \(\lambda_I-\lambda_Q\) has the sign of \(m(k-1)\), after multiplication by positive denominators. Thus the first branch of \(\mathfrak a\) is \(\lambda_I/\lambda_R\). As \(k\) grows below \(m\), its numerator increases and its denominator decreases, giving strict increase when a pair of such ranks exists. If \(k=m<n\), the \(R\) mode disappears and \(\lambda_I=1/(n-1)\), \(\lambda_Q=(n-m)/(n(n-1))\), proving the second branch. If \(k=m=n\), only the \(I\) mode survives and the ellipsoid is a Frobenius ball on the Birkhoff affine hull.

For \(m\ge2\) the pre-saturation value is
\[
\mathfrak a_{m,n,m-1}=m-1+\frac{m-2}{n-1},
\]
whereas the saturated value is \(n/(n-m)\) when \(n>m\) (and \(1\) when \(n=m\)). If \(n=m+1\), the latter is \(m+1\), strictly larger than the former for \(m\ge3\); for \(m=2\), the pre-saturation value is one and the saturated value is greater whenever \(n>2\). For \(m=3\), comparison gives an increase at \(n=4,5\) and a decrease for \(n\ge6\). For \(m\ge4,n\ge m+2\), the elementary bound \(n/(n-m)\le(m+2)/2\le m-1 <m-1+(m-2)/(n-1)\) gives a strict decrease. For \(m=n\), the final value is one, hence a strict decrease whenever \(m\ge3\), with equality for \(m=n=2\). These exhaust the integer possibilities and give the fixed-\(m\) limiting ratio.

## Verification
The reproducible `verify.py` uses Python 3 standard-library exact rational arithmetic to enumerate all \(k\)-matchings for \(2\le m\le4\), \(m\le n\le5\), and all allowed ranks; it compares the explicit projection energies against actual vertices, reconstructs covariance entries, verifies Mahalanobis contacts of the proposed ellipsoid, and compares the complete anisotropy transition classification on a much larger finite parameter grid. Recorded successful output: `VERIFY_OK exact_enumerated_cases=25 exact_vertex_contacts=1016 rank_spectral_order_comparisons=110920`. Execute `python verify.py` in the extracted package directory. These finite checks corroborate but do **not** replace Steps 1–4, which prove the statement for every allowed integer parameter.

## Relationship to prior work
Gill and Linusson [1] defined and structurally analyzed precisely these \(k\)-assignment polytopes (including their fractional description); Torres [2] extended the normality and linear-description framework to \(k\)-matching polytopes of arbitrary bipartite graphs. The general result that an orbit-transitive convex body has an enclosing ellipsoid determined by its uniform-vertex covariance is a standard consequence of ellipsoid optimization, not claimed as new. The work here is the closed three-mode spectrum **for all rectangular cardinalities including degenerate endpoint affine hulls**, with a complete sharp integer classification of the saturated rank's Euclidean spectral reversal.

Previously published same-object results calculate the largest inscribed Euclidean ball and, for square dimensions, the maximum-volume **inscribed** John ellipsoid [3,4]. Their facet-contact and incenter results do not imply the minimum-volume **enclosing** ellipsoid: taking a polar transforms the body itself, rather than exchanging the two ellipsoids of the same body. Even the known minimum enclosing sphere gives only the sum of squared axes and cannot determine the three-mode determinant or the saturated-step reversal. Published formulas for enclosing ellipsoids of other polytopes (such as partial permutohedra and graphical zonotopes) concern different vertex configurations.

## Limitations
This is a geometric theorem for complete-bipartite fixed-cardinality matching polytopes in the canonical Frobenius realization, not for arbitrary bipartite graphs, weighted matrix norms, or uniform-volume covariance of interior points. The proof does not establish an independent bibliographic priority certificate; an equivalent calculation could exist in older transportation-polytope or matrix-design literature. The inequalities compare *squared* semiaxes, not raw semiaxes. The changing dimension at saturation is essential: ratios compare the intrinsic ellipsoids of different affine hulls, rather than two ellipsoids in one ambient full-dimensional family.

## References
[1] Jonna Gill and Svante Linusson, *The k-assignment polytope*, Discrete Optimization 6(2) (2009), 148–161, DOI 10.1016/j.disopt.2008.10.003; lawful author postprint: https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.

[2] Juan Camilo Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (first public 2023-06-20); Revista Colombiana de Matemáticas 57(2) (2023), 193–206, DOI 10.15446/recolma.v57n2.115853; https://arxiv.org/abs/2306.11910.

[3] *A Birkhoff-polytope family of incenters for partial assignment polytopes*, published mathematical finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-birkhoff-polytope-family-of-incenters-for-partial-assignment-p--6c3de65c0b12.

[4] *Exact John ellipsoid of square fixed-cardinality assignment polytopes*, published mathematical finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-square-fixed-cardinality-assignment-poly--d070eb07f633.
