# Sharp radial profile for the sum of vertex distances in a regular tetrahedron
## Finding
Let \(A_1A_2A_3A_4\) be a regular tetrahedron with circumcenter \(O\) and circumradius \(R>0\). For \(P\in\mathbb R^3\), define \(\rho=OP\) and \(S(P)=\sum_{i=1}^4 PA_i\). Then
\[
|R-\rho|+3\sqrt{R^2+\rho^2+\frac{2R\rho}{3}}\le S(P)\le R+\rho+3\sqrt{R^2+\rho^2-\frac{2R\rho}{3}}.
\]
For each fixed \(\rho>0\), the lower equality points are exactly the four points on the vertex rays, and the upper equality points are exactly the four points on the opposite rays, all at distance \(\rho\) from \(O\). At \(\rho=0\), both endpoints are \(4R\). Every intermediate value occurs.

## Assumptions and scope
The tetrahedron is Euclidean and regular. The point \(P\) is arbitrary in space, including outside the tetrahedron. Distances are ordinary nonnegative Euclidean distances. The result concerns the unweighted first power of the four vertex distances.

## Proof
Let \(v_1,\ldots,v_4\) be the unit vectors from \(O\) toward the vertices. Regularity gives
\[
\sum_i v_i=0,\qquad v_i\cdot v_j=-\frac13\ (i\ne j),\qquad \sum_i v_i v_i^{\mathsf T}=\frac43 I.
\]
For \(\rho>0\), set \(w=(P-O)/\rho\) and \(t_i=w\cdot v_i\). Then
\[
\sum_i t_i=0,\qquad \sum_i t_i^2=\frac43.
\]
Conversely, every real quadruple with these two constraints comes from a unique unit \(w\), namely
\[
w=\frac34\sum_i t_i v_i.
\]
Thus the direction space is exactly
\[
M=\left\{t\in\mathbb R^4:\sum_i t_i=0,\ \sum_i t_i^2=\frac43\right\}.
\]
Write \(x=\rho/R\) and \(f_x(t)=\sqrt{1+x^2-2xt}\). Then \(S(P)/R=F_x(t)=\sum_i f_x(t_i)\). For \(x>0\) and \(x\ne1\),
\[
f_x'(t)=-\frac{x}{\sqrt{1+x^2-2xt}},\quad f_x''(t)=-\frac{x^2}{(1+x^2-2xt)^{3/2}},\quad f_x'''(t)=-\frac{3x^3}{(1+x^2-2xt)^{5/2}}<0.
\]
At a constrained critical point, \(f_x'(t_i)=\lambda+2\mu t_i\). Since \(f_x'\) is strictly concave, a line can meet its graph in at most two points. Hence the four coordinates have at most two distinct values. Solving the two constraints gives, up to permutation, only
\[
(1,-\tfrac13,-\tfrac13,-\tfrac13),\quad (-1,\tfrac13,\tfrac13,\tfrac13),\quad (\tfrac1{\sqrt3},\tfrac1{\sqrt3},-\tfrac1{\sqrt3},-\tfrac1{\sqrt3}).
\]
If the two values are \(a>b\), then
\[
2\mu=\frac{f_x'(a)-f_x'(b)}{a-b},
\]
and strict concavity gives \(f_x''(a)<2\mu<f_x''(b)\). On the tangent space, this makes the first type a strict minimum, the second type a strict maximum, and the two-plus-two type a saddle. Compactness of \(M\) therefore makes the first two types the global minimum and maximum.

Substitution yields
\[
F_x^{\min}=|1-x|+3\sqrt{1+x^2+\frac{2x}{3}},\qquad
F_x^{\max}=1+x+3\sqrt{1+x^2-\frac{2x}{3}}.
\]
Multiplication by \(R\) gives the stated bounds and equality rays. At \(x=1\), the inequalities follow by continuity from \(x\ne1\). The only nonsmooth points are the vertex directions. The remaining saddle value is \(2\sqrt{2-2/\sqrt3}+2\sqrt{2+2/\sqrt3}\); after squaring, its strict comparison with \(2\sqrt6\) and \(2+2\sqrt3\) reduces respectively to \(2/3>1/4\) and \(8/3<3\). Thus equality does not enlarge. At \(x=0\), all four distances are \(R\). Finally, for \(\rho>0\) the direction sphere is connected, and the continuous image under \(S\) is the full interval between its minimum and maximum.

## Verification
The proof is analytic. The accompanying `verify.py` checks the tetrahedral frame identities, reconstruction of directions, the endpoint formulas on all eight extremal rays, and both inequalities on deterministic random directions for radii spanning several orders of magnitude. These finite computations are consistency checks only.

## Relationship to prior work
Problem 3 of the Eighth International Mathematical Olympiad states the classical unconstrained theorem that the circumcenter minimizes the sum of distances to the vertices of a regular tetrahedron. The present result fixes \(OP\) and determines both sharp directional extrema and the complete range on every centered sphere.

Meskhishvili's treatment of cyclic averages for Platonic solids gives the fixed-radius second- and fourth-power identities for a regular tetrahedron and notes that other powers retain directional dependence. The inspected regular-tetrahedron section does not state this first-power fixed-radius extremal profile.

## Limitations
No claim is made for nonregular tetrahedra, weighted sums, or other distance powers. The inspected sources and searches do not prove absolute novelty; older geometry, geometric-median, or majorization literature may contain an equivalent shellwise statement under different terminology.

## References
1. Eighth International Mathematical Olympiad, 1966, Problem 3, official problem set: https://www.imo-official.com/assets/documents/problems/1966/1966_eng.pdf
2. The IMO Compendium Group, *The IMO Compendium*, reproduction of the 1966 contest problems.
3. Mamuka Meskhishvili, “Cyclic Averages of Regular Polygons and Platonic Solids,” *Communications in Mathematics and Applications* 11 (2020), 335–355; arXiv:2010.12340; DOI: 10.26713/cma.v11i3.1420.
