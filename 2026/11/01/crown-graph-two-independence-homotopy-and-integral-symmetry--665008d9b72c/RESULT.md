# Crown-graph two-independence homotopy and integral symmetry

## Finding

For each integer \(n\geq 3\), let \(C_n\) be the crown graph with vertex set \(A\sqcup B\), where \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), and with edges \(a_i b_j\) exactly when \(i\ne j\). This is the graph obtained from \(K_{n,n}\) by removing one perfect matching. Define the two-independence (dissociation) complex
\[
X_n=\operatorname{Ind}_2(C_n)=\{\sigma\subseteq A\sqcup B:\operatorname{maxdeg}(C_n[\sigma])\leq 1\},
\]
where \(\operatorname{maxdeg}(H)\) denotes the maximum vertex degree of a graph. Then, **for every** \(n\geq3\),
\[
\boxed{X_n\simeq\bigvee^{\binom{n-1}{2}} S^2.}
\]
Moreover, the full graph automorphism group is \(\mathfrak S_n\times C_2\). Let
\[
V_n=\ker\!\left(\mathbb Z^n\xrightarrow{\text{sum}}\mathbb Z\right),
\]
with its natural \(\mathfrak S_n\)-action, and let \(\varepsilon\) be the nontrivial integral sign character of the factor \(C_2\) which exchanges the two bipartition classes. Then the **integral**, not merely rational, top reduced homology module is
\[
\boxed{\widetilde H_2(X_n;\mathbb Z)\cong (\bigwedge^2 V_n)\otimes\varepsilon.}
\]
All other reduced integral homology vanishes. For a permutation \(\sigma\) having \(f\) fixed points and \(t\) disjoint two-cycles, the trace of \((\sigma,\tau^e)\) on this module is
\[
(-1)^e\left(\frac{(f-1)(f-2)}{2}-t\right),\qquad e\in\{0,1\},
\]
where \(\tau(a_i)=b_i\) and \(\tau(b_i)=a_i\).

## Assumptions and scope

Graphs are finite and simple. The two-independence complex uses the **induced** maximum-degree-at-most-one condition, equivalently forbidding a three-vertex path as a (not necessarily induced) subgraph. The homotopy statement concerns geometric realizations of finite abstract simplicial complexes. The group module is an integral action on simplicial homology, with no claim of an equivariant homotopy equivalence. The range is exactly every integer \(n\geq3\); no inference from finite experiments is used for the infinite family.

The crown graph is also \(K_n\times K_2\) in the categorical graph-product convention, or the bipartite Kneser graph \(H(n,1)\). The names are alternative descriptions of the **same** graph, not additional hypotheses.

## Proof

**Step 1 (all faces).** For distinct \(i,j\) put
\[
Q_{ij}=\Delta(\{a_i,b_i,a_j,b_j\}),\qquad Z_n=\bigcup_{i<j}Q_{ij},
\]
and write \(\Delta(A)\) and \(\Delta(B)\) for the full simplices on the bipartition classes. Then
\[
X_n=\Delta(A)\cup Z_n\cup\Delta(B).\tag{1}
\]
Indeed, every one-sided vertex subset is a face. For a mixed face, let \(p\) and \(q\) be its numbers of vertices in \(A\) and \(B\). Each selected vertex is adjacent to every selected vertex on the opposite side except at most its equal-index partner. Thus if \(p\geq3\), a selected vertex of \(B\) has induced degree at least \(2\); similarly \(q\geq3\) is impossible. Hence \(p,q\leq2\). When \((p,q)=(2,1)\) or \((1,2)\), the singleton's index must be among the two indices on the other side. When \((p,q)=(2,2)\), the two index sets must coincide. Every mixed face is therefore contained in some \(Q_{ij}\) (the pair with coincident indices also lies in any such tetrahedron through that index). Conversely, the induced graph on the four vertices of \(Q_{ij}\) consists of the two disjoint edges \(a_ib_j\) and \(a_jb_i\), so every face of every \(Q_{ij}\) is allowed. This proves (1).

**Step 2 (two contractible pieces).** Put \(Y_A=\Delta(A)\cup Z_n\) and \(Y_B=\Delta(B)\cup Z_n\). Their union is \(X_n\) and their intersection, as geometric simplicial complexes, is exactly \(Z_n\). Every maximal simplex of \(Y_A\) containing \(b_i\) also contains \(a_i\). Consequently \(b_i\) is a dominated simplicial vertex and can be removed by a strong simplicial collapse. Applying this for every \(i\) collapses \(Y_A\) onto the full simplex \(\Delta(A)\). Likewise \(Y_B\) collapses to \(\Delta(B)\). Both pieces are therefore contractible. Because finite subcomplex inclusions are cofibrations, the homotopy pushout of this cover gives
\[
X_n\simeq \Sigma Z_n.\tag{2}
\]
This use of the suspension is a nonequivariant equivalence; the homology action is checked separately below.

**Step 3 (collapse of the common intersection).** In \(Z_n\), every maximal simplex containing \(b_i\) also contains \(a_i\), so successively removing \(b_1,\ldots,b_n\) is a strong collapse to the complete graph \(K_n^{(1)}\) on \(a_1,\ldots,a_n\). The graph has \(n\) vertices and \(\binom n2\) edges. Its cycle rank is \(\binom n2-n+1=\binom{n-1}{2}\). Combining this with (2) proves the integral sphere-wedge homotopy type for all \(n\geq3\).

**Step 4 (full symmetry and its integral module).** The connected graph \(C_n\) has a unique bipartition up to exchange. An automorphism that preserves both sides must induce the **same** permutation of the indices on both sides, since the absent cross-edges form the unique perfect matching of nonadjacencies. Exchanging the sides is the central involution \(\tau\). Therefore \(\operatorname{Aut}(C_n)=\mathfrak S_n\times\langle\tau\rangle\).

The connecting isomorphism in reduced integral Mayer–Vietoris for the cover \(X_n=Y_A\cup Y_B\) is
\[
\widetilde H_2(X_n;\mathbb Z)\xrightarrow{\cong}H_1(Z_n;\mathbb Z),\tag{3}
\]
because both pieces are contractible. Its restriction to \(\mathfrak S_n\) is natural and equivariant. The vertex map \(b_i\mapsto a_i\), \(a_i\mapsto a_i\) is a \(\mathfrak S_n\)-equivariant simplicial retraction \(Z_n\to K_n^{(1)}\) and is homotopic to the identity after inclusion. The oriented edge chain group of \(K_n^{(1)}\) is \(\bigwedge^2\mathbb Z^n\), with boundary \(e_i\wedge e_j\mapsto e_j-e_i\). Writing \(V_n=\ker(\mathrm{sum})\), the kernel of this boundary is exactly \(\bigwedge^2 V_n\): split the surjection \(\mathbb Z^n\to\mathbb Z\) as abelian groups and apply contraction by the sum functional. As the graph has no two-chains, this kernel is its integral first homology.

For every face \(\sigma\subseteq Z_n\) choose a tetrahedron \(Q_{ij}\) containing it. The union \(\sigma\cup\tau(\sigma)\) also lies in \(Q_{ij}\); hence \(\tau|_{Z_n}\) is simplicially contiguous to the identity and induces \(+1\) on \(H_1(Z_n;\mathbb Z)\). But \(\tau\) exchanges \(Y_A\) and \(Y_B\). Swapping the two ordered pieces reverses the sign of the Mayer–Vietoris connecting morphism, so \(\tau\) acts as \(-1\) on \(\widetilde H_2(X_n;\mathbb Z)\). This proves the asserted integral module, including the tensor factor \(\varepsilon\).

Finally, the trace of a permutation on \(V_n\) is \(f-1\), while the trace of its square on \(V_n\) is \(f+2t-1\). The identity \(\operatorname{tr}(\bigwedge^2 T)=\big((\operatorname{tr}T)^2-\operatorname{tr}(T^2)\big)/2\) proves the displayed character formula; the factor \(\tau^e\) contributes \((-1)^e\).

## Verification

The standalone standard-library Python program `verify.py` independently constructs all faces by both (i) the maximum-induced-degree definition and (ii) the tetrahedral cover (1), for every \(3\leq n\leq6\), and checks agreement across all ambient vertex subsets. It checks the full face vectors, mod-two boundary ranks, and the reduced simplicial Lefschetz character for **every** element of \(\mathfrak S_n\times C_2\) in those cases. `verification_output.txt` contains the actual program output. Run `python3 verify.py` from the folder containing the file. These finite calculations test the proof but do not replace its uniform collapse argument.

## Relationship to prior work

Taylan's 2015 study of graph devoid complexes develops homotopy-reduction tools and classifies the corresponding complex for paths, cycles, and forests. Its cycle theorem covers the crown case \(n=3\), since the three-crown is a six-cycle, but not the general crown family. Nilakantan and Shukla (2017) treat the **same crown graphs** as \(G_m^{m-1}=K_2\times K_m\), but their stated invariant is the **ordinary** independence complex (parameter one); the present theorem concerns parameter two and its full integral symmetry module. Deshpande and Singh (2020) classify higher-independence complexes of complete multipartite graphs; their complete-bipartite specialization gives \(\operatorname{Ind}_2(K_{n,n})\simeq\bigvee^{n^2-1}S^1\). The present graph deletes a perfect matching, is not complete multipartite, and instead has all reduced homology in degree two. This matching-deletion dimension change is the motivating structural distinction.

The previously calculated three-cube case of two-independence is exactly the four-crown case and is not claimed as a new isolated computation. The contribution is the uniform full-family homotopy theorem and its integral symmetric-group-plus-swap module, including all larger crown graphs. Searches also considered the aliases *dissociation complex*, *induced maximum-degree-one complex*, *bipartite Kneser graph*, and *categorical product of complete graphs*. No covering theorem was found in the inspected relevant sources; this is not a claim that unindexed equivalent work is impossible.

## Limitations

The theorem is specific to the two-independence complex of the matching-deleted complete bipartite graph, for \(n\geq3\). It neither classifies other higher-independence parameters nor supplies an equivariant homotopy equivalence. The program checks finite parameters only; the infinite quantifier is justified by the proof's explicit simplicial decomposition and dominated-vertex collapses. Publication priority is not conclusively established by finite literature searches, and no independent mathematical review has been performed.

## References

1. D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, publicly submitted 2015-01-27, https://arxiv.org/html/1501.06754v1.
2. N. Nilakantan and S. Shukla, *Homotopy type of the independence complexes of a family of regular bipartite graphs*, arXiv:1709.04789v1, submitted 2017-09-14, https://arxiv.org/abs/1709.04789.
3. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, submitted 2020-01-15, https://arxiv.org/abs/2001.05448, especially Theorem 3.5.
4. E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (graph definition and aliases).
