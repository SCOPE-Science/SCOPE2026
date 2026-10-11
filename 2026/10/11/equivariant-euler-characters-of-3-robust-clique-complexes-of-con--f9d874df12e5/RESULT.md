# Equivariant Euler characters of \(3\)-robust clique complexes of connected bipartite graphs

## Finding
For a finite connected simple bipartite graph \(G\), let \(K=I_3(G)\) be the simplicial complex whose faces are vertex subsets \(S\) for which the induced graph has independence number \(\alpha(G[S])\leq2\). Let \(\mathcal C_4(G)\) denote its set of unoriented simple four-cycles; write \(B=H_1(G;\mathbb Q)\). For any finite graph-automorphism group \(\Gamma\), equality holds in the Grothendieck ring of rational \(\Gamma\)-representations:

\[
\sum_{j\geq0}(-1)^j[\widetilde H_j(K;\mathbb Q)]
= [\mathbb Q[\mathcal C_4(G)]]-[\operatorname{Sym}^2 B].
\]

Thus for \(g\in\Gamma\), if \(c_4(g)=|\mathcal C_4(G)^g|\) and \(\tau(g)=\operatorname{tr}(g\mid B)\), then

\[
\widetilde L(g;K)=c_4(g)-\frac{\tau(g)^2+\tau(g^2)}2.
\]

The trace \(\tau(g)\) is computable without homology matrices: it is the signed number of fixed unoriented edges (positive when the endpoints are preserved, negative when exchanged), minus the number of fixed vertices, plus one. If \(b=|E(G)|-|V(G)|+1\), then

\[
\widetilde\chi(K)=|\mathcal C_4(G)|-\binom{b+1}{2}.
\]

For finite \(\Gamma\), the quotient has
\[
\widetilde\chi(K/\Gamma)=|\mathcal C_4(G)/\Gamma|-\dim(\operatorname{Sym}^2 B)^\Gamma.
\]

For example, the cube graph has \(b=5\) and six four-cycles, so its reduced Euler characteristic is \(-9\). Its full order-\(48\) graph automorphism group yields quotient reduced Euler characteristic \(-1\): the four-cycle permutation representation has one invariant dimension and the symmetric-square representation has two.

## Assumptions and scope
The graph is finite, connected, simple and bipartite. All representations are over \(\mathbb Q\), and the group \(\Gamma\) is finite; any subgroup of the finite graph-automorphism group is allowed. The notation \([M]\) denotes the class of a rational representation \(M\). The displayed identity is an *alternating homology character*, not a claim that homology is concentrated in one degree. When \(G\) has one vertex the reduced complex is contractible and the assertion still holds.

## Proof
Set \(V=\mathbb Q[V(G)]\), and let \(E=C_1(G;\mathbb Q)\) be the signed edge representation: an oriented edge \([u,v]\) is negated if a symmetry reverses it. Let \(U=\mathbb Q[E(G)]\) be the unsigned edge permutation module. The connected graph chain complex gives \([B]=[E]-[V]+[\mathbb Q]\).

Bipartiteness, via the matching-cover equality, implies that a four-element set is a face of \(K\) precisely when its induced graph contains two disjoint edges. A three-element set is a face precisely when it contains an edge; every pair is a face; no set of five or more vertices is a face. Indeed, \(\alpha(G[S])=|S|-\nu(G[S])\) for an induced bipartite subgraph, and \(\nu(G[S])\leq\lfloor |S|/2\rfloor\).

Put \(T=C_2(K;\mathbb Q)\) and \(F=C_3(K;\mathbb Q)\). Decompose \(E\otimes V\) into oriented edges with a marked endpoint and oriented edges with a marked vertex off the edge. The endpoint part is \(E\oplus U\). Map the other part to \(T\) by \([u,v]\otimes w\mapsto[u,v,w]\). It is surjective. Because a three-vertex set in a bipartite graph spans at most two graph edges, there is exactly one kernel generator for every unordered adjacent edge pair and none for a triple with one edge. If adjacent edges are oriented \(e=[a,b]\) and \(f=[b,c]\), the generator is \(e\otimes c-f\otimes a\). Its orientation rule under permutations agrees with the product \(ef\) in \(\operatorname{Sym}^2E\). Denote this adjacent-edge-pair module by \(A\). Hence

\[
[E\otimes V]=[E]+[U]+[T]+[A].
\]

Partition the basis of \(\operatorname{Sym}^2E\) into diagonal edge squares, adjacent distinct-edge pairs, and disjoint distinct-edge pairs. The diagonal part is \(U\), because reversing an oriented edge does not change its square. Write \(D\) for the disjoint-pair module. Then

\[
[\operatorname{Sym}^2E]=[U]+[A]+[D].
\]

The map \(D\to F\) that sends \([a,b][c,d]\) to \([a,b,c,d]\) is well-defined (switching two two-vertex blocks has even sign) and surjective by the four-face characterization. A four-face with only one perfect matching contributes no kernel. A four-face with two perfect matchings is necessarily an induced four-cycle, since the graph is bipartite; the relation between the two oriented matchings is their *sum*. All automorphisms preserving this square preserve that sum, so the kernel is the **unsigned** four-cycle permutation module. Therefore

\[
[D]=[F]+[\mathbb Q[\mathcal C_4(G)]].
\]

Eliminating \(A,U,D\) gives

\[
[T]-[F]=[E\otimes V]-[E]-[\operatorname{Sym}^2E]+[\mathbb Q[\mathcal C_4(G)]].
\]

The full one-skeleton of \(K\) gives \(C_1(K;\mathbb Q)=\bigwedge^2V\), and the alternating *reduced* homology class agrees with the reduced cellular chain class:

\[
\mathcal E_K=[V]-[\bigwedge^2V]+[T]-[F]-[\mathbb Q].
\]

Finally, because \([B]=[E]-[V]+[\mathbb Q]\), the symmetric-square identity for virtual representations yields

\[
[\operatorname{Sym}^2 B]=[\operatorname{Sym}^2E]+[E]+[\mathbb Q]-[E\otimes V]-[V]+[\bigwedge^2V].
\]

Substitution proves \(\mathcal E_K=[\mathbb Q[\mathcal C_4(G)]]-[\operatorname{Sym}^2B]\). The standard symmetric-square trace identity gives \(\operatorname{tr}(g\mid\operatorname{Sym}^2B)=(\tau(g)^2+\tau(g^2))/2\). Connectedness gives the signed graph-cycle-space trace \(\tau(g)=\operatorname{tr}(g\mid E)-\operatorname{tr}(g\mid V)+1\). Evaluation at the identity yields the numerical formula. Taking rational invariants under a finite group gives the quotient formula.

For rectangular grids, the cycle space is an orientation-sign twist of the square-face permutation module; the twist disappears on symmetric squares. Since every four-cycle is an elementary square, the virtual homology class specializes to the *negative* permutation module on unordered pairs of distinct square faces. Combining this with the previously established degree-three homology concentration of grid robust clique complexes recovers the actual degree-three permutation module for all rectangular sizes and all graph symmetries (not merely even-sided grids).

## Verification
The standalone Python program `verify.py` enumerates the complex by the defining independence condition and independently computes the signed simplicial Lefschetz trace of every listed graph automorphism. It then constructs the four-cycle permutation trace and the symmetric-square cycle-space trace. It completed comparisons for \(232\) connected bipartite graphs, \(858\) automorphisms, and complete checks for a \(2\)-by-\(5\), \(3\)-by-\(4\), \(4\)-by-\(4\) grid and all \(48\) cube symmetries, reporting `VERIFY_OK`. The proof covers all finite connected bipartite graphs; finite enumeration is only an independent consistency check.

## Relationship to prior work
M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs* (arXiv:2602.11365, first public February 11, 2026), studies the topology of these complexes on grid and square-sequence graphs, including homology concentration and wedge multiplicities. The theorem above instead computes the **entire equivariant alternating homology representation for arbitrary connected bipartite graphs**; its grid specialization is compatible with those homotopy results. Kim and Lew (arXiv:1912.12605) study graph independence-bounded complexes and collapsibility; Choe and Jung (arXiv:2502.20987) study higher secant complexes and homological algebra. The character identity is not asserted by the inspected sections of these works. Previously observed even-grid reflection characters are a special case, not independent evidence for all graphs or the full graph-automorphism action.

## Limitations
No degreewise homology decomposition or integral torsion statement is asserted for general bipartite graphs. In particular, a nonzero alternating character does not locate the homological degree. The proof relies essentially on bipartiteness, and the theorem is not claimed for general triangle-free graphs. No independent external audit or exhaustive survey of unindexed literature has been performed.

## References
1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, https://arxiv.org/abs/2602.11365 (first posted 2026-02-11).
2. Kim and Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, https://arxiv.org/abs/1912.12605.
3. Choe and Jung, *A Fröberg type theorem for higher secant complexes*, arXiv:2502.20987, https://arxiv.org/abs/2502.20987.
