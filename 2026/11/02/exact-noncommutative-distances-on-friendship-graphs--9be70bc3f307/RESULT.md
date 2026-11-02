# Exact noncommutative distances on friendship graphs

## Finding

For every integer \(m\ge2\), let \(F_m\) be the friendship graph formed by \(m\) edge-disjoint triangles with a common vertex \(h\), and other vertices \(u_i,v_i\) for \(1\le i\le m\). Its unweighted adjacency matrix is denoted \(D\). The Connes distance associated to this finite-dimensional Dirac operator is

\[
d_D(x,y)=\sup\big\{|f(x)-f(y)|:f:V(F_m)\to\mathbb R,\ \|[D,\operatorname{diag}(f)]\|_{2\to2}\le1\big\}.
\]

For distinct vertices, **every distance is independent of \(m\)** and has precisely one of two values:

\[
\boxed{d_D(h,u_i)=d_D(h,v_i)=d_D(u_i,v_i)=\sqrt{\frac23}},
\]

\[
\boxed{d_D(x,y)=\sqrt{\frac32}\quad\text{when }x\in\{u_i,v_i\},\ y\in\{u_j,v_j\},\ i\ne j.}
\]

Also \(d_D(x,x)=0\). In particular, the cross-triangle distance is \(3/2\) times each within-triangle distance, whereas the corresponding shortest-path ratio is two. The answer applies to every finite number of petals, not only the five-vertex butterfly graph.

## Assumptions and scope

All graph edges have unit adjacency coefficient and there are no other edges; the full adjacency matrix, rather than an incidence-Dirac operator, defines the commutator. The operator norm is the Euclidean spectral norm over \(\mathbb C^{2m+1}\). Only selfadjoint diagonal functions are needed: if a complex diagonal function is allowed and has a prescribed endpoint difference, multiplication by a unit complex scalar and taking its real part preserve that endpoint difference and do not increase the commutator norm. This establishes equivalence with the usual selfadjoint finite-spectral-triple convention.

## Proof

**1. Reduction to one or two triangles.** For a vertex pair in one triangle, restrict the commutator to the principal submatrix on the hub and that triangle. Its spectral norm is no larger than the full norm. For a pair in two different triangles, do the same for the induced five-vertex two-triangle graph. Conversely, any function on the retained vertices extends to every omitted triangle by giving both its leaves the hub value. Every commutator entry involving an omitted leaf then vanishes, leaving the retained commutator plus a zero block. Thus both inequalities are equalities. This argument is valid for every \(m\ge2\) and does not assume an asymptotic limit.

**2. One triangle.** Subtract a constant so that the hub value is zero, and write the other values as \(a,b\). The commutator is a real skew-symmetric \(3\times3\) matrix. Its characteristic polynomial is

\[
\lambda\big(\lambda^2+L_3(a,b)\big),\qquad
L_3(a,b)=a^2+b^2+(a-b)^2.
\]

Consequently its norm squared equals \(L_3(a,b)\). For fixed hub-to-leaf difference \(a\), completing the square gives

\[
L_3(a,b)=\frac32a^2+2\left(b-\frac a2\right)^2.
\]

Thus a unit-norm commutator permits \(|a|\le\sqrt{2/3}\), attained at \(b=a/2\). For the leaf-to-leaf difference \(\delta=a-b\), write \(a=s+\delta/2\), \(b=s-\delta/2\). Then

\[
L_3(a,b)=2s^2+\frac32\delta^2.
\]

The same sharp distance \(\sqrt{2/3}\) is attained at \(s=0\), or \(a=-b=\delta/2\).

**3. Leaves in different triangles.** Work on the five vertices \(h,u_1,v_1,u_2,v_2\). The automorphism exchanging the two triangles fixes the hub and preserves the commutator norm. For any test function \(f\), replace it by half the difference between \(f\) and the function obtained by exchanging the triangles. This leaves \(f(u_1)-f(u_2)\) unchanged (including sign), and by convexity cannot increase the norm. After subtracting a constant, the values are therefore

\[
(f(h),f(u_1),f(v_1),f(u_2),f(v_2))=(0,a,b,-a,-b).
\]

Writing \(\delta=a-b\) and \(z=(a,b,-a,-b)^{\mathsf T}\), the skew commutator is

\[
K=\begin{pmatrix}0&z^{\mathsf T}\\-z&B\end{pmatrix},\qquad
B=\begin{pmatrix}0&-\delta&0&0\\\delta&0&0&0\\0&0&0&\delta\\0&0&-\delta&0\end{pmatrix}.
\]

Here \(B^2=-\delta^2 I_4\) and \(z^{\mathsf T}Bz=0\). Direct block elimination, or the invariant span of the hub, \(z\), and \(Bz\), gives the exact characteristic polynomial

\[
\det(\lambda I_5-K)=\lambda(\lambda^2+\delta^2)\big(\lambda^2+\|z\|_2^2+\delta^2\big).
\]

It follows that

\[
\|K\|^2=2(a^2+b^2)+(a-b)^2
=\frac83a^2+3\left(b-\frac a3\right)^2.
\]

The endpoint difference is \(2a\); hence \(\|K\|^2\ge\frac23(2a)^2\), with equality at \(b=a/3\). The maximal difference for \(\|K\|\le1\) is therefore \(\sqrt{3/2}\). Equality is attained by \(a=\sqrt{3/8}\), \(b=a/3\). The other cross-petal pairs follow by graph automorphisms. This exhausts all vertex-pair orbits and proves the theorem.

## Verification

Run `python artifacts/check_windmill.py` with SymPy and NumPy installed. The standalone checker verifies exact symbolic characteristic polynomials for both retained commutator matrices, exact completed-square identities giving the three optima, and direct norm-one sharp witnesses for all graphs having one through eight triangles. A successful run prints a single `PASS` line. Symbolic matrix calculations support the algebraic identities; the reduction and all-\(m\) quantifiers are proved above and are not inferred from finite experiments.

## Relationship to prior work

Clare, Li, Poon and Swartz [1] develop matrix-optimization methods for graph Connes distances and characterize weighted path graphs; their explicit path formulas do not imply the two-triangle cross-petal calculation because the butterfly graph has cycles. Besnard [2] establishes the graph-pruning theorem and the triangle distance \(\sqrt{2/3}\) for unit edges. Accordingly, the one-triangle value and locality principle are **earlier results**, not asserted as new here. Their combination alone does not determine the five-vertex cross-petal optimum \(\sqrt{3/2}\), which requires the five-dimensional commutator calculation above. Swartz [3] investigates graph edge deletion and weighted four-cycles, not this complete friendship-graph pair-distance formula. The claimed increment is the sharp cross-petal value and, consequently, the complete metric for the natural family.

## Limitations

The result requires unit adjacency weights and the adjacency-matrix Dirac convention. No formula for nonuniform petal weights, arbitrary graph cacti or other spectral triples follows. The prior-art comparison is based on inspected primary texts and search results rather than an exhaustive mathematical bibliography. Independent mathematical assessment has not been performed.

## References

[1] P. Clare, C.-K. Li, E. Poon and E. Swartz, *Noncommutative Distances on Graphs: An Explicit Approach via Birkhoff-James Orthogonality*, arXiv:2409.04146v1, first posted 2024-09-06; https://arxiv.org/pdf/2409.04146.

[2] F. Besnard, *Estimating noncommutative distances on graphs*, arXiv:2105.09056v1, first posted 2021-05-19; https://arxiv.org/pdf/2105.09056.

[3] E. Swartz, *The effect of edge deletion on noncommutative distances on graphs*, arXiv:2610.07718, 2026; https://arxiv.org/abs/2610.07718.
