# First cyclic-band departure from full-support stability in doubly stochastic least squares

## Finding

Let \(\mathcal B_n=\{X\in\mathbb R^{n\times n}:X\mathbf1=\mathbf1,\ X^\top\mathbf1=\mathbf1,\ X_{ij}\ge0\}\). Let \(\Pi_n\) be the nearest-point map onto \(\mathcal B_n\) for the Frobenius metric, but measure data perturbations and output perturbations by the maximum absolute matrix entry \(\|\cdot\|_{\max}\). Index rows and columns by \(0,1,\ldots,n-1\), and for \(n\ge3\) and \(2\le k\le n\) define the cyclic consecutive-band face support
\[
S_{n,k}=\{(i,j):(j-i)\bmod n\in\{0,1,\ldots,k-1\}\}.
\]
Its corresponding relative-interior doubly stochastic matrix \(X_{n,k}\) has every supported entry equal to \(1/k\) and all other entries zero. A *strict face point* means an input whose projection is supported exactly on \(S_{n,k}\) and for which all unsupported nonnegativity KKT multipliers are strictly positive. Let \(\lambda_{n,k}\) be the induced \(\ell^\infty\)-matrix norm of the Jacobian of \(\Pi_n\) at such a point. All strict face points for this support have the same Jacobian, and such points exist.

**Exact finite cutoff.** For every integer \(3\le n\le12\) and every \(2\le k\le n\),
\[
\lambda_{n,k}\le\lambda_{n,n}=4\left(1-\frac1n\right)^2.
\]
For \(n=13\), the *only* width giving strict excess over full support is \(k=7\), and
\[
\lambda_{13,7}=\frac{3745290244}{1096631627}
=\frac{576}{169}+\frac{99556468}{14256211151}
>\lambda_{13,13}=\frac{576}{169}.
\]
For all the other widths \(2\le k\le12\) the norm is strictly less than the full-support value. The local \(13\)-point amplification is attained by a finite pair of **strictly positive input matrices**. Consequently the global Lipschitz constant of \(\Pi_{13}\) is at least \(3745290244/1096631627\), although its exact global value is not asserted.

## Assumptions and scope

Everything is real and unweighted in the Frobenius projection objective. The word *first* refers **only** to the ordered family of cyclic consecutive-band supports \(S_{n,k}\) for \(3\le n\le13\); it does not claim the same cutoff for arbitrary faces of \(\mathcal B_n\). Only the indicated finite range is classified. The local operator norm uses arbitrary coordinatewise perturbations of the full observation matrix and the usual entrywise maximum norm on the output. The Jacobian is taken on a strictly complementary region where the active support does not change.

## Proof

**1. Reduction to an exact graph projection.** List the \(nk\) entries of \(S_{n,k}\) in lexicographic order. Let \(B=B_{n,k}\) be the \((2n-1)\)-by-\(nk\) zero-one matrix: the column corresponding to \((i,j)\) has a one in row \(i\), and also in row \(n+j\) when \(j<n-1\). The missing final column-sum equation is redundant. The bipartite support graph contains the two cyclic matchings with displacements zero and one, hence is connected. Therefore \(B\) has full row rank and
\[
Q_{n,k}=I_{nk}-B^\top(BB^\top)^{-1}B
\]
is the orthogonal projector onto the tangent space of fixed row and column sums, restricted to supported entries. Outside this support its matrix entries are zero.

Put \(X=X_{n,k}\) and let \(\mathbf J\) denote the all-ones matrix. At the input \(Y=X+2\mathbf J-\mathbf1_{S^c}\), the projection is exactly \(X\): its residual is the sum of the row/column-sum normal \(2\mathbf J\) and strictly negative coordinate normals \(-\mathbf1_{S^c}\). The on-face entries of \(X\) and the multipliers on its complement are strictly positive. The KKT conditions therefore hold with strict complementarity, and the projection is locally affine with Jacobian the zero extension of \(Q_{n,k}\). Thus
\[
\lambda_{n,k}=\max_{e\in S_{n,k}}\sum_{f\in S_{n,k}}|(Q_{n,k})_{ef}|.
\]
Simultaneous cyclic row-column translation acts transitively on each of the \(k\) edge-displacement types \(d\in\{0,\ldots,k-1\}\); it suffices to evaluate exactly the row indexed by \(e=(0,d)\) for each such \(d\).

**2. Full support.** When \(k=n\), the projection onto the homogeneous row/column-sum tangent space satisfies
\[
(Q_{n,n})_{(i,j),(a,b)}=(\mathbf1_{i=a}-1/n)(\mathbf1_{j=b}-1/n).
\]
Taking one absolute row sum gives \(4(1-1/n)^2\) exactly.

**3. Exhaustive rational certificate for the finite cutoff.** For each \(n\in\{3,\ldots,13\}\), \(k\in\{2,\ldots,n\}\), and displacement \(d\in\{0,\ldots,k-1\}\), form the integral matrix \(B\), invert its positive-definite integral Gram matrix by exact rational Gauss–Jordan elimination, and compute the row norm using the formula in step 1. There are \(440\) orbit-row calculations, not an arbitrary sample: translation symmetry proves the enumeration is exhaustive for these supports. The included standalone Python program `checker.py` uses only standard-library rational arithmetic and asserts, without numerical tolerances, every finite inequality, full-support formula, the unique exceptional width, and the exact exceptional fraction and difference. For \(n=3,\ldots,12\), the maximizing width is always \(k=n\). For \(n=13\), exactly \(k=7\) exceeds that width; its maximum comes from displacement \(d=0\). This is a finite, completely specified rational certificate, not an inference from floating-point experiments.

**4. Attainment by strictly positive data.** For \((n,k)=(13,7)\), write \(S=S_{13,7}\), \(Q=Q_{13,7}\), and \(e=(0,0)\). Let \(H\) vanish off \(S\), and on supported entries set \(H_f=\operatorname{sgn}(Q_{ef})\). The exact certificate finds every \(Q_{ef}\ne0\), so \(\|H\|_{\max}=1\) and \((QH)_e=\lambda_{13,7}\). Choose \(t=1/1000\) and the positive inputs
\[
Y_0=X_{13,7}+2\mathbf J-\mathbf1_{S^c},\qquad Y_1=Y_0+tH.
\]
The projected candidates are \(Z_0=X_{13,7}\) and \(Z_1=X_{13,7}+tQH\), with \(QH\) extended by zero outside \(S\). Exact rational calculations give the smallest supported coordinate of \(Z_1\) as
\[
\frac{77794225863}{548315813500}>0
\]
and the smallest complementary KKT multiplier as
\[
\frac{1094735762271}{1096631627000}>0.
\]
The row/column sums of \(Z_1\) equal one and the residual has the appropriate equality normals and complementary negative coordinate normals. These strict KKT checks prove \(\Pi_{13}(Y_i)=Z_i\), not just an infinitesimal assertion. Both \(Y_i\) are strictly positive and
\[
\frac{\|\Pi_{13}(Y_1)-\Pi_{13}(Y_0)\|_{\max}}{\|Y_1-Y_0\|_{\max}}=\frac{3745290244}{1096631627}.
\]
The all-ones shift in the input does not change its Euclidean projection, since every doubly stochastic matrix has the same total entry sum.

## Verification

Run `python3 checker.py` with Python \(3\) (standard library only). The program constructs every matrix directly from the defining support, carries out exact rational Gauss–Jordan inversion, checks all \(440\) symmetry representatives, independently constructs the maximizing sign direction, verifies the active primal coordinates and complementary multipliers, and confirms the exact finite-pair ratio. The expected terminal line is `ALL EXACT CHECKS PASSED`. An inverse matrix check uses exact pivot elimination; the nonzero pivot property follows independently from connectedness of the bipartite band graph.

## Relationship to prior work

Kassel and Wu's transfer-current formulation [1] supplies the graph-Laplacian viewpoint for the same edge-gradient projector. Hager and Zhang [2] study sparse polyhedral projection algorithms. Li, Sun and Toh [3, Sections 2–5] give general active-constraint Jacobian formulas for the Birkhoff projection and large-scale numerical algorithms. None of the examined results states the exact comparison of \(S_{n,k}\) with full support through \(n=13\), the unique width-seven excess, or this finite positive-input witness. In particular, the general Jacobian formula determines the matrix to be evaluated but does not itself tabulate or prove the \(440\) exact absolute-row comparisons. The difference is a finite sharp support-family boundary, not a claimed new general Jacobian identity.

## Limitations

This result does not determine the global Lipschitz modulus of \(\Pi_n\) for any \(n\), does not examine arbitrary Birkhoff supports, and makes no asymptotic assertion for large \(n\). It does not establish the first departure among all faces or show that every support-size change behaves monotonically. The historical claim is confined to material inspected; earlier equivalent tabulations under other electrical-network or convex-projection terminology remain possible. The exact rational certificate is finite and makes no inference beyond the declared range.

## References

[1] A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, first posted 10 December 2013, https://arxiv.org/abs/1312.2946.

[2] W. W. Hager and H. Zhang, *Projection onto a Polyhedron that Exploits Sparsity*, SIAM Journal on Optimization 26 (2016), 1773–1798, DOI:10.1137/15M102825X, published online 1 September 2016.

[3] X. Li, D. Sun and K.-C. Toh, *On the efficient computation of a generalized Jacobian of the projector over the Birkhoff polytope*, arXiv:1702.05934, first posted 20 February 2017, https://arxiv.org/abs/1702.05934.
