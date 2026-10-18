# Leaf-budget spectrum of temporal periods on finite Alexandrov trees

## Finding

Let \(T\) be a nonempty finite rooted tree **order**, that is, a finite poset with a least element \(r\) such that the principal downset \(\downarrow x=\{y\in T:y\le x\}\) is linearly ordered for each \(x\in T\). Write \(L=\max T\) for the set of maximal elements (leaves) and \(k=|L|\ge1\). Equip \(T\) with its Alexandrov topology of upsets. For any continuous self-map \(f:T\to T\) and any arbitrary valuation \(P\subseteq T\), the sets
\[
P_n=f^{-n}[P]\qquad(n\ge0)
\]
are the truth sets of successive iterations of the dynamic-topological 'next' modality applied to the atom \(p\). Define the **least eventual period** \(\pi(f,P)\) as the unique least positive integer \(t\) such that some \(N\ge0\) satisfies \(P_{n+t}=P_n\) for all \(n\ge N\).

For integers \(t\ge1\), let
\[
\lambda(1)=0,\qquad\lambda(t)=\sum_{q\mid t,\ q\text{ prime}}q^{v_q(t)}\quad(t>1).
\]
Then the exact period spectrum, with \(T\) **fixed** and only \(f,P\) varying, is
\[
\boxed{\{\pi(f,P):f\in\operatorname{End}_{\le}(T),\ P\subseteq T\}
=\{t\ge1:\lambda(t)\le k\}.}
\]
Its largest element is \(g(k)\), the classical Landau function (maximum order of a permutation of \(k\) letters). For example, five leaves permit period six by a two-cycle and a three-cycle; seven leaves permit periods ten and twelve but **not** period eight (since \(\lambda(8)=8\)). The spectrum depends only on the leaf count, not on the depth or detailed shape of the tree.

## Assumptions and scope

The order is antisymmetric, finite, nonempty, and rooted with linearly ordered principal downsets. No upper bound on height, branching, or the number of internal vertices is imposed. For finite Alexandrov upset spaces, continuity is equivalent to monotonicity: \(x\le y\Rightarrow f(x)\le f(y)\). Valuations may be arbitrary subsets, not only open subsets; this is the standard propositional dynamic topological semantics. The result concerns the sequence of **global truth sets** \(P_n\), not the period of a single world's orbit; no other modal operators are needed.

## Proof

**1. Stable image and its leaf action.** Because \(T\) is finite, choose \(N\) for which \(S=f^N[T]=f^{N+1}[T]\). Then \(f|_S\) is a bijection. It is an order automorphism: some positive power of this finite permutation is the identity, so its inverse is a positive iterate and is order preserving. With the inherited order, \(S\) is also a finite tree order because every downset in \(S\) is a subchain of a downset in \(T\). Its maximal set \(M=\max S\) is an antichain and has size \(s=|M|\le k\): extend each \(m\in M\) to a leaf of \(T\); different \(m\)'s cannot share one ambient leaf, because two points below the same tree-order element are comparable.

Every order automorphism \(a\) of \(S\) is uniquely determined by its action on \(M\). Indeed, for \(x\in S\) put \(M_x=\{m\in M:x\le m\}\ne\varnothing\) and \(h(x)=|\{y\in S:y\le x\}|\). Two incomparable points have disjoint \(M_x\)'s (otherwise they lie below a common maximal point and must be comparable). Two comparable distinct points have different \(h\)-values. Hence the pair \((M_x,h(x))\) uniquely identifies \(x\). If \(a\) fixes every element of \(M\), it preserves both invariants and therefore fixes every point. Thus the automorphism group acts faithfully on \(M\). In particular, the order of \(f|_S\) equals the order of its induced permutation \(\sigma\) on the \(s\le k\) maximal elements.

For \(m=\operatorname{ord}(\sigma)\), all \(x\in T\) satisfy \(f^{N+m}(x)=f^N(x)\). Therefore \(P_{n+m}=P_n\) for every valuation \(P\) and all \(n\ge N\). The least eventual period \(t=\pi(f,P)\) divides \(m\).

**2. Prime-power budget.** Suppose a permutation of \(s\) letters has order divisible by \(t>1\), with cycle lengths \(c_1,\ldots,c_j\) whose sum is \(s\). For each prime \(q\mid t\), assign the largest prime power \(q^{v_q(t)}\) to one cycle length divisible by it. In any given cycle, the assigned prime powers are pairwise coprime, and their product divides the cycle length. The sum of finitely many pairwise coprime integers at least two is at most their product (for two distinct such integers this begins with \(2+3\le2\cdot3\), and induction uses \(ab\ge a+b\) when \(a,b\ge2\)). Therefore the sum of assigned prime powers in each cycle does not exceed that cycle's length. Summing over cycles gives \(\lambda(t)\le s\le k\). For \(t=1\) the bound is automatic. This proves that only listed periods occur.

**3. Every budgeted period occurs on every tree shape.** Conversely, fix \(t>1\) with \(\lambda(t)\le k\). Partition \(\lambda(t)\) distinct leaves into disjoint cycles of lengths \(q^{v_q(t)}\), one for each prime \(q\mid t\), and fix all remaining leaves. This gives a permutation \(\sigma\) of \(L\) of order exactly \(t\). Extend \(\sigma\) to a map \(f:T\to T\) by setting \(f(x)=r\) for every non-leaf and \(f(\ell)=\sigma(\ell)\) for every leaf \(\ell\). This is order preserving: comparable points are either both non-leaves or a non-leaf is below a leaf, and \(r\le f(\ell)\).

Choose a valuation \(P\) containing exactly one leaf from each nontrivial cycle and no other point. Under repeated preimage by \(f\), the restriction of \(P_n\) to such a cycle has period exactly its length, and all non-leaf truth values vanish after the first step. Hence the least eventual period is the least common multiple of the chosen prime-power cycle lengths, namely \(t\). For \(t=1\), take \(P=\varnothing\). This proves the claimed spectrum.

**4. Sharp maximum.** The cycle-budget argument shows that \(\max\{t:\lambda(t)\le k\}\) is precisely the maximum order of a permutation on \(k\) letters, which is Landau's function \(g(k)\): every permutation order meets the budget, and the construction above realizes all admissible prime-power decompositions. The period six construction on five leaves demonstrates that the global period need not be bounded by the number of leaves itself.

## Verification

Run `python3 tree_temporal_verifier.py` using Python's standard library. The checker independently enumerates all 34 increasing-parent representations of rooted tree orders on one to five vertices (covering every rooted-tree isomorphism type), all 5,430 order-preserving maps among them and all 168,950 one-atom valuations for those maps, verifying the budget inequality. It separately constructs every budgeted period for binary-tree shapes through nine vertices, checks continuity, and tests the period-six five-leaf star and the non-tree boundary below. The observed output is:

`VERIFY_OK trees= 34 monotone_maps= 5430 valuation_tests= 168950 max_periods_seen= [(1, 1), (2, 2), (3, 3), (4, 4)] constructed_spectra_through_n=9`

The infinite family of tree sizes and prime-power periods is covered by the preceding symbolic proof; finite tests alone would not establish the theorem.

## Relationship to prior work

Vooijs and Fernández-Duque (2026) develop Alexandrov dynamic topological logic, including continuous dynamical maps and temporal next truth-set semantics, and prove computable enumerability of the full logic. Their discussion of tree-like structures concerns model-search unravellings, not the exact temporal-period spectrum on a fixed finite rooted tree. The permutation-order invariant \(g(k)\) and its prime-power formula are classical (Landau; see Deléglise and Nicolas). The theorem here applies those known arithmetic ingredients only after proving a tree-specific stable-image leaf-action reduction and the realization of every period on every fixed rooted tree.

## Limitations

The leaf budget does **not** hold for arbitrary finite Alexandrov posets. For instance the four-point diamond \(r<a,b<u\) has only one maximal point, but the continuous involution exchanging \(a,b\) realizes period two for a suitable valuation. The restriction to rooted tree orders is essential. The result does not assert a new characterization of all Alexandrov DTL validities, a complexity bound for full model checking, or novelty of Landau's function. Earlier work on finite poset endomorphism monoids could contain an equivalent version of this period-spectrum theorem under different terminology.

## References

1. N. C. Vooijs and D. Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, LIPIcs 380, Article 81, published 2026-07-09. DOI: 10.4230/LIPIcs.LICS.2026.81. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol380-lics2026/LIPIcs.LICS.2026.81/LIPIcs.LICS.2026.81.pdf.
2. M. Deléglise and J.-L. Nicolas, *The Landau function and the Riemann Hypothesis*, arXiv:1907.07664 (2019). https://arxiv.org/abs/1907.07664.
3. L. Alsedà and X. Ye, *No division and the set of periods for tree maps*, Ergodic Theory and Dynamical Systems 15 (1995), 221–237, https://doi.org/10.1017/S0143385700008348. This concerns continuous maps on geometric trees, a different notion of tree from the finite Alexandrov tree orders here.
