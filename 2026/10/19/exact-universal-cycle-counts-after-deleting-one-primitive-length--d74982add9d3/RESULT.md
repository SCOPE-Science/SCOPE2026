# Exact universal-cycle counts after deleting one primitive length-three necklace

## Finding
For a fixed alphabet \(\Sigma\) with \(q\ge3\) labeled symbols, let \(w\in\Sigma^3\) be primitive (that is, not constant). Delete the complete orbit \(\mathcal R(w)=\{w,\rho(w),\rho^2(w)\}\) under cyclic rotation. Let \(U_q(w)\) be the number, modulo cyclic rotations of positions **only**, of cyclic strings whose length-three cyclic factors are exactly the \(q^3-3\) members of \(\Sigma^3\setminus\mathcal R(w)\), each appearing once. Reversal and alphabet relabeling are not identified.

There are precisely two cases up to relabeling. Write \(D_q=(q!)^{q^2}/q^3\), the total number of order-three de Bruijn cycles on the same labeled alphabet. If \(w\) has two equal symbols, then
\[
U_q(w)=\frac{D_q}{(q-1)^3}\frac{(q-2)(q^2-q+1)}{q^3}.
\]
If all three symbols of \(w\) are different, then
\[
U_q(w)=\frac{D_q}{(q-1)^3}\frac{q^4-3q^3+3q^2-3q+3}{q^4}.
\]
In particular both counts equal \(12096\) when \(q=3\). For every \(q\ge4\), deleting an orbit with two equal symbols yields strictly more cycles than deleting an orbit with all distinct symbols: the respective normalized arborescence factors differ by \((q-3)/q^4\). The binary two-equal-symbol boundary has no such universal cycle.

## Assumptions and scope
The alphabet symbols are individually labeled. A cyclic string is an equivalence class under rotation of **positions**, not rotation of labels or reversal. Each cyclic factor occurrence is indexed by its starting position. The factor set contains every possible three-letter word except the three distinct cyclic rotations of one nonconstant word; no multiplicities are allowed. The theorem counts finite circular words for every integer \(q\ge3\); the binary no-cycle observation is supplementary.

## Proof
**Step 1: Directed de Bruijn graph and reduced degrees.** Let \(V=\Sigma^2\), \(N=q^2\), and let the complete graph have, for every triple \(abc\), one directed edge \((a,b)\to(b,c)\) bearing that triple. Write \(A\) for its adjacency matrix. Each vertex has indegree and outdegree \(q\); moreover \(A^2=J\), the all-ones matrix, because there is exactly one directed walk of length two between any specified ordered pair of vertices. Removing the orbit \(\mathcal R(w)\) deletes one directed three-cycle with pairwise distinct vertices \(v_i=(w_i,w_{i+1})\), indices modulo three. The resulting graph is balanced, with degrees \(q-1\) at those three vertices and \(q\) elsewhere. Its Eulerian circuits, modulo cyclic rotation, correspond bijectively to the counted words, since edges carry distinct triples.

**Step 2: Unperturbed tree determinant.** Let \(L=qI-A\), let \(P=J/N\), and put
\[
G=(L+P)^{-1}-P=\frac Iq+\frac A{q^2}-\frac{2P}{q}.
\]
Indeed \(LP=0\), \(A^2=q^2P\), \(LG=I-P\), and \(G\mathbf1=0\). Since the eigenvalues of \(A\) are \(q\) once and zero \(N-1\) times (counting algebraic multiplicity), the directed matrix-tree theorem gives \(t_0=q^{N-3}\) in-arborescences rooted at any fixed vertex. Equivalently, \(\det(L+P)=Nt_0\).

**Step 3: Exact rank-three deletion.** With \(e_v\) a vertex coordinate vector, define matrices whose columns are \(X_i=e_{v_i}\) and \(Y_i=e_{v_i}-e_{v_{i+1}}\). The reduced Laplacian is \(L'=L-XY^T\). The determinant lemma and the directed matrix-tree theorem give
\[
\frac t{t_0}=\frac{\det(L'+P)}{\det(L+P)}
=\det(I_3-K),\qquad
K_{ij}=\frac{[v_i=v_j]-[v_{i+1}=v_j]}q
+\frac{[\operatorname{suffix}(v_i)=\operatorname{prefix}(v_j)]-[\operatorname{suffix}(v_{i+1})=\operatorname{prefix}(v_j)]}{q^2}.
\]
The \(P\)-terms cancel because the differences in \(Y_i\) sum to zero. In the two classes, take the representative \(w=001\) or \(w=012\). Their respective \(K\) matrices are
\[
K_{001}=\begin{pmatrix}
q^{-1}+q^{-2}&-q^{-1}+q^{-2}&-q^{-2}\\
-q^{-2}&q^{-1}-q^{-2}&-q^{-1}+q^{-2}\\
-q^{-1}&0&q^{-1}
\end{pmatrix},\qquad
K_{012}=\begin{pmatrix}
q^{-1}&-q^{-1}+q^{-2}&-q^{-2}\\
-q^{-2}&q^{-1}&-q^{-1}+q^{-2}\\
-q^{-1}+q^{-2}&-q^{-2}&q^{-1}
\end{pmatrix}.
\]
Direct three-by-three determinants yield
\[
\frac{t_{001}}{t_0}=\frac{(q-2)(q^2-q+1)}{q^3},\qquad
\frac{t_{012}}{t_0}=\frac{q^4-3q^3+3q^2-3q+3}{q^4}.
\]
These are positive for all \(q\ge3\). Positivity of the directed tree cofactor means the balanced graph has an in-arborescence; balance then forces strong connectivity on its nonzero-degree vertices. Thus the BEST theorem applies.

**Step 4: Euler tour count and simplification.** For either case, BEST counts directed Euler circuits up to cyclic edge rotation as
\[
U_q(w)=t_w\,((q-2)!)^3((q-1)!)^{q^2-3}.
\]
Every edge has a distinct triple label, so neither nontrivial rotational periodicity nor additional quotienting is possible. Substituting \(t_w=q^{q^2-3}\det(I_3-K)\), and \(q!=q(q-1)!\), gives the two asserted forms with \(D_q=(q!)^{q^2}/q^3\). Their determinant-factor difference is exactly \((q-3)/q^4\); this establishes equality at \(q=3\) and a strict inequality thereafter. For \(q=2\), the repeated-symbol determinant vanishes and the balanced graph has no Euler tour.

## Verification
The accompanying self-contained `verify.py` (Python 3 standard library only) independently constructs the reduced graph and its integral Laplacian from all allowed triples; computes a cofactor by exact fraction-free Bareiss elimination for every \(2\le q\le6\) for applicable classes; evaluates the separate rank-three determinant with rational arithmetic; and checks the two closed formulas. For \(q=2,3\), it additionally enumerates all Euler circuits directly by depth-first search after fixing the first uniquely labeled edge. The complete ternary counts are \(12096\) for each class. This finite replay corroborates, but does not replace, the all-\(q\) determinant proof. Run `python3 verify.py` from the package directory and require the final line `ALL_CHECKS_PASS`.

## Relationship to prior work
Au, *Generalized de Bruijn words for Primitive words and Powers* (first arXiv version 2009), constructs cycles using **all** primitive factors. Kociumaka–Radoszewski–Rytter (conference 2014, expanded arXiv 2015) algorithmically rank Lyndon words and decode lexicographically minimal full-dictionary de Bruijn cycles; this does not enumerate tours of a one-orbit-deleted graph. Sawada–Williams–Wong (2016) construct lexicographically smallest cycles for several rotation-closed dictionaries, notably complements of **periodic** necklaces, but do not count all cycles after deleting exactly one **primitive** length-three orbit. Chen–Kitaev–Sun (2019) determine existence probabilities for at most two forbidden factors in general alphabets and finite binary cases; the present three-factor count for every \(q\ge3\) is not a stated result of that paper. The standard matrix-tree/BEST formulas supply generic counting machinery, not the evaluated two-class expressions.

## Limitations
This proof treats exactly one primitive necklace of length three, not multiple deleted necklaces, not other factor lengths, and not dictionaries with arbitrary restrictions. Counts are not quotient by symbol permutations or reversal, and do not address compression, algorithms for ranking the resulting cycles, or any asymptotic uncertainty in other regimes. The close-source comparison does not certify priority over all possible earlier or unindexed literature. No independent audit has been performed.

## References
1. Y. H. Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997v1 (2009); published *Discrete Mathematics* 338 (2015), 2320–2331.
2. T. Kociumaka, J. Radoszewski, W. Rytter, *Computing k-th Lyndon Word and Decoding Lexicographically Minimal de Bruijn Sequence*, CPM (2014), doi:10.1007/978-3-319-07566-2_21; expanded arXiv:1510.02637v1.
3. J. Sawada, A. Williams, D. Wong, *Generalizing the Classic Greedy and Necklace Constructions of de Bruijn Sequences and Universal Cycles*, *Electronic Journal of Combinatorics* 23(1) (2016), #P1.24, doi:10.37236/5517.
4. H. Z. Q. Chen, S. Kitaev, B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116v1 (2019).
5. The directed matrix-tree theorem and the BEST enumeration theorem, in their classical forms.
