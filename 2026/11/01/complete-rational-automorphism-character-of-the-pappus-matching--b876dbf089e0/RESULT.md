# Complete rational automorphism character of the Pappus matching complex

## Finding
Let \(P\) be the Pappus cubic graph on the vertex set \(\{0,\ldots,17\}\), specified by the Hamiltonian cycle and the LCF chords \([5,7,-7,7,-7,-5]^3\). Let \(K=\mathcal M(P)\) be the ordinary matching complex: its vertices are the 27 edges of \(P\), and its faces are the pairwise vertex-disjoint edge sets. Its full automorphism group \(G=\operatorname{Aut}(P)\) has order 216.

**The complete rational homology character** \(\chi(g)=\operatorname{tr}(g\mid\widetilde H_5(K;\mathbb Q))\) is specified by the following table. Each cycle type is written as a multiset of cycle lengths on, respectively, the 18 original graph vertices and the 27 graph edges; exponent zero is omitted. Every group element belongs to exactly one row, and the row counts total 216. The last column is its character value.

| Order | Graph-vertex cycle type | Graph-edge cycle type | Number of elements | \(\chi\) |
| ---: | :--- | :--- | ---: | ---: |
| 1 | \(1^{18}\) | \(1^{27}\) | 1 | 40 |
| 2 | \(1^6 2^6\) | \(1^3 2^{12}\) | 9 | 0 |
| 2 | \(1^4 2^7\) | \(1^3 2^{12}\) | 18 | \(-4\) |
| 2 | \(2^9\) | \(1^3 2^{12}\) | 18 | 4 |
| 3 | \(1^3 3^5\) | \(3^9\) | 12 | 1 |
| 3 | \(3^6\) | \(3^9\) | 14 | 4 |
| 4 | \(2^3 4^3\) | \(1^3 4^6\) | 18 | 0 |
| 6 | \(1\,2\,3\,6^2\) | \(3\,6^4\) | 36 | \(-1\) |
| 6 | \(3^2 6^2\) | \(3\,6^4\) | 18 | 0 |
| 6 | \(6^3\) | \(3\,6^4\) | 36 | \(-2\) |
| 12 | \(6\,12\) | \(3\,12^2\) | 36 | 0 |

All other reduced rational homology groups vanish, and \(\dim_{\mathbb Q}\widetilde H_5(K;\mathbb Q)=40\). The full invariant subspace vanishes because the sum of all 216 character values is zero. Consequently, for the ordinary topological quotient,
\[
\widetilde H_*(K/G;\mathbb Q)=0.
\]
This is a classification of the **full character**, not a claim about an integral representation lattice or an equivariant wedge decomposition.

## Assumptions and scope
The LCF notation means that the eighteen vertices carry the cycle edges \(\{i,i+1\bmod18\}\), together with edges \(\{i,i+s_i\bmod18\}\), where the eighteen-entry sequence \((s_i)\) is three copies of \((5,7,-7,7,-7,-5)\). Graph edges are undirected and duplicates removed. There are exactly 27 distinct edges. The matching complex uses **ordinary** disjoint graph-edge matchings, not induced matchings, maximal-matchings-only complexes, or configuration spaces.

\(G\) acts simplicially by permuting original graph vertices, thus graph edges and faces. Homology is reduced rational simplicial homology; the quotient means the ordinary orbit space of the geometric realization. No assertion is made for another 18-vertex graph or arbitrary cubic graphs.

## Proof
**1. Rational homology is concentrated in degree five.** Exact recursive enumeration of all matching faces, including the empty face, gives counts by matching cardinality \(0\) through \(9\):
\[
(1,27,297,1719,5643,10557,10737,5319,1026,42).
\]
The full reduced mod-two boundary-rank vector, with source matching cardinality \(1\) through \(9\), is
\[
(1,26,271,1448,4195,6362,4335,984,42).
\]
Each rank is obtained by exact bitset elimination on the full augmented simplicial boundary; the complete generator is supplied in `verify_pappus_mod2.py`. The reduced mod-two Betti vector in simplex degrees zero through eight is \((0,0,0,0,0,40,0,0,0)\). A finitely generated integral homology group has rational rank no larger than its mod-two homology dimension (by universal coefficients). Thus all reduced rational groups except possibly degree five vanish. The exact alternating face count is \(40\), giving reduced Euler characteristic \(-40\), so \(\dim\widetilde H_5(K;\mathbb Q)=40\).

**2. Exhaustion of the symmetry group.** Enumerate bijections of the 18 graph vertices by incremental partial assignments; admit an extension only when adjacency **and nonadjacency** are preserved for every already assigned vertex pair. At the complete-assignment stage every map is a graph automorphism. The procedure generates each possible automorphism exactly once, obtaining 216. It is exhaustive because any automorphism restricts to an admissible partial assignment at every stage. For each map, form its induced permutation on the 27 graph edges and compute its two cycle types.

**3. Signed Lefschetz formula.** Fix an automorphism \(g\), and let a matching \(M\) fixed setwise have \(k\) edges. Its oriented simplex contributes \((-1)^{k-1}\operatorname{sgn}(g\mid M)\) to the ordinary alternating chain trace. After subtracting the augmentation in reduced degree \(-1\), this gives
\[
\widetilde L(g)=-\sum_{M\colon gM=M}(-1)^{|M|}\operatorname{sgn}(g\mid M),
\]
including the empty matching with sign one. Because rational reduced homology is concentrated in **odd** degree five, \(\widetilde L(g)=-\chi(g)\), hence
\[
\chi(g)=\sum_{M\colon gM=M}(-1)^{|M|}\operatorname{sgn}(g\mid M).
\]
The equality remains valid when \(g\) reverses orientations of some faces.

**4. Orbit reduction.** A matching fixed setwise by \(g\) is a union of full edge-cycles of \(g\). Only cycles whose constituent graph edges are pairwise disjoint can occur; two such cycles can co-occur precisely when they use disjoint sets of original graph vertices. An allowed edge cycle of length \(\ell\) contributes \((-1)^\ell(-1)^{\ell-1}=-1\) to the formula. Therefore, if \(\mathscr O_g\) is the finite collection of internally disjoint edge cycles, then
\[
\chi(g)=\sum_{\substack{J\subseteq\mathscr O_g\\\text{cycles of }J\text{ mutually vertex-disjoint}}}(-1)^{|J|}.
\]
This is a finite, exact evaluation of the independence polynomial of the edge-cycle conflict graph at \(-1\). Evaluating it on all 216 automorphisms gives the eleven rows displayed above. A second verifier separately enumerates **every** matching fixed by each automorphism and its actual induced simplex orientation sign; all 216 direct answers agree with the orbit-reduction formula.

**5. Rational quotient.** Summing the character values with the row multiplicities gives
\[
40+18(-4)+18(4)+12(1)+14(4)+36(-1)+36(-2)=0.
\]
Character averaging thus yields \(\dim\widetilde H_5(K;\mathbb Q)^G=0\). For a finite simplicial group action, barycentric subdivision removes simplex inversions, and rational averaging identifies the homology of the orbit space with the invariant homology. All its reduced rational homology therefore vanishes.

## Verification
Run `python3 verify_pappus_character.py` and `python3 verify_pappus_mod2.py` with Python 3.9 or later. Both use only the Python standard library, construct their graph and matching faces from the LCF sequence, and contain exact assertions. The character program checks all 216 automorphisms through two different chain-trace algorithms, validates all character multiplicities and group-invariant dimension, and prints `DIRECT_AND_ORBITAL_216_CHECKS_OK`. The other program computes every augmented mod-two boundary rank and prints `HOMOLOGY_MOD2_OK`. Their execution outputs are included as `verification_character.log` and `verification_mod2.log`.

## Relationship to prior work
Björner, Lovász, Vrećica and Živaljević study matching-complex topology in a foundational 1994 paper, primarily for complete and bipartite complete graphs; this does not determine the action of the Pappus graph's symmetry group on the matching complex in question. The standard Pappus graph identification and LCF description are recorded by MathWorld.

Two earlier exact published calculations concern **precisely** this ordinary Pappus matching complex: *Mod-2 homology of the Pappus matching complex* determines the forty-dimensional mod-two group, and *Integral homotopy type of the Pappus graph matching complex* proves the nonequivariant integral wedge of forty five-spheres. These results are expressly treated as prior work and do not compute the 216-element rational character, its eleven cycle profiles, or the full-group invariant subspace. A different calculation for the *induced* Pappus matching complex concerns a strict subcomplex and does not imply the present representation. Known automorphism counts of the Pappus graph alone likewise do not specify the action on homology.

## Limitations
The result is confined to rational representation theory and rational homology of the full orbit space; it does not determine an integral automorphism-module lattice, integral quotient homology, equivariant homotopy type, or quotient fundamental group. The exact computations are exhaustive for the specified finite graph, but do not imply a theorem for all 18-vertex cubic symmetric graphs. Bibliographic uniqueness cannot be certified against unindexed work. The quotient is asserted to be **rationally acyclic**, not contractible.

## References
1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39, first published 1994-02-01. https://doi.org/10.1112/jlms/49.1.25
2. E. W. Weisstein, *Pappus Graph*, MathWorld, for the 18-vertex graph, LCF representation and group size. https://mathworld.wolfram.com/PappusGraph.html
3. *Integral homotopy type of the Pappus graph matching complex*, published published-finding corpus record. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
4. *Mod-2 homology of the Pappus matching complex*, published published-finding corpus record. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-pappus-matching-complex--a28326a5f491
