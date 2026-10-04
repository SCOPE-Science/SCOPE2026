# Exact Chen–Liu–Li \(G_L\) constant of the regular octagonal plane
## Finding
Let \(X_8=(\mathbb R^2,N)\), where
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the Chen–Liu–Li geometric constant
\[
G_L(X)=\sup\left\{\|x+y\|^2+\|2x-y\|^2:\ \|x\|=\|y\|=\|x-y\|=1\right\},
\]
one has
\[
G_L(X_8)=18-8\sqrt2=6.686291501015239\ldots .
\]
The maximum is attained, for example, at
\[
x=(1,\sqrt2-1),\qquad y=(3-2\sqrt2,1),
\]
for which
\[
N(x+y)=N(2x-y)=2\sqrt2-1.
\]

## Assumptions and scope
The space is real and two-dimensional. The displayed norm is the Minkowski functional of a regular octagon with facets having support functionals
\[
\pm s,\quad \pm t,\quad \frac{\pm s\pm t}{\sqrt2}.
\]
The claim concerns exactly the definition of \(G_L\) above: the supremum ranges over all ordered pairs \((x,y)\) satisfying all three unit-sphere constraints. No smoothness or strict-convexity assumption is imposed.

## Proof
The dihedral isometry group of the regular octagon is transitive on its eight facets. Every unit vector lies on at least one facet, so after an isometry one may write
\[
x=(1,u),\qquad 1-\sqrt2\le u\le\sqrt2-1.
\]
Write the eight support functionals as \(f_0,\ldots,f_7\). For every feasible pair, choose an active functional \(f_i\) for \(y\) and an active functional \(f_j\) for \(x-y\). If their supporting lines are not parallel, the equations
\[
f_i(y)=1,\qquad f_j(x-y)=1
\]
solve \(y\) as an affine function of \(u\). Imposing all inequalities \(f_k(y)\le1\), \(f_k(x-y)\le1\), together with the facet range for \(x\), leaves exactly six distinct affine feasible branches:
\[
\begin{aligned}
y&=(2-\sqrt2-u,1),&&3-2\sqrt2\le u\le\sqrt2-1,\\
y&=(2-\sqrt2+u,-1),&&1-\sqrt2\le u\le2\sqrt2-3,\\
y&=(\sqrt2-1-u,1+u),&&1-\sqrt2\le u\le2\sqrt2-3,\\
y&=((1-u)/2,\sqrt2-(1-u)/2),&&2\sqrt2-3\le u\le3-2\sqrt2,\\
y&=(\sqrt2-1+u,u-1),&&3-2\sqrt2\le u\le\sqrt2-1,\\
y&=((1+u)/2,(1+u)/2-\sqrt2),&&2\sqrt2-3\le u\le3-2\sqrt2.
\end{aligned}
\]
Parallel active lines add no missing feasible family. Equal-oriented supports would force a support value \(2\) at the unit vector \(x\). Opposite horizontal supports cannot vanish at \(x\); opposite diagonal supports would force \(|u|=1\), outside the facet interval. Opposite vertical supports force \(u=0\), but then the unit constraints imply simultaneously a free coordinate at most \(\sqrt2-1\) and at least \(2-\sqrt2\), which is impossible because \(\sqrt2-1<2-\sqrt2\).

On any of the six branches, each of \(N(x+y)\) and \(N(2x-y)\) is the maximum of eight affine functions of \(u\). Subdivide a branch at all support-switch points. On every resulting subinterval the objective
\[
N(x+y)^2+N(2x-y)^2
\]
is a sum of squares of two affine functions, hence a convex quadratic. Its maximum on that subinterval is therefore attained at an endpoint. Exact evaluation over all branch endpoints and support-switch points gives the global upper bound
\[
N(x+y)^2+N(2x-y)^2\le18-8\sqrt2.
\]
For the displayed pair \(x=(1,\sqrt2-1)\), \(y=(3-2\sqrt2,1)\), direct substitution gives
\[
N(x)=N(y)=N(x-y)=1,
\]
and
\[
N(x+y)=N(2x-y)=2\sqrt2-1.
\]
Thus the objective equals
\[
2(2\sqrt2-1)^2=18-8\sqrt2,
\]
so the upper bound is sharp.

## Verification
The accompanying exact checker `artifacts/verify_gl_octagon.py` uses only the Python standard library and arithmetic in \(\mathbb Q(\sqrt2)\). It reconstructs the support-functional decomposition from the 64 active-facet pairs, rules out the parallel degeneracies, deduplicates the six feasible affine branches, subdivides them at every support switch, verifies convexity of every resulting quadratic cell, and checks the explicit maximizing pair. A successful run prints `VERIFY_OK`; the captured output is in `artifacts/verification_output.txt`.

## Relationship to prior work
Chen, Liu and Li introduced \(G_L\) for equilateral pairs and proved the universal estimate \(9/2\le G_L(X)\le8\). Their examples give \(G_L(\ell_\infty)=8\), upper bounds for \(\ell_p\), and the Hilbert-space value \(6\), but do not compute the regular-octagonal plane.

The regular octagon is also a canonical example in the literature on perimeters of equilateral triangles in normed planes. Those perimeter parameters optimize a different functional on a different formulation of inscribed triangles and do not determine the sum-of-squares objective defining \(G_L\). In particular, knowing a common side length or perimeter does not fix either \(N(x+y)\) or \(N(2x-y)\).

A related exact computation for the product-type quantity \(\sqrt{N(x+y)N(2x-y)}\) on the same octagonal plane does not imply the present result: an upper bound on a product does not provide the sharp upper bound for the corresponding sum of squares. The present proof separately optimizes the \(G_L\) objective over the entire equilateral-pair set.

## Limitations
The proof is specific to the regular-octagonal norm and does not give a formula for regular \(2m\)-gons in general. The literature and database comparisons support originality to the best of the searches recorded in the accompanying review, but they cannot exclude unindexed or inaccessible prior work. No independent audit has been performed.

## References
1. B. Chen, Q. Liu and Y. Li, *Inscribed triangles in the unit sphere and a new class of geometric constants*, arXiv:2112.05922, first posted 11 December 2021; journal version: *Symmetry* 14 (2022), 72, https://doi.org/10.3390/sym14010072.
2. J. Alonso, P. Martín and P. L. Papini, *Perimeter of Triangles Inscribed in the Unit Ball of Normed Planes*, *Mediterranean Journal of Mathematics* 22 (2025), 46, https://doi.org/10.1007/s00009-025-02805-6.
