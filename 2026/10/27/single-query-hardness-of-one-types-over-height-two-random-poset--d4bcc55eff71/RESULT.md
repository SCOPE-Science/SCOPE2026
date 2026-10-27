# Single-query hardness of one-types over height-two random-poset parameters

## Finding

Let \(\mathbb D\) be the countable homogeneous universal partial order. For a finite induced parameter poset \(P\), let \(c(P)\) denote the number of **nonalgebraic complete one-types** over the individually named parameters. For a bipartite graph \(G=(A\sqcup B,E)\) with \(|A|=a\ge1\), \(|B|=b\ge1\), form the height-at-most-two poset \(P_G\) by declaring \(x<y\) precisely when \(x\in A\), \(y\in B\) and \(xy\in E\). Write \(i(G)\) for the number of independent vertex sets of \(G\), including the empty set, and \(\overline G^{\mathrm{bip}}\) for the bipartite complement, with the same specified bipartition.

**Exact identity.** For every such bipartite graph,
\[
\boxed{c(P_G)=2i(G)+i(\overline G^{\mathrm{bip}})-2^a-2^b.}
\]

**One-query extraction.** Adjoin \(k=a+b\) isolated vertices to the \(A\)-side of \(G\), obtaining \(G^{+}\). Then
\[
\boxed{i(G)=\left\lfloor\frac{c(P_{G^{+}})+1}{2^{k+1}}\right\rfloor.}
\]
Consequently exact computation of \(c(P)\) on input posets of **height exactly two** is \(\#\mathrm P\)-complete under polynomial-time Turing reductions. The reduction from exact bipartite independent-set counting to this restricted type-counting problem uses one oracle query and polynomial-time integer postprocessing. The total number of complete one-types, including the \(|P|\) algebraic equality types, is \(|P|+c(P)\) and has the same hardness conclusion.

The height boundary is sharp in complexity terms: on height-one posets (antichains of size \(n\)), \(c(P)=2^{n+1}-1\) is computable directly.

## Assumptions and scope

The strict order on the finite input is explicitly given. The height of a finite poset is the maximal length in vertices of a chain; an empty poset has height zero. A graph with a specified bipartition may contain isolated vertices, which remain incomparable to every other parameter. A height-two poset contains a comparability but no three-element chain. All number counts are exact, with bit complexity polynomial in the input size for the reduction.

A nonalgebraic type is represented by the ordered pair \((L,U)\) where \(L=\{p\in P:p<x\}\), \(U=\{p\in P:x<p\}\), and \(x\notin P\). The standard one-point extension criterion requires \(L\) a downset, \(U\) an upset, and \(l<u\) for every \(l\in L,u\in U\). Fraïssé homogeneity and the extension property identify these admissible pairs with complete nonalgebraic one-types.

## Proof

**1. The exact height-two formula.** The poset \(P_G\) has comparability graph exactly \(G\); therefore its antichains are precisely the independent sets of \(G\). For every finite poset, each downset is determined uniquely by its maximal antichain, so the number of downsets of \(P_G\) is \(i(G)\). The number of upsets is the same.

If either \(L\) or \(U\) is empty, the extension criterion allows any downset or upset, respectively. This gives \(2i(G)-1\) pairs after correcting the double count of \((\varnothing,\varnothing)\).

If both \(L\) and \(U\) are nonempty, the condition \(L<U\) forces \(L\subseteq A\) and \(U\subseteq B\), even in the presence of isolated vertices. Conversely, any nonempty pair of subsets \(L\subseteq A\), \(U\subseteq B\) with every cross pair in \(E\) is an admissible downset/upset pair. Such pairs are exactly the pairs of nonempty subsets forming complete (not necessarily induced or maximal) bipartite subgraphs of \(G\).

Choosing \(L\subseteq A\) and \(U\subseteq B\) with every cross pair in \(E\) is equivalent to choosing an independent set of the bipartite complement. Among these choices, \(2^a\) have \(U=\varnothing\), \(2^b\) have \(L=\varnothing\), and the empty-empty pair occurs in both. Thus the nonempty-pair contribution is
\[
i(\overline G^{\mathrm{bip}})-2^a-2^b+1.
\]
Adding it to \(2i(G)-1\) proves the exact formula.

**2. Isolated-side amplification.** Set \(H=\overline G^{\mathrm{bip}}\) and add \(k\) isolated vertices to the \(A\)-part of \(G\). Then \(i(G^{+})=2^k i(G)\). In the bipartite complement of \(G^{+}\), these additional vertices are each adjacent to every vertex in \(B\). An independent set that contains none of the new vertices is an independent set of \(H\). An independent set containing at least one new vertex contains no vertex of \(B\), but may contain any subset of the original \(A\); there are \((2^k-1)2^a\) such sets. Hence
\[
i(\overline{G^{+}}^{\mathrm{bip}})=i(H)+(2^k-1)2^a,
\]
and the exact formula becomes
\[
c(P_{G^{+}})=2^{k+1}i(G)+\Delta,
\qquad \Delta=i(H)-2^a-2^b.
\]
Independence sets contained entirely within one side of \(H\) show \(i(H)\ge2^a+2^b-1\), so \(\Delta\ge-1\). Trivially \(i(H)\le2^{a+b}\), hence \(\Delta<2^{a+b}=2^k\). Therefore
\[
0\le\Delta+1<2^{k+1},
\]
and integer division yields the displayed one-query extraction identity.

**3. Exact-height-two and complexity statements.** Counting \(i(G)\) for bipartite graphs is a classical \(\#\mathrm P\)-complete exact counting problem; in particular Vadhan proves it hard even for planar bipartite bounded-degree inputs. If the given \(G\) has no edges, or simply to enforce the height promise uniformly, adjoin a disjoint single edge to obtain a bipartite graph \(G_*\). Then \(i(G_*)=3i(G)\), and its height-two poset \(P_{G_*}\) has a strict comparability. Apply the single-query construction to \(G_*\), extract \(i(G_*)\) by integer division, and divide by three. Thus a single oracle query on a height-exactly-two poset computes \(i(G)\). The construction adds only linearly many vertices, and the numbers manipulated have only linearly many binary digits.

Membership of the type-count function in \(\#\mathrm P\) follows by nondeterministically choosing for each parameter exactly one of the three statuses 'below the new point', 'above the new point', or 'incomparable', and checking in polynomial time that the resulting relation is a partial order. Each admissible extension has exactly one status certificate. For the total complete-type count, include an additional tagged choice for each algebraic equality type. The problem is therefore \(\#\mathrm P\)-complete under polynomial-time Turing reductions.

For a height-one poset, the only admissible pairs have \(L=\varnothing\) or \(U=\varnothing\); the displayed direct count follows.

## Verification

The standalone `verify.py` implements two independent finite representations of the nonalgebraic count: (i) an explicit three-status per-parameter enumeration checking all closure and transitivity requirements, and (ii) two bipartite independence counts used in the exact identity. It also checks isolated-side amplification and the single-query integer division, plus the extra disjoint-edge step enforcing height exactly two.

Run using `python3 verify.py` in the directory containing this file. The companion `verify_output.txt` records the complete deterministic summary. The finite tests include all 682 specified-bipartition graphs with \(1\le a,b\le3\), 240 reproducible larger graph samples, and 130 disjoint-edge checks. These finite computations are corroboration of the general argument, not an exhaustive proof over arbitrary graph sizes.

## Relationship to prior work

Dolinka and Mašulović (arXiv:1009.2892v1; journal version 2012, Lemma 3.3 in the 2011 preprint version) describe the standard downset/upset criterion for one-point extensions of finite partial orders, used here without novelty claim. The published finding “Finite-parameter 1-type counting in the random poset is #P-complete” proves unrestricted hardness, including the restriction to posets with a greatest element; its proof uses an ordinal-sum/top-chain construction and two oracle queries. That result does **not** imply the exact-height-two restriction or the one-query bipartite-complement extraction proved here. Its general one-point extension characterization is an essential predecessor.

Vadhan's exact graph counting result supplies the established bipartite independent-set hardness and is not claimed as new. A Campo and Erné (arXiv:1802.01419v1) investigate different poset-extension enumerators (fixed sets of minimal elements), while George and Yeats (arXiv:2511.14924v1) study a generalized interval polynomial with an opposite, containment-based relation between upsets and downsets. Neither examined formulation supplies the height-two one-type identity or a single-query reduction. Direct searches for these aliases and implication forms found no published theorem with the stated combination; this remains a limited originality assessment, not proof of publication priority.

## Limitations

The complexity statement uses polynomial-time Turing reductions, with a one-query reduction **from bipartite independent-set counting**. No claim is made that the target problem is complete under parsimonious reductions or under a specified stronger many-one completeness notion. The reduction does not preserve bounded degree or connectedness of the poset's comparability graph, and isolated parameters are essential to its presented extraction. No approximation-counting statement is made. A specialized unindexed prior treatment of height-two extension counting cannot be excluded, and independent scientific validation has not been performed.

## References

1. Igor Dolinka and Dragan Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” arXiv:1009.2892v1 (first submitted 15 September 2010), *Proceedings of the Edinburgh Mathematical Society* 55 (2012), 635–656, DOI:10.1017/S0013091510001161.
2. Salil P. Vadhan, “The Complexity of Counting in Sparse, Regular, and Planar Graphs,” *SIAM Journal on Computing* 31 (2001), 398–427, DOI:10.1137/S0097539797321602.
3. “Finite-parameter 1-type counting in the random poset is #P-complete,” published 4 October 2026; publicly available at `https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`.
4. Frank a Campo and Marcel Erné, “Exponential functions of finite posets and the number of extensions with a fixed set of minimal points,” arXiv:1802.01419v1 (2018).
5. Ian George and Karen Yeats, “The Generalized Interval Polynomial of a Poset,” arXiv:2511.14924v1 (2025).
