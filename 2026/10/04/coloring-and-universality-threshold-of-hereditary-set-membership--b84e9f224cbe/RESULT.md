# Coloring and universality threshold of hereditary-set membership graphs

## Finding
For every infinite regular cardinal \(\kappa\), let \(G_\kappa\) be the simple graph on \(H(\kappa)\) in which distinct vertices \(x,y\) are adjacent exactly when \(x\in y\) or \(y\in x\). Then \(G_\kappa\) has the full \(<\kappa\)-extension property: for all disjoint \(A,B\subseteq H(\kappa)\) with \(|A|,|B|<\kappa\), there is a vertex adjacent to every point of \(A\) and to no point of \(B\).

Consequently, \(G_\kappa\) contains an induced copy of every graph of cardinality at most \(\kappa\). At the same time,
\[
\omega(G_\kappa)=\chi(G_\kappa)=\chi_\ell(G_\kappa)=\operatorname{Col}(G_\kappa)=\kappa,
\]
where \(\chi_\ell\) is the list-chromatic number and \(\operatorname{Col}\) is the coloring number. Hence \(G_\kappa\) does not contain \(K_{\kappa^+}\), so the largest cardinal at which it is induced-universal for all graphs is exactly \(\kappa\).

For \(\kappa=\omega_1\), this applies to the hereditary-countable membership graph that Kostana identifies with the canonical prime \((\omega_1,\mathfrak c)\)-saturated graph. Thus, even when \(\mathfrak c>\omega_1\), that graph is induced-universal for all graphs of size \(\omega_1\) but cannot be induced-universal for all graphs of size \(\omega_2\); its clique, ordinary chromatic, list-chromatic, and coloring numbers are all exactly \(\omega_1\).

## Assumptions and scope
Work in ZFC. The regularity of \(\kappa\) is used only to ensure that a set of fewer than \(\kappa\) many members of \(H(\kappa)\), and the auxiliary set built from it, still belong to \(H(\kappa)\). The coloring calculation itself only uses that every vertex has cardinality below \(\kappa\).

The claim is about the undirected membership graph on the actual hereditary-size level \(H(\kappa)\), not about arbitrary models of set theory. “Universal” means induced-universal: every graph in the stated cardinal range occurs as an induced subgraph.

## Proof
Let \(A,B\subseteq H(\kappa)\) be disjoint and satisfy \(|A|,|B|<\kappa\). Because \(\kappa\) is regular, \(B\in H(\kappa)\), and
\[
z=A\cup\{B\}
\]
also lies in \(H(\kappa)\). Every \(a\in A\) belongs to \(z\), so \(z\) is adjacent to every point of \(A\).

Now fix \(b\in B\). We have \(b\notin z\): it is not in \(A\), and \(b=B\) would imply \(B\in B\), contradicting Foundation. Also \(z\notin b\), since otherwise
\[
b\in B\in z\in b
\]
would be a membership cycle, again contradicting Foundation. Thus \(z\) is adjacent to no point of \(B\). This proves the full \(<\kappa\)-extension property. The same cycle argument shows that \(z\notin A\cup B\), so the witness is fresh.

To embed an arbitrary graph \(F\) with \(|F|\le\kappa\), enumerate its vertices as \((v_\alpha)_{\alpha<\lambda}\) for \(\lambda\le\kappa\). Recursively, after embedding all earlier vertices, split their images into the set \(A_\alpha\) that should be adjacent to the image of \(v_\alpha\) and the set \(B_\alpha\) that should not. Since \(\alpha<\kappa\), both have cardinality below \(\kappa\); the extension property supplies a fresh vertex with exactly the required incidences to the earlier image. The recursion is therefore an induced embedding of \(F\) into \(G_\kappa\).

For the coloring invariants, well-order \(H(\kappa)\) first by increasing von Neumann rank and then arbitrarily within each rank. If \(y\) is an earlier neighbor of \(x\), then \(x\in y\) is impossible because membership strictly raises rank. Hence necessarily \(y\in x\). Conversely every member of \(x\) has smaller rank and is an earlier neighbor. Therefore the earlier-neighbor set of \(x\) in this well-order is exactly \(x\), and so has cardinality below \(\kappa\). This witnesses
\[
\operatorname{Col}(G_\kappa)\le\kappa.
\]

On the other hand, every ordinal \(\alpha<\kappa\) belongs to \(H(\kappa)\), and the von Neumann ordinals below \(\kappa\) form a clique because \(\alpha\in\beta\) whenever \(\alpha<\beta\). Hence \(\omega(G_\kappa)\ge\kappa\). Using the standard inequalities
\[
\omega(G)\le\chi(G)\le\chi_\ell(G)\le\operatorname{Col}(G),
\]
where the last inequality follows by greedy list-coloring along a coloring-number well-order, all four invariants are forced to equal \(\kappa\). In particular \(K_{\kappa^+}\) cannot occur as a subgraph, so universality fails already at \(\kappa^+\). Together with the embedding argument, the exact induced-universality threshold is \(\kappa\).

## Verification
The proof was checked at three independent logical pressure points. First, regularity is exactly what closes \(H(\kappa)\) under the \(<\kappa\)-sized auxiliary construction \(A\cup\{B\}\). Second, Foundation rules out both unwanted ways a point of \(B\) could become adjacent to that witness. Third, in a rank-compatible well-order, the earlier neighbors of a vertex \(x\) are not merely bounded by \(x\); they are exactly the members of \(x\), making the coloring-number bound immediate.

A small finite replay in `artifacts/check_finite_membership.py` constructs the hereditary-finite levels through \(V_4\), checks the rank-order predecessor-neighbor identity there, verifies the ordinal clique through \(4\), and checks the finite analogue of the extension witness on all disjoint pairs of subsets of \(V_2\). It prints `VERIFY_OK`. The script is only a sanity check of the membership bookkeeping; the infinite-cardinal statement is established by the proof above.

## Relationship to prior work
Kostana identifies \((H(\omega_1),\in\cup\ni)\) with the prime \((\omega_1,\mathfrak c)\)-saturated graph and proves that the prime graph has coloring number \(\omega_1\). The same paper explicitly points to the higher hereditary levels \(H(\kappa)\) as natural set-theoretic analogues. Adam-Day and Cameron recall the hereditary-finite membership presentation of the Rado graph and observe that, under CH, the membership graph on hereditarily countable sets is a universal graph of cardinality \(\aleph_1\).

The contribution here is the uniform higher-cardinal synthesis: the explicit \(<\kappa\)-extension witness works for every infinite regular \(\kappa\), gives induced universality through \(\kappa\) without cardinal-arithmetic assumptions, and combines with the rank orientation and the ordinal clique to give the exact clique/chromatic/list-chromatic/coloring-number identity and the sharp failure of universality at \(\kappa^+\). Targeted searches did not locate this package of statements in the inspected sources.

## Limitations
The argument is short and uses standard facts about \(H(\kappa)\), Foundation, coloring number, and greedy list coloring. It is therefore plausible that an equivalent observation exists as folklore or in material not indexed by the searches. No claim is made for singular \(\kappa\): the specific extension witness need not remain in \(H(\kappa)\) because unions of fewer than \(\kappa\) hereditary-small sets can have hereditary size \(\kappa\).

The result determines the first cardinal at which full induced universality fails, but it does not classify which individual graphs of cardinality above \(\kappa\) embed into \(G_\kappa\).

## References
1. Z. Kostana, “On countably saturated linear orders and certain class of countably saturated graphs,” arXiv:1907.00432 (first public version 30 June 2019); *Archive for Mathematical Logic* 60 (2021), 189–209, DOI: 10.1007/s00153-020-00742-7.
2. B. Adam-Day and P. J. Cameron, “Undirecting membership in models of Anti-Foundation,” *Aequationes Mathematicae* 95 (2021), 393–400, DOI: 10.1007/s00010-020-00763-w.
