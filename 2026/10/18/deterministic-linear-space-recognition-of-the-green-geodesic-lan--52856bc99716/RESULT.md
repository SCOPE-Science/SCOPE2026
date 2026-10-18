# Deterministic linear-space recognition of the Green-geodesic languages of free inverse monoids

## Finding

**Theorem.** Fix any finite nonempty alphabet \(X\), and let \(\widetilde X=X\sqcup X^{-1}\) be its formal inverse alphabet. For an arbitrary input word \(w\in\widetilde X^*\), write \(n=|w|\). Let \(T=T(w)\) be the finite Munn subtree of the Cayley tree of the free group \(F(X)\): its vertices are precisely the freely reduced values of the \(n+1\) prefixes of \(w\). Let \(o=1\), let \(t\in T\) be the freely reduced value of the full word, let \(e=|V(T)|-1\), and use Cayley-graph distance \(d\). Define

\[
\varepsilon_o=\max_{v\in V(T)}d(o,v),\qquad
\varepsilon_t=\max_{v\in V(T)}d(t,v),\qquad
\Delta=\max_{u,v\in V(T)}d(u,v).
\]

For Green's relations in the free inverse monoid \(\operatorname{FIM}(X)\), the languages of shortest representatives of individual \(\mathcal R\)-, \(\mathcal L\)-, and \(\mathcal D\)-classes have the exact membership tests

\[
\begin{aligned}
w\in\mathcal R\text{-}\mathrm{Geo}&\iff n=2e-\varepsilon_o,\\
w\in\mathcal L\text{-}\mathrm{Geo}&\iff n=2e-\varepsilon_t,\\
w\in\mathcal D\text{-}\mathrm{Geo}&\iff n=2e-\Delta.
\end{aligned}
\]

**All three languages are decidable by deterministic machines using \(O(n)\) work space and polynomial time.** In particular, for every finite nonempty \(X\) they are context-sensitive and have context-sensitive complements. This resolves the context-sensitivity part (not the indexed-language part) of the language-hierarchy question posed in Section 11 of Bodart–Carvalho–Monteiro (2026). The standard fixed-two-roots analogue, included for comparison, is \(w\in\mathcal H\text{-}\mathrm{Geo}\iff n=2e-d(o,t)\).

## Assumptions and scope

The language alphabet is the fixed finite set \(\widetilde X\), and word length always counts letters from this set. Input may be empty; then \(T\) has one vertex, all four minima vanish, and the tests accept. The space bound is deterministic \(O(n)\) on a standard read-only-input, read/write-work-tape model; it does not claim logarithmic space or an indexed-language classification. In the Munn model, a word is represented by \((T,t)\), with \(o\in T\) the distinguished initial vertex and \(t\in T\) the distinguished terminal vertex. Trees and translations below live in the Cayley tree of the free group, not in a finite quotient.

## Proof

**1. Munn coordinates and Green classes.** The prefix vertices of a word form a finite connected subtree \(T\). The well-known Munn model identifies elements of \(\operatorname{FIM}(X)\) with pairs \((T,t)\) of a finite subtree containing \(o\) and a terminal vertex \(t\in T\). For any inverse monoid, two elements are \(\mathcal R\)-related exactly when their products with their inverses on the right coincide; in Munn coordinates this product has tree \(T\) and terminal \(o\). Thus the \(\mathcal R\)-class fixes \(T\) and \(o\), leaving the terminal vertex free. Dually, the \(\mathcal L\)-class fixes the translation \(t^{-1}T\) rooted at its terminal vertex, leaving the initial vertex free relative to that terminal-rooted tree. A \(\mathcal D\)-class allows both roots to vary while keeping the same finite edge-labelled unrooted tree up to left translation. To see the last statement directly, any \(\mathcal R\)-mate of \((T,t)\) has the form \((T,v)\) for some \(v\in T\), and its \(\mathcal L\)-class has terminal-rooted tree \(v^{-1}T\). Conversely every such rerooting is realized. A label-preserving isomorphism between connected subtrees of the free-group Cayley tree is precisely the restriction of a left translation, so these rerootings exhaust the \(\mathcal D\)-class.

**2. Exact shortest walks on a tree.** For a finite tree \(T\) with \(e\) edges and prescribed start and end vertices \(s,u\), the least length of any walk beginning at \(s\), ending at \(u\), and traversing every edge is

\[
\ell_T(s,u)=2e-d(s,u).
\]

Indeed, deleting each edge separates the tree into two components. An edge on the unique \(s\)-to-\(u\) path must be crossed an odd positive number of times, hence at least once. Any edge off that path must be crossed an even positive number, hence at least twice. Summing gives the lower bound. Traverse each off-path branch out and back during the unique \(s\)-to-\(u\) path to attain equality. Such a walk yields a word with exactly this Munn tree, because it traverses precisely the tree's edges and the labelled Cayley-tree path determines its letters.

**3. Optimization within each Green class.** For \(\mathcal R\), the start is \(o\) and the end can be any vertex; minimizing the formula from step 2 gives \(2e-\varepsilon_o\). For \(\mathcal L\), translated terminal-rooted coordinates fix the terminal root and allow the other end to vary, giving \(2e-\varepsilon_t\). For \(\mathcal D\), both vertices vary, giving \(2e-\Delta\). In each case the minimizing walk realizes an actual member of the same Green class. Hence comparison with the input's length \(n\) gives exactly the three displayed language tests. For \(\mathcal H=\mathcal R\cap\mathcal L\), the finite subtree has no nontrivial translation stabilizer, so both roots are fixed, yielding the supplementary \(2e-d(o,t)\) formula.

**4. Linear-workspace algorithm.** The input's \(n+1\) freely reduced prefix values have at most \(n\) letters each. A left-to-right free-reduction stack stores any one such value in \(O(n)\) cells; two simultaneous prefix values and one reduced difference word still occupy \(O(n)\) cells. Enumerate prefix indices \(i,j\in\{0,\ldots,n\}\) using \(O(\log n)\) counters. To count distinct vertices, regard a prefix as new only when no earlier prefix has the same reduced value; this determines \(e\) with repeated scans and no table of all vertices. For distances, recompute reduced prefix values on demand and reduce the concatenation of the inverse of one with the other. Taking maxima over one or two prefix indices obtains \(\varepsilon_o,\varepsilon_t,\Delta\), including repeated vertices harmlessly. These loops use polynomial time and \(O(n)\) work space. Compare the resulting integers with \(n\) and halt, accepting or rejecting. Deterministic linear-space languages and their complements are context-sensitive by the linear-bounded-automaton characterization. No unbounded free-group data structure, exponential enumeration, or hypothetical shortest-word oracle is needed.

## Verification

Run `python3 artifacts/verify.py` using only the Python standard library. The verifier independently enumerates all words through length 10 in rank one, through length 6 in rank two, and through length 4 in rank three, totaling 9,063 words. It computes Green-class equivalence invariants of Munn trees, enumerates the true shortest length among all words up to each corresponding cutoff, and separately compares that minimum with all four tree-distance predictions. Each tested element has a shortest representative no longer than the input, so a cutoff at the input's maximum length suffices for these finite checks. The script returns `VERIFY_OK`. These checks do not prove the unbounded theorem; the proof is the tree-tour and workspace argument above.

## Relationship to prior work

Bodart, Carvalho and Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251 (first publicly posted 28 September 2026), define these Green-geodesic languages, give geometric descriptions through Munn trees and establish context-free/non-context-free results. Their Section 11 explicitly asks, for rank at least two, whether the \(\mathcal D\)-, \(\mathcal R\)- and \(\mathcal L\)-languages are context-sensitive. The present result addresses the **resource-bound question**, not the novelty of the Munn representation or the underlying geodesic characterizations. The deterministic reusable-workspace construction is the additional ingredient.

The classical Munn-tree model and the growth work of Kambites, Nyberg-Brodda, Szakács and Webb provide background on free inverse monoids, but their cited growth-rate results do not themselves state a linear-space Green-geodesic recognizer. An explicit earlier resource-bound result with the same implications would subsume the present claim.

## Limitations

The theorem is for finite, fixed generating alphabets and their formal inverses. It does not locate these languages within the hierarchy of indexed languages, prove logspace recognition, determine language growth, or generalize to arbitrary inverse monoids. The length formulae are standard consequences of Munn trees and tree routing; the new claim assessed here is the simultaneous deterministic linear-space bound and consequent context-sensitive classification. Literature coverage is not guaranteed to be exhaustive, and independent mathematical auditing has not been performed.

## References

1. C. Bodart, A. Carvalho, and A.-C. C. Monteiro, *Green languages and growth of free inverse monoids*, arXiv:2609.35251, first submitted 28 September 2026. https://arxiv.org/abs/2609.35251 ; full-text sections 1, 2, 9 and 11 at https://arxiv.org/html/2609.35251 .
2. M. Kambites, C.-F. Nyberg-Brodda, N. Szakács, and R. Webb, *The growth of free inverse monoids*, arXiv:2407.10489, 15 July 2024; Journal of the Institute of Mathematics of Jussieu 25 (2026), 2047–2067. https://arxiv.org/abs/2407.10489 .
3. W. D. Munn, the classical Munn-tree representation of free inverse semigroups; recalled as preliminary background in Reference 1.
