# Simple roots control the minimum sphere of transitive-tournament directed edge polytopes
## Finding
Let
\[
n\ge3,
\]
and let \(T_n\) be the transitive tournament on \([n]\), with arrows
\[
i\longrightarrow j
\quad\Longleftrightarrow\quad
i<j.
\]
Its directed edge polytope is
\[
P_n
=
\operatorname{conv}
\left\{
e_i-e_j:
1\le i<j\le n
\right\}
\subset\mathbb R^n.
\tag{1}
\]

Put
\[
S_n
=
\sum_{k=1}^{n-1}k(n-k)
=
\frac{n(n^2-1)}6.
\tag{2}
\]
Then the unique minimum enclosing Euclidean ball of \(P_n\) has center
\[
\boxed{
c_n
=
\frac1{S_n}
\sum_{k=1}^n
(n+1-2k)e_k
}
\tag{3}
\]
and squared radius
\[
\boxed{
R_n^2
=
2-\frac2{S_n}
=
2-\frac{12}{n(n^2-1)}.
}
\tag{4}
\]

There is a complete radial-shell refinement. If
\[
d=j-i,
\qquad
1\le d\le n-1,
\]
then
\[
\boxed{
\|e_i-e_j-c_n\|^2
=
2-\frac{4d-2}{S_n}.
}
\tag{5}
\]
Thus the \(n(n-1)/2\) vertices split into exactly \(n-1\) strict shells, and the shell indexed by \(d\) has multiplicity
\[
n-d.
\tag{6}
\]

The outer shell is \(d=1\). Therefore the contact set of the minimum sphere is exactly
\[
\boxed{
\left\{
e_i-e_{i+1}:
1\le i<n
\right\},
}
\tag{7}
\]
the simple roots of type \(A_{n-1}\).

Moreover,
\[
\boxed{
c_n
=
\sum_{i=1}^{n-1}
\frac{i(n-i)}{S_n}
(e_i-e_{i+1}).
}
\tag{8}
\]
The coefficients in (8) are positive and sum to \(1\). Hence the center lies in the relative interior of the contact simplex.

The metric conclusion is sparse: the full transitive tournament has
\[
\frac{n(n-1)}2
\]
directed-edge vertices, but only the \(n-1\) Hamilton-path edges
\[
1\to2\to\cdots\to n
\]
control its minimum enclosing sphere.

## Assumptions and scope
The realization is the standard directed-edge realization in the orthonormal basis of \(\mathbb R^n\).

The primary source defines the directed edge polytope of a quiver \(Q\) as
\[
\operatorname{DE}(Q)
=
\operatorname{conv}
\{e_v-e_w:v\to w\},
\]
and proves that every arrow vector is a vertex. For \(T_n\), this is exactly (1).

Every vertex lies in the zero-sum hyperplane
\[
H_0
=
\left\{
x\in\mathbb R^n:
\sum_{k=1}^n x_k=0
\right\}.
\]
The center (3) also lies in \(H_0\). Distances are ordinary Euclidean distances in the standard realization.

For \(n\ge3\), the transitive tournament has no rank function with unit increment on every arrow: the arrows
\[
1\to2,\qquad2\to3,\qquad1\to3
\]
would require simultaneous rank differences \(1,1,1\), which is impossible. Thus sphere formulas requiring such a rank function do not apply to this family.

## Proof
For
\[
1\le i<n,
\]
write
\[
\alpha_i=e_i-e_{i+1}.
\tag{9}
\]
Define
\[
\lambda_i
=
\frac{i(n-i)}{S_n}.
\tag{10}
\]
By (2),
\[
\sum_{i=1}^{n-1}\lambda_i=1.
\tag{11}
\]
All \(\lambda_i\) are strictly positive.

Now expand
\[
\sum_{i=1}^{n-1}\lambda_i\alpha_i.
\]
With the endpoint conventions
\[
\lambda_0=\lambda_n=0,
\]
the coefficient of \(e_k\) is
\[
\lambda_k-\lambda_{k-1}.
\]
A direct calculation gives
\[
\lambda_k-\lambda_{k-1}
=
\frac{k(n-k)-(k-1)(n-k+1)}{S_n}
=
\frac{n+1-2k}{S_n}.
\tag{12}
\]
Hence
\[
c_n
=
\sum_{i=1}^{n-1}\lambda_i\alpha_i,
\]
proving (8).

Next,
\[
\sum_{k=1}^n(n+1-2k)^2
=
\frac{n(n^2-1)}3
=
2S_n.
\tag{13}
\]
Therefore
\[
\|c_n\|^2
=
\frac2{S_n}.
\tag{14}
\]

Take any vertex
\[
v_{ij}=e_i-e_j,
\qquad
i<j,
\]
and set
\[
d=j-i.
\]
From (3),
\[
\langle c_n,v_{ij}\rangle
=
(c_n)_i-(c_n)_j
=
\frac{2d}{S_n}.
\tag{15}
\]
Since
\[
\|v_{ij}\|^2=2,
\]
equations (14)--(15) give
\[
\begin{aligned}
\|v_{ij}-c_n\|^2
&=
\|v_{ij}\|^2
+
\|c_n\|^2
-
2\langle c_n,v_{ij}\rangle\\
&=
2+\frac2{S_n}-\frac{4d}{S_n}\\
&=
2-\frac{4d-2}{S_n}.
\end{aligned}
\]
This proves (5).

The right side is strictly decreasing in \(d\). There are exactly
\[
n-d
\]
pairs \(i<j\) with \(j-i=d\), proving (6). The maximum occurs exactly when
\[
d=1,
\]
so every vertex lies in the ball centered at \(c_n\) with squared radius
\[
R_n^2
=
2-\frac2{S_n},
\]
and the only boundary vertices are the simple roots \(\alpha_i\).

It remains to prove that this containing ball is globally minimal and that its center is unique.

The contact representation (8) gives
\[
c_n
=
\sum_{i=1}^{n-1}\lambda_i\alpha_i,
\qquad
\lambda_i>0,
\qquad
\sum_i\lambda_i=1.
\tag{16}
\]
All contact vertices satisfy
\[
\|\alpha_i-c_n\|^2=R_n^2.
\tag{17}
\]
For any proposed center \(y\in\mathbb R^n\),
\[
\begin{aligned}
\sum_{i=1}^{n-1}
\lambda_i
\|\alpha_i-y\|^2
&=
\sum_i\lambda_i
\|\alpha_i-c_n+c_n-y\|^2\\
&=
R_n^2
+
\|y-c_n\|^2,
\end{aligned}
\tag{18}
\]
because
\[
\sum_i\lambda_i(\alpha_i-c_n)=0.
\]
Hence at least one contact vertex satisfies
\[
\|\alpha_i-y\|^2
\ge
R_n^2+\|y-c_n\|^2.
\]
No ball centered away from \(c_n\) can have radius at most \(R_n\), and every ball containing \(P_n\) must contain the contact vertices. Thus (3)--(4) give the unique minimum enclosing ball.

## Verification
The proof is symbolic for every \(n\ge3\).

The source-dependent facts were checked in the primary full text: the definition of a directed edge polytope, the statement that every arrow vector is a vertex, and the standard coordinate realization. The public record verifies the first public date and primary MSC classification.

A same-object type-\(A\) positive-root paper was also inspected because the transitive tournament gives the complete positive-root set. Its program concerns triangulations, Kostant chambers, resonance arrangements, and threshold functions; targeted full-text searches found no circumradius, minimum-enclosing-ball, or Euclidean-radius statement.

The accompanying `verify.py` checks the shell identity, contact barycentric coefficients, and radius formula with exact rational arithmetic for
\[
3\le n\le100.
\]
For
\[
3\le n\le9,
\]
it also independently solves the full ambient minimum-enclosing-ball epigraph problem over all \(n(n-1)/2\) vertices and compares the numerical optimum with (3)--(4). The finite replay is corroborative only.

## Relationship to prior work
Numata, Takahashi, and Tamaki develop the dimension and face theory of directed edge polytopes. Their paper gives the exact vertex realization used here but does not state a Euclidean circumradius or minimum-enclosing-sphere theorem.

Gutekunst, Mészáros, and Petersen study the complete type-\(A\) positive-root configuration through root cones, triangulations, the resonance arrangement, and Kostant chambers. Their full text likewise contains no Euclidean radius computation.

Known sphere formulas for ranked or semi-balanced directed-edge configurations require a layer function increasing by one on every arrow. The transitive tournament fails that hypothesis as soon as \(n\ge3\), because its directed triangles contain shortcut edges.

The new phenomenon is that the complete positive-root vertex set has a unique minimum sphere supported only by the simple-root chain. The exact radial shell of a vertex depends only on the interval length
\[
j-i.
\]

## Limitations
The theorem concerns the transitive tournament and its standard incidence-vector realization.

It does not give the minimum enclosing sphere of an arbitrary tournament or arbitrary acyclic quiver. In those families the contact set need not be a Hamilton path and radial distances need not depend on one gap parameter.

The formula is Euclidean-realization-specific; a nonorthogonal affine image need not preserve it.

A broader theorem for ordered root configurations might subsume the transitive-tournament calculation under different terminology. No such covering metric statement was located in the targeted comparisons.

## References
1. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521, first public version 2022-03-28; *Australasian Journal of Combinatorics* 88(1) (2024), 77--96.
2. Samuel C. Gutekunst, Karola Mészáros, and T. Kyle Petersen, *Root Cones and the Resonance Arrangement*, arXiv:1903.06595, first public version 2019-03-15; *Electronic Journal of Combinatorics* 28(1) (2021), P1.12, DOI 10.37236/8759.
