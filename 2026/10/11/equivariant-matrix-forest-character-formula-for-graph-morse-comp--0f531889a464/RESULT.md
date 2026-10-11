# Equivariant matrix–forest character formula for graph Morse complexes

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with \(|V|\ge 1\), and let \(g\) be an automorphism. Form the ordinary discrete Morse matching complex \(\mathfrak M(G)\): its vertices are incident pairs \((v,\{v,w\})\), written \(v\to w\), and its faces are the acyclic partial matchings of the graph's incidence diagram. Write \(\mathcal O\) for the orbits of \(g\) on \(V\), and \(d_A=|A|\) for each orbit. For different orbits \(A,B\), set

\[
w_{AB}=\begin{cases}|N_G(a)\cap B|,& d_B\mid d_A,\\0,&d_B\nmid d_A,\end{cases}\qquad a\in A,
\]

and put \(w_{AA}=0\). This is independent of the choice of \(a\). Define the row-outgoing orbit Laplacian \(L_g\) by \((L_g)_{AA}=\sum_{B\ne A}w_{AB}\) and \((L_g)_{AB}=-w_{AB}\) for \(A\ne B\). Define the diagonal matrix \(D_g(t)\) by \((D_g(t))_{AA}=(-1)^{d_A-1}t^{d_A}\).

**Theorem.** With augmented simplicial chains over \(\mathbb Q\), including the empty face as a degree \(-1\) basis element, the full graded character is

\[
\boxed{\sum_{q\ge-1}\operatorname{tr}\!\left(g\mid\widetilde C_q(\mathfrak M(G);\mathbb Q)\right)t^{q+1}
=\det\!\left(I+D_g(t)L_g\right).}
\]

The sum is finite. In particular, the reduced homological Lefschetz number (with the augmented degree \(-1\) convention for the edge-free case) is

\[
\boxed{\widetilde\Lambda\!\left(g;\mathfrak M(G)\right)=-\det(I-L_g).}
\]

For the complete graph \(K_n\), if \(r_d\) counts the \(d\)-cycles of \(g\in S_n\), and \(s_d=\sum_{e\mid d,\,e<d}e r_e\), then, writing \(y_d=(-1)^{d-1}t^d\), the graded character has the explicit cycle-type factorization

\[
\boxed{F_{K_n,g}(t)=\prod_{d:r_d>0}(1+y_d s_d)\bigl(1+y_d(s_d+d r_d)\bigr)^{r_d-1}.}
\]

Consequently,

\[
\widetilde\Lambda\!\left(g;\mathfrak M(K_n)\right)
=-\prod_{d:r_d>0}(1-s_d)(1-s_d-d r_d)^{r_d-1}.
\]

All formulas hold for every graph order, every automorphism and every allowable permutation cycle type; no homology-concentration hypothesis is made.

## Assumptions and scope

The ordinary matching complex is essential: these statements concern the Chari–Joswig complex of **all** acyclic Hasse-diagram matchings of a one-dimensional simplicial complex, not the different strong discrete Morse complex. The formal variable \(t\) tracks the number of chosen incidence pairs. A chosen incidence pair \((v,\{v,w\})\) is directed as \(v\to w\), away from its matched vertex. The empty face contributes the constant term \(1\). When \(E=\varnothing\), the object has only the empty face; its augmented reduced Lefschetz number is \(-1\), agreeing with the determinant convention. No orientation choice on \(G\) enters the statement.

## Proof

**1. Functional-forest model.** A simplex of \(\mathfrak M(G)\) amounts to selecting at most one outgoing arrow \(v\to w\) at each \(v\), with \(\{v,w\}\in E\), and with no directed cycles. Indeed a Hasse matching pairs a vertex with at most one incident edge, and an edge with at most one endpoint. A directed cycle in the chosen arrows is exactly a closed gradient path; conversely a selected undirected cycle with outdegree at most one forces a directed cycle. Thus these are precisely rooted oriented forests, with roots at unused vertices [2, Proposition 3.1].

**2. Fixed faces and orbit divisibility.** A simplex is setwise fixed by \(g\) precisely when its partial successor function \(f\) is equivariant: \(f(gv)=gf(v)\), with \(f(\bot)=\bot\). All vertices in a \(g\)-orbit \(A\) are either unused or used. In the latter case \(f\) is determined by the neighbor \(b=f(a)\) of one representative \(a\in A\). Equivariance implies \(g^{d_A}b=b\), so \(b\) lies in an orbit \(B\) with \(d_B\mid d_A\). Choosing \(b\in A\) gives an equivariant cyclic shift on \(A\), hence a directed cycle, and is forbidden. For any \(B\ne A\) satisfying divisibility, there are exactly \(w_{AB}\) distinct choices for the arrow orbit \(A\to B\). Every chosen arrow orbit comprises exactly \(d_A\) incidence-pair vertices.

**3. Quotient acyclicity.** Record one arrow \(A\to B\) for each used source orbit, with the actual neighbor choice as its label. The result is a directed partial functional graph on \(\mathcal O\). A directed cycle in the original selected arrows projects to a closed directed walk in this quotient, and hence to a quotient directed cycle. Conversely, suppose the quotient has a cycle \(A_1\to\cdots\to A_k\to A_1\). Divisibility around the cycle forces all \(d_{A_i}\) to be equal. Each corresponding equivariant successor map is a bijection between cyclic orbits of the same size. Their composite is a shift of the finite cyclic orbit \(A_1\), hence periodic; an original directed cycle follows. Therefore fixed faces are in bijection with directed rooted forests on \(\mathcal O\), where each arrow \(A\to B\) has \(w_{AB}\) choices.

**4. The chain sign.** The action of \(g\) on the simplex vertices in one chosen arrow orbit of size \(d_A\) is a \(d_A\)-cycle, contributing orientation sign \((-1)^{d_A-1}\). The action on a fixed simplex has the product of these signs. Thus its contribution to the trace on the augmented simplex chain group in degree \(q\) is \(\prod_{A\text{ used}}(-1)^{d_A-1}\), with \(q+1=\sum_{A\text{ used}}d_A\). Consequently the generating character is the signed, source-weighted generating polynomial of directed rooted forests on \(\mathcal O\).

**5. Matrix–forest identity.** The directed matrix–forest theorem [4, Theorem 3, transposed to the row-outgoing convention] states that for any finite weighted directed graph with row Laplacian \(L\) and commuting source weights \(z_A\),

\[
\det(I+\operatorname{diag}(z_A)L)
=\sum_{\text{rooted directed forests }T}\prod_{A\to B\in T}z_Aw_{AB}.
\]

This also follows by expanding the principal minors of \(L\) and applying the directed all-minors matrix–tree theorem. Substituting \(z_A=(-1)^{d_A-1}t^{d_A}\) proves the graded character formula. By the alternating trace identity on augmented chain complexes, \(\widetilde\Lambda(g)=-F_{G,g}(-1)\). Since \((-1)^{d_A-1}(-1)^{d_A}=-1\), one has \(D_g(-1)=-I\), proving the reduced Lefschetz determinant.

**6. Complete-graph cycle factorization.** In \(K_n\), distinct vertex orbits of lengths \(d_A,d_B\) have \(w_{AB}=d_B\) when \(d_B\mid d_A\), and zero otherwise. Ordering orbit classes by increasing length makes \(I+D_g(t)L_g\) block triangular: arrows only point to equal-size or smaller divisor-size classes. For a fixed length \(d\) occurring \(r_d>0\) times, the corresponding diagonal block is

\[
\bigl(1+y_d(s_d+d r_d)\bigr)I_{r_d}-y_d d J_{r_d},
\]

where \(J\) is the all-ones matrix. Its eigenvalue on the constant vector is \(1+y_ds_d\), and its other \(r_d-1\) eigenvalues are \(1+y_d(s_d+d r_d)\). Multiplying their products over all lengths proves the explicit cycle-type formula. Evaluating at \(t=-1\) proves the final expression. This calculation is valid even if some factors vanish; no inversion is used.

## Verification

The included standalone `verify.py` uses exact rational Gaussian elimination for integer determinants and independently enumerates acyclic partial successor functions with their induced orientation signs. It tests the entire graded polynomial by evaluation at more points than its maximum degree, for **every** graph and automorphism with one through four labeled vertices: **293** graph–automorphism instances. It independently checks the \(K_n\) cycle-type Lefschetz factorization for every permutation on \(2\le n\le6\), and the full graded trace on three six-vertex examples, including two distinct symmetries of \(K_{3,3}\). The command is `python3 verify.py`; the observed output is recorded in `VERIFICATION.md`. The proof for arbitrary order is symbolic and does not rely on extrapolating these tests.

## Relationship to prior work

Chari and Joswig [2, Proposition 3.1 and Corollary 3.3] identify ordinary graph Morse simplices with rooted forests and determine the nonequivariant face polynomial from the usual Laplacian; setting \(g=1\) in the present theorem recovers that statement. Contreras and Tawfeek [3, Theorem 3.5] rederive this nonequivariant Laplacian enumeration. Chebotarev and Shamis [4] establish the directed matrix–forest determinant needed here, but do not identify the orbit-divisibility quotient of graph Morse matchings or its chain orientation signs. General simplicial Lefschetz fixed-simplex signs are standard [5]. Kozlov [6, Section 6] studies the \(S_n\)-quotient of the complete directed-forest complex and its invariant homology, but does not state the individual graded character in the displayed orbit-Laplacian form. The recent work [1] renews study of Morse-matching complexes and distinguishes their ordinary and strong versions, without supplying the present equivariant graph formula in the accessible abstract. The novelty claim is the **uniform all-graph equivariant graded character and orbit-Laplacian reduction**, not any of these constituent facts individually.

## Limitations

The formula determines the action on augmented chain groups and the alternating trace on reduced homology; it does **not** by itself determine each homology representation or a homotopy type for an arbitrary graph. In contrast with the usual graph Laplacian, the orbit Laplacian is generally nonsymmetric and may have nonzero weights only in one direction between unequal-length orbits. The complete 2026 preprint [1] was not accessible during the comparison; its public abstract was checked, so an incidental equivalence in its full text cannot be ruled out solely from that abstract. Other unindexed equivalent treatments of equivariant rooted-forest enumeration may exist. No independent validation has been performed.

## References

[1] K. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first public 2026-09-06), https://arxiv.org/abs/2609.06844.

[2] M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234 (2000), https://arxiv.org/pdf/math/0011234, especially Proposition 3.1 and Corollary 3.3.

[3] I. Contreras and A. R. Tawfeek, *On discrete gradient vector fields and Laplacians of simplicial complexes*, arXiv:2105.05388v2 (2022), https://arxiv.org/pdf/2105.05388, especially Theorem 3.5 and Remark 4.

[4] P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, arXiv:math/0602575v2, https://arxiv.org/pdf/math/0602575, especially directed Theorem 3.

[5] O. Knill, *A Brouwer fixed-point theorem for graph endomorphisms*, Fixed Point Theory Appl. **2013**, article 85, https://doi.org/10.1186/1687-1812-2013-85, especially Section 3.

[6] D. N. Kozlov, *Spectral sequences on combinatorial simplicial complexes*, J. Algebraic Combin. **14** (2001), 27–48, https://doi.org/10.1023/A:1011209803008, especially Section 6.
