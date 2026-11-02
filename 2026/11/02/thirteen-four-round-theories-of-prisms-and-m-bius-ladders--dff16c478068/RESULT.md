# Thirteen four-round theories of prisms and Möbius ladders

## Finding
For integers \(n\ge3\) and \(\varepsilon\in\{0,1\}\), let \(L(n,\varepsilon)\) be the undirected simple cubic graph with vertices \((i,a)\), where \(0\le i<n\) and \(a\in\{0,1\}\). Join the two vertices in each column; join \((i,a)\) to \((i+1,a)\) for \(0\le i<n-1\); and join \((n-1,a)\) to \((0,a\oplus\varepsilon)\), where \(\oplus\) is addition modulo two. Thus \(L(n,0)\cong C_n\square K_2\) is the prism graph, and \(L(n,1)\) is the Möbius ladder on \(2n\) vertices.

Write \(G\equiv_4 H\) when \(G,H\) satisfy the same first-order sentences of quantifier rank at most four in the language of equality and undirected adjacency, without distinguished colours, columns, or rungs. Then, for all \(m,n\ge3\) and \(\varepsilon,\delta\in\{0,1\}\),
\[
L(m,\varepsilon)\equiv_4 L(n,\delta)
\quad\Longleftrightarrow\quad
\bigl(m=n<9\ \text{and}\ \varepsilon=\delta\bigr)
\ \text{or}\ \bigl(m,n\ge9\bigr).
\]
In particular, the combined family has exactly thirteen rank-four theories: twelve singleton classes for the two twists at widths three through eight, and a single common class containing every width at least nine and either twist. Every class has a representative on at most eighteen vertices; eighteen is the sharp representative ceiling **within this combined family**. In particular, a planar prism and a nonplanar Möbius ladder can be four-round equivalent already when each has eighteen vertices.

## Assumptions and scope
All graphs are finite, uncoloured, simple, loopless, undirected, and are interpreted only with the binary adjacency relation and equality. The parameters \(n,m\) denote columns, not total vertices. The assertion does not hold with column/rung predicates added, and says nothing about quantifier rank five or higher. The exact finite computation is restricted to widths three through thirty-two; the infinite range follows separately from a mathematical winning strategy.

## Proof

### 1. Signed circular-gap lemma
We prove that for every \(r\ge0\), all signed ladders \(L(n,\varepsilon)\) with \(n\ge2^{r+1}\) are equivalent in the \(r\)-round Ehrenfeucht–Fraïssé game, for both twists. We need the assertion only for \(r=4\).

Represent the \(n\) columns as a cyclic order. Transporting the layer label \(a\) once clockwise across an ordinary column-to-column gap leaves \(a\) unchanged, while transport across the seam from column \(n-1\) to column zero flips it if and only if \(\varepsilon=1\). Consequently each oriented interval between columns has a parity \(h\in\{0,1\}\), with parities adding modulo two when an interval is split.

In a partial play with \(s\) rounds remaining, put \(B_s=2^{s+1}\). Keep the distinct selected columns matched bijectively in the same cyclic order. At each selected column, keep a layer offset identifying its two row labels with the two labels in the corresponding column, so that all selected vertices in that column are matched using the same offset. For each clockwise gap between consecutive selected columns require one of the following: (i) the two gap lengths are equal and strictly less than \(B_s\), and the two column layer offsets agree with the difference of interval-transport parities; or (ii) both gap lengths are at least \(B_s\), with no parity condition. This invariant is symmetric in the two graphs. It includes repeated selections and two selected vertices in one column.

Suppose \(s\ge1\) and the next move uses a previously unselected column inside a corresponding pair of gaps. Write its two new positive subgap lengths as \(u,v\) and the old source length as \(u+v\). If the source gap is short, its target has the same length and parity constraint; choose the same offset \(u\) in the target. The parity constraint on the old gap makes the two new constraints consistent with a suitable choice of the row offset for the new column. If the source gap is long, both old gap lengths are at least \(B_s=2B_{s-1}\). If \(u<B_{s-1}\), match exactly this short left subgap; otherwise, if \(v<B_{s-1}\), match the short right subgap. In either case the other subgap remains long in both graphs, and the new row offset is chosen to satisfy the single short-gap parity constraint. If neither subgap is short, choose any position in the target leaving at least \(B_{s-1}\) columns of gap length on both sides, and choose either row offset. There cannot be two short subgaps inside a long old gap. Thus the invariant survives with \(s-1\) rounds. If the new move is in an already selected column, use its fixed row offset; no gap changes. These choices are valid regardless of which graph Spoiler played in.

At the first move, map any vertex to any vertex: there is then a single cyclic gap of length \(n\), and it is long when the current bound permits it. After at most \(r\) moves the invariant reaches \(s=0\), with \(B_0=2\). Repeated vertices and rung adjacency agree by the row-offset rule. Horizontal adjacency across different selected columns occurs exactly across an oriented gap of length one; this is a short gap and its transport parity constraint makes the two endpoints adjacent in the source exactly when their images are adjacent in the target. All equalities and adjacency atoms are therefore preserved. This wins the game. In particular, \(n,m\ge32\) implies \(L(n,\varepsilon)\equiv_4L(m,\delta)\) for either choice of twists.

### 2. Complete finite boundary
For every width \(3\le n\le32\), compute **exact** rank-four types in both graphs, including all tuples with repetitions. Define the quantifier-free atomic signature \(A_G(\bar v)\) to record equality and adjacency for every pair of positions in the ordered tuple. Recursively, for any \(s\ge0\), define
\[
T_{G,0}(\bar v)=A_G(\bar v),\qquad
T_{G,s+1}(\bar v)=\{T_{G,s}(\bar v,w):w\in V(G)\}.
\]
The root signature \(T_{G,4}(())\) completely determines agreement on all first-order sentences of quantifier rank at most four: the recursion captures every possible existential extension, its complement captures universal extensions, and Boolean connectives only compare the resulting types. In the provided implementation each type is interned **globally across both families and all tested widths**, so a shared identifier means literal equality of the complete recursive type, not coincidence of a local numbering scheme.

The file `code/orbit_types.py` computes the signatures exactly after a rigorously sound symmetry reduction: all graphs are vertex-transitive; when the first tuple vertex is normalised to zero, reversing the circular coordinate is an automorphism. Thus each ordered tuple needed by the recurrence can be replaced by the lexicographically smaller of its two reflected forms without changing its type. In addition, `code/direct_types.py` performs a separately written recursion on **all** ordered triples and all possible fourth vertices without using any symmetry quotient, and checks the overlapping range \(3\le n\le14\).

The orbit-reduced exhaustive computation identifies the rank-four root types as follows: the prism at width \(n=3,4,5,6,7,8\) has identifier \(2(n-3)\), the corresponding Möbius ladder has identifier \(2(n-3)+1\), and **both** at every width \(9\le n\le32\) have identifier 12. See `data/classification.tsv`, `data/orbit_types.txt`, and `data/direct_types.txt`. Type identifiers are only labels; equality and inequality are established by the exact signatures.

### 3. Joining the ranges
The finite calculation separates every width below nine from every other width or twist; it also shows every width nine through thirty-two has the same root type. The signed circular-gap lemma identifies every width thirty-two and above across both twists. Transitivity of \(\equiv_4\) joins the finite and infinite ranges. All thirteen classes have their smallest family members at widths three through nine. Their largest smallest order is \(2\cdot9=18\), proving sharpness within the family.

## Verification
Use Python 3 with no third-party dependencies. From the directory containing the embedded paths, run `python code/orbit_types.py 33` and `python code/direct_types.py 15`. The former exhaustively computes the thirty widths three through thirty-two, for sixty graphs total; the latter independently computes all widths three through fourteen, for twenty-four graphs. In each output row the first field is width, the next two tuples or numbers encode the prism and twisted graph's exact root types, and matching identifiers mean matching rank-four theories. The recorded outputs are included. The finite programs do **not** establish the infinite game lemma, which is proved separately above.

## Relationship to prior work
Guy and Harary, *On the Möbius Ladders* (1967), define the nonplanar graph family and prove its crossing number is one. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game* (arXiv first posted 2004-01-26), studies quantifier-rank distinctions and graph games at a general level. Brown and Hoshino, *The Ehrenfeucht–Fraïssé Game for Paths and Cycles* (2007), classify pairs of paths and pairs of cycles and develop interval methods. Neither inspected statement implies a comparison between ordinary and twisted ladders, or gives the exact width-nine threshold and thirteen logical classes. A separate literature search found topology, graph complexes, and homology results concerning the two families; those invariants have different definitions and do not entail the rank-four type classification. The local signed-gap strategy is a proof for the current objects, not an application that treats a ladder as an ordinary cycle.

## Limitations
There has been no independent expert audit of this finding. The computational check is finite only; the infinite statement is dependent on the stated signed-gap game lemma. The investigation of historical priority did not locate the full 1984 Brown–Woodrow technical report on graph Ehrenfeucht games, so a previously published equivalent theorem remains a residual possibility. The 1967 Guy–Harary article is bibliographically dated October 1967 without a verified first-public day; the earliest **day-verified** source used for the source-date field is the 2004-01-26 arXiv posting, not an invented day in 1967. The representative bound is only within the stated two graph families; no claim is made about smallest representatives among all finite graphs.

## References
1. R. K. Guy and F. Harary, “On the Möbius Ladders,” *Canadian Mathematical Bulletin* **10** (1967), 493–496, DOI: 10.4153/CMB-1967-046-4. Full text inspected for the graph definition and crossing-number theorem.
2. O. Verbitsky, “The First Order Definability of Graphs with Separators via the Ehrenfeucht Game,” arXiv:math/0401361, first posted 2004-01-26. General bounded-rank graph-logic context.
3. J. Brown and R. Hoshino, “The Ehrenfeucht–Fraïssé Game for Paths and Cycles,” *Ars Combinatoria* **83** (2007), 193–212. Publisher lists publication 2007-04-30. Main theorem and conclusion inspected.
4. J. I. Brown and R. E. Woodrow, “Ehrenfeucht Games and Graphs,” University of Calgary technical report (1984), cited by Brown and Hoshino; full text not located during this investigation.
