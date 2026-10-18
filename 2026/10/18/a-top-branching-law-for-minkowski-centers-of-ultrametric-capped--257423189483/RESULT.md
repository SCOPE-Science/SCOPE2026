# A top-branching law for Minkowski centers of ultrametric-capped metric polytopes

## Finding

For a strictly positive finite ultrametric \(w\) on \([n]\), where \(n\ge3\), let \(K_w\) be the convex body of symmetric semimetrics \(d\) satisfying every triangle inequality and the coordinate bounds \(d_{ij}\le w_{ij}\). The Minkowski asymmetry of \(K_w\) is exactly \(2\), independent of the number of points and of the cap heights. Its complete set of minimizing centers is dictated solely by the branching at the *highest* ultrametric level.

Write \(R=\max_{i<j}w_{ij}\) and define \(i\sim j\) if either \(i=j\) or \(w_{ij}<R\). This is an equivalence relation. If the resulting partition has at least three blocks, the unique center is
\[
 c_{ij}=\frac{2w_{ij}}3.
\]
If there are exactly two blocks \(A,B\), let
\[
 L=\max\{w_{ij}: i\ne j,\ \{i,j\}\subseteq A\text{ or }\{i,j\}\subseteq B\}.
\]
There is at least one such pair since \(n\ge3\), and \(0<L<R\). All centers, without exception, form the segment
\[
 c_{ij}(h)=\begin{cases}
 \frac{2w_{ij}}3,&i,j\text{ in the same top block},\\
 \frac{2R-h}{3},&i,j\text{ in different top blocks},
 \end{cases}
 \qquad 0\le h\le R-L.
\]
The segment has positive Euclidean length \(\sqrt{|A||B|}(R-L)/3\) in the standard pair-coordinate space. Therefore the full optimal-center set has affine dimension either \(0\) or \(1\), with the positive-dimensional case occurring exactly at a binary top split.

## Assumptions and scope

An ultrametric is a symmetric matrix \(w\), zero on the diagonal, with \(w_{ij}>0\) for distinct labels and \(w_{ij}\le\max\{w_{ik},w_{jk}\}\) for every triple. The ambient space has one coordinate per unordered pair of labels. A semimetric may have zero off-diagonal entries. Thus
\[
 K_w=\{d\in\mathbb R^{\binom n2}:0\le d_{ij}\le w_{ij},\quad d_{ij}\le d_{ik}+d_{jk}\ \forall\ i,j,k\text{ distinct}\}.
\]
It is a compact full-dimensional convex polytope: the constant vector \(d_{ij}=\varepsilon\) is strictly feasible for every sufficiently small \(\varepsilon>0\). For a compact full-dimensional body \(K\), define
\[
 s(K)=\inf_{c\in\mathbb R^m}\inf\{s\ge1:-(K-c)\subseteq s(K-c)\}.
\]
Every minimizing \(c\) lies in \(K\). No genericity assumption is made on heights, ties, or the numbers of children at interior dendrogram nodes. The statement concerns the **ordinary convex polytope of all dominated semimetrics**, not the generally nonconvex space of ultrametrics dominated by \(w\).

## Proof

**1. The H-description has only caps and triangle inequalities.** The triangle inequalities by themselves imply \(d_{ij}\ge0\), since adding \(d_{ik}\le d_{ij}+d_{jk}\) to \(d_{jk}\le d_{ij}+d_{ik}\) gives \(2d_{ij}\ge0\). Therefore it suffices to retain upper coordinate bounds and all oriented triangle bounds
\[
 F_{ij,k}(d):=d_{ij}-d_{ik}-d_{jk}\le0.
\]
For each pair \(ij\), the minimum and maximum of the coordinate functional on \(K_w\) are \(0\) and \(w_{ij}\), attained at the zero semimetric and at \(w\) itself, respectively.

**2. Exact negative support of every triangle functional.** For distinct \(i,j,k\), the triangle inequality gives
\[
 d_{ik}+d_{jk}-d_{ij}\le 2\min\{d_{ik},d_{jk}\}\le2\min\{w_{ik},w_{jk}\}.
\]
Equality is attained globally, not merely on the three coordinates: put \(r=\min\{w_{ik},w_{jk}\}\), and define \(f(v)=\min\{r,\operatorname{dist}_w(v,\{i,j\})\}\) on all labels. Distance to a set and truncation are each \(1\)-Lipschitz, so \(d_{uv}=|f(u)-f(v)|\) is a semimetric bounded by \(w_{uv}\). It has \(d_{ij}=0\) and \(d_{ik}=d_{jk}=r\). Consequently
\[
 \min_{d\in K_w}F_{ij,k}(d)=-2\min\{w_{ik},w_{jk}\},\quad
 \max_{d\in K_w}F_{ij,k}(d)=0.
\]

**3. Exact reflection constraints.** If a bounded polytope has a halfspace description \(a\cdot x\le b\) and \(m(a)=\min_{x\in K}a\cdot x\), the reflected inclusion \(-(K-c)\subseteq s(K-c)\) is equivalent to \((s+1)a\cdot c\le sb+m(a)\) for every displayed halfspace. Set \(z=(s+1)c\). Applying Step 2 to our complete H-description, the inclusion is equivalent to
\[
 z_{ij}\le s w_{ij},\qquad
 z_{ik}+z_{jk}-z_{ij}\ge2\min\{w_{ik},w_{jk}\}
\]
for every unordered pair and every ordered triangle. The constraints are necessary and sufficient; no assumption that the displayed halfspaces are irredundant is needed.

**4. Universal lower bound.** Choose any three labels and a pair \(ij\) whose cap \(a=w_{ij}\) is the smallest of the three positive caps. Adding the two constraints from Step 3 for the other two oriented sides yields \(2z_{ij}\ge4a\), while the coordinate cap gives \(z_{ij}\le sa\). Since \(a>0\), necessarily \(s\ge2\).

**5. Attainment at two.** For \(s=2\), choose \(z_{ij}=2w_{ij}\), equivalently \(c_{ij}=2w_{ij}/3\). The upper bounds hold with equality. Because \(w\) is ultrametric,
\[
 2w_{ik}+2w_{jk}-2w_{ij}
 \ge 2\min\{w_{ik},w_{jk}\},
\]
so the other inequalities hold too. Step 3 gives \(s(K_w)\le2\), completing the equality \(s(K_w)=2\).

**6. Local classification of every optimal center.** Fix \(s=2\) and define nonnegative cap deficits \(\delta_{ij}=2w_{ij}-3c_{ij}\). By Step 3, they satisfy
\[
 \delta_{ij}-\delta_{ik}-\delta_{jk}
 \ge 2\bigl(w_{ij}-\max\{w_{ik},w_{jk}\}\bigr)
\]
for all distinct triples. An ultrametric triangle is either equilateral, with caps \((r,r,r)\), or isosceles with exactly two maximal caps, \((t,r,r)\) where \(t<r\).

For an equilateral triangle, the three inequalities read \(\delta_a\ge\delta_b+\delta_c\) cyclically. Summation and nonnegativity force all three deficits to vanish. For a \((t,r,r)\) triangle, the two inequalities oriented toward a maximal-cap side imply that the short-side deficit is zero and both long-side deficits coincide, say with value \(h\). The short-side inequality then imposes precisely \(0\le h\le r-t\). Conversely, these patterns satisfy every local inequality, so they are a complete characterization.

**7. Global top-level propagation.** At the maximum cap \(R\), the relation \(i\sim j\iff w_{ij}<R\) is transitive by the strong triangle inequality and hence partitions the labels into \(m\ge2\) nonempty blocks. Every internal pair belongs to a \((w_{ij},R,R)\) triangle by choosing a label outside its block, so every internal deficit is zero. If \(m\ge3\), every cross-block pair lies in an \((R,R,R)\) triangle with a label in a third block. All cross deficits are therefore zero as well, yielding the unique center in Step 5.

If \(m=2\), denote the blocks by \(A,B\). The \((t,R,R)\) triangles with two labels from one block and one from the other show that two cross-block deficits sharing either endpoint coincide. The complete bipartite graph on \(A,B\) is edge-connected under these elementary comparisons (also if one block is a singleton), so every cross deficit has one common value \(h\). Every internal pair with cap \(t\) imposes \(h\le R-t\). Taking the largest such cap \(L\) gives \(0\le h\le R-L\). Conversely, all choices in this interval obey the complete local rules of Step 6. Substitution into the definition of \(\delta\) yields exactly the displayed nondegenerate segment. This proves both necessity and sufficiency.

## Verification

The proof is exact and covers every \(n\ge3\) and every strictly positive real-valued ultrametric. The auxiliary `CHECKER.py` constructs the halfspace systems independently and uses linear programming to check, on six explicit fixtures and 32 seeded ultrametric instances with \(3\le n\le6\), the negative support values, global optimum \(s=2\), and the minimum and maximum of **every center coordinate**. All 38 fixtures passed. Numerical linear programs are supporting tests, not substitutes for the argument above. To reproduce: run `python CHECKER.py` with Python 3, NumPy and SciPy installed.

For an explicit small example, take three labels with \(w_{12}=t\), \(w_{13}=w_{23}=R\) and \(0<t<R\). The full center segment has \(c_{12}=2t/3\) and \(c_{13}=c_{23}=(2R-h)/3\) for \(0\le h\le R-t\). Thus even three-point capped metric polytopes can have nonunique Minkowski centers, unlike the equilateral cap case.

## Relationship to prior work

Gartsman and Linial, *On the Löwner-John Ellipsoids of the Metric Polytope* (2023), study the special uniform ceiling \(w_{ij}=1\) and obtain the maximal inscribed and minimal circumscribed ellipsoids of the resulting metric polytope. Their different ellipsoidal center notions and volume bounds do not yield the stated Minkowski-asymmetry invariant or ultrametric binary/ternary center-locus dichotomy. Kozma, Meyerovitch, Peled, and Samotij (2021) study typical points and volume of that uniform-ceiling metric polytope, rather than optimal reflection centers.

Den Hertog, Pauphilet, and Soali, *Minkowski Centers via Robust Optimization* (first publicly released in 2022), give a general linear-optimization method for Minkowski centers of polyhedra. The present argument explicitly evaluates the needed support minima for metric-triangle functionals and resolves the optimal-center set for the infinite family of ultrametric ceilings; the general algorithm does not by itself state or specialize to this branching classification. Lin, Sturmfels, Tang, and Yoshida, *Convexity in Tree Spaces* (2015), describe tropical geometry of the **space of ultrametrics**, a different geometric object from the ordinary convex body of all semimetrics dominated by a fixed ultrametric.

## Limitations

The cap \(w\) must satisfy the ultrametric inequality and must have strictly positive pairwise values. Ordinary non-ultrametric metric ceilings are not classified here. Two labels are excluded because their bounded metric polytope is an interval with asymmetry \(1\). The result identifies Minkowski centers, not John, Löwner, Chebyshev, tropical, or barycentric centers. The finite computational checks certify only their explicit fixtures and not all dimensions. The novelty assessment compares the indicated mathematical statements, but cannot exclude an unindexed or differently formulated older equivalent theorem; independent validation has not been performed.

## References

1. D. den Hertog, J. Pauphilet and M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, Optimization Online (first posted 2022-01-19), https://optimization-online.org/2022/01/8768/ ; full-text https://optimization-online.org/wp-content/uploads/2022/01/Minkowski_Final-1.pdf.
2. R. Gartsman and N. Linial, *On the Löwner-John Ellipsoids of the Metric Polytope* (first posted 2023-04-19), arXiv:2305.02113, https://arxiv.org/html/2305.02113v1.
3. G. Kozma, T. Meyerovitch, R. Peled and W. Samotij, *What does a typical metric space look like?* (2021), arXiv:2104.01689, https://arxiv.org/html/2104.01689v2.
4. B. Lin, B. Sturmfels, X. Tang and R. Yoshida, *Convexity in Tree Spaces* (2015), arXiv:1510.08797, https://arxiv.org/html/1510.08797v3.
