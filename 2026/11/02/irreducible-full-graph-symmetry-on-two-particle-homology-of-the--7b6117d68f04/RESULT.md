# Irreducible full-graph symmetry on two-particle homology of the complete bipartite graph on eight vertices

## Finding
Let \(K_{4,4}\) have labelled bipartition \(A=\{0,1,2,3\}\) and \(B=\{4,5,6,7\}\), and let \(X=\operatorname{UConf}_2(|K_{4,4}|)\) denote its ordinary unordered configuration space of two distinct points. Its full graph automorphism group is \(G=(S_4\times S_4)\rtimes C_2\), of order \(1152\). Write \(V_{211}=S^{(2,1,1)}\) and \(V_{22}=S^{(2,2)}\) for the three- and two-dimensional rational Specht representations of \(S_4\). Then
\[
H_2(X;\mathbb Q)\cong\operatorname{Ind}^{G}_{S_4\times S_4}(V_{211}\boxtimes V_{22}),
\qquad H_2(X;\mathbb Z)\cong\mathbb Z^{12}.
\]
The induced rational representation is irreducible. More explicitly, its restriction to the part-preserving subgroup is \((V_{211}\boxtimes V_{22})\oplus(V_{22}\boxtimes V_{211})\); the character is zero on each of the 576 part-swapping automorphisms. The other rational Betti numbers are \(b_0=1\), \(b_1=9\), and all higher Betti numbers vanish. The full-group quotient has no positive-degree rational homology.

## Assumptions and scope
The configuration is an ordinary topological configuration of two unordered *distinct points on the geometric graph*, not a sink configuration permitting collisions and not the graph matching or Morse complex. Symmetries permute the two four-vertex bipartition classes independently and may exchange the classes. All representation statements use characteristic zero. The integral assertion concerns \(H_2\), not possible torsion in \(H_1\).

## Proof
**Finite cubical model.** The Abrams discrete unordered configuration model applies without subdividing: adjacent essential vertices have graph distance at least one, and the girth four is at least three, as required for two points. An unoriented zero-cell is a pair of distinct graph vertices, a one-cell is a vertex disjoint from an edge, and a two-cell is a pair of edges with disjoint endpoint sets. Orient each edge from \(A\) to \(B\), and orient the two-cell \((e,f)\) by the ordered pair \(e<f\). The chain-group ranks are
\[
\dim C_0=\binom82=28,\quad \dim C_1=16\cdot6=96,\quad \dim C_2=\tfrac12\,16\cdot9=72.
\]
For \(e=(a,b)\) and \(f=(c,d)\) with the indicated orientations, boundaries are
\[
\partial_1(v,e)=(v,b)-(v,a),\qquad
\partial_2(e,f)=(b,f)-(a,f)-(d,e)+(c,e).
\]
The attached deterministic checker constructs these sparse *integer* matrices and checks \(\partial_1\partial_2=0\).

**Exact ranks, rather than experimental guesses.** The complex has connected one-skeleton (a particle can be moved along edges while the second waits), so \(\operatorname{rank}_{\mathbb Q}\partial_1\le27\). A sparse elimination modulo the prime \(1009\) gives rank \(27\), hence equality in characteristic zero. For \(\partial_2\), modular elimination gives rank at least \(60\). The checker independently constructs eighteen integral two-torus cycles from every unordered complementary pair of disjoint four-cycles and finds twelve of them linearly independent modulo \(1009\). All eighteen are checked to have zero integral boundary, so the characteristic-zero kernel has dimension at least twelve and \(\operatorname{rank}_{\mathbb Q}\partial_2\le72-12=60\). Thus its rational rank is **exactly** \(60\). We obtain \(b_2=12\) and \(b_1=96-27-60=9\). Because the two-dimensional chain group is free abelian and there are no three-cells, its submodule \(H_2=\ker\partial_2\) is torsion-free of rank twelve.

**First-homology trace.** Summing the trajectories of both unordered particles defines a natural homomorphism \(H_1(X;\mathbb Q)\to H_1(K_{4,4};\mathbb Q)\). Every graph four-cycle is represented by moving one particle around it while the second remains at an exterior vertex; four-cycles generate the graph cycle lattice, proving surjectivity. The graph's cycle rank is \(16-8+1=9\), so this map is an equivariant isomorphism of rational homology. Its character at \(g\in G\) equals \(\operatorname{tr}_{C_1(K_{4,4})}(g)-\operatorname{tr}_{C_0(K_{4,4})}(g)+1\), using signed edges.

**Top-homology character.** The signed cubical Lefschetz identity now yields, for every \(g\in G\),
\[
\operatorname{tr}_{H_2}(g)=\operatorname{tr}_{C_0(X)}(g)-\operatorname{tr}_{C_1(X)}(g)+\operatorname{tr}_{C_2(X)}(g)
+\operatorname{tr}_{C_1(K_{4,4})}(g)-\operatorname{tr}_{C_0(K_{4,4})}(g).
\]
For a part-preserving automorphism \(g=(p,q)\in S_4\times S_4\), this finite identity evaluates exactly to
\[
\chi_2(p,q)=\chi_{211}(p)\chi_{22}(q)+\chi_{22}(p)\chi_{211}(q).
\]
For each part-interchanging automorphism, it evaluates to zero. These identities were verified for every \(576+576=1152\) group elements by the standalone code, with all signs determined by actual permutations of cubical cells. The two summands on restriction are nonisomorphic irreducible representations exchanged by the nontrivial coset; Clifford theory implies that the induced twelve-dimensional rational representation is irreducible. Independently, the exact character self-inner-product is \(\sum_{g\in G}\chi_2(g)^2/1152=1\). Character averaging gives no positive-degree rational invariants, including in degree one; finite-group transfer identifies the rational homology of the orbit space with these invariants.

## Verification
Execute `python3 verify.py` with ordinary Python 3. The checker performs exact signed fixed-cell counts, checks the chain-complex identity and the integral square-torus cycles, computes three ranks modulo \(1009\) and proves the characteristic-zero ranks by matching rational upper and lower bounds. It tests all \(1152\) graph automorphisms, the character formulas, diagonal restriction, irreducibility and vanishing invariants. Successful replay prints `K44_UNORDERED_TWO_POINT_12_IRRED_WREATH_CERTIFIED`. A field computation by itself is not used as a proof of a rational upper bound: the explicitly verified independent integral cycles supply that bound.

## Relationship to prior work
Maciążek and Sawicki (2018 preprint; 2019 journal publication) develop graph configuration homology and the topology of disjoint-cycle product classes. Ramos and Yun (2026), §3.3, Theorem 3.17, Table 3 and Example 3.18, compute the diagonal \(S_4\)-action on the unordered top homology of \(K_{4,4}\), namely \(2S^{(2,1,1)}\oplus2S^{(3,1)}\), and analyze generators under diagonal vertex permutations. The present result refines that diagonal action to the full independent-vertex-permutation and bipartition-exchange group, distinguishing the unique irreducible twelve-dimensional wreath-product module and the zero trace of every part exchange. The earlier diagonal representation alone does not determine a unique extension to the full group.

## Limitations
This result treats only two unordered points on \(K_{4,4}\) and the rational representation on second homology; no integral \(G\)-lattice isomorphism beyond the free rank is claimed, and no claim is made about integral torsion in first homology or the integral homology of quotients. The novelty comparison does not exclude inaccessible or unindexed equivalent papers, and no independent audit has been performed.

## References
1. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, initial public preprint 7 June 2018, arXiv:1806.02846, https://arxiv.org/abs/1806.02846 .
2. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, first posted 11 June 2026, arXiv:2606.13813, https://arxiv.org/pdf/2606.13813 , especially §3.3 and Table 3.
