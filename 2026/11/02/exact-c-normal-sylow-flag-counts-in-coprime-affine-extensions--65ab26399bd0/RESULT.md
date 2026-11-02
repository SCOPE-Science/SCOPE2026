# Exact c-normal Sylow-flag counts in coprime affine extensions

## Finding

**Theorem.** Let \(p\) be prime, let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_p\), with \(n\geq1\), and let a finite group \(H\) of order coprime to \(p\) act linearly on \(V\). Set \(G=V\rtimes H\), \(F=V^H\), and \(U=[V,H]=\sum_{h\in H}(h-1)V\). Put \(f=\dim F\) and \(u=\dim U\), so \(n=f+u\).

A subgroup \(W\leq G\) is **c-normal** if a normal subgroup \(N\trianglelefteq G\) satisfies \(WN=G\) and \(W\cap N\leq\operatorname{Core}_G(W)\). A **c-normal maximal Sylow-\(p\) chain** in \(G\) means a complete flag \(0=W_0<W_1<\dots<W_n=V\), each step of index \(p\), with every intermediate \(W_i\) c-normal in \(G\).

First, for any \(\mathbb F_p\)-subspace \(W\leq V\),
\[
W\text{ is c-normal in }G\quad\Longleftrightarrow\quad W\cap U\text{ is }H\text{-invariant}.
\]

Let \(C_p(G)\) count those flags. If \(U\) has a simple \(\mathbb F_pH\)-constituent of dimension greater than one, then \(C_p(G)=0\). Otherwise let \(m_\chi\) be the multiplicity of each *nontrivial* linear character \(\chi:H\to\mathbb F_p^\times\) occurring in \(U\). Define
\[
\Phi_p(k)=\prod_{j=1}^{k}\frac{p^j-1}{p-1},\quad \Phi_p(0)=1,\qquad
{n\brack u}_p=\prod_{j=0}^{u-1}\frac{p^{n-j}-1}{p^{u-j}-1}.
\]
Then the exact number of c-normal maximal Sylow-\(p\) chains is
\[
\boxed{C_p(G)={n\brack u}_p\,\Phi_p(f)\,
\frac{u!}{\prod_\chi m_\chi!}\prod_\chi\Phi_p(m_\chi).}
\]
Empty products and \({n\brack0}_p\) equal one. In particular the proportion of all \(\Phi_p(n)\) complete flags which are c-normal is zero in the first case and otherwise equals
\[
\boxed{\frac{C_p(G)}{\Phi_p(n)}=
\frac{u!}{\prod_\chi m_\chi!}\,
\frac{\prod_\chi\Phi_p(m_\chi)}{\Phi_p(u)}.}
\]
The proportion is independent of the dimension of the fixed-point space \(F\).

Consequently such a chain exists if and only if the image of \(H\) in \(\operatorname{GL}(V)\) is simultaneously diagonalizable over \(\mathbb F_p\). Every complete flag is c-normal precisely when \(H\) acts on \(U\) by a single scalar character (or \(U=0\)). Neither assertion assumes \(H\) cyclic, abelian, or faithful.

## Assumptions and scope

The action is linear, \(H\) is finite, and \(p\nmid|H|\). The Sylow \(p\)-subgroup \(V\) is elementary abelian and normal in the semidirect product. The complete flags count **labelled subgroup chains**, not conjugacy orbits. All statements refer to c-normality *in \(G\)*, not normality inside \(V\) or AC-normality for an external action. The endpoint subgroups \(0\) and \(V\) automatically satisfy c-normality, so the interior convention does not affect the counts.

## Proof

**1. The coprime decomposition.** Since \(p\nmid|H|\), the averaging idempotent \(e=|H|^{-1}\sum_{h\in H}h\in\operatorname{End}_{\mathbb F_p}(V)\) projects onto \(F=V^H\). Moreover \((1-e)V=U\), since \(e(h-1)=0\) and \(v-ev\) is the average of the vectors \(v-hv\). Thus \(V=F\oplus U\). The group \(H\) acts trivially on \(F\), and \(U\) has no trivial simple constituent.

**2. C-normality of an arbitrary subspace.** Suppose \(W\leq V\) is c-normal. Take \(N\trianglelefteq G\) with \(G=WN\) and \(W\cap N\leq\operatorname{Core}_G(W)\). The quotient \(G/N\), being the image of \(W\), is a \(p\)-group. Since \(H\) has \(p\)-coprime order, its image is trivial: \(H\leq N\). Hence \(U=[V,H]\leq N\). Therefore \(W\cap U\leq W\cap N\leq\operatorname{Core}_G(W)\), and the latter is \(H\)-stable, proving necessity.

Conversely assume \(K=W\cap U\) is \(H\)-stable. Let \(\pi_F:V\to F\) denote projection along \(U\). Choose a vector-space complement \(L\leq F\) of \(\pi_F(W)\). The group \(N=(U\oplus L)\rtimes H\) is normal in \(G\): the subspace \(U\oplus L\) is \(H\)-invariant and contains every commutator \([V,H]\). Furthermore \(WN=G\), and \(W\cap N=W\cap(U\oplus L)=W\cap U=K\). As \(K\) is \(H\)-stable and is contained in the abelian normal subgroup \(V\), it is normal in \(G\); thus \(K\leq\operatorname{Core}_G(W)\). This proves sufficiency.

**3. Invariant flags in \(U\).** For a complete flag \((W_i)_{i=0}^{n}\), form its intersection sequence \(K_i=W_i\cap U\) and projection sequence \(L_i=\pi_F(W_i)\). Across each dimension-one step, precisely one of \(\dim K_i\) or \(\dim L_i\) rises by one. A c-normal chain therefore determines an \(H\)-invariant complete flag of \(U\), an arbitrary complete flag of \(F\), and a shuffle of \(u\) intersection steps with \(f\) projection steps. Conversely these data, with the graph lifts counted below, specify exactly the desired chains.

By Maschke's theorem \(U\) is semisimple. It admits an \(H\)-invariant complete flag if and only if all its simple constituents are one-dimensional. In that case \(U=\bigoplus_\chi U_\chi\), where \(\chi\) ranges over the distinct nontrivial \(\mathbb F_p\)-valued characters and \(\dim U_\chi=m_\chi\). Every invariant subspace decomposes into eigenspace components, so an invariant complete flag consists of a full flag in each \(U_\chi\), interleaved in one of \(u!/\prod_\chi m_\chi!\) ways. There are therefore \((u!/\prod_\chi m_\chi!)\prod_\chi\Phi_p(m_\chi)\) invariant full flags of \(U\). There are \(\Phi_p(f)\) arbitrary full flags of \(F\).

**4. Counting all lifts of fixed component flags.** Fix those two component flags, and consider a shuffle path recording \(a\) intersection steps and \(b\) projection steps. The subspace \(W\) with \(W\cap U=K_a\) and \(\pi_F(W)=L_b\) is the graph of a unique linear map \(L_b\to U/K_a\), lifted together with \(K_a\). At an intersection step \((a,b)\to(a+1,b)\), the graph map has a unique induced image in the new quotient. At a projection step \((a,b)\to(a,b+1)\), the graph map can be extended in exactly \(p^{u-a}\) ways. Thus a fixed shuffle receives weight equal to the product of these projection-step factors. Summing weights over all shuffles gives \(S(u,f)\) satisfying
\[
S(u,0)=S(0,f)=1,\qquad
S(u,f)=S(u-1,f)+p^uS(u,f-1).
\]
The Gaussian-binomial recurrence (or a direct product calculation) gives \(S(u,f)={u+f\brack u}_p\). This proves the exact count and the displayed proportion, using \(\Phi_p(n)={n\brack u}_p\Phi_p(u)\Phi_p(f)\).

**5. Extremes.** A full invariant flag exists exactly when all simple constituents of \(U\) are one-dimensional; together with the trivial action on \(F\), this is simultaneous diagonalizability of the representation. Every possible flag is c-normal exactly when every subspace of \(U\) is \(H\)-stable. In particular all lines of \(U\) are then invariant, so each operator from \(H\) is scalar on \(U\); the converse follows from the criterion in Step 2.

## Verification

The standalone program `verify.py` enumerates every subspace and complete flag for nine small cyclic-complement examples, checks the invariant-intersection criterion against direct conjugacy/normal-subgroup enumeration where the full semidirect group has at most twenty elements, and verifies the closed formula. It additionally checks three groups with noncyclic complements generated by commuting diagonal matrices. Run `python3 verify.py`; successful execution ends with `VERIFY_OK` and `MULTI_VERIFY_OK`.

Selected independent outputs: for \(\mathbb F_5^3\rtimes C_4\) with action \(\operatorname{diag}(2,3,1)\), exactly \(62\) of \(186\) full flags are c-normal; with action \(\operatorname{diag}(2,2,1)\), all \(186\) are c-normal. For \(\mathbb F_2^2\rtimes C_3\) with the irreducible action, none of its three full flags is c-normal. For the noncyclic \(C_2\times C_2\) action with two distinct moving characters and one fixed coordinate over \(\mathbb F_3\), the count is \(26\) out of \(52\).

These finite checks are consistency tests; the symbolic proof above establishes every allowed dimension and coprime complement.

## Relationship to prior work

Wei Meng and Feiyu Geng (2026, arXiv:2610.26968) introduce the maximal-chain condition used here and prove consequences for \(p\)-nilpotence and supersolvability. Their full preprint treats structural existence implications, not the exact count for coprime elementary-abelian extensions. Beltrán and Shao (2023) investigate AC-normality of subgroups invariant under an *external* coprime action, using criteria for solvability and \(p\)-nilpotence; their property and conclusions do not give this all-subspace criterion or flag enumerator. Tărnăuceanu (2015) counts unrestricted chains in elementary abelian groups; the c-normal requirement depends on an ambient semidirect product and is absent there.

## Limitations

The theorem requires an elementary abelian normal Sylow subgroup with a complement of order coprime to \(p\). It does not enumerate chains for non-elementary abelian kernels, non-split extensions, or arbitrary finite groups. Full historical priority is not established: older subgroup-chain and c-normality literature might contain an equivalent characterization in different language.

## References

- W. Meng and F. Geng, *On c-Normal Maximal Chains of Sylow Subgroups in Finite Groups*, arXiv:2610.26968, first publicly posted 18 October 2026. https://arxiv.org/abs/2610.26968
- A. Beltrán and C. Shao, *c-Normality and coprime action in finite groups*, Acta Mathematica Hungarica 171 (2023), 39–52, DOI:10.1007/s10474-023-01376-w. https://doi.org/10.1007/s10474-023-01376-w
- M. Tărnăuceanu, *The number of chains of subgroups of a finite elementary abelian p-group*, U.P.B. Scientific Bulletin, Series A 77(4) (2015), 65–68, arXiv:1506.08298. https://arxiv.org/abs/1506.08298
