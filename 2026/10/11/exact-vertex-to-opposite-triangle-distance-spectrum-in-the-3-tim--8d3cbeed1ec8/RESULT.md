# Exact vertex-to-opposite-triangle distance spectrum in the \(3\times3\times3\) lattice cube

## Finding

Let \(L=\{0,1,2\}^{3}\) and let \(\mathcal M\) consist of all pairs \((p,T)\), where \(p\in L\), \(T=\operatorname{conv}\{a,b,c\}\), the three vertices \(a,b,c\in L\) are distinct and unordered, and \(p,a,b,c\) are affinely independent. In particular, \(p\) is the marked vertex of a nondegenerate lattice tetrahedron and \(T\) is its opposite triangular face. The distance is the Euclidean distance to the **closed triangle**, not just to its supporting plane.

There are exactly \(58\,528\) such marked tetrahedra, arising from \(14\,632\) unmarked tetrahedra. The squared distances
\[r(p,T)=\operatorname{dist}(p,T)^2\]
have exactly **88 distinct rational values**. The complete spectrum, including the multiplicity of every value, is `spectrum.csv`. Equivalently, if one chooses a marked tetrahedron uniformly from \(\mathcal M\), the probability that its squared vertex-to-face distance equals a value \(r\) in that table is the recorded multiplicity divided by \(58\,528\).

The first three distinct squared-distance levels, with multiplicities, are
\[
\begin{array}{c|ccc}
\text{rank}&1&2&3\\\hline
r&1/29&1/21&1/17\\
\#\{(p,T):r(p,T)=r\}&48&96&24
\end{array}.
\]
The first level is a single orbit under the \(48\) Euclidean symmetries of the cube; the second splits into **exactly two cube-symmetry orbits of size 48 each**; the third is a single orbit of size 24. Canonical representatives, with the marked point written first and the other three vertices defining the triangle, are

- First level: \((1,1,1)\) and \((0,0,0),(0,1,2),(2,2,1)\).
- Second level, first orbit: \((0,1,1)\) and \((0,0,0),(0,1,2),(1,2,0)\).
- Second level, second orbit: \((1,1,1)\) and \((0,0,0),(0,1,2),(2,1,1)\).
- Third level: \((1,1,1)\) and \((0,0,0),(1,2,2),(2,1,2)\).

Consequently, every marked tetrahedron outside the unique minimum orbit satisfies the **sharp isolation bound**
\[
\operatorname{dist}(p,T)\ge \frac{1}{\sqrt{21}},
\]
with equality exactly in the two second-level orbits. Relative to the known minimum \(1/\sqrt{29}\), nonminimizers therefore have a distance at least \(\sqrt{29/21}\) times as large.

## Assumptions and scope

All coordinates use the ordinary Euclidean metric on \(\mathbb R^3\). A triangle is unordered; only the marked vertex is distinguished. The condition of affine independence excludes coplanar point–triangle pairs, including point–triangle pairs that are disjoint within the same plane. Exactly four marked pairs arise from each full-dimensional tetrahedron. The theorem is confined to the lattice cube with coordinate set \(\{0,1,2\}\): it does not assert the spectrum for larger lattice cubes or for two nontrivial opposing faces of a different type.

## Proof

**Step 1: exact formula for each distance.** For a marked pair choose an ordering of the triangle vertices and put
\[u=b-a,\quad v=c-a,\quad q=p-a,\quad n=u\times v,\quad G=n\cdot n.\]
Affine independence means \(q\cdot n\ne0\), and therefore \(G>0\). The perpendicular projection of \(p\) onto the plane of \(T\) has the barycentric form \(a+\alpha u+\beta v\) with
\[
\alpha=\frac{(v\cdot v)(q\cdot u)-(u\cdot v)(q\cdot v)}{G},\qquad
\beta=\frac{(u\cdot u)(q\cdot v)-(u\cdot v)(q\cdot u)}{G}.
\]
If \(\alpha\ge0\), \(\beta\ge0\), and \(\alpha+\beta\le1\), the perpendicular foot belongs to the closed triangle, and the squared distance is exactly
\[r(p,T)=\frac{(q\cdot n)^2}{G}.\]
Otherwise the nearest point in \(T\) lies on an edge. For an edge with endpoints \(x,y\), define
\[
t=\max\left\{0,\min\left\{1,\frac{(p-x)\cdot(y-x)}{\lVert y-x\rVert^2}\right\}\right\}.
\]
The corresponding squared edge distance is \(\lVert p-x-t(y-x)\rVert^2\). The minimum over the three edges is then the squared distance to the triangle. All these values are rational because every coordinate is integral and the formulas involve only exact rational arithmetic.

**Step 2: finite exhaustion.** `verify.py` iterates through the \(27\) choices of \(p\) and all three-element subsets of \(L\), ignores triples containing \(p\), and retains precisely those for which \(q\cdot(u\times v)\ne0\). Such a nonzero determinant is necessary and sufficient for a marked full-dimensional tetrahedron. Since the triple is represented by a combination, each marked tetrahedron appears **once**, and since every tetrahedron can be marked at exactly four vertices, the retained count is four times the unmarked count.

The exact rational formula of Step 1 is evaluated for every retained object. An independent convex-quadratic candidate method computes the minimum over the three vertices, three closed edges and the interior stationary point (when feasible). These are all possible minimizers because a strictly convex quadratic on the compact triangle attains its minimum either at an interior stationary point or on a boundary face. The two calculations are compared for every retained object.

This exhaustive, finite exact-integer-and-rational procedure gives \(58\,528\) retained pairs, \(19\,744\) with perpendicular foot in the triangle, and the 88-row table `spectrum.csv`. The table is sorted by increasing \(r\), contains each value precisely once, and its integer multiplicities total \(58\,528\). Because the candidate generation exhausts the finite definition of \(\mathcal M\), the table is an exhaustive mathematical classification rather than a statistical sample.

**Step 3: symmetry-orbit classification.** The full Euclidean symmetry group of \(L\) consists of \(3!\cdot2^3=48\) maps formed by coordinate permutations and coordinate reflections \(z\mapsto2-z\). They preserve distances and send the triangle vertex set to an unordered triangle vertex set. For each configuration with squared distance \(1/29\), \(1/21\), or \(1/17\), `verify.py` considers every such transform, sorts the transformed triangle vertices, and chooses the lexicographically least resulting tuple. Equality of these canonical tuples is equivalent to membership in the same cube-symmetry orbit. The exact canonical-orbit census gives respectively one orbit of size 48, two orbits of size 48, and one orbit of size 24, with the representatives listed in the Finding. Together with the ordered spectrum, this proves the sharp isolation statement.

## Verification

Run `python3 verify.py` in a directory containing both `verify.py` and `spectrum.csv`, using Python 3 and no third-party packages. The program constructs every candidate configuration from first principles, computes exact rational distances in two ways, compares all \(58\,528\) results, verifies the complete 88-entry table and its sum, and reproduces the first three distance levels and their symmetry orbits. A successful execution prints four `VERIFY_OK` lines. These computations are **exhaustive over the stated finite domain**; no approximate arithmetic or Monte Carlo argument is used.

## Relationship to prior work

Deza and Pournin, *Flat simplices and kissing polytopes* (arXiv:2601.03183v1), Theorem 1.1 and Proposition 4.1, prove the global minimum \(1/\sqrt{29}\) in this cube and the uniqueness of its minimizing orbit; they also establish a formula for larger cubes. Those published results are not claimed here as new. The new object is the **complete finite distance distribution**, its 88 attained levels and multiplicities, and especially the sharp next-level bound with two distinct geometric equality orbits. The primary manuscript reports only global minima and uniqueness, not the second level or the entire distribution.

Deza, Liu and Pournin, *Kissing polytopes in dimension 3* (arXiv:2502.19554v1), and *Small kissing polytopes* (arXiv:2412.03479v1), study minimal distances between disjoint lattice polytopes and least-squares geometry. Their minima and general models are related but do not state this marked point-to-triangle spectrum. This distinction is substantive: a theorem identifying the global minimum and all its minimizers does not imply the exact next nonminimal value or the complete distribution of all other values.

## Limitations

The result is a finite-domain classification for the smallest nonbinary lattice cube. It does not provide an asymptotic law in the cube side length, a geometric characterization of all 88 distance levels, or a best uniform stability inequality for all larger cubes. The code supplies an auditable exhaustive proof for this finite case but is not a proof about arbitrarily large cubes. Prior work on minimal distances is acknowledged; equivalence to an unindexed prior finite census cannot be excluded solely through literature searches. No independent external audit is asserted.

## References

1. A. Deza and L. Pournin, *Flat simplices and kissing polytopes*, arXiv:2601.03183v1, 6 January 2026; Theorem 1.1, Proposition 4.1, Sections 4–5.
2. A. Deza, Z. Liu and L. Pournin, *Kissing polytopes in dimension 3*, arXiv:2502.19554v1, 26 February 2025; Sections 2–4.
3. A. Deza, Z. Liu and L. Pournin, *Small kissing polytopes*, arXiv:2412.03479v1, 4 December 2024; Sections 2–4.
