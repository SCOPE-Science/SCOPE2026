# Complete ternary translation character of the radius-two Hamming Rips complex

## Finding

Let \(V=(\mathbb Z/3\mathbb Z)^3\), endowed with Hamming distance \(d_H(u,v)=|\{i:u_i\ne v_i\}|\). Let \(K\) be the **inclusive radius-two Vietoris--Rips complex**: a nonempty subset \(\sigma\subseteq V\) is a face exactly when \(d_H(u,v)\le2\) for every \(u,v\in\sigma\). The translation group \(A=V\) acts on \(K\) by \(t_a(v)=v+a\). For a vector \(a\), write \(\operatorname{wt}(a)=|\{i:a_i\ne0\}|\).

The only nonzero reduced rational homology of \(K\) is
\[
\widetilde H_3(K;\mathbb Q)\cong\mathbb Q^{46}.
\]
**The new equivariant assertion** is that its complete character under the 27 translations depends only on the weight:
\[
\boxed{\operatorname{tr}\bigl(t_a\mid\widetilde H_3(K;\mathbb Q)\bigr)
=\begin{cases}46,&\operatorname{wt}(a)=0,\\4,&\operatorname{wt}(a)=1,\\-2,&\operatorname{wt}(a)=2,\\1,&\operatorname{wt}(a)=3.\end{cases}}
\]
Set \(\omega=e^{2\pi i/3}\). For every \(\xi\in A\), let \(\lambda_\xi(a)=\omega^{\xi\cdot a}\). The multiplicity of \(\lambda_\xi\) in \(\widetilde H_3(K;\mathbb C)\) is precisely
\[
\boxed{m_\xi=\begin{cases}2,&\operatorname{wt}(\xi)\le2,\\1,&\operatorname{wt}(\xi)=3.\end{cases}}
\]
Equivalently, as a complex representation,
\[
\widetilde H_3(K;\mathbb C)\cong\mathbb C[A]\oplus
\bigoplus_{\operatorname{wt}(\xi)\le2}\mathbb C_{\lambda_\xi}.
\]
There are 19 characters in the second summand. In particular the invariant subspace has dimension two, and the finite quotient \(|K|/A\) has reduced rational homology \(\mathbb Q^2\) in degree three and zero in every other degree.

## Assumptions and scope

This concerns the specific finite 27-point ternary Hamming metric, at **weak distance threshold two**. The homology-character assertion is over characteristic-zero fields; it does not classify the integral \(\mathbb Z[A]\)-lattice. Vertex coordinates are ordered lexicographically \((x,y,z)\leftrightarrow9x+3y+z\). We treat all 27 translations, not the full wreath-product automorphism group. The geometric action can fix barycenters of simplices even when it fixes no vertices.

## Proof

**1. Topological homology input, independently reconstructed.** Two vertices are forbidden to share a Rips face if and only if all their coordinates differ. Hence
\[
K=\operatorname{Ind}(K_3\times K_3\times K_3),
\]
with the categorical graph product. Enumerating the nonempty cliques of the allowed-pair graph by lexicographically increasing vertex backtracking yields exactly 5,949 faces, with dimension-indexed vector
\[
(f_0,\ldots,f_8)=(27,243,945,1728,1620,945,351,81,9).
\]
Here is a completely specified finite Morse matching. Initially mark every nonempty face unmatched. For \(i=0,\ldots,26\), take every still-unmatched face \(\sigma\) not containing vertex \(i\), pair it with \(\sigma\cup\{i\}\) whenever the latter is also unmatched, and remove both faces. Order the simultaneous pairs within each stage by increasing 27-bit face mask. The accompanying **independent standalone verifier** reconstructs these faces and pairs directly from the metric. It obtains 2,951 valid pairs and 47 critical faces: one vertex and exactly 46 three-simplices. It builds the *entire* codimension-one face-poset graph, orients every matched covering relation upward and every other relation downward, and topologically sorts all 5,949 vertices across 27,189 directed incidences. Every vertex is visited, proving acyclicity. Forman's finite acyclic-matching theorem gives a CW complex with one zero-cell and 46 three-cells, and no cells in degrees one or two; all attaching maps land at the sole point. Thus \(K\simeq\bigvee^{46}S^3\), so its ordinary rational homology has exactly the stated concentration. As a separate diagnostic, exact mod-two boundary ranks are \((26,217,728,954,666,279,72,9)\). The quoted homotopy type is previously recorded in the sources; it is **not** asserted as a new finding here.

**2. Lefschetz reduction.** For any translation \(a\), the alternating signed trace on the simplicial chains equals the alternating trace on homology. Since \(K\) is connected with only reduced degree-three homology, its ordinary Lefschetz number \(L(a)\) satisfies
\[
L(a)=1-\operatorname{tr}(t_a\mid\widetilde H_3(K;\mathbb Q)).
\]
For \(a\ne0\), every vertex orbit has length three. Any face fixed setwise by \(t_a\) is a disjoint union of complete translation orbits, each of cardinality three. The vertex permutation on such a face is a product of three-cycles, hence has positive orientation sign. A union of \(k\) orbits contributes \((-1)^{3k-1}=(-1)^{k-1}\) to \(L(a)\). Consequently \(L(a)\) is the Euler characteristic of the abstract complex of admissible subsets of the nine translation orbits.

**3. Classification of fixed orbit complexes.** If \(\operatorname{wt}(a)=1\), assume the translation varies only the first coordinate. The nine orbits are indexed by the unchanged pair \((y,z)\in\mathbb F_3^2\). Two orbits can be united into a face exactly when their indices agree in \(y\) or \(z\): if both differ, choose vertices with differing first coordinates and obtain forbidden Hamming distance three. Thus the orbit complex is the clique complex of the \(3\)-by-\(3\) rook graph. Its face counts are \((9,18,6)\), and \(L(a)=9-18+6=-3\).

If \(\operatorname{wt}(a)=2\), the third coordinate remains fixed. Orbits with the same third coordinate may be united freely, since all points share that coordinate. Orbits with distinct third coordinates cannot be united: among relative phase choices in the two varying coordinates, choose a pair differing in both, producing Hamming distance three. There are three orbits in each of three fixed-coordinate layers, so the orbit complex is a disjoint union of three filled triangles, with face counts \((9,9,3)\). Hence \(L(a)=9-9+3=3\).

If \(\operatorname{wt}(a)=3\), all three vertices in any nontrivial translation orbit differ in every coordinate. No complete orbit spans a face. There are no nonempty invariant faces and \(L(a)=0\).

For \(a=0\), the trace on \(\widetilde H_3\) is its already established dimension 46; equivalently the face vector gives Euler characteristic \(-45\). Substituting the three values of \(L(a)\) into the Lefschetz relation proves the four-case trace formula.

**4. Character multiplicities.** The characters of \(A\) are the \(\lambda_\xi\), each one-dimensional over \(\mathbb C\). Orthogonality gives
\[
m_\xi=\frac1{27}\sum_{a\in A}\operatorname{tr}(t_a)\,\omega^{-\xi\cdot a}.
\]
If \(k=\operatorname{wt}(\xi)\), then the weighted number of translation vectors of each Hamming weight is encoded by
\[
P_k(t)=(1-t)^k(1+2t)^{3-k}.
\]
Indeed, summing \(\omega^{-\xi_i a_i}\) over the two nonzero choices of \(a_i\) gives \(-1\) for nonzero \(\xi_i\) and \(2\) for zero \(\xi_i\). Therefore
\[
27m_\xi=46[t^0]P_k(t)+4[t^1]P_k(t)-2[t^2]P_k(t)+[t^3]P_k(t).
\]
For \(k=0,1,2,3\), the respective numerators are \(54,54,54,27\). This proves multiplicities \(2,2,2,1\). Counting characters by weight gives \(2(1+6+12)+8=46\), consistent with the chain calculation.

**5. Quotient.** In characteristic zero, barycentric subdivision makes this finite simplicial group action without inversions; the quotient chain complex identifies with invariant chains. Taking invariants is exact over \(\mathbb Q\). The quotient's rational homology is therefore the invariant part of the original rational homology. Precisely two copies of the trivial character occur, proving the quotient statement.

## Verification

The accompanying standard-library-only `verify.py` reconstructs the complete face set, matching, directed Hasse acyclicity, and all mod-two boundary ranks from the 27 labeled triples; it does not import numerical certificates or external data. It independently calculates signed fixed-simplex Lefschetz numbers for all 27 translations, enumerates the nine-orbit quotient complexes for representatives of weights one, two, and three, and computes all Fourier multiplicities with **integer arithmetic**, not floating approximations. Successful replay is recorded in `verification_output.txt`. The finite exhaustive steps are complete for this precise 27-point object, not an extrapolation to other alphabet sizes.

## Relationship to prior work

Adamaszek's 2011 paper provides the graph-power-to-Rips framework and cycle-power calculations, not the ternary Hamming translation action [1]. Goyal--Shukla--Singh prove two-factor categorical complete-graph independence-complex results [2]; Antolín Camarena--Carnero Bravo prove the three-factor case when one factor is \(K_2\), and conjecture a nonequivariant three-factor formula [3]. Two publicly indexed 2026 analyses prove the **same** 27-point nonequivariant homotopy type and barcode [4,5], but their complete inspected scientific statements and proofs do not compute translation traces, Fourier multiplicities, or rational translation-quotient homology. This finding therefore claims **only the equivariant refinement**, not the known rank or homotopy classification. Galetto--Montaño--Wellner treat the binary hypercube and its hyperoctahedral action [6]; their stated domain does not include the ternary alphabet. The separate neighborhood complex \(\mathcal N(H(3,3))\) is not the radius-two Rips complex and cannot imply this character merely from its Betti numbers.

## Limitations

The representation is restricted to the translation subgroup, not the entire automorphism group. The claim is over rational/complex coefficients and does not determine the integral module, equivariant homotopy type, integral homology of the quotient, or the corresponding results for general ternary dimensions. Although the relevant indexed results and full relevant primary statements were compared, an equivalent unindexed computation cannot be excluded; independent scientific validation has not occurred.

## References

[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first submitted 2011-04-03, https://arxiv.org/abs/1104.0433 .

[2] S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, https://arxiv.org/abs/1905.06926 .

[3] O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, Proposition 25 and Conjecture 26, https://arxiv.org/html/2307.12401v2 .

[4] *The ternary Hamming Rips filtration and the \(K_3\times K_3\times K_3\) case*, published research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-ternary-hamming-rips-filtration-and-the-k-3-times-k-3-times--964b171a73c5 .

[5] *Complete Vietoris--Rips persistence of the ternary three-cube*, published research record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-of-the-ternary-three-cube--62d7487289d8 .

[6] F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris--Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, https://arxiv.org/abs/2606.20784 .
