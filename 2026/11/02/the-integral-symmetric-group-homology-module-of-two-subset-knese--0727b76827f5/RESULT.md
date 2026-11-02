# The integral symmetric-group homology module of two-subset Kneser independence complexes

## Finding
For every integer \(n\ge4\), let \(KG(n,2)\) be the graph on the two-element subsets of \([n]\), with disjoint pairs adjacent, and let \(X_n=\operatorname{Ind}(KG(n,2))\). Write \(W_n=\mathbb Z^{[n]}\) for the integer permutation module and \(V_n=\ker(\epsilon:W_n\to\mathbb Z)\), where \(\epsilon(e_i)=1\). Under the natural action of \(\mathfrak S_n\), there is an **integral equivariant isomorphism**
\[
\widetilde H_2(X_n;\mathbb Z)\cong_{\mathbb Z[\mathfrak S_n]}\bigwedge^3 V_n,
\qquad
\widetilde H_j(X_n;\mathbb Z)=0\quad(j\ne2).
\]
In particular, rational homology is the irreducible hook Specht module \(S^{(n-3,1,1,1)}\), of rank \(\binom{n-1}{3}\). For a permutation with exactly \(m_d\) cycles of length \(d\), the complete degree-two character is
\[
\chi(g)=\frac{(m_1-1)(m_1-2)(m_1-3)}6-(m_1-1)m_2+m_3.
\]
The polynomial, including when \(m_1=0\), is interpreted over the integers. An explicit integral homology basis is indexed by three-element subsets of \(\{2,\ldots,n\}\).

## Assumptions and scope
The coefficient ring for the principal result is \(\mathbb Z\), not merely a field. The symmetric group acts by permuting the underlying labels, hence by simplicial automorphisms of \(X_n\); chain orientations carry the induced signs. All claims hold for each integer \(n\ge4\). Reduced homology is used, and no claim is made about general \(KG(n,k)\) for \(k>2\). The non-equivariant wedge-of-spheres homotopy type and Betti rank were established previously by Barmak [1]; the content here is the full integral symmetry module and character.

## Proof
**1. An equivariant star-and-triangle decomposition.** A face of \(X_n\) is a set of pairwise intersecting edges of the complete graph on \([n]\). Every such family is either contained in a star at some vertex, or is the three edges of a triangle. To see this, choose two intersecting edges \(ij\) and \(ik\). If a third edge avoids \(i\), it must equal \(jk\); any edge meeting all three edges of this triangle is one of those three. Let \(\sigma_i\) be the simplex consisting of all edges incident to \(i\), let \(A=\bigcup_i\sigma_i\), and write \(\tau_{ijk}\) for the 2-simplex on vertices \(ij,ik,jk\), for \(i<j<k\). Then \(X_n\) is obtained from \(A\) by adjoining exactly the \(\binom n3\) triangle 2-simplices \(\tau_{ijk}\); their boundaries lie in \(A\), while their interiors are outside \(A\). The decomposition is invariant under \(\mathfrak S_n\).

**2. An explicit equivariant graph retraction.** Distinct \(\sigma_i\) and \(\sigma_j\) intersect exactly in the vertex \(ij\), with no triple intersections. Let \(b_i\) be the barycenter of \(\sigma_i\), and \(T\) the union of the segments \([b_i,ij]\) over distinct \(i,j\). This \(T\) is a subdivision of the complete graph on \([n]\). On a point \(x\) of \(\sigma_i\) with barycentric coordinates \(\lambda_j\), let \(t\) be the largest coordinate minus the second-largest one. If the largest coordinate is uniquely at \(ij\), set \(r(x)=(1-t)b_i+t(ij)\); when it is tied, set \(r(x)=b_i\). The definition is continuous across ties, fixes all segments \([b_i,ij]\), and fixes the common vertices \(ij\), so the local definitions glue. The straight homotopy \((1-s)x+sr(x)\) within each convex \(\sigma_i\) is an \(\mathfrak S_n\)-equivariant strong deformation retraction \(A\searrow T\). Thus \(H_1(A;\mathbb Z)\) is the integral cycle lattice of \(K_n\), and \(H_j(A;\mathbb Z)=0\) for \(j\ge2\).

**3. Identifying the equivariant attaching map.** Orient \(\tau_{ijk}\) as \([ij,ik,jk]\). Permuting its three edge vertices has the same orientation sign as permuting the underlying three labels. Therefore the relative group \(H_2(X_n,A;\mathbb Z)=C_2(X_n,A;\mathbb Z)\) identifies equivariantly with \(\bigwedge^3 W_n\) by \(\tau_{ijk}\mapsto e_i\wedge e_j\wedge e_k\). In the graph \(T\), the oriented boundary of \(\tau_{ijk}\) is, up to a single global sign convention, the triangle cycle \(ij+jk-ik\). With edge orientations \(e_i\wedge e_j\) for \(i<j\), the associated connecting homomorphism is therefore, up to a global sign, the **augmentation contraction**
\[
\iota_\epsilon:\bigwedge^3W_n\longrightarrow\bigwedge^2 W_n,\qquad
\iota_\epsilon(e_i\wedge e_j\wedge e_k)
=e_j\wedge e_k-e_i\wedge e_k+e_i\wedge e_j.
\]
Its image is the entire integral cycle lattice \(\ker(\partial_1:\bigwedge^2W_n\to W_n)\): the triangles through any fixed vertex, say vertex \(1\), form an integral basis of that lattice (subtract the unique root-star paths from every edge). This is an integral-surjectivity argument, not a rank calculation over a field.

**4. Long exact sequence and integral kernel.** Since \(H_2(A)=0\), and the connecting map is surjective onto \(H_1(A)\), the long exact sequence of \((X_n,A)\) gives \(\widetilde H_1(X_n)=0\) and
\[
\widetilde H_2(X_n;\mathbb Z)\cong_{\mathbb Z[\mathfrak S_n]}\ker\iota_\epsilon.
\]
As abelian groups \(W_n=V_n\oplus\mathbb Z e_1\), so \(\bigwedge^3W_n=\bigwedge^3V_n\oplus(e_1\wedge\bigwedge^2V_n)\). Contraction kills the first summand and maps the second isomorphically onto \(\bigwedge^2V_n\). Consequently \(\ker\iota_\epsilon=\bigwedge^3V_n\), as an **invariant sublattice** of \(\bigwedge^3W_n\); the use of \(e_1\) to split groups does not claim that the splitting itself is equivariant. There is no relative homology outside degree two, so higher reduced homology vanishes; the connected graph \(A\) also gives \(\widetilde H_0(X_n)=0\).

**5. Integral basis and character.** For each \(2\le i<j<k\le n\), the wedge \((e_i-e_1)\wedge(e_j-e_1)\wedge(e_k-e_1)\) gives the relative two-chain \(\tau_{ijk}-\tau_{1jk}+\tau_{1ik}-\tau_{1ij}\), interpreted using the orientations above. Its attaching boundary is null-homologous in \(A\) over the integers and can be capped by integral 2-chains in the stars; subtracting such a cap yields an absolute 2-cycle, unique up to homology because \(H_2(A)=0\). These wedges form a lattice basis. The character generating function of the augmentation representation is
\[
\sum_{r\ge0}\operatorname{tr}(g\mid\bigwedge^r(V_n\otimes\mathbb Q))t^r
=\frac{\prod_{d\ge1}(1-(-t)^d)^{m_d}}{1+t}.
\]
Extracting the coefficient of \(t^3\) gives the stated polynomial. The standard exterior-power identity identifies \(\bigwedge^3(V_n\otimes\mathbb Q)\) with the hook Specht module \(S^{(n-3,1,1,1)}\).

## Verification
The standalone \(\texttt{verify.py}\) enumerates all faces and signed chain maps for \(4\le n\le7\), computes boundary ranks over the prime field of order \(101\), and checks the character from signed fixed-simplex traces on every permutation conjugacy class. The independently written \(\texttt{verify_alt.py}\) constructs oriented triangle boundaries directly, checks their \(\mathfrak S_n\)-equivariance on all adjacent transpositions, and checks the tetrahedral kernel identities for \(4\le n\le9\). Both programs passed when executed. These finite tests are corroboration only; the integral and all-parameter statements follow from steps 1–5.

## Relationship to prior work
Barmak [1, §4.6, Theorem 4.11] proved that this independence complex has homotopy type a wedge of \(\binom{n-1}{3}\) two-spheres. This prior result already determines ordinary homology ranks and torsion-freeness; neither is claimed new. The displayed proof in [1] uses a distinguished label in its reduction and does not identify the integral \(\mathfrak S_n\)-module, its equivariant boundary contraction, or the full character. Feng and Wang [2, introduction] explicitly cite Barmak's two-subset case and turn to the higher-subset Kneser complexes; their inspected introduction does not provide the present module formula. Closely related research records for **neighborhood** and **Čech** complexes of \(KG(6,2)\), and **stable** Kneser complexes, concern different simplicial complexes or smaller symmetry groups, so do not imply this claim. Absence of an indexed duplicate is not a priority certificate.

## Limitations
The claimed new information is the integral symmetry representation and its all-parameter character, **not** the pre-existing homotopy type, rank, or known Kneser graph facts. The proof concerns two-subset Kneser graphs only. The originality comparison is limited to inspected accessible primary literature and searchable records; an earlier equivalent integral equivariant presentation could exist in unindexed work. No independent external scholarly audit has been performed.

## References
[1] J. A. Barmak, *Star Clusters in Independence Complexes of Graphs*, arXiv:1007.0418, first public version dated 2010-07-02, especially §4.6, Theorem 4.11. https://arxiv.org/abs/1007.0418

[2] Z. Feng and G. Wang, *The Homotopy Types of Independence Complexes of Kneser Graphs*, arXiv:2404.10566 (2024), introduction. https://arxiv.org/abs/2404.10566
