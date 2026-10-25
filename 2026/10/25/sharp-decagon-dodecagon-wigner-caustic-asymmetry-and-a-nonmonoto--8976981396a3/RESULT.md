# Sharp decagon–dodecagon Wigner-caustic asymmetry and a nonmonotone extremal transition

## Finding

Let \(P\) be a strictly convex equiangular polygon with \(2n\) sides, where \(n=5\) or \(n=6\), whose opposite supporting-side distances are all equal (discrete constant width). Let \(W(P)\) be the closed polygonal Wigner caustic formed by the midpoints of its \(n\) opposite-vertex diagonals, and let \(A^*(W(P))\) denote its oriented shoelace area. Then the following sharp, unattained bounds hold:

\[
0\leq\frac{|A^*(W(P))|}{A(P)}<
\begin{cases}
(\sqrt5-2)/4,&2n=10,\\
(\sqrt3-1)/8,&2n=12.
\end{cases}
\]

Every limiting maximizer is classified by the finite signed-cyclic parameter orbits below: there are exactly twelve for ten sides and four for twelve sides, after fixing the positive scale, a rotation of the edge-direction frame and a translation. In the decagonal case **all** twelve vertices of the compact parameter polytope maximize the Wigner area; in the dodecagonal case **only four** of its twenty-eight vertices do. In particular, the optimal area ratio increases strictly from ten to twelve sides:
\[
(\sqrt5-2)/4 < (\sqrt3-1)/8.
\]

## Assumptions and scope

Fix an arbitrary scale \(s>0\) and rotate the polygon so that its successive unit edge directions are \(u_j=(\cos(j\pi/n),\sin(j\pi/n))\), \(j=0,\ldots,2n-1\). Its central symmetral is a regular \(2n\)-gon of side length \(s\). Write opposite edge lengths as
\[
\ell_j=s+d_j,\qquad \ell_{j+n}=s-d_j,\qquad j=0,\ldots,n-1.
\]
Closure is equivalent to \(\sum_{j=0}^{n-1}d_j u_j=0\). The polygon is strictly convex with exactly \(2n\) nonzero edges precisely when \(|d_j|<s\) for all \(j\). These hypotheses parametrize the entire indicated discrete constant-width equality family, not all convex \(2n\)-gons. Scale to \(s=1\) for the finite optimization, and denote by \(\mathcal D_n\) the compact polytope of parameter vectors with the same closure equations and \(|d_j|\leq1\). Boundary points describe possibly degenerate polygonal limits.

The signed cyclic shift \(T(d_0,\ldots,d_{n-1})=(-d_{n-1},d_0,\ldots,d_{n-2})\) has order \(2n\), preserves \(\mathcal D_n\), and corresponds to rotating the edge-direction indexing. The limiting maximizing vectors are exactly the orbits:

- For \(n=5\), the orbit of \((1,-1,1,-1,1)\), of length two, together with the orbit of \((-(\sqrt5-2),1,-(\sqrt5-2),-1,1)\), of length ten.
- For \(n=6\), the orbit of \((1,1,-1,-1,1,1)\), of length four.

Distinct listed vectors are distinct in the fixed edge-direction parameterization; no claim is made that all yield geometrically noncongruent limiting bodies.

## Proof

**Reduction to a finite quadratic program.** For \(j=0,\ldots,n-1\), write \(P_j\) for the successive vertices. The Wigner vertices \(W_j=(P_j+P_{j+n})/2\) satisfy \(W_{j+1}-W_j=d_j u_j\). Thus the signed area is
\[
A^*(W)=\frac12\sum_{0\leq i<j<n}d_id_j\sin((j-i)\pi/n),\qquad
F_n(d):=-A^*(W).
\]
The symmetral \(Q=(P+(-P))/2\) is the regular \(2n\)-gon with side length \(s\); hence
\[
A(Q)=\frac{n s^2}{2\tan(\pi/(2n))},\qquad
A(P)=A(Q)-2F_n(d).
\]
The second identity follows directly by expanding the shoelace sums with \(P_j=W_j+Q_j\), using \(W_{j+n}=W_j\) and \(Q_{j+n}=-Q_j\); opposite mixed terms cancel. The Brunn–Minkowski equality condition shows that \(A(Q)>A(P)\) unless \(P\) is centrally symmetric. Since any nonzero vector in the closure subspace can be scaled to a valid strict polygon, \(F_n\) is a **positive-definite quadratic form** on the \((n-2)\)-dimensional closure subspace. Thus it is strictly convex. Furthermore \(F_n(d)/(A(Q)-2F_n(d))\) is strictly increasing in \(F_n(d)\) wherever the polygon has positive area. The required supremum therefore comes from maximizing \(F_n\) over \(\mathcal D_n\). Strict convexity implies every maximizer is a vertex.

**Exhaustive vertex classification.** A vertex of \(\mathcal D_n\), an \((n-2)\)-dimensional section of the cube, must have at least \(n-2\) saturated coordinates. Otherwise, a nonzero feasible two-sided perturbation preserves every active coordinate, contrary to extremality. Conversely, select \(n-2\) saturated coordinates, assign their signs, and solve the two closure equations for the remaining two coordinates. Every vertex occurs from a pair with invertible \(2\)-by-\(2\) coefficient matrix. There are just \(\binom n2 2^{n-2}\) assignments: eighty for \(n=5\) and two hundred forty for \(n=6\). Exact algebraic evaluation, with duplicates removed, gives the **complete** orbit table:

| \(n\) | Orbit representative for \(d\), with \(s=1\) | Orbit size | \(F_n\) at each vertex |
|---|---|---:|---|
| 5 | \((1,-1,1,-1,1)\) | 2 | \(F_5^\star\) |
| 5 | \((2-\sqrt5,1,2-\sqrt5,-1,1)\) | 10 | \(F_5^\star\) |
| 6 | \((1,1,-1,-1,1,1)\) | 4 | \(\sqrt3/2\) |
| 6 | \((1,0,-1,1,1-\sqrt3,1)\) | 12 | \((\sqrt3-1)/2\) |
| 6 | \((1,3-2\sqrt3,3-2\sqrt3,1,-1,1)\) | 12 | \((5\sqrt3-8)/2\) |

Here \(F_5^\star=(5-2\sqrt5)\cot(\pi/10)/4\). For \(n=5\), each of the twelve vertices is maximal; for \(n=6\), only the orbit of size four has the largest quadratic value. The finite classification is completely reproducible in `verify_wigner.py`: the enumeration loops over **every** active-set/sign assignment, solves its linear constraints exactly, rejects it by exact algebraic inequalities when inadmissible, checks equality with the displayed orbit list, and checks each quadratic value symbolically. The table can also be obtained by these explicit two-equation substitutions without a numerical search.

**Sharp normalized constants and nonattainment.** With \(s=1\), the two symmetral areas are \(A(Q_5)=5\cot(\pi/10)/2\) and \(A(Q_6)=3\cot(\pi/12)=6+3\sqrt3\). Substituting the exact quadratic maxima into \(F/(A(Q)-2F)\) and simplifying yields \((\sqrt5-2)/4\) and \((\sqrt3-1)/8\). Every maximizing parameter vector has saturated coordinates, so it is excluded by strict edge positivity. Conversely, multiplying any maximizing vector by \(t\in(0,1)\) gives a strictly convex valid polygon, and its ratio converges to the displayed bound as \(t\uparrow1\). Compactness and strict convexity imply every maximizing sequence approaches the stated extremal vertex sets (after normalizing scale and the direction frame). Finally \(2(\sqrt5-2)<\sqrt3-1\), establishing the strict increase.

## Verification

From this directory run `python verify_wigner.py` with SymPy installed. Its expected final line is `EXACT_WIGNER_DECAGON_DODECAGON_OK 12 28`. The checker uses exact algebraic sign comparisons, counts all active-set assignments and distinct feasible vertices, verifies the five cyclic orbits and their exact quadratic values, checks the final radical inequalities, and independently reconstructs representative polygons to check both the Wigner shoelace area and symmetral-area identity. The continuum reduction rests on the analytic strict-convexity and active-set arguments, not on finite sampling.

## Relationship to prior work

The 2026 work of Konicer and collaborators gives the general improved polygonal isoperimetric inequality and the universal sharp (over all CPPOSes of fixed even vertex count) upper ratio \(1/4\). Its Theorem 4.4 characterizes the equiangular constant-width equality family, and Equation (4.8) is the area decomposition used here. Those general theorems do **not** optimize the Wigner ratio inside that restricted equality family. An earlier published result gives the eight-sided restricted sharp value \((\sqrt2-1)/6\) and its extremal parameter classification. The present theorem determines the next two even side counts simultaneously, exposes a different maximizer-orbit structure, and proves the restricted sharp constants are not monotonically decreasing in side count. The 2013 construction by Craizer, Teixeira and da Silva supplies the original polygonal area-evolute setting but no such extremal ratio. General discrete Fourier isoperimetric estimates do not by themselves give the constrained cube-section quadratic maxima.

## Limitations

These are **suprema**, not attained maxima, over strictly convex polygons. Only the ten- and twelve-sided restricted discrete constant-width classes are solved; no assertion is made for other side counts, arbitrary CPPOSes, smooth constant-width ovals, or the centre symmetry set. The extreme shapes lie on a parameter boundary where some edge lengths vanish. Full independent scientific validation has not been performed, and earlier equivalent unpublished or unindexed work cannot be ruled out categorically.

## References

1. I. Konicer, B. Murawski, B. Rogala, T. Wieczorek, M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612v1 (first posted 21 June 2026), Theorems 4.4, 4.7, Equation (4.8). https://arxiv.org/abs/2606.22612
2. M. Craizer, R. C. Teixeira, M. A. H. B. da Silva, *Polygons with Parallel Opposite Sides*, Discrete Comput. Geom. 50 (2013), 474–490, arXiv:1210.2442. https://arxiv.org/abs/1210.2442
3. *Sharp Wigner-caustic area bound within the equiangular constant-width octagon family*, published mathematical finding, 2026, identifier e2fc8c8ec4e3.
4. K.-K. Kwong, *A Unified Approach to Higher Order Discrete and Smooth Isoperimetric Inequalities*, Mathematika 70 (2024), article e12238, arXiv:2111.13352. https://arxiv.org/abs/2111.13352
