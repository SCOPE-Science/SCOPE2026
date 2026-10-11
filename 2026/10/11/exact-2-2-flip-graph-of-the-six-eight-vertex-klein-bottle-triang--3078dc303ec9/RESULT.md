# Exact \(2\)-\(2\) flip graph of the six eight-vertex Klein-bottle triangulations
## Finding
Let \(\mathcal T=\{242,1133,404,161,323\text{-A},323\text{-B}\}\) be the six combinatorial isomorphism types of eight-vertex triangulations of the Klein bottle classified by Cervone. For \(X,Y\in\mathcal T\), define \(m(X,Y)\) to be the number of edges of a representative of type \(X\) on which a legal \(2\)-\(2\) bistellar flip produces a triangulation of type \(Y\). The complete nonzero transition data are
\[
\begin{aligned}
242 &: 1133^{(2)},\,161^{(2)},\,323\text{-A}^{(2)},\,404^{(1)},\\
323\text{-A} &: 1133^{(2)},\,242^{(2)},\,323\text{-B}^{(2)},\\
404 &: 242^{(4)},\\
161 &: 1133^{(2)},\,161^{(2)},\,242^{(2)},\,323\text{-B}^{(2)},\\
1133 &: 1133^{(1)},\,161^{(1)},\,242^{(1)},\,323\text{-A}^{(1)},\,323\text{-B}^{(1)},\\
323\text{-B} &: 1133^{(2)},\,161^{(2)},\,323\text{-A}^{(2)}.
\end{aligned}
\]
Here the superscript is a multiplicity, not a power. After loops and multiplicities are discarded, the resulting six-vertex type graph has nine edges, is connected, and has diameter \(3\). Its unique leaf is \(404\), adjacent only to \(242\). The only types admitting a flip to an isomorphic triangulation are \(161\) and \(1133\), with respectively two and one such flippable edges.

## Assumptions and scope
A legal \(2\)-\(2\) bistellar flip is taken in the standard simplicial-surface sense: if an edge \(ab\) is contained in exactly the two triangles \(abc\) and \(abd\), and \(cd\) is not already an edge, then those two triangles are replaced by \(acd\) and \(bcd\). Counts are made on labeled representatives but are invariant under simplicial isomorphism, since an isomorphism bijects flippable edges and preserves the target isomorphism type.

The calculation starts from the published \(242\) facet list
\[
123,237,135,157,147,126,246,168,148,248,346,347,568,356,258,257.
\]
No assertion is made about flips that change the number of vertices, about geometric realizability in \(\mathbb R^3\), or about larger triangulations of the Klein bottle.

## Proof
Starting from the exact \(242\) facet list, exhaust every legal \(2\)-\(2\) flip. After each flip, canonicalize the resulting two-dimensional complex up to vertex relabeling. Repeat this process breadth-first until no new isomorphism class occurs.

Exactly six canonical classes occur. They are identified with Cervone's six types by their vertex-valence multisets:
\[
\begin{array}{c|c}
242&(5,5,6,6,6,6,7,7)\\
1133&(4,5,6,6,6,7,7,7)\\
404&(5,5,5,5,7,7,7,7)\\
161&(5,6,6,6,6,6,6,7)\\
323\text{-A},323\text{-B}&(5,5,5,6,6,7,7,7).
\end{array}
\]
For the two \(323\) types, let \(u,v,w\) be the three degree-\(7\) vertices. The type is \(323\text{-A}\) exactly when \(\{u,v,w\}\) is a triangle, and \(323\text{-B}\) otherwise.

For each of the six representatives, exhaust all flippable edges and classify every target by the same invariant-and-canonicalization procedure. Omitting loops and multiplicity produces the nine undirected adjacencies
\[
\begin{gathered}
404\!-\!242,\quad 242\!-\!1133,\quad 242\!-\!161,\quad 242\!-\!323\text{-A},\\
1133\!-\!161,\quad 1133\!-\!323\text{-A},\quad 1133\!-\!323\text{-B},\\
161\!-\!323\text{-B},\quad 323\text{-A}\!-\!323\text{-B}.
\end{gathered}
\]
Breadth-first distance calculation on this graph gives diameter \(3\), and inspection of the degrees gives the unique leaf \(404\).

## Verification
The standalone verifier `verify.py` uses only the Python standard library. It reconstructs the \(242\) complex, checks that every discovered representative has \(16\) triangles, \(24\) edges, edge degree \(2\), and cyclic vertex links, exhausts the full flip closure up to combinatorial isomorphism, identifies exactly six classes, then recomputes every directed transition multiplicity. It also independently computes the underlying simple graph, its connectivity, its diameter, the unique leaf, and the self-flip types.

A replay of the packaged verifier prints:
`VERIFY_OK classes=6 flip_counts=242:7,323-A:6,404:4,161:8,1133:5,323-B:6 underlying_edges=9 diameter=3 leaf=404 self_flip_types=1133,161`

## Relationship to prior work
Cervone's classification proves that there are exactly six combinatorial types of eight-vertex Klein-bottle triangulations and explicitly introduces edge conversion, which is the \(2\)-\(2\) flip used here. The inspected classification text uses selected conversions to construct and distinguish the six types, but it does not give the complete directed flip-multiplicity table above, the nine-edge quotient graph, its diameter, or the self-flip census.

Karve's thesis reproduces the exact \(242\) facet list used as the computational seed. Sulanke later classified all \(29\) irreducible triangulations of the Klein bottle, a broader vertex-count setting; that classification provides context but does not by itself imply the exact all-edge transition table among the six eight-vertex types.

## Limitations
This is an exact finite result for the six vertex-minimal triangulations and for \(2\)-\(2\) bistellar moves only. It does not classify longer flip paths through triangulations with more than eight vertices, nor does it address geometric immersions or metric optimization. The principal originality risk is an unindexed or non-searchable historical table that may already record the same complete transition multiplicities.

## References
1. D. P. Cervone, *Vertex-Minimal Simplicial Immersions of the Klein Bottle in Three Space*, Geometriae Dedicata 50 (1994), 117–141. DOI `10.1007/BF01265307`.
2. V. Karve, thesis containing the exact six eight-vertex Klein-bottle triangulations and the \(242\) facet list, page 103 of the inspected PDF.
3. T. Sulanke, *Note on the Irreducible Triangulations of the Klein Bottle*, arXiv `math/0407008`.
4. F. H. Lutz, *Triangulated Manifolds with Few Vertices: Combinatorial Manifolds*, arXiv `math/0506372`.
