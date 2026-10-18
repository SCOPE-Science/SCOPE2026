# Optimal additional stage arrows over finite star scope orders

## Finding
Fix a natural scope tree with one root \(r\) and \(k\ge 1\) labelled incomparable leaves \(L\). Equip it with the rooted-star scope preorder \(\preceq\). The stage preorder \(S\) may be any preorder containing \(\preceq\). A stage presentation consists of all fixed scope arrows \(r\to u\), \(u\in L\), and a set of additional ordered pairs, whose reflexive transitive closure equals \(S\). Loops cost nothing and can be omitted. Let \(m(S)\) be the smallest number of additional arrows in such a presentation.

**Classification and exact cost.** The leaf restriction \(T=S\cap(L\times L)\) is an arbitrary preorder. Define \(U=\{u\in L:\forall v\in L,\ uTv\}\). Either no leaf reaches the root, or \(U\ne\varnothing\) and exactly the leaves of \(U\) reach it; both options are available when \(U\ne\varnothing\). Write \(Q\) for the partial order on the equivalence classes of \(T\) under mutual reachability, and \(h(Q)\) for the number of its strict cover pairs. Set \(c(C)=|C|\) for classes of size at least two, and \(c(C)=0\) for singleton classes. Then
\[
m(S)=\begin{cases}
\sum_{C\in Q}c(C)+h(Q),&\text{if no leaf reaches }r,\\
|U|+\sum_{C\in Q,\ C\ne U}c(C)+h(Q\setminus\{U\}),&\text{if exactly }U\text{ reaches }r.
\end{cases}
\]
Here \(U\), if nonempty, is itself the unique least equivalence class of \(Q\), and \(Q\setminus\{U\}\) carries the induced partial order.

**Sharp universal budget.** Let \(M(k)=\max_S m(S)\), over every such stage preorder on the fixed labelled star. Then
\[
M(k)=\begin{cases}1&k=1,\\2&k=2,\\3&k=3,\\5&k=4,\\\lfloor k^2/4\rfloor&k\ge5.\end{cases}
\]
The special four-leaf value is greater than the ordinary quadratic value \(4\).

**Semantic distinctness.** In the one-world fragment of bounded modal logic, for any two different stage preorders on this fixed scope star there is an upward-closed valuation of one atom \(p\) and a leaf \(u\) at which the same bounded box formula \(\Box_{\succeq !}p\) has different truth values. Thus the classification concerns modally distinguishable finite structures, not merely drawings of a relation.

## Assumptions and scope
The node set is finite, and arrows are directed. We count *only additional non-scope arrows*; the \(k\) root-to-leaf scope arrows are compulsory and uncharged. Each additional arrow must be an actual pair belonging to the target preorder \(S\); the constructed optimal presentations have this property. Reachability includes empty paths, and all preorders are reflexive and transitive. The BML semantic comparison fixes a single outer world, a single atom, and allows the valuations prescribed in Definition 2.1 of the motivating reference. This is not a statement about all infinite BML structures or about deriving a unique syntax for arbitrary staged programs.

## Proof
**1. Root dichotomy.** Let \(T\) be the leaf restriction of \(S\). If \(uSr\), then \(uSv\) for every leaf \(v\), because \(rSv\). Thus \(u\in U\). If \(v\in U\) and \(uSr\), then \(vTu\) and hence \(vSr\). Consequently, the root-reaching leaves are either empty or exactly \(U\). Moreover, if \(U\ne\varnothing\), any two elements of \(U\) are mutually related, and \(U\) forms the unique least class of the quotient partial order \(Q\). Conversely, adjoining exactly the pairs \(U\times\{r\}\) to the reflexive/transitive scope-plus-\(T\) relation yields a preorder: the resulting composition introduces no new leaf comparisons because every member of \(U\) already reaches every leaf. It is therefore a legitimate second option. The full \(S\) is determined by \(T\) and this flag.

**2. Optimal cost when the root is not merged.** Inside a leaf component \(C\) with at least two elements, any presentation needs at least \(|C|\) internal extra arrows: each vertex requires at least one outgoing internal arrow, because no path between two leaves can pass through the root when no leaf reaches it. A cycle through \(C\) meets the bound. Each cover \(C\prec D\) in the quotient requires at least one additional arrow from \(C\) to \(D\): a path of length two or more through distinct components would contradict the cover property, and the mandatory root arrows cannot occur on any path starting at a leaf. Conversely, one such arrow per cover, together with the cycles, generates precisely all of \(S\). These types of arrows are disjoint; hence the displayed sum is optimal.

**3. Optimal cost when the root is merged.** The root component is \(\{r\}\cup U\). Every \(u\in U\) must have at least one extra outgoing arrow into this root component, because the only mandatory arrows start at the root, and an arrow from \(u\) toward a different component cannot return. Therefore at least \(|U|\) additional arrows are required, achieved by the arrows \(u\to r\) for all \(u\in U\). The mandatory arrows \(r\to v\) already provide every transition from the root component to higher quotient components. Among the remaining leaf components, cycles and one arrow for each cover of the induced order are necessary and sufficient exactly as in Step 2. The three lower-bound categories are disjoint, giving the second formula. In particular the merge case costs no more than the unmerged case on the same \(T\) unless \(Q\) is a single singleton: if \(Q\) has more than one class then its least class has at least one outgoing cover, compensating for the possible extra one-edge merger.

**4. Sharp worst case.** For an unmerged preorder let \(q=|Q|\) and let \(t\) be the number of nonsingleton equivalence classes. Then \(t\le\min(q,k-q)\), and \(\sum c(C)=k-q+t\). The undirected Hasse graph has no triangle, so Mantel's theorem gives \(h(Q)\le\lfloor q^2/4\rfloor\). Hence
\[
m(S)\le f_k(q):=\lfloor q^2/4\rfloor+k-q+\min(q,k-q).
\]
For \(q\le k/2\), this bound is \(k+\lfloor q^2/4\rfloor\), increasing with \(q\). For \(q\ge k/2\), it is \(\lfloor q^2/4\rfloor+2(k-q)\), nondecreasing for integer \(q\ge4\). Direct evaluation at \(k\le7\), and the inequalities \(k+\lfloor k^2/16\rfloor\le\lfloor k^2/4\rfloor\) and \(\lceil k/2\rceil\ge4\) for \(k\ge8\), show that the maximum is at most the asserted value for every \(k\ge2\). The merged case has no larger cost for \(k\ge2\), by the comparison at the end of Step 3; at \(k=1\), the merged option costs one and the unmerged option zero. Sharpness is witnessed for \(k=2,3\) by a single mutually reachable leaf class, for \(k=4\) by two mutually reachable two-leaf classes with one cover between them (five extra arrows), and for all \(k\ge5\) by an antisymmetric leaf preorder with a complete bipartite height-two Hasse diagram of class sizes \(\lfloor k/2\rfloor\) and \(\lceil k/2\rceil\). These witnesses are unmerged, except for \(k=1\).

**5. Distinguishing formula.** The BML box \(\Box_{\succeq !}p\), evaluated at a leaf, requires \(p\) at all stage-successors of that leaf, since every node is above the global root \(!\) in the scope preorder. All subsets of leaves, with the root false, are upward-closed scope valuations. If two stage preorders disagree about whether a given leaf can reach the root, choose \(V(p)=L\); the formula distinguishes them. Otherwise their root-reaching sets coincide. If their leaf relations differ at \((u,v)\), then \(u\) cannot reach the root in either stage preorder (root reachability forces every leaf-successor); choose \(V(p)=L\setminus\{v\}\). The formula is true at \(u\) precisely in the relation lacking that pair. This proves one-formula semantic separation.

## Verification
The accompanying self-contained `verify_star.py` exhaustively enumerates all choices of additional directed leaf-origin arrows for \(k=1,2,3,4\), closes them together with the compulsory star, and determines the minimum arrow cost for every resulting stage preorder. Independently of the profile formula, it compares semantic truth-signatures of \(\Box_{\succeq !}p\) under the specified valuations. It obtains respectively \(2,7,45,500\) distinct structures and maximal minimum extra-arrow counts \(1,2,3,5\). It also evaluates the extremal optimization over quotient sizes for \(5\le k\le39\). The full arbitrary-\(k\) result is proved above; finite tests alone would not establish it.

## Relationship to prior work
Murase and Maniwa introduce BML and its stage preorder containing its scope preorder, along with Kripke semantics and a type-theoretic interpretation [1]. They do not give this fixed-star semantic separation and constrained exact arrow-budget theorem in the inspected material. The classical transitive-reduction theorem of Aho, Garey and Ullman [2] already determines minimum unconstrained reachability presentations by quotient covers and cycles; this foundational component is **not new**. Our cost is different: all scope arrows must be included and are free, and the permitted merger of a leaf component with the root changes which intercomponent covers need paying for. The theorem classifies that constrained setting, including its four-leaf exceptional extremum, and proves separation by one BML formula. The *unweighted total count* of stage relations agrees with the known OEIS sequence A326878 [3]; no claim of numerical-sequence discovery is made.

## Limitations
This is an exact classification of finite one-level stars, not arbitrary scope trees or general growing-world Kripke models. The result does not prove novel transitive-reduction theory for unrestricted directed graphs. The construction allows an arbitrary additional arrow belonging to the target preorder rather than requiring arrows to come from a separate input graph. Older equivalent results expressed as constrained transitive reductions may exist; independent peer review and independent audit have not occurred.

## References
[1] Y. Murase and A. Maniwa, *Bounded Modal Logic*, arXiv:2602.09462 (first posted 2026-02-10); author full-text version, https://www.fos.kuis.kyoto-u.ac.jp/~murase/files/bml-draft.pdf; especially Definition 2.1 and Definition 4.1.

[2] A. V. Aho, M. R. Garey and J. D. Ullman, *The Transitive Reduction of a Directed Graph*, SIAM J. Comput. 1 (1972), 131–137, DOI 10.1137/0201008; Theorem 2. Lawful full-text copy: https://www.cs.tufts.edu/comp/150FP/archive/al-aho/transitive-reduction.pdf.

[3] OEIS A326878, *Number of topologies whose points are a subset of {1,...,n}*, https://oeis.org/A326878 (existing enumerative equivalence).