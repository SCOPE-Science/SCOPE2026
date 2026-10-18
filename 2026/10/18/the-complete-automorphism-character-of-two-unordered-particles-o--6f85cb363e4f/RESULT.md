# The complete automorphism character of two unordered particles on the Pappus graph

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, realized as the incidence graph of the affine plane \(\mathbb F_3^2\): its nine point vertices are \((x,y)\), its nine line vertices are \([m,b]\), and \((x,y)\) is adjacent to \([m,b]\) exactly when \(y=mx+b\) over \(\mathbb F_3\). Let \(X=\operatorname{UConf}_2(|P|)\) be the space of unordered, distinct points on the geometric realization of \(P\). Its full graph-automorphism group \(G=\operatorname{Aut}(P)\) has order \(216\).

There are precisely thirteen conjugacy classes of \(G\). Number the classes by the reproducible ordering specified below. The complete rational second-homology character is
\[
\chi_{H_2(X;\mathbb Q)}=(27,3,-3,-3,0,0,0,3,0,0,0,0,0).
\]
Moreover \(H_1(X;\mathbb Q)\cong H_1(P;\mathbb Q)\) naturally as \(G\)-modules (dimension \(10\)), and \(H_2(X;\mathbb Z)\cong\mathbb Z^{27}\) as abelian groups. The degree-two complex character is the multiplicity-free sum of six irreducibles of degrees \(1,4,4,6,6,6\), in which the final two are conjugate over \(\mathbb Q(\sqrt3)\). Consequently the rational module is a direct sum of **five pairwise nonisomorphic rational irreducibles** of degrees \(1,4,4,6,12\). Neither \(G\) nor its index-two bipartition-preserving subgroup fixes a nonzero rational degree-two homology class.

The complete class data and characters (columns \(C_1,\ldots,C_{13}\)) are:

| Row | \(C_1\) | \(C_2\) | \(C_3\) | \(C_4\) | \(C_5\) | \(C_6\) | \(C_7\) | \(C_8\) | \(C_9\) | \(C_{10}\) | \(C_{11}\) | \(C_{12}\) | \(C_{13}\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Class size |1|9|18|18|2|12|12|18|18|36|36|18|18|
| Element order |1|2|2|2|3|3|3|4|6|6|6|12|12|
| \(\chi_{H_2}\) |27|3|-3|-3|0|0|0|3|0|0|0|0|0|
| \(\psi_1\) |1|1|-1|-1|1|1|1|1|1|-1|-1|1|1|
| \(\psi_4\) |4|0|0|-2|4|-2|1|0|0|0|1|0|0|
| \(\psi'_4\) |4|0|-2|0|4|1|-2|0|0|1|0|0|0|
| \(\psi_6\) |6|-2|0|0|-3|0|0|2|1|0|0|-1|-1|
| \(\psi_{6,+}\) |6|2|0|0|-3|0|0|0|-1|0|0|\(\sqrt3\)|\(-\sqrt3\)|
| \(\psi_{6,-}\) |6|2|0|0|-3|0|0|0|-1|0|0|\(-\sqrt3\)|\(\sqrt3\)|

Order classes by (element order, class size, value of \(\chi_{H_2}\), lexicographically smallest vertex permutation in the class). The vertex order is points \((x,y)\) at index \(3x+y\), then lines \([m,b]\) at index \(9+3m+b\), each coordinate ranging from \(0\) through \(2\). This makes the two pairs of equal-order/equal-size classes unambiguous. All entries are exact.

## Assumptions and scope
The graph is simple and finite. Configuration points are allowed anywhere on edges but must remain distinct, and particle labels are forgotten. Coefficients for the equivariant character are rational unless specified. The chain model is the two-particle unordered cubical discretization: an oriented one-cell consists of a graph edge and a disjoint stationary graph vertex; a two-cell consists of two disjoint edges, with orientations and factor ordering fixed lexicographically. Since every simple cycle has length at least six and distinct essential vertices are at least one edge apart, this cubical model is homotopy equivalent to the ordinary configuration space for two particles by the standard subdivision criterion. The automorphisms act cellularly and preserve this equivalence.

## Proof
**(1) Exact cubical chain complex.** The graph has \(18\) vertices and \(27\) edges. There are \(153\) zero-cells, \(432\) one-cells and \(297\) two-cells. Choose the natural increasing orientation for every graph edge \(a<b\). Write a one-cell \((ab,c)\), with \(c\notin\{a,b\}\), and a two-cell \((ab,cd)\) for disjoint oriented graph edges with \(ab<cd\). The boundary maps are
\[
\begin{aligned}
\partial_1(ab,c)&=(b,c)-(a,c),\\
\partial_2(ab,cd)&=(cd,b)-(cd,a)-(ab,d)+(ab,c).
\end{aligned}
\]
The verifier constructs each sparse integer column from these formulas and checks \(\partial_1\partial_2=0\). Elementary modular elimination gives
\[
\operatorname{rank}_{\mathbb F_3}\partial_1=152,\qquad
\operatorname{rank}_{\mathbb F_3}\partial_2=270.
\]
The first rank is also exactly \(152\) over \(\mathbb Q\), because the one-skeleton is connected and there are \(153\) vertices.

**(2) The natural first-homology identification.** On each one-cell \((ab,c)\), send the moving particle's oriented edge to \(ab\) in \(C_1(P)\). This \(G\)-equivariant map \(T\) sends cubical two-boundaries to zero and therefore induces \(H_1(X;\mathbb Q)\to H_1(P;\mathbb Q)\). The sparse block matrix \([\partial_1;T]\) has rank \(162\) over \(\mathbb F_3\). Therefore the restriction of \(T\) to \(\ker\partial_1\) has rank at least \(10\) over \(\mathbb Q\). Its image lies in the ten-dimensional graph cycle space. Thus \(\dim H_1(X;\mathbb Q)\ge10\). Conversely the modular rank \(270\) bounds \(\dim H_1(X;\mathbb Q)\le432-152-270=10\). Hence equality holds, \(\operatorname{rank}_{\mathbb Q}\partial_2=270\), and the map on first homology is an equivariant isomorphism. It follows that the rational second Betti number is \(297-270=27\). Since degree two has no outgoing boundary, \(H_2(X;\mathbb Z)=\ker(\partial_2:\mathbb Z^{297}\to\mathbb Z^{432})\) is free abelian of rank \(27\).

**(3) The full character.** An automorphism \(g\) acts on each cubical cell by permutation, carrying orientation signs. Write \(t_i(g)\) for the signed trace in degree \(i\), and \(e(g)\), \(v(g)\) for the signed edge trace and ordinary vertex trace on \(P\). Because the graph is connected, the first-homology character is \(\chi_{H_1}(g)=e(g)-v(g)+1\). The cellular Lefschetz identity gives
\[
\chi_{H_2}(g)=t_0(g)-t_1(g)+t_2(g)+e(g)-v(g).
\]
An exhaustive graph automorphism search yields exactly \(216\) permutations. Evaluate this finite signed-fixed-cell formula for each automorphism, and compute its conjugacy classes: there are thirteen, with the sizes, orders and traces in the table. Summing character values over all \(216\) elements yields zero, and summing over the \(108\) bipartition-preserving elements also yields zero, proving the invariant statements.

**(4) Exact irreducible decomposition.** Enumerate the thirteen class sums \(z_i=\sum_{g\in C_i}g\) and compute their products in the center of the rational group algebra using the full \(216^2\) multiplication table. For the six proposed rows \(\psi\), the numbers \(\lambda_i=|C_i|\psi(C_i)/\psi(1)\), treated exactly in \(\mathbb Q(\sqrt3)\), obey the complete central-character equations \(\lambda_i\lambda_j=\sum_k N_{ij}^{k}\lambda_k\). The six rows also have pairwise orthonormal class-function inner products, verified by exact arithmetic. They therefore are distinct irreducible complex characters. Their pointwise sum is precisely the already computed \(\chi_{H_2}\). The two nonrational six-dimensional constituents are exchanged by the Galois automorphism of \(\mathbb Q(\sqrt3)\). Since the complete representation is defined over \(\mathbb Q\) and each constituent occurs once, their sum gives an irreducible twelve-dimensional rational summand; each other constituent is individually defined over \(\mathbb Q\). This proves the decomposition.

## Verification
Run `python verify_pappus.py` with a compatible installed NetworkX package (`requirements.txt`). This standalone deterministic verifier constructs the graph, cubical chains and all \(216\) permutations. It checks every boundary composition, modular ranks over the primes \(2,3,5,101\), the augmented map rank, all signed Lefschetz character values, every conjugacy class, the full class-sum multiplication algebra, six central-character identities, orthogonality and decomposition. The exact calculations have been executed successfully. No floating-point approximations, random sampling, finite extrapolation or claimed infinite classification enter the proof.

## Relationship to prior work
Farber and Hanbury studied the topology and homology of ordered two-particle graph configuration spaces and gave structural results using graph intersection forms, but do not give the evaluated thirteen-class Pappus character. Ko and Park's work on graph braid groups addresses general homology, notably abelianization and torsion phenomena; it does not evaluate this \(216\)-element action. Published results about the Pappus graph's *independence complex*, *matching complex* and three-particle configuration space have different chain complexes or particle numbers and do not imply this full two-particle character. The novelty claimed here is solely the complete equivariant rational classification for the specified graph and configuration space, not the underlying general graph-configuration machinery.

## Limitations
The theorem treats a single canonical graph and unordered two-particle configurations. It does not determine all integral equivariant extension classes, describe the entire fundamental group, or generalize the character formula to arbitrary affine incidence graphs. A general coefficient-sensitive description of \(H_1(X;\mathbb Z)\) is not claimed. These statements have undergone a mathematical consistency and reproducibility review, not an independent audit; undiscovered literature could contain an equivalent full character.

## References
1. Michael Farber and Elizabeth Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300, first posted 13 May 2010. https://arxiv.org/abs/1005.2300
2. Ki Hyoung Ko and Hyo Won Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (2011). https://arxiv.org/abs/1101.2648
3. Maciążek and Sawicki, *Non-abelian quantum statistics on graphs*, *Communications in Mathematical Physics* (2019). https://doi.org/10.1007/s00220-019-03583-5
