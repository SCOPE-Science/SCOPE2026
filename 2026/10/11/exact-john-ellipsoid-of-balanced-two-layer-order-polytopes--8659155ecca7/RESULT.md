# Exact John ellipsoid of balanced two-layer order polytopes

## Finding
For every integer \(k\geq 1\), let
\[
Q_k=\{(x,y)\in\mathbb R^k\times\mathbb R^k:0\leq x_i\leq y_j\leq1\text{ for all }1\leq i,j\leq k\}.
\]
This is the standard-Euclidean order polytope of the ordinal sum of two \(k\)-element antichains. Put
\[
q_k=\sqrt{2-1/k},\qquad a_k=\frac1{2+q_k},\qquad t_k=\frac{q_k}{2+q_k}=1-2a_k.
\]
Let \(A_k\) be the positive-definite operator acting by the following scalar eigenvalues on mutually orthogonal subspaces of \(\mathbb R^{2k}\):
\[
\begin{array}{c|c|c}
\text{subspace}&\text{squared semiaxis}&\text{multiplicity}\\\hline
\{(x,y):\sum_i x_i=\sum_j y_j=0\}&u_k=\dfrac{a_kt_k}{1+t_k}&2(k-1)\\
\operatorname{span}\{(\mathbf1_k,\mathbf1_k)\}&w_k=\dfrac{a_k}{2}&1\\
\operatorname{span}\{(\mathbf1_k,-\mathbf1_k)\}&z_k=\dfrac{a_kt_k}{2}&1
\end{array}
\]
(the first subspace is zero-dimensional when \(k=1\)). Then the **unique maximum-volume Euclidean ellipsoid contained in** \(Q_k\) is
\[
E_k=\left\{v:(v-c_k)^\mathsf T A_k^{-1}(v-c_k)\leq1\right\},\qquad
c_k=(a_k\mathbf1_k,(1-a_k)\mathbf1_k).
\]
Its exact \(2k\)-dimensional volume, with \(\kappa_{2k}\) denoting unit-ball volume, is
\[
\operatorname{vol}_{2k}(E_k)
=\kappa_{2k}\,\frac{a_k\sqrt{t_k}}2\left(\frac{a_kt_k}{1+t_k}\right)^{k-1}.
\]
**Every one of the \(k^2+2k\) facets** of \(Q_k\) touches \(E_k\) at a distinct point, in that facet's relative interior. The contact-value parameter \(t_k\) is equivalently the unique root in \((0,1)\) of
\[
(2k+1)t^2+(4k-2)t-(2k-1)=0,
\]
and \(t_k\to\sqrt2-1\) as \(k\to\infty\).

## Assumptions and scope
The metric is the ordinary Euclidean metric on all \(2k\) coordinates, not the intrinsic metric of a different affine realization. The inequalities \(x_i\ge0\), \(y_j\le1\), and \(x_i-y_j\le0\) are precisely the irredundant facets; their number is \(2k+k^2\). The polytope is full-dimensional, since \(x_i=1/4\), \(y_j=3/4\) is strictly feasible. The maximum-volume inscribed ellipsoid is called the John ellipsoid; it is not the circumscribed Löwner ellipsoid.

## Proof
**1. Algebraic parameter and shape.** Write \(a=a_k\), \(t=t_k\), \(u=u_k\), \(w=w_k\), \(z=z_k\). By definition \(2a+t=1\) and
\[
t^2=a^2(2-1/k).
\]
The latter identity is equivalent, after eliminating \(a=(1-t)/2\), to the displayed quadratic, which has one positive root in \((0,1)\). In the decomposition into the two transverse blocks and the symmetric and antisymmetric all-ones directions, inversion of the four scalar actions gives
\[
A_k^{-1}=\left(\frac2a+\frac2t\right)I_{2k}-\frac2{kt}
\begin{pmatrix}0&J_k\\J_k&0\end{pmatrix},
\]
where \(J_k\) is the \(k\)-by-\(k\) all-ones matrix. This also shows \(A_k\succ0\), since all listed eigenvalues are positive.

**2. Exact facet contacts and containment.** For any coordinate unit vector \(e_i\) in the first block and \(f_j\) in the second block, the diagonal and cross-block entries of \(A_k\) are
\[
\alpha=\frac{(k-1)u+(w+z)/2}{k},\qquad
\gamma=\frac{w-z}{2k}.
\]
Substitution of \(2a+t=1\) and \(t^2=a^2(2-1/k)\) yields
\[
\alpha=a^2,\qquad \gamma=\frac{a^2}{2k},\qquad
(e_i-f_j)^\mathsf TA_k(e_i-f_j)=2(\alpha-\gamma)=t^2.
\]
The outward normals and slacks of all defining facets from \(c_k\) are
\[
\begin{array}{c|c|c}
\text{facet}&\text{outward normal}&\text{slack}\\\hline
x_i=0&-e_i&a\\
y_j=1&f_j&a\\
x_i=y_j&e_i-f_j&t
\end{array}.
\]
For an ellipsoid \(c+A^{1/2}B_2\), its maximum in the direction of a normal \(n\) is \(n\cdot c+\sqrt{n^\mathsf TA n}\). Here every square root equals the corresponding slack, so \(E_k\subseteq Q_k\) and **every defining facet touches** \(E_k\). The tangent points are \(c_k+A_kn/s\). The facet normals are pairwise nonproportional, and a smooth ellipsoid has only one supporting normal at each boundary point, so contact points are distinct and lie in the relative interiors of their facets.

**3. An exact John certificate.** Give each of the \(2k\) coordinate-facet contacts weight \(1-t=2a\), and each of the \(k^2\) cross-facet contacts weight \(2t/k\). All weights are positive. If \((n_\ell,s_\ell,\omega_\ell)\) runs over these facet normal, slack and weight triples, direct summation gives
\[
\sum_\ell\omega_\ell\frac{n_\ell}{s_\ell}=0,
\qquad
\sum_\ell\omega_\ell\frac{n_\ell n_\ell^\mathsf T}{s_\ell^2}
=\left(\frac2a+\frac2t\right)I_{2k}-\frac2{kt}
\begin{pmatrix}0&J_k\\J_k&0\end{pmatrix}=A_k^{-1}.
\]
The first cancellation uses \((1-t)/a=2\), with exactly \(k\) cross-facet terms of size \((2t/k)/t=2/k\) incident to each coordinate. For the second identity, coordinate facets contribute \(2I/a\), while cross-facet normals contribute \(2I/t\) and off-block entries \(-2/(kt)\). Defining unit-sphere contact vectors \(p_\ell=A_k^{1/2}n_\ell/s_\ell\), the two equalities become
\[
\sum_\ell\omega_\ell p_\ell=0,
\qquad \sum_\ell\omega_\ell p_\ell p_\ell^\mathsf T=I_{2k}.
\]
These are precisely the positive contact-decomposition conditions in John's characterization of the **unique** maximum-volume inscribed ellipsoid. Thus \(E_k\) is globally optimal, including against nonsymmetric and off-center competitors.

**4. Volume and limit.** Multiplying the \(2k\) eigenvalues gives \(\det A_k=u^{2k-2}wz\). Taking a square root yields the volume formula. Since \(\sqrt{2-1/k}\to\sqrt2\), the explicit formula for \(t_k\) gives the stated limiting value.

## Verification
The standalone file `verify_john_order.py` checks polynomial divisibility of both key facet quadratic identities by the defining polynomial in \(t\), then checks all facet contacts, weighted John-matrix identities, equilibrium, and eigenvalues numerically for each \(1\leq k\leq60\), totaling 77,470 facet instances. Run `python3 verify_john_order.py` with `sympy` and `numpy` installed. These finite numerical tests support but do not replace the universal proof, which consists of the exact identities and the John contact certificate above.

## Relationship to prior work
Mori's work on triangular faces of maximal-ranked-poset order and chain polytopes concerns the combinatorics of triangular two-faces, not Euclidean maximal-volume inscribed ellipsoids. Ahmad, Fourier, and Joswig treat the face structures and \(f\)-vectors of maximal ranked posets, including the family with layer vector \((k,k)\), but their formulas do not imply the Euclidean shape and weighted contact certificate above. Stanley's order-polytope construction and John's ellipsoid-contact characterization are prior foundations, not claimed as new. The present statement concerns the explicit metric optimum for one natural infinite family.

## Limitations
The theorem covers equally sized two-level antichains only; it does not provide an ellipsoid formula for unequal layer sizes, other ranked posets, chain polytopes, or affinely distorted embeddings. The limits of the supporting numerical tests are given under Verification. The geometric theorem makes no claim about unexamined affine models or distinct possible presentations in the literature.

## References
1. Aki Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset*, arXiv:2404.00263, first posted 2024-03-30, https://arxiv.org/html/2404.00263v3 .
2. Ibrahim Ahmad, Ghislain Fourier, and Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, https://arxiv.org/html/2309.01626v2 .
3. Richard P. Stanley, *Two Poset Polytopes*, Discrete & Computational Geometry 1 (1986), 9–23.
4. Fritz John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant* (1948), 187–204.
