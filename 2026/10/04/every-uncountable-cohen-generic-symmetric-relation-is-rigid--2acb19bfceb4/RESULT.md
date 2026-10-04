# Every uncountable Cohen-generic symmetric relation is rigid

## Finding
Fix an integer \(n\ge 2\) and an uncountable set \(S\). Let \(\mathbf K_{\mathrm{sym},n}\) be the class of finite structures in a language with one symmetric \(n\)-ary relation \(R\), and let \(\mathbb P\) be the finite-condition forcing whose conditions are members of \(\mathbf K_{\mathrm{sym},n}\) with finite underlying set contained in \(S\), ordered by extension. If \(G\subseteq\mathbb P\) is generic, then the union \(\mathcal H_G=\bigcup G\) is rigid:
\[
\operatorname{Aut}(\mathcal H_G)=\{\operatorname{id}_S\}.
\]
Thus the symmetric-relation rigidity conjecture stated by Ackerman, Golshani, and Mirabi holds in every arity \(n\ge2\) and for every uncountable underlying cardinal.

## Assumptions and scope
The relation is symmetric, meaning that its truth value is invariant under permutations of its \(n\) coordinates. The proof only uses relation instances on \(n\) distinct points, so it applies whether the ambient convention permits or forbids relation tuples with repeated coordinates. A condition is finite and specifies the induced relation on its finite support. Because \(\mathbf K_{\mathrm{sym},n}\) is the unrestricted finite symmetric-relation class, compatible conditions with the same induced structure on their common support have a free amalgam: every previously unspecified cross-support \(n\)-set may be assigned either relation value independently.

The theorem concerns uncountable Cohen-style finite-condition generics. It does not assert rigidity of the countable Fraïssé limit, which is highly homogeneous and therefore non-rigid.

## Proof
Suppose toward a contradiction that a condition \(p\in\mathbb P\) forces that \(\dot h\) is a nonidentity automorphism of the generic structure.

First note a separation property. Let \(F\subseteq S\) be any infinite ground-model set, and let \(x\ne y\) be points of \(S\). Below every condition there is an extension and distinct points \(z_1,\ldots,z_{n-1}\in F\setminus\{x,y\}\) such that
\[
R(x,z_1,\ldots,z_{n-1})
\quad\text{and}\quad
\neg R(y,z_1,\ldots,z_{n-1}).
\]
Indeed, choose the \(z_i\) outside the finite support of the condition and freely prescribe these two cross-support relation values. Consequently, if an automorphism sends \(x\) to \(y\ne x\), it cannot fix every point of \(F\). Hence \(p\) forces that \(\dot h\) moves a point in every infinite ground-model subset of \(S\).

Choose an uncountable family \((F_\xi)_{\xi<\lambda}\) of pairwise disjoint countably infinite ground-model subsets of \(S\), where \(\lambda\) is uncountable. For each \(\xi\), strengthen \(p\) to a finite condition \(p_\xi\), choose \(s_\xi\in F_\xi\), and decide a value \(t_\xi\ne s_\xi\) such that
\[
p_\xi\Vdash \dot h(s_\xi)=t_\xi.
\]
Strengthen once more so that both \(s_\xi\) and \(t_\xi\) lie in the support of \(p_\xi\).

Apply the \(\Delta\)-system lemma to the uncountable family of finite supports. After thinning, the supports have a common finite root \(D\), their petals are pairwise disjoint, and all \(p_\xi\) induce the same structure on \(D\). Discard the finitely many indices for which \(s_\xi\in D\). We may also arrange that every \(t_\xi\notin D\). To see this, if uncountably many \(t_\xi\) belonged to the finite root, two distinct indices would have the same value \(t_\xi=t_\eta=d\in D\). The free amalgam of \(p_\xi\) and \(p_\eta\) would then force both \(\dot h(s_\xi)=d\) and \(\dot h(s_\eta)=d\) with \(s_\xi\ne s_\eta\), contradicting injectivity of \(\dot h\). Thus, after thinning, both \(s_\xi\) and \(t_\xi\) lie in the petal of \(p_\xi\). In particular, for distinct indices all selected source and image points are distinct.

Choose distinct indices \(\xi_1,\ldots,\xi_n\), and write \(a_i=s_{\xi_i}\) and \(b_i=t_{\xi_i}\). Freely amalgamate the conditions \(p_{\xi_1},\ldots,p_{\xi_n}\). Since the \(a_i\) lie in different petals, the \(n\)-set \(\{a_1,\ldots,a_n\}\) is not contained in the support of any one original condition; likewise for \(\{b_1,\ldots,b_n\}\). Therefore these two cross-petal relation values were not previously decided. Extend the amalgam to a condition \(q\) satisfying
\[
R(a_1,\ldots,a_n)
\quad\text{and}\quad
\neg R(b_1,\ldots,b_n).
\]
The condition \(q\) still forces \(\dot h(a_i)=b_i\) for every \(i\). But an automorphism must preserve \(R\), so it must send the true relation instance on \((a_1,\ldots,a_n)\) to a true relation instance on \((b_1,\ldots,b_n)\), contradicting the second prescription. Therefore no condition can force a nonidentity automorphism, and the generic structure is rigid.

## Verification
The proof uses four ingredients only: finite support, free amalgamation for the unrestricted symmetric relation, the \(\Delta\)-system lemma for uncountably many finite supports, and the ability to decide the value of a forced function at a named point. The separation lemma prevents a nontrivial automorphism from being supported on only finitely many of the chosen ground-model blocks. The root-collision argument ensures that the chosen images can be placed in disjoint petals before the final \(n\)-way amalgam.

The accompanying finite bookkeeping checker verifies, for arities \(2\) through \(8\), that the source and image \(n\)-sets in the last step are cross-petal sets absent from each individual support and can therefore receive opposite relation values in a free amalgam. This computation is a sanity check of the finite amalgamation bookkeeping, not a substitute for the forcing and \(\Delta\)-system argument.

## Relationship to prior work
Kostana proved rigidity of the uncountable Cohen-generic graph by a binary \(\Delta\)-system argument and observed analogous binary relational examples. Ackerman, Golshani, and Mirabi later isolated the higher-arity obstruction: their Section 4 explains that the existing pair-based rigidity method does not directly handle a lone \(n\)-ary relation for \(n>2\), proves higher-arity rigidity after adding tuple-naming functions under additional hypotheses, and states as Conjecture 4.10 that the uncountable generic for the class of finite symmetric \(n\)-ary structures should be rigid for every \(n\ge2\).

The argument above resolves precisely that conjectured case without adding function symbols. Its extra step is to take \(n\) petals from the \(\Delta\)-system and prescribe opposite values on the source and image cross-petal \(n\)-sets. Searches for the conjecture number, the exact rigidity statement, symmetric \(n\)-ary Cohen generics, and generic hypergraph rigidity found the conjecture and the binary predecessor but no source proving this all-arity statement. A 2025 paper on forcing with invariant measures discusses Cohen generic structures but did not contain the conjecture number or a hypergraph resolution in the inspected text.

## Limitations
This is a forcing theorem relative to the standard finite-condition generic construction; it does not claim that an arbitrary uncountable symmetric relation is rigid. It also does not assert any stronger absoluteness statement for rigidity under later forcing extensions. The originality assessment is literature-based: although the exact statement was still presented as an explicit conjecture in the 2023 source and was not found in targeted later searches, an unindexed or unpublished proof could exist.

## References
1. Z. Kostana, *Cohen-like first order structures*, arXiv:2009.03552, first version 2020-09-08; Annals of Pure and Applied Logic 174 (2023), 103172, DOI 10.1016/j.apal.2022.103172.
2. N. Ackerman, M. Golshani, M. Mirabi, *Cohen Generic Structures with Functions*, arXiv:2310.11582, first version 2023-10-17. In particular, Section 4 and Conjecture 4.10.
3. N. Ackerman, C. Freer, M. Golshani, M. Mirabi, R. Patel, *Forcing with Invariant Measures*, Logica Universalis 19 (2025), 799–840, DOI 10.1007/s11787-025-00394-2. This later source was checked for overlap, not used in the proof.
