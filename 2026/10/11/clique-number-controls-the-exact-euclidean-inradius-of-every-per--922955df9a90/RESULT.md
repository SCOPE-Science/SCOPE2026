# Clique number controls the exact Euclidean inradius of every perfect stable-set polytope
## Finding
Let \(G=(V,E)\) be a nonempty finite perfect graph, and let
\[
\omega=\omega(G)
\]
be its clique number. Its stable-set polytope is
\[
\operatorname{STAB}(G)
=
\operatorname{conv}
\{\chi_S:S\subseteq V\text{ is stable}\}
\subseteq\mathbb R^V.
\]

With the standard Euclidean metric,
\[
\boxed{
r_{\mathrm{in}}\!\left(\operatorname{STAB}(G)\right)
=
\frac{1}{\omega+\sqrt{\omega}}.
}
\tag{1}
\]

Write
\[
r_*=\frac{1}{\omega+\sqrt{\omega}}.
\]
Then the complete set of centers of largest inscribed Euclidean balls is
\[
\boxed{
\left\{
c\in\mathbb R^V:
c_v\ge r_*\ \text{for every }v\in V,\quad
\sum_{v\in C}c_v
\le
1-r_*\sqrt{|C|}
\ \text{for every maximal clique }C
\right\}.
}
\tag{2}
\]

In particular,
\[
r_*\mathbf 1
\]
is always an incenter. It is the unique incenter if and only if every vertex of \(G\) belongs to a maximum clique.

For the maximal ball centered at \(r_*\mathbf1\), the tangent facets are exactly:
- every coordinate facet \(x_v=0\);
- every maximal-clique facet
  \[
  \sum_{v\in C}x_v=1
  \]
  for which \(|C|=\omega\).

Hence, if \(m_\omega(G)\) is the number of maximum cliques, that centered ball has exactly
\[
\boxed{|V|+m_\omega(G)}
\tag{3}
\]
tangent facets.

Finally, the metric determines the clique number:
\[
\boxed{
\omega(G)
=
\left(
\frac{\sqrt{1+4/r_{\mathrm{in}}}-1}{2}
\right)^2.
}
\tag{4}
\]
Since \(G\) is perfect,
\[
\chi(G)=\omega(G),
\]
so the canonical Euclidean inradius also determines the chromatic number.

## Assumptions and scope
The graph is finite, nonempty, and perfect. The metric is the ordinary Euclidean metric in the canonical characteristic-vector realization of the stable-set polytope.

The theorem uses the classical perfect-graph description of the stable-set polytope by nonnegativity and clique inequalities. It does not claim the same formula for arbitrary graphs, where additional facet classes can reduce the inradius.

A maximal clique means inclusion-maximal. A maximum clique means one of cardinality \(\omega(G)\). The distinction is essential for the full incenter formula and the tangency statement.

## Proof
For a perfect graph, the stable-set polytope has the exact inequality description
\[
x_v\ge0
\qquad(v\in V)
\tag{5}
\]
and
\[
\sum_{v\in C}x_v\le1
\qquad
(C\text{ a maximal clique}).
\tag{6}
\]

These inequalities are facet-defining. For (5), the origin together with the singleton stable-set vectors \(e_u\) for \(u\ne v\) are affinely independent points of the face \(x_v=0\).

For (6), fix a maximal clique \(C\). The singleton vectors \(e_c\), \(c\in C\), lie on the hyperplane \(x(C)=1\). For every \(u\notin C\), maximality of \(C\) gives some \(c(u)\in C\) nonadjacent to \(u\), so
\[
e_u+e_{c(u)}
\]
is also the characteristic vector of a stable set and lies on \(x(C)=1\). The resulting \(|V|\) points are linearly independent after ordering the coordinates with \(V\setminus C\) first, hence affinely independent on that hyperplane. Thus (6) is a facet.

Let a Euclidean ball of radius \(r\) centered at \(c\) lie in \(\operatorname{STAB}(G)\). Its distance to the coordinate facet \(x_v=0\) is \(c_v\), hence
\[
c_v\ge r
\qquad(v\in V).
\tag{7}
\]
The normal of the clique facet (6) is the characteristic vector \(\mathbf1_C\), whose Euclidean norm is \(\sqrt{|C|}\). Therefore
\[
c(C)+r\sqrt{|C|}\le1
\qquad
(C\text{ maximal clique}).
\tag{8}
\]

Choose a maximum clique \(C_*\), so \(|C_*|=\omega\). By (7),
\[
c(C_*)\ge\omega r.
\]
Combining this with (8) gives
\[
\omega r+r\sqrt{\omega}\le1,
\]
and hence
\[
r\le\frac1{\omega+\sqrt{\omega}}.
\tag{9}
\]

Now set
\[
r_*=\frac1{\omega+\sqrt{\omega}},
\qquad
c_*=r_*\mathbf1.
\]
The coordinate constraints have distance exactly \(r_*\). For a maximal clique \(C\) of size \(k\le\omega\),
\[
c_*(C)+r_*\sqrt{k}
=
r_*(k+\sqrt{k})
\le
r_*(\omega+\sqrt{\omega})
=
1,
\]
because \(k+\sqrt{k}\) is strictly increasing. Thus the radius-\(r_*\) ball centered at \(c_*\) lies in the polytope. Together with (9), this proves (1).

For a fixed radius \(r_*\), conditions (7)--(8) are necessary and sufficient for the whole Euclidean ball to lie in every defining halfspace. Substituting \(r_*\) gives exactly (2), so (2) is the complete incenter set.

If every vertex belongs to a maximum clique, let \(c\) satisfy (2). On any maximum clique \(C\),
\[
c(C)\le1-r_*\sqrt{\omega}=\omega r_*,
\]
while every term \(c_v\ge r_*\). Therefore
\[
c_v=r_*
\]
for every \(v\in C\). If maximum cliques cover \(V\), this forces
\[
c=r_*\mathbf1,
\]
so the incenter is unique.

Conversely, suppose that some vertex \(u\) belongs to no maximum clique. Every maximal clique containing \(u\) then has cardinality strictly less than \(\omega\). At \(c_*=r_*\mathbf1\), every such clique inequality in (2) has strictly positive slack
\[
1-r_*(|C|+\sqrt{|C|})>0.
\]
There are only finitely many maximal cliques containing \(u\), so one may increase only the \(u\)-coordinate of \(c_*\) by a sufficiently small positive amount while preserving all inequalities in (2). This produces a second incenter. Hence uniqueness is equivalent to coverage by maximum cliques.

At the uniform incenter, every coordinate facet is tangent because its distance is \(r_*\). A maximal-clique facet of cardinality \(k\) has distance
\[
\frac{1-kr_*}{\sqrt{k}}.
\]
It equals \(r_*\) exactly when
\[
r_*(k+\sqrt{k})=1,
\]
which, by strict monotonicity of \(k+\sqrt{k}\), occurs exactly at \(k=\omega\). This proves the tangency statement and (3).

Finally, if
\[
r_{\mathrm{in}}=\frac1{\omega+\sqrt{\omega}},
\]
then \(y=\sqrt{\omega}\) satisfies
\[
y^2+y=\frac1{r_{\mathrm{in}}},
\]
so
\[
y=\frac{\sqrt{1+4/r_{\mathrm{in}}}-1}{2}.
\]
Squaring proves (4). Perfectness then gives \(\chi(G)=\omega(G)\).

## Verification
The proof is symbolic and applies to every nonempty finite perfect graph. It uses only the exact perfect-graph halfspace description and elementary Euclidean distances to facets.

The source-dependent premise was checked directly in full text: for perfect graphs, nonnegativity together with maximal-clique inequalities characterizes the stable-set polytope. The argument above separately verifies that these inequalities are facets, so the tangency language does not rely on an unproved irredundancy assumption.

The accompanying `verify.py` enumerates several perfect graph families, reconstructs all stable sets and maximal cliques, verifies every defining inequality on every stable-set vertex, and checks the predicted inradius, the active clique sizes, and the maximum-clique-cover uniqueness criterion. The computation is corroborative only.

## Relationship to prior work
Kohl, Olsen, and Sanyal study stable-set polytopes of perfect graphs inside their theory of anti-blocking and unconditional reflexive polytopes. Their paper, whose primary classification is \(52B20\), supplies the middle-period geometry anchor and emphasizes the geometric role of perfect-graph stable-set polytopes.

Hu and Laurent give a detailed full-text treatment of stable-set polytopes for perfect graphs and explicitly recall Chvátal's theorem that nonnegativity and maximal-clique inequalities form the complete linear description. Their work studies extension complexity rather than Euclidean metric balls.

Neither inspected source states the formula (1), the full center locus (2), the maximum-clique-cover uniqueness criterion, or the tangent-facet classification. Full-text searches of the directly relevant papers did not locate “inradius,” “Chebyshev center,” or “largest inscribed ball” results for this object. Targeted published-result and literature searches under stable-set, perfect-graph, clique-number, inradius, Chebyshev-center, and exact-formula terminology likewise did not locate a statement implying the theorem.

A nearby same-week result on Hansen polytopes also uses perfect graphs, but it concerns a different centrally symmetric lift in one higher dimension; its radius formula does not imply the present metric theorem for \(\operatorname{STAB}(G)\).

## Limitations
The formula depends on the canonical Euclidean characteristic-vector realization. It is not invariant under arbitrary affine transformations.

Perfectness is essential to the proof because it guarantees that clique inequalities and nonnegativity are the complete description. For nonperfect graphs, odd-hole, rank, or other facets can be closer to the interior and can lower the inradius.

The originality assessment leaves a residual risk that the formula has appeared as folklore or as a short example in general Chebyshev-center literature. The metric theorem is independently proved here rather than inferred from search nonappearance.

## References
1. Florian Kohl, McCabe Olsen, and Raman Sanyal, *Unconditional Reflexive Polytopes*, arXiv:1906.01469, first public version 2019-06-03; Discrete & Computational Geometry 64 (2020), 427--452, DOI 10.1007/s00454-020-00199-8.
2. Hao Hu and Monique Laurent, *On the Linear Extension Complexity of Stable Set Polytopes for Perfect Graphs*, European Journal of Combinatorics 80 (2019), 247--260, DOI 10.1016/j.ejc.2018.02.014.
3. Václav Chvátal, *On Certain Polytopes Associated with Graphs*, Journal of Combinatorial Theory, Series B 18 (1975), 138--154.
