# Exact generalized \(G_L\) profile of the regular octagonal Banach plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For every real \(p\in[1,\infty)\), define
\[
G_L(X_8,p)=\sup\left\{N(x+y)^p+N(2x-y)^p:N(x)=N(y)=N(x-y)=1\right\}.
\]
Then
\[
G_L(X_8,p)=2(2\sqrt2-1)^p.
\]
The stronger pointwise estimate behind the formula is that every admissible pair satisfies
\[
N(x+y)\le 2\sqrt2-1,\qquad N(2x-y)\le 2\sqrt2-1.
\]
Both inequalities are sharp simultaneously.

## Assumptions and scope
The space is the real two-dimensional normed space whose unit ball is the Euclidean regular octagon with vertices
\[
(1,\sqrt2-1),\ (\sqrt2-1,1),\ (1-\sqrt2,1),\ (-1,\sqrt2-1)
\]
and their negatives. The exponent satisfies \(1\le p<\infty\). No claim is made for \(p<1\), for complex scalars, or for other polygonal norms.

## Proof
Write the eight boundary edges of the unit ball as \(E_0,\ldots,E_7\). Any admissible pair \((x,y)\), with \(N(x)=N(y)=N(x-y)=1\), belongs to some triple
\[
x\in E_i,\qquad y\in E_j,\qquad x-y\in E_k.
\]
Parametrize the three edges affinely by parameters \(t,u,v\in[0,1]\). The vector equation \(x-y=(x-y)\) written with the three edge parametrizations is a two-equation affine system in \((t,u,v)\). For every nonempty edge triple its solution set is a closed interval. Exact elimination over \(\mathbb Q(\sqrt2)\) yields 48 feasible edge-family intervals.

On any one such interval, both vectors \(x+y\) and \(2x-y\) depend affinely on one parameter. The octagonal norm is the maximum of its eight supporting linear functionals, hence each function
\[
s\longmapsto N(x(s)+y(s)),\qquad s\longmapsto N(2x(s)-y(s))
\]
is convex and piecewise affine. Therefore the maximum of either function on a feasible interval occurs at an endpoint. The accompanying exact verifier additionally inserts every support-change point; across 128 checked endpoint/support breakpoints the only distinct ordered pairs of shifted norms are
\[
(3-\sqrt2,2\sqrt2-1),\quad
(1+1/\sqrt2,2\sqrt2-1),\quad
(2\sqrt2-1,3-\sqrt2),
\]
\[
(2\sqrt2-1,1+1/\sqrt2),\quad
(2\sqrt2-1,2\sqrt2-1).
\]
Thus each shifted norm is at most \(2\sqrt2-1\) for every admissible pair.

For sharpness, take
\[
x=(1,\sqrt2-1),\qquad y=(3-2\sqrt2,1).
\]
Direct substitution gives
\[
N(x)=N(y)=N(x-y)=1
\]
and
\[
N(x+y)=N(2x-y)=2\sqrt2-1.
\]
Since \(p\ge1\), raising the pointwise bounds to the power \(p\) and adding proves the upper bound \(2(2\sqrt2-1)^p\), while the displayed pair attains it.

## Verification
The standalone file `glp_octagon_verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\). It enumerates all ordered edge triples, solves their affine equilateral constraints exactly, intersects with the unit parameter cube, and checks the shifted norms at all interval endpoints and all support-change points. A successful replay prints `VERIFY_OK`, reports 48 feasible edge families, 128 support-breakpoint checks, five distinct shifted-norm pairs, and the exact maximum \(-1+2\sqrt2\) for each shifted norm. The analytic proof above explains why this finite polyhedral enumeration is exhaustive rather than experimental sampling.

## Relationship to prior work
Chen, Liu, and Li introduced \(G_L(X,p)\) for \(p\in[1,\infty)\) as a generalized form of their equilateral-triangle constant. Their paper gives general bounds and examples but does not evaluate this generalized profile on the regular octagonal plane. The previously available exact regular-octagon result for \(G_L(X)=G_L(X,2)\) covers only the single exponent \(p=2\). A separate exact regular-octagon result for the geometric-mean constant \(T_G\) controls the product \(N(x+y)N(2x-y)\). Neither statement implies the separate pointwise bounds proved here; those bounds are what force one common extremizer for every \(p\ge1\).

## Limitations
The result is specific to the regular octagonal norm and finite exponents \(p\ge1\). The proof uses the polyhedral edge structure essentially. The literature comparison is finite and cannot exclude an uncatalogued equivalent formulation, although the defining paper and the closest exact same-object records were compared at the statement-and-implication level.

## References
1. B. Chen, Q. Liu, Y. Li, “Inscribed Triangles in the Unit Sphere and a New Class of Geometric Constants,” arXiv:2112.05922, first public version 11 December 2021; later Symmetry 14 (2022), 72, DOI 10.3390/sym14010072.
2. Published exact regular-octagon record: “Exact Chen–Liu–Li \(G_L\) constant of the regular octagonal plane,” identifier `2026/10/4/SCOPE-exact-chen-liu-li-g-l-constant-of-the-regular-octagonal-plane--f0a5701db2b3`.
3. Published exact regular-octagon record: “Exact \(T_G\) constant of the regular octagonal Banach plane,” identifier `2026/10/4/SCOPE-exact-t-g-constant-of-the-regular-octagonal-banach-plane--3b6f71e2e4f4`.
