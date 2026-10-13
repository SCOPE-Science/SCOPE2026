# Optimal geodesic packings in tensor products of complete graphs

## Finding
For every pair of integers \(m,n\geq 3\), the direct (categorical/tensor) product of two complete graphs has geodesic packing number
\[
\operatorname{gpack}(K_m\times K_n)=\left\lfloor\frac{mn}{3}\right\rfloor.
\]
More strongly, its vertex set can be partitioned into \(\lfloor mn/3\rfloor\) vertex-disjoint induced three-vertex paths and precisely \(mn\bmod 3\) unused vertices. Each path is a maximal shortest path in the product. An explicit constructive tiling works for every pair of dimensions and is given below.

## Assumptions and scope
All graphs are finite, undirected, and simple. The direct product \(K_m\times K_n\) has vertex set \([m]\times[n]\), where distinct \((i,j)\) and \((k,\ell)\) are adjacent if and only if \(i\neq k\) and \(j\neq\ell\). This is the **complement** of the rectangular rook graph, not its Cartesian product. A geodesic is a shortest path between its endpoints, and a maximal geodesic is one not properly contained as a subpath in another geodesic. A geodesic packing is a family of pairwise vertex-disjoint maximal geodesics.

The theorem assumes both \(m\geq3\) and \(n\geq3\). It makes no claim for products having a factor of order one or two.

## Proof
**1. All maximal geodesics have three vertices.** Two vertices differing in both coordinates are adjacent. If two distinct vertices have the same row, say \((i,j),(i,\ell)\), choose a different row \(k\) and a column \(h\notin\{j,\ell\}\). Then \((i,j),(k,h),(i,\ell)\) is a two-edge path; the case of a common column is symmetric. Hence the graph has diameter two. Furthermore, every edge \((i,j)(k,\ell)\) can be extended to the two-edge geodesic \((i,j),(k,\ell),(i,h)\) with \(h\notin\{j,\ell\}\). Thus no one-edge geodesic is maximal, whereas every two-edge geodesic is maximal because the diameter is two. Every maximal geodesic therefore occupies exactly three vertices, proving
\[
\operatorname{gpack}(K_m\times K_n)\leq\left\lfloor\frac{mn}{3}\right\rfloor.
\]

**2. Six checked local certificates.** For each array below, cells carrying the same digit constitute one path. A period is an unused cell. Rows in the display correspond to first coordinates, and columns to second coordinates. Each digit appears exactly three times. For each digit the three cells induce precisely two product-graph edges (equivalently, the unique nonadjacent pair shares a row or column, and the remaining cell differs in both coordinates from those endpoints). Thus the digit classes are vertex-disjoint maximal geodesics.

The six arrays are:

```text
3 by 3                3 by 4
1 2 2                 1 2 3 4
3 1 1                 1 2 3 4
2 3 3                 2 1 4 3

3 by 5                4 by 4
1 2 3 3 2             1 2 3 4
4 5 4 5 3             5 4 5 1
5 1 2 1 4             . 5 2 1
                      3 4 2 3

4 by 5                5 by 5
1 2 3 3 4             1 . 1 2 3
2 5 2 4 1             4 5 2 3 4
1 . 6 . 6             6 5 6 7 1
5 6 5 4 3             7 7 8 2 6
                      8 4 5 3 8
```

The \(3\)-by-\(3\), \(3\)-by-\(4\), and \(3\)-by-\(5\) arrays cover every cell. The \(4\)-by-\(4\), \(4\)-by-\(5\), and \(5\)-by-\(5\) arrays leave respectively one, two, and one cell uncovered. Transposing any array preserves the same property.

**3. Tiling every rectangle.** Each integer \(t\geq3\) can be expressed as a sum of \(3\)'s, with at most one additional summand, either \(4\) or \(5\). Explicitly, take a leading \(4\) when \(t\equiv1\pmod3\), a leading \(5\) when \(t\equiv2\pmod3\), and only \(3\)'s when \(t\equiv0\pmod3\). Partition the rows and columns of the \(m\)-by-\(n\) rectangle according to these decompositions. Each resulting block is of one of the six displayed sizes, up to transposition.

Every block with a side of length three is completely filled by geodesic triples. There is at most one block with neither side of length three. If it exists, it is a \(4\)-by-\(4\), \(4\)-by-\(5\), \(5\)-by-\(4\), or \(5\)-by-\(5\) block, leaving respectively \(1,2,2,1\) cells. The number of unused cells is therefore at most two. Because every chosen path has three vertices, its residue is necessarily \(mn\bmod3\). Translating the local paths into the full rectangle preserves adjacency and nonadjacency of each triple, hence preserves maximal-geodesic status by Step 1. This produces exactly \(\lfloor mn/3\rfloor\) pairwise disjoint maximal geodesics, attaining the upper bound. \(\square\)

## Verification
The self-contained `verify.py` reads the six hard-coded arrays, groups cells by digit, checks their induced two-edge-path property, builds and checks all rectangular packings for \(3\leq m,n\leq50\) (2,304 instances), and independently enumerates all possible induced three-vertex paths and finds optimal-size disjoint families for five small boards. To reproduce: execute `python3 verify.py` in a directory containing the standalone file. The captured output is in `verification_output.txt`.

These computational checks verify the finite certificate data and sample constructions; the arbitrary-dimension claim follows from the mathematical tiling argument, not from enumerating finitely many rectangles. An arbitrary graph's induced three-vertex-path packing may be smaller than its vertex count divided by three; the construction is essential here.

## Relationship to prior work
Manuel, Brešar and Klavžar introduced geodesic packing, established its general three-vertices-per-geodesic bound, and studied the **Cartesian** rook graph and other graph products [1]. Their bound yields the upper inequality in Step 1 but does not by itself produce the exact packing for the **direct** product considered here. Brešar, Dravec, Hedžet and Samadi studied induced matchings and edge-open packings in direct products, including products of complete graphs [2]. Neither invariant is the vertex-disjoint induced-three-vertex-path packing characterized here: edge-open packings permit larger star components and count edges, whereas this result packs three-vertex geodesics and counts paths. The displayed construction is a near-factor by induced three-vertex paths of the complement of a rectangular rook graph.

## Limitations
The theorem excludes \(m<3\) or \(n<3\), where the product may have different distance and connectivity behavior. It does not enumerate all optimum packings, classify their symmetry orbits, determine a geodesic transversal number, or extend automatically to more than two tensor factors. An equivalent induced-\(P_3\)-packing statement could exist under older tiling terminology; the literature comparison is finite rather than a proof of global novelty. The executable verifier supplies finite checks, not an independent formal proof.

## References
1. P. Manuel, B. Brešar and S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325 (first posted 2022-10-27), particularly Section 2 and the conclusions. https://arxiv.org/html/2210.15325v3
2. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first posted 2024-06-06), particularly Section 4. https://arxiv.org/html/2406.04020v2
