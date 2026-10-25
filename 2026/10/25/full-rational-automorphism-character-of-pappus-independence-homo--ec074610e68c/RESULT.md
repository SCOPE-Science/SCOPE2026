# Full rational automorphism character of Pappus independence homology

## Finding
Let \(P\) be the 18-vertex Pappus graph with LCF word \([5,7,-7,7,-7,-5]^3\). Its full automorphism group \(G=\operatorname{Aut}(P)\) has order \(216\), and \(X=\operatorname{Ind}(P)\) has reduced rational homology in exactly one degree: \(\widetilde H_4(X;\mathbb Q)\), of dimension \(10\). The **complete rational character under all 216 automorphisms** splits as
\[
\boxed{\ \widetilde H_4(X;\mathbb Q)\otimes_{\mathbb Q}\mathbb C\ \cong\ U_4\oplus U_6\ },
\]
where \(U_4\) and \(U_6\) are two distinct absolutely irreducible complex representations of dimensions \(4\) and \(6\). Their characters are rational, and the two summands are realized over \(\mathbb Q\); consequently \(\widetilde H_4(X;\mathbb Q)\cong W_4\oplus W_6\) with irreducible rational representations of dimensions \(4\) and \(6\).

The following table determines the two irreducible characters on all 13 conjugacy classes. A class is identified by its size, element order, whether it exchanges the two bipartition classes (0 or 1), and its permutation cycle type on the 18 graph vertices. Classes 8 and 11 have the same listed invariants but are **different conjugacy classes**, and happen to have equal displayed character values.

| Class | Size | Order | Exchange | Vertex cycles | \(\chi_{4}\) | \(\chi_{6}\) | Sum |
| ---: | ---: | ---: | ---: | :--- | ---: | ---: | ---: |
| 1 | 18 | 2 | 0 | \(1^4 2^7\) | 2 | 0 | 2 |
| 2 | 9 | 2 | 0 | \(1^6 2^6\) | 0 | -2 | -2 |
| 3 | 36 | 6 | 0 | \(1\,2\,3\,6^2\) | -1 | 0 | -1 |
| 4 | 12 | 3 | 0 | \(1^3 3^5\) | 1 | 0 | 1 |
| 5 | 18 | 2 | 1 | \(2^9\) | 0 | 0 | 0 |
| 6 | 18 | 4 | 1 | \(2^3 4^3\) | 0 | 2 | 2 |
| 7 | 36 | 6 | 1 | \(6^3\) | 0 | 0 | 0 |
| 8 | 18 | 12 | 1 | \(6\,12\) | 0 | -1 | -1 |
| 9 | 12 | 3 | 0 | \(3^6\) | -2 | 0 | -2 |
| 10 | 18 | 6 | 0 | \(3^2 6^2\) | 0 | 1 | 1 |
| 11 | 18 | 12 | 1 | \(6\,12\) | 0 | -1 | -1 |
| 12 | 2 | 3 | 0 | \(3^6\) | 4 | -3 | 1 |
| 13 | 1 | 1 | 0 | \(1^{18}\) | 4 | 6 | 10 |

In particular, the trivial representation is absent. The natural quotient satisfies
\[
\boxed{\ \widetilde H_*(X/G;\mathbb Q)=0.\ }
\]
This quotient statement concerns rational homology, not integral homology or contractibility.

## Assumptions and scope
The graph vertices are \(0,\ldots,17\). For each \(i\), include the edges \(\{i,i+1\}\) and \(\{i,i+c_i\}\), with indices modulo \(18\) and \((c_i)=[5,7,-7,7,-7,-5]^3\). Duplicate edges are identified. This produces a cubic bipartite graph with 27 edges. The independence complex contains precisely vertex sets with no graph edge. A graph automorphism acts on oriented simplicial chains by the sign of the induced vertex permutation. The two bipartition classes are even and odd labels in this chosen LCF model.

All character and module assertions are over characteristic zero. The previously established nonequivariant homotopy equivalence \(X\simeq\bigvee^{10}S^4\) is used solely as context; it is not a novel conclusion here.

## Proof
**1. Homological concentration.** Exhaustive enumeration from the explicit adjacency masks yields 2,598 augmented faces, including the empty set. The nonempty face counts in dimensions zero through eight are
\[
(18,126,438,801,756,348,90,18,2).
\]
The exact augmented mod-two boundary ranks from \(\partial_k\) (where \(k\) is face cardinality, so \(\partial_1\) maps vertices to the empty face) are
\[
(1,17,109,329,472,274,74,16,2).
\]
Thus mod-two reduced homology is zero except for dimension four, where it has dimension ten. The universal coefficient theorem and finite generation imply rational homology vanishes in every other degree. The alternating sum of face numbers gives reduced Euler characteristic ten, forcing rational fourth Betti number ten.

**2. Exact equivariant Lefschetz character.** Enumerate all 216 adjacency-preserving bijections by exhaustive backtracking, then conjugate every element to obtain the 13 conjugacy classes. Fix \(g\in G\). Partition its 18 vertex labels into permutation cycles; discard each cycle whose vertices are not an independent set of \(P\). Form the conflict graph \(Q_g\) on the remaining cycles, connecting two cycles if any original edge joins them. Let
\[
I(Q_g,z)=\sum_{S\in\operatorname{Ind}(Q_g)}z^{|S|}.
\]
A nonempty simplex fixed setwise by \(g\) consists of whole permutation cycles. An included cycle of length \(j\) contributes simplicial orientation sign \((-1)^{j-1}\) and alternating-chain sign \((-1)^j\), whose product is \(-1\). Accounting for the empty face at reduced degree minus one gives
\[
\operatorname{tr}\bigl(g\mid\widetilde H_4(X;\mathbb Q)\bigr)
=\widetilde L(g;X)=-I(Q_g,-1).
\]
The first equality uses the homology concentration and the fact that its degree is even. This formula determines the character of **every** group element, not only selected generators or involutions. The checker computes the orbit-polynomial formula recursively and independently recomputes each of the 216 traces by explicit signed fixed-simplicial-face enumeration.

**3. Irreducibility and rational splitting.** Tabulate the resulting class-constant character as the last column above. The two candidate class functions in columns \(\chi_4\) and \(\chi_6\) add to it. For each candidate \(\psi\) of degree \(d\in\{4,6\}\), exact rational arithmetic verifies its norm-one character identity
\[
\frac1{216}\sum_C|C|\psi(C)^2=1,
\]
as well as its zero inner product with the trivial character. More decisively, define the central character of the class sum \(K_C\) as \(\lambda_\psi(K_C)=|C|\psi(C)/d\). For all \(13^2\) pairs of conjugacy classes \(C,D\), the checker multiplies their class sums in the concrete 216-element group and verifies exactly that \(\lambda_\psi(K_CK_D)=\lambda_\psi(K_C)\lambda_\psi(K_D)\). These are unital algebra homomorphisms from the center of \(\mathbb C[G]\); semisimplicity identifies them with genuine irreducible central characters. The degrees at the identity are four and six, and both functions are integer valued. Their sum is the character on the rational ten-dimensional homology with multiplicity one each, so rationality and multiplicity one force Schur index one and descent to irreducible rational representations, as claimed.

**4. Quotient.** The average of the 216 computed character values is zero. Consequently there are no invariant reduced rational homology classes. In characteristic zero, cellular averaging (or the equivariant transfer argument after suitable subdivision) identifies rational homology of a finite-group quotient with the invariant rational homology, proving the stated vanishing.

## Verification
Run `python3 verify_pappus_full_aut.py` with Python 3.10 or later, standard library only. The program independently reconstitutes the 18-vertex graph, enumerates all 2,598 augmented faces, computes nine full mod-two boundary ranks, constructs all 216 automorphisms and 13 conjugacy classes, checks every signed Lefschetz trace by two distinct methods, and certifies both irreducible class-algebra characters using exact fractions. Completion markers are `PAPPUS_FULL_216_AUTOMORPHISM_CHARACTER_VERIFIED` and `PAPPUS_DIRECT_SIGNED_TRACE_ALL_216_VERIFIED`.

The finite enumeration is exhaustive for this explicitly defined graph. Its complete source is provided and has no hidden data files. No claim is made for a family of larger incidence graphs.

## Relationship to prior work
Tsukuda proves a general Alexander-duality relation for independence complexes of incidence graphs, applicable as structural background because the Pappus graph is a Levi graph. Berghoff develops a general spectral sequence for graph independence homology, with examples on paths and cycles; that work does not compute the Pappus automorphism-group character.

Two previously published exact Pappus computations are particularly close and must be separated from the new claim. *The Pappus independence complex is a wedge of ten four-spheres* establishes the nonequivariant homotopy type, and *Order-three symmetry on Pappus independence homology* establishes only the \(C_3\)-character for \(r(i)=i+6\pmod{18}\), namely \((10,-2,-2)\). That restriction does not determine the complete 13-class character or the distinct four- and six-dimensional irreducible constituents. The present character is consistent with that earlier cyclic restriction. Search results cannot exclude otherwise unindexed equivalent work.

## Limitations
The classification is exact for this single finite Pappus graph and its full 216-element automorphism group. It does not identify the integral \(\mathbb Z[G]\)-lattice, prove integrally acyclic symmetry quotients, assert a new nonequivariant sphere-wedge result, or extend to all Levi graphs. The numerical characters depend on the explicit LCF model, although the representation itself is graph-invariant up to isomorphism. Possible obscure or unindexed equivalent computations remain an originality risk.

## References
1. Shuichi Tsukuda, “Independence complexes and incidence graphs,” *Contributions to Discrete Mathematics* 12 (2017), 28–46, DOI: 10.55016/ojs/cdm.v12i1.62277 (published 2017-09-27).
2. Marko Berghoff, “On the homology of independence complexes,” arXiv:2008.06267 (first posted 2020-08-14), *Combinatorial Theory* 2 (2022).
3. “The Pappus independence complex is \(\bigvee^{10}S^4\),” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-pappus-independence-complex-is-bigvee-10-s-4--81f85f0cc9c6 .
4. “Order-three symmetry on Pappus independence homology,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31 .
5. Wolfram MathWorld, “Pappus Graph,” https://mathworld.wolfram.com/PappusGraph.html .
