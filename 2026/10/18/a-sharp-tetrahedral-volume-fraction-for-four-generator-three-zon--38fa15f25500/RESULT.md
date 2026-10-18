# A sharp tetrahedral-volume fraction for four-generator three-zonotopes

## Finding

Let \(u_1,u_2,u_3,u_4\in\mathbb R^3\) span \(\mathbb R^3\), with zero vectors and dependent triples permitted. Put
\[
Z=\sum_{i=1}^4[-u_i,u_i],\qquad
\delta_i=\left|\det(u_1,\ldots,\widehat{u_i},\ldots,u_4)\right|,
\qquad S=\sum_{i=1}^4\delta_i,\qquad m=\max_i\delta_i.
\]
Here the hat means omitting that vector, and \(S>0\). Let \(M(Z)\) be the greatest Euclidean volume of any tetrahedron contained in \(Z\), including tetrahedra with vertices anywhere in its boundary or interior. Then
\[
\boxed{\quad\frac{M(Z)}{\operatorname{vol}_3(Z)}
\ \ge\ \frac{S+m}{6S}\ =\ \frac16+\frac{m}{6S}\ \ge\ \frac5{24}.\quad}
\]
The universal constant \(5/24\) is attained **if and only if** the four absolute triple determinants are equal (necessarily positive). Equivalently, equality holds precisely for invertible affine images of the regular rhombic dodecahedron
\[
P=\operatorname{conv}\left(\{(\pm1,\pm1,\pm1)\}\cup\{\pm2e_1,\pm2e_2,\pm2e_3\}\right).
\]
For this model \(\operatorname{vol}_3(P)=16\) and \(M(P)=10/3\). Its **only eight maximizing tetrahedra** are
\[
T_\varepsilon=\operatorname{conv}\{\varepsilon,
-2\varepsilon_1e_1,-2\varepsilon_2e_2,-2\varepsilon_3e_3\},
\quad\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{-1,1\}^3.
\]
All maximizers have their vertices among the fourteen polytope vertices. The formula for the eight maximizers transports by every invertible affine equivalence.

A quantitative determinant-imbalance consequence accompanies the bound. If \(\eta\ge0\) and \(M(Z)/\operatorname{vol}_3(Z)\le5/24+\eta\), then for each \(i\),
\[
\frac14-18\eta\ \le\ \frac{\delta_i}{S}\ \le\ \frac14+6\eta.
\]
Thus a near-minimal tetrahedral fraction forces the four normalized generator minors to be nearly balanced.

## Assumptions and scope

Four generating segments are counted with multiplicity. A segment may degenerate, and some triples of generators may be dependent; the only required nondegeneracy is \(\operatorname{span}\{u_i\}=\mathbb R^3\). The result is invariant under independent sign changes of generators and arbitrary invertible affine transformations of the body. It concerns the **largest contained tetrahedron** (not the largest tetrahedron whose vertices have a prescribed shape, not a regular-tetrahedron packing, and not the inradius or a surface-area extremum).

## Proof

### 1. A uniform explicit tetrahedron

Choose a triple achieving \(m>0\), relabel it \(u_1,u_2,u_3\), and apply an invertible linear map. Independent sign changes of generators, which do not change \(Z\), permit the normalization
\[
u_1=e_1,\qquad u_2=e_2,\qquad u_3=e_3,\qquad
u_4=(a,b,c),\qquad 0\le a,b,c\le1.
\]
The final inequalities follow because replacing any one basis generator with \(u_4\) produces a triple whose determinant is at most the chosen largest one in absolute value. In the normalized coordinates,
\[
(\delta_1,\delta_2,\delta_3,\delta_4)=(a,b,c,1),
\qquad S=1+a+b+c.
\]
The zonotope-volume determinant formula gives
\[
\operatorname{vol}_3(Z)=8\sum_{1\le i<j<k\le4}|\det(u_i,u_j,u_k)|
=8(1+a+b+c).
\]
This is also obtained by partitioning a three-dimensional Minkowski sum of segments into parallelotopes; the volume identity itself is classical.

Consider the four points of \(Z\) with generator signs
\[
\begin{aligned}
 p_0&=-u_1-u_2-u_3-u_4,\\
 p_1&=-u_1+u_2+u_3+u_4,\\
 p_2&= u_1-u_2+u_3+u_4,\\
 p_3&= u_1+u_2-u_3+u_4.
\end{aligned}
\]
Their edge matrix is
\[
[p_1-p_0,p_2-p_0,p_3-p_0]
=2\begin{pmatrix}
a&1+a&1+a\\
1+b&b&1+b\\
1+c&1+c&c
\end{pmatrix}.
\]
Expansion yields
\[
\left|\det(p_1-p_0,p_2-p_0,p_3-p_0)\right|
=8(2+a+b+c).
\]
The displayed points therefore form a tetrahedron of volume \(\frac43(2+a+b+c)\), with normalized volume
\[
\frac{2+a+b+c}{6(1+a+b+c)}=\frac{S+1}{6S}.
\]
Undoing the affine normalization restores the largest minor \(m\) and gives the bound \((S+m)/(6S)\). Since \(m\ge S/4\), the universal \(5/24\) bound follows. Equality in that lower estimate requires \(m=S/4\), which is equivalent to all four minors being positive and equal.

### 2. The balanced generator relation and the rhombic dodecahedron

When all four minors are equal, the normalization above has \(a=b=c=1\). Reversing the sign of its fourth generator gives the unique linear dependence \(u_1+u_2+u_3+u_4=0\), with its four coefficients all of unit magnitude. Every such spanning four-vector system is related by an invertible linear transformation to
\[
q_1=\tfrac12(1,1,1),\quad
q_2=\tfrac12(1,-1,-1),\quad
q_3=\tfrac12(-1,1,-1),\quad
q_4=\tfrac12(-1,-1,1).
\]
The zonotope \(\sum_i[-q_i,q_i]\) has precisely fourteen vertices: the six points \(\pm2e_i\) and the eight sign corners of the unit cube. Thus it equals \(P\) above. In the other direction any affine image of \(P\) has a four-generator presentation with equal positive absolute triple determinants. Consequently the equality classification in terms of minors is exactly the asserted affine-body classification, once sharpness for \(P\) is verified.

The volume \(\operatorname{vol}_3(P)=16\) follows without approximation: start with the cube \([-1,1]^3\) of volume \(8\) and attach six congruent pyramids of base area \(4\) and perpendicular height \(1\); their interiors are pairwise disjoint, so the additional volume is \(6\cdot4/3=8\).

### 3. Complete finite upper bound and equality sets

For an arbitrary tetrahedron \(\operatorname{conv}\{x_0,x_1,x_2,x_3\}\subseteq P\), the oriented determinant \(\det(x_1-x_0,x_2-x_0,x_3-x_0)\) is separately affine in each point. Every point is a convex combination of polytope vertices. Consequently the absolute determinant is bounded by its largest value on four vertices of \(P\). This reduction is analytic and does not assume the unknown optimizer is vertex-supported.

An exact integer enumeration of the \(\binom{14}{4}=1001\) unordered four-vertex subsets gives the complete histogram below. The first column \(k\) is the number of axial vertices \(\pm2e_i\) used; all entries count subsets having the indicated absolute determinant.

| \(k\) | \(0\) | \(4\) | \(8\) | \(12\) | \(16\) | \(20\) | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | 0 | 56 | 0 | 2 | 0 | 70 |
| 1 | 48 | 144 | 96 | 48 | 0 | 0 | 336 |
| 2 | 72 | 144 | 144 | 48 | 12 | 0 | 420 |
| 3 | 0 | 32 | 96 | 24 | 0 | 8 | 160 |
| 4 | 3 | 0 | 0 | 0 | 12 | 0 | 15 |
| **All** | **135** | **320** | **392** | **120** | **26** | **8** | **1001** |

The table has a short independently executable exact-integer proof in `verify.py`: it constructs the fourteen vertices explicitly, iterates over all 1001 subsets, evaluates each \(3\times3\) edge determinant by two different formulas, checks every histogram cell and verifies that the eight determinant-20 subsets are precisely the \(T_\varepsilon\) above. There is no numerical tolerance or sampling in this finite classification. Hence the maximum determinant is \(20\), the maximum contained tetrahedron volume is \(20/6=10/3\), and the maximum volume fraction is \((10/3)/16=5/24\).

The same exact check shows that any two *different* determinant-20 vertex tetrahedra have at most two vertices in common. This excludes unlisted nonvertex maximizers. Indeed, if a tetrahedron with one nonvertex corner had determinant of absolute value \(20\), express each corner as a convex combination of polytope vertices. Separate affinity writes its oriented determinant as a convex average of the corresponding oriented vertex determinants, all between \(-20\) and \(20\). Equality at an endpoint forces every positively weighted vertex choice to have that same endpoint determinant. A nonvertex corner has a representation supported on at least two distinct vertices. Keeping three positively weighted vertex choices for the other corners fixed would then produce two different maximizing vertex tetrahedra sharing those three vertices, contradicting the checked intersection property. Thus every maximizing corner is a polytope vertex and the eight configurations listed are exhaustive.

### 4. Quantitative imbalance

Set \(p_i=\delta_i/S\), so \(\sum_i p_i=1\) and \(\max_i p_i=m/S\). The first bound proved above reads \(M(Z)/\operatorname{vol}_3(Z)\ge(1+\max_i p_i)/6\). If the left side is at most \(5/24+\eta\), then \(\max_i p_i\le1/4+6\eta\). Since \(p_i=1-\sum_{j\ne i}p_j\), every \(p_i\ge1-3(1/4+6\eta)=1/4-18\eta\). This proves the stated two-sided control.

## Verification

Run `python3 verify.py` with Python's standard library from the same directory as this document. It performs exactly 1001 vertex-subset determinant checks with two independent determinant expressions; verifies all 30 histogram cells, the eight maximizing geometric vertex sets, their pairwise intersection bound, the exact volume fraction, and 64 supplemental rational parameter checks for the displayed universal witness formula. The certificate returned `VERIFY_OK vertex_sets=1001 max_determinant=20 maximizing_sets=8 max_intersection=2 parameter_samples=64`.

The universal inequality for **all real generating vectors** comes from the explicit determinant calculation and the zonotope-volume identity in Step 1, not from the 64 samples. The exhaustive finite check is complete only for the fourteen-vertex equality model; Step 2 and affine invariance transport that completed classification to every equality case. 

## Relationship to prior work

Di Summa, Eisenbrand, Faenza and Moldenhauer investigate the general maximum-volume-simplex/subdeterminant problem and its computational difficulty; their results do not state a sharp, affine-invariant tetrahedral-volume fraction for the four-generator zonotope family. Akopyan and Glazyrin study maximum-volume simplices, centrally symmetric containment, and parallelotopes, but their inspected statements do not give this four-generator sharp fraction or complete equality classification. Joós and Lángi examine zonotopes generated by their ambient dimension plus one segment, including rhombic dodecahedra; their relevant extremal theorems concern intrinsic volumes, circumradius and mean width, rather than the normalized volume of a largest contained tetrahedron. Their Corollary 1 records the classical zonotope determinant-volume identity used in Step 1. The present result therefore addresses a different geometric functional on the same important family.

## Limitations

The theorem covers at most four generating segments in three dimensions; no extension to arbitrary zonohedra or higher-dimensional zonotopes is asserted. The imbalance bound is necessary for near equality, not a claimed optimal converse or a stability bound on Banach–Mazur distance. The determinant histogram is an exact proof for a finite specified vertex set, not a general infinite-case computation. Historical priority remains potentially incomplete: an older equivalent formula or affine classification may occur in classical polytope or zonotope literature under other terminology.

## References

1. M. Di Summa, F. Eisenbrand, Y. Faenza and C. Moldenhauer, *On largest volume simplices and sub-determinants*, arXiv:1406.3512 (first public version June 13, 2014), https://arxiv.org/abs/1406.3512.
2. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, preprint dated December 4, 2012; published in *Periodica Mathematica Hungarica* **69** (2014), 251–256, https://dcglab.uniyar.ac.ru/sites/default/files/papers/preprints/Akopyan_Glazyrin_Volumes.pdf.
3. A. Joós and Z. Lángi, *Isoperimetric Problems for Zonotopes*, arXiv:2206.03204 (2022), https://arxiv.org/abs/2206.03204.
