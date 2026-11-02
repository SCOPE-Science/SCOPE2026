# Complete super-domination polynomial and minimum-set rigidity of rectangular rook graphs

## Finding

For every pair of integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\), whose vertices are the cells of an \(m\)-by-\(n\) board and where distinct cells are adjacent exactly when they share a row or column. A set \(D\subseteq V(R_{m,n})\) is **super dominating** when each vertex \(u\notin D\) has a neighbor \(v\in D\) for which \(N(v)\cap(V\setminus D)=\{u\}\).

Let the **omission enumerator** be
\[
P_{m,n}(z)=\sum_{D\text{ super dominating}}z^{mn-|D|}.
\]
Define the explicitly computable polynomial
\[
C_{m,n}(z)=m!n!\,[x^m y^n]\,(e^x-1)(e^y-1)
\exp\!\left(x(e^{yz}-1)+y(e^{xz}-1-xz)\right),
\]
where coefficient extraction is in formal power series in \(x,y\), with coefficients in \(\mathbb Q[z]\). Write \(\left\{\begin{smallmatrix} a\\b\end{smallmatrix}\right\}\) for a Stirling number of the second kind, interpreted as zero for \(b>a\). Then **every** super-dominating set of the rook graph is counted by
\[
\boxed{P_{m,n}(z)=C_{m,n}(z)
+\left(n^m-n!\left\{\begin{smallmatrix}m\\n\end{smallmatrix}\right\}\right)z^m
+\left(m^n-m!\left\{\begin{smallmatrix}n\\m\end{smallmatrix}\right\}\right)z^n.}
\]
In particular, the ordinary cardinality polynomial of selected sets is \(z^{mn}P_{m,n}(z^{-1})\).

In the stable range \(m,n\ge5\), the maximum possible omission size is \(m+n-4\) (equivalently \(\gamma_{sp}(R_{m,n})=mn-m-n+4\), a **previously known** value). There are precisely
\[
\boxed{m(m-1)n(n-1)}
\]
minimum super-dominating sets. Every one is the complement of exactly one configuration
\[
U=\{(r_*,j):j\notin\{c_*,c_0\}\}
\cup\{(i,c_*):i\notin\{r_*,r_0\}\},
\]
where \(r_*\ne r_0\) are ordered rows and \(c_*\ne c_0\) are ordered columns. This describes every optimum, including its labelled count.

## Assumptions and scope

All graphs are finite, simple, and undirected. Both factors have at least two vertices. The open neighborhood \(N(v)\) excludes \(v\). The empty omitted set, corresponding to selecting every vertex, is super dominating and supplies the constant term \(1\) of \(P_{m,n}\). Rows, columns, and board cells are labeled. In the minimum-set classification \(m,n\ge5\); the polynomial formula itself covers all \(m,n\ge2\).

Associate with any omitted set \(U=V\setminus D\) the bipartite incidence graph \(B(U)\): its row vertices and column vertices are the two parts, and it contains edge \(ij\) exactly when cell \((i,j)\) is omitted. A row or column is **empty** when it is isolated in \(B(U)\). A bipartite **star forest** is a disjoint union of stars (including single edges) and isolated vertices.

## Proof

**Step 1: Exact local witness condition.** For a selected cell \((i,b)\in D\), its omitted neighbors comprise the other omitted cells in row \(i\) and the omitted cells in column \(b\). These two collections are disjoint because \((i,b)\notin U\). Therefore \((i,b)\) privately witnesses an omitted cell \((i,j)\) exactly when row \(i\) contains only that omitted cell and column \(b\) is empty. Symmetrically, a selected cell \((a,j)\) witnesses \((i,j)\) exactly when column \(j\) contains only that omitted cell and row \(a\) is empty. Hence \(D\) is super dominating if and only if every edge \((i,j)\in E(B(U))\) satisfies at least one of
\[
\deg_B(i)=1\text{ and some column is isolated},\qquad
\deg_B(j)=1\text{ and some row is isolated}.
\]
The claim is also vacuously valid for \(U=\varnothing\).

**Step 2: Exhaustive, disjoint structural trichotomy.** When both sides have an isolated vertex, the criterion requires each edge of \(B(U)\) to have a degree-one endpoint. A nontrivial connected graph with this property is a star: if an edge joined two vertices each of degree at least two, the condition would fail; equivalently, if a component had two distinct vertices of degree at least two, a shortest path between them would contain an edge with neither endpoint of degree one. Thus \(B(U)\) is a star forest with an isolated row and an isolated column. If columns have an isolate but rows do not, only the first witness condition can hold and every row has degree exactly one. This is a function from the \(m\) rows to the \(n\) columns, and the isolated-column requirement says the function is nonsurjective. If rows have an isolate but columns do not, analogously every column has degree one and the corresponding function from the \(n\) columns to the \(m\) rows is nonsurjective. If neither side has an isolate, no nonempty omitted set can satisfy the witness condition. These cases partition all admissible \(U\).

**Step 3: Count the both-isolated star forests.** Use labeled combinatorial exponential generating functions, with \(x\) marking rows, \(y\) marking columns, and \(z\) marking edges. The isolated rows and columns contribute \((e^x-1)(e^y-1)\), since both types must occur. Each nontrivial star has one of two mutually exclusive descriptions: a row center with \(d\ge1\) column leaves, giving \(x(e^{yz}-1)\), or a column center with \(d\ge2\) row leaves, giving \(y(e^{xz}-1-xz)\). The second family excludes \(d=1\) to prevent counting an isolated edge twice. Taking the labeled set of star components gives the exponential displayed in the definition of \(C_{m,n}\). Coefficient extraction and the factors \(m!n!\) count labeled incidence graphs exactly once.

**Step 4: Count the remaining two classes.** There are \(n^m\) functions from the rows to columns. The surjective ones number \(n!\left\{\begin{smallmatrix}m\\n\end{smallmatrix}\right\}\), so the nonsurjective choices contribute the first correction at exactly \(m\) omitted cells. Interchanging the parts gives the other correction at \(n\) omissions. By Step 2, the three families are disjoint and exhaustive, proving the polynomial identity.

**Step 5: Classify every optimum for \(m,n\ge5\).** The two function families omit \(m\) or \(n\) cells, strictly fewer than \(m+n-4\). In a both-isolated star forest, let \(p\le m-1\) and \(q\le n-1\) be its nonisolated row and column counts and \(k\) its number of nontrivial star components. Such a forest has \(p+q-k\) edges. If \(k\ge2\), this is at most \(m+n-4\), with equality only if \(k=2,p=m-1,q=n-1\). If \(k=1\), the single star has at most \(\max\{m-1,n-1\}<m+n-4\) edges; if \(k=0\), it has none. At equality with \(k=2\), at least four row vertices and four column vertices are nonisolated. Both components therefore cannot be row-centered, and both cannot be column-centered. Nor can either be a single edge, which would leave at most two nonisolated vertices on one side. Consequently one component is a row-centered star with \(n-2\) column leaves, and the other a column-centered star with \(m-2\) row leaves. They avoid each other's centers; one row and one column are isolated. This is exactly the displayed \(U\) template. Conversely each template satisfies Step 2 and has \(m+n-4\) edges. Its two centers and two isolated coordinates are uniquely recoverable for \(m,n\ge5\), yielding exactly \(m(m-1)n(n-1)\) distinct labeled optima. Their complementary selected sets have cardinality \(mn-m-n+4\). QED.

## Verification

The self-contained `verify_rook.py` uses an independent neighborhood-bitmask implementation of the original super-domination definition. It exhaustively checks all omitted subsets for board sizes \((2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4)\), matching every coefficient with a separate labeled-star-forest recurrence plus inclusion-exclusion implementation of \(C_{m,n}\). It also checks all \(\binom{25}{6}=177100\) six-cell omissions on the five-by-five board: precisely \(400\) are valid, and all match the proposed two-star construction. Symbolic polynomial computations verify the extremal coefficient formula for \((5,5),(5,6),(6,6),(5,8),(8,5)\). The program prints `VERIFY_OK` on complete success. Run with `python3 verify_rook.py` in the directory containing the file. The general theorem rests on Steps 1–5 rather than finite enumeration.

For illustration,
\[
P_{3,3}(z)=1+9z+36z^2+42z^3,\qquad
P_{5,5}(z)=1+25z+300z^2+1900z^3+6550z^4+10810z^5+400z^6.
\]

## Relationship to prior work

Klein, Rodríguez-Velázquez, and Yi, *On the super domination number of graphs* (first available as arXiv:1705.00928 on 2017-05-02), Theorem 30, already determine \(\gamma_{sp}(K_m\square K_n)\) for \(m,n\ge4\), including the scalar value quoted above. The present result **does not** claim this value as new. Their proof supplies a particular optimum and an upper bound on omissions; it does not enumerate super-dominating sets of all cardinalities or classify every optimum. Ghanbari, Jäger, and Lehtilä, *Super Domination: Graph Classes, Products and Enumeration* (arXiv:2209.01795), Section 6, count minima for other graph families such as complete graphs, complete bipartite graphs, friendship graphs, paths and cycles, not rectangular rook graphs. Mertens, *Domination Polynomial of the Rook Graph* (2024), gives the polynomial for **ordinary** domination, which is a weaker property. Kaidash's *Super domination polynomial of a graph* (2024) develops the polynomial invariant and examples on other graph families; its full text was inaccessible in the available sources, leaving a documented publication-priority risk. The assessed refinement is the precise two-parameter full enumerator and all-minimum rigidity statement.

## Limitations

The EGF counts the specific super-domination predicate stated above; it does not classify all minimum sets for boundary regimes with \(\min\{m,n\}<5\), though the complete polynomial determines their numbers. The optimal rigidity classification is restricted to \(m,n\ge5\). No formula for arbitrary Cartesian graph factors is asserted. The 2024 Kaidash chapter could not be inspected in full; although accessible summaries list different graph families, definitive literature priority is not established. Finite program checks do not certify the infinite theorem independently.

## References

1. D. J. Klein, J. A. Rodríguez-Velázquez and E. Yi, *On the super domination number of graphs*, arXiv:1705.00928, first version 2017-05-02, especially Theorem 30. https://arxiv.org/pdf/1705.00928
2. N. Ghanbari, G. Jäger and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795 (2022), especially Section 6. https://arxiv.org/pdf/2209.01795
3. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), article 24.3.7. https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.pdf
4. P. A. Kaidash, *Super domination polynomial of a graph*, Communications in Computer and Information Science 2239 (2024), 85–95. DOI 10.1007/978-3-031-73365-9_6; abstract and listed examples: https://sciact.math.nsc.ru/public/article/5672/en
