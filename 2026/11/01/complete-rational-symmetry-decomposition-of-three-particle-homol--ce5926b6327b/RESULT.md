# Complete rational symmetry decomposition of three-particle homology on the utility-graph extension

## Finding

Let \(G=K_{3,4}\) with its natural \(S_3\times S_4\) automorphism group, and \(X=\operatorname{UConf}_3(|G|)\). As rational \(S_3\times S_4\)-modules,
\[
H_1(X;\mathbb Q)\cong S^{(2,1)}\boxtimes S^{(3,1)},
\]
and
\[
\begin{aligned}
H_2(X;\mathbb Q)\cong{}&S^{(1,1,1)}\boxtimes\left(2S^{(2,2)}\oplus S^{(3,1)}\oplus S^{(2,1,1)}\right)\\
&\oplus S^{(2,1)}\boxtimes\left(S^{(1,1,1,1)}\oplus S^{(2,2)}\oplus S^{(3,1)}\oplus S^{(2,1,1)}\right).
\end{aligned}
\]
Here the Specht labels in the first and second factors are partitions of \(3\) and \(4\), respectively, and \(\boxtimes\) denotes the exterior tensor product. In particular the complete rational Betti vector is \((1,6,28,0)\), neither positive-degree homology contains an invariant vector under the full group, and \(X/(S_3\times S_4)\) has vanishing reduced rational homology. The rational ranks, including the rank \(28\), were already established in prior literature; the claim's new content is the complete seven-constituent action on \(H_2\) and its symmetry consequences.

The expression contains seven inequivalent irreducible constituents in degree two: one appears twice and six occur once. The dimensions are \(4+3+3+2+4+6+6=28\). This fully determines the character on all \(144\) automorphisms, including the group-fixed subspace. The Betti ranks and torsion-free second homology are **not** asserted as new: they are present in the later exact-homology table of An (2026).

## Assumptions and scope

Let the graph \(G\) have bipartition \(A=\{0,1,2\}\) and \(B=\{3,4,5,6\}\), with all \(12\) cross edges and no within-part edges. \(X\) comprises unordered three-element subsets of the geometric realization \(|G|\) whose points are pairwise distinct. The vertex-label permutations preserving the two part sizes form exactly \(S_3\times S_4\). All representation statements are over \(\mathbb Q\); they neither assert integral semisimplicity nor an equivariant homotopy equivalence.

For each integer \(n\), \(S^\lambda\) denotes the usual rational Specht module of the symmetric group on \(n\) letters for a partition \(\lambda\vdash n\). The degree-zero homology is the trivial one-dimensional representation; the complex has no rational homology above degree two.

## Proof

**The chain model.** Use the reduced Świątkowski model from An–Drummond-Cole–Knudsen (Definition 4.7, Theorem 4.5, Proposition 4.9). Its weight-three chain groups have degree-\(d\) basis elements
\[
(v_1<\cdots<v_d;\ h_{v_1,e_1}-h_{v_1,e^0_1},\ldots,h_{v_d,e_d}-h_{v_d,e^0_d};\,\mathsf m),
\]
where \(0\le d\le3\), the \(v_i\) are distinct graph vertices, \(e^0_i\) is the fixed first incident edge at \(v_i\), the other \(e_i\) are incident edges, and \(\mathsf m\) is a commutative edge monomial of degree \(3-d\). The differential sends a local difference to the corresponding difference of edge variables and extends by the alternating Koszul rule. Explicit degree dimensions are \((364,1326,1476,491)\). Each group automorphism acts on edge monomials by permutation, on local differences by re-expansion relative to the destination first edge, and on ordered degree-one factors with the permutation sign. This is a rationally equivariant model of the topological configuration-space chains.

**Rank control.** All columns of the three boundary maps are constructed explicitly in the accompanying checker. Their exact ranks modulo \(3\) are \((363,957,491)\). Hence the rational ranks are bounded below by these integers. The image of the first boundary consists of the augmentation-zero subspace of degree-three edge monomials, because differences of incident edge variables generate all monomial differences in the connected line graph. Thus its rational rank is exactly \(364-1=363\). Ko–Park's first-homology formula, applied to this simple three-connected nonplanar graph, gives \(H_1(X;\mathbb Z)\cong\mathbb Z^6\oplus\mathbb Z/2\). Therefore \(\operatorname{rank}_{\mathbb Q}\partial_2=(1326-363)-6=957\), matching the modular lower bound. Since \(\partial_3\) already has \(491\) independent columns modulo \(3\), it is injective over \(\mathbb Q\). Consequently \(\beta_2=1476-957-491=28\) and \(\beta_3=0\). These ranks agree with the independent published classification in An (2026, Table 1), but their derivation here certifies the actual chain complex used for the representation calculation.

**First-homology character.** The natural map tracking the sum of the three particle trajectories sends \(H_1(X;\mathbb Q)\) onto the graph's cycle space. A cycle in any four-edge square of \(G\) can be realized by moving one particle around it while the other two occupy vertices outside that square. Such squares generate the graph cycle space, so the map is surjective. Both sides have dimension \(6\) and the map respects graph automorphisms; hence it is an isomorphism. Since the graph is complete bipartite, its cycle representation is the outer tensor product of the two augmentation representations: \(S^{(2,1)}\boxtimes S^{(3,1)}\).

**Second-homology character and decomposition.** Let \(L(g)=\sum_{d=0}^3(-1)^d\operatorname{tr}(g\mid C_d)\) be the rational alternating chain trace. Since only homological degrees zero, one and two survive,
\[
\chi_{H_2}(g)=L(g)-1+\chi_{H_1}(g).
\]
The checker determines every \(L(g)\) by exact signed diagonal terms for all \(3!\cdot4!=144\) graph automorphisms. It also verifies the induced chain map identities on every basis generator in all positive degrees for four generators of the automorphism group. For the five rational irreducible characters of \(S_4\), use the trivial and sign characters, the two-subset permutation character minus the four-point permutation character for \(S^{(2,2)}\), and the standard character \(\#\mathrm{Fix}-1\) with and without sign for \(S^{(3,1)}\) and \(S^{(2,1,1)}\). Pair each with the trivial, sign, and standard characters of \(S_3\). The exact inner product over all \(144\) automorphisms gives precisely the seven multiplicities displayed under Finding, with no other constituents.

**Full-symmetry quotient.** Neither degree-one nor degree-two representation has a trivial constituent, so both positive-degree invariant spaces vanish. Finite group transfer over \(\mathbb Q\) identifies rational homology of the ordinary orbit space with group invariants. Thus \(\widetilde H_*(X/(S_3\times S_4);\mathbb Q)=0\). The quotient need not be contractible.

## Verification

Run the included standard-library program `verify_k34.py` with Python 3.9 or newer. It independently builds all \(3657\) chain-basis elements, checks \(\partial^2=0\) for all columns, and reports the sparse boundary nonzero counts \((2652,5904,2946)\) and exact boundary ranks over primes \(2,3,5,101\). It checks the four automorphism-generator chain maps on all basis vectors; computes the complete set of group characters from chain traces; and verifies exact irreducible inner products and zero fixed-space multiplicities. Its recorded output is in `verification_output.txt`. Modulo-prime elimination is used only to establish rational rank lower bounds; the needed rational upper bound follows from Ko–Park's theorem as explained above.

## Relationship to prior work

Ko and Park (2011), Theorem 3.16, determine first integral homology for graph braid groups, including the six free generators and two-torsion for this graph. An, Drummond-Cole and Knudsen (2017 first preprint; later published) provide the reduced Świątkowski model and functoriality used here. Most closely, An (October 2026), Section 3.5 and Table 1, **already computes the full integral Betti groups for three particles on \(K_{4,3}\)**, including \(H_2\cong\mathbb Z^{28}\); Section 5.1 proves a multiplicity-free representation theorem for **top-degree** \(H_m(B_m K_{a,b};\mathbb Q)\), which here is \(H_3=0\). The character and seven-constituent representation of the **degree-two** group is different information. The general top-degree theorem does not imply the stated degree-two decomposition without an additional equivariant chain calculation. A targeted search of related published records and comparison with other published statements did not identify the same degree-two representation. Absence of an indexed match is not evidence of absolute priority.

## Limitations

The result classifies the rational representation for one finite graph and one particle count. It does not supply an integral equivariant lattice decomposition, an integral homotopy classification, a cohomology ring, or an equivariant homotopy equivalence. The nonequivariant ranks are known prior art, and the significance asserted here is confined to the natural complete symmetry invariant and the rational quotient consequence. It has not undergone independent mathematical audit; an equivalent unpublished or unindexed character calculation cannot be excluded.

## References

1. K. H. Ko and H. W. Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648v1 (first public 2011-01-13), Theorem 3.16.
2. B. H. An, G. C. Drummond-Cole, and B. Knudsen, *Subdivisional Spaces and Graph Braid Groups*, arXiv:1708.02351 (first public 2017-08-08), Definition 4.7, Theorem 4.5, Proposition 4.9.
3. B. H. An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305v1 (first public 2026-10-03), Section 3.5, Table 1, Section 5.1.
