# The complete \(S_4\)-character on tetrahedral discrete Morse matching homology

## Finding
Let \(X=\mathcal M(\Delta^3)\) denote the **ordinary**, non-pure complex of nonempty discrete Morse matchings on the full tetrahedral three-simplex. The natural action of permutations of its four vertices induces the following character on the only nonzero reduced rational homology group:

\[
\begin{array}{c|rrrrr}
\text{cycle type}&(1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\\hline
\operatorname{tr}(g\mid H_4(X;\mathbb Q))&99&1&-1&0&-1
\end{array}
\]

In particular the complete rational representation is
\[
H_4(X;\mathbb Q)\cong
4\operatorname{Sp}_{(4)}\oplus13\operatorname{Sp}_{(3,1)}
\oplus8\operatorname{Sp}_{(2,2)}\oplus12\operatorname{Sp}_{(2,1,1)}
\oplus4\operatorname{Sp}_{(1,1,1,1)},
\]
where \(\operatorname{Sp}_{\lambda}\) is the irreducible rational Specht representation for a partition \(\lambda\) of four. All other reduced rational homology groups vanish. The representation dimension is \(4+39+16+36+4=99\).

## Assumptions and scope
The full simplex has the fifteen **nonempty** faces, indexed by nonzero four-bit masks. Its Hasse diagram has 28 cover relations \((a,b)\), with \(b\) obtained by adjoining one vertex to \(a\). A discrete Morse matching is a set \(W\) of these relations whose endpoints are pairwise disjoint and for which reversing the matched arrows in the directed Hasse diagram yields no directed cycle. The vertices of \(X\) are individual cover relations and its simplices are the nonempty acyclic matchings \(W\), one simplex of dimension \(|W|-1\) for each such set.

The relabeling action sends every cover relation \((a,b)\) to \((g(a),g(b))\). It preserves compatible matchings and acyclicity, hence acts simplicially on \(X\). This is not a calculation for \(\mathcal M(\partial\Delta^3)\), the pure Morse matching complex, or the generalized matching complex.

## Proof
**A. Homology concentration and its orientation.** Theorem 20 and Table 2 of Scoville (arXiv:2604.18172v1) give \(X\simeq\bigvee^{99}S^4\). Thus ordinary rational homology is \(\mathbb Q\) in degree zero, is 99-dimensional in degree four, and vanishes in all other degrees. The induced action on the degree-zero group is trivial because \(X\) is connected. For every \(g\in S_4\), the simplicial Lefschetz identity therefore yields
\[
L(g;X)=\sum_{q\ge0}(-1)^q\operatorname{tr}(g\mid C_q(X;\mathbb Q))
=1+\operatorname{tr}(g\mid H_4(X;\mathbb Q)).
\]

**B. Exact signed fixed-simplex formula.** Order the 28 Hasse edges lexicographically. For a nonempty matching \(W=\{e_1<\cdots<e_k\}\) fixed setwise by \(g\), the action on its oriented simplex contributes the sign of the permutation \(g:e_i\mapsto g(e_i)\) of these \(k\) edges. Non-fixed simplices have zero diagonal chain coefficient. Hence
\[
L(g;X)=\sum_{\substack{\varnothing\ne W\subseteq E(H)\\W\text{ an acyclic matching}\\gW=W}}
(-1)^{|W|-1}\operatorname{sgn}(g|_W).
\]
This finite identity is a chain-level proof: it includes the orientation sign; an unsigned count of fixed matchings would generally be incorrect.

**C. Exhaustive certificate.** The supplied `verification.py` constructs all 28 cover relations from the fifteen nonzero face masks. A recursive first-available-edge branching procedure enumerates every matching exactly once: it selects a relation, removes relations incident to the same Hasse faces, and subsequently considers the remaining relations in increasing order. No choices are omitted or duplicated. Each generated matching is tested for acyclicity by topological sorting the entire oriented Hasse diagram after reversing precisely its matching edges. The test terminates after processing all fifteen faces if and only if the directed graph is acyclic. Therefore the procedure exhausts, rather than samples, the entire finite simplicial complex. It finds 14,720 nonempty Hasse matchings, of which 12,820 are acyclic, with dimension-wise face counts
\[
(f_0,\ldots,f_6)=(28,300,1544,3932,4632,2128,256),
\]
matching the published Table 1 exactly.

For each permutation class representative, the program evaluates the signed fixed-simplex formula. Independently, it finds all orbits of the permutation on the Hasse edges and enumerates unions of orbit blocks, rejecting blocks with repeated endpoints and checking the acyclicity of every remaining union. On a cyclic orbit block of length \(s\), the permutation sign is \((-1)^{s-1}\); multiplying these signs gives an independent trace calculation without iterating the previously enumerated 12,820 simplices. Both exact enumerations agree class by class:
\[
\begin{array}{c|rrrrr}
\text{cycle type}&(1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\\hline
\text{class size}&1&6&3&8&6\\
\text{fixed simplices}&12820&146&16&7&0\\
L(g;X)&100&2&0&1&0
\end{array}
\]
The program also directly checks that these values agree for all 24 vertex permutations, not only their five representatives. Subtracting the degree-zero trace gives the stated fourth-homology character \((99,1,-1,0,-1)\).

**D. Character decomposition.** In the same class ordering, the rational irreducible characters of \(S_4\) are
\[
\begin{array}{c|rrrrr}
\operatorname{Sp}_{(4)}&1&1&1&1&1\\
\operatorname{Sp}_{(3,1)}&3&1&-1&0&-1\\
\operatorname{Sp}_{(2,2)}&2&0&2&-1&0\\
\operatorname{Sp}_{(2,1,1)}&3&-1&-1&0&1\\
\operatorname{Sp}_{(1,1,1,1)}&1&-1&1&1&-1
\end{array}
\]
For each character \(\psi\), its multiplicity is
\[
\langle\chi,\psi\rangle=\frac1{24}\left(\chi_1\psi_1+6\chi_2\psi_2+3\chi_3\psi_3+8\chi_4\psi_4+6\chi_5\psi_5\right).
\]
The exact inner products are respectively \(4,13,8,12,4\). Maschke's theorem over \(\mathbb Q\) and rational realizability of the five Specht representations give the asserted isomorphism of rational \(S_4\)-modules.

## Verification
Run `python3 verification.py` with Python 3 and the standard library only. It asserts the previously published face vector and the exact count of acyclic matchings; executes both independent fixed-trace methods for all five cycle types; checks all 24 permutations; calculates all five character inner products as nonnegative integers; and prints `VERIFY_OK`. Replaying the complete embedded source requires no auxiliary data, package, network, or external program. The source is provided alongside this document. The proof of exhaustive coverage is the finite recursion and acyclicity criterion described above, not the mere existence of a test log.

## Relationship to prior work
Chari and Joswig introduced the discrete Morse matching complex and described its acyclic Hasse matching model (arXiv:math/0011234v1). Lin and Scoville established the natural automorphism action on the Morse complex (arXiv:1904.10907v1, Section 3.1). Scoville computed the ordinary \(99\)-sphere homotopy type and the complete face vector for the full tetrahedral Morse matching complex (arXiv:2604.18172v1, Tables 1–2 and Theorem 20). Those results supply the exact input topological concentration and the group action, but do not specify their induced fourth-homology character. The new mathematical datum is the complete action of tetrahedral relabelings on this homology group, which is not implied by its dimension or by identifying the automorphism group.

## Limitations
This is a finite exact classification for the full three-simplex, not a formula for all simplex dimensions. The result is rational and does not specify integral Specht-lattice decompositions or an equivariant wedge-of-spheres homotopy equivalence. The existence of an unindexed equivalent equivariant computation cannot be excluded by literature search alone. The numerical verification is exhaustive on the explicitly defined finite input but cannot certify claims for other inputs.

## References
1. N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1 (first publicly posted 2026-04-20), Tables 1–2 and Theorem 20. https://arxiv.org/abs/2604.18172
2. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907v1 (2019), Section 3.1. https://arxiv.org/abs/1904.10907
3. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000), Sections 2–3. https://arxiv.org/abs/math/0011234
