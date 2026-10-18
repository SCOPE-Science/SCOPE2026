# Arithmetic rigidity and exact census of open-independent open-locating-dominating sets in rook graphs

## Finding

For integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with vertex set \([m]\times[n]\). Let \(\mathscr C_{m,n}\) consist of all subsets \(S\) such that each vertex has a nonempty, distinct **open** neighborhood signature \(N(v)\cap S\), and each selected vertex has at most one selected neighbor. Such sets are called open-independent open-locating-dominating sets (\(OLD_{oind}\)-sets).

**Complete classification.** Every \(S\in\mathscr C_{m,n}\) is the disjoint union of isolated horizontal selected edges and isolated vertical selected edges, with different edges using pairwise disjoint sets of rows and pairwise disjoint sets of columns. Exactly one of these alternatives holds:

1. **Horizontal-only:** \(m=h\ge2\), \(n=2h\) or \(n=2h+1\), with \(h\) horizontal edges. There is no empty row and at most one empty column.
2. **Vertical-only:** \(n=v\ge2\), \(m=2v\) or \(m=2v+1\), with \(v\) vertical edges. There is no empty column and at most one empty row.
3. **Mixed:** integers \(h,v\ge1\) satisfy \(m=h+2v\) and \(n=2h+v\). All rows and columns are occupied, with \(h\) horizontal edges and \(v\) vertical edges.

Conversely **every** configuration described by one of these alternatives is an \(OLD_{oind}\)-set. The alternatives are mutually exclusive. In particular, no set exists for a board outside these arithmetic families. Every existing set on the same board has the same size and hence is automatically minimum.

The exact number \(c_{m,n}=|\mathscr C_{m,n}|\) and common cardinality \(\ell_{m,n}\), if positive, are

\[
(c_{m,n},\ell_{m,n})=
\begin{cases}
\left(\dfrac{n!}{2^m},2m\right),&n\in\{2m,2m+1\},\\[3pt]
\left(\dfrac{m!}{2^n},2n\right),&m\in\{2n,2n+1\},\\[3pt]
\left(\dfrac{m!n!}{2^{h+v}h!v!},2(h+v)\right),&m=h+2v,\ n=2h+v,\ h,v\in\mathbb Z_{\ge1},\\[3pt]
(0,\text{undefined}),&\text{otherwise}.
\end{cases}
\]

In the mixed case, the parameters are uniquely determined as \(h=(2n-m)/3\), \(v=(2m-n)/3\); its common cardinality is \(2(m+n)/3\). On a square board, \(\mathscr C_{m,m}\ne\varnothing\) if and only if \(3\mid m\), in which case \(h=v=m/3\) and the number of sets is \((m!)^2/(2^{2m/3}((m/3)!)^2)\).

## Assumptions and scope

Graphs are finite, simple, undirected and have labeled vertices. Two squares \((i,j),(i',j')\) are adjacent precisely when they differ in exactly one coordinate. Signatures use **open** rather than closed neighborhoods. The open-independence condition is \(|N(x)\cap S|\le1\) for selected \(x\); since every vertex must have a nonempty signature, this inequality is equality for selected vertices. The factorial counts distinguish subsets of the labeled vertex set, not orbits under graph automorphisms. No claim is made for factors \(K_1\), where several additional boundary cases arise.

## Proof

**Step 1: induced-edge structure.** If \(S\) is valid, each selected vertex has exactly one neighbor in \(S\), so the induced subgraph \(R_{m,n}[S]\) is a disjoint union of copies of \(K_2\). Every such edge is horizontal (two vertices in one row) or vertical (two in one column). Any two distinct induced edges cannot use a common row: otherwise two endpoints of different components would be adjacent. The same applies to columns. Write \(h\) and \(v\) for the numbers of horizontal and vertical edges. Their occupied-row and occupied-column counts are, respectively,

\[r=h+2v,\qquad c=2h+v.\]

**Step 2: occupancy restrictions.** If two columns were empty, the two cells in those columns of any fixed row would have identical signatures (the selected vertices of that row). Thus at most one column can be empty; symmetrically at most one row can be empty. Furthermore, if \(h>0\) and a row is empty, choose an endpoint \(x\) of a horizontal selected edge and consider the cell in the empty row and \(x\)'s column. Its signature is exactly \(\{x\}\), which is also the signature of the selected mate of \(x\). This contradicts location. Hence \(h>0\) forbids an empty row. By transpose, \(v>0\) forbids an empty column. It follows that in the horizontal-only case \(m=h\) and \(n\in\{2h,2h+1\}\); in the vertical-only case \(n=v\) and \(m\in\{2v,2v+1\}\); and in the mixed case \(m=h+2v\), \(n=2h+v\). Since \(m,n\ge2\), a pure case has at least two selected edges.

**Step 3: sufficiency and unique signatures.** Take any induced-edge configuration with the stated occupancy. Each selected vertex has the singleton signature consisting of its unique mate; these singletons are pairwise distinct. Any unselected cell \((i,j)\) has signature \(S_i\cup S^j\), where \(S_i\) is the selected part of its row and \(S^j\) the selected part of its column (disjoint for an unselected cell). Write \(H\) and \(V\) for the disjoint sets of selected vertices that belong to horizontal and vertical components. In a mixed configuration, row types have two \(H\)-vertices or one \(V\)-vertex, and column types have one \(H\)-vertex or two \(V\)-vertices. Thus unselected signatures have the following distinct \((|H\cap N(x)\cap S|,|V\cap N(x)\cap S|)\) profiles: horizontal row with horizontal column \((3,0)\), horizontal row with vertical column \((2,2)\), vertical row with horizontal column \((1,1)\), and vertical row with vertical column \((0,3)\). For the \((3,0)\) profile, the unique pair belonging to one horizontal edge identifies the row, and the remaining vertex identifies the column. The \((0,3)\) profile is the transpose: the unique vertical-edge pair identifies the column, and the remaining vertex the row. In the other two profiles, the signature's labeled row and column pieces identify both coordinates directly. Consequently distinct unselected cells have different signatures, each containing at least two selected vertices and so distinct from all selected-vertex singleton signatures.

For a horizontal-only configuration, the same \((3,0)\) signatures distinguish cells in occupied columns; if there is one empty column, cells there have pair signatures consisting of the two vertices of their respective horizontal row-edge, different for distinct rows and different in cardinality from all occupied-column unselected signatures. The vertical-only case follows by transposing the board. Thus **every** allowed arrangement is valid. This step proves location explicitly: the general two-neighbor necessary condition alone would not be enough in a graph containing triangles or four-cycles.

**Step 4: labeled enumeration and size.** In a mixed arrangement, assign the \(h\) horizontal edges one row and two unordered columns apiece, and the \(v\) vertical edges two unordered rows and one column apiece. All rows and columns are used. There are \(m!n!\) allocations if components and their endpoints are temporarily ordered. Division by \(2^{h+v}\) forgets order inside the two-row or two-column components, and division by \(h!v!\) forgets the order of horizontal and vertical components. Hence the count is \(m!n!/(2^{h+v}h!v!)\). In a horizontal-only arrangement, partition \(2m\) columns into the unordered pairs attached to the \(m\) named rows; if \(n=2m+1\), first choose the one empty column. Both give \(n!/2^m\). The vertical formula is symmetric. Every selected edge contributes two vertices, giving common size \(2(h+v)\), or \(2m\)/\(2n\) in pure cases. No alternative can coexist on one board because the mixed inequalities are strict \(m<2n\), \(n<2m\) whereas a pure case has a dimension at least twice the other. This exhausts all cases. \(\square\)

## Verification

A standalone Python verifier (`verify.py`) reconstructs rook-graph open-neighborhood bitmasks and checks nonempty, distinct signatures plus the induced-degree-one condition directly; it does not use the proof's component-type recognition. It enumerates **all even-sized vertex subsets** on twelve small labeled boards, including all boards \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5)\), and compares the complete cardinality histogram to the formulas. It also checks explicit constructions at larger parameters up to \((18,18)\), horizontal-only boards up to \((12,25)\), and vertical-only boards up to \((11,5)\). The delivered `verification_output.txt` records the exact results and terminates with `VERIFICATION_OK`. Exhaustive finite checks corroborate but do **not** replace the all-parameter proof.

## Relationship to prior work

Seo and Slater (2017) introduced open-independent open-locating domination and established structural and complexity results, with applications to trees and infinite grids. Cappelle, Coelho, Foulds and Longo (first public arXiv version 14 March 2021; DMTCS 2022) further developed complexity and existence criteria for \(P_4\)-tidy graphs and complementary prisms of cographs. Their general necessary two-neighbor condition motivates Step 2 above, but does not give sufficiency on rook graphs; Step 3 supplies that missing family-specific argument. Junnila, Laihonen and Lehtilä (2018) studied other locating and identifying code parameters on rook graphs and computed their minimum sizes, while their 2023/2025 work examines direct products and three-dimensional Hamming graphs under other code definitions. Those bounds do not imply the open-neighborhood, induced-matching classification or the exact census in the theorem. Published mathematical-record searches and comparisons with separately published neighborhood-complex and identifying-code results identified no theorem that determines these \(OLD_{oind}\)-sets.

## Limitations

The statement concerns exactly two Cartesian complete-graph factors with both dimensions at least two. It does not assert anything about higher-dimensional Hamming graphs, infinite grids, or other identifying-code variants. The bibliographic comparison cannot exclude equivalent statements in unindexed or undiscovered papers; independent scientific validation has not been performed. The theorem is proved mathematically above, with bounded exact computation as an additional reproducibility check.

## References

1. S. J. Seo and P. J. Slater, *Open-independent, open-locating-dominating sets*, Electronic Journal of Graph Theory and Applications 5 (2017), 179–193, DOI:10.5614/ejgta.2017.5.2.2; https://www.ejgta.org/index.php/ejgta/article/download/210/pdf_47.
2. M. R. Cappelle, E. Coelho, L. R. Foulds, H. J. Longo, *Open-independent, open-locating-dominating sets: structural aspects of some classes of graphs*, arXiv:2103.07972 (v1, 2021-03-14), Discrete Mathematics & Theoretical Computer Science 24 (2022), DOI:10.46298/dmtcs.8440; https://arxiv.org/html/2103.07972v4.
3. V. Junnila, T. Laihonen, T. Lehtilä, *On regular and new types of codes for location-domination*, Discrete Applied Mathematics 247 (2018), 225–241, DOI:10.1016/j.dam.2018.03.050.
4. V. Junnila, T. Laihonen, T. Lehtilä, *New Optimal Results on Codes for Location in Graphs*, arXiv:2306.07862 (v1, 2023-06-13); https://arxiv.org/abs/2306.07862.
