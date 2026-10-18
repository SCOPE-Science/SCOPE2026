# Optimal Roman labelings of direct products of two complete graphs

## Finding
Let \(m,n\ge4\) be integers and let \(G_{m,n}=K_m\times K_n\) be the **direct (tensor) graph product**. Its vertices are the ordered pairs \((i,j)\in[m]\times[n]\), with two vertices adjacent precisely when both coordinates differ. A Roman dominating function is a map \(f:V(G_{m,n})\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\). Its weight is \(\omega(f)=\sum_v f(v)\).

The previously known minimum weight is \(\gamma_R(G_{m,n})=6\). Define \(N_{m,n}\) to be the number of **distinct labeled functions**, on the fixed coordinate-labeled graph, with this minimum weight. Then
\[
N_{m,n}=6\binom{m}{3}\binom{n}{3}+6\binom{m}{2}\binom{n}{2}+\mathbf{1}_{\{n=4\}}m\binom{n}{2}+\mathbf{1}_{\{m=4\}}n\binom{m}{2}.
\]
In addition, the following five geometric types are an exhaustive, pairwise disjoint classification of all minimum functions (every unspecified vertex has label \(0\)):

1. **Three matched defenders:** Label \(2\) at three cells in three distinct rows and three distinct columns. Their number is \(6\binom{m}{3}\binom{n}{3}\).
2. **Three defenders in an elbow:** In any \(2\times2\) rectangle, label \(2\) at exactly three of the four cells. Their number is \(4\binom{m}{2}\binom{n}{2}\).
3. **Two diagonal defenders:** In any \(2\times2\) rectangle, label \(2\) at one diagonal pair and label \(1\) at the opposite diagonal pair. Their number is \(2\binom{m}{2}\binom{n}{2}\).
4. **Four-column boundary:** Only if \(n=4\), choose one row, label any two cells there \(2\) and its other two cells \(1\). Their number is \(m\binom{4}{2}\).
5. **Four-row boundary:** Only if \(m=4\), choose one column, label any two cells there \(2\) and its other two cells \(1\). Their number is \(n\binom{4}{2}\).

The two-defender and three-defender counts are respectively
\[
N^{(2)}_{m,n}=2\binom{m}{2}\binom{n}{2}+\mathbf1_{\{n=4\}}m\binom n2+\mathbf1_{\{m=4\}}n\binom m2,
\quad N^{(3)}_{m,n}=6\binom{m}{3}\binom{n}{3}+4\binom{m}{2}\binom{n}{2}.
\]
In particular, as \(n\to\infty\) with any fixed \(m\ge4\), the proportion of optimal functions of type 1 tends to \(1\). The same holds when \(m\to\infty\) with fixed \(n\ge4\).

## Assumptions and scope
All graphs are finite, simple, and have named coordinate vertices. Here \(\times\) means **direct/tensor product**, not Cartesian or strong product. The domain is exactly the integer pairs \(m,n\ge4\). We count maps, not orbits of maps under graph automorphisms. The Roman rule does not require positive-label vertices to have positive neighbors, unlike *total* Roman domination.

## Proof
Write \(D=f^{-1}(2)\) and \(O=f^{-1}(1)\). A cell \((r,c)\) fails to have a defender neighbor if and only if for **every** \((i,j)\in D\), at least one of \(r=i\), \(c=j\) holds. Let \(B(D)\) be the set of such cells. A labeling is Roman precisely when \(B(D)\setminus D\subseteq O\). Its weight is \(2|D|+|O|\).

There can be no Roman function of weight below \(6\). If \(|D|=0\), all \(mn\ge16\) cells must be labeled \(1\). If \(|D|=1\), its entire row and column, except the defender itself, require label \(1\), yielding weight at least \(m+n\ge8\). If \(|D|=2\), then there are always at least two cells in \(B(D)\setminus D\): for defenders in different rows and columns these are the two cross corners of their rectangle; for defenders in the same row there are \(n-2\ge2\) other cells of that row; for defenders in the same column there are \(m-2\ge2\) other cells of that column. Consequently, two defenders require weight at least \(6\). At least three defenders cost at least \(6\) by themselves.

For \(|D|=2\) and weight \(6\), precisely two vertices carry label \(1\), hence \(|B(D)\setminus D|=2\). If the defender rows and columns differ, the two cross corners are exactly those label-\(1\) vertices (type 3). If they share a row, the row has exactly \(n-2\) required ones, so \(n=4\) and type 4 results. If they share a column, \(m=4\) and type 5 results. The preceding descriptions exhaust the two-defender case and their displayed counts follow by choosing the relevant rectangle, diagonal, row, or column.

For \(|D|=3\) and weight \(6\), \(O\) is empty, so every cell outside \(D\) must have a defender neighbor. If the three defenders lie in distinct rows and distinct columns, no row together with a column can contain all three defenders; therefore \(B(D)=\varnothing\). This gives type 1. If two defenders share a row \(r\) while the third has row different from \(r\) and column \(c\) different from both shared-row defender columns, the cell \((r,c)\notin D\) is in \(B(D)\): it is blocked from each defender. Thus this configuration is invalid. If instead the third column agrees with one shared-row defender column, the defenders form three corners of a rectangle. Here \(B(D)\) consists only of their common elbow, which itself belongs to \(D\), giving type 2. The argument with rows and columns interchanged covers configurations with a shared column. Three defenders all in one row are impossible because \(n\ge4\) leaves an undefended zero cell in that row, and similarly for three in one column. These cases cover every triple, establishing necessity and sufficiency.

A type-2 triple exists for every \(m,n\ge4\), proving that the lower bound \(6\) is attained. For type 1, choose three rows, three columns, and a bijection of the triples, giving \(6\binom m3\binom n3\). For type 2, choose a two-by-two rectangle and its missing corner, giving \(4\binom m2\binom n2\). For type 3, choose a rectangle and one of the two diagonals of defenders, giving \(2\binom m2\binom n2\). The boundary families contribute the final two terms. The families are disjoint, hence summation proves the formula. The asymptotic assertion follows because type 1 grows cubically in the increasing side length, while every other type grows at most quadratically (with the other side fixed).

## Verification
The supplied standalone `verify.py` constructs the graph using the explicit rule that both coordinates must differ, not the rectangle proof classification. For each listed board it enumerates all possible two- or three-defender placements, determines every vertex not defended by graph adjacency, supplies the forced label-one cells, and enumerates all remaining label-one choices at total weight six. The separate elementary lower bounds in the proof rule out zero and one defenders and weights below six, while four or more defenders already weigh at least eight. Running `python3 verify.py` reproduces `verification_output.txt`, with exact agreement for \((m,n)\in\{(4,4),(4,5),(4,6),(5,5),(5,6),(6,6),(7,7),(8,9)\}\). This finite computation checks these instances only; the infinite statement rests on the preceding proof.

## Relationship to prior work
Cabrera Martínez, Peterin, and Yero (arXiv:2105.10006v1, 20 May 2021; subsequently AIMS Mathematics 6, 2021, doi:10.3934/math.2021643) proved \(\gamma_R(K_m\times K_n)=6\) for \(m,n\ge4\) in Proposition 2.1. They display an elbow-shaped feasible construction and prove the numerical lower bound; the proposition does **not** classify or enumerate all optimum labelings. Our result treats this established value as a premise independently reconstructed here; the contribution is the complete classification, count, and geometric boundary behavior.

The earlier study of total Roman domination in direct products (Cabrera Martínez, Kuziak, Peterin, and Yero, arXiv:2005.13608v1; Mathematics 8 (2020), 1438) imposes the additional condition that positive vertices induce no isolated vertex. In particular, in our elbow configuration the elbow vertex is isolated within the positive support, so the total variant does not cover the enumeration here. Vemuri (arXiv:1908.02445v1, 2019) treats ordinary set domination of direct products of cliques, a different invariant without the distinction between labels \(1\) and \(2\). A two-prime unitary Cayley graph provides an equivalent description of the same graph family under coordinate relabeling; this equivalence was included in the literature search.

## Limitations
The claim is confined to two factors of orders at least four and does not assert formulas for smaller factors, higher direct products, noncomplete factors, or the full Roman domination polynomial. The result is a self-reviewed research claim, not an independent mathematical certification. Although full primary texts and mathematical-search records were compared for domination numbers and variant invariants, an unindexed equivalent optimal-labeling enumeration remains a residual bibliographic possibility.

## References
1. A. Cabrera Martínez, I. Peterin, I. G. Yero, *Roman domination in direct product graphs and rooted product graphs*, arXiv:2105.10006v1 (first publicly posted 2021-05-20); AIMS Mathematics 6 (2021), 11084–11096, doi:10.3934/math.2021643, especially Proposition 2.1.
2. A. Cabrera Martínez, D. Kuziak, I. Peterin, I. G. Yero, *Dominating the direct product of two graphs through total Roman strategies*, arXiv:2005.13608v1 (2020), Mathematics 8 (2020), 1438, doi:10.3390/math8091438.
3. H. Vemuri, *Domination in direct products of complete graphs*, arXiv:1908.02445v1 (2019).
4. E. J. Cockayne, P. M. Dreyer Jr., S. M. Hedetniemi, S. T. Hedetniemi, *On Roman domination in graphs*, Discrete Mathematics 278 (2004), 11–22.
