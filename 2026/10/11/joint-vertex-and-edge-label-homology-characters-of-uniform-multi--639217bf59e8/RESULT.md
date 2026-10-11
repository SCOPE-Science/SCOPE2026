# Joint vertex-and-edge-label homology characters of uniform multiclique complexes

## Finding
For integers \(n\ge 2\) and \(q\ge 2\), let \(X_{n,q}\) be the geometric realization of the simplicial poset whose nonempty faces are pairs \((I,c)\), where \(I\subseteq[n]\) and \(c:\binom{I}{2}\to[q]\) assigns one of \(q\) parallel-edge labels to each unordered pair. Restriction of labels defines the face relation. Vertex relabeling and a simultaneous permutation of all edge labels give a commuting action of \(S_n\times S_q\).

**Theorem.** All reduced rational homology of \(X_{n,q}\) vanishes outside degree \(n-1\). Let \(g\in S_n\) have cycles of lengths \(\lambda_1,\ldots,\lambda_c\), and let \(h\in S_q\). Write \(f_h(t)=|\operatorname{Fix}(h^t;[q])|\). For \(J\subseteq[c]\), set
\[
 W_{g,h}(J)=
 \prod_{i\in J}f_h(\lambda_i)^{\lfloor(\lambda_i-1)/2\rfloor}
 \prod_{\substack{i\in J\\2\mid\lambda_i}}f_h(\lambda_i/2)
 \prod_{\substack{i<j\\i,j\in J}}
 f_h(\operatorname{lcm}(\lambda_i,\lambda_j))^{\gcd(\lambda_i,\lambda_j)},
\]
with empty products equal to one, including \(W_{g,h}(\varnothing)=1\). The **complete joint rational character** is
\[
 \boxed{\operatorname{tr}((g,h)\mid\widetilde H_{n-1}(X_{n,q};\mathbb Q))
 =(-1)^n\sum_{J\subseteq[c]}(-1)^{|J|}W_{g,h}(J).}
\]
In particular, when \(h=1\), put
\[
 E_g(J)=\sum_{i\in J}\lfloor\lambda_i/2\rfloor+
 \sum_{\substack{i<j\\i,j\in J}}\gcd(\lambda_i,\lambda_j).
\]
Then the vertex-permutation character is \((-1)^n\sum_J(-1)^{|J|}q^{E_g(J)}\), and the top Betti number is
\[
 \boxed{\beta_{n-1}(X_{n,q})=(-1)^n\sum_{k=0}^n(-1)^k\binom nk q^{\binom k2}.}
\]
As a symmetry-sensitive quotient consequence, for \(n=3\) the commuting edge-label action identifies
\[
 \boxed{\widetilde H_2(X_{3,q}/S_3;\mathbb Q)\cong
 \bigwedge^3\mathbb Q^q}\quad\text{as \(S_q\)-representations},
\]
where \(\mathbb Q^q\) is the natural permutation module. Hence the second rational Betti number of this quotient is \(\binom q3\), whereas \(\dim\widetilde H_2(X_{3,q};\mathbb Q)=q^3-3q+2\).

## Assumptions and scope
The multigraph has \(n\) labeled vertices, exactly \(q\) parallel edges between every two distinct vertices, and no loops. The same global label set \([q]\) is used for every parallel-edge family. Under \((g,h)\), the face \((I,c)\) becomes \((gI,c')\) with \(c'(\{gu,gv\})=h(c(\{u,v\}))\). Homology and representations are over \(\mathbb Q\). The finite-subgroup quotients are geometric quotients of the realizations, not quotients of posets formed by identifying elements.

## Proof
First, the face poset is the edge inflation of a simplex, equivalently the multiclique complex of a complete \(q\)-fold multigraph. The full-dimensional wedge theorem of Ayzenberg--Rukhovich (Theorem 1) and its finite-sheaf formulation by Ayzenberg--Khoroshavkina (Theorem 5.1, Proposition 4.12 and Corollary 7.2) give
\[
 X_{n,q}\simeq\bigvee S^{n-1}.
\]
The wedge multiplicity can be zero. Therefore the only possible nonzero reduced homology is \(\widetilde H_{n-1}\). This is a **nonequivariant** homotopy equivalence; no equivariant wedge splitting is assumed.

The regular CW cells are precisely the colored faces \((I,c)\), with a \((|I|-1)\)-cell for each one. Orient each cell by increasing vertex order. A group element \((g,h)\) contributes to the trace on that cellular chain group only for cells it fixes setwise, with local degree \(\operatorname{sgn}(g|_I)\). The reduced cellular Lefschetz number therefore equals
\[
 -1+\sum_{\varnothing\ne I\subseteq[n],\;gI=I}
 (-1)^{|I|-1}\operatorname{sgn}(g|_I)N_{g,h}(I),
\]
where \(N_{g,h}(I)\) counts compatible edge-label assignments fixed by \((g,h)\). The initial \(-1\) is the augmentation contribution. The Hopf trace formula equates this alternating cellular trace with the alternating reduced homology trace over \(\mathbb Q\).

A subset \(I\) fixed by \(g\) is a union of entire cycles, say \(I=\bigcup_{i\in J}C_i\). Its orientation sign is \((-1)^{|I|-|J|}\), so the product with \((-1)^{|I|-1}\) reduces to \((-1)^{|J|-1}\). To evaluate \(N_{g,h}(I)\), take each orbit of \(g\) on unordered pairs of vertices inside \(I\). An orbit of length \(t\) admits exactly \(f_h(t)\) color assignments fixed by the joint action: choose a label fixed by \(h^t\) for one edge and propagate it around that orbit by \(h\).

Inside a vertex cycle of length \(a\), the unordered pairs split into \(\lfloor(a-1)/2\rfloor\) orbits of length \(a\), plus, when \(a\) is even, one diametral orbit of length \(a/2\). Between vertex cycles of lengths \(a\) and \(b\), the \(ab\) cross-pairs split into \(\gcd(a,b)\) orbits, each of length \(\operatorname{lcm}(a,b)\). Thus \(N_{g,h}(I)=W_{g,h}(J)\). The reduced Lefschetz number is
\[
 -\sum_{J\subseteq[c]}(-1)^{|J|}W_{g,h}(J).
\]
Since it equals \((-1)^{n-1}\) times the sole reduced homology trace, the joint-character formula follows. Taking \(h=1\) makes every \(f_h(t)=q\), yielding \(E_g(J)\); taking also \(g=1\) yields the Betti formula.

For the quotient statement at \(n=3\), finite-group rational transfer after equivariant barycentric subdivision gives
\[
 H_*(X_{3,q}/S_3;\mathbb Q)\cong H_*(X_{3,q};\mathbb Q)^{S_3}.
\]
A transposition fixing any edge exchanges its endpoints and reverses its cellular orientation. Hence the \(S_3\)-invariant cellular one-chains vanish. Exactness of invariants over characteristic zero then implies that every \(S_3\)-invariant oriented two-chain is a cycle. There are no three-chains. The top two-chains are tensors of the \(q\)-dimensional edge-label permutation module indexed by the three edges of a triangle. The action of vertex permutations on these three edges has the same parity as the vertex permutation; the two-cell orientation contributes precisely that parity. Therefore their \(S_3\)-invariants are the alternating third tensors, canonically \(\bigwedge^3\mathbb Q^q\), equivariantly for \(S_q\). This gives the quotient statement.

## Verification
The standalone `verify.py` implements the cycle-index character and an independent fixed-cell trace by explicitly enumerating vertex subsets, permutation orbits on unordered pairs, and orientation signs. It also builds cellular boundary matrices directly from colored faces and computes their ranks over \(\mathbb F_2\) for eight finite parameter pairs. For the low-dimensional quotient it compares the averaged top character with the character of \(\bigwedge^3\mathbb Q^q\) across all color-permutation cycle types tested. Execute `python3 verify.py` using the Python standard library. The exact output is `VERIFY_OK direct_signed_character_checks= 170 exact_mod2_homology_cases= 8 exterior_cube_character_checks= 41`.

## Relationship to prior work
Ayzenberg--Rukhovich (2020 preprint, subsequently published) introduced multiclique complexes and proved the nonequivariant sphere-wedge statement for complete multigraphs, with a top Betti formula and functorial inclusions. Ayzenberg--Khoroshavkina (2026) placed these complexes in a broader framework of flabby finite étale sheaves and generalized inflations, establishing the homotopy concentration used above. The present theorem does **not** claim either wedge theorem as new. It refines their topological results to an explicit joint rational character under the commuting vertex- and edge-label permutation actions, and identifies the nontrivial color representation surviving the three-vertex quotient. The cycle-type formula, in particular its mixed \(\gcd\)/\(\operatorname{lcm}\) dependence, is not stated in either inspected source.

## Limitations
The representation is determined over \(\mathbb Q\); no integral \(S_n\times S_q\)-module decomposition, equivariant homotopy wedge splitting, or homotopy classification of the quotients is asserted. The proof uses the established nonequivariant wedge theorem as an input. Finite computations corroborate but do not substitute for the general proof. Completeness of literature searches is not a proof of historical novelty.

## References
1. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1, publicly submitted February 9, 2026, especially Proposition 4.12, Theorem 5.1 and Corollary 7.2; https://arxiv.org/abs/2602.08694.
2. A. Ayzenberg and A. Rukhovich, *Clique complexes of multigraphs, edge inflations, and tournaplexes*, arXiv:2012.07600v1, publicly submitted December 14, 2020, especially Theorem 1, formula (3.1), and Section 6; https://arxiv.org/abs/2012.07600.
