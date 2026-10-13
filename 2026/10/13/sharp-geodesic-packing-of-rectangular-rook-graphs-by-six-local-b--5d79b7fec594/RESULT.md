# Sharp geodesic packing of rectangular rook graphs by six local bricks

## Finding

**Theorem.** For every pair of integers \(m,n\ge 2\), the geodesic-packing number of the Cartesian product of complete graphs satisfies
\[
\operatorname{gpack}(K_m\square K_n)=\left\lfloor\frac{mn}{3}\right\rfloor.
\]
Here a geodesic packing is a collection of *pairwise vertex-disjoint maximal shortest paths*, and its number is the number of paths, not the number of vertices. Moreover, a packing attaining the formula can be constructed in \(O(mn)\) operations by a fixed family of six explicit rectangular bricks. Thus every rectangular rook graph admits a maximal-geodesic packing leaving at most two vertices unused.

## Assumptions and scope

Graphs are finite, simple and undirected. Let \(K_m\square K_n\) be the graph whose vertices are grid cells \((i,j)\in\{0,\ldots,m-1\}\times\{0,\ldots,n-1\}\); distinct cells are adjacent precisely when they have a common row or a common column. The conditions \(m,n\ge2\) are essential for the claim as stated: if one factor is a single vertex, the graph is complete and its maximal geodesics have two, rather than three, vertices.

A maximal geodesic is a shortest path not contained as a subpath in a longer shortest path. No requirement forbids edges between distinct packed paths; only their vertex sets must be disjoint. A three-cell right angle (also called an \(L\)-triple below) is a set of three corners of a \(2\times2\) rectangle. It admits a unique length-two shortest path, whose middle cell shares a row with one endpoint and a column with the other.

## Proof

**1. All maximal geodesics are \(L\)-triples.** Any two cells have distance one if they share a row or column, and distance two otherwise. Since both dimensions are at least two, any two adjacent cells can be extended to a length-two shortest path by choosing a cell in a different row and in the column of an endpoint (or vice versa). Thus no path of length at most one is maximal. Every length-two shortest path has nonadjacent endpoints, so its three cells are precisely three corners of a rectangle with two rows and two columns. Every such path is maximal because the diameter is two. Consequently, every packed path uses exactly three vertices, and
\[
\operatorname{gpack}(K_m\square K_n)\le\left\lfloor\frac{mn}{3}\right\rfloor.
\]

**2. Six optimal bricks.** In the following small arrays, equal digits mark the three cells of a packed path; a dot denotes an unused cell. Different digits mark distinct, vertex-disjoint paths. Coordinates are local to each displayed rectangular brick.

```
2 x 2       2 x 3       3 x 3
.1          122         122
11          112         113
                        323

2 x 4       3 x 4       4 x 4
..12        1234        .123
1212        1133        1122
            2244        3453
                        4455
```

In every array, each digit occurs three times and occupies an \(L\)-triple. The respective path counts are \(1,2,3,2,4,5\), which equal the floors of the brick areas divided by three. Transposing a brick also produces a valid brick with the same count. Therefore heights \(2,3,4\) are available for every brick of width \(2,3,4\), using the transposed \(2\times3\) and \(2\times4\) arrays when needed.

**3. Every height with width three.** Every integer \(m\ge2\) has a decomposition into summands of sizes two and three: use only twos if \(m\) is even, and one three plus twos if \(m\) is odd. Partition an \(m\times3\) rectangle vertically into \(2\times3\) and \(3\times3\) bricks. They yield exactly \(m\) disjoint \(L\)-triples, saturating all \(3m\) cells.

**4. Every height with width two or four.** Write \(m=3q+r\), \(r\in\{0,1,2\}\). When \(r=0\), split into \(q\) bands of height three; when \(r=1\) (necessarily \(q\ge1\) since \(m\ge2\)), split into \(q-1\) height-three bands and one height-four band; when \(r=2\), split into \(q\) height-three bands and one height-two band. Use the available transposed bricks for width two and the displayed bricks for width four. The numbers of paths are exactly
\[
\begin{array}{c|c}
\text{width}&\text{number of paths}\hline
2&\lfloor2m/3\rfloor\\
4&\lfloor4m/3\rfloor.
\end{array}
\]
Indeed, in the residue-zero case these are \(2q\) and \(4q\); in residue-one they are \(2(q-1)+2=2q\) and \(4(q-1)+5=4q+1\); in residue-two they are \(2q+1\) and \(4q+2\).

**5. Assemble an arbitrary rectangle.** Split its \(n\) columns according to the residue of \(n\) modulo three:

* If \(n=3q\), take \(q\) strips of width three.
* If \(n=3q+2\), take \(q\) strips of width three and one of width two.
* If \(n=3q+1\), necessarily \(n\ge4\); take \(q-1\) strips of width three and one of width four.

Every width-three strip contains \(m\) packed paths by step 3. By step 4, a width-two or width-four remainder contributes \(\lfloor2m/3\rfloor\) or \(\lfloor4m/3\rfloor\) paths, respectively. Summing across the disjoint strips therefore gives
\[
\begin{cases}
qm,&n=3q,\\
qm+\lfloor2m/3\rfloor,&n=3q+2,\\
(q-1)m+\lfloor4m/3\rfloor,&n=3q+1.
\end{cases}
\]
Each expression equals \(\lfloor mn/3\rfloor\). A path lying in a brick remains an \(L\)-triple in the entire graph; paths from distinct bricks use disjoint vertices. This proves the lower bound, hence equality. Traversing the strips and their fixed-size bricks emits exactly \(\lfloor mn/3\rfloor\) paths in \(O(mn)\) integer operations and output space. \(\square\)

## Verification

The accompanying standalone `verify.py` encodes the six templates as explicit triples of cell coordinates, builds the decomposition for arbitrary dimensions, and checks that every emitted triple is a length-two induced shortest path, that no two paths meet, that all coordinates lie on the board, and that the number emitted equals \(\lfloor mn/3\rfloor\). Its exact subset-dynamic-programming subroutine independently enumerates all right-angle triples for small boards and computes the actual maximum, without assuming the construction or upper-bound formula.

Running `python3 verify.py` checked all six brick maxima by exact dynamic programming; checked the construction for every \(2\le m,n\le60\) (3,481 board sizes); and compared the claimed optimum with exhaustive maximum-packing computations for 14 additional boards of at most 21 cells. The saved output is `verification_output.txt`. These finite tests are corroboration: the proof above handles all dimensions.

## Relationship to prior work

Manuel, Brešar and Klavžar introduced the maximal-geodesic-packing framework and determined the geodesic *transversal* number of square rook graphs. They explicitly derived \(\operatorname{gpack}(K_n\square K_n)\le n^2/3\) as an upper bound (Lemma 2.3 and the paragraph after Proposition 2.6), but did not construct a packing attaining the bound in every order, and did not state the rectangular equality. The result here supplies the missing matching construction and extends it to arbitrary positive dimensions at least two.

Kaneko, Kelmans and Nishimura established nearly spanning packings of arbitrary three-vertex paths in broad claw-free graphs; that invariant permits a triangle's two edges and does not require induced paths or shortest-path maximality. A rook-graph instance of their theorem alone does not yield the right-angle packings required here. Kelmans's work on induced-star packings, and Király and Szabó's induced graph-packing framework, are relevant broader theories. Their identified general results do not provide an explicit rectangular rook-graph equality in the material inspected; a formally equivalent specialized consequence in a source not read in full is a residual literature risk. The six-brick proof given above does not assume either theory.

## Limitations

The theorem covers exactly two nontrivial complete-graph factors, not products with a single-vertex factor, nor arbitrary Cartesian graph products or higher-dimensional rook graphs. It determines the largest number of packed paths and exhibits one such packing, but does not enumerate all optimum packings. Finite computations check dimensions only up to the stated sizes; they are not an exhaustive proof for all dimensions. Literature overlap beyond the inspected original article and the available abstracts of older general packing work is unresolved and should be examined before asserting priority.

## References

1. P. Manuel, B. Brešar, and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325, originally posted 27 October 2022; *Applied Mathematics and Computation* 459 (2023), 128277. https://arxiv.org/abs/2210.15325 ; https://doi.org/10.1016/j.amc.2023.128277 .
2. A. Kaneko, A. Kelmans, and T. Nishimura, *On packing 3-vertex paths in a graph*, *Journal of Graph Theory* 36 (2001), 175–197. https://doi.org/10.1002/1097-0118(200104)36:4%3C175::AID-JGT1005%3E3.0.CO;2-T .
3. A. K. Kelmans, *Optimal packing of induced stars in a graph*, *Discrete Mathematics* 173 (1997), 97–127. https://doi.org/10.1016/S0012-365X(96)00121-5 .
4. Z. Király and J. Szabó, *Induced Graph Packing Problems*, *Graphs and Combinatorics* 26 (2010), 243–257. https://doi.org/10.1007/s00373-010-0906-0 .
