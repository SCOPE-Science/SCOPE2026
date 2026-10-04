# Exact even centro-affine facet spectrum of parallelotopes
## Finding
For every full-dimensional origin-symmetric parallelotope \(P\subset\mathbb R^n\) with \(n\ge 2\), use the facet masses, ridge conductances, and Dirichlet form introduced by Hu and Ivaki:
\[
m_i=h_i\mathcal H^{n-1}(F_i),\qquad
c_{ij}=\frac{h_i h_j\mathcal H^{n-2}(F_i\cap F_j)}{\sin\theta_{ij}},
\]
with \(c_{ij}=0\) for nonadjacent facets, and
\[
L_P(f,f)=\sum_{\{i,j\}}c_{ij}(f_i-f_j)^2.
\]
For every even facet function \(f\), meaning \(f_{-i}=f_i\), the exact identity
\[
L_P(f,f)=n\sum_i m_i(f_i-\bar f)^2
\]
holds. Hence every nonconstant even Rayleigh quotient is exactly \(n\). The complete even generalized spectrum is therefore \(0\) on constants and \(n\) with multiplicity \(n-1\), and in particular
\[
\lambda_{1,e}(P)=n.
\]

## Assumptions and scope
The polytope is full dimensional, origin symmetric, and a parallelotope. The dimension satisfies \(n\ge 2\). Facets are labeled in antipodal pairs as in Hu--Ivaki. The statement concerns their finite-dimensional facet-network operator; it does not identify the spectrum of a smooth approximation, and it does not assert that every parallelotope is a local or global minimizer of \(\lambda_{1,e}\) under support perturbations.

## Proof
First note an affine covariance that is useful independently of the special shape. Let \(A\in GL(n,\mathbb R)\), let \(P'=AP\), and let a facet of \(P\) have unit normal \(u_i\) and support value \(h_i\). Put
\[
w_i=A^{-T}u_i,\qquad u_i'=\frac{w_i}{\lVert w_i\rVert},\qquad h_i'=\frac{h_i}{\lVert w_i\rVert}.
\]
The codimension-one Jacobian formula gives
\[
\mathcal H^{n-1}(AF_i)=|\det A|\,\lVert w_i\rVert\,\mathcal H^{n-1}(F_i),
\]
so
\[
m_i'=|\det A|m_i.
\]
For an adjacent pair, write \(R_{ij}=F_i\cap F_j\). Since \(\lVert u_i\wedge u_j\rVert=\sin\theta_{ij}\), the codimension-two Jacobian formula is
\[
\mathcal H^{n-2}(A R_{ij})
=|\det A|\frac{\lVert w_i\wedge w_j\rVert}{\sin\theta_{ij}}\mathcal H^{n-2}(R_{ij}).
\]
The transformed angle satisfies
\[
\sin\theta_{ij}'=
\frac{\lVert w_i\wedge w_j\rVert}{\lVert w_i\rVert\lVert w_j\rVert}.
\]
Substitution into the conductance definition gives
\[
c_{ij}'=|\det A|c_{ij}.
\]
Thus both the Dirichlet numerator and weighted-variance denominator are multiplied by \(|\det A|\), so the Rayleigh form is invariant under invertible linear images.

Every origin-symmetric parallelotope is an invertible linear image of a box
\[
B=\prod_{k=1}^n[-a_k,a_k],\qquad a_k>0.
\]
It is therefore enough to calculate on \(B\). Put \(V=\prod_{k=1}^n a_k\). Each signed coordinate facet has support value \(a_i\) and area \(2^{n-1}V/a_i\), hence every facet mass is the same number
\[
M=2^{n-1}V.
\]
If two facets come from distinct coordinate directions, their normals are orthogonal and their common ridge has area \(2^{n-2}V/(a_i a_j)\). Hence every such ridge has conductance
\[
C=2^{n-2}V.
\]
Opposite facets are nonadjacent.

An even facet function is determined by values \(x_1,\ldots,x_n\) on the \(n\) antipodal facet pairs. Its weighted mean is
\[
\bar x=\frac1n\sum_{i=1}^n x_i.
\]
For each unordered coordinate pair \(i<j\), there are four adjacent signed-facet pairs, so
\[
L_B(f,f)=4C\sum_{i<j}(x_i-x_j)^2.
\]
The weighted variance over the \(2n\) signed facets is
\[
\sum_i m_i(f_i-\bar f)^2
=2M\sum_{i=1}^n(x_i-\bar x)^2.
\]
Because \(4C=2M=2^nV\), the elementary complete-graph identity
\[
\sum_{i<j}(x_i-x_j)^2
=n\sum_{i=1}^n(x_i-\bar x)^2
\]
gives the claimed quadratic-form identity. The even facet space has dimension \(n\); constants occupy one dimension. Therefore the orthogonal complement of constants has dimension \(n-1\), and the generalized operator is exactly multiplication by \(n\) there. This proves the spectral statement.

## Verification
The proof is analytic and covers all \(n\ge 2\). A standalone exact-rational checker, `verify.py`, independently evaluates the box numerator and denominator for nonconstant rational test vectors in dimensions \(2,3,4,5\) and checks the identity exactly. Its successful output is `VERIFY_OK exact box Rayleigh identity in dimensions [2, 3, 4, 5]`.

The computation is only a finite algebraic sanity check. The infinite-dimensional range of dimensions and the affine reduction are established by the formulas above, not by enumeration or numerical evidence.

## Relationship to prior work
Hu and Ivaki introduced the facet-network masses, conductances, and even spectral gap in arXiv:2609.21670v1. Their Theorem 1.1 gives a lower bound for local minimizers under support perturbations. Remark 1.2 strengthens that bound in terms of eigenvalue multiplicity and states that, among global minimizers with bounded facet-pair count, multiplicity \(n-1\) forces a parallelotope. The paper does not state the exact quadratic-form identity above, the exact value \(\lambda_{1,e}=n\) for every parallelotope, or the complete even spectrum of a parallelotope.

The same paper recalls smooth results giving lower bounds of \(n\) for unconditional smooth bodies and smooth origin-symmetric zonoids. Those smooth inequalities concern a different operator and regularity class and do not imply the discrete facet-network equality or its \(n-1\) multiplicity. The present calculation supplies the canonical exact benchmark suggested by the parallelotope extremal discussion.

## Limitations
No claim is made that the value \(n\) characterizes parallelotopes among all origin-symmetric polytopes. No local-minimality or global-minimality statement is proved. The argument uses the specific Hu--Ivaki normalization of facet masses and ridge conductances; changing that normalization changes the operator. The literature comparison did not find an earlier public statement of the exact full even spectrum, but a residual bibliographic risk remains because Hu--Ivaki explicitly note that further details concerning their multiplicity discussion may appear elsewhere.

## References
1. Y. Hu and M. N. Ivaki, *Centro-affine spectral geometry of polytopes*, arXiv:2609.21670v1, first public 18 September 2026. In particular, Eq. (1.3), Theorem 1.1, and Remark 1.2.
2. Y. Hu and M. N. Ivaki, *Centro-affine Poincaré inequality: Unconditional convex bodies*, arXiv:2607.20223, 2026.
3. R. van Handel, *The local logarithmic Brunn--Minkowski inequality for zonoids*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 2327, 2023, pp. 355--379.
