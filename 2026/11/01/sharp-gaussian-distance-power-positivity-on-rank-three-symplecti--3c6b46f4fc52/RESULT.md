# Sharp Gaussian distance-power positivity on rank-three symplectic dual polar graphs

## Finding
Let \(q\ge2\) be any prime power. Let \(V=\mathbb F_q^6\) have a nondegenerate alternating bilinear form, let \(X_q\) be its three-dimensional maximal totally isotropic subspaces, and give \(X_q\) the dual-polar graph distance \(\rho(U,W)=3-\dim(U\cap W)\). For \(p>0\), put \(D_p(U,W)=\rho(U,W)^p\) and \(D_p(U,U)=0\); for \(p=0\), stipulate \(D_0(U,W)=1\) when \(U\ne W\) and \(D_0(U,U)=0\). For \(t>0\), put \(K_{t,p}(U,W)=\exp(-tD_p(U,W))\).

There is a unique \(\alpha_q\in(0,1)\) with
\[
q^2(3^{\alpha_q}-2^{\alpha_q})=1.
\]
For every such \(q\) and every \(p\ge0\),
\[
K_{t,p}\succeq0\text{ for every }t>0\quad\Longleftrightarrow\quad 0\le p\le\alpha_q.
\]
In fact every admitted \(K_{t,p}\) is strictly positive definite for every \(t>0\). For \(p>\alpha_q\), the kernel fails positive semidefiniteness for all sufficiently small positive \(t\).

At \(p=\alpha_q\), the powered distance matrix restricted to the zero-sum subspace has exactly \(q^6+q^4+q^2\) zero eigenvalues, and all remaining eigenvalues on that subspace are strictly negative. Consequently \(D_{\alpha_q}\) is the squared distance matrix of a configuration of \(|X_q|=(q+1)(q^2+1)(q^3+1)\) **distinct** Euclidean points with minimum possible ambient dimension precisely
\[
q(q^2+1)^2.
\]
For \(0\le p<\alpha_q\), the minimum squared-distance embedding dimension is \(|X_q|-1\). For fixed \(q\), the threshold is exact as given; as \(q\to\infty\) through prime powers,
\[
\alpha_q=\frac{1}{q^2\log(3/2)}+O(q^{-4}).
\]

## Assumptions and scope
The finite field has arbitrary prime-power order, including characteristic two. A *Lagrangian* is a maximal (dimension-three) totally isotropic subspace of the six-dimensional symplectic vector space; the graph joins two distinct Lagrangians when their intersection has dimension two. The distance formula above is exact. The parameter domain is all real \(p\ge0\), with the explicit off-diagonal convention at \(p=0\), and all real \(t>0\). The assertions are universal in the prime power \(q\); no restriction to particular finite test cases is assumed.

## Proof
**1. Intersection algebra.** Set \(S=q^2+q+1\). Double-counting incidence of nonzero one-dimensional subspaces with Lagrangians, followed by passage to a rank-two symplectic quotient, gives
\[
N=|X_q|=(q+1)(q^2+1)(q^3+1).
\]
The standard dual-polar intersection counts (also obtained by choosing a codimension-one subspace in a generator and one of its \(q\) alternative extensions) are
\[
b_i=q^{i+1}[3-i]_q,\qquad c_i=[i]_q,\qquad a_i=q^i-1\qquad(0\le i\le3),
\]
where \([h]_q=(q^h-1)/(q-1)\), \(b_3=c_0=0\), and \(a_i+b_i+c_i=qS\). Explicitly, the action of the adjacency matrix on functions constant on distance spheres is
\[
B=\begin{pmatrix}
0&qS&0&0\\
1&q-1&q^2(q+1)&0\\
0&q+1&q^2-1&q^3\\
0&0&S&q^3-1
\end{pmatrix}.
\]
Its characteristic polynomial factors exactly as
\[
\det(zI-B)=(z-qS)(z-q^2-q+1)(z+1)(z+S).
\]
The distance matrices \(A_0=I,A_1,A_2,A_3\) satisfy
\[
A_1^2=qS I+(q-1)A_1+(q+1)A_2,
\]
\[
A_1A_2=q^2(q+1)A_1+(q^2-1)A_2+SA_3.
\]
Thus the complete eigenvalue table for \(A_1,A_2,A_3\), with one row per primitive common eigenspace, is

| Eigenspace | \(A_1\) | \(A_2\) | \(A_3\) |
|---|---:|---:|---:|
| constants | \(qS\) | \(q^3S\) | \(q^6\) |
| \(E_1\) | \(q^2+q-1\) | \(q(q^2-q-1)\) | \(-q^3\) |
| \(E_2\) | \(-1\) | \(-q^2\) | \(q^2\) |
| \(E_3\) | \(-S\) | \(qS\) | \(-q^3\) |

The distance sphere valencies are \((k_0,k_1,k_2,k_3)=(1,qS,q^3S,q^6)\). Standard row orthogonality, equivalently \(m_j=N/(\sum_{i=0}^3 P_{j,i}^2/k_i)\), yields the multiplicities
\[
m_0=1,\quad m_1=\frac{q(q^2+1)S}{2},\quad m_2=q^2(q^4+q^2+1),\quad m_3=\frac{q(q^2+1)(q^2-q+1)}{2}.
\]
The four values sum exactly to \(N\); every \(m_j\) is positive.

**2. The precise sign obstruction.** Write \(u=2^p\) and \(v=3^p\), including \(u=v=1\) at \(p=0\). Since \(D_p=A_1+uA_2+vA_3\), its three eigenvalues on the zero-sum subspace are
\[
\begin{aligned}
F_1(p)&=q^2+q-1+q(q^2-q-1)2^p-q^3 3^p,\\
F_2(p)&=-1+q^2(3^p-2^p),\\
F_3(p)&=-S+qS2^p-q^3 3^p.
\end{aligned}
\]
At \(p=0\), all three equal \(-1\). The function \(3^p-2^p\) is strictly increasing on \([0,\infty)\), starts at zero, and equals one at \(p=1\). Hence \(F_2\) has exactly one zero \(\alpha_q\in(0,1)\), is negative before it, and positive afterward.

The other branches are strictly negative for \(0\le p\le1\). Indeed,
\[
F_3''(p)=qS(\log2)^2 2^p-q^3(\log3)^2 3^p<0
\]
for \(p\ge0\), because \(S/q^2\le7/4<(\log_2 3)^2\) (use \(\log_2 3>4/3\)). When \(q\ge3\), one also has \(F_3'(0)<0\), because \(S/q^2\le13/9<3/2<\log_2 3\). Therefore \(F_3(p)<F_3(0)=-1\) for all \(p>0\) in this case. When \(q=2\), one has \(F_3(0)=-1\) and
\[
F_3'(0)=14\log2-8\log3=2\log(128/81)<1.
\]
The last strict bound follows from \(128/81<13/8<e^{1/2}\). Strict concavity then implies \(F_3(p)\le-1+pF_3'(0)<0\) for \(0\le p\le1\). Finally,
\[
F_3(p)-F_1(p)=2q(q+1)(2^p-1)\ge0,
\]
so \(F_1(p)\le F_3(p)<0\) on this interval. It follows that \(D_p\) is conditionally negative semidefinite exactly for \(0\le p\le\alpha_q\), and at equality its entire zero-sum nullspace is \(E_2\), of multiplicity \(m_2\).

**3. Exponential positivity and embedding rank.** The finite-space Schoenberg equivalence says a symmetric zero-diagonal matrix \(D\) is conditionally negative semidefinite exactly when the matrix with entries \(e^{-tD_{ij}}\) is positive semidefinite for every \(t>0\). This proves the classification. Strict positivity at admissible \(p\) follows by Euclidean squared-distance representation of \(D_p\) and strict positive definiteness of the Gaussian Gram matrix on distinct Euclidean points. The points are distinct since all off-diagonal powered distances are positive. Conversely, if \(p>\alpha_q\), a vector in \(E_2\) has positive \(D_p\)-quadratic form and zero coordinate sum, so its \(K_{t,p}\)-quadratic form equals the strictly negative quantity \(-t\langle D_pv,v\rangle+O(t^2)\) for sufficiently small positive \(t\).

Let \(H=I-J/N\). The centered Gram matrix of the Euclidean realization is \(-HD_pH/2\), so its rank is the minimum embedding dimension. At the endpoint, \(m_2=q^6+q^4+q^2\), hence
\[
N-1-m_2=q(q^2+1)^2.
\]
Below the endpoint, all three nontrivial eigenvalues are negative, and the rank is \(N-1\). Finally, expanding \(3^p-2^p=p\log(3/2)+O(p^2)\) at the unique root proves the stated asymptotic.

## Verification
The accompanying standalone script `dual_polar_rank3_checker.py` is run with Python 3 and NumPy using `python dual_polar_rank3_checker.py`. It independently enumerates the 135 Lagrangian subspaces over \(\mathbb F_2\) from binary row spaces, reconstructs all pair distances, verifies the full exact integer distance-intersection identities, and checks the predicted adjacency eigenvalue multiplicities and endpoint rank numerically. It additionally tests the symbolic intersection/eigenvalue formulas and sign inequalities for representative field orders \(q=2,3,4,5,7,8,9,11,16,25,32,64,101\). The observed output was `ALGEBRA_CHECK_OK`, `FULL_GF2_GRAPH_CHECK_OK`, and `CHECK_OK`. These finite tests are not used to infer the universal theorem; that theorem is proved by the algebraic and analytic argument above.

## Relationship to prior work
The original dual-polar association scheme, the symplectic distance-intersection parameters, and their general eigenvalue formulas are established results. Moorhouse and Williford (arXiv:1504.01067, §4) explicitly give the symplectic graph construction and the intersection parameters in odd characteristic; Ihringer and Metsch (arXiv:1510.01697, §7, especially Theorem 7.2) present the general dual-polar eigenmatrix for all relevant prime powers. Their results furnish the spectral machinery, but the inspected material does not state the distance-power Gaussian positivity interval, prove which nonconstant branch sets its endpoint for every field order, or identify the resulting Euclidean rank collapse. Feragen, Lauze, and Hauberg (arXiv:1411.0296, Theorem 5) restate the general Schoenberg criterion; it has no polar-graph-specific cutoff. The new mathematical step here is the field-uniform sign comparison for the three radial eigenbranches and the sharp endpoint rank, not a new derivation of the association scheme itself.

## Limitations
The parameter \(p\) is nonnegative and the statement concerns **positivity for every positive scale** \(t\); it does not classify positivity at an isolated fixed scale when \(p>\alpha_q\). The general eigenmatrix is prior mathematics, not claimed as new. Independent mathematical audit and validation have not been performed. Earlier association-scheme presentations could contain an equivalent powered-distance special case; this remains an originality risk despite the targeted comparisons.

## References
1. A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (initial public preprint 2014-11-02), especially the Schoenberg equivalence.
2. G. E. Moorhouse, J. Williford, *Double Covers of Symplectic Dual Polar Graphs*, arXiv:1504.01067 (initial public preprint 2015-04-04), §4.
3. F. Ihringer, K. Metsch, *Large \(\{0,1,\ldots,t\}\)-Cliques in Dual Polar Graphs*, arXiv:1510.01697 (initial public preprint 2015-10-06), §7.
