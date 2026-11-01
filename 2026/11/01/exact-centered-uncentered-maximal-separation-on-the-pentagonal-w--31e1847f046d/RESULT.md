# Exact centered–uncentered maximal separation on the pentagonal wheel

## Finding
Let \(G=K_1\vee C_5\) have hub \(0\) and rim vertices \(1,2,3,4,5\), cyclically ordered. Let \(M_c\) and \(M_u\) be the centered and uncentered Hardy–Littlewood maximal operators over closed graph-distance balls, using counting measure. Their exact, attained real \(\ell^2\) norms are
\[
\|M_c\|_{2\to2}=\sqrt{3/2},\qquad
\|M_u\|_{2\to2}=\sqrt{\lambda_*},
\]
where \(\lambda_*\) is the unique real root in \((81/50,1621/1000)\) of
\[
64\lambda^3-120\lambda^2+27\lambda-1=0.
\]
Thus \(\|M_u\|_{2\to2}>\|M_c\|_{2\to2}\). Numerically the two norms are approximately \(1.2247448714\) and \(1.2730413769\), respectively.

For the centered operator, every nonzero real extremizer has, up to a positive scalar and independently chosen coordinate signs, the absolute-value pattern \((5,1,1,1,1,1)\), in hub-first order. There is one labeled nonnegative extremizing ray.

For the uncentered operator, put
\[
d=64\lambda_*^2-24\lambda_*+1,\qquad
y=\frac{24\lambda_*-1}{d},\qquad
z=\frac{8\lambda_*-1}{d}.
\]
Here \(0<z<y<1\). Every nonzero extremizer has, up to positive scaling and independent coordinate signs, a cyclic rotation of the rim coordinates of \((1,1,y,z,z,y)\), with the first entry corresponding to the hub. There are exactly five labeled nonnegative extremizing rays, forming one orbit of the rim-rotation group. Hence freeing the ball centers both strictly raises the strong Hilbert norm and breaks the centered extremizer's full rim symmetry.

## Assumptions and scope
The six vertices are \(\{0,1,2,3,4,5\}\). Vertex \(0\) is adjacent to every rim vertex, while rim vertices \(i,j\) are adjacent exactly when \(i-j\equiv\pm1\pmod5\). The metric is unweighted shortest-path distance. Every distinct pair is at distance one or two. A ball is \(B(c,r)=\{v:d_G(c,v)\le r\}\); radii \(0,1,2\) suffice. The operators are
\[
M_cf(v)=\max_{r=0,1,2}\frac{\sum_{w\in B(v,r)}|f(w)|}{|B(v,r)|},
\quad
M_uf(v)=\max_{c,r:\ v\in B(c,r)}\frac{\sum_{w\in B(c,r)}|f(w)|}{|B(c,r)|}.
\]
The norm is the supremum of \(\|M f\|_{\ell^2(V)}/\|f\|_{\ell^2(V)}\) over nonzero real functions. Complex inputs give the same norm when defined through absolute values, but the equality classification here is stated for real inputs.

## Proof
**Exact finite linearization.** The distinct metric balls comprise six singletons, five four-point balls centered at rim vertices, and the full six-point ball. Each hub output of \(M_c\) has two possible averaging rows and each rim output three, producing \(2\cdot3^5=486\) selected-row matrices. For \(M_u\), the hub has seven distinct possible rows (one singleton, five rim-centered four-point balls, and the full ball), and each rim output five (one singleton, three admissible four-point balls, and the full ball), producing \(7\cdot5^5=21875\) selected-row matrices.

Write \(A_\sigma\) for a matrix formed by choosing one admissible averaging row independently at each output vertex. For every input \(f\), taking \(g=|f|\) yields
\[
\|M f\|_2^2=\max_\sigma\|A_\sigma g\|_2^2.
\]
All \(A_\sigma\) are entrywise nonnegative. For each matrix, an operator-norm maximizing right singular vector may be chosen nonnegative (replace any singular vector by its coordinatewise absolute value). Therefore
\[
\|M\|_{2\to2}^2=\max_\sigma\lambda_{\max}(A_\sigma^{\mathsf T}A_\sigma).
\]
This maximization is exhaustive, not sampled.

**Exact upper-bound certificates.** Every selected row has denominators dividing \(12\), so \(B_\sigma=12A_\sigma\) is integral. A symmetric rational matrix is positive definite if and only if every leading principal minor is positive. The accompanying standalone verifier applies exact fraction-free Bareiss elimination to every matrix, using only integers. It checks that \(216I-B_\sigma^{\mathsf T}B_\sigma\) is positive definite for exactly \(485\) centered selections. The remaining centered selection is the one with hub singleton and all five rim-centered radius-one averages. It also checks that
\[
5832I-25B_\sigma^{\mathsf T}B_\sigma
\]
is positive definite for exactly \(21870\) uncentered selections. The remaining five are precisely the five rim rotations of one exceptional selection. Thus every nonexceptional centered matrix has squared norm \(<3/2\), and every nonexceptional uncentered matrix has squared norm \(<81/50\). The finite enumeration is reproducible using `python3 wheel6_certificate.py` and no external libraries.

**Centered exceptional matrix and equality.** The centered exceptional matrix selects the hub singleton and every rim radius-one ball. Its input \((5,1,1,1,1,1)\) produces output \((5,2,2,2,2,2)\), yielding squared quotient \((25+5\cdot4)/(25+5)=3/2\). This positive input is a right singular eigenvector for the squared norm, and all its selected ball averages beat every alternative strictly. Because its Gram matrix is nonnegative and possesses a strictly positive eigenvector, \(3/2\) is the Perron eigenvalue; the corresponding eigenspace is one-dimensional (equivalently, the radial quotient has a simple leading eigenvalue). The integer certificate excludes every other selection. All centered extremizers therefore have the asserted pattern and arbitrary independent signs.

**Uncentered exceptional matrix and equality.** Fix the rim peak at vertex \(1\). The exceptional averaging matrix, in hub-first order, is
\[
A=\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&0&0&0\\
1/4&1/4&1/4&0&0&1/4\\
1/4&1/4&1/4&1/4&0&0\\
1/4&1/4&0&0&1/4&1/4\\
1/4&1/4&1/4&0&0&1/4
\end{pmatrix}.
\]
On symmetric vectors \((x,x,y,z,z,y)\), its Gram operator is the symmetric three-dimensional matrix
\[
\frac1{16}\begin{pmatrix}24&6&2\\6&5&1\\2&1&1\end{pmatrix}.
\]
The characteristic polynomial of this reduced matrix is \((64\lambda^3-120\lambda^2+27\lambda-1)/64\). The cubic changes sign across \((81/50,1621/1000)\) and is strictly increasing on that interval; hence it has exactly one root \(\lambda_*\) there. With \(x=1\), its eigenvector equations solve to the displayed values \(y,z\), both strictly between zero and one with \(z<y\). The remaining Gram eigendirections have no greater eigenvalue: more directly, \(A^{\mathsf T}A\) is entrywise nonnegative, and its strictly positive eigenvector forces \(\lambda_*\) to equal the spectral radius (the weighted sup-norm Perron bound).

The selecting rows are strict for the maximizing vector. The hub and vertex \(1\) each choose their singleton with average \(1\); rim vertices \(2,5\) choose the four-point ball centered at \(1\), averaging to \((1+y)/2\); and vertices \(3,4\) choose the adjacent four-point balls centered at \(2,5\), respectively, averaging to \((2+y+z)/4\). Comparing with all other balls gives strict inequalities from \(0<z<y<1\). The verifier also proves the strict comparisons by exact rational interval arithmetic over the isolated root bracket. Hence this eigenvector actually attains \(M_u\), with squared norm \(\lambda_*>81/50>3/2\).

The five exceptional matrices are exactly the rim rotations of this matrix. Their top singular eigenvalues are simple, as their Gram matrices admit strictly positive eigenvectors and the reduced cubic root is simple (or by Perron–Frobenius irreducibility). The strict selection and exact enumeration therefore classify *all* real equality cases, allowing independent input signs.

## Verification
Run `python3 wheel6_certificate.py` with Python 3 standard library. The program independently constructs graph balls, enumerates the \(486\) centered and \(21875\) uncentered legal matrix selections, computes all Gram matrices and fraction-free integer principal-minor tests, identifies precisely the exceptional selections and their rim-rotation orbit, checks the exceptional Gram matrix and cubic eigenvector identities, isolates the cubic root with exact rationals, and proves the maximizing ball choices strictly through rational interval comparisons. Its deterministic terminal result is `CERTIFICATE_OK centered_selections=486 centered_exceptions=1 uncentered_selections=21875 uncentered_exceptions=5`, followed by the stated thresholds and cubic. The proof uses no numerical sampling or unverified infinite extrapolation.

## Relationship to prior work
Soria and Tradacete established the finite-graph centered maximal-operator framework and sharp general estimates, with special results for complete graphs, stars and paths [1]. Their norm analysis does not contain the uncentered pentagonal-wheel \(\ell^2\) constant or its five-ray equality classification. González-Riquelme and Madrid determined sharp centered \(\ell^2\) norms for complete graphs and stars, and explicitly defined the uncentered graph-ball version [2]; their analyzed graph families do not include \(K_1\vee C_5\). A subsequent study of centered maximal-operator extremizers again treats complete graphs and stars rather than wheels [3]. Sharp results for the centered variation seminorm and other graph invariants cannot imply this exact uncentered strong-\(\ell^2\) norm or the centered/uncentered equality-set separation. This claim does not attribute originality to the definitions, finite-matrix reduction principle, Perron theory, or integer linear-algebra testing.

## Limitations
The result is confined to the unweighted six-vertex pentagonal wheel, counting measure, graph-distance balls, and strong \(\ell^2\). No claim is made for other wheels, weighted measures, \(\ell^p\) with \(p\ne2\), or graph variation norms. Complete publication-priority exclusion of unindexed equivalent computations is not asserted.

## References
[1] J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1 (first publicly submitted 2014-10-22), https://arxiv.org/abs/1410.6204.

[2] C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first publicly submitted 2020-05-06), https://arxiv.org/abs/2005.03146.

[3] C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1 (first publicly submitted 2020-11-05), https://arxiv.org/abs/2011.02630.
