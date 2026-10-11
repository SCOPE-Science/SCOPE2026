# Tree Laplacian simplices exhibit sharp, lattice-invisible Euclidean inradius exponents
## Finding
Let \(T\) be any finite simple tree on \(n\ge2\) vertices, with graph Laplacian \(L=D-A\). Its **canonical Euclidean Laplacian simplex** is
\[
Q_T=\operatorname{conv}\{Le_1,\ldots,Le_n\}\subset H_n,
\qquad
H_n=\left\{x\in\mathbb R^n:\sum_{i=1}^n x_i=0\right\}.
\tag{1}
\]
The metric is the ordinary Euclidean metric on the ambient zero-sum hyperplane \(H_n\), not a metric transported by a lattice-coordinate change. Set
\[
v^{(i)}=L^\dagger e_i,
\qquad s_i=\|v^{(i)}\|_2,
\qquad S_T=\sum_{i=1}^n s_i.
\tag{2}
\]
The exact Euclidean inradius and the unique incenter are
\[
\boxed{\rho_T=\frac1{S_T}},
\qquad
\boxed{c_T=\frac1{S_T}\sum_{i=1}^n s_iLe_i}.
\tag{3}
\]
For **every** tree, the following bounds hold:
\[
\boxed{
\frac{6}{\sqrt n(n^2-1)}
\le\rho_T\le
\frac{4\sqrt2\,n}{(n+2)(n-1)}.
}
\tag{4}
\]
Both powers of \(n\) are optimal. Indeed, the star on \(n\) vertices satisfies
\[
\begin{aligned}
s_{\rm hub}^2&=\frac{n-1}{n^3},\\
s_{\rm leaf}^2&=\frac{n^3-n^2-n-1}{n^3},
\end{aligned}
\tag{5}
\]
and hence
\[
\boxed{
\rho_{K_{1,n-1}}
=\left[
\sqrt{\frac{n-1}{n^3}}
+(n-1)\sqrt{\frac{n^3-n^2-n-1}{n^3}}
\right]^{-1},
\qquad
\lim_{n\to\infty}n\rho_{K_{1,n-1}}=1.
}
\tag{6}
\]
For the path \(P_n\), number vertices consecutively and put
\[
z_i=i-\frac{n+1}{2}.
\]
Then
\[
\boxed{
\|L(P_n)^\dagger e_i\|_2^2
=\frac{n^4+10n^2-11+120(n^2+1)z_i^2-240z_i^4}{720n}.
}
\tag{7}
\]
Thus \(\rho_{P_n}\) is exactly the reciprocal of the sum of the square roots in (7), and
\[
\boxed{
\lim_{n\to\infty}n^{5/2}\rho_{P_n}=C_{\rm path},
}
\qquad
C_{\rm path}
=\left[\int_0^1
\sqrt{\frac{1+120(t-1/2)^2-240(t-1/2)^4}{720}}\,dt
\right]^{-1}
\approx10.1708468399938.
\tag{8}
\]
In particular,
\[
\boxed{
\frac{\rho_{K_{1,n-1}}}{\rho_{P_n}}
\sim\frac{n^{3/2}}{C_{\rm path}}.
}
\tag{9}
\]
This is a polynomially growing Euclidean distortion between tree Laplacian simplices that are nevertheless **all unimodularly equivalent** as lattice simplices.

## Assumptions and scope
The tree \(T\) is undirected, simple, connected, and unweighted; \(n\ge2\). The vertex labels only select coordinates and do not affect the value of the inradius. The Laplacian is the symmetric matrix \(L=D-A\), with rank \(n-1\), \(L\mathbf1=0\), and \(L^\dagger\) its Moore--Penrose pseudoinverse.

This canonical realization (1) uses the **full column vectors of \(L\)** in \(H_n\). The lattice-coordinate realization often used for Ehrhart theory is related by a generally nonorthogonal linear map. The distinction is essential because inradius is not preserved by arbitrary unimodular linear transformations.

Braun and Meyer introduced the Laplacian simplex and proved in Proposition 4.1 of their 2017 paper that every tree Laplacian simplex of a fixed order is unimodularly equivalent to the standard reflexive simplex. The new conclusions concern the Euclidean metric of (1), not the lattice-equivalence class.

## Proof
**Exact Euclidean facet geometry.** As \(T\) is connected,
\[
L^\dagger L=LL^\dagger=I-\frac1n\mathbf1\mathbf1^{\mathsf T}.
\tag{10}
\]
The \(n\) vertices \(Le_i\) affinely span \(H_n\). For \(x\in H_n\), set
\[
\lambda_i(x)=\frac1n+\langle L^\dagger e_i,x\rangle.
\tag{11}
\]
Equation (10) gives
\[
\lambda_i(Le_j)=\frac1n+\delta_{ij}-\frac1n=\delta_{ij},
\qquad\sum_i\lambda_i(x)=1.
\]
Consequently these are the affine barycentric coordinates of (1), and the facets are precisely \(\lambda_i(x)=0\). Each has an intrinsic unit normal parallel to \(v^{(i)}=L^\dagger e_i\), so its Euclidean clearance from an interior point \(x\) is \(\lambda_i(x)/s_i\).

If a Euclidean ball of radius \(\rho\) is inscribed at \(x\), then \(\lambda_i(x)\ge\rho s_i\) for every \(i\). Summing gives \(1\ge\rho S_T\). The point \(c_T\) in (3) has barycentric coordinates \(\lambda_i(c_T)=s_i/S_T\), so this bound is attained. Equality forces each of the \(n\) barycentric constraints to be equality. Because the barycentric map is injective, the incenter is unique. This proves (3).

**Uniform lower bound.** Let \(\mu_2,\ldots,\mu_n>0\) be the nonzero Laplacian eigenvalues. Cauchy--Schwarz and positivity give
\[
\begin{aligned}
S_T
&\le\sqrt{n\sum_i\|L^\dagger e_i\|^2}
=\sqrt{n\sum_{j=2}^n\mu_j^{-2}}\\
&\le\sqrt n\sum_{j=2}^n\mu_j^{-1}
=\sqrt n\,\operatorname{tr}(L^\dagger).
\end{aligned}
\tag{12}
\]
For a unit-edge tree, electrical effective resistance equals ordinary graph distance. The standard resistance identity therefore yields
\[
n\operatorname{tr}(L^\dagger)
=\sum_{u<v}d_T(u,v)=W(T),
\tag{13}
\]
where \(W(T)\) is the Wiener index.

For completeness, the elementary tree bound is
\[
W(T)\le\frac{n(n^2-1)}6.
\tag{14}
\]
To prove (14), delete a leaf \(\ell\) of an \(n\)-vertex tree. The distances from \(\ell\) to the \(n-1\) remaining vertices, written in nondecreasing order, have the \(j\)-th distance at most \(j\): until all vertices are reached, the unique geodesic to a furthest vertex supplies at least one vertex at each smaller distance. Hence their total is at most \(n(n-1)/2\). Starting with the single vertex and inducting gives
\[
W(T)\le\sum_{k=2}^n\frac{k(k-1)}2=\frac{n(n^2-1)}6.
\]
Combining (12)--(14),
\[
S_T\le\frac{(n^2-1)\sqrt n}{6},
\]
which gives the first inequality of (4).

**Uniform upper bound.** Write \(N_{\le2}\) for the number of vertices with degree at most two. The degree sum \(2n-2\) implies
\[
N_{\le2}\ge\frac{n+2}{2},
\tag{15}
\]
since every other vertex has degree at least three. Fix any such vertex \(i\). Some neighbor \(j\) lies across an edge whose component \(B\), not containing \(i\), has size
\[
b=|B|\ge\frac{n-1}2.
\tag{16}
\]
Indeed, removal of \(i\) yields at most two components whose total size is \(n-1\).

The vector \(v=v^{(i)}=L^\dagger e_i\) satisfies
\[
Lv=e_i-\frac1n\mathbf1.
\tag{17}
\]
Summing (17) over \(B\), the internal edge differences cancel and the only boundary edge is \(ij\). Thus
\[
v_j-v_i=-\frac bn,
\qquad
\|v\|\ge\frac{|v_i-v_j|}{\sqrt2}
\ge\frac{n-1}{2\sqrt2\,n}.
\tag{18}
\]
Summing (18) over at least \((n+2)/2\) vertices gives
\[
S_T\ge\frac{(n+2)(n-1)}{4\sqrt2\,n}.
\]
Taking reciprocals proves the second inequality of (4).

**Exact star profile.** For the hub source of \(K_{1,n-1}\), (17) and the zero-sum condition imply
\[
v_{\rm hub}=\frac{n-1}{n^2},
\qquad v_{\rm leaf}=-\frac1{n^2}
\]
for the corresponding column of \(L^\dagger\), yielding the first formula in (5). For a source at one leaf, its pseudoinverse column has values
\[
-\frac1{n^2}\text{ at the hub},
\qquad
\frac{n^2-n-1}{n^2}\text{ at the source leaf},
\qquad
-\frac{n+1}{n^2}\text{ at each other leaf}.
\tag{19}
\]
Squaring and summing gives the second formula in (5). Formula (6) and its \(n^{-1}\) asymptotic follow.

**Exact path profile.** For the path vertices ordered \(1,\ldots,n\), the \(i\)-th pseudoinverse column \(v^{(i)}\) satisfies
\[
v^{(i)}_{k+1}-v^{(i)}_k=\frac{k}{n}-\mathbf1_{\{i\le k\}}.
\tag{20}
\]
The unique zero-sum solution is
\[
\boxed{
v^{(i)}_k
=\frac{(n-i)(n-i+1)}{2n}
-\frac{n^2-1}{6n}
+\frac{k(k-1)}{2n}
-(k-i)_+,
}
\tag{21}
\]
where \((a)_+=\max\{a,0\}\). This can be checked directly in (17). Squaring (21), summing over \(1\le k\le n\), and using the standard sums of powers through degree four yields (7). This algebra is replayed in exact fractions by the standalone checker.

Put \(t_i=i/n\). The right side of (7), divided by \(n^3\), converges uniformly over \(1\le i\le n\) to
\[
f(t_i)=\frac{1+120(t_i-1/2)^2-240(t_i-1/2)^4}{720}.
\]
This polynomial is strictly positive on \([0,1]\), so taking square roots preserves uniform convergence. Therefore the finite sums in (3) are Riemann sums satisfying
\[
\frac{S_{P_n}}{n^{5/2}}
\longrightarrow\int_0^1\sqrt{f(t)}\,dt.
\]
This proves (8) and, together with (6), the comparison (9).

## Verification
The proof covers **all** finite simple trees of order \(n\ge2\). The attached standalone `verify.py` computes exact Moore--Penrose columns using rational inversion of \(L+\mathbf1\mathbf1^{\mathsf T}/n\), reconstructs the incenter from barycentric facet clearances, and checks both universal bounds on all labeled trees through order six and deterministic larger specimens. It independently checks the path expression (21), polynomial (7), star formula (19), the tree Wiener identity, and the two asymptotic limits. These finite checks supplement, but do not replace, the all-order proof.

## Relationship to prior work
Braun and Meyer's *Laplacian Simplices* introduces exactly the canonical convex hull of the graph-Laplacian columns. Proposition 4.1 proves that **all tree cases of a fixed order are unimodularly equivalent** as lattice simplices; the paper instead develops reflexivity, normalized volume, and Ehrhart invariants. Its path calculations concern lattice equivalence, not intrinsic Euclidean radius.

Meyer and Pllaha's *Laplacian Simplices II* studies the same objects through codes and Ehrhart theory. Neither inspected paper develops the all-tree Euclidean inradius bounds, incenter formula, or path/star exponent separation.

A different use of the graph Laplacian in Devriendt's work constructs an effective-resistance simplex through an inverse-Gram or pseudoinverse relationship. That realization is not the column-Laplacian simplex (1). Generic simplex facet-distance identities and extra-symmetry formulas do not themselves imply tree-uniform bounds or different asymptotic orders for paths and stars. Similarly, geometric radii of **Laplacian lattices under simplicial distance functions** are a different metric problem.

The main structural point is a failure of **lattice geometry to predict Euclidean shape**: the lattice types coincide for all trees, while their canonical embeddings admit polynomially diverging inradii. The universal bounds prove this scale discrepancy cannot grow with a larger exponent among trees.

## Limitations
No claim is made that paths minimize or stars maximize the inradius among all trees at every **fixed** \(n\); the proved result is the universal scale window with two extremal-order witnesses and exact formulas for those witnesses.

Changing the ambient Euclidean realization by a nonorthogonal lattice basis changes these radii. Weighted trees, general connected graphs, circumradii, and more refined exact extremal constants for arbitrary trees are not covered. The exact general inradius identity (3) follows from standard simplex geometry; the additional all-tree bounds and their sharp asymptotic separation are the substantive contribution.

## References
1. Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085v1, first public version 2017-06-21, especially Definition 3.3 and Proposition 4.1.
2. Marie Meyer and Tefjol Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960, 2018.
3. Karel Devriendt, *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*, arXiv:2010.04521, 2020.
4. Karel Devriendt and Piet Van Mieghem, *The Simplex Geometry of Graphs*, arXiv:1807.06475, 2018.
5. *The Laplacian lattice of a graph under a simplicial distance function*, *European Journal of Combinatorics* 34 (2013), 1051--1070, DOI 10.1016/j.ejc.2013.01.010 (different object and metric).
