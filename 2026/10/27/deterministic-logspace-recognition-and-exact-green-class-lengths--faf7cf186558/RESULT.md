# Deterministic-logspace recognition and exact Green-class lengths in free inverse monoids

## Finding
For each **fixed** integer \(r\ge1\), the four Green-geodesic languages of the free inverse monoid \(\mathrm{FIM}_r\), with respect to the usual letters and their inverses, belong to deterministic logspace \(\mathrm L\). In fact, the minimum lengths in all four Green classes are simultaneously computable with \(O(\log(n+2))\) working bits on an input word of length \(n\).

For the Munn tree \(T\) of the input word, let \(e=|E(T)|\), let \(s\) and \(t\) be its initial and terminal vertices, let \(d\) be its graph distance, and let \(\operatorname{ecc}\) and \(\operatorname{diam}\) denote eccentricity and diameter. The **exact class-minimum lengths** are
\[
\begin{aligned}
\ell_{\mathcal H}&=2e-d(s,t),\\
\ell_{\mathcal R}&=2e-\operatorname{ecc}(s),\\
\ell_{\mathcal L}&=2e-\operatorname{ecc}(t),\\
\ell_{\mathcal D}&=2e-\operatorname{diam}(T).
\end{aligned}
\]
An input belongs to the associated Green-geodesic language precisely when its own length equals the indicated minimum. In particular, for rank at least two, the previously established neither-context-free-nor-co-context-free languages for \(\mathcal R,\mathcal L,\mathcal D\) are nevertheless in deterministic logspace, settling the context-sensitivity part of the question in Section 11 of Bodart–Carvalho–Monteiro (2026) with a stronger bound.

## Assumptions and scope
Fix \(r\ge1\) *before* measuring complexity. Let \(X=\{x_1,\ldots,x_r\}\) and \(\Sigma=X\sqcup X^{-1}\). An input is any \(w=w_1\cdots w_n\in\Sigma^*\), including the empty word. Let \(F_X\) be the free group, let \(g_i\in F_X\) be the element represented by the prefix \(w_1\cdots w_i\), with \(g_0=1\), and put \(P=\{g_i:0\le i\le n\}\). The induced Munn subtree is the finite connected subtree of the free-group Cayley tree with vertex set \(P\). Its roots are \(s=g_0\), \(t=g_n\), and its edge count is \(e=|P|-1\). Shortest Green-class length means the minimum length of a word representing **any member of that Green class**, not necessarily the original element.

No complexity claim is made for an arbitrary nonstandard generating set, a variable finitely presented inverse monoid, or uniform graph-group presentations. The rank is fixed; constants may depend on \(r\).

## Proof
**(1) The exact walk bound.** In any finite tree with \(e\) edges and prescribed starting and ending vertices \(a,b\), every edge off the unique \(a\)-to-\(b\) path must be traversed at least twice by any covering walk; each edge on that path must be traversed at least once. Thus every covering walk has length at least \(2e-d(a,b)\). A depth-first tour with each off-path edge used once in each direction, and each on-path edge used exactly once, attains this bound. Such a walk spells a word whose Munn tree is exactly the chosen subtree and whose endpoints are exactly \(a,b\).

**(2) Minima within Green classes.** By the Munn-tree characterization of Green relations, the \(\mathcal H\)-class fixes the tree and both endpoints; the \(\mathcal R\)-class fixes the tree and starting vertex; the \(\mathcal L\)-class fixes the tree and ending vertex; and the \(\mathcal D\)-class fixes the unrooted labeled tree up to the usual translation of its placement in the Cayley tree. Every vertex is a possible free endpoint when its root is not fixed. Applying (1) and maximizing the allowed endpoint distance gives the four displayed equalities. Root translations do not alter edge count or distances. Since \(w\) itself represents its class, \(n\) cannot be below any minimum; equality is exactly class-geodesicity.

**(3) Deterministic logarithmic space.** Diekert–Kausch–Lohrey (2012, Theorem 5.1) prove that for a *fixed* graph group, the shortlex normal form can be computed by a deterministic logspace transducer. Free groups on fixed \(r\) generators are graph groups with no commuting edges. Thus the freely reduced length of any input substring and the equality of any two prefixes can be evaluated in deterministic logspace. In particular, for \(i<j\), the free-group distance \(d(g_i,g_j)\) is the reduced length of the contiguous substring \(w_{i+1}\cdots w_j\), and prefix equality is exactly the condition that this length is zero.

A machine maintains only \(O(\log(n+2))\)-bit indices and counters. It counts distinct prefix vertices by scanning \(i=0,\ldots,n\) and testing whether prefix \(i\) appeared at an earlier index \(j<i\), using repeated prefix equality tests. This yields \(e=|P|-1\). A nested scan over all pairs of prefix indices computes \(d(s,t)\), the two eccentricities, and the diameter as maxima of their reduced-subword distances; duplicate prefixes do not affect maxima. The group reductions can be called successively on virtual input substrings by a fixed logspace transducer, so no reduced words or full Munn tree need be stored. All counters have \(O(\log(n+2))\) bits, and recomputation does not increase the asymptotic space bound. Finally, subtract each extremum from \(2e\) and compare with \(n\). This proves logspace computability of all four minima and recognition of all four languages.

The empty-word case has \(e=0\) and all four minima zero.

## Verification
A standalone, standard-library Python checker `green_geodesic_check.py` enumerates every word of lengths zero through six over the symmetric two-generator alphabet (\(5461\) words). It computes Munn prefix-vertex sets, their rooted and translated Green-class keys, and, independently, the shortest enumerated representative of every class. For each of the four relations and every tested word it confirms agreement with the four tree formulas. It prints `VERIFY_OK` upon success. These finite tests do not establish the asymptotic-space theorem; the proof of the space bound is the counter/loop construction in (3).

## Relationship to prior work
Bodart, Carvalho and Monteiro (arXiv:2609.35251, first version dated 2026-09-28) introduce the Green-geodesic languages. Their Section 4 supplies the tree/eccentricity/diameter descriptions; Section 11 explicitly asks whether \(\mathcal D\)-, \(\mathcal R\)-, and \(\mathcal L\)-geodesic languages are context-sensitive. The geometric ingredients of the length formulas are therefore **credited** to their tree analysis. Their results for rank at least two show that these three languages are neither context-free nor co-context-free, but do not provide a logspace recognition theorem.

Diekert, Kausch and Lohrey (arXiv:1201.3174, Theorem 5.1) establish logspace shortlex normal forms in fixed graph groups, in particular free groups. That prerequisite does not itself optimize words over nontrivial Green classes. The present observation uses implicit prefix-vertex enumeration plus tree extremal distances to combine these antecedents into the stronger deterministic-logspace bound. The proof is short because of these substantial earlier results, not independent of them.

The related Carvalho–Monteiro paper on conjugacy geodesics (arXiv:2608.10379) studies a different equivalence relation and does not supply the four claimed complexity bounds.

## Limitations
The theorem concerns the standard symmetric alphabet for each fixed finite rank. It does not classify the languages as indexed, prove optimal logspace hardness, or extend the result to arbitrary generating sets or inverse monoids. The exact tree minima are compatible with the earlier geometric descriptions, and the main newly assessed contribution is the **logspace computation** of all four class-minimum lengths. Since the algorithm combines known logspace free-group reductions with known Green/Munn-tree geometry, the possibility that its complexity consequence is implicit in unindexed prior work remains an originality risk. The finite checker is not a resource-bound certificate or an independent mathematical audit.

## References
1. C. Bodart, A. Carvalho, A.-C. C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251v2 (initial version 2026-09-28), §§2–4, 11. https://arxiv.org/html/2609.35251v2
2. V. Diekert, J. Kausch, M. Lohrey, *Logspace computations in Coxeter groups and graph groups*, arXiv:1201.3174v1 (2012), Theorem 5.1. https://arxiv.org/html/1201.3174v1
3. A. Carvalho, A.-C. C. Monteiro, *Conjugacy languages in free inverse monoids*, arXiv:2608.10379v1 (2026). https://arxiv.org/abs/2608.10379
4. W. D. Munn, *Free inverse semigroups*, Semigroup Forum 5 (1972), 262–269. Munn-tree characterization (credited in reference 1).
