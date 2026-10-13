# Induced and maximal induced matchings of rectangular rook graphs

## Finding

Let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), with labeled rows and columns and integers \(m,n\ge2\). Let \(\mathcal I_{m,n}(z)\) count induced matchings by their number of edges, including the empty matching. Let \(\mathcal M_{m,n}(z)\) count the inclusion-maximal induced matchings. Both complete distributions have the following bivariate exponential generating functions:

\[
\sum_{m,n\ge0}\mathcal I_{m,n}(z)\frac{u^m v^n}{m!n!}
=\exp\!\left(u+v+\frac z2(uv^2+u^2v)\right),
\]

\[
\sum_{m,n\ge0}\mathcal M_{m,n}(z)\frac{u^m v^n}{m!n!}
=(e^u+e^v-1+uv)\exp\!\left(\frac z2(uv^2+u^2v)\right).
\]

For an explicit finite coefficient formula, put \(r=m-a-2b\) and \(c=n-2a-b\). With \(a,b\) ranging over nonnegative integers for which \(r,c\ge0\), define

\[
N_{m,n}(a,b)=\frac{m!n!}{2^{a+b}a!b!r!c!}.
\]

Then

\[
\mathcal I_{m,n}(z)=\sum_{a,b:\ r,c\ge0} N_{m,n}(a,b)z^{a+b},
\]

\[
\mathcal M_{m,n}(z)=\sum_{\substack{a,b:\ r,c\ge0\\
 r=0\ \text{or}\ c=0\ \text{or}\ (r,c)=(1,1)}}N_{m,n}(a,b)z^{a+b}.
\]

In particular, the greatest induced-matching cardinality and smallest cardinality of an inclusion-maximal induced matching are respectively

\[
\nu_{\mathrm{ind}}(R_{m,n})=\min\!\left(m,n,\left\lfloor\frac{m+n}{3}\right\rfloor\right),
\qquad
\mu_{\mathrm{ind}}(R_{m,n})=\left\lceil\frac{\min(m,n)}2\right\rceil.
\]

Consequently, **every inclusion-maximal induced matching has maximum cardinality** precisely for the nine unordered rectangular sizes

\[
\{(m,n): 2\le m\le n,\ R_{m,n}\text{ is well-indumatched}\}
=\{(2,2),(2,3),(3,3),(3,4),(3,5),(4,4),(5,5),(5,6),(7,7)\}.
\]

Here the displayed equality is a classification of the *sizes satisfying the property*, not an assertion that all pairs \((m,n)\) equal the displayed set.

## Assumptions and scope

Graphs are finite, simple, and undirected. The rook graph has one vertex per square of an \(m\)-by-\(n\) rectangular board and adjacency exactly when two distinct squares share a row or column. An induced matching is a set of graph edges whose endpoints induce a disjoint union of copies of \(K_2\); it is inclusion-maximal if no further edge can be adjoined while retaining this property. The generating functions extend the definition to \(m=0\) or \(n=0\) by treating the edgeless graph as having its empty matching, both induced and maximal.

The theorem concerns **induced** rather than ordinary matchings and **maximal** rather than maximum matchings; these notions must not be interchanged. The coefficient polynomials count matchings on labeled boards, not isomorphism classes.

## Proof

**Bijection.** Identify a square \((i,j)\) with edge \(x_i y_j\) of \(K_{m,n}\). Every edge of the rook graph consists of two edges of \(K_{m,n}\) sharing exactly one vertex; its two corresponding edges form a \(P_3\) (a star with two leaves). If two distinct rook edges belong to an induced matching, none of their four square-vertices may be adjacent in the rook graph. Hence the associated two \(P_3\)'s have disjoint vertex supports in \(K_{m,n}\). Conversely, any family of vertex-disjoint \(P_3\)'s in \(K_{m,n}\) supplies an induced matching in the rook graph, with no overcounting.

A star centered in the row part consumes one row and two columns; a star centered in the column part consumes two rows and one column. Let there be \(a\) stars of the former type and \(b\) of the latter. The numbers of unused row and column vertices are exactly \(r=m-a-2b\) and \(c=n-2a-b\). Choosing the center sets and assigning disjoint unordered leaf-pairs gives

\[
\binom ma\binom nb\frac{(m-a)_{\underline{2b}}}{2^b}\frac{(n-b)_{\underline{2a}}}{2^a}
=\frac{m!n!}{2^{a+b}a!b!r!c!}.
\]

These choices are mutually exclusive and exhaustive. The labeled-set exponential formula, with component weights \(u\), \(v\), \(zuv^2/2\), and \(zu^2v/2\), proves the first generating function.

**Maximality.** After selecting a family of vertex-disjoint \(P_3\)'s, a new rook edge can be added exactly when the unused rows and columns support another \(P_3\) in their complete bipartite graph \(K_{r,c}\). Such a path exists exactly when \((r\ge1\ \text{and}\ c\ge2)\) or \((r\ge2\ \text{and}\ c\ge1)\). Thus the family is maximal exactly when \(r=0\), or \(c=0\), or \((r,c)=(1,1)\). This proves the coefficient restriction above, including all boundary cases. The exponential weights for the allowed unmatched vertices are \(e^u+e^v-1+uv\): all remaining vertices on one side, with the doubly-empty choice counted once, or exactly one on each side. This proves the second generating function.

**Largest cardinality.** Fix \(k=a+b\). Nonnegative integer star counts satisfying the row and column capacities exist exactly when

\[
\max(0,2k-n)\le b\le\min(k,m-k).
\]

These inequalities have an integer solution if and only if \(k\le m\), \(k\le n\), and \(3k\le m+n\). This proves the asserted maximum. Any maximum induced matching is necessarily inclusion-maximal.

**Smallest maximal cardinality.** By transposing the board suppose \(m\le n\). If a maximal packing leaves no unused row, its \(k\) components each cover at most two rows, so \(k\ge\lceil m/2\rceil\). If it leaves no unused column, the same argument yields \(k\ge\lceil n/2\rceil\). The remaining maximality case leaves exactly one unused vertex in each part, giving \(3k=m+n-2\). Hence \(k\ge\lceil(2m-2)/3\rceil\ge\lceil m/2\rceil\); the last inequality follows directly for \(m\ge4\), and by inspection for \(m=2,3\).

This lower bound is attained by covering all \(m\) rows: when \(m=2h\), use \(h\) disjoint column-centered stars; when \(m=2h+1\ge3\), use \(h\) column-centered stars and one row-centered star. The latter consumes \(h+2\le m\le n\) columns. Both constructions are maximal because no unused rows remain. Therefore the smallest maximal size is \(\lceil m/2\rceil\).

**Well-indumatched classification.** All maximal induced matchings have the same size if and only if the proved largest and smallest values coincide. Setting \(p=\min(m,n)\), \(q=\max(m,n)\), and \(h=\lceil p/2\rceil\), equality (for \(p\ge2\)) means \(3h\le p+q\le3h+2\). Combined with \(q\ge p\), this forces \(p\in\{2,3,4,5,7\}\); direct substitution gives exactly the nine pairs listed in the finding. Each excluded pair has two maximal induced matchings of different cardinalities, supplied by the preceding extremal constructions.

## Verification

The accompanying standalone `verify.py` constructs rook-graph edges from their square coordinates and enumerates all induced matchings directly using a conflict relation on endpoint adjacencies. It tests maximality against every possible addable graph edge, independently of the \(P_3\) parameter formula. For every rectangular size \(2\le m,n\le5\), all coefficients of both polynomials agree exactly (16 boards; 6,201 induced matchings in total). Independently, the two extremal-size formulas agree with the finite coefficient sums for every pair \(2\le m,n\le18\).

For example,

\[
\mathcal I_{3,3}(z)=1+18z+9z^2,\qquad \mathcal M_{3,3}(z)=9z^2,
\]

and the inclusion-maximal matching counts at sizes \(3\) and \(4\) of \(R_{6,6}\) are \(3600\) and \(8100\), respectively. The finite tests are corroboration, not a proof for unbounded board sizes; the bijection and counting above supply that proof.

## Relationship to prior work

Induced matchings (also called strong or distance-two matchings) and the distinction between maximal and maximum were established earlier. Basavaraju, Heggernes, van 't Hof, Saei, and Villanger (arXiv:1312.5180, first version 18 December 2013) prove a sharp *upper bound* on the number of maximal induced matchings of arbitrary triangle-free graphs. Rectangular rook graphs typically contain triangles, and the bound does not enumerate their matchings. Baptiste, Kovalyov, Orlovich, Werner, and Zverovich (2012 proceedings, expanded 2016 article) investigate graphs in which all maximal induced matchings have equal size and give general recognition and forbidden-subgraph results; those general results do not evaluate the rook-graph enumerators or list the nine exceptional board shapes.

Pippenger (UBC TR-2001-12, dated 10 September 2001) enumerates ordinary matchings in incidence graphs of complete and complete bipartite graphs. Incidence-graph edges pair an original vertex with an original edge; they are different objects from vertex-disjoint two-edge paths in \(K_{m,n}\). OEIS A341847 and A341850 concern maximal and maximum **ordinary** matchings of rook graphs, respectively, not induced matchings. The new assertion here is the exact two-distribution evaluation and its explicit cardinality consequences, not the general definitions, the classical labeled-set formula, or recognition complexity.

## Limitations

No universal closed expression is claimed for the number of maximum induced matchings beyond coefficient extraction from the displayed explicit finite sum. The classification is for two-dimensional rectangular rook graphs, not arbitrary Hamming products or arbitrary line graphs. A differently indexed enumeration of disjoint \(P_3\)-packings in complete bipartite graphs could imply the first generating function, and an unlocated specialized earlier study could overlap the maximality part. The full original Pippenger PDF was not materially readable in the available retrieval, although its source-page abstract and mathematical object were identifiable. Independent mathematical review remains outstanding.

## References

1. M. Basavaraju, P. Heggernes, P. van 't Hof, R. Saei, and Y. Villanger, *Maximal induced matchings in triangle-free graphs*, arXiv:1312.5180v1 (18 December 2013), https://arxiv.org/abs/1312.5180.
2. P. Baptiste, M. Y. Kovalyov, Y. L. Orlovich, F. Werner, and I. E. Zverovich, *Graphs with maximal induced matchings of the same size*, IFAC Proceedings Volumes (2012), DOI: 10.3182/20120523-3-RO-2023.00065, https://doi.org/10.3182/20120523-3-RO-2023.00065.
3. P. Baptiste, M. Y. Kovalyov, Y. L. Orlovich, F. Werner, and I. E. Zverovich, *Graphs with maximal induced matchings of the same size*, Discrete Applied Mathematics 216 (2016/17), 15–28, DOI: 10.1016/j.dam.2016.08.015, https://doi.org/10.1016/j.dam.2016.08.015.
4. N. Pippenger, *Enumeration of matchings in the incidence graphs of complete and complete bipartite graphs*, UBC Technical Report TR-2001-12 (10 September 2001), https://www.cs.ubc.ca/tr/2001/tr-2001-12.
5. *OEIS A341847*, table of numbers of maximal ordinary matchings in rook graphs, https://oeis.org/A341847; and *OEIS A341850*, table of maximum ordinary matchings, https://oeis.org/A341850.
6. *Induced matchings in asteroidal triple-free graphs*, Discrete Applied Mathematics 132 (2003), DOI: 10.1016/S0166-218X(03)00390-1, https://doi.org/10.1016/S0166-218X(03)00390-1.
