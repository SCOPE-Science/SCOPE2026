# Integral symmetry modules of generalized Mycielskian crown independence complexes

## Finding
For every integer \(n\geq 3\) and every integer \(\ell\geq 0\), let \(\operatorname{Cr}_n=K_{n,n}\setminus M_n\) be the crown graph with parts \(\{a_i\}_{i=1}^n\) and \(\{b_i\}_{i=1}^n\), where \(a_i\) is adjacent to \(b_j\) exactly when \(i\neq j\). Let \(X_{n,\ell}=\operatorname{Ind}(\mu_\ell(\operatorname{Cr}_n))\), for the generalized Mycielskian defined below. The group \(\Gamma_n=S_n\times C_2\) acts by simultaneous relabeling of the indices and by interchanging the two parts in every layer.

Write \(U_n=\ker(\mathbb Z^n\xrightarrow{\sum}\mathbb Z)\), with its natural integral permutation action of \(S_n\). For \(k\geq0\), define integral \(\Gamma_n\)-modules \(P_k=U_n^{\otimes 2k}\) and \(Q_k=U_n^{\otimes(2k+1)}\), using \(P_0=\mathbb Z\). The part-exchange generator \(\tau\) acts on \(P_k\) by flipping the factors in each consecutive pair and on \(Q_k\) by negating the first factor and flipping each of the remaining consecutive pairs. The symmetric group acts diagonally in every tensor factor. Then the only nonzero reduced integral homology modules are
\[
\begin{array}{c|c}
\ell & \widetilde H_*(X_{n,\ell};\mathbb Z) \\\hline
3k & \widetilde H_{4k+1}\cong Q_k,\quad \widetilde H_{4k}\cong P_k \\
3k+1 & \widetilde H_{4k+2}\cong Q_k \\
3k+2 & \widetilde H_{4k+3}\cong P_{k+1}.
\end{array}
\]
In particular, all reduced homology is free abelian. Both summands for \(\ell=0\) are present: reduced homology is \(U_n\) in degree one and \(\mathbb Z\) in degree zero.

For every \(\sigma\in S_n\), put \(u(\sigma)=|\operatorname{Fix}(\sigma)|-1\) and \(v(\sigma)=|\operatorname{Fix}(\sigma^2)|-1\). The complete rational characters, in the degrees shown above, are
\[
\begin{aligned}
\operatorname{tr}(\sigma\mid P_k)&=u(\sigma)^{2k}, &\operatorname{tr}(\sigma\tau\mid P_k)&=v(\sigma)^k,\\
\operatorname{tr}(\sigma\mid Q_k)&=u(\sigma)^{2k+1},&\operatorname{tr}(\sigma\tau\mid Q_k)&=-u(\sigma)v(\sigma)^k.
\end{aligned}
\]
The convention for a zero tensor power is \(z^0=1\), including at \(z=0\). These characters determine the complete rational representations. The integral module descriptions above give more information than characters alone.

## Assumptions and scope
The ordinary graph \(\mu_\ell(G)\) has vertices \((g,t)\), \(g\in V(G)\), \(1\leq t\leq\ell+1\), and one apex \(w\). It has copies of each edge of \(G\) between consecutive layers, all edges of \(G\) inside the final layer, and edges from \(w\) to every vertex of the first layer. No other edges occur. A graph's independence complex contains precisely its independent vertex sets. Tensor powers are over \(\mathbb Z\), all joins are simplicial joins on disjoint vertex sets, and \(\widetilde H_*\) uses integral coefficients unless a coefficient field is explicitly given. All actions are induced by genuine graph automorphisms. No equivariant *homotopy-type* classification is claimed.

## Proof
**1. Crown cycle lattice.** The independence complex \(I=\operatorname{Ind}(\operatorname{Cr}_n)\) is the union of the two full simplices on the parts and the \(n\) independent-pair edges \(\{a_i,b_i\}\). Collapsing the two simplices gives a connected graph with \(n\) parallel bridges. Its only reduced homology is \(\widetilde H_1(I;\mathbb Z)=U_n\). Orient bridges from the first part to the second. A simultaneous index permutation permutes bridges; the part exchange reverses every bridge, proving the \(S_n\times C_2\) module \(U_n\) with \(\tau=-1\).

**2. Double-cover join lattice.** Since the crown graph is bipartite, its Kronecker double cover \(\operatorname{Cr}_n\times K_2\) is the disjoint union of two copies of \(\operatorname{Cr}_n\). Consequently \(J=\operatorname{Ind}(\operatorname{Cr}_n\times K_2)=I*I\) has reduced homology only in degree three, with integral module \(U_n\otimes U_n\). The part-exchange automorphism swaps the two connected components of the double cover and acts by minus the identity on the bridge homology of each. Exchanging two join factors whose reduced homology lies in degree one contributes the Koszul sign \((-1)^{(1+1)(1+1)}=+1\). The two minus signs also cancel. Hence \(\tau(x\otimes y)=y\otimes x\) on \(\widetilde H_3(J)\). On a join of \(k\) double-cover factors, the action is the consecutive-pair flip on \(P_k\); its reduced homology is in degree \(4k-1\) for \(k\geq1\). Joining additionally with \(I\) gives degree \(4k+1\) and module \(Q_k\), where the \(I\) factor supplies the single negative sign.

**3. Equivariant graph folds.** If \(N(u_i)\subseteq N(v_i)\) for every member of an automorphism-stable collection of paired vertices, the targets \(u_i\) are independent, and simultaneous replacements \(v_i\mapsto u_i\) satisfy the indicated neighborhood inclusions, then deleting all \(v_i\) induces an equivariant homotopy equivalence of independence complexes. Indeed the replacement is a simplicial retraction, equivariant under the action on the pairs, and the retraction followed by inclusion is contiguous to the identity: each independent simplex remains independent after adjoining the replacement targets. This applies to entire layers in the Mycielski graph.

Set \(A_\ell=\operatorname{Ind}(\mu_\ell(\operatorname{Cr}_n)-w)\) and \(B_\ell=\operatorname{Ind}(\mu_\ell(\operatorname{Cr}_n)-N[w])\). Folding the layers \(3,6,\ldots,3k\) onto layers two steps earlier, followed where needed by a last-layer fold, gives the following equivariant homotopy equivalences:
\[
\begin{array}{c|ccc}
&\ell=3k&\ell=3k+1&\ell=3k+2\\\hline
A_\ell & I*J^{*k}& * &J^{*(k+1)}\\
B_\ell & J^{*k}&I*J^{*k}& *.
\end{array}
\]
Here \(*\) means a contractible complex, and the case \(k=0\) in the first column is interpreted separately as \(A_0=I\) and \(B_0\) containing only the empty face. To see each fold concretely, after deleting the apex, layers numbered \(3,6,\ldots\) can be folded toward \(1,4,\ldots\), leaving pairs \((1,2),(4,5),\ldots\); after deleting its closed neighborhood, layers \(4,7,\ldots\) fold toward \(2,5,\ldots\), leaving \((2,3),(5,6),\ldots\). An unpaired terminal graph layer contributes \(I\), an unpaired terminal independent layer contributes a simplex, and a remaining pair contributes \(J\). All folds are compatible with index permutations and part exchange because entire layers, not arbitrarily selected indices, are treated at each step.

**4. Equivariant Mayer–Vietoris.** The full independence complex is \(X_{n,\ell}=A_\ell\cup(w*B_\ell)\) with intersection \(B_\ell\); the apex cone is contractible and its apex is group-fixed. Thus there is an equivariant long exact reduced-homology sequence. In the \(3k\) case for \(k\geq1\), the only groups of \(A_{3k}\) and \(B_{3k}\) are in degrees \(4k+1\) and \(4k-1\), respectively. Exactness gives the canonically induced \(Q_k\) and \(P_k\) groups in degrees \(4k+1\) and \(4k\). In the \(3k+1\) case \(A\) is acyclic and \(B\) has module \(Q_k\) in degree \(4k+1\), giving a \(Q_k\) group in degree \(4k+2\). In the \(3k+2\) case \(B\) is acyclic and \(A\) has module \(P_{k+1}\) in degree \(4k+3\). For \(\ell=0\), the apex is a separate connected component of \(\operatorname{Ind}(\mu_0(\operatorname{Cr}_n))\), yielding \(Q_0=U_n\) in degree one and \(P_0=\mathbb Z\) in reduced degree zero. Because all the module isomorphisms arise through equivariant maps and connecting homomorphisms, they are integral, not merely rational. The stated vanishing in all other degrees follows from exactness.

**5. Characters.** The rational trace of \(\sigma\) on \(U_n\) is \(u(\sigma)\). Consequently a diagonal action on a tensor power has trace the corresponding power of \(u(\sigma)\). For any finite-dimensional vector space and linear map \(M\), \(\operatorname{tr}((M\otimes M)\circ\operatorname{flip})=\operatorname{tr}(M^2)\). Applying this identity independently to each flipped pair gives a factor \(v(\sigma)\); on \(Q_k\) the first factor supplies \(-u(\sigma)\). This proves all four character formulas.

## Verification
Run \(`python3 verify_crown.py`\) with Python 3 and no external packages. The checker independently forms the generalized Mycielski graph, computes the signed invariant-independent-set sum by enumerating automorphism vertex orbits with memoized deletion, and compares it with the derived character. It checks 180 conjugacy-class representatives with \(3\leq n\leq5\), \(0\leq\ell\leq5\), and both choices of part exchange. It also constructs all simplices and computes mod-two boundary ranks for six small cases, including the mixed-degree case \((n,\ell)=(3,3)\). These finite calculations check the formulas but are not the proof for arbitrarily large parameters; the fold and long-exact-sequence arguments above supply that proof.

## Relationship to prior work
Carnero Bravo (2026), Theorem 5, Proposition 10 and Corollary 8, already give a broad **nonequivariant** homotopy decomposition for generalized Mycielskians; in particular Corollary 8 covers the crown family as \(K_2\times K_n\). Thus the ranks and dimensions are *not* presented as new here. Goyal, Shukla and Singh (2019) establish the underlying nonequivariant complete-graph-product independence complex and a related generalized Mycielskian classification for complete graphs. The claim here is the integral \(S_n\times C_2\) homology module and the character at part-exchanging symmetries, where the trace depends on the fixed points of \(\sigma^2\) as well as those of \(\sigma\). This is not determined by the nonequivariant sphere multiplicities. A related published record determines an \(S_n\)-module for Mycielskians of \(K_n\); that base graph is different from the crown, and the part-exchange involution analyzed here has no counterpart in the \(K_n\) result.

## Limitations
No assertion is made about fixed-point subspaces in the sense of genuine equivariant homotopy theory, integral homology of arbitrary group quotients, higher generalized Mycielskian iterations, or graphs outside the crown family. The tensor description is an isomorphism of integral modules, not a canonical basis for each homology group. The exhaustive computational checks extend only to the stated finite parameters. An equivalent equivariant refinement in literature not inspected may exist; independence from the nonequivariant formulas does not by itself establish novelty.

## References
1. Andrés Carnero Bravo, *Independence complexes of generalized Mycielskian graphs*, arXiv:2601.13432, first submitted 2026-01-19; especially Theorem 5, Proposition 10 and Corollary 8. https://arxiv.org/abs/2601.13432 and https://arxiv.org/html/2601.13432
2. Shuchita Goyal, Samir Shukla and Anurag Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first submitted 2019-05-16; especially Section 3 and Theorem 4.12. https://arxiv.org/html/1905.06926v1
