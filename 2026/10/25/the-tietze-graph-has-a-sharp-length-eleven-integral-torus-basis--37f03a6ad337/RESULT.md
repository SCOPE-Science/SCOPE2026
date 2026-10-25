# The Tietze graph has a sharp length-eleven integral torus basis and an index-two parity obstruction

## Finding
Let \(G\) be the twelve-vertex Tietze graph, constructed by replacing vertex \(0\) of the standard Petersen graph with a triangle, joining its three vertices to the former neighbors \(1,4,5\) in that order. Let \(X=\operatorname{UConf}_2(|G|)\) be the ordinary unordered configuration space of two distinct points of the geometric realization of \(G\). An *embedded product torus* is the image of the product of two vertex-disjoint simple cycles under their canonical inclusion in \(X\). Its *total length* is the sum of the edge lengths of the two cycles.

Then
\[
H_2(X;\mathbb Z)\cong\mathbb Z^9.
\]
The graph has exactly \(27\) unordered vertex-disjoint simple-cycle pairs. Among these, the classes of total length at most \(10\) generate a rank-four subgroup, but the classes of total length at most \(11\) generate *all* of \(H_2(X;\mathbb Z)\). In particular, the six triangle–pentagon tori together with the six pentagon–hexagon tori contain an integral basis consisting of three of the former and all six of the latter. Thus \(11\) is the sharp total-length cutoff for generating integral second homology using disjoint-simple-cycle product tori.

There is a further integral distinction: the ten classes consisting of all four triangle–hexagon and all six pentagon–hexagon tori span a subgroup \(L\) such that
\[
H_2(X;\mathbb Z)/L\cong\mathbb Z/2\mathbb Z.
\]
Adding the class of **any one** of the six triangle–pentagon tori to \(L\) yields all of \(H_2(X;\mathbb Z)\).

## Assumptions and scope
The graph is the simple cubic graph on \(\{0,\ldots,11\}\) with its entire sorted edge list

```text
(0,1) (0,5) (0,9) (1,2) (1,6) (2,3)
(2,7) (3,8) (3,10) (4,6) (4,7) (4,11)
(5,7) (5,8) (6,8) (9,10) (9,11) (10,11)
```

This labeling agrees with the explicitly reconstructed Petersen-to-Tietze operation in `verify_tietze.py`. All cycles are simple and all disjointness is vertex disjointness, not just edge disjointness. The total-length threshold applies to embedded product tori from these cycle pairs, not to arbitrary singular two-cycles. A sign choice in orienting a cycle changes only the sign of its torus class and does not change any integral lattice.

For this graph, every path between distinct essential vertices contains at least one edge, and every homotopically essential closed path has at least three edges. The unlabeled two-particle stable-equivalence theorem of Prue–Scrimshaw consequently identifies the ordinary space with the finite unordered cubical deleted-product model used below. The simple graph has no loops or multiple edges, so no additional subdivision is required for two particles.

## Proof
**Cubical chains.** Let \(V\) and \(E\) be the ordered vertex and edge sets. The unordered two-particle deleted product has zero-cells \(\{u,v\}\) for distinct vertices, one-cells \((u,e)\) when \(u\notin e\), and two-cells \((e,f)\) when edges \(e<f\) have disjoint endpoints. There are exactly \((66,180,117)\) cells in dimensions zero, one and two. Write \(e=(a,b)\) and \(f=(c,d)\) in increasing endpoint order. With the orientation \(e\times f\), its cellular boundary is
\[
\partial_2(e,f)=(b,f)-(a,f)-(d,e)+(c,e).
\]
This formula agrees with the quotient orientation: reversing the order of the two one-dimensional factors introduces a minus sign. Direct construction gives \(\partial_1\partial_2=0\), and exact elimination modulo \(101\) yields \(\operatorname{rank}_{\mathbb F_{101}}\partial_2=108\).

**Geometric cycles.** Orient each simple cycle by first choosing its lexicographically smaller vertex traversal starting at the smallest vertex. The external product of two vertex-disjoint cycles is a cellular two-cycle with a \(\pm1\) coefficient at each ordered pair of its constituent edges; when the edge order in a two-cell is reversed, the coefficient changes sign. Exhaustive cycle enumeration yields the pair multiplicities

| Cycle lengths | Number of pairs |
|---|---:|
| \((3,5)\) | 6 |
| \((3,6)\) | 4 |
| \((3,8)\) | 3 |
| \((3,9)\) | 2 |
| \((5,6)\) | 6 |
| \((5,7)\) | 6 |

The sum is \(27\). Every enumerated product class has zero cellular boundary.

**Integral basis certificate.** Sort all simple cycles first by length and then lexicographically. Sort disjoint cycle pairs lexicographically by their two cycle indices, numbered from zero, and sort the cellular two-cells lexicographically by their two oriented edges, again numbered from zero. The product cycles with pair indices

```text
0 2 3 15 17 19 21 23 25
```

have a signed \(9\)-by-\(9\) coordinate minor in two-cell rows

```text
0 2 4 10 13 15 47 67 95
```

with exact determinant \(-1\). The first three selected classes are triangle–pentagon products, and the other six are the entire pentagon–hexagon family. Hence their \(\mathbb Z\)-span is primitive in the ambient free two-chain group, and it has rank \(9\). Since these are two-cycles, the rational rank of \(\partial_2\) is at most \(117-9=108\); the modular rank above forces equality. Therefore \(\ker\partial_2\) has rank exactly nine. Its primitive rank-nine sublattice generated by the selected cycles must be the entire kernel: an inclusion of two rank-nine lattices with nontrivial finite quotient would contradict primitivity in the full chain group. There are no cellular three-cells, so this kernel is \(H_2(X;\mathbb Z)\).

**Sharp length cutoff.** All disjoint cycle pairs with total length at most ten belong to the \((3,5)\) and \((3,6)\) families, ten pairs in total. Exact rational elimination on their signed two-chain vectors gives rank four, which proves that they cannot generate rank-nine second homology. At total length eleven the \((3,8)\) and \((5,6)\) families join the list, which already contains the nine integral basis classes certified above. Thus the threshold is precisely eleven.

**Parity quotient.** Use the nine row indices of the unimodular minor as integral coordinates on \(H_2(X;\mathbb Z)\); they are integral coordinates because the selected basis has minor determinant \(-1\). The nine-by-ten coordinate matrix for all four \((3,6)\) and all six \((5,6)\) classes has ten maximal minors, indexed by the omitted column, equal to

```text
 2  2 -2 -2 -2  2  0 -2  0  0
```

Their greatest common divisor is two, so the column lattice has index two in the rank-nine integral homology lattice. In the same ordered nine cellular coordinates, the mod-two functional with coefficient vector \((1,1,1,1,1,1,0,1,1)\) vanishes on all ten chosen-family torus classes and evaluates to one on each of the six triangle–pentagon classes. Correspondingly, the ten-column matrix has rank eight modulo two, and adjoining **each** of the six \((3,5)\) columns separately raises that rank to nine. Thus every triangle–pentagon class represents the nonzero coset of this index-two subgroup and kills the quotient.

## Verification
Run `python3 verify_tietze.py` with Python 3 and no external packages. The program reconstructs the labeled graph from a Petersen graph, enumerates all simple cycles by a complete canonical depth-first traversal, assembles the entire signed cubical chain complex, verifies every cellular boundary composition and product-torus cycle, computes the modular boundary rank and exact rational short-family rank, and checks the displayed integer minors using fraction-free Bareiss elimination. For the index-two quotient it independently checks the gcd of all ten maximal minors and the mod-two rank change after adding each triangle–pentagon class. The expected final marker is `VERIFY_OK_TIETZE_INTEGRAL_TORUS_LENGTH_THRESHOLD`.

## Relationship to prior work
Barnett–Farber (2009) developed the intersection form for **ordered** two-point graph configurations and a planar cohomology analysis. Farber–Hanbury (2010) analyzed ordered two-point homology and mature graphs. Prue–Scrimshaw established the subdivision bounds allowing the finite discrete model to compute the actual unordered space. An–Knudsen's planar second-homology generator theorem does not cover the nonplanar Tietze graph, which contains the Petersen graph as a minor by contracting its distinguished triangle. Those sources do not state the present Tietze-specific length cutoff, nine-class primitive basis, or parity index. A Petersen-graph two-particle homology computation concerns a different graph and does not imply these Tietze integral cycle-length lattices.

## Limitations
The result is an exact finite-graph statement, not a formula for arbitrary triangle expansions or for configurations of three or more particles. It does not classify all singular representatives of second homology; the minimum length is only among the specified embedded product tori. The exact enumeration is self-contained and exhaustive for this twelve-vertex labeled graph. Specialized equivalent computations in unpublished or unindexed literature, including a 2010 doctoral thesis whose complete text was not retrievable during comparison, cannot be excluded. No independent mathematical audit has been performed.

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, Algebraic & Geometric Topology **9** (2009), 593–624. arXiv:0903.2180, https://arxiv.org/abs/0903.2180.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, Algebraic & Geometric Topology **10** (2010), 2203–2227. arXiv:1005.2300, https://arxiv.org/abs/1005.2300.
3. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, https://arxiv.org/abs/0909.5511 (Theorem 3.2).
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, Journal of Topology **15** (2022), 666–691. arXiv:2008.10371, https://arxiv.org/abs/2008.10371.
5. K. Barnett, *The Configuration Space of Two Particles Moving on a Graph*, doctoral thesis, Durham University (2010), https://etheses.durham.ac.uk/293/ (abstract inspected; complete thesis not retrieved).
