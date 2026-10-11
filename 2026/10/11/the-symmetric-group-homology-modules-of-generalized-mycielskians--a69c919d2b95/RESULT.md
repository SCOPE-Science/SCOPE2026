# The symmetric-group homology modules of generalized Mycielskians of complete graphs

## Finding
For every pair of integers \(n\ge2\) and \(\ell\ge0\), let \(X_{n,\ell}\) be the independence complex of the \(\ell\)-Mycielskian of the complete graph on \(n\) labels (defined below). The symmetric group \(S_n\) acts by simultaneously permuting labels at all levels. Write \(U_n=\ker(\mathbb Q^n\xrightarrow{\sum}\mathbb Q)\) for its standard permutation-augmentation representation, and adopt \(U_n^{\otimes0}=\mathbb Q\). For each integer \(k\ge0\), there are natural-isomorphism classes of rational \(S_n\)-modules
\[
\widetilde H_i(X_{n,3k};\mathbb Q)\cong
\begin{cases}
U_n^{\otimes(k+1)}\oplus U_n^{\otimes k},&i=2k,\\
0,&i\ne2k,
\end{cases}
\]
and, for each \(q\in\{1,2\}\),
\[
\widetilde H_i(X_{n,3k+q};\mathbb Q)\cong
\begin{cases}
U_n^{\otimes(k+1)},&i=2k+1,\\
0,&i\ne2k+1.
\end{cases}
\]
The direct-sum splitting in the first formula is not asserted to be canonical. Equivalently, if \(f(g)=|\{a:g(a)=a\}|\) for \(g\in S_n\), then the entire nonzero homology character is
\[
\chi_{n,3k}(g)=f(g)(f(g)-1)^k,\qquad
\chi_{n,3k+q}(g)=(f(g)-1)^{k+1}\quad(q=1,2).
\]
Here exponent zero is interpreted as \(z^0=1\), including \(z=0\). The formulas recover the known nonequivariant homology dimensions \(n(n-1)^k\) and \((n-1)^{k+1}\), but provide all conjugacy-class traces, which the dimensions do not determine.

## Assumptions and scope
For \(n\ge2\) and \(\ell\ge0\), the graph \(G_{n,\ell}\) has vertex set \(\{(j,a):0\le j\le\ell,1\le a\le n\}\cup\{w\}\). Its edges are \(\{(j,a),(j+1,b)\}\) whenever \(0\le j<\ell\) and \(a\ne b\); all \(\{(\ell,a),(\ell,b)\}\) with \(a\ne b\); and the edges \(\{w,(0,a)\}\) for all labels. There are no other edges. This is the indexing convention in arXiv:2601.13432v1: in particular \(G_{n,0}\cong K_{n+1}\). A finite set of vertices is a face of \(X_{n,\ell}=\operatorname{Ind}(G_{n,\ell})\) exactly when it contains no edge. Each permutation of \(\{1,\ldots,n\}\) acts at every level and fixes \(w\). Homology is reduced simplicial homology with coefficients \(\mathbb Q\), including the canonical permutation signs on oriented simplices. All assertions concern this \(S_n\) action; neither integral module structure nor the full graph automorphism group is classified.

## Proof
**1. A simultaneous equivariant fold.** Suppose a finite graph \(H\) has an \(S_n\)-invariant collection of independent vertices \(U=\{u_a\}\) and a disjoint invariant collection \(V=\{v_a\}\) with \(N_H(u_a)\subseteq N_H(v_a)\) for each label. The map sending each \(v_a\) to \(u_a\) and fixing all other vertices induces an \(S_n\)-equivariant simplicial map \(F:\operatorname{Ind}(H)\to\operatorname{Ind}(H-V)\). To see this, suppose a face contains a vertex \(z\) adjacent to some \(u_a\): then \(z\in N_H(v_a)\), so the face could not contain \(v_a\). The mapped vertices \(u_a\) are pairwise nonadjacent. More strongly, for every independent face \(\sigma\), the union \(\sigma\cup F(\sigma)\) remains independent: the only added vertices are selected \(u_a\), none adjacent to any vertex of the original face by the neighborhood inclusion. Consequently the inclusion followed by \(F\) is contiguous to the identity map. The other composite is the identity on \(\operatorname{Ind}(H-V)\). The contiguity homotopy is equivariant, since \(F\) and face unions commute with label permutations. Thus the fold is an \(S_n\)-homotopy equivalence. The vertices of \(V\) need not be independent.

**2. The elementary factors.** Let \(C_n=\operatorname{Ind}(K_n)\): this consists of \(n\) isolated labeled vertices, and \(\widetilde H_0(C_n;\mathbb Q)=U_n\). Let \(B_n=\operatorname{Ind}(K_n\times P_2)\), where the product is categorical and \(P_2\) is a single edge. Its faces are two full \((n-1)\)-simplices (one in each part) and precisely \(n\) bridge edges joining corresponding labels; no bridge belongs to any higher-dimensional mixed face. Collapsing the two simplices to points is an equivariant homotopy equivalence (each simplex is an invariant contractible subcomplex with an invariant barycenter), leaving a graph with two fixed vertices and \(n\) edges permuted by \(S_n\). Its reduced homology is concentrated in degree one, with chain-kernel description \(\widetilde H_1(B_n;\mathbb Q)=\ker(\mathbb Q^n\xrightarrow{\sum}\mathbb Q)=U_n\).

**3. Decomposing the apex.** For \(\ell\ge1\), set \(A=\operatorname{Ind}(G_{n,\ell}-w)\) and \(D=\operatorname{Ind}(G_{n,\ell}-N[w])\); the standard independent-set decomposition is exactly \(X_{n,\ell}=A\cup(w*D)\), with intersection \(D\), all equivariantly. In \(G_{n,\ell}-w\), fold the entire levels \(2,5,8,\ldots\) successively onto the levels two steps before them. When processing level \(j\), intervening level \(j-1\) remains and level \(j-3\) has already been removed. Thus every surviving neighbor of \((j-2,a)\) lies in level \(j-1\) with a different label, and is also a neighbor of \((j,a)\); this remains true if level \(j\) is the top clique. The simultaneous-fold lemma applies. The surviving graph is a disjoint union of two-layer categorical-product blocks and, depending on the residue of \(\ell\), a final clique or a final adjacent two-level graph with a clique on its upper level. The latter folds equivariantly to an independent vertex layer, whose independence complex is a simplex with fixed barycenter.

For \(D\), levels zero and the apex are removed initially. Fold levels \(3,6,9,\ldots\) onto the levels two before them, again by the same neighborhood inclusion. It follows that all equivalences below are \(S_n\)-equivariant:
\[
\begin{array}{c|c|c}
\ell & A & D\\\hline
3k,\ k\ge1 & C_n*B_n^{*k} & B_n^{*k}\\
3k+1 & \text{contractible} & C_n*B_n^{*k}\\
3k+2 & B_n^{*(k+1)} & \text{contractible}.
\end{array}
\]
The joins are on disjoint labeled level blocks; the \(S_n\) action is diagonal and does not permute the block positions. Each contractible case has an equivariant contraction to the barycenter of the final independent level.

**4. Homology and the extension.** The join Künneth isomorphism over \(\mathbb Q\) gives \(\widetilde H_{2k-1}(B_n^{*k};\mathbb Q)\cong U_n^{\otimes k}\) for \(k\ge1\), \(\widetilde H_{2k}(C_n*B_n^{*k};\mathbb Q)\cong U_n^{\otimes(k+1)}\), and \(\widetilde H_{2k+1}(B_n^{*(k+1)};\mathbb Q)\cong U_n^{\otimes(k+1)}\), with vanishing in other degrees. These isomorphisms respect the diagonal coordinate action. The Mayer–Vietoris long exact sequence for \(X=A\cup(w*D)\), whose second member is contractible, implies for \(\ell=3k\) and \(k\ge1\) a short exact sequence of rational \(S_n\)-modules
\[
0\longrightarrow U_n^{\otimes(k+1)}\longrightarrow\widetilde H_{2k}(X_{n,3k};\mathbb Q)\longrightarrow U_n^{\otimes k}\longrightarrow0.
\]
The neighboring groups vanish because the factors have homology in the indicated unique degrees. This sequence splits as an abstract \(S_n\)-module by Maschke's theorem over \(\mathbb Q\); the splitting need not be canonical. For \(\ell=3k+1\), the contractibility of \(A\) shifts the unique homology of \(D\) up one degree; for \(\ell=3k+2\), contractibility of \(D\) identifies the homology of \(X\) with that of \(A\). For \(\ell=0\), the graph is \(K_{n+1}\) and the discrete \(n+1\)-point independence complex has \(\widetilde H_0\cong U_n\oplus\mathbb Q\), independently matching the first formula at \(k=0\). This proves the module statements and all homological vanishing assertions.

**5. Characters.** The permutation module \(\mathbb Q^n\) has trace \(f(g)\), so \(\chi_{U_n}(g)=f(g)-1\). A tensor-product character is the product of factor characters, and a direct-sum character is the sum. Therefore \(\chi_{3k}(g)=(f(g)-1)^{k+1}+(f(g)-1)^k=f(g)(f(g)-1)^k\) and \(\chi_{3k+q}(g)=(f(g)-1)^{k+1}\) for \(q=1,2\), with the stipulated exponent-zero convention. No argument depends on finite experimental extrapolation.

## Verification
The standalone Python 3 standard-library program `verify.py` constructs the graphs directly from the definition. It tests 76 pairwise simultaneous-fold checks, 1,144 coordinate-permutation character comparisons using independent orbit-based signed Lefschetz Euler sums, 112 separate face-by-face signed traces, and 16 exact mod-two boundary-matrix homology calculations for explicitly bounded small examples. Run `python3 verify.py` from the directory containing this file; successful replay prints `VERIFY_OK folds=76 orbit_characters=1144 direct_traces=112 mod2_homology_cases=16`. All infinite-parameter conclusions follow from the preceding mathematical proof, not from finite checks.

## Relationship to prior work
Carnero Bravo, arXiv:2601.13432v1, Theorem 5 and Corollary 7, provides the generalized-Mycielskian homotopy classification and the wedge multiplicities \(n(n-1)^k\), \((n-1)^{k+1}\). Its fold strategy motivates the invariant-level decomposition here. The additional equivariant fold proof and module calculations identify the full \(S_n\) character, which those ordinary homotopy types do not determine. Goyal, Shukla and Singh, arXiv:1905.06926v1, Theorem 4.12, also studies complete-graph generalized Mycielskians nonequivariantly, with an index shift. Comparisons of the primary full texts and searches for representation-theoretic equivalents did not yield this module formula. Those searches do not exclude an unindexed derivation.

## Limitations
The result determines rational coordinate-permutation homology modules, not canonical equivariant wedge decompositions, integral module splittings, actions of all possible graph automorphisms, or persistence under graph/filtration changes. The \(\ell=3k\) splitting is guaranteed only abstractly over \(\mathbb Q\). The equivariant homotopy equivalences of the folded subcomplexes are proved; an equivariant splitting of the full apex union is **not** claimed. No independent audit is represented as having taken place.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432v1, first public 2026-01-19, Theorem 5 and Corollary 7. https://arxiv.org/html/2601.13432v1
2. Shuchita Goyal, Samir Shukla, Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926v1, 2019, Theorem 4.12. https://arxiv.org/html/1905.06926v1
