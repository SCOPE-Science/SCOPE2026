# A sharp parity criterion and Jordan census for edge-parity dynamics on Hamming products

## Finding
Let \(r\ge2\), and let \(m_1,\ldots,m_r\ge2\) be integers. Set \(G=K_{m_1}\square\cdots\square K_{m_r}\), with \(F\) the synchronous, open-neighborhood neighbor-sum update on the line graph \(L(G)\) over any finite field \(\mathbb F_q\) of characteristic two. The vertex of \(L(G)\) representing an edge of \(G\) sums the states of all other edges sharing an endpoint with it.

**Sharp parity dichotomy.** The matrix \(F\) is nilpotent if and only if every \(m_i\) is even. If some \(m_i\) is odd, \(F\) has a nonzero fixed configuration, explicitly constructed in the proof.

**Complete all-even classification.** If all \(m_i\) are even, define
\[
N=\prod_{i=1}^{r}m_i,\qquad D=\sum_{i=1}^{r}(m_i-1),\qquad E=ND/2,\qquad H=\prod_{i=1}^{r}(m_i-2).
\]
Then \(L(G)\) has \(E\) vertices and \(F^3=0\). Over \(\mathbb F_q\), the complete Jordan form is
\[
F\sim J_3(0)^{\oplus ((N-H)/2-2)}\oplus J_2(0)^{\oplus(H+2)}\oplus J_1(0)^{\oplus((N(D-3)-H)/2+2)}.
\]
Equivalently,
\[
\operatorname{rank}F=N-2,\qquad \operatorname{rank}F^2=(N-H)/2-2,\qquad \operatorname{rank}F^3=0.
\]
For \(t\in\{0,1,2,3\}\), the numbers \(C_t\) of configurations whose **first** arrival at zero is at update \(t\) are
\[
\begin{aligned}
C_0&=1,\\
C_1&=q^{E-N+2}-1,\\
C_2&=q^{E-(N-H)/2+2}-q^{E-N+2},\\
C_3&=q^E-q^{E-(N-H)/2+2}.
\end{aligned}
\]
Zero is the unique periodic state. The nilpotency index is exactly three except for \((m_1,m_2)=(2,2)\), where it is two. The integers \(H\) and \(H+2\) respectively measure the tensor-homology obstruction and the number of two-step nilpotent Jordan blocks.

## Assumptions and scope
Graphs are finite, simple, undirected, and loopless. The Cartesian product has tuples \((a_1,\dots,a_r)\) as vertices, with exactly one coordinate changing along an edge. Each \(m_i\ge2\), \(r\ge2\), and \(\mathbb F_q\) is any field with \(q=2^s\) elements and \(s\ge1\). The line graph has one vertex for every original edge and an adjacency exactly when two distinct edges share an endpoint. The edge-update matrix is the unweighted adjacency matrix of that line graph (no self-loops). The all-even formulas exclude no tuples beyond the stated conditions. The odd-factor statement guarantees at least one nonzero fixed point but does not classify all its orbits.

## Proof
**1. Incidence reduction.** Put \(B\in\mathbb F_q^{N\times E}\) for the unsigned vertex-edge incidence matrix of \(G\). In characteristic two, every column of \(B\) has two ones. Since distinct edges of a simple graph meet in at most one endpoint,
\[
F=B^{\mathsf T}B,\qquad L=BB^{\mathsf T},\qquad F^2=B^{\mathsf T}LB,\qquad F^3=B^{\mathsf T}L^2B.
\]
Here \(L\) is the characteristic-two graph Laplacian. As \(G\) is connected, the image of \(B\) is the coordinate-sum-zero hyperplane \(W\subseteq\mathbb F_q^N\), and \(\ker B^{\mathsf T}=\langle\mathbf 1\rangle\), where \(\mathbf1\) is the all-ones vector.

**2. Product Laplacian.** On each factor \(K_{m_i}\), its characteristic-two Laplacian is \(L_i=(m_i\bmod2)I+J_{m_i}\), where \(J_{m_i}\) is the all-ones matrix. Accordingly,
\[
L=\sum_{i=1}^r I\otimes\cdots\otimes L_i\otimes\cdots\otimes I.
\]
If every \(m_i\) is even, each \(L_i=J_{m_i}\), and \(L_i^2=m_iJ_{m_i}=0\). Different tensor summands commute and all cross terms cancel in characteristic two, hence \(L^2=0\). By step 1, \(F^3=0\).

**3. Exact rank of \(L\).** For each even \(m_i\), choose a vector \(a_i\) of coordinate sum one and let \(b_i=\mathbf1\). Then \(J_{m_i}a_i=b_i\), \(J_{m_i}b_i=0\). A complementary \((m_i-2)\)-dimensional subspace of \(\ker J_{m_i}\) is killed by \(J_{m_i}\). Thus the complex \((\mathbb F_q^{m_i},J_{m_i})\) splits as one contractible two-block plus \(m_i-2\) isolated one-blocks. In their tensor product with differential \(L\), any summand containing a two-block is contractible: use the homotopy that sends its \(b_i\) to \(a_i\) and annihilates \(a_i\); other-coordinate terms anticommute with this homotopy because their twice-occurring cross terms vanish in characteristic two. Only the all-one-block tensor summand survives, and it has dimension \(H=\prod_i(m_i-2)\). Since \(L^2=0\), its homology has dimension \(N-2\operatorname{rank}L\). Therefore
\[
\operatorname{rank}L=(N-H)/2.
\]
This argument works unchanged over every characteristic-two field.

**4. Exact edge ranks.** All-even factors imply \(N\) is even, so \(\mathbf1\in W\). Step 1 gives \(\operatorname{rank}F=(N-1)-1=N-2\). To compute the second rank, select one factor \(i\) and a coordinate unit vector \(e\) there. Since \(r\ge2\), the vector \(x=e\otimes\bigotimes_{j\ne i}\mathbf1_j\) has coordinate sum zero. Moreover \(Lx=\mathbf1\), so \(\mathbf1\in L(W)\). As \(L\) is symmetric and \(\mathbf1\in\operatorname{im}L\), every vector in \(\ker L\) has coordinate sum zero, so \(\ker L\subseteq W\). Consequently \(\dim L(W)=\operatorname{rank}L-1\). Applying \(B^{\mathsf T}\) kills exactly the all-ones line in \(L(W)\), proving
\[
\operatorname{rank}F^2=\operatorname{rank}L-2=(N-H)/2-2.
\]
The Jordan multiplicity of length three is \(\operatorname{rank}F^2\), of length two is \(\operatorname{rank}F-2\operatorname{rank}F^2\), and of length one is \(E-2\operatorname{rank}F+\operatorname{rank}F^2\). Substitution yields the displayed Jordan form. Since \(\dim\ker F^t=E-\operatorname{rank}F^t\), successive differences of \(q^{\dim\ker F^t}\) give the four first-zero-time populations. The expression for \(\operatorname{rank}F^2\) vanishes precisely for the two-factor product \(K_2\square K_2\), establishing sharpness.

**5. Odd-factor obstruction.** Suppose some \(m_i\) is odd. On that factor, \(L_i=I+J_{m_i}\), so \(L_i(e_0+e_1)=e_0+e_1\). Every other factor Laplacian annihilates its all-ones vector. Therefore
\[
v=(e_0+e_1)_i\otimes\bigotimes_{j\ne i}\mathbf1_j
\]
is a nonconstant eigenvector of \(L\) with eigenvalue one and has coordinate sum zero. Put \(y=B^{\mathsf T}v\). Connectedness makes \(y\ne0\), and
\[
Fy=B^{\mathsf T}BB^{\mathsf T}v=B^{\mathsf T}Lv=B^{\mathsf T}v=y.
\]
Thus the edge dynamics has a nonzero fixed configuration and cannot be nilpotent. Together with steps 2–4, this proves the if-and-only-if statement.

## Verification
Two independently structured bit-matrix programs are supplied in `verification/verify_hamming.py` and `verification/verify_hamming.cpp`. Run `python3 verification/verify_hamming.py`; compile and run `g++ -std=c++17 -O2 verification/verify_hamming.cpp -o verify_hamming && ./verify_hamming`. The Python program computes binary matrix ranks of the first three edge-update powers for fourteen all-even products, including \((4,4,4)\) with \(288\) edge states, and directly constructs and verifies nonzero fixed configurations for seven odd-factor products. The C++ program independently constructs edges by coordinate differences and computes ranks for seven all-even products, then exhaustively enumerates all binary configurations on products with \(4\), \(12\), and \(16\) edges. Both outputs are embedded as text files. These finite checks independently corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Davis, Domke and Garner (2004) studied ordinary real adjacency ranks of line graphs, including products of complete graphs; their spectral calculations are over characteristic zero and do not determine characteristic-two nilpotent Jordan blocks or first-zero-time distributions. Fish, Key and Mwambene (2010) analyzed binary codes from line graphs of Boolean cubes and codes from Hamming graphs; these address related matrices and include important rank/code antecedents. A previously recorded cube-edge calculation (opaque identifier `5c15f12b-1ac7-45d5-a0a4-6e6ef1df96ac`) already covers the all-\(m_i=2\) specialization of the present result, which is **not** claimed to be new here. The substantive added assertions concern arbitrary products of even-order cliques, the nontrivial tensor-homology term \(H\), and necessity of evenness through explicit fixed states in every odd-factor case. General linear cellular-automaton results, such as Zaidenberg (2006), are background and do not by themselves supply these edge-network Jordan multiplicities.

## Limitations
The theorem is limited to open-neighborhood edge-sum dynamics in characteristic two and Cartesian products of complete graphs; it does not claim the same bound for weighted rules or other characteristics. For odd-factor products, the theorem proves existence of a nonzero fixed state rather than a full recurrent census. Earlier code-theoretic full texts from 2010 were not accessible in this assessment; their abstracts and source records were checked, but the absence of an equivalent statement in their complete texts is not asserted. Such unavailable material and unindexed publications remain originality risks. The finite enumerations and sampled ranks are supplementary to the algebraic proof, not exhaustive over parameters.

## References
1. G. J. Davis, G. S. Domke, C. R. Garner Jr., *Ranks of Line Graphs of Regular Graphs*, J. Combin. Math. Combin. Comput. **49** (2004), 113–128. Published 31 May 2004. https://combinatorialpress.com/jcmcc-articles/volume-049/ranks-of-line-graphs-of-regular-graphs/ . Relevant pages 113 and 125–127 examined in full-paper scans.
2. W. Fish, J. D. Key, E. Mwambene, *Binary codes from the line graph of the n-cube*, J. Symbolic Comput. **45** (2010), 800–812. https://doi.org/10.1016/j.jsc.2010.03.012 . Abstract and indexed manuscript opening examined; complete manuscript was inaccessible.
3. W. Fish, J. D. Key, E. Mwambene, *Codes from incidence matrices and line graphs of Hamming graphs*, Discrete Math. **310** (2010), 1884–1897. https://doi.org/10.1016/j.disc.2010.02.010 . Abstract examined; full article unavailable.
4. M. Zaidenberg, *Convolution equations on lattices: periodic solutions with values in a prime characteristic field*, arXiv:math-ph/0606070, first posted 29 June 2006. https://arxiv.org/abs/math-ph/0606070 . Background scope assessed from abstract.
